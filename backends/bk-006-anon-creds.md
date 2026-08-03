# OONI Anonymous Credentials Protocol

- authors: Michele Orrù, Arturo Filastò
- status: draft

OONI probes submit network measurements to a collector. The collector has the ability, without identifying each single probe, to enforce access policies for users. This is done via keyed-verification anonymous credentials (KVAC) [CMZ14, Orr25]. The OONI collector is both issuer and verifier of these credentials. The protocol and its implementation are described in [OTSG26].

At every submission, the probe proves (in zero knowledge) possession of a credential satisfying the collector's submission policy. Submissions by the same probe in the same scope are linkable through the pseudonym. Everything else is unlinkable, including the same user across different countries or networks.

## Protocol overview

```mermaid
sequenceDiagram
    participant User as Probe
    participant Server as OONI Collector

    Note over User, Server: 1. Manifest retrieval
    User->>Server: GET /api/v1/manifest
    Server->>User: manifest (public parameters, submission policy)
    Note over User: pin public parameters

    Note over User, Server: 2. Registration
    Note over User: (req, st) = Reg.prepare(pp)
    User->>Server: POST /api/v1/sign_credential (req)
    Note over Server: age := today (Julian day), count := 0<br/>add server share to nym_id<br/>rep = Reg.handle(sk, req)
    Server->>User: rep
    Note over User: cred = Reg.finalize(st, rep)<br/>store credential

    Note over User, Server: 3. Measurement submission (repeatable)
    Note over User: NYM = nym_id * DOMAIN(probe_cc, probe_asn)<br/>(req, st), probe_id = Sub.prepare(cred, pp, policy)
    User->>Server: POST /api/v1/submit_measurement (content, probe_id, req)
    Note over Server: match policy on (cc, asn)<br/>moderate by probe_id (e.g. blocklist)<br/>verify proof; blind-issue New with count+1<br/>store content + verification status
    Server->>User: rep
    Note over User: cred' = Sub.finalize(st, rep)<br/>replace credential

    Note over User, Server: 4. Credential update (key rotation)
    Note over User: (req, st) = Upd.prepare(cred, pp_new)
    User->>Server: POST /api/v1/update_credential (req)
    Note over Server: rep = Upd.handle(sk_new, sk_old, req)
    Server->>User: rep
    Note over User: cred' = Upd.finalize(st, rep)<br/>replace credential
```

## Credential

| attribute           | contents                     | set by                       | visibility                |
|---------------------|------------------------------|------------------------------|---------------------------|
| `nym_id`            | pseudonym key, scalar        | user&server, at issuance     | never revealed            |
| `age`               | Julian day of issuance (u32) | server, at issuance          | hidden after issuance; range-proved      |
| `measurement_count` | accepted submissions (u32)   | 0 at issuance; +1/submit     | hidden after issuance; range-proved      |


The user stores the attributes `(nym_id, age, measurement_count)` and the KVAC `(P, Q)`. The attributes **MUST** be kept private: leaking `nym_id` links every pseudonym the probe ever produced. The server stores `(sk, pp)`. The server's signing key **MUST** be kept private: leaking `sk` will allow generating arbitrary credentials. Attribute values live in scalars; `age` and `measurement_count` that do not fit in 32 bits **MUST** be rejected (`scalar_u32`). The attribute `age` is the Julian day of issuance; the policy bounds `[age_lo, age_hi]` are Julian days.

The credential is a µCMZ algebraic MAC [Orr25] over ristretto255 [RFC9496]. Protocol messages are bincode-serialized structs (fixed-width little-endian integers; points as 32-byte compressed ristretto, scalars as 32-byte little-endian), carried base64-encoded in JSON string fields over HTTPS. Serialized, the credential together with its attributes is 406 bytes and is stored permanently by the user; the public parameters are 170 bytes.

All zero-knowledge proofs below are sigma protocols for linear relations with bit-decomposition range proofs [SIGMA-PROOFS, FIAT-SHAMIR, OTSG26, CMZ-RS]. They require a cryptographically secure entropy source from the caller.

## HTTP API

| endpoint                          | protocol               |
|-----------------------------------|------------------------|
| `GET  /api/v1/manifest`           | parameter distribution |
| `POST /api/v1/sign_credential`    | registration           |
| `POST /api/v1/submit_measurement` | submission             |
| `POST /api/v1/update_credential`  | key rotation           |

Measured message sizes (bincode encoding, before the 4/3 base64 expansion):

| message      | request | response |
|--------------|---------|----------|
| registration | 141 B   | 237 B    |
| submission   | 2.0–5.2 KB (see below) | 173 B |
| update       | 493 B   | 173 B    |

Registration and update messages are fixed-size, and processed in a few milliseconds on commodity hardware. The submission cost is dominated by the two bit-decomposition range proofs: 1997 bytes for a 31-day age window and measurement count in `[0, 100)`; 5197 bytes when the count upper bound is pinned to `2^32 - 1`.

## Manifest

The manifest has the following shape:

```json
{
  "manifest": {
    "nym_scope": "ooni.org/{probe_cc}/{probe_asn}",
    "public_parameters": "<base64>",
    "submission_policy": [
      { "match":  { "probe_cc": "IT", "probe_asn": "*" },
        "policy": { "age": [lo, hi], "min_measurement_count": n } },
      { "match":  { "probe_cc": "*", "probe_asn": "*" },
        "policy": { "age": [lo, hi], "min_measurement_count": 0 } }
    ]
  },
  "meta": { "version": "...", "last_modification_date": "...",
            "manifest_url": "...", "library_version": "...",
            "protocol_version": "..." }
}
```

The manifest is the trust anchor of the system: anonymity requires all users to share the same view of the public parameters, since a server handing tailored parameters to a targeted user can link that user's submissions.

To do so, the manifest exists in a versioned public S3 bucket, so that keys used by the server are versioned. The manifest **SHOULD** be made available publicly, and be accessible to all users, including VPNs or privacy-preserving network layers. It is **RECOMMENDED** that the users access the manifest via an anonymity network. Policy entries are matched by first-match rule. The last entry **MUST** be `*/*`. `meta.version` is the version ID of the manifest.

The policy will partition the anonymity set. Each valid submission will reveal that the user has a certain age and measurement count matching the policy. The user authentication system is **pseudonymous**, and the same identity is leaked across the same scope (country and network). Transport metadata (IP address, TLS session reuse, timing) is not covered by the anonymous credential system.

## Registration

During registration, the server may apply a sequence of checks on the client requesting a credential. These are outside the anonymous credential system, and may include CAPTCHAs, logins, or other forms of identification. These will not de-anonymize the user during submission. The registration flow is as follows:

```
User                                              Server
----                                              ------
pin pp from manifest
req, st <- Reg.prepare(pp, session_id)
        --- POST /api/v1/sign_credential ------------>
            { manifest_version, credential_sign_request: req }
                                                  404 if manifest_version stale
                                                  rep <- Reg.handle(sk, session_id, req):
                                                    age   := today
                                                    count := 0
                                                    add server share to nym_id
        <-- { credential_sign_response: rep, emission_day } ---
cred <- Reg.finalize(st, rep):
  verify issuance proof under pp
  check |age - today| <= 1, count = 0
store cred
```

The proof session identifier is the constant `"ooni.org/userauth/v1/reg"`. The attributes of the issued credential are:

- `age` is set by the server and checked by the user. The `age` must correspond to the client's own UTC day, and this **MUST** be checked before storing the credential, within a one-day clock-skew tolerance.
- `measurement_count` is implicit, and set to zero by both the user and the server.
- `nym_id` is jointly generated adding shares (random nonces) from both server and user. Being jointly generated, user identifiers will not collide as long as either of them is honest.

Throttling registration is possible via CAPTCHAs and IP limits. Tracking IPs at issuance will not compromise anonymity of the probe during submission. These additional measures are not part of the core credential library.


## Measurement submission

The submission protocol presents the credential revealing a pseudonym, and re-issues a new credential for the same `nym_id` and an updated measurement count.

```
User                                              Server
----                                              ------
(req, st), probe_id <- Sub.prepare(cred, pp, session_id,
                         DOMAIN, NYM, policy ranges)
        --- POST /api/v1/submit_measurement -------->
            { format, content, nym: b64(probe_id),
              zkp_request: b64(req || NYM),
              manifest_version, protocol_version }
                                                  validate cc/asn
                                                  validate version (manifest, min protocol)
                                                  policy <- first match on (cc, asn)
                                                  compute mh, session_id from content
                                                  check probe identifier matches NYM
                                                  verify proof; blind-issue New
                                                  strip nym, zkp_request; store
                                                  content + is_verified ∈ {t,f,u}
        <-- { measurement_uid, report_id, verification_status,
              submit_response, protocol_version, error } ---
cred' <- Sub.finalize(st, submit_response):
  verify issuance proof under pinned pp
replace stored credential with cred'
```

The presentation data depends on the following variables:

```
scope      = "ooni.org/" || probe_cc || "/" || probe_asn
DOMAIN     = hash_to_group(SHA-512, scope)        # per-scope generator
NYM        = nym_id * DOMAIN                      # algebraic PRF at (probe_cc, probe_asn)
probe_id   = SHA-256("ooni.org/userauth/v1/pid" || compress(NYM))
mh         = SHA-256(content)                     # measurement body bytes, fixed length
session_id = SHA-256("ooni.org/v1/sid" || mh)
```

`probe_cc` is the two-letter uppercase ASCII country identifier, and `probe_asn` is `"AS"` followed by the decimal ASN without leading zeros (total length 3–12). Country and ASN **MUST** be unique and validated *before* invoking the measurement submission, else two different pseudonyms for the same network can be created. Country and ASN **MUST** be read from the user submission.

The probe identifier `probe_id` is deterministic per-scope (country and ASN). The probe identifier **MAY** be permanently stored and used in the application layer in the future. The probe identifier **SHOULD** be used to moderate access and ban denial-of-service attempts; for instance, the server **MAY** maintain a blocklist of banned probe identifiers and refuse the submission before verifying the proof. The variable `DOMAIN` **MAY** be cached for efficiency. `NYM` **SHOULD NOT** be stored permanently, else stored data will contain group elements usable for offline Diffie-Hellman tests.

The measurement hash `mh` **MUST** uniquely identify the user's submission. In particular, it **MUST** include the payload stored by the server and a timestamp, to prevent proofs from being replayed over different measurements without having a valid credential. Repeated requests with the same measurement hash **MUST** be rejected at the application layer, since this is not handled by the credential library. A failed credential submission (for instance, due to network issues) **MAY** be sent again, provided the caller runs `Sub.prepare` again.

The submission protocol reveals:

```
age_lo   <= age               <= age_hi         (range proof)
count_lo <= measurement_count <= 2^32 - 2       (range proof)
```

with `(age_lo, age_hi, count_lo)` taken from the manifest policy entry matching the scope. All three values **MUST** fit in 32 bits. Additionally, it issues a new credential `New` such that:
```
New.nym_id            = Old.nym_id
New.age               = Old.age
New.measurement_count = Old.measurement_count + 1
```

where `Old` is the old credential.

Clients **MUST** make sure that the public parameters `pp` are the latest available in the manifest, else the server will learn the last manifest version used by the user. Timing of manifest requests and presentation, if not properly handled, will correlate the user requests. Clients **SHOULD** use the new credential and safely delete the previous one, otherwise their measurement count will not increase.

The credential system, by itself, does not enforce that the data in the submission is correct. In particular, the server **MAY** accept a timestamp mismatch with the measurement data, or invalid measurement data. The credential does not authenticate the data carried in the measurement, only properties about the user submitting the measurement.

A measurement not accompanied by a credential should be considered `unverified`. A measurement accompanied by an out-of-date credential should be considered `unverified`. An invalid credential with up-to-date version should be considered `failed verification`. Otherwise, a measurement is `valid`.

## Credential update

The credential is re-issued with the same attributes, but under a new signing key. All attributes are kept hidden and, in particular, `nym_id` is the same. Old credentials are valid under `(sk_old, pp_old)`, `New` issued under `(sk_new, pp_new)`.

```
User                                              Server
----                                              ------
fetch new manifest; pin pp_new
req, st <- Upd.prepare(cred, pp_new, session_id)
        --- POST /api/v1/update_credential --------->
            { old_manifest_version, manifest_version, update_request: req }
                                                  rep <- Upd.handle(sk_new, sk_old, session_id, req)
        <-- { update_response: rep } ---
cred' <- Upd.finalize(st, rep); replace credential
```

The proof session identifier is the constant `"ooni.org/userauth/v1/upd"`. The user proves in zero knowledge that the hidden attributes of the new credential request equal those of a valid credential under the old key.

This endpoint supports rotation of the server signing key, both scheduled and after compromise. Forcing users through an update step partitions the anonymity set between old and new keys, and temporarily gates access to the submission server. Additional checks and filters for users requesting a credential **MAY** be applied at this stage. For instance, it is possible to re-issue credentials only for users with a given measurement count, or for users that solve some human challenge.

## Security considerations

The pseudonym is the algebraic PRF `NYM = nym_id * hash_to_group(scope)` (Naor–Pinkas–Reingold style [NPR99]) over ristretto255, whose pseudorandomness reduces to DDH: roughly 128-bit classical security, and no post-quantum security. The `probe_id` exists to mitigate this risk for data at rest.

No double-spend detection is performed within the credential library. However, users using the same credentials will be subject to the same access policy and, in particular, the same pseudonyms across networks. Applications may block suspicious pseudonyms from submitting further measurements. The update protocol proves that `nym_id` is preserved, so neither re-issuance path can be used to fork a credential into two distinct pseudonymous identities.
A malicious issuer can try to tag a credential through the attributes it controls; see the client-side checks in Registration. It can also serve different public parameters to different users, breaking unlinkability; see Manifest.

## References

- [CMZ14] Chase, Meiklejohn, Zaverucha. *Algebraic MACs and Keyed-Verification Anonymous Credentials.* CCS 2014.
  <https://eprint.iacr.org/2013/516>
- [Orr25] Orrù. *Revisiting Keyed-Verification Anonymous Credentials.* CCS 2025.
  <https://eprint.iacr.org/2024/1552>
- [OTSG26] Orrù, Tulloch, Snyder-Graf, Goldberg. *sigma-rs: A Modular Approach
  for Keyed-Verification Anonymous Credentials.*
  <https://eprint.iacr.org/2026/794>
- [CMZ-RS] Goldberg. *`cmz` crate*, v0.2. <https://crates.io/crates/cmz>
- [SIGMA-PROOFS] draft-irtf-cfrg-sigma-protocols.
  <https://datatracker.ietf.org/doc/draft-irtf-cfrg-sigma-protocols/>
- [FIAT-SHAMIR] draft-irtf-cfrg-fiat-shamir.
  <https://datatracker.ietf.org/doc/draft-irtf-cfrg-fiat-shamir/>
- [RFC9496] ristretto255 and decaf448 groups.
  <https://www.rfc-editor.org/rfc/rfc9496>
- [NPR99] Naor, Pinkas, Reingold. *Distributed Pseudo-random Functions and KDCs.* EUROCRYPT 1999.
- [DY05] Dodis, Yampolskiy. *A Verifiable Random Function with Short Proofs and Keys.* PKC 2005.
- Backend integration: `ooni/backend`, service `ooniapi/services/ooniprobe`,
  router `routers/v1/probe_services.py`. <https://github.com/ooni/backend>

# Specification version number

2023-12-01-001

-   _status_: current

# Specification name

Signal

# Test preconditions

-   An internet connection

# Expected impact

Ability to detect if the Signal instant messaging platform, by checking if it's
possible to establish a TLS connection and send a GET request to the signal
server backends.

# Expected inputs

None

# Test description

This test will check if it's possible to connect to the [signal
server](https://github.com/signalapp/Signal-Server) backend and perform a HTTP
GET request.

The endpoints used for testing are the following:

-   https://cdsi.signal.org/
-   https://chat.signal.org/
-   https://sfu.voip.signal.org/
-   https://storage.signal.org/

The TLS certificate is validated against these custom Signal CA root certificates:

```
-----BEGIN CERTIFICATE-----
MIID7zCCAtegAwIBAgIJAIm6LatK5PNiMA0GCSqGSIb3DQEBBQUAMIGNMQswCQYD
VQQGEwJVUzETMBEGA1UECAwKQ2FsaWZvcm5pYTEWMBQGA1UEBwwNU2FuIEZyYW5j
aXNjbzEdMBsGA1UECgwUT3BlbiBXaGlzcGVyIFN5c3RlbXMxHTAbBgNVBAsMFE9w
ZW4gV2hpc3BlciBTeXN0ZW1zMRMwEQYDVQQDDApUZXh0U2VjdXJlMB4XDTEzMDMy
NTIyMTgzNVoXDTIzMDMyMzIyMTgzNVowgY0xCzAJBgNVBAYTAlVTMRMwEQYDVQQI
DApDYWxpZm9ybmlhMRYwFAYDVQQHDA1TYW4gRnJhbmNpc2NvMR0wGwYDVQQKDBRP
cGVuIFdoaXNwZXIgU3lzdGVtczEdMBsGA1UECwwUT3BlbiBXaGlzcGVyIFN5c3Rl
bXMxEzARBgNVBAMMClRleHRTZWN1cmUwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAw
ggEKAoIBAQDBSWBpOCBDF0i4q2d4jAXkSXUGpbeWugVPQCjaL6qD9QDOxeW1afvf
Po863i6Crq1KDxHpB36EwzVcjwLkFTIMeo7t9s1FQolAt3mErV2U0vie6Ves+yj6
grSfxwIDAcdsKmI0a1SQCZlr3Q1tcHAkAKFRxYNawADyps5B+Zmqcgf653TXS5/0
IPPQLocLn8GWLwOYNnYfBvILKDMItmZTtEbucdigxEA9mfIvvHADEbteLtVgwBm9
R5vVvtwrD6CCxI3pgH7EH7kMP0Od93wLisvn1yhHY7FuYlrkYqdkMvWUrKoASVw4
jb69vaeJCUdU+HCoXOSP1PQcL6WenNCHAgMBAAGjUDBOMB0GA1UdDgQWBBQBixjx
P/s5GURuhYa+lGUypzI8kDAfBgNVHSMEGDAWgBQBixjxP/s5GURuhYa+lGUypzI8
kDAMBgNVHRMEBTADAQH/MA0GCSqGSIb3DQEBBQUAA4IBAQB+Hr4hC56m0LvJAu1R
K6NuPDbTMEN7/jMojFHxH4P3XPFfupjR+bkDq0pPOU6JjIxnrD1XD/EVmTTaTVY5
iOheyv7UzJOefb2pLOc9qsuvI4fnaESh9bhzln+LXxtCrRPGhkxA1IMIo3J/s2WF
/KVYZyciu6b4ubJ91XPAuBNZwImug7/srWvbpk0hq6A6z140WTVSKtJG7EP41kJe
/oF4usY5J7LPkxK3LWzMJnb5EIJDmRvyH8pyRwWg6Qm6qiGFaI4nL8QU4La1x2en
4DGXRaLMPRwjELNgQPodR38zoCMuA8gHZfZYYoZ7D7Q1wNUiVHcxuFrEeBaYJbLE
rwLV
-----END CERTIFICATE-----
```

and

```
-----BEGIN CERTIFICATE-----
MIIF2zCCA8OgAwIBAgIUAMHz4g60cIDBpPr1gyZ/JDaaPpcwDQYJKoZIhvcNAQEL
BQAwdTELMAkGA1UEBhMCVVMxEzARBgNVBAgTCkNhbGlmb3JuaWExFjAUBgNVBAcT
DU1vdW50YWluIFZpZXcxHjAcBgNVBAoTFVNpZ25hbCBNZXNzZW5nZXIsIExMQzEZ
MBcGA1UEAxMQU2lnbmFsIE1lc3NlbmdlcjAeFw0yMjAxMjYwMDQ1NTFaFw0zMjAx
MjQwMDQ1NTBaMHUxCzAJBgNVBAYTAlVTMRMwEQYDVQQIEwpDYWxpZm9ybmlhMRYw
FAYDVQQHEw1Nb3VudGFpbiBWaWV3MR4wHAYDVQQKExVTaWduYWwgTWVzc2VuZ2Vy
LCBMTEMxGTAXBgNVBAMTEFNpZ25hbCBNZXNzZW5nZXIwggIiMA0GCSqGSIb3DQEB
AQUAA4ICDwAwggIKAoICAQDEecifxMHHlDhxbERVdErOhGsLO08PUdNkATjZ1kT5
1uPf5JPiRbus9F4J/GgBQ4ANSAjIDZuFY0WOvG/i0qvxthpW70ocp8IjkiWTNiA8
1zQNQdCiWbGDU4B1sLi2o4JgJMweSkQFiyDynqWgHpw+KmvytCzRWnvrrptIfE4G
PxNOsAtXFbVH++8JO42IaKRVlbfpe/lUHbjiYmIpQroZPGPY4Oql8KM3o39ObPnT
o1WoM4moyOOZpU3lV1awftvWBx1sbTBL02sQWfHRxgNVF+Pj0fdDMMFdFJobArrL
VfK2Ua+dYN4pV5XIxzVarSRW73CXqQ+2qloPW/ynpa3gRtYeGWV4jl7eD0PmeHpK
OY78idP4H1jfAv0TAVeKpuB5ZFZ2szcySxrQa8d7FIf0kNJe9gIRjbQ+XrvnN+ZZ
vj6d+8uBJq8LfQaFhlVfI0/aIdggScapR7w8oLpvdflUWqcTLeXVNLVrg15cEDwd
lV8PVscT/KT0bfNzKI80qBq8LyRmauAqP0CDjayYGb2UAabnhefgmRY6aBE5mXxd
byAEzzCS3vDxjeTD8v8nbDq+SD6lJi0i7jgwEfNDhe9XK50baK15Udc8Cr/ZlhGM
jNmWqBd0jIpaZm1rzWA0k4VwXtDwpBXSz8oBFshiXs3FD6jHY2IhOR3ppbyd4qRU
pwIDAQABo2MwYTAOBgNVHQ8BAf8EBAMCAQYwDwYDVR0TAQH/BAUwAwEB/zAdBgNV
HQ4EFgQUtfNLxuXWS9DlgGuMUMNnW7yx83EwHwYDVR0jBBgwFoAUtfNLxuXWS9Dl
gGuMUMNnW7yx83EwDQYJKoZIhvcNAQELBQADggIBABUeiryS0qjykBN75aoHO9bV
PrrX+DSJIB9V2YzkFVyh/io65QJMG8naWVGOSpVRwUwhZVKh3JVp/miPgzTGAo7z
hrDIoXc+ih7orAMb19qol/2Ha8OZLa75LojJNRbZoCR5C+gM8C+spMLjFf9k3JVx
dajhtRUcR0zYhwsBS7qZ5Me0d6gRXD0ZiSbadMMxSw6KfKk3ePmPb9gX+MRTS63c
8mLzVYB/3fe/bkpq4RUwzUHvoZf+SUD7NzSQRQQMfvAHlxk11TVNxScYPtxXDyiy
3Cssl9gWrrWqQ/omuHipoH62J7h8KAYbr6oEIq+Czuenc3eCIBGBBfvCpuFOgckA
XXE4MlBasEU0MO66GrTCgMt9bAmSw3TrRP12+ZUFxYNtqWluRU8JWQ4FCCPcz9pg
MRBOgn4lTxDZG+I47OKNuSRjFEP94cdgxd3H/5BK7WHUz1tAGQ4BgepSXgmjzifF
T5FVTDTl3ZnWUVBXiHYtbOBgLiSIkbqGMCLtrBtFIeQ7RRTb3L+IE9R0UB0cJB3A
Xbf1lVkOcmrdu2h8A32aCwtr5S1fBF1unlG7imPmqJfpOMWa8yIF/KWVm29JAPq8
Lrsybb0z5gg8w7ZblEuB9zOW9M3l60DXuJO6l7g+deV6P96rv2unHS8UlvWiVWDy
9qfgAJizyy3kqM4lOwBH
-----END CERTIFICATE-----
```

If the connection to any of the signal server endpoints fails, we write

```json
{
    "signal_backend_failure": "FAILURE STRING",
    "signal_backend_status": "blocked"
}
```

If none of the signal server endpoints are blocked then we write:

```json
{
    "signal_backend_failure": null,
    "signal_backend_status": "ok"
}
```

We also perform a DNS query to uptime.signal.org, which is used to inform us if
the signal backend services should be down. The test logic ignores the result of
this DNS query.

# Expected output

## Parent data format

-   `df-001-httpt`
-   `df-002-dnst`
-   `df-005-tcpconnect`
-   `df-006-tlshandshake`

## Semantics

```
{
    "signal_backend_failure": "failure_string" | null,
    "signal_backend_status": "blocked" | "ok" | null,
}
```

The meaning of the various keys is described in the above section.

## Possible conclusions

If it is possible for users to use the Signal messenger software

## Data analysis considerations

All data collected with `test_version <= 0.2.1` after 2022-10-19 should be
treated with extra care, as the values of `signal_backend_failure` and
`signal_backend_status` cannot be trusted.`
This is a result of signal having changed the root CA for at least one of their
endpoints (`sfu.voip.signal.org`) resulting in TLS validation errors.

For more information see: https://github.com/ooni/probe/issues/2344

Data collected with `test_version <= 0.2.3` after 2023-11-07 will contain false
positives, since signal has dropped one their legacy endpoints.

For more information see: https://github.com/ooni/probe/issues/2627

## Example output sample

```JSON
{
  "annotations": {
    "architecture": "arm64",
    "engine_name": "ooniprobe-engine",
    "engine_version": "3.20.0-alpha",
    "go_version": "go1.20.11",
    "platform": "macos",
    "vcs_modified": "true",
    "vcs_revision": "b4d03b59d8f98d9734594f5fd07559d1458b2577",
    "vcs_time": "2023-12-01T00:52:15Z",
    "vcs_tool": "git"
  },
  "data_format_version": "0.2.0",
  "extensions": {
    "dnst": 0,
    "httpt": 0,
    "netevents": 0,
    "tcpconnect": 0,
    "tlshandshake": 0,
    "tunnel": 0
  },
  "input": null,
  "measurement_start_time": "2023-12-01 10:24:59",
  "probe_asn": "AS30722",
  "probe_cc": "IT",
  "probe_ip": "127.0.0.1",
  "probe_network_name": "Vodafone Italia S.p.A.",
  "report_id": "20231201T102459Z_signal_IT_30722_n1_TRwjDbqHNDLIskk7",
  "resolver_asn": "AS30722",
  "resolver_ip": "91.80.36.88",
  "resolver_network_name": "Vodafone Italia S.p.A.",
  "software_name": "miniooni",
  "software_version": "3.20.0-alpha",
  "test_keys": {
    "agent": "redirect",
    "failed_operation": null,
    "failure": null,
    "network_events": [
      {
        "failure": null,
        "operation": "http_transaction_start",
        "t": 0.000576708
      },
      {
        "failure": null,
        "operation": "resolve_start",
        "t": 0.000657333
      },
      {
        "failure": null,
        "operation": "resolve_done",
        "t": 0.022948125
      },
      {
        "address": "35.186.192.249:443",
        "failure": null,
        "operation": "connect",
        "proto": "tcp",
        "t": 0.039867916
      },
      {
        "failure": null,
        "operation": "tls_handshake_start",
        "t": 0.039884791
      },
      {
        "failure": null,
        "num_bytes": 285,
        "operation": "write",
        "t": 0.040325291
      },
      {
        "failure": null,
        "num_bytes": 576,
        "operation": "read",
        "t": 0.059093333
      },
      {
        "failure": null,
        "num_bytes": 2583,
        "operation": "read",
        "t": 0.059355291
      },
      {
        "failure": null,
        "num_bytes": 64,
        "operation": "write",
        "t": 0.065680583
      },
      {
        "failure": null,
        "operation": "tls_handshake_done",
        "t": 0.065709583
      },
      {
        "failure": null,
        "num_bytes": 86,
        "operation": "write",
        "t": 0.065776875
      },
      {
        "failure": null,
        "num_bytes": 200,
        "operation": "write",
        "t": 0.065868875
      },
      {
        "failure": null,
        "num_bytes": 93,
        "operation": "read",
        "t": 0.083310291
      },
      {
        "failure": null,
        "num_bytes": 31,
        "operation": "write",
        "t": 0.083422208
      },
      {
        "failure": null,
        "num_bytes": 134,
        "operation": "read",
        "t": 0.100395625
      },
      {
        "failure": null,
        "num_bytes": 39,
        "operation": "write",
        "t": 0.10055125
      },
      {
        "failure": null,
        "operation": "http_transaction_done",
        "t": 0.100626708
      },
      {
        "failure": null,
        "num_bytes": 24,
        "operation": "write",
        "t": 0.100830666
      },
      {
        "failure": "connection_already_closed",
        "operation": "read",
        "t": 0.100927916
      },
      {
        "failure": null,
        "operation": "http_transaction_start",
        "t": 0.104003458
      },
      {
        "failure": null,
        "operation": "resolve_start",
        "t": 0.1040835
      },
      {
        "failure": null,
        "operation": "resolve_done",
        "t": 0.129525291
      },
      {
        "address": "142.251.209.19:443",
        "failure": null,
        "operation": "connect",
        "proto": "tcp",
        "t": 0.146504125
      },
      {
        "failure": null,
        "operation": "tls_handshake_start",
        "t": 0.146513041
      },
      {
        "failure": null,
        "num_bytes": 284,
        "operation": "write",
        "t": 0.146776416
      },
      {
        "failure": null,
        "num_bytes": 576,
        "operation": "read",
        "t": 0.184033375
      },
      {
        "failure": null,
        "num_bytes": 2583,
        "operation": "read",
        "t": 0.18443875
      },
      {
        "failure": null,
        "num_bytes": 64,
        "operation": "write",
        "t": 0.191190083
      },
      {
        "failure": null,
        "operation": "tls_handshake_done",
        "t": 0.191272375
      },
      {
        "failure": null,
        "num_bytes": 86,
        "operation": "write",
        "t": 0.191347041
      },
      {
        "failure": null,
        "num_bytes": 199,
        "operation": "write",
        "t": 0.191451958
      },
      {
        "failure": null,
        "num_bytes": 62,
        "operation": "read",
        "t": 0.222293958
      },
      {
        "failure": null,
        "num_bytes": 31,
        "operation": "write",
        "t": 0.222354958
      },
      {
        "failure": null,
        "num_bytes": 31,
        "operation": "read",
        "t": 0.227344166
      },
      {
        "failure": null,
        "num_bytes": 240,
        "operation": "read",
        "t": 0.314269291
      },
      {
        "failure": null,
        "num_bytes": 39,
        "operation": "write",
        "t": 0.3143645
      },
      {
        "failure": null,
        "operation": "http_transaction_done",
        "t": 0.314396541
      },
      {
        "failure": null,
        "num_bytes": 24,
        "operation": "write",
        "t": 0.314487791
      },
      {
        "failure": "connection_already_closed",
        "operation": "read",
        "t": 0.314551791
      },
      {
        "failure": null,
        "operation": "resolve_start",
        "t": 0.317448083
      },
      {
        "failure": null,
        "operation": "resolve_done",
        "t": 0.347637375
      },
      {
        "failure": null,
        "operation": "http_transaction_start",
        "t": 0.000597458
      },
      {
        "failure": null,
        "operation": "resolve_start",
        "t": 0.000657666
      },
      {
        "failure": null,
        "operation": "resolve_done",
        "t": 0.023001916
      },
      {
        "address": "40.122.45.194:443",
        "failure": null,
        "operation": "connect",
        "proto": "tcp",
        "t": 0.174280458
      },
      {
        "failure": null,
        "operation": "tls_handshake_start",
        "t": 0.174306583
      },
      {
        "failure": null,
        "num_bytes": 281,
        "operation": "write",
        "t": 0.17473575
      },
      {
        "failure": null,
        "num_bytes": 576,
        "operation": "read",
        "t": 0.326950458
      },
      {
        "failure": null,
        "num_bytes": 3177,
        "operation": "read",
        "t": 0.32717075
      },
      {
        "failure": null,
        "num_bytes": 80,
        "operation": "write",
        "t": 0.333873625
      },
      {
        "failure": null,
        "operation": "tls_handshake_done",
        "t": 0.333897875
      },
      {
        "failure": null,
        "num_bytes": 86,
        "operation": "write",
        "t": 0.333955291
      },
      {
        "failure": null,
        "num_bytes": 197,
        "operation": "write",
        "t": 0.334039958
      },
      {
        "failure": null,
        "num_bytes": 933,
        "operation": "read",
        "t": 0.482234875
      },
      {
        "failure": null,
        "num_bytes": 31,
        "operation": "write",
        "t": 0.482318416
      },
      {
        "failure": null,
        "operation": "http_transaction_done",
        "t": 0.482728958
      },
      {
        "failure": null,
        "num_bytes": 24,
        "operation": "write",
        "t": 0.482853833
      },
      {
        "failure": "connection_already_closed",
        "operation": "read",
        "t": 0.482953208
      },
      {
        "failure": null,
        "operation": "http_transaction_start",
        "t": 0.000588458
      },
      {
        "failure": null,
        "operation": "resolve_start",
        "t": 0.000672916
      },
      {
        "failure": null,
        "operation": "resolve_done",
        "t": 0.024907458
      },
      {
        "address": "13.248.212.111:443",
        "failure": null,
        "operation": "connect",
        "proto": "tcp",
        "t": 0.051451208
      },
      {
        "failure": null,
        "operation": "tls_handshake_start",
        "t": 0.051475833
      },
      {
        "failure": null,
        "num_bytes": 281,
        "operation": "write",
        "t": 0.05185825
      },
      {
        "failure": null,
        "num_bytes": 576,
        "operation": "read",
        "t": 0.304952458
      },
      {
        "failure": null,
        "num_bytes": 3073,
        "operation": "read",
        "t": 0.3050445
      },
      {
        "failure": null,
        "num_bytes": 126,
        "operation": "write",
        "t": 0.314246708
      },
      {
        "failure": null,
        "num_bytes": 120,
        "operation": "read",
        "t": 0.450914875
      },
      {
        "failure": null,
        "operation": "tls_handshake_done",
        "t": 0.451029208
      },
      {
        "failure": null,
        "num_bytes": 93,
        "operation": "write",
        "t": 0.451205291
      },
      {
        "failure": null,
        "num_bytes": 204,
        "operation": "write",
        "t": 0.451414583
      },
      {
        "failure": null,
        "num_bytes": 38,
        "operation": "write",
        "t": 0.451478666
      },
      {
        "failure": null,
        "num_bytes": 246,
        "operation": "read",
        "t": 0.588587541
      },
      {
        "failure": null,
        "operation": "http_transaction_done",
        "t": 0.588948708
      },
      {
        "failure": null,
        "num_bytes": 31,
        "operation": "write",
        "t": 0.58910275
      },
      {
        "failure": "connection_already_closed",
        "operation": "read",
        "t": 0.589209458
      }
    ],
    "queries": [
      {
        "answers": [
          {
            "asn": 15169,
            "as_org_name": "Google LLC",
            "answer_type": "A",
            "ipv4": "35.186.192.249",
            "ttl": null
          }
        ],
        "engine": "system",
        "failure": null,
        "hostname": "sfu.voip.signal.org",
        "query_type": "A",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "",
        "t": 0.022948125,
        "tags": null
      },
      {
        "answers": [
          {
            "asn": 396982,
            "as_org_name": "Google LLC",
            "answer_type": "AAAA",
            "ipv6": "2600:1901:0:217a::",
            "ttl": null
          }
        ],
        "engine": "system",
        "failure": null,
        "hostname": "sfu.voip.signal.org",
        "query_type": "AAAA",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "",
        "t": 0.022948125,
        "tags": null
      },
      {
        "answers": [
          {
            "asn": 15169,
            "as_org_name": "Google LLC",
            "answer_type": "A",
            "ipv4": "142.251.209.19",
            "ttl": null
          }
        ],
        "engine": "system",
        "failure": null,
        "hostname": "storage.signal.org",
        "query_type": "A",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "",
        "t": 0.129525291,
        "tags": null
      },
      {
        "answers": [
          {
            "asn": 15169,
            "as_org_name": "Google LLC",
            "answer_type": "AAAA",
            "ipv6": "2a00:1450:4002:410::2013",
            "ttl": null
          }
        ],
        "engine": "system",
        "failure": null,
        "hostname": "storage.signal.org",
        "query_type": "AAAA",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "",
        "t": 0.129525291,
        "tags": null
      },
      {
        "answers": [
          {
            "answer_type": "A",
            "ipv4": "127.0.0.1",
            "ttl": null
          }
        ],
        "engine": "system",
        "failure": null,
        "hostname": "uptime.signal.org",
        "query_type": "A",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "",
        "t": 0.347637375,
        "tags": null
      },
      {
        "answers": [
          {
            "asn": 8075,
            "as_org_name": "Microsoft Corporation",
            "answer_type": "A",
            "ipv4": "40.122.45.194",
            "ttl": null
          }
        ],
        "engine": "system",
        "failure": null,
        "hostname": "cdsi.signal.org",
        "query_type": "A",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "",
        "t": 0.023001916,
        "tags": null
      },
      {
        "answers": [
          {
            "asn": 8075,
            "as_org_name": "Microsoft Corporation",
            "answer_type": "AAAA",
            "ipv6": "2603:1030:7::1",
            "ttl": null
          }
        ],
        "engine": "system",
        "failure": null,
        "hostname": "cdsi.signal.org",
        "query_type": "AAAA",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "",
        "t": 0.023001916,
        "tags": null
      },
      {
        "answers": [
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "13.248.212.111",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "76.223.92.165",
            "ttl": null
          }
        ],
        "engine": "system",
        "failure": null,
        "hostname": "chat.signal.org",
        "query_type": "A",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "",
        "t": 0.024907458,
        "tags": null
      },
      {
        "answers": [
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "AAAA",
            "ipv6": "2600:9000:a507:ab6d:4ce3:2f58:25d7:9cbf",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "AAAA",
            "ipv6": "2600:9000:a61f:527c:d5eb:a431:5239:3232",
            "ttl": null
          }
        ],
        "engine": "system",
        "failure": null,
        "hostname": "chat.signal.org",
        "query_type": "AAAA",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "",
        "t": 0.024907458,
        "tags": null
      }
    ],
    "requests": [
      {
        "failure": null,
        "request": {
          "body": "",
          "body_is_truncated": false,
          "headers_list": [
            [
              "Accept",
              "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
            ],
            [
              "Accept-Language",
              "en-US,en;q=0.9"
            ],
            [
              "Host",
              "sfu.voip.signal.org"
            ],
            [
              "User-Agent",
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/[scrubbed] Safari/537.36"
            ]
          ],
          "headers": {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
            "Host": "sfu.voip.signal.org",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/[scrubbed] Safari/537.36"
          },
          "method": "GET",
          "tor": {
            "exit_ip": null,
            "exit_name": null,
            "is_tor": false
          },
          "x_transport": "tcp",
          "url": "https://sfu.voip.signal.org/"
        },
        "response": {
          "body": "",
          "body_is_truncated": false,
          "code": 503,
          "headers_list": [
            [
              "Alt-Svc",
              "h3=\":443\"; ma=2592000,h3-29=\":443\"; ma=2592000"
            ],
            [
              "Content-Length",
              "0"
            ],
            [
              "Date",
              "Fri, 01 Dec 2023 10:24:58 GMT"
            ],
            [
              "Via",
              "1.1 google"
            ]
          ],
          "headers": {
            "Alt-Svc": "h3=\":443\"; ma=2592000,h3-29=\":443\"; ma=2592000",
            "Content-Length": "0",
            "Date": "Fri, 01 Dec 2023 10:24:58 GMT",
            "Via": "1.1 google"
          }
        },
        "t": 0.100626708,
        "tags": null
      },
      {
        "failure": null,
        "request": {
          "body": "",
          "body_is_truncated": false,
          "headers_list": [
            [
              "Accept",
              "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
            ],
            [
              "Accept-Language",
              "en-US,en;q=0.9"
            ],
            [
              "Host",
              "storage.signal.org"
            ],
            [
              "User-Agent",
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/[scrubbed] Safari/537.36"
            ]
          ],
          "headers": {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
            "Host": "storage.signal.org",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/[scrubbed] Safari/537.36"
          },
          "method": "GET",
          "tor": {
            "exit_ip": null,
            "exit_name": null,
            "is_tor": false
          },
          "x_transport": "tcp",
          "url": "https://storage.signal.org/"
        },
        "response": {
          "body": "{\"code\":404,\"message\":\"HTTP 404 Not Found\"}",
          "body_is_truncated": false,
          "code": 404,
          "headers_list": [
            [
              "Content-Length",
              "43"
            ],
            [
              "Content-Type",
              "application/json"
            ],
            [
              "Date",
              "Fri, 01 Dec 2023 10:24:59 GMT"
            ],
            [
              "Vary",
              "Accept-Encoding"
            ],
            [
              "Via",
              "1.1 google"
            ]
          ],
          "headers": {
            "Content-Length": "43",
            "Content-Type": "application/json",
            "Date": "Fri, 01 Dec 2023 10:24:59 GMT",
            "Vary": "Accept-Encoding",
            "Via": "1.1 google"
          }
        },
        "t": 0.314396541,
        "tags": null
      },
      {
        "failure": null,
        "request": {
          "body": "",
          "body_is_truncated": false,
          "headers_list": [
            [
              "Accept",
              "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
            ],
            [
              "Accept-Language",
              "en-US,en;q=0.9"
            ],
            [
              "Host",
              "cdsi.signal.org"
            ],
            [
              "User-Agent",
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/[scrubbed] Safari/537.36"
            ]
          ],
          "headers": {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
            "Host": "cdsi.signal.org",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/[scrubbed] Safari/537.36"
          },
          "method": "GET",
          "tor": {
            "exit_ip": null,
            "exit_name": null,
            "is_tor": false
          },
          "x_transport": "tcp",
          "url": "https://cdsi.signal.org/"
        },
        "response": {
          "body": "<html>\r\n<head><title>404 Not Found</title></head>\r\n<body>\r\n<center><h1>404 Not Found</h1></center>\r\n<hr><center>nginx</center>\r\n</body>\r\n</html>\r\n<!-- a padding to disable MSIE and Chrome friendly error page -->\r\n<!-- a padding to disable MSIE and Chrome friendly error page -->\r\n<!-- a padding to disable MSIE and Chrome friendly error page -->\r\n<!-- a padding to disable MSIE and Chrome friendly error page -->\r\n<!-- a padding to disable MSIE and Chrome friendly error page -->\r\n<!-- a padding to disable MSIE and Chrome friendly error page -->\r\n",
          "body_is_truncated": false,
          "code": 404,
          "headers_list": [
            [
              "Content-Length",
              "548"
            ],
            [
              "Content-Type",
              "text/html"
            ],
            [
              "Date",
              "Fri, 01 Dec 2023 10:24:59 GMT"
            ],
            [
              "Strict-Transport-Security",
              "max-age=15724800; includeSubDomains"
            ]
          ],
          "headers": {
            "Content-Length": "548",
            "Content-Type": "text/html",
            "Date": "Fri, 01 Dec 2023 10:24:59 GMT",
            "Strict-Transport-Security": "max-age=15724800; includeSubDomains"
          }
        },
        "t": 0.482728958,
        "tags": null
      },
      {
        "failure": null,
        "request": {
          "body": "",
          "body_is_truncated": false,
          "headers_list": [
            [
              "Accept",
              "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
            ],
            [
              "Accept-Language",
              "en-US,en;q=0.9"
            ],
            [
              "Host",
              "chat.signal.org"
            ],
            [
              "User-Agent",
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/[scrubbed] Safari/537.36"
            ]
          ],
          "headers": {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
            "Host": "chat.signal.org",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/[scrubbed] Safari/537.36"
          },
          "method": "GET",
          "tor": {
            "exit_ip": null,
            "exit_name": null,
            "is_tor": false
          },
          "x_transport": "tcp",
          "url": "https://chat.signal.org/"
        },
        "response": {
          "body": "{\"code\":404,\"message\":\"HTTP 404 Not Found\"}",
          "body_is_truncated": false,
          "code": 404,
          "headers_list": [
            [
              "Content-Length",
              "43"
            ],
            [
              "Content-Type",
              "application/json"
            ],
            [
              "Date",
              "Fri, 01 Dec 2023 10:24:59 GMT"
            ],
            [
              "Vary",
              "Origin"
            ],
            [
              "X-Signal-Timestamp",
              "1701426299483"
            ]
          ],
          "headers": {
            "Content-Length": "43",
            "Content-Type": "application/json",
            "Date": "Fri, 01 Dec 2023 10:24:59 GMT",
            "Vary": "Origin",
            "X-Signal-Timestamp": "1701426299483"
          }
        },
        "t": 0.588948708,
        "tags": null
      }
    ],
    "tcp_connect": [
      {
        "ip": "35.186.192.249",
        "port": 443,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.039867916,
        "tags": null
      },
      {
        "ip": "142.251.209.19",
        "port": 443,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.146504125,
        "tags": null
      },
      {
        "ip": "40.122.45.194",
        "port": 443,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.174280458,
        "tags": null
      },
      {
        "ip": "13.248.212.111",
        "port": 443,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.051451208,
        "tags": null
      }
    ],
    "tls_handshakes": [
      {
        "network": "",
        "address": "35.186.192.249:443",
        "cipher_suite": "TLS_AES_128_GCM_SHA256",
        "failure": null,
        "negotiated_protocol": "h2",
        "no_tls_verify": false,
        "peer_certificates": [
          {
            "data": "MIIEjDCCAnSgAwIBAgITW4b9u495SmFdlnv6HT1H3nQPNDANBgkqhkiG9w0BAQsFADB1MQswCQYDVQQGEwJVUzETMBEGA1UECBMKQ2FsaWZvcm5pYTEWMBQGA1UEBxMNTW91bnRhaW4gVmlldzEeMBwGA1UEChMVU2lnbmFsIE1lc3NlbmdlciwgTExDMRkwFwYDVQQDExBTaWduYWwgTWVzc2VuZ2VyMB4XDTIzMDgzMTE5NTE1MloXDTI0MTAwMTAxNDAzN1owADCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAKk+bnbTZGIYwHUlYez/psfAEl+NARVqrywQgKD133LACnpIi9qDzeihb1wLvlhgjSzm1+xm7xxAk1A7AYSL1b8Y788R/74iSu0PCzXg+bAeexePPGdVuofJvG6fZm5IZyJ/zuQI2/7yBwIP8dcwuMCFlah4ERK9Fw40FzS2P0b0naIfS8PX4AUc+yum9LfDTI16xpGa5CnISif42KmD88QOrjtlzKKKTVaUbQNx4ZN8pgxkZ2dx5ePxiBwFmq6SNcqsFQO/ReXwu/810QGGOBfnsoJ8VG3g02LzpfYs0ssM07SDaoX2P1OAVQEyLUQkMtkJZWB37c5XfTLri5ksZGkCAwEAAaOBiTCBhjATBgNVHSUEDDAKBggrBgEFBQcDATAMBgNVHRMBAf8EAjAAMB0GA1UdDgQWBBTik/p/NEWGfE8Wy4wAYI0gzMKjxzAfBgNVHSMEGDAWgBS180vG5dZL0OWAa4xQw2dbvLHzcTAhBgNVHREBAf8EFzAVghNzZnUudm9pcC5zaWduYWwub3JnMA0GCSqGSIb3DQEBCwUAA4ICAQBaJzCnLgvGMoWNcWLFEgTkQQspjbMJbK+VJMmxLNBYoJGmttMjPfdmTm41JkVRhHL4284+CWDkSGkwewy6vcUaTBgQOUjgnFG/IduYkHczu2XENAOuGAWFNrd1CFLG/q+NZoe2bZKGlERHNwfJKDn2KjNSeqLCx+v0AEx8ufQAZxshJ4FEiEZs3qkrmPihcj/rM65Kfa9IO+7oM91xEqGYt6hmqDmFjZeC0CTp2r0jWwpIvHsC7qSwiLmkM42S/fHF6gocpwmAupfuK7CAYvgKXzmMyrm/7IsP1pq6AgPP9Fdmtww//KWf9UOxRHheQuUqwUivQHvVMEguOmFh7ICIQGCzk/ai/duWJ0v8JkMrngnvcvQqDrcWRmW8UkCPwMiFooqo815JWDOHGlSsBcUpmcOHo/f7pAJPnQz6QvJuJ3GdwAR78qkPq2pas9h2cdnzrCPFbBkSC2fz921jo2xDtBq2GLxCprNv3+TRtY8tAUfyZjWmgFfbFc0VAOx/vxHBkrQ8pvLkcNITQ8/0A/wKoETMdbdSCwIof5El1BqJG3LkQt0e6DrL85CjC96+yfa0fImZt7c5utJ8CrgXjTTt2gt6i6EDs7wDkZitJJHmS6v+BJkaN23onlE5+74vRvBEzcIuRYlRcxvPCV202QtFb+osv4yA+1EIH66DLGbHUA==",
            "format": "base64"
          },
          {
            "data": "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",
            "format": "base64"
          }
        ],
        "server_name": "sfu.voip.signal.org",
        "t": 0.065709583,
        "tags": null,
        "tls_version": "TLSv1.3"
      },
      {
        "network": "",
        "address": "142.251.209.19:443",
        "cipher_suite": "TLS_AES_128_GCM_SHA256",
        "failure": null,
        "negotiated_protocol": "h2",
        "no_tls_verify": false,
        "peer_certificates": [
          {
            "data": "MIIEjDCCAnSgAwIBAgIUALI2lpq1U2N7tB7L2JhFsmVmlncwDQYJKoZIhvcNAQELBQAwdTELMAkGA1UEBhMCVVMxEzARBgNVBAgTCkNhbGlmb3JuaWExFjAUBgNVBAcTDU1vdW50YWluIFZpZXcxHjAcBgNVBAoTFVNpZ25hbCBNZXNzZW5nZXIsIExMQzEZMBcGA1UEAxMQU2lnbmFsIE1lc3NlbmdlcjAeFw0yMzEwMjcxOTI3NTdaFw0yNDExMjcwMTE2NDJaMAAwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCWT0fBzBO/H/S9NLd3KDy8+75UuKlXYhDAECTq4HDxRl+8IPM0YBlzsqKuufeTdPm9qqwAa82psVmDBpgAyaWnfpqEkE5zmEMVKd/AqaOrVi0HMEJFyUcMPWh8NNDqF1GnrGGzNk1Huhz+EmtFBUUb7Wrhw/3laxTQPjLVmiR+xGsJd/MXcTfbAeamYRcOwcH/vATDy51iQr1a6+Jv6T0hdBHnLi3Sjr54Cx9g1uCw1hTztWUF1MPtBDT+uj1aPmqb02WrfCxvORLnksD7wX+jZqs51TNvs/Bjuj+p5blgm93ixETWkU5XJFV0d2BbDwQKUjrDCwWC0nIlkwfWJ5/jAgMBAAGjgYgwgYUwEwYDVR0lBAwwCgYIKwYBBQUHAwEwDAYDVR0TAQH/BAIwADAdBgNVHQ4EFgQU/xhJJjvNDsBsJPIng+oFZYxOnvswHwYDVR0jBBgwFoAUtfNLxuXWS9DlgGuMUMNnW7yx83EwIAYDVR0RAQH/BBYwFIISc3RvcmFnZS5zaWduYWwub3JnMA0GCSqGSIb3DQEBCwUAA4ICAQA7Hq+1NyGqur/7KzHd6gm4IRbxYlO7DDs3yyN7gS8d8QMMnJiJAE1z/O4opHdvZuAwQT1gZhJCmOC69emT/cKjdaMAPgbTWPQWXqfvWFJhZC+Sc6dxU5/DUQKaA7CqnIFVGrXHa/4VZD3RzdOQOuo6XspS/U5kVciNyEWQrRCGj9rgoYTvUBeyAw/brv1slkG//uGAJwZQpGxMmVbzKvGrFGq2xDkAdHHfaurXYlWhqNS/ILdvV9ZkkFOP7kvRlI0w4FX/OfL7wMFnw6h4VTmWSC2qXSyxnlePqF3KrY4LbBU7lb3W2w81iz/I0LcbJxZw/vdhTzt11uJLmWI+3d8PKUJKW8xCCuc0iJFWB8BdTaNMs5ekMwwzKsRePtEnTlxVJ35f7In1+R3MmU1Mmol+U1kdw4e7RSHA6hr0BRgaf09Q8JFOu0tv30geFTtb0CU0niorBJfp3QPMblG0Stz27xLTs49xDa+hrbM4P79Hxp0GSzYDHteBn2tUVIZAvaw0J6guPnTYMh+sKoCROq8XvPFK1zsM2uzaf5/Spobe8Sb1V2F15o288aPHtXtjZz662495tdqeEhrFfkf0O/40g+cNX71e0ahz0kshoUBCbuUD2FkrTaalHerN2eZzKzWRJuQzeh6Qi5aTAVW8Tco89CdvvnSMyFXrB17tzaKlUA==",
            "format": "base64"
          },
          {
            "data": "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",
            "format": "base64"
          }
        ],
        "server_name": "storage.signal.org",
        "t": 0.191272375,
        "tags": null,
        "tls_version": "TLSv1.3"
      },
      {
        "network": "",
        "address": "40.122.45.194:443",
        "cipher_suite": "TLS_AES_256_GCM_SHA384",
        "failure": null,
        "negotiated_protocol": "h2",
        "no_tls_verify": false,
        "peer_certificates": [
          {
            "data": "MIIFiDCCA3CgAwIBAgITFAWY15fwehAAbNuenU3NyCi/NDANBgkqhkiG9w0BAQsFADB1MQswCQYDVQQGEwJVUzETMBEGA1UECBMKQ2FsaWZvcm5pYTEWMBQGA1UEBxMNTW91bnRhaW4gVmlldzEeMBwGA1UEChMVU2lnbmFsIE1lc3NlbmdlciwgTExDMRkwFwYDVQQDExBTaWduYWwgTWVzc2VuZ2VyMB4XDTIzMDUwMjE5NDQxNFoXDTI0MDYwMjAxMzI1OVowADCCAiIwDQYJKoZIhvcNAQEBBQADggIPADCCAgoCggIBAO0g8eM//V/6pkZe6Po++L7FQfxzIPlUxwnaUFcJ3feqU94nvMl9AjeLwhzoCgdtbEkEnt56Crg9s4fmJlADGaLBGF5UZZ9reSZcv5zz62JlHnrbUGWQl4n1Xf2NQ+wx66hp7ADpFWKYbNWrkw4mbP29ieBdqEWW7MQzdOkONDThAy4q2+grz9yhGaoOC2FCgNOPv12r4yD1xcboXoBDkVKTyO8GBVd5O4ubB8xuAh9hDzqn0zcfU/tBpnR6X208icjCqPTbygZFN9gOtsQdiIyrl2roemXml4b7T0cveRvqBIm2cwpeeSyoGbEzc7dKlvS9RgiANhcxU7sU5dDVUWJLyi8PUtiXyJWq2UTeRnjGO6Nthut8P7hxLUv5/6ZqZ+p/56i25NXWegR8scqp+uvUW/5hPj2GZg3R3VIp0wMcIPHme3+87ruAzFV3DX2cz1xLZGhBaHMD6z5yqoZYupxclgGQUjmB5M0CzRbpyvuejAHZqU1i5Se/pNT8wzJVb+rBTOxhjXdIwwibnoeXHYGBG9Kzik9N8fKjD6HoyJEuaNULM0WB8u5wDoF9x/O5yFfpz8iKN3tmTskyuFj6G8TgfHoappA7TFZu/fdDt0+84n6J1exUEYXnub5xFLnrqWD0NNhjsFLxZGuC/WAgGrx/VAzZ2f5ChP7t7OY4SaizAgMBAAGjgYUwgYIwEwYDVR0lBAwwCgYIKwYBBQUHAwEwDAYDVR0TAQH/BAIwADAdBgNVHQ4EFgQUQVd2bIG0eSdqgBrd86nFFNCzhyQwHwYDVR0jBBgwFoAUtfNLxuXWS9DlgGuMUMNnW7yx83EwHQYDVR0RAQH/BBMwEYIPY2RzaS5zaWduYWwub3JnMA0GCSqGSIb3DQEBCwUAA4ICAQDDjjXidpm/NG+/5uxnA4h8DHca5+htw8sWpsPJexfbAoeudsFY9MqDhHKdoIMZfJ0E5SMB65klEAU9Q3EXhWqmv4ZfX1g9X+KTDFUPtdcOiMNL9gnKVsvTSULPhFkGzAkDkocFwI9UlE9qmX+jB+m/xmDLCmXR7NbsSV2Zif/sNtWqBmbzbFgvfkzIjMC4JcXHhX4S6EuWaJAKcFgs/0na6r74ykodjE5iNsYWPDvEBXjD2eCQ7V+iiHz4Ne6pmzNUfvrLSJC/mJsLiaVJdSGrZqRt5o5fVAaaw4sCDaWsWZIVBc+vt00mwwASEblz2HVjHoCjIb/5WRtxKmQGKK18Vpg9fuN9WmA9RzuLAvTOh3Z+omE9jf0WClQkcLr0lISvfX0l0AW4yPHINxtXgZs19tdYgJtMGBodZ0WHUN9PU4+WDZVZJ55etDn+Xb1nAGrBWZavfZ2jEiYiZ3YyTHK6MJtK6XvFhui5HclwjEgPDnhCkIlnWu6+Th4nRT3JcGgATd9Yzomi17/kDiZJhN8U+En49XiC3sBVX0t1W5kgrHejQTuJRcsvLXg730SCpFythlGr5hjhc4yZ64coamXdmLQvorcQm15Efvk5jmqngWlPaO3882Pt8zUKohixCBe16YBi07FT4Qv35ExQj1dE/cwXxFAH3FWXog1HWw9dBg==",
            "format": "base64"
          },
          {
            "data": "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",
            "format": "base64"
          }
        ],
        "server_name": "cdsi.signal.org",
        "t": 0.333897875,
        "tags": null,
        "tls_version": "TLSv1.3"
      },
      {
        "network": "",
        "address": "13.248.212.111:443",
        "cipher_suite": "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256",
        "failure": null,
        "negotiated_protocol": "h2",
        "no_tls_verify": false,
        "peer_certificates": [
          {
            "data": "MIIFiDCCA3CgAwIBAgITGB3sX1A1db5n46qLCCpWpZ2prTANBgkqhkiG9w0BAQsFADB1MQswCQYDVQQGEwJVUzETMBEGA1UECBMKQ2FsaWZvcm5pYTEWMBQGA1UEBxMNTW91bnRhaW4gVmlldzEeMBwGA1UEChMVU2lnbmFsIE1lc3NlbmdlciwgTExDMRkwFwYDVQQDExBTaWduYWwgTWVzc2VuZ2VyMB4XDTIzMTAyNzE1MzEyNVoXDTI0MTEyNjIxMjAxMFowADCCAiIwDQYJKoZIhvcNAQEBBQADggIPADCCAgoCggIBAL6PdkAcAGn6DnhdJ0MVw0HrRitYaCGhwPGFLPKJYk+jk/07BFzVJMKXmpYX09cle6ktlW7qiZ01uCU7CQ6rK9TFmb9RISrs91BZcguiMnoaxqIXaZmpWgC9pxH9NUB7DpHnsitClpCirOjYVqqVl0vT+zkr5vfSo1xapihVXsE9DLfgZG0snaqs+trEql/b0W8nITSoYgq9zpifIqgSAxPM/iNwV1JpmulE3Vv626cPuTIjihTnmIxt8JITZQNZyz5TpeCy6SsvKIw5Tv33FlPOjngkGySc85WrrUNIFEVJXLTVeA9JHxg/dDqn1uboos8/9+JGC8B3Hy2RAFk+1cyrUwYatVL07crb2HRPPzBl3WJhuyD9oBSa8WHNwPyrPnmm319BaWjtYPRWMgrFe/DoiJosqa4BPgjJY8ojZ1qm3b99wWAhidaD6qHWmwWPtEzVXaJK7pKUoXIfAxt2+zpf3ExT+uOEQypm9z4Jj5iGmF3ThFhdG3wG9Bdor7x476Cp11V9p/PS6xoYMFyzQeTTQc8dq452URW90cVH0NKDYk3x69HGaWzaNPp7eQ7ZtSiDuQfuD1BDqBjGh6zylRSFAUYD93bgD9+uRuxyIy03ru9aQ7T4oEEEiYXe1JzBudnn5wKyatmDbcP1Wldl95hegNzyN/wIcE4X+aJjLP09AgMBAAGjgYUwgYIwEwYDVR0lBAwwCgYIKwYBBQUHAwEwDAYDVR0TAQH/BAIwADAdBgNVHQ4EFgQUX7370ZNRvgNpAEYStHQCIvxADXUwHwYDVR0jBBgwFoAUtfNLxuXWS9DlgGuMUMNnW7yx83EwHQYDVR0RAQH/BBMwEYIPY2hhdC5zaWduYWwub3JnMA0GCSqGSIb3DQEBCwUAA4ICAQAQtBCo5EP7trsUfInYvU1n3T6XhL5pTZkaRMl2fAoc9EqskmaDTkOrX7uzQJ7Cwff4MKUxyvXjvj89S8U0o/HzHxxKpC7kXdnzAv2twp/vj3sEMgiRkJrZg6WecNjy4L3TbWfz617vFiYCKFENIuWvxfCg+jgajqsTNFbxQuAmLHeIqCKst3yFWBkqD7dZA/bHQgU+ATkuz5ySFYMqIGvDorY5ToNOsg8Iu356wL/h0ugxUaRgPoST4ZwEYQLuzl8VPXjWaEsZxyQa3yyvfdw0OgS0HT9y+JZ1uteT+BmFAhWC04e3+v1hOvw0NiCglRNkQiLdORWxXF5tQSijYbsRJyBSCBk+b9aEvcPV3XIyOs6b4nL0z7qd+9HXk8nJYeRnGdx6Th8OFFsjGSW2DrTKaPzeWGWmmcPs2JEosz8YF3YEqNhLFcIOeMGef9bvfT1cf6qiOTDIDIgBCD434pdob1W1qTJjXBYB+o+bwMhnN5btvefe/TaKpfDIu/wtTvWmCvz2uQhucr+vzoEDHd3kYaYtmZHOVYsUX4rswUNDDuNs3p4fPRSzv9GqMfQnwsbPQ3FSd7fkCnE1t79CeB+mQGPHBCk9y1Zb9ILZycJgobdiFdkssMhoo7KOR0hGHTLUh+x3hw+mbeNyW6YmqMkHT9Lzfa9m8/vK2whttEZl0Q==",
            "format": "base64"
          },
          {
            "data": "MIIF2zCCA8OgAwIBAgIUAMHz4g60cIDBpPr1gyZ/JDaaPpcwDQYJKoZIhvcNAQELBQAwdTELMAkGA1UEBhMCVVMxEzARBgNVBAgTCkNhbGlmb3JuaWExFjAUBgNVBAcTDU1vdW50YWluIFZpZXcxHjAcBgNVBAoTFVNpZ25hbCBNZXNzZW5nZXIsIExMQzEZMBcGA1UEAxMQU2lnbmFsIE1lc3NlbmdlcjAeFw0yMjAxMjYwMDQ1NTFaFw0zMjAxMjQwMDQ1NTBaMHUxCzAJBgNVBAYTAlVTMRMwEQYDVQQIEwpDYWxpZm9ybmlhMRYwFAYDVQQHEw1Nb3VudGFpbiBWaWV3MR4wHAYDVQQKExVTaWduYWwgTWVzc2VuZ2VyLCBMTEMxGTAXBgNVBAMTEFNpZ25hbCBNZXNzZW5nZXIwggIiMA0GCSqGSIb3DQEBAQUAA4ICDwAwggIKAoICAQDEecifxMHHlDhxbERVdErOhGsLO08PUdNkATjZ1kT51uPf5JPiRbus9F4J/GgBQ4ANSAjIDZuFY0WOvG/i0qvxthpW70ocp8IjkiWTNiA81zQNQdCiWbGDU4B1sLi2o4JgJMweSkQFiyDynqWgHpw+KmvytCzRWnvrrptIfE4GPxNOsAtXFbVH++8JO42IaKRVlbfpe/lUHbjiYmIpQroZPGPY4Oql8KM3o39ObPnTo1WoM4moyOOZpU3lV1awftvWBx1sbTBL02sQWfHRxgNVF+Pj0fdDMMFdFJobArrLVfK2Ua+dYN4pV5XIxzVarSRW73CXqQ+2qloPW/ynpa3gRtYeGWV4jl7eD0PmeHpKOY78idP4H1jfAv0TAVeKpuB5ZFZ2szcySxrQa8d7FIf0kNJe9gIRjbQ+XrvnN+ZZvj6d+8uBJq8LfQaFhlVfI0/aIdggScapR7w8oLpvdflUWqcTLeXVNLVrg15cEDwdlV8PVscT/KT0bfNzKI80qBq8LyRmauAqP0CDjayYGb2UAabnhefgmRY6aBE5mXxdbyAEzzCS3vDxjeTD8v8nbDq+SD6lJi0i7jgwEfNDhe9XK50baK15Udc8Cr/ZlhGMjNmWqBd0jIpaZm1rzWA0k4VwXtDwpBXSz8oBFshiXs3FD6jHY2IhOR3ppbyd4qRUpwIDAQABo2MwYTAOBgNVHQ8BAf8EBAMCAQYwDwYDVR0TAQH/BAUwAwEB/zAdBgNVHQ4EFgQUtfNLxuXWS9DlgGuMUMNnW7yx83EwHwYDVR0jBBgwFoAUtfNLxuXWS9DlgGuMUMNnW7yx83EwDQYJKoZIhvcNAQELBQADggIBABUeiryS0qjykBN75aoHO9bVPrrX+DSJIB9V2YzkFVyh/io65QJMG8naWVGOSpVRwUwhZVKh3JVp/miPgzTGAo7zhrDIoXc+ih7orAMb19qol/2Ha8OZLa75LojJNRbZoCR5C+gM8C+spMLjFf9k3JVxdajhtRUcR0zYhwsBS7qZ5Me0d6gRXD0ZiSbadMMxSw6KfKk3ePmPb9gX+MRTS63c8mLzVYB/3fe/bkpq4RUwzUHvoZf+SUD7NzSQRQQMfvAHlxk11TVNxScYPtxXDyiy3Cssl9gWrrWqQ/omuHipoH62J7h8KAYbr6oEIq+Czuenc3eCIBGBBfvCpuFOgckAXXE4MlBasEU0MO66GrTCgMt9bAmSw3TrRP12+ZUFxYNtqWluRU8JWQ4FCCPcz9pgMRBOgn4lTxDZG+I47OKNuSRjFEP94cdgxd3H/5BK7WHUz1tAGQ4BgepSXgmjzifFT5FVTDTl3ZnWUVBXiHYtbOBgLiSIkbqGMCLtrBtFIeQ7RRTb3L+IE9R0UB0cJB3AXbf1lVkOcmrdu2h8A32aCwtr5S1fBF1unlG7imPmqJfpOMWa8yIF/KWVm29JAPq8Lrsybb0z5gg8w7ZblEuB9zOW9M3l60DXuJO6l7g+deV6P96rv2unHS8UlvWiVWDy9qfgAJizyy3kqM4lOwBH",
            "format": "base64"
          }
        ],
        "server_name": "chat.signal.org",
        "t": 0.451029208,
        "tags": null,
        "tls_version": "TLSv1.2"
      }
    ],
    "signal_backend_status": "ok",
    "signal_backend_failure": null
  },
  "test_name": "signal",
  "test_runtime": 0.595529583,
  "test_start_time": "2023-12-01 10:24:58",
  "test_version": "0.2.5"
}
```

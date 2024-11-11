# TLSHandshake Data Format

This document describes the keys with `test_keys` that all experiments
using TLS SHOULD populate, possibly using directly the specific template
code. See this directory's [README](README.md) for the basic concepts.

| Name       | `tlshandshake` |
|------------|----------------|
| Version    | 0              |

## Specification

```JSON
{
    "tls_handshakes": []
}
```

- `tls_handshakes` (`[]TLSHandshake`): list of `TLSHandshake` objects.

## TLSHandshake

```JSON
{
    "network": "",
    "address": "",
    "cipher_suite": "",
    "conn_id": 1231,
    "failure": "ssl_invalid_hostname",
    "so_error": "host_unreachable",
    "negotiated_protocol": "",
    "no_tls_verify": false,
    "peer_certificates": [],
    "server_name": "example.com",
    "echconfig": "",
    "t0": 1.001,
    "t": 1.11,
    "tags": [],
    "tls_version": "",
    "transaction_id": 1
}
```
- `network` (`string`; optional): The network for the handshake (`"tcp"` or `"udp"`). Until
2022-09-08, we incorrectly documented that this could have been either `"tls"` or `"quic"` but
the code always used `"tcp"`, so we adapted the spec to the code. On the same day, we also
realized that using `"udp"` instead of `"quic"` would be more consistent, so we also changed
`"quic"` to always become `"udp"`. These changes occurred during the OONI Probe
v3.16.0 release cycle in [ooni/probe-cli#946](https://github.com/ooni/probe-cli/pull/946).

- `address` (`string`): The endpoint IP address (host:port) with which the handshake is performed.

- `cipher_suite` (`string`): the negotiated cipher suite, if any.

- `conn_id` (`int`; optional; since 2020-01-11; deprecated): identifier of the connection. See
the discussion in `df-008-netevents.md`.

- `failure` (`string`; nullable): if there was an error, this field is
a string indicating the error, otherwise it MUST be `null`.

- `so_error` (`string`; optional): If there was a soft error (e.g. `ICMP Time Exceeded`), this 
field is a string indicating the error, otherwise it is omitted.

- `negotiated_protocol`: (`string`): the protocol negotiated with ALPN, if any.

- `no_tls_verify`: (`bool`): indicates if we have bypassed certificate chain validation when performing
the TLS handshake.

- `peer_certificates`: (`[]BinaryData`): list of peer certificates in ASN.1
DER format represented using the `BinaryData` object described
in `df-001-httpt.md`.

- `server_name`: (`string`; optional): server name used as part of the TLS handshake
to verify the server's X.509 certificate. Note that, when this field contains an IP
address rather than a domain name, the corresponding value is not included in the TLS
ClientHello as described by [RFC 6066, Section 3](https://datatracker.ietf.org/doc/html/rfc6066#section-3);

- `outer_server_name`: (`string`; optional): server name used in the
`ClientHelloOuter` when [TLS ECH](https://www.ietf.org/archive/id/draft-ietf-tls-esni-22.html)
is being used. When this is set, the `server_name` field indicates the field
used inside of the encrypted client hello.

- `echconfig`: (`string`; optional): ECHConfig as defined in [TLS ECH
  Spec](https://www.ietf.org/archive/id/draft-ietf-tls-esni-22.html#name-encrypted-clienthello-confi)
base64 encoded as it would be presented inside of an SVCB HTTPS SvcParam as per
[RFC9460](https://www.rfc-editor.org/rfc/rfc9460.html). In the event that only
[GREASE ECH](https://www.ietf.org/archive/id/draft-ietf-tls-esni-22.html#name-grease-psk) is being used, it will contain the
string literal `GREASE`.

- `t0` (`float`): number of seconds elapsed since `measurement_start_time`
measured in the moment in which we started the operation (`t - t0` gives you
the amount of time spent performing the operation);

- `t` (`float`): number of seconds elapsed since `measurement_start_time`
measured in the moment in which `failure` is determined (`t - t0` gives you
the amount of time spent performing the operation);

- `tags` (`[]string`; optional): list of tags for this event. This is useful to
understand what part of a complex measurement generated an event.

- `tls_version` (`string`): the negotiated TLS version, if any.

- `transaction_id` (`int`; optional; since 2020-01-11): the set of operations
to which this event belongs to (typically an HTTP transaction or a DNS
round trip). A zero or missing value means we don't know the transaction
to which this code belongs to.

## Example

In the following example we've omitted all the keys that are
not relevant to the TLS data format:

```JSON
{
  "network": "tcp",
  "address": "93.184.216.34:443",
  "cipher_suite": "TLS_AES_256_GCM_SHA384",
  "failure": null,
  "negotiated_protocol": "h2",
  "no_tls_verify": false,
  "peer_certificates": [
    {
      "data": "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",
      "format": "base64"
    },
    {
      "data": "MIIEvjCCA6agAwIBAgIQBtjZBNVYQ0b2ii+nVCJ+xDANBgkqhkiG9w0BAQsFADBhMQswCQYDVQQGEwJVUzEVMBMGA1UEChMMRGlnaUNlcnQgSW5jMRkwFwYDVQQLExB3d3cuZGlnaWNlcnQuY29tMSAwHgYDVQQDExdEaWdpQ2VydCBHbG9iYWwgUm9vdCBDQTAeFw0yMTA0MTQwMDAwMDBaFw0zMTA0MTMyMzU5NTlaME8xCzAJBgNVBAYTAlVTMRUwEwYDVQQKEwxEaWdpQ2VydCBJbmMxKTAnBgNVBAMTIERpZ2lDZXJ0IFRMUyBSU0EgU0hBMjU2IDIwMjAgQ0ExMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwUuzZUdwvN1PWNvsnO3DZuUfMRNUrUpmRh8sCuxkB+Uu3Ny5CiDt3+PE0J6aqXodgojlEVbbHp9YwlHnLDQNLtKS4VbL8Xlfs7uHyiUDe5pSQWYQYE9XE0nw6Ddng9/n00tnTCJRpt8OmRDtV1F0JuJ9x8piLhMbfyOIJVNvwTRYAIuE//i+p1hJInuWraKImxW8oHzf6VGo1bDtN+I2tIJLYrVJmuzHZ9bjPvXj1hJeRPG/cUJ9WIQDgLGBAfr5yjK7tI4nhyfFK3TUqNaX3sNk+crOU6JWvHgXjkkDKa77SU+kFbnO8lwZV21reacroicgE7XQPUDTITAHk+qZ9QIDAQABo4IBgjCCAX4wEgYDVR0TAQH/BAgwBgEB/wIBADAdBgNVHQ4EFgQUt2ui6qiqhIx56rTaD5iyxZV2ufQwHwYDVR0jBBgwFoAUA95QNVbRTLtm8KPiGxvDl7I90VUwDgYDVR0PAQH/BAQDAgGGMB0GA1UdJQQWMBQGCCsGAQUFBwMBBggrBgEFBQcDAjB2BggrBgEFBQcBAQRqMGgwJAYIKwYBBQUHMAGGGGh0dHA6Ly9vY3NwLmRpZ2ljZXJ0LmNvbTBABggrBgEFBQcwAoY0aHR0cDovL2NhY2VydHMuZGlnaWNlcnQuY29tL0RpZ2lDZXJ0R2xvYmFsUm9vdENBLmNydDBCBgNVHR8EOzA5MDegNaAzhjFodHRwOi8vY3JsMy5kaWdpY2VydC5jb20vRGlnaUNlcnRHbG9iYWxSb290Q0EuY3JsMD0GA1UdIAQ2MDQwCwYJYIZIAYb9bAIBMAcGBWeBDAEBMAgGBmeBDAECATAIBgZngQwBAgIwCAYGZ4EMAQIDMA0GCSqGSIb3DQEBCwUAA4IBAQCAMs5eC91uWg0Kr+HWhMvAjvqFcO3aXbMM9yt1QP6FCvrzMXi3cEsaiVi6gL3zax3pfs8LulicWdSQ0/1s/dCYbbdxglvPbQtaCdB73sRD2Cqk3p5BJl+7j5nL3a7hqG+fh/50tx8bIKuxT8b1Z11dmzzp/2n3YWzW2fP9NsarA4h20ksudYbj/NhVfSbCEXffPgK2fPOre3qGNm+499iTcc+G33Mw+nur7SpZyEKEOxEXGlLzyQ4UfaJbcme6ce1XR2bFuAJKZTRei9AqPCCcUZlM51Ke92sRKw2Sfh3oius2FkOH6ipjv3U/697EA7sKPPcw7+uvTPyLNhBzPvOk",
      "format": "base64"
    }
  ],
  "server_name": "example.com",
  "t0": 0.601812,
  "t": 0.900702,
  "tags": [],
  "tls_version": "TLSv1.3",
  "transaction_id": 4
}
```

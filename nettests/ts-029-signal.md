# Specification version number

2021-02-15-001

* _status_: current

# Specification name

Signal

# Test preconditions

* An internet connection

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

* https://textsecure-service.whispersystems.org/
* https://storage.signal.org/
* https://api.directory.signal.org/
* https://cdn.signal.org/
* https://cdn2.signal.org/
* https://sfu.voip.signal.org/

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
MIIEjDCCAnSgAwIBAgITV+dgmSk1+75Wwn/Mjz8f+gQ9qTANBgkqhkiG9w0BAQsF
ADB1MQswCQYDVQQGEwJVUzETMBEGA1UECBMKQ2FsaWZvcm5pYTEWMBQGA1UEBxMN
TW91bnRhaW4gVmlldzEeMBwGA1UEChMVU2lnbmFsIE1lc3NlbmdlciwgTExDMRkw
FwYDVQQDExBTaWduYWwgTWVzc2VuZ2VyMB4XDTIyMDgyMzE2NTIxMVoXDTIzMDky
MzIyNDA1NlowADCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBALf8th0A
N5TFsvvdfaSP1WyCMn5Ql81IF5D0pXrdE9fGDz5AaeAbCazxXU8tnjZiUr4a/BGD
h3ZxORHXJ2SA3HA2UFG+qHik59QNGkY4Jv4emTM5QLw0fcsGRgJnzb7A60LRoxGs
17jxD1zyVl/SXn/Ql3cvBrHjxPzJ6NcQG4Pek7YieH2xiMP794QUu0XJYlBx0uvx
xOI3qpw5c6oNORGY8hlwWzbv+sqvShXhteOlkzluKtIqpL8+NV206JIqLkaKFjB7
To14TSFF3tYxxsHYwDhRKPatqYpbebx3iCo0H33dL0gjoUtdvRgsdHqnUQXSqoRH
cUYCIPs3FivKNrcCAwEAAaOBiTCBhjATBgNVHSUEDDAKBggrBgEFBQcDATAMBgNV
HRMBAf8EAjAAMB0GA1UdDgQWBBSidZq+TLJkcDuNV5j1KbOm/l+dhjAfBgNVHSME
GDAWgBS180vG5dZL0OWAa4xQw2dbvLHzcTAhBgNVHREBAf8EFzAVghNzZnUudm9p
cC5zaWduYWwub3JnMA0GCSqGSIb3DQEBCwUAA4ICAQCDchlftHXUm3sFWL86GKUs
w7nxOiJDZYR+xIVGbsUarBolEsZZkYjTDB427ZjgBS+Nfhhbrw4k2LMarkxf2TQX
aelPHRa5xNPVfkrN8xw4fv/8TLE9GSjKlrNJm1EoTZL5CYWQU+qe4CuKfAJU6h8l
xIkcik61aCeNLQoaI1L3V8tPXmmqMWpsnZmFg6YLGeMTLs4skdFqgLOnx9EF2jgO
7EAJ9HcrgSPirQeuDJKhamaLtQiqIQR8L3H4YG1FDiuOeto6f1LRCIqjH1Mye1BM
33Qg/VilLQIWp8+C4GJZ0+LO1cfatNh8tkDbrwMzUeA1nLEZHMlgXE05z00euNlQ
0+evTmJzWRKJHugPnA3vvdzy4lbYvYWaXs8pACrVpESui8I+v6jdH814lOxpDwNH
bPrxfOxhIxfFiVttCl3AQZBLJM6M0ty6/Q7bYsdNT23jKMl0AmDhj9qn/7dzYcVi
vI0XKaaJl4ov3IDbuMe0oZWhoLwzPuWxxkWDjTb8ngDnWZT1o5dAR9fltr38m42N
uA/SkxghiAMmvkC8nhEJ7yT2hme+rozPZSp1SSEDViDkA4KnnQpMcNiotCQpNOe7
YfA9uSnjHjZloRTPUgtkKQ3u8ZZprFQlS2jDE18BRGdh24V5OsCbMvFPtrEsjG4H
5xvkiIV0FpbMk4Gj8I4Hbw==
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

# Expected output

## Parent data format

* `df-001-httpt`
* `df-002-dnst`
* `df-005-tcpconnect`
* `df-006-tlshandshake`

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

All data collected with `test_version` `0.2.0` after 2022-10-19 should be
treated with extra care, as the values of `signal_backend_failure` and
`signal_backend_status` cannot be trusted.`
This is a result of signal having changed the root CA for at least one of their
endpoints (`sfu.voip.signal.org`) resulting in TLS validation errors.

For more information see: https://github.com/ooni/probe/issues/2344

## Example output sample

```json
{
    "annotations": {
        "assets_version": "20210129095811",
        "engine_name": "ooniprobe-engine",
        "engine_version": "3.5.2",
        "platform": "macos"
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
    "measurement_start_time": "2021-02-15 17:33:22",
    "probe_asn": "AS30722",
    "probe_cc": "IT",
    "probe_ip": "127.0.0.1",
    "probe_network_name": "Vodafone Italia S.p.A.",
    "report_id": "",
    "resolver_asn": "AS30722",
    "resolver_ip": "91.80.37.85",
    "resolver_network_name": "Vodafone Italia S.p.A.",
    "software_name": "miniooni",
    "software_version": "3.5.2",
    "test_keys": {
        "agent": "redirect",
        "failed_operation": null,
        "failure": null,
        "network_events": [
            {
                "failure": null,
                "operation": "http_transaction_start",
                "t": 8.3823e-05
            },
            {
                "failure": null,
                "operation": "http_request_metadata",
                "t": 8.7827e-05
            },
            {
                "failure": null,
                "operation": "resolve_start",
                "t": 0.000141854
            },
            {
                "failure": null,
                "operation": "resolve_done",
                "t": 0.003337152
            },
            {
                "address": "142.250.180.110:443",
                "failure": null,
                "operation": "connect",
                "proto": "tcp",
                "t": 0.024007924
            },
            {
                "failure": null,
                "operation": "tls_handshake_start",
                "t": 0.024014429
            },
            {
                "failure": null,
                "num_bytes": 307,
                "operation": "write",
                "t": 0.024158859
            },
            {
                "failure": null,
                "num_bytes": 517,
                "operation": "read",
                "t": 0.061207645
            },
            {
                "failure": null,
                "num_bytes": 3718,
                "operation": "read",
                "t": 0.06132087
            },
            {
                "failure": null,
                "num_bytes": 30,
                "operation": "write",
                "t": 0.061625791
            },
            {
                "failure": "ssl_invalid_hostname",
                "operation": "tls_handshake_done",
                "t": 0.061638291
            },
            {
                "failure": "ssl_invalid_hostname",
                "operation": "http_transaction_done",
                "t": 0.061672419
            },
            {
                "failure": null,
                "operation": "http_transaction_start",
                "t": 6.5205e-05
            },
            {
                "failure": null,
                "operation": "http_request_metadata",
                "t": 7.1212e-05
            },
            {
                "failure": null,
                "operation": "resolve_start",
                "t": 0.000102339
            },
            {
                "failure": null,
                "operation": "resolve_done",
                "t": 0.001511908
            },
            {
                "address": "142.250.180.83:443",
                "failure": null,
                "operation": "connect",
                "proto": "tcp",
                "t": 0.020983631
            },
            {
                "failure": null,
                "operation": "tls_handshake_start",
                "t": 0.021020682
            },
            {
                "failure": null,
                "num_bytes": 288,
                "operation": "write",
                "t": 0.021162342
            },
            {
                "failure": null,
                "num_bytes": 517,
                "operation": "read",
                "t": 0.058904077
            },
            {
                "failure": null,
                "num_bytes": 1029,
                "operation": "read",
                "t": 0.059088685
            },
            {
                "failure": null,
                "num_bytes": 64,
                "operation": "write",
                "t": 0.059631968
            },
            {
                "failure": null,
                "operation": "tls_handshake_done",
                "t": 0.059647893
            },
            {
                "failure": null,
                "num_bytes": 86,
                "operation": "write",
                "t": 0.059732277
            },
            {
                "failure": null,
                "num_bytes": 207,
                "operation": "write",
                "t": 0.059875286
            },
            {
                "failure": null,
                "operation": "http_wrote_headers",
                "t": 0.059876245
            },
            {
                "failure": null,
                "operation": "http_wrote_request",
                "t": 0.059876496
            },
            {
                "failure": null,
                "num_bytes": 93,
                "operation": "read",
                "t": 0.095560129
            },
            {
                "failure": null,
                "num_bytes": 31,
                "operation": "write",
                "t": 0.095595054
            },
            {
                "failure": null,
                "num_bytes": 240,
                "operation": "read",
                "t": 0.182925014
            },
            {
                "failure": null,
                "operation": "http_first_response_byte",
                "t": 0.182959583
            },
            {
                "failure": null,
                "num_bytes": 39,
                "operation": "write",
                "t": 0.182993097
            },
            {
                "failure": null,
                "operation": "http_response_metadata",
                "t": 0.183023028
            },
            {
                "failure": null,
                "operation": "http_response_body_snapshot",
                "t": 0.183038401
            },
            {
                "failure": null,
                "operation": "http_transaction_done",
                "t": 0.183038763
            },
            {
                "failure": null,
                "num_bytes": 24,
                "operation": "write",
                "t": 0.183065863
            },
            {
                "failure": null,
                "operation": "http_transaction_start",
                "t": 0.183376502
            },
            {
                "failure": null,
                "operation": "http_request_metadata",
                "t": 0.183386905
            },
            {
                "failure": null,
                "operation": "resolve_start",
                "t": 0.183978066
            },
            {
                "failure": null,
                "operation": "resolve_done",
                "t": 0.184795576
            },
            {
                "address": "104.18.28.74:443",
                "failure": null,
                "operation": "connect",
                "proto": "tcp",
                "t": 0.221721016
            },
            {
                "failure": null,
                "operation": "tls_handshake_start",
                "t": 0.221728716
            },
            {
                "failure": null,
                "num_bytes": 285,
                "operation": "write",
                "t": 0.221855386
            },
            {
                "failure": null,
                "num_bytes": 517,
                "operation": "read",
                "t": 0.261125427
            },
            {
                "failure": null,
                "num_bytes": 1027,
                "operation": "read",
                "t": 0.261234019
            },
            {
                "failure": null,
                "num_bytes": 64,
                "operation": "write",
                "t": 0.26150956
            },
            {
                "failure": null,
                "operation": "tls_handshake_done",
                "t": 0.261521176
            },
            {
                "failure": null,
                "num_bytes": 86,
                "operation": "write",
                "t": 0.26156617
            },
            {
                "failure": null,
                "num_bytes": 205,
                "operation": "write",
                "t": 0.261604205
            },
            {
                "failure": null,
                "operation": "http_wrote_headers",
                "t": 0.261604807
            },
            {
                "failure": null,
                "operation": "http_wrote_request",
                "t": 0.261604996
            },
            {
                "failure": null,
                "num_bytes": 71,
                "operation": "read",
                "t": 0.298637859
            },
            {
                "failure": null,
                "num_bytes": 31,
                "operation": "write",
                "t": 0.298690079
            },
            {
                "failure": null,
                "num_bytes": 703,
                "operation": "read",
                "t": 0.315380945
            },
            {
                "failure": null,
                "operation": "http_first_response_byte",
                "t": 0.315457591
            },
            {
                "failure": null,
                "operation": "http_response_metadata",
                "t": 0.315536195
            },
            {
                "failure": null,
                "operation": "http_response_body_snapshot",
                "t": 0.315543117
            },
            {
                "failure": null,
                "operation": "http_transaction_done",
                "t": 0.315543519
            },
            {
                "failure": null,
                "num_bytes": 24,
                "operation": "write",
                "t": 0.315612024
            },
            {
                "failure": null,
                "operation": "http_transaction_start",
                "t": 0.061873488
            },
            {
                "failure": null,
                "operation": "http_request_metadata",
                "t": 0.061877121
            },
            {
                "failure": null,
                "operation": "resolve_start",
                "t": 0.061908456
            },
            {
                "failure": null,
                "operation": "resolve_done",
                "t": 0.063186985
            },
            {
                "address": "52.222.133.65:443",
                "failure": null,
                "operation": "connect",
                "proto": "tcp",
                "t": 0.075162082
            },
            {
                "failure": null,
                "operation": "tls_handshake_start",
                "t": 0.075200223
            },
            {
                "failure": null,
                "num_bytes": 284,
                "operation": "write",
                "t": 0.075327924
            },
            {
                "failure": null,
                "num_bytes": 517,
                "operation": "read",
                "t": 0.087022739
            },
            {
                "failure": null,
                "num_bytes": 921,
                "operation": "read",
                "t": 0.087209949
            },
            {
                "failure": null,
                "num_bytes": 1063,
                "operation": "read",
                "t": 0.089562666
            },
            {
                "failure": null,
                "num_bytes": 64,
                "operation": "write",
                "t": 0.090256622
            },
            {
                "failure": null,
                "operation": "tls_handshake_done",
                "t": 0.090274688
            },
            {
                "failure": null,
                "num_bytes": 86,
                "operation": "write",
                "t": 0.090389725
            },
            {
                "failure": null,
                "num_bytes": 204,
                "operation": "write",
                "t": 0.090556616
            },
            {
                "failure": null,
                "operation": "http_wrote_headers",
                "t": 0.090558243
            },
            {
                "failure": null,
                "operation": "http_wrote_request",
                "t": 0.090558612
            },
            {
                "failure": null,
                "num_bytes": 71,
                "operation": "read",
                "t": 0.103536155
            },
            {
                "failure": null,
                "num_bytes": 31,
                "operation": "write",
                "t": 0.103587541
            },
            {
                "failure": null,
                "num_bytes": 549,
                "operation": "read",
                "t": 0.534620228
            },
            {
                "failure": null,
                "operation": "http_first_response_byte",
                "t": 0.534684437
            },
            {
                "failure": null,
                "operation": "http_response_metadata",
                "t": 0.534731677
            },
            {
                "failure": null,
                "operation": "http_response_body_snapshot",
                "t": 0.534738715
            },
            {
                "failure": null,
                "operation": "http_transaction_done",
                "t": 0.534739079
            },
            {
                "failure": null,
                "num_bytes": 24,
                "operation": "write",
                "t": 0.534800491
            },
            {
                "failure": null,
                "operation": "http_transaction_start",
                "t": 6.5202e-05
            },
            {
                "failure": null,
                "operation": "http_request_metadata",
                "t": 8.6486e-05
            },
            {
                "failure": null,
                "operation": "resolve_start",
                "t": 0.000150194
            },
            {
                "failure": null,
                "operation": "resolve_done",
                "t": 0.001506337
            },
            {
                "address": "20.62.208.25:443",
                "failure": null,
                "operation": "connect",
                "proto": "tcp",
                "t": 0.119333786
            },
            {
                "failure": null,
                "operation": "tls_handshake_start",
                "t": 0.119346492
            },
            {
                "failure": null,
                "num_bytes": 294,
                "operation": "write",
                "t": 0.119427559
            },
            {
                "failure": null,
                "num_bytes": 517,
                "operation": "read",
                "t": 0.573607399
            },
            {
                "failure": null,
                "num_bytes": 1034,
                "operation": "read",
                "t": 0.573677755
            },
            {
                "failure": null,
                "num_bytes": 126,
                "operation": "write",
                "t": 0.574411487
            },
            {
                "failure": null,
                "num_bytes": 51,
                "operation": "read",
                "t": 0.741364574
            },
            {
                "failure": null,
                "operation": "tls_handshake_done",
                "t": 0.741477576
            },
            {
                "failure": null,
                "operation": "http_wrote_headers",
                "t": 0.741607712
            },
            {
                "failure": null,
                "operation": "http_wrote_request",
                "t": 0.741610825
            },
            {
                "failure": null,
                "num_bytes": 320,
                "operation": "write",
                "t": 0.741645076
            },
            {
                "failure": null,
                "num_bytes": 400,
                "operation": "read",
                "t": 0.878362333
            },
            {
                "failure": null,
                "operation": "http_first_response_byte",
                "t": 0.878405897
            },
            {
                "failure": null,
                "operation": "http_response_metadata",
                "t": 0.87858159
            },
            {
                "failure": null,
                "operation": "http_response_body_snapshot",
                "t": 0.878630291
            },
            {
                "failure": null,
                "operation": "http_transaction_done",
                "t": 0.87863092
            },
            {
                "failure": null,
                "num_bytes": 31,
                "operation": "write",
                "t": 0.878693338
            }
        ],
        "queries": [
            {
                "answers": [
                    {
                        "asn": 15169,
                        "as_org_name": "Google LLC",
                        "answer_type": "A",
                        "ipv4": "142.250.180.110",
                        "ttl": null
                    }
                ],
                "engine": "system",
                "failure": null,
                "hostname": "textsecure-service.whispersystems.org",
                "query_type": "A",
                "resolver_hostname": null,
                "resolver_port": null,
                "resolver_address": "",
                "t": 0.003337152
            },
            {
                "answers": [
                    {
                        "asn": 15169,
                        "as_org_name": "Google LLC",
                        "answer_type": "A",
                        "ipv4": "142.250.180.83",
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
                "t": 0.001511908
            },
            {
                "answers": [
                    {
                        "asn": 15169,
                        "as_org_name": "Google LLC",
                        "answer_type": "AAAA",
                        "ipv6": "2a00:1450:4002:402::2013",
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
                "t": 0.001511908
            },
            {
                "answers": [
                    {
                        "asn": 13335,
                        "as_org_name": "Cloudflare, Inc.",
                        "answer_type": "A",
                        "ipv4": "104.18.28.74",
                        "ttl": null
                    },
                    {
                        "asn": 13335,
                        "as_org_name": "Cloudflare, Inc.",
                        "answer_type": "A",
                        "ipv4": "104.18.29.74",
                        "ttl": null
                    }
                ],
                "engine": "system",
                "failure": null,
                "hostname": "cdn2.signal.org",
                "query_type": "A",
                "resolver_hostname": null,
                "resolver_port": null,
                "resolver_address": "",
                "t": 0.184795576
            },
            {
                "answers": [
                    {
                        "asn": 13335,
                        "as_org_name": "Cloudflare, Inc.",
                        "answer_type": "AAAA",
                        "ipv6": "2606:4700::6812:1c4a",
                        "ttl": null
                    },
                    {
                        "asn": 13335,
                        "as_org_name": "Cloudflare, Inc.",
                        "answer_type": "AAAA",
                        "ipv6": "2606:4700::6812:1d4a",
                        "ttl": null
                    }
                ],
                "engine": "system",
                "failure": null,
                "hostname": "cdn2.signal.org",
                "query_type": "AAAA",
                "resolver_hostname": null,
                "resolver_port": null,
                "resolver_address": "",
                "t": 0.184795576
            },
            {
                "answers": [
                    {
                        "asn": 16509,
                        "as_org_name": "Amazon.com, Inc.",
                        "answer_type": "A",
                        "ipv4": "52.222.133.65",
                        "ttl": null
                    },
                    {
                        "asn": 16509,
                        "as_org_name": "Amazon.com, Inc.",
                        "answer_type": "A",
                        "ipv4": "52.222.133.123",
                        "ttl": null
                    },
                    {
                        "asn": 16509,
                        "as_org_name": "Amazon.com, Inc.",
                        "answer_type": "A",
                        "ipv4": "52.222.133.51",
                        "ttl": null
                    },
                    {
                        "asn": 16509,
                        "as_org_name": "Amazon.com, Inc.",
                        "answer_type": "A",
                        "ipv4": "52.222.133.111",
                        "ttl": null
                    }
                ],
                "engine": "system",
                "failure": null,
                "hostname": "cdn.signal.org",
                "query_type": "A",
                "resolver_hostname": null,
                "resolver_port": null,
                "resolver_address": "",
                "t": 0.063186985
            },
            {
                "answers": [
                    {
                        "asn": 16509,
                        "as_org_name": "Amazon.com, Inc.",
                        "answer_type": "AAAA",
                        "ipv6": "2600:9000:201a:9000:1d:4f32:50c0:93a1",
                        "ttl": null
                    },
                    {
                        "asn": 16509,
                        "as_org_name": "Amazon.com, Inc.",
                        "answer_type": "AAAA",
                        "ipv6": "2600:9000:201a:e00:1d:4f32:50c0:93a1",
                        "ttl": null
                    },
                    {
                        "asn": 16509,
                        "as_org_name": "Amazon.com, Inc.",
                        "answer_type": "AAAA",
                        "ipv6": "2600:9000:201a:8200:1d:4f32:50c0:93a1",
                        "ttl": null
                    },
                    {
                        "asn": 16509,
                        "as_org_name": "Amazon.com, Inc.",
                        "answer_type": "AAAA",
                        "ipv6": "2600:9000:201a:2600:1d:4f32:50c0:93a1",
                        "ttl": null
                    },
                    {
                        "asn": 16509,
                        "as_org_name": "Amazon.com, Inc.",
                        "answer_type": "AAAA",
                        "ipv6": "2600:9000:201a:a400:1d:4f32:50c0:93a1",
                        "ttl": null
                    },
                    {
                        "asn": 16509,
                        "as_org_name": "Amazon.com, Inc.",
                        "answer_type": "AAAA",
                        "ipv6": "2600:9000:201a:5c00:1d:4f32:50c0:93a1",
                        "ttl": null
                    },
                    {
                        "asn": 16509,
                        "as_org_name": "Amazon.com, Inc.",
                        "answer_type": "AAAA",
                        "ipv6": "2600:9000:201a:fe00:1d:4f32:50c0:93a1",
                        "ttl": null
                    },
                    {
                        "asn": 16509,
                        "as_org_name": "Amazon.com, Inc.",
                        "answer_type": "AAAA",
                        "ipv6": "2600:9000:201a:9200:1d:4f32:50c0:93a1",
                        "ttl": null
                    }
                ],
                "engine": "system",
                "failure": null,
                "hostname": "cdn.signal.org",
                "query_type": "AAAA",
                "resolver_hostname": null,
                "resolver_port": null,
                "resolver_address": "",
                "t": 0.063186985
            },
            {
                "answers": [
                    {
                        "asn": 8075,
                        "as_org_name": "Microsoft Corporation",
                        "answer_type": "A",
                        "ipv4": "20.62.208.25",
                        "ttl": null
                    }
                ],
                "engine": "system",
                "failure": null,
                "hostname": "api.directory.signal.org",
                "query_type": "A",
                "resolver_hostname": null,
                "resolver_port": null,
                "resolver_address": "",
                "t": 0.001506337
            }
        ],
        "requests": [
            {
                "failure": "ssl_invalid_hostname",
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
                            "en-US;q=0.8,en;q=0.5"
                        ],
                        [
                            "Host",
                            "textsecure-service.whispersystems.org"
                        ],
                        [
                            "User-Agent",
                            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
                        ]
                    ],
                    "headers": {
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                        "Accept-Language": "en-US;q=0.8,en;q=0.5",
                        "Host": "textsecure-service.whispersystems.org",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
                    },
                    "method": "GET",
                    "tor": {
                        "exit_ip": null,
                        "exit_name": null,
                        "is_tor": false
                    },
                    "x_transport": "tcp",
                    "url": "https://textsecure-service.whispersystems.org/"
                },
                "response": {
                    "body": "",
                    "body_is_truncated": false,
                    "code": 0,
                    "headers_list": null,
                    "headers": null
                },
                "t": 8.3823e-05
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
                            "en-US;q=0.8,en;q=0.5"
                        ],
                        [
                            "Host",
                            "storage.signal.org"
                        ],
                        [
                            "User-Agent",
                            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
                        ]
                    ],
                    "headers": {
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                        "Accept-Language": "en-US;q=0.8,en;q=0.5",
                        "Host": "storage.signal.org",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
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
                            "Mon, 15 Feb 2021 17:33:22 GMT"
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
                        "Date": "Mon, 15 Feb 2021 17:33:22 GMT",
                        "Vary": "Accept-Encoding",
                        "Via": "1.1 google"
                    }
                },
                "t": 6.5205e-05
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
                            "en-US;q=0.8,en;q=0.5"
                        ],
                        [
                            "Host",
                            "cdn2.signal.org"
                        ],
                        [
                            "User-Agent",
                            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
                        ]
                    ],
                    "headers": {
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                        "Accept-Language": "en-US;q=0.8,en;q=0.5",
                        "Host": "cdn2.signal.org",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
                    },
                    "method": "GET",
                    "tor": {
                        "exit_ip": null,
                        "exit_name": null,
                        "is_tor": false
                    },
                    "x_transport": "tcp",
                    "url": "https://cdn2.signal.org/"
                },
                "response": {
                    "body": "<?xml version='1.0' encoding='UTF-8'?><Error><Code>AccessDenied</Code><Message>Access denied.</Message></Error>",
                    "body_is_truncated": false,
                    "code": 403,
                    "headers_list": [
                        [
                            "Age",
                            "33"
                        ],
                        [
                            "Alt-Svc",
                            "h3-27=\":443\"; ma=86400, h3-28=\":443\"; ma=86400, h3-29=\":443\"; ma=86400"
                        ],
                        [
                            "Cache-Control",
                            "private, max-age=0"
                        ],
                        [
                            "Cf-Cache-Status",
                            "HIT"
                        ],
                        [
                            "Cf-Ray",
                            "6220c607ba9ec2e0-FRA"
                        ],
                        [
                            "Cf-Request-Id",
                            "08485a18d50000c2e033910000000001"
                        ],
                        [
                            "Content-Length",
                            "111"
                        ],
                        [
                            "Content-Type",
                            "application/xml; charset=UTF-8"
                        ],
                        [
                            "Date",
                            "Mon, 15 Feb 2021 17:33:22 GMT"
                        ],
                        [
                            "Expect-Ct",
                            "max-age=604800, report-uri=\"https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct\""
                        ],
                        [
                            "Expires",
                            "Mon, 15 Feb 2021 17:32:08 GMT"
                        ],
                        [
                            "Server",
                            "cloudflare"
                        ],
                        [
                            "Set-Cookie",
                            "__cfduid=dfc841fb42a90ff05bbca8aa2528f9aa81613410402; expires=Wed, 17-Mar-21 17:33:22 GMT; path=/; domain=.signal.org; HttpOnly; SameSite=Lax; Secure"
                        ],
                        [
                            "X-Guploader-Uploadid",
                            "ABg5-Uy5q7NYviUOk-5vK468Ibyy8hL3hu0tfSgqRmq6qfKaXb2cyMBf4zAZhRIDt5_tNuxVTJsrj1uDLT-XLxuV3g4"
                        ]
                    ],
                    "headers": {
                        "Age": "33",
                        "Alt-Svc": "h3-27=\":443\"; ma=86400, h3-28=\":443\"; ma=86400, h3-29=\":443\"; ma=86400",
                        "Cache-Control": "private, max-age=0",
                        "Cf-Cache-Status": "HIT",
                        "Cf-Ray": "6220c607ba9ec2e0-FRA",
                        "Cf-Request-Id": "08485a18d50000c2e033910000000001",
                        "Content-Length": "111",
                        "Content-Type": "application/xml; charset=UTF-8",
                        "Date": "Mon, 15 Feb 2021 17:33:22 GMT",
                        "Expect-Ct": "max-age=604800, report-uri=\"https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct\"",
                        "Expires": "Mon, 15 Feb 2021 17:32:08 GMT",
                        "Server": "cloudflare",
                        "Set-Cookie": "__cfduid=dfc841fb42a90ff05bbca8aa2528f9aa81613410402; expires=Wed, 17-Mar-21 17:33:22 GMT; path=/; domain=.signal.org; HttpOnly; SameSite=Lax; Secure",
                        "X-Guploader-Uploadid": "ABg5-Uy5q7NYviUOk-5vK468Ibyy8hL3hu0tfSgqRmq6qfKaXb2cyMBf4zAZhRIDt5_tNuxVTJsrj1uDLT-XLxuV3g4"
                    }
                },
                "t": 0.183376502
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
                            "en-US;q=0.8,en;q=0.5"
                        ],
                        [
                            "Host",
                            "cdn.signal.org"
                        ],
                        [
                            "User-Agent",
                            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
                        ]
                    ],
                    "headers": {
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                        "Accept-Language": "en-US;q=0.8,en;q=0.5",
                        "Host": "cdn.signal.org",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
                    },
                    "method": "GET",
                    "tor": {
                        "exit_ip": null,
                        "exit_name": null,
                        "is_tor": false
                    },
                    "x_transport": "tcp",
                    "url": "https://cdn.signal.org/"
                },
                "response": {
                    "body": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<Error><Code>AccessDenied</Code><Message>Access Denied</Message><RequestId>434490AB3620BED4</RequestId><HostId>dCBYVvE1lZDT72gnsjlB4ygasfg3NlF0WgJ6yh1ZDJ2RtVmFJJjmmjy67W64YOI5x5gJQGE33pw=</HostId></Error>",
                    "body_is_truncated": false,
                    "code": 403,
                    "headers_list": [
                        [
                            "Content-Type",
                            "application/xml"
                        ],
                        [
                            "Date",
                            "Mon, 15 Feb 2021 17:33:22 GMT"
                        ],
                        [
                            "Server",
                            "AmazonS3"
                        ],
                        [
                            "Via",
                            "1.1 9e5254d8eec8cbe3c98843660346590d.cloudfront.net (CloudFront)"
                        ],
                        [
                            "X-Amz-Bucket-Region",
                            "us-east-1"
                        ],
                        [
                            "X-Amz-Cf-Id",
                            "Rb5eRyAA-pwTstBGQap4PWgToi8YWeTkB5ptkq2s3DbtXnG0iz2_4w=="
                        ],
                        [
                            "X-Amz-Cf-Pop",
                            "FCO50-C2"
                        ],
                        [
                            "X-Cache",
                            "Error from cloudfront"
                        ]
                    ],
                    "headers": {
                        "Content-Type": "application/xml",
                        "Date": "Mon, 15 Feb 2021 17:33:22 GMT",
                        "Server": "AmazonS3",
                        "Via": "1.1 9e5254d8eec8cbe3c98843660346590d.cloudfront.net (CloudFront)",
                        "X-Amz-Bucket-Region": "us-east-1",
                        "X-Amz-Cf-Id": "Rb5eRyAA-pwTstBGQap4PWgToi8YWeTkB5ptkq2s3DbtXnG0iz2_4w==",
                        "X-Amz-Cf-Pop": "FCO50-C2",
                        "X-Cache": "Error from cloudfront"
                    }
                },
                "t": 0.061873488
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
                            "en-US;q=0.8,en;q=0.5"
                        ],
                        [
                            "Host",
                            "api.directory.signal.org"
                        ],
                        [
                            "User-Agent",
                            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
                        ]
                    ],
                    "headers": {
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                        "Accept-Language": "en-US;q=0.8,en;q=0.5",
                        "Host": "api.directory.signal.org",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
                    },
                    "method": "GET",
                    "tor": {
                        "exit_ip": null,
                        "exit_name": null,
                        "is_tor": false
                    },
                    "x_transport": "tcp",
                    "url": "https://api.directory.signal.org/"
                },
                "response": {
                    "body": "{\"code\":404,\"message\":\"HTTP 404 Not Found\"}",
                    "body_is_truncated": false,
                    "code": 404,
                    "headers_list": [
                        [
                            "Connection",
                            "keep-alive"
                        ],
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
                            "Mon, 15 Feb 2021 17:33:23 GMT"
                        ],
                        [
                            "Set-Cookie",
                            "ApplicationGatewayAffinityCORS=342c9d768cee7dcf78917a3159b94d54; Path=/; SameSite=None; Secure"
                        ],
                        [
                            "Set-Cookie",
                            "ApplicationGatewayAffinity=342c9d768cee7dcf78917a3159b94d54; Path=/"
                        ]
                    ],
                    "headers": {
                        "Connection": "keep-alive",
                        "Content-Length": "43",
                        "Content-Type": "application/json",
                        "Date": "Mon, 15 Feb 2021 17:33:23 GMT",
                        "Set-Cookie": "ApplicationGatewayAffinityCORS=342c9d768cee7dcf78917a3159b94d54; Path=/; SameSite=None; Secure"
                    }
                },
                "t": 6.5202e-05
            }
        ],
        "tcp_connect": [
            {
                "ip": "142.250.180.110",
                "port": 443,
                "status": {
                    "failure": null,
                    "success": true
                },
                "t": 0.024007924
            },
            {
                "ip": "142.250.180.83",
                "port": 443,
                "status": {
                    "failure": null,
                    "success": true
                },
                "t": 0.020983631
            },
            {
                "ip": "104.18.28.74",
                "port": 443,
                "status": {
                    "failure": null,
                    "success": true
                },
                "t": 0.221721016
            },
            {
                "ip": "52.222.133.65",
                "port": 443,
                "status": {
                    "failure": null,
                    "success": true
                },
                "t": 0.075162082
            },
            {
                "ip": "20.62.208.25",
                "port": 443,
                "status": {
                    "failure": null,
                    "success": true
                },
                "t": 0.119333786
            }
        ],
        "tls_handshakes": [
            {
                "cipher_suite": "",
                "failure": "ssl_invalid_hostname",
                "negotiated_protocol": "",
                "no_tls_verify": false,
                "peer_certificates": [
                    {
                        "data": "MIIKUTCCCTmgAwIBAgIRAPYaTUsjP4iRBQAAAACHSSgwDQYJKoZIhvcNAQELBQAwQjELMAkGA1UEBhMCVVMxHjAcBgNVBAoTFUdvb2dsZSBUcnVzdCBTZXJ2aWNlczETMBEGA1UEAxMKR1RTIENBIDFPMTAeFw0yMTAxMjYwODQ2MzRaFw0yMTA0MjAwODQ2MzNaMGYxCzAJBgNVBAYTAlVTMRMwEQYDVQQIEwpDYWxpZm9ybmlhMRYwFAYDVQQHEw1Nb3VudGFpbiBWaWV3MRMwEQYDVQQKEwpHb29nbGUgTExDMRUwEwYDVQQDDAwqLmdvb2dsZS5jb20wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQC76xx0UdZ36/41rZNPfQ/yQ05vsBLUO0d+3uMOhvDlpst+XvIsG6L+vLDgf3RiQRFlei0hKqqLOtWLDc/y0+OmaaC+8ft1zljBYdvQlAYoZrT79Cc5pAIDq7G1OZ7cC4ahDno/n46FHjT/UTUAMYa8cKWBaMPneMIsKvn8nMdZzHkfO2nUd6OEecn90XweMvNmx8De6h5AlIgG3m66hkD/UCSdxn7yJHBQVdHgkfTqzv3sz2YyBQGNi288F1bn541f6khEfYti1MvXRtkky7yLCQNUG6PtvuSU4cKaNvRklHigf5i1nVdGEuH61gAElZIklSiaOVK46UyU4DGtbdWNAgMBAAGjggccMIIHGDAOBgNVHQ8BAf8EBAMCBaAwEwYDVR0lBAwwCgYIKwYBBQUHAwEwDAYDVR0TAQH/BAIwADAdBgNVHQ4EFgQU8zCvllLd3jhBk//+Wdjo40Q+T3gwHwYDVR0jBBgwFoAUmNH4bhDrz5vsYJ8YkBug630J/SswaAYIKwYBBQUHAQEEXDBaMCsGCCsGAQUFBzABhh9odHRwOi8vb2NzcC5wa2kuZ29vZy9ndHMxbzFjb3JlMCsGCCsGAQUFBzAChh9odHRwOi8vcGtpLmdvb2cvZ3NyMi9HVFMxTzEuY3J0MIIE1wYDVR0RBIIEzjCCBMqCDCouZ29vZ2xlLmNvbYINKi5hbmRyb2lkLmNvbYIWKi5hcHBlbmdpbmUuZ29vZ2xlLmNvbYIJKi5iZG4uZGV2ghIqLmNsb3VkLmdvb2dsZS5jb22CGCouY3Jvd2Rzb3VyY2UuZ29vZ2xlLmNvbYIYKi5kYXRhY29tcHV0ZS5nb29nbGUuY29tghMqLmZsYXNoLmFuZHJvaWQuY29tggYqLmcuY2+CDiouZ2NwLmd2dDIuY29tghEqLmdjcGNkbi5ndnQxLmNvbYIKKi5nZ3BodC5jboIOKi5na2VjbmFwcHMuY26CFiouZ29vZ2xlLWFuYWx5dGljcy5jb22CCyouZ29vZ2xlLmNhggsqLmdvb2dsZS5jbIIOKi5nb29nbGUuY28uaW6CDiouZ29vZ2xlLmNvLmpwgg4qLmdvb2dsZS5jby51a4IPKi5nb29nbGUuY29tLmFygg8qLmdvb2dsZS5jb20uYXWCDyouZ29vZ2xlLmNvbS5icoIPKi5nb29nbGUuY29tLmNvgg8qLmdvb2dsZS5jb20ubXiCDyouZ29vZ2xlLmNvbS50coIPKi5nb29nbGUuY29tLnZuggsqLmdvb2dsZS5kZYILKi5nb29nbGUuZXOCCyouZ29vZ2xlLmZyggsqLmdvb2dsZS5odYILKi5nb29nbGUuaXSCCyouZ29vZ2xlLm5sggsqLmdvb2dsZS5wbIILKi5nb29nbGUucHSCEiouZ29vZ2xlYWRhcGlzLmNvbYIPKi5nb29nbGVhcGlzLmNughEqLmdvb2dsZWNuYXBwcy5jboIUKi5nb29nbGVjb21tZXJjZS5jb22CESouZ29vZ2xldmlkZW8uY29tggwqLmdzdGF0aWMuY26CDSouZ3N0YXRpYy5jb22CEiouZ3N0YXRpY2NuYXBwcy5jboIKKi5ndnQxLmNvbYIKKi5ndnQyLmNvbYIUKi5tZXRyaWMuZ3N0YXRpYy5jb22CDCoudXJjaGluLmNvbYIQKi51cmwuZ29vZ2xlLmNvbYITKi53ZWFyLmdrZWNuYXBwcy5jboIWKi55b3V0dWJlLW5vY29va2llLmNvbYINKi55b3V0dWJlLmNvbYIWKi55b3V0dWJlZWR1Y2F0aW9uLmNvbYIRKi55b3V0dWJla2lkcy5jb22CByoueXQuYmWCCyoueXRpbWcuY29tghphbmRyb2lkLmNsaWVudHMuZ29vZ2xlLmNvbYILYW5kcm9pZC5jb22CG2RldmVsb3Blci5hbmRyb2lkLmdvb2dsZS5jboIcZGV2ZWxvcGVycy5hbmRyb2lkLmdvb2dsZS5jboIEZy5jb4IIZ2dwaHQuY26CDGdrZWNuYXBwcy5jboIGZ29vLmdsghRnb29nbGUtYW5hbHl0aWNzLmNvbYIKZ29vZ2xlLmNvbYIPZ29vZ2xlY25hcHBzLmNughJnb29nbGVjb21tZXJjZS5jb22CGHNvdXJjZS5hbmRyb2lkLmdvb2dsZS5jboIKdXJjaGluLmNvbYIKd3d3Lmdvby5nbIIIeW91dHUuYmWCC3lvdXR1YmUuY29tghR5b3V0dWJlZWR1Y2F0aW9uLmNvbYIPeW91dHViZWtpZHMuY29tggV5dC5iZTAhBgNVHSAEGjAYMAgGBmeBDAECAjAMBgorBgEEAdZ5AgUDMDMGA1UdHwQsMCowKKAmoCSGImh0dHA6Ly9jcmwucGtpLmdvb2cvR1RTMU8xY29yZS5jcmwwggEEBgorBgEEAdZ5AgQCBIH1BIHyAPAAdQD2XJQv0XcwIhRUGAgwlFaO400TGTO/3wwvIAvMTvFk4wAAAXc+FnUIAAAEAwBGMEQCIGdSbv2rIqV+utuD7yCg0EXCIc+axvXTFOyKwsFF+NjZAiAkSU6Qe/otVV7n8eXhh3ZWnVapTybYFSOckMH9XtiuKQB3AO7Ale6NcmQPkuPDuRvHEqNpagl7S2oaFDjmR7LL7cX5AAABdz4WdSAAAAQDAEgwRgIhAKa6rv9Tr72J73VUZjAZjIPmrnnn8aGritcAd1awrTc9AiEAqprA7uQp+p2QW4GJf9dxJGNbmTvfLqBrHhEgHx1QzS0wDQYJKoZIhvcNAQELBQADggEBAKqqna2R8ipHXUocrN8RWt80UEcZ/Ez1G2kohcZNeMQfKbikRf+MBi/BHAfHTEEE1Zh8REDJ98noeg/zgNtDaoKIYCL46r54v0cBfDfMtmwlPDRi3J7i5TC5ahRfxbT7bGKDEgkg9Kai7dbeexknVuWv+VPIPILNL5l7S3um/SYuwA0LA+mzHaPARLDQqFSSebILEt+w3L0S7QSknmEQOcAEzMrL8qWcfyufL2ZTeHN/KmlB9LcKHXIkWDpitkIknAZtihxZAuC57w95WldM4Ayw93YzkMVzszEyCRhMvowvdV3/HxM2EEp2N3noShH8oIS8czHrvOHcraU6GzfCjT4=",
                        "format": "base64"
                    }
                ],
                "server_name": "textsecure-service.whispersystems.org",
                "t": 0.061638291,
                "tls_version": ""
            },
            {
                "cipher_suite": "TLS_AES_128_GCM_SHA256",
                "failure": null,
                "negotiated_protocol": "h2",
                "no_tls_verify": false,
                "peer_certificates": [
                    {
                        "data": "MIIEIzCCAwugAwIBAgICECYwDQYJKoZIhvcNAQELBQAwgY0xCzAJBgNVBAYTAlVTMRMwEQYDVQQIDApDYWxpZm9ybmlhMRYwFAYDVQQHDA1TYW4gRnJhbmNpc2NvMR0wGwYDVQQKDBRPcGVuIFdoaXNwZXIgU3lzdGVtczEdMBsGA1UECwwUT3BlbiBXaGlzcGVyIFN5c3RlbXMxEzARBgNVBAMMClRleHRTZWN1cmUwHhcNMTkwNjAxMDAwMDAwWhcNMzAwMTA3MDAyMTA2WjB9MQswCQYDVQQGEwJVUzETMBEGA1UECAwKQ2FsaWZvcm5pYTEdMBsGA1UECgwUT3BlbiBXaGlzcGVyIFN5c3RlbXMxHTAbBgNVBAsMFE9wZW4gV2hpc3BlciBTeXN0ZW1zMRswGQYDVQQDDBJzdG9yYWdlLnNpZ25hbC5vcmcwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCwfI+K4NNgP/1UT61JsJm0B2Fsn+vsfEYri31MkLzMIJIX2gurEiQkaZvrOjvr0t4u20roplJCGdBOTIQ7lA5W+JbuvetjCwQAiqKc16chPzL6SFeIR3/EuHdRqiNy74lE6hOw2wyqiguXucndVxYmgeLUTBDw8NpOAznRhT13/V7SaI7hu1Z78GchiAwjstso8xzaWQq337Rp99mnW0DiwFLxMR7a1fpKsAXOaTs9KBndysOof5RubOZhgaKLTF5NArszXqRHttUT1NtIWVO34TEnV1lCMlWt3Xado63XO/f4XJN2qUGroSOeLXK4HzKuRVksC80H3sZhm4va3DptAgMBAAGjgZswgZgwCQYDVR0TBAIwADAsBglghkgBhvhCAQ0EHxYdT3BlblNTTCBHZW5lcmF0ZWQgQ2VydGlmaWNhdGUwHQYDVR0OBBYEFBYeJP0ZL4FCY340H+apTO7gO2hoMB8GA1UdIwQYMBaAFAGLGPE/+zkZRG6Fhr6UZTKnMjyQMB0GA1UdEQQWMBSCEnN0b3JhZ2Uuc2lnbmFsLm9yZzANBgkqhkiG9w0BAQsFAAOCAQEAnJ3pcm1aFge9ChCnCqOdBBMBjFNBqDc+8/WdzmoopPh/t++vcqE60qFUDfXsu8ecX1rgbOk6U3PRKkqJ4g9V6M+WPeH09vAbNmMSern6JAH+/DCRJRb9202f3noWc5H091mnGM3dTG263jT8iRByjfCejPIzdj6uxjNWGuMopot/MVV1en8kgNbYu1mLeIXYfvzz4GTp4nCNg2b4rH6N/DOgP9KV1c+8nfIlyyNvfeOEp+V60+9gVMJY5A8Jh20YjAHd5rcEfJ9OapoJ3PhnDwjpHKQhQBImbhZhIOHqmODudzYE8WwMEBQn/zR5zO9X36OM0QzXKyemv7pjqw85mw==",
                        "format": "base64"
                    }
                ],
                "server_name": "storage.signal.org",
                "t": 0.059647893,
                "tls_version": "TLSv1.3"
            },
            {
                "cipher_suite": "TLS_AES_128_GCM_SHA256",
                "failure": null,
                "negotiated_protocol": "h2",
                "no_tls_verify": false,
                "peer_certificates": [
                    {
                        "data": "MIIEHTCCAwWgAwIBAgICECwwDQYJKoZIhvcNAQELBQAwgY0xCzAJBgNVBAYTAlVTMRMwEQYDVQQIDApDYWxpZm9ybmlhMRYwFAYDVQQHDA1TYW4gRnJhbmNpc2NvMR0wGwYDVQQKDBRPcGVuIFdoaXNwZXIgU3lzdGVtczEdMBsGA1UECwwUT3BlbiBXaGlzcGVyIFN5c3RlbXMxEzARBgNVBAMMClRleHRTZWN1cmUwHhcNMTkwNjAxMDAwMDAwWhcNMzAwMzE4MTkxMTM2WjB6MQswCQYDVQQGEwJVUzETMBEGA1UECAwKQ2FsaWZvcm5pYTEdMBsGA1UECgwUT3BlbiBXaGlzcGVyIFN5c3RlbXMxHTAbBgNVBAsMFE9wZW4gV2hpc3BlciBTeXN0ZW1zMRgwFgYDVQQDDA9jZG4yLnNpZ25hbC5vcmcwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQC7RvcmiCpeLRMrj3ntVuglVD+EuY9DvaeDRm0MF6/T/No2IGFqCNSxpvK821lmVVZyohWB3YhKmEQLEz31aNAGfwVzRNp477zKYHh0PG//UTqayv6M5n0lPGmunV254plGG8028ZKW+kJRwEPJLPRj6F+1KbvEJLEXSvXF/wLYHoOcWcPNjJtgmWstmMPlANBQ7yZJ+a3IxU9wT40AhLOTtN5LXvfe9w19TUvVG5ZtJQFv66rjcLAHthmYTWPATUzf98uAnkzUXoj8eBthuSGczQ0TKTgCHPT4aCQcns22x99RHTDfhbDz9SYhlCsiEEeEYQm6z2rkd/zRe4mvEZ+PAgMBAAGjgZgwgZUwCQYDVR0TBAIwADAsBglghkgBhvhCAQ0EHxYdT3BlblNTTCBHZW5lcmF0ZWQgQ2VydGlmaWNhdGUwHQYDVR0OBBYEFLD5Cz5EcyGADdxcHQXKLYOyBIriMB8GA1UdIwQYMBaAFAGLGPE/+zkZRG6Fhr6UZTKnMjyQMBoGA1UdEQQTMBGCD2NkbjIuc2lnbmFsLm9yZzANBgkqhkiG9w0BAQsFAAOCAQEAMiI8izFaj6A77xiLb7x4FXqlj4XJaXFioL30YmHTP57CWCuShbFASvYIYIrcMrPI0imi/MojM7DTiW0PV47BAsk9p6JTcjRNmsLr3Ig2SEE5rm9f813RoCx8Bzii9/afMezIuaL0Cjyh+6db+8BTRUdoz+DaaxkvWM/xalMk6APZWoKcXqpJhRRGMa/SgFRprvEG7n6nip86NyneTdWL/6HbDNfDlS2kwDs7ZEK//dt19BuXE6FZYYwWTRFP0L/j1JCT1RO0D5N4EzdmvCqms689AMCQQLamXsFqXBwsxDXSvrHK/KXicPvrCG7dN258NSDUYjwToFFEsc5s5MQq5A==",
                        "format": "base64"
                    }
                ],
                "server_name": "cdn2.signal.org",
                "t": 0.261521176,
                "tls_version": "TLSv1.3"
            },
            {
                "cipher_suite": "TLS_AES_128_GCM_SHA256",
                "failure": null,
                "negotiated_protocol": "h2",
                "no_tls_verify": false,
                "peer_certificates": [
                    {
                        "data": "MIIDoDCCAoigAwIBAgICEBcwDQYJKoZIhvcNAQELBQAwgY0xCzAJBgNVBAYTAlVTMRMwEQYDVQQIDApDYWxpZm9ybmlhMRYwFAYDVQQHDA1TYW4gRnJhbmNpc2NvMR0wGwYDVQQKDBRPcGVuIFdoaXNwZXIgU3lzdGVtczEdMBsGA1UECwwUT3BlbiBXaGlzcGVyIFN5c3RlbXMxEzARBgNVBAMMClRleHRTZWN1cmUwHhcNMTkwMjE1MTczODE3WhcNMjkwMzEyMTgxOTUwWjB5MQswCQYDVQQGEwJVUzETMBEGA1UECAwKQ2FsaWZvcm5pYTEdMBsGA1UECgwUT3BlbiBXaGlzcGVyIFN5c3RlbXMxHTAbBgNVBAsMFE9wZW4gV2hpc3BlciBTeXN0ZW1zMRcwFQYDVQQDDA5jZG4uc2lnbmFsLm9yZzCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAM18LQzkZEfWlg4hw/dBL9paXMIB8No3GZAgAy/09MbfinutJhogqyGsfD9QVwKOcVCvolxWRJxOVHLvfJ+j3OjaizipPSg4tJBcbN+9ZakhzUpPRoghEI4yiKrl0Sqi7vJNILC1JTYvkRytQ9n/4Jbs5Y2RBnRT1TPYTV57UYEJTbpi7gEiAWGj2rth0iCCvOasx+qhZEdPOn1e6lwVwWKHe0IcTRfT2CWMW01KVLcW86+adINJC/1ymCCoUyAve8Qsdf59G5bmObwjQzhxFqFhHY7QFfbJcvl0n1Cn1eglY+a/RyEDs5oux7VcZ8aj6P5GLiya+i08XBOQs3AuHwECAwEAAaMdMBswGQYDVR0RBBIwEIIOY2RuLnNpZ25hbC5vcmcwDQYJKoZIhvcNAQELBQADggEBAG/PlhcSBiL6fGKTGRpaoycPg7hJ9ziHLiB+y0QyB5wqO5derbp7SMXlOZV+SdL63ngqyVoN0iuC4BM7lU8DJithuOT+DkdBUHAdejNgRNl0tgpxiKFhl81NV1bHcDkHXtI6Eg31yWJKn5PkQX5bVICwoe1ebZJdERU+Uc4uf9IUgrJmkWNSNRRVNtXEiyL7WEbG3MlOE7UNzIJWYeBa/F7AWNItLd5fu9hbJvGq/pLUxVuNeSr2mrSxLF/UtUYOvxNSwLpLCNoS7wnv60ZtLmXBCZ8hswk/q79aWHy3ln5ByH72UEQs3psE2qaoOv8CGulVWMPSRA2lUjj3NNE1CfI=",
                        "format": "base64"
                    },
                    {
                        "data": "MIID7zCCAtegAwIBAgIJAIm6LatK5PNiMA0GCSqGSIb3DQEBBQUAMIGNMQswCQYDVQQGEwJVUzETMBEGA1UECAwKQ2FsaWZvcm5pYTEWMBQGA1UEBwwNU2FuIEZyYW5jaXNjbzEdMBsGA1UECgwUT3BlbiBXaGlzcGVyIFN5c3RlbXMxHTAbBgNVBAsMFE9wZW4gV2hpc3BlciBTeXN0ZW1zMRMwEQYDVQQDDApUZXh0U2VjdXJlMB4XDTEzMDMyNTIyMTgzNVoXDTIzMDMyMzIyMTgzNVowgY0xCzAJBgNVBAYTAlVTMRMwEQYDVQQIDApDYWxpZm9ybmlhMRYwFAYDVQQHDA1TYW4gRnJhbmNpc2NvMR0wGwYDVQQKDBRPcGVuIFdoaXNwZXIgU3lzdGVtczEdMBsGA1UECwwUT3BlbiBXaGlzcGVyIFN5c3RlbXMxEzARBgNVBAMMClRleHRTZWN1cmUwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDBSWBpOCBDF0i4q2d4jAXkSXUGpbeWugVPQCjaL6qD9QDOxeW1afvfPo863i6Crq1KDxHpB36EwzVcjwLkFTIMeo7t9s1FQolAt3mErV2U0vie6Ves+yj6grSfxwIDAcdsKmI0a1SQCZlr3Q1tcHAkAKFRxYNawADyps5B+Zmqcgf653TXS5/0IPPQLocLn8GWLwOYNnYfBvILKDMItmZTtEbucdigxEA9mfIvvHADEbteLtVgwBm9R5vVvtwrD6CCxI3pgH7EH7kMP0Od93wLisvn1yhHY7FuYlrkYqdkMvWUrKoASVw4jb69vaeJCUdU+HCoXOSP1PQcL6WenNCHAgMBAAGjUDBOMB0GA1UdDgQWBBQBixjxP/s5GURuhYa+lGUypzI8kDAfBgNVHSMEGDAWgBQBixjxP/s5GURuhYa+lGUypzI8kDAMBgNVHRMEBTADAQH/MA0GCSqGSIb3DQEBBQUAA4IBAQB+Hr4hC56m0LvJAu1RK6NuPDbTMEN7/jMojFHxH4P3XPFfupjR+bkDq0pPOU6JjIxnrD1XD/EVmTTaTVY5iOheyv7UzJOefb2pLOc9qsuvI4fnaESh9bhzln+LXxtCrRPGhkxA1IMIo3J/s2WF/KVYZyciu6b4ubJ91XPAuBNZwImug7/srWvbpk0hq6A6z140WTVSKtJG7EP41kJe/oF4usY5J7LPkxK3LWzMJnb5EIJDmRvyH8pyRwWg6Qm6qiGFaI4nL8QU4La1x2en4DGXRaLMPRwjELNgQPodR38zoCMuA8gHZfZYYoZ7D7Q1wNUiVHcxuFrEeBaYJbLErwLV",
                        "format": "base64"
                    }
                ],
                "server_name": "cdn.signal.org",
                "t": 0.090274688,
                "tls_version": "TLSv1.3"
            },
            {
                "cipher_suite": "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384",
                "failure": null,
                "negotiated_protocol": "http/1.1",
                "no_tls_verify": false,
                "peer_certificates": [
                    {
                        "data": "MIIEMDCCAxigAwIBAgICEDowDQYJKoZIhvcNAQELBQAwgY0xCzAJBgNVBAYTAlVTMRMwEQYDVQQIDApDYWxpZm9ybmlhMRYwFAYDVQQHDA1TYW4gRnJhbmNpc2NvMR0wGwYDVQQKDBRPcGVuIFdoaXNwZXIgU3lzdGVtczEdMBsGA1UECwwUT3BlbiBXaGlzcGVyIFN5c3RlbXMxEzARBgNVBAMMClRleHRTZWN1cmUwHhcNMTkwNjAxMDAwMDAwWhcNMzEwMTA5MDMzNzEwWjCBgzELMAkGA1UEBhMCVVMxEzARBgNVBAgMCkNhbGlmb3JuaWExHTAbBgNVBAoMFE9wZW4gV2hpc3BlciBTeXN0ZW1zMR0wGwYDVQQLDBRPcGVuIFdoaXNwZXIgU3lzdGVtczEhMB8GA1UEAwwYYXBpLmRpcmVjdG9yeS5zaWduYWwub3JnMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAz5QXsh6QPygdgwIY86CbopBAng5zHHknvD3pX3vOBkt7Gd6IlZ+Jle/QFblaqTFPTuU/VX1oT4OIc5ZTNb5g/LvKMTBRzEset9CeTjx5STRcmWRlPeu3AJPZZEOvCH3AN55GOOiF8FQpqoFVIhSUFS17iuRr3iGLA0Khn0Ink0qJouQuBqfrx8AL+r5dfTfEqs4sxpS34rxy5M8z7HrccxbdcBHkNfn/QRLVikmzpFIBhlMcd9C8orobx+9Zv1cTsyl7m95Ma6zm/aAVT1nPfKi9t666kYvuTezkehbOCsPqTuGZipQ8620vWs4o0u6X+t9JJfYaTHHFlAU+GuYzCQIDAQABo4GhMIGeMAkGA1UdEwQCMAAwLAYJYIZIAYb4QgENBB8WHU9wZW5TU0wgR2VuZXJhdGVkIENlcnRpZmljYXRlMB0GA1UdDgQWBBSvJRKESl+1u6wiVs7ju08VUdaFLzAfBgNVHSMEGDAWgBQBixjxP/s5GURuhYa+lGUypzI8kDAjBgNVHREEHDAaghhhcGkuZGlyZWN0b3J5LnNpZ25hbC5vcmcwDQYJKoZIhvcNAQELBQADggEBAFganu/WuRTlcn2NYQPBGjVLtFUmvxZ8Y0U9u3Vg+fj8hXkpC3IN0MlWslmKEIFJTYUJKpUqvmCPuhjvsaUKCsF1ECaydzl6Tt6nQZmc74epLxDCprbClM8iLDZS+0ojUZdF/fGjT16NnoUy1aT2BhpFsIQOZCqM40jf1sHWRSsvnojPu8/NzHWBuRjtHKMJ/I9knakOywrd3htDQdySadU+7uwKRnX/adRpvr3sYi/4cR5sHuf6bAmL6eCBiZ4yTkYTQ0sPjAEYCrC2HsQPfYMdAPPMWuMlxgRDJkYT9y18jb9FXF6xVf7HhPWQZUmeym0sPsdNE2uKBEuo2YZXxrE=",
                        "format": "base64"
                    }
                ],
                "server_name": "api.directory.signal.org",
                "t": 0.741477576,
                "tls_version": "TLSv1.2"
            }
        ],
        "signal_backend_status": "blocked",
        "signal_backend_failure": "ssl_invalid_hostname"
    },
    "test_name": "signal",
    "test_runtime": 0.883808968,
    "test_start_time": "2021-02-15 17:33:22",
    "test_version": "0.2.0"
}
```

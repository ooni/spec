# Specification version number

2021-02-15-001

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

* https://textsecure-service.whispersystems.org
* https://storage.signal.org/
* https://api.directory.signal.org/
* https://cdn.signal.org/
* https://cdn2.signal.org/

The TLS certificate is validated against the custom Signal CA root certificate:
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
    "measurement_start_time": "2021-02-15 16:52:47",
    "probe_asn": "AS30722",
    "probe_cc": "IT",
    "probe_ip": "127.0.0.1",
    "probe_network_name": "Vodafone Italia S.p.A.",
    "report_id": "",
    "resolver_asn": "AS30722",
    "resolver_ip": "91.80.37.82",
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
                "t": 0.000117074
            },
            {
                "failure": null,
                "operation": "http_request_metadata",
                "t": 0.000120257
            },
            {
                "failure": null,
                "operation": "resolve_start",
                "t": 0.000151844
            },
            {
                "failure": null,
                "operation": "resolve_done",
                "t": 0.014726835
            },
            {
                "address": "142.250.180.147:443",
                "failure": null,
                "operation": "connect",
                "proto": "tcp",
                "t": 0.036293429
            },
            {
                "failure": null,
                "operation": "tls_handshake_start",
                "t": 0.036308942
            },
            {
                "failure": null,
                "num_bytes": 288,
                "operation": "write",
                "t": 0.036457185
            },
            {
                "failure": null,
                "num_bytes": 517,
                "operation": "read",
                "t": 0.075489157
            },
            {
                "failure": null,
                "num_bytes": 1029,
                "operation": "read",
                "t": 0.075646495
            },
            {
                "failure": null,
                "num_bytes": 64,
                "operation": "write",
                "t": 0.076218701
            },
            {
                "failure": null,
                "operation": "tls_handshake_done",
                "t": 0.076237046
            },
            {
                "failure": null,
                "num_bytes": 86,
                "operation": "write",
                "t": 0.076325772
            },
            {
                "failure": null,
                "num_bytes": 207,
                "operation": "write",
                "t": 0.07649319
            },
            {
                "failure": null,
                "operation": "http_wrote_headers",
                "t": 0.076495695
            },
            {
                "failure": null,
                "operation": "http_wrote_request",
                "t": 0.076496049
            },
            {
                "failure": null,
                "num_bytes": 93,
                "operation": "read",
                "t": 0.11419255
            },
            {
                "failure": null,
                "num_bytes": 31,
                "operation": "write",
                "t": 0.114231187
            },
            {
                "failure": null,
                "num_bytes": 240,
                "operation": "read",
                "t": 0.201021384
            },
            {
                "failure": null,
                "operation": "http_first_response_byte",
                "t": 0.201062071
            },
            {
                "failure": null,
                "num_bytes": 39,
                "operation": "write",
                "t": 0.201121639
            },
            {
                "failure": null,
                "operation": "http_response_metadata",
                "t": 0.201142295
            },
            {
                "failure": null,
                "operation": "http_response_body_snapshot",
                "t": 0.201155671
            },
            {
                "failure": null,
                "operation": "http_transaction_done",
                "t": 0.201156182
            },
            {
                "failure": null,
                "num_bytes": 24,
                "operation": "write",
                "t": 0.201205288
            },
            {
                "failure": null,
                "operation": "http_transaction_start",
                "t": 6.6564e-05
            },
            {
                "failure": null,
                "operation": "http_request_metadata",
                "t": 7.4319e-05
            },
            {
                "failure": null,
                "operation": "resolve_start",
                "t": 0.000139003
            },
            {
                "failure": null,
                "operation": "resolve_done",
                "t": 0.016812225
            },
            {
                "address": "13.248.212.111:443",
                "failure": null,
                "operation": "connect",
                "proto": "tcp",
                "t": 0.133626978
            },
            {
                "failure": null,
                "operation": "tls_handshake_start",
                "t": 0.133631495
            },
            {
                "failure": null,
                "num_bytes": 307,
                "operation": "write",
                "t": 0.133701144
            },
            {
                "failure": null,
                "num_bytes": 517,
                "operation": "read",
                "t": 0.251622222
            },
            {
                "failure": null,
                "num_bytes": 1961,
                "operation": "read",
                "t": 0.251666211
            },
            {
                "failure": null,
                "num_bytes": 126,
                "operation": "write",
                "t": 0.252517012
            },
            {
                "failure": null,
                "num_bytes": 120,
                "operation": "read",
                "t": 0.368537445
            },
            {
                "failure": null,
                "operation": "tls_handshake_done",
                "t": 0.36859464
            },
            {
                "failure": null,
                "num_bytes": 93,
                "operation": "write",
                "t": 0.368677618
            },
            {
                "failure": null,
                "num_bytes": 227,
                "operation": "write",
                "t": 0.368755579
            },
            {
                "failure": null,
                "operation": "http_wrote_headers",
                "t": 0.368756905
            },
            {
                "failure": null,
                "operation": "http_wrote_request",
                "t": 0.368758133
            },
            {
                "failure": null,
                "num_bytes": 38,
                "operation": "write",
                "t": 0.368793118
            },
            {
                "failure": null,
                "num_bytes": 234,
                "operation": "read",
                "t": 0.485707536
            },
            {
                "failure": null,
                "operation": "http_first_response_byte",
                "t": 0.485747126
            },
            {
                "failure": null,
                "operation": "http_response_metadata",
                "t": 0.485790208
            },
            {
                "failure": null,
                "operation": "http_response_body_snapshot",
                "t": 0.485795867
            },
            {
                "failure": null,
                "operation": "http_transaction_done",
                "t": 0.485796213
            },
            {
                "failure": null,
                "num_bytes": 31,
                "operation": "write",
                "t": 0.485840599
            },
            {
                "failure": null,
                "operation": "http_transaction_start",
                "t": 0.20182473
            },
            {
                "failure": null,
                "operation": "http_request_metadata",
                "t": 0.201851676
            },
            {
                "failure": null,
                "operation": "resolve_start",
                "t": 0.201942808
            },
            {
                "failure": null,
                "operation": "resolve_done",
                "t": 0.219257682
            },
            {
                "address": "52.222.133.51:443",
                "failure": null,
                "operation": "connect",
                "proto": "tcp",
                "t": 0.23065447
            },
            {
                "failure": null,
                "operation": "tls_handshake_start",
                "t": 0.230670325
            },
            {
                "failure": null,
                "num_bytes": 284,
                "operation": "write",
                "t": 0.230793014
            },
            {
                "failure": null,
                "num_bytes": 517,
                "operation": "read",
                "t": 0.242065893
            },
            {
                "failure": null,
                "num_bytes": 1984,
                "operation": "read",
                "t": 0.242238326
            },
            {
                "failure": null,
                "num_bytes": 64,
                "operation": "write",
                "t": 0.242876526
            },
            {
                "failure": null,
                "operation": "tls_handshake_done",
                "t": 0.2428913
            },
            {
                "failure": null,
                "num_bytes": 86,
                "operation": "write",
                "t": 0.242957142
            },
            {
                "failure": null,
                "num_bytes": 204,
                "operation": "write",
                "t": 0.243023959
            },
            {
                "failure": null,
                "operation": "http_wrote_headers",
                "t": 0.243025155
            },
            {
                "failure": null,
                "operation": "http_wrote_request",
                "t": 0.24302549
            },
            {
                "failure": null,
                "num_bytes": 71,
                "operation": "read",
                "t": 0.255296877
            },
            {
                "failure": null,
                "num_bytes": 31,
                "operation": "write",
                "t": 0.25534063
            },
            {
                "failure": null,
                "num_bytes": 550,
                "operation": "read",
                "t": 0.676372647
            },
            {
                "failure": null,
                "operation": "http_first_response_byte",
                "t": 0.676418568
            },
            {
                "failure": null,
                "operation": "http_response_metadata",
                "t": 0.676465003
            },
            {
                "failure": null,
                "operation": "http_response_body_snapshot",
                "t": 0.676470953
            },
            {
                "failure": null,
                "operation": "http_transaction_done",
                "t": 0.676471455
            },
            {
                "failure": null,
                "num_bytes": 24,
                "operation": "write",
                "t": 0.676517443
            },
            {
                "failure": null,
                "operation": "http_transaction_start",
                "t": 0.486272951
            },
            {
                "failure": null,
                "operation": "http_request_metadata",
                "t": 0.486278694
            },
            {
                "failure": null,
                "operation": "resolve_start",
                "t": 0.48633062
            },
            {
                "failure": null,
                "operation": "resolve_done",
                "t": 0.504074913
            },
            {
                "address": "104.18.29.74:443",
                "failure": null,
                "operation": "connect",
                "proto": "tcp",
                "t": 0.542334183
            },
            {
                "failure": null,
                "operation": "tls_handshake_start",
                "t": 0.542341129
            },
            {
                "failure": null,
                "num_bytes": 285,
                "operation": "write",
                "t": 0.54246448
            },
            {
                "failure": null,
                "num_bytes": 517,
                "operation": "read",
                "t": 0.582450066
            },
            {
                "failure": null,
                "num_bytes": 1027,
                "operation": "read",
                "t": 0.582569298
            },
            {
                "failure": null,
                "num_bytes": 64,
                "operation": "write",
                "t": 0.582897662
            },
            {
                "failure": null,
                "operation": "tls_handshake_done",
                "t": 0.58290873
            },
            {
                "failure": null,
                "num_bytes": 86,
                "operation": "write",
                "t": 0.582958866
            },
            {
                "failure": null,
                "num_bytes": 205,
                "operation": "write",
                "t": 0.58300844
            },
            {
                "failure": null,
                "operation": "http_wrote_headers",
                "t": 0.583009304
            },
            {
                "failure": null,
                "operation": "http_wrote_request",
                "t": 0.58300958
            },
            {
                "failure": null,
                "num_bytes": 71,
                "operation": "read",
                "t": 0.619124777
            },
            {
                "failure": null,
                "num_bytes": 31,
                "operation": "write",
                "t": 0.61916891
            },
            {
                "failure": null,
                "num_bytes": 702,
                "operation": "read",
                "t": 0.721718882
            },
            {
                "failure": null,
                "operation": "http_first_response_byte",
                "t": 0.721778072
            },
            {
                "failure": null,
                "operation": "http_response_metadata",
                "t": 0.721835193
            },
            {
                "failure": null,
                "operation": "http_response_body_snapshot",
                "t": 0.721840859
            },
            {
                "failure": null,
                "operation": "http_transaction_done",
                "t": 0.721841291
            },
            {
                "failure": null,
                "num_bytes": 24,
                "operation": "write",
                "t": 0.72188623
            },
            {
                "failure": null,
                "operation": "http_transaction_start",
                "t": 9.4633e-05
            },
            {
                "failure": null,
                "operation": "http_request_metadata",
                "t": 9.7654e-05
            },
            {
                "failure": null,
                "operation": "resolve_start",
                "t": 0.000138964
            },
            {
                "failure": null,
                "operation": "resolve_done",
                "t": 1.03238251
            },
            {
                "address": "20.62.208.25:443",
                "failure": null,
                "operation": "connect",
                "proto": "tcp",
                "t": 1.150872371
            },
            {
                "failure": null,
                "operation": "tls_handshake_start",
                "t": 1.150878958
            },
            {
                "failure": null,
                "num_bytes": 294,
                "operation": "write",
                "t": 1.151035826
            },
            {
                "failure": null,
                "num_bytes": 517,
                "operation": "read",
                "t": 1.27634095
            },
            {
                "failure": null,
                "num_bytes": 1034,
                "operation": "read",
                "t": 1.2763768149999999
            },
            {
                "failure": null,
                "num_bytes": 126,
                "operation": "write",
                "t": 1.276979535
            },
            {
                "failure": null,
                "num_bytes": 51,
                "operation": "read",
                "t": 1.395997701
            },
            {
                "failure": null,
                "operation": "tls_handshake_done",
                "t": 1.39604682
            },
            {
                "failure": null,
                "operation": "http_wrote_headers",
                "t": 1.396145397
            },
            {
                "failure": null,
                "operation": "http_wrote_request",
                "t": 1.396148881
            },
            {
                "failure": null,
                "num_bytes": 320,
                "operation": "write",
                "t": 1.396180446
            },
            {
                "failure": null,
                "num_bytes": 400,
                "operation": "read",
                "t": 1.521891281
            },
            {
                "failure": null,
                "operation": "http_first_response_byte",
                "t": 1.521904575
            },
            {
                "failure": null,
                "operation": "http_response_metadata",
                "t": 1.52195405
            },
            {
                "failure": null,
                "operation": "http_response_body_snapshot",
                "t": 1.52198375
            },
            {
                "failure": null,
                "operation": "http_transaction_done",
                "t": 1.521984254
            },
            {
                "failure": null,
                "num_bytes": 31,
                "operation": "write",
                "t": 1.522036626
            }
        ],
        "queries": [
            {
                "answers": [
                    {
                        "asn": 15169,
                        "as_org_name": "Google LLC",
                        "answer_type": "A",
                        "ipv4": "142.250.180.147",
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
                "t": 0.014726835
            },
            {
                "answers": [
                    {
                        "asn": 15169,
                        "as_org_name": "Google LLC",
                        "answer_type": "AAAA",
                        "ipv6": "2a00:1450:4002:807::2013",
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
                "t": 0.014726835
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
                "hostname": "textsecure-service.whispersystems.org",
                "query_type": "A",
                "resolver_hostname": null,
                "resolver_port": null,
                "resolver_address": "",
                "t": 0.016812225
            },
            {
                "answers": [
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
                        "ipv4": "52.222.133.65",
                        "ttl": null
                    },
                    {
                        "asn": 16509,
                        "as_org_name": "Amazon.com, Inc.",
                        "answer_type": "A",
                        "ipv4": "52.222.133.111",
                        "ttl": null
                    },
                    {
                        "asn": 16509,
                        "as_org_name": "Amazon.com, Inc.",
                        "answer_type": "A",
                        "ipv4": "52.222.133.123",
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
                "t": 0.219257682
            },
            {
                "answers": [
                    {
                        "asn": 16509,
                        "as_org_name": "Amazon.com, Inc.",
                        "answer_type": "AAAA",
                        "ipv6": "2600:9000:201a:7000:1d:4f32:50c0:93a1",
                        "ttl": null
                    },
                    {
                        "asn": 16509,
                        "as_org_name": "Amazon.com, Inc.",
                        "answer_type": "AAAA",
                        "ipv6": "2600:9000:201a:6200:1d:4f32:50c0:93a1",
                        "ttl": null
                    },
                    {
                        "asn": 16509,
                        "as_org_name": "Amazon.com, Inc.",
                        "answer_type": "AAAA",
                        "ipv6": "2600:9000:201a:9400:1d:4f32:50c0:93a1",
                        "ttl": null
                    },
                    {
                        "asn": 16509,
                        "as_org_name": "Amazon.com, Inc.",
                        "answer_type": "AAAA",
                        "ipv6": "2600:9000:201a:3e00:1d:4f32:50c0:93a1",
                        "ttl": null
                    },
                    {
                        "asn": 16509,
                        "as_org_name": "Amazon.com, Inc.",
                        "answer_type": "AAAA",
                        "ipv6": "2600:9000:201a:f200:1d:4f32:50c0:93a1",
                        "ttl": null
                    },
                    {
                        "asn": 16509,
                        "as_org_name": "Amazon.com, Inc.",
                        "answer_type": "AAAA",
                        "ipv6": "2600:9000:201a:e400:1d:4f32:50c0:93a1",
                        "ttl": null
                    },
                    {
                        "asn": 16509,
                        "as_org_name": "Amazon.com, Inc.",
                        "answer_type": "AAAA",
                        "ipv6": "2600:9000:201a:6a00:1d:4f32:50c0:93a1",
                        "ttl": null
                    },
                    {
                        "asn": 16509,
                        "as_org_name": "Amazon.com, Inc.",
                        "answer_type": "AAAA",
                        "ipv6": "2600:9000:201a:7e00:1d:4f32:50c0:93a1",
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
                "t": 0.219257682
            },
            {
                "answers": [
                    {
                        "asn": 13335,
                        "as_org_name": "Cloudflare, Inc.",
                        "answer_type": "A",
                        "ipv4": "104.18.29.74",
                        "ttl": null
                    },
                    {
                        "asn": 13335,
                        "as_org_name": "Cloudflare, Inc.",
                        "answer_type": "A",
                        "ipv4": "104.18.28.74",
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
                "t": 0.504074913
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
                "t": 0.504074913
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
                "t": 1.03238251
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
                            "Mon, 15 Feb 2021 16:52:47 GMT"
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
                        "Date": "Mon, 15 Feb 2021 16:52:47 GMT",
                        "Vary": "Accept-Encoding",
                        "Via": "1.1 google"
                    }
                },
                "t": 0.000117074
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
                            "Mon, 15 Feb 2021 16:52:47 GMT"
                        ],
                        [
                            "X-Signal-Timestamp",
                            "1613407967811"
                        ]
                    ],
                    "headers": {
                        "Content-Length": "43",
                        "Content-Type": "application/json",
                        "Date": "Mon, 15 Feb 2021 16:52:47 GMT",
                        "X-Signal-Timestamp": "1613407967811"
                    }
                },
                "t": 6.6564e-05
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
                    "body": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<Error><Code>AccessDenied</Code><Message>Access Denied</Message><RequestId>E1A469508BB64CFE</RequestId><HostId>7RFZ/2gVaEa5+SdTEfN1pHPeYdwFS7D0yBWfP4ime5sT7VWAV7laQj8uRsMg84NXsekc8sDpzC0=</HostId></Error>",
                    "body_is_truncated": false,
                    "code": 403,
                    "headers_list": [
                        [
                            "Content-Type",
                            "application/xml"
                        ],
                        [
                            "Date",
                            "Mon, 15 Feb 2021 16:52:47 GMT"
                        ],
                        [
                            "Server",
                            "AmazonS3"
                        ],
                        [
                            "Via",
                            "1.1 1441300fb39c0f5aec47f76b881279bb.cloudfront.net (CloudFront)"
                        ],
                        [
                            "X-Amz-Bucket-Region",
                            "us-east-1"
                        ],
                        [
                            "X-Amz-Cf-Id",
                            "EoZanYbPmYR1Bg4eY70LPtYU6tKtpd0j-C5AITFU35VkdLWvwjRyJw=="
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
                        "Date": "Mon, 15 Feb 2021 16:52:47 GMT",
                        "Server": "AmazonS3",
                        "Via": "1.1 1441300fb39c0f5aec47f76b881279bb.cloudfront.net (CloudFront)",
                        "X-Amz-Bucket-Region": "us-east-1",
                        "X-Amz-Cf-Id": "EoZanYbPmYR1Bg4eY70LPtYU6tKtpd0j-C5AITFU35VkdLWvwjRyJw==",
                        "X-Amz-Cf-Pop": "FCO50-C2",
                        "X-Cache": "Error from cloudfront"
                    }
                },
                "t": 0.20182473
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
                            "62208a97ea9b2c3e-FRA"
                        ],
                        [
                            "Cf-Request-Id",
                            "084834f2f100002c3e8f280000000001"
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
                            "Mon, 15 Feb 2021 16:52:48 GMT"
                        ],
                        [
                            "Expect-Ct",
                            "max-age=604800, report-uri=\"https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct\""
                        ],
                        [
                            "Expires",
                            "Mon, 15 Feb 2021 16:49:19 GMT"
                        ],
                        [
                            "Server",
                            "cloudflare"
                        ],
                        [
                            "Set-Cookie",
                            "__cfduid=d9cba064c996b79a1228870a04cfcb1b51613407967; expires=Wed, 17-Mar-21 16:52:47 GMT; path=/; domain=.signal.org; HttpOnly; SameSite=Lax; Secure"
                        ],
                        [
                            "X-Guploader-Uploadid",
                            "ABg5-Uy30ebUdoQBOq-BhCHU-E2sZPQEKSHLkXTobOjYUOuNrBgJ6H6hTyxvkHxfu7f9IKiv706P245f05V50Loj6zQ"
                        ]
                    ],
                    "headers": {
                        "Alt-Svc": "h3-27=\":443\"; ma=86400, h3-28=\":443\"; ma=86400, h3-29=\":443\"; ma=86400",
                        "Cache-Control": "private, max-age=0",
                        "Cf-Cache-Status": "HIT",
                        "Cf-Ray": "62208a97ea9b2c3e-FRA",
                        "Cf-Request-Id": "084834f2f100002c3e8f280000000001",
                        "Content-Length": "111",
                        "Content-Type": "application/xml; charset=UTF-8",
                        "Date": "Mon, 15 Feb 2021 16:52:48 GMT",
                        "Expect-Ct": "max-age=604800, report-uri=\"https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct\"",
                        "Expires": "Mon, 15 Feb 2021 16:49:19 GMT",
                        "Server": "cloudflare",
                        "Set-Cookie": "__cfduid=d9cba064c996b79a1228870a04cfcb1b51613407967; expires=Wed, 17-Mar-21 16:52:47 GMT; path=/; domain=.signal.org; HttpOnly; SameSite=Lax; Secure",
                        "X-Guploader-Uploadid": "ABg5-Uy30ebUdoQBOq-BhCHU-E2sZPQEKSHLkXTobOjYUOuNrBgJ6H6hTyxvkHxfu7f9IKiv706P245f05V50Loj6zQ"
                    }
                },
                "t": 0.486272951
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
                            "Mon, 15 Feb 2021 16:52:48 GMT"
                        ],
                        [
                            "Set-Cookie",
                            "ApplicationGatewayAffinityCORS=f3e96611c67e0ad070ed38a5ceabe076; Path=/; SameSite=None; Secure"
                        ],
                        [
                            "Set-Cookie",
                            "ApplicationGatewayAffinity=f3e96611c67e0ad070ed38a5ceabe076; Path=/"
                        ]
                    ],
                    "headers": {
                        "Connection": "keep-alive",
                        "Content-Length": "43",
                        "Content-Type": "application/json",
                        "Date": "Mon, 15 Feb 2021 16:52:48 GMT",
                        "Set-Cookie": "ApplicationGatewayAffinityCORS=f3e96611c67e0ad070ed38a5ceabe076; Path=/; SameSite=None; Secure"
                    }
                },
                "t": 9.4633e-05
            }
        ],
        "tcp_connect": [
            {
                "ip": "142.250.180.147",
                "port": 443,
                "status": {
                    "failure": null,
                    "success": true
                },
                "t": 0.036293429
            },
            {
                "ip": "13.248.212.111",
                "port": 443,
                "status": {
                    "failure": null,
                    "success": true
                },
                "t": 0.133626978
            },
            {
                "ip": "52.222.133.51",
                "port": 443,
                "status": {
                    "failure": null,
                    "success": true
                },
                "t": 0.23065447
            },
            {
                "ip": "104.18.29.74",
                "port": 443,
                "status": {
                    "failure": null,
                    "success": true
                },
                "t": 0.542334183
            },
            {
                "ip": "20.62.208.25",
                "port": 443,
                "status": {
                    "failure": null,
                    "success": true
                },
                "t": 1.150872371
            }
        ],
        "tls_handshakes": [
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
                "t": 0.076237046,
                "tls_version": "TLSv1.3"
            },
            {
                "cipher_suite": "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256",
                "failure": null,
                "negotiated_protocol": "h2",
                "no_tls_verify": false,
                "peer_certificates": [
                    {
                        "data": "MIID4zCCAsugAwIBAgICEBgwDQYJKoZIhvcNAQELBQAwgY0xCzAJBgNVBAYTAlVTMRMwEQYDVQQIDApDYWxpZm9ybmlhMRYwFAYDVQQHDA1TYW4gRnJhbmNpc2NvMR0wGwYDVQQKDBRPcGVuIFdoaXNwZXIgU3lzdGVtczEdMBsGA1UECwwUT3BlbiBXaGlzcGVyIFN5c3RlbXMxEzARBgNVBAMMClRleHRTZWN1cmUwHhcNMTkwMjE1MTczODE3WhcNMjkwMzEyMTgyMDIwWjCBkDELMAkGA1UEBhMCVVMxEzARBgNVBAgMCkNhbGlmb3JuaWExHTAbBgNVBAoMFE9wZW4gV2hpc3BlciBTeXN0ZW1zMR0wGwYDVQQLDBRPcGVuIFdoaXNwZXIgU3lzdGVtczEuMCwGA1UEAwwldGV4dHNlY3VyZS1zZXJ2aWNlLndoaXNwZXJzeXN0ZW1zLm9yZzCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAKzIEbXRRbfAosvPk4magHWzsHhwOzu7On7EA4xxqViHbN4ox4jl5Lh9mu6nVW0eBvxc9zQKPG0ijgQJN/SV53jFwjqqtr4JYTsHzKs6bgHlYH6sW3XHxePj5JFKSSXWY7lKNASVl5KkSmhaiYItEPExvSoPB9bNwupixZ5Ae0iIE/NYQA6yZXpQTY0dBU0l1q0pQeXzLXqgJetThzSXr6j5soNO2KyRoMBNbI42fPUYvWRCOUfyUNI2fb3qsuZD+QQ7YKxl5hgDBU8oNCNN80sNWjhh5nFEOWGj5lxl1qYTkp3sWJJGYD6cuQDJ1DrSKNbDUWnslIe+wvZfTx9+km0CAwEAAaNIMEYwRAYDVR0RBD0wO4IldGV4dHNlY3VyZS1zZXJ2aWNlLndoaXNwZXJzeXN0ZW1zLm9yZ4ISc2VydmljZS5zaWduYWwub3JnMA0GCSqGSIb3DQEBCwUAA4IBAQApay5HvPcMP+HE2vS3WOxL/ygG1o/q4zcO/VYOfA7q2yiFN2FDF8lEcwEqcDMAz2+hGK/fXi2gaIYq6fp3fL9OtzIrXmUNCB2I9PpuI4jj6xUtERecOXSaHE2C3TI3t7CIcvhbGU1OrJiDLbVFHE8RAetsJJyd2YWuzBwd9U3oWS4ZNzjlwQLTOiJpoApSKmMlQ6OVfgdr6rRTI1ocw+q4/wDxcYEhiLoMljy42A/WrwXzyUMDkcAtZHTjkUAuSLivn434nLcYXalMUIW8sQNLksKTqVH26MKS2t2HRVs4cwDfmtGzmWSLbgRBl/8Oquq5XLLNEUIM31NVcBUFpKhJ",
                        "format": "base64"
                    },
                    {
                        "data": "MIID7zCCAtegAwIBAgIJAIm6LatK5PNiMA0GCSqGSIb3DQEBBQUAMIGNMQswCQYDVQQGEwJVUzETMBEGA1UECAwKQ2FsaWZvcm5pYTEWMBQGA1UEBwwNU2FuIEZyYW5jaXNjbzEdMBsGA1UECgwUT3BlbiBXaGlzcGVyIFN5c3RlbXMxHTAbBgNVBAsMFE9wZW4gV2hpc3BlciBTeXN0ZW1zMRMwEQYDVQQDDApUZXh0U2VjdXJlMB4XDTEzMDMyNTIyMTgzNVoXDTIzMDMyMzIyMTgzNVowgY0xCzAJBgNVBAYTAlVTMRMwEQYDVQQIDApDYWxpZm9ybmlhMRYwFAYDVQQHDA1TYW4gRnJhbmNpc2NvMR0wGwYDVQQKDBRPcGVuIFdoaXNwZXIgU3lzdGVtczEdMBsGA1UECwwUT3BlbiBXaGlzcGVyIFN5c3RlbXMxEzARBgNVBAMMClRleHRTZWN1cmUwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDBSWBpOCBDF0i4q2d4jAXkSXUGpbeWugVPQCjaL6qD9QDOxeW1afvfPo863i6Crq1KDxHpB36EwzVcjwLkFTIMeo7t9s1FQolAt3mErV2U0vie6Ves+yj6grSfxwIDAcdsKmI0a1SQCZlr3Q1tcHAkAKFRxYNawADyps5B+Zmqcgf653TXS5/0IPPQLocLn8GWLwOYNnYfBvILKDMItmZTtEbucdigxEA9mfIvvHADEbteLtVgwBm9R5vVvtwrD6CCxI3pgH7EH7kMP0Od93wLisvn1yhHY7FuYlrkYqdkMvWUrKoASVw4jb69vaeJCUdU+HCoXOSP1PQcL6WenNCHAgMBAAGjUDBOMB0GA1UdDgQWBBQBixjxP/s5GURuhYa+lGUypzI8kDAfBgNVHSMEGDAWgBQBixjxP/s5GURuhYa+lGUypzI8kDAMBgNVHRMEBTADAQH/MA0GCSqGSIb3DQEBBQUAA4IBAQB+Hr4hC56m0LvJAu1RK6NuPDbTMEN7/jMojFHxH4P3XPFfupjR+bkDq0pPOU6JjIxnrD1XD/EVmTTaTVY5iOheyv7UzJOefb2pLOc9qsuvI4fnaESh9bhzln+LXxtCrRPGhkxA1IMIo3J/s2WF/KVYZyciu6b4ubJ91XPAuBNZwImug7/srWvbpk0hq6A6z140WTVSKtJG7EP41kJe/oF4usY5J7LPkxK3LWzMJnb5EIJDmRvyH8pyRwWg6Qm6qiGFaI4nL8QU4La1x2en4DGXRaLMPRwjELNgQPodR38zoCMuA8gHZfZYYoZ7D7Q1wNUiVHcxuFrEeBaYJbLErwLV",
                        "format": "base64"
                    }
                ],
                "server_name": "textsecure-service.whispersystems.org",
                "t": 0.36859464,
                "tls_version": "TLSv1.2"
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
                "t": 0.2428913,
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
                "t": 0.58290873,
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
                "t": 1.39604682,
                "tls_version": "TLSv1.2"
            }
        ],
        "signal_backend_status": "ok",
        "signal_backend_failure": null
    },
    "test_name": "signal",
    "test_runtime": 1.527484045,
    "test_start_time": "2021-02-15 16:52:47",
    "test_version": "0.2.0"
}
```

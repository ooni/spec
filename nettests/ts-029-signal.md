# Specification version number

2023-11-13-001

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

-   https://api.backup.signal.org/
-   https://cdn.signal.org/
-   https://cdn2.signal.org/
-   https://cdn3.signal.org/
-   https://cdsi.signal.org/
-   https://chat.signal.org/
-   https://sfu.voip.signal.org/
-   https://storage.signal.org/
-   https://svr2.signal.org/
-   https://ud-chat.signal.org/
-   https://updates.signal.org/
-   https://updates2.signal.org/

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

```json
{
    "annotations": {
        "architecture": "arm64",
        "engine_name": "ooniprobe-engine",
        "engine_version": "3.20.0-alpha",
        "go_version": "go1.20.11",
        "platform": "macos",
        "vcs_modified": "true",
        "vcs_revision": "5d686b19758084a8752e22d331904baf80b1791c",
        "vcs_time": "2023-11-13T07:24:58Z",
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
    "measurement_start_time": "2023-11-13 07:35:51",
    "probe_asn": "AS3320",
    "probe_cc": "DE",
    "probe_ip": "127.0.0.1",
    "probe_network_name": "Deutsche Telekom AG",
    "report_id": "20231113T073551Z_signal_DE_3320_n1_MYC31bl3sxzN2GDL",
    "resolver_asn": "AS3320",
    "resolver_ip": "109.237.176.80",
    "resolver_network_name": "Deutsche Telekom AG",
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
                "t": 0.000896833
            },
            {
                "failure": null,
                "operation": "resolve_start",
                "t": 0.001054083
            },
            {
                "failure": null,
                "operation": "resolve_done",
                "t": 0.028635875
            },
            {
                "address": "13.32.121.94:443",
                "failure": null,
                "operation": "connect",
                "proto": "tcp",
                "t": 0.072114292
            },
            {
                "failure": null,
                "operation": "tls_handshake_start",
                "t": 0.07213925
            },
            {
                "failure": null,
                "num_bytes": 280,
                "operation": "write",
                "t": 0.072808042
            },
            {
                "failure": null,
                "num_bytes": 576,
                "operation": "read",
                "t": 0.11167775
            },
            {
                "failure": null,
                "num_bytes": 2648,
                "operation": "read",
                "t": 0.111803167
            },
            {
                "failure": null,
                "num_bytes": 64,
                "operation": "write",
                "t": 0.11444075
            },
            {
                "failure": null,
                "operation": "tls_handshake_done",
                "t": 0.114484917
            },
            {
                "failure": null,
                "num_bytes": 86,
                "operation": "write",
                "t": 0.114544417
            },
            {
                "failure": null,
                "num_bytes": 196,
                "operation": "write",
                "t": 0.114640375
            },
            {
                "failure": null,
                "num_bytes": 217,
                "operation": "read",
                "t": 0.138036208
            },
            {
                "failure": null,
                "num_bytes": 31,
                "operation": "write",
                "t": 0.138082708
            },
            {
                "failure": null,
                "num_bytes": 551,
                "operation": "read",
                "t": 0.541370083
            },
            {
                "failure": null,
                "operation": "http_transaction_done",
                "t": 0.541969292
            },
            {
                "failure": null,
                "num_bytes": 24,
                "operation": "write",
                "t": 0.542201625
            },
            {
                "failure": "connection_already_closed",
                "operation": "read",
                "t": 0.542361375
            },
            {
                "failure": null,
                "operation": "http_transaction_start",
                "t": 0.000894333
            },
            {
                "failure": null,
                "operation": "resolve_start",
                "t": 0.000971542
            },
            {
                "failure": null,
                "operation": "resolve_done",
                "t": 0.02212725
            },
            {
                "address": "104.18.37.148:443",
                "failure": null,
                "operation": "connect",
                "proto": "tcp",
                "t": 0.072151042
            },
            {
                "failure": null,
                "operation": "tls_handshake_start",
                "t": 0.072166333
            },
            {
                "failure": null,
                "num_bytes": 281,
                "operation": "write",
                "t": 0.072827833
            },
            {
                "failure": null,
                "num_bytes": 576,
                "operation": "read",
                "t": 0.11386575
            },
            {
                "failure": null,
                "num_bytes": 3095,
                "operation": "read",
                "t": 0.113979625
            },
            {
                "failure": null,
                "num_bytes": 64,
                "operation": "write",
                "t": 0.11733975
            },
            {
                "failure": null,
                "operation": "tls_handshake_done",
                "t": 0.117355583
            },
            {
                "failure": null,
                "num_bytes": 86,
                "operation": "write",
                "t": 0.117388542
            },
            {
                "failure": null,
                "num_bytes": 197,
                "operation": "write",
                "t": 0.117433208
            },
            {
                "failure": null,
                "num_bytes": 71,
                "operation": "read",
                "t": 0.155802
            },
            {
                "failure": null,
                "num_bytes": 31,
                "operation": "write",
                "t": 0.155823167
            },
            {
                "failure": null,
                "num_bytes": 456,
                "operation": "read",
                "t": 0.541307125
            },
            {
                "failure": null,
                "operation": "http_transaction_done",
                "t": 0.54201425
            },
            {
                "failure": null,
                "num_bytes": 24,
                "operation": "write",
                "t": 0.542180625
            },
            {
                "failure": "connection_already_closed",
                "operation": "read",
                "t": 0.54229425
            },
            {
                "failure": null,
                "operation": "http_transaction_start",
                "t": 0.000898
            },
            {
                "failure": null,
                "operation": "resolve_start",
                "t": 0.001048958
            },
            {
                "failure": null,
                "operation": "resolve_done",
                "t": 0.04332925
            },
            {
                "address": "13.32.121.64:443",
                "failure": null,
                "operation": "connect",
                "proto": "tcp",
                "t": 0.072173542
            },
            {
                "failure": null,
                "operation": "tls_handshake_start",
                "t": 0.072241542
            },
            {
                "failure": null,
                "num_bytes": 287,
                "operation": "write",
                "t": 0.072808708
            },
            {
                "failure": null,
                "num_bytes": 576,
                "operation": "read",
                "t": 0.111638375
            },
            {
                "failure": null,
                "num_bytes": 2686,
                "operation": "read",
                "t": 0.111789333
            },
            {
                "failure": null,
                "num_bytes": 64,
                "operation": "write",
                "t": 0.114455833
            },
            {
                "failure": null,
                "operation": "tls_handshake_done",
                "t": 0.114521708
            },
            {
                "failure": null,
                "num_bytes": 86,
                "operation": "write",
                "t": 0.114638292
            },
            {
                "failure": null,
                "num_bytes": 201,
                "operation": "write",
                "t": 0.114734833
            },
            {
                "failure": null,
                "num_bytes": 217,
                "operation": "read",
                "t": 0.136093208
            },
            {
                "failure": null,
                "num_bytes": 31,
                "operation": "write",
                "t": 0.1361245
            },
            {
                "failure": null,
                "num_bytes": 452,
                "operation": "read",
                "t": 0.611803542
            },
            {
                "failure": null,
                "operation": "http_transaction_done",
                "t": 0.612210292
            },
            {
                "failure": null,
                "num_bytes": 24,
                "operation": "write",
                "t": 0.612374333
            },
            {
                "failure": null,
                "operation": "http_transaction_start",
                "t": 0.612681
            },
            {
                "failure": null,
                "operation": "resolve_start",
                "t": 0.612821542
            },
            {
                "failure": null,
                "operation": "resolve_done",
                "t": 0.644540417
            },
            {
                "address": "35.186.192.249:443",
                "failure": null,
                "operation": "connect",
                "proto": "tcp",
                "t": 0.668444042
            },
            {
                "failure": null,
                "operation": "tls_handshake_start",
                "t": 0.668478542
            },
            {
                "failure": null,
                "num_bytes": 285,
                "operation": "write",
                "t": 0.66871125
            },
            {
                "failure": null,
                "num_bytes": 576,
                "operation": "read",
                "t": 0.69441
            },
            {
                "failure": null,
                "num_bytes": 2583,
                "operation": "read",
                "t": 0.694646167
            },
            {
                "failure": null,
                "num_bytes": 64,
                "operation": "write",
                "t": 0.698432833
            },
            {
                "failure": null,
                "operation": "tls_handshake_done",
                "t": 0.698501417
            },
            {
                "failure": null,
                "num_bytes": 86,
                "operation": "write",
                "t": 0.698605125
            },
            {
                "failure": null,
                "num_bytes": 200,
                "operation": "write",
                "t": 0.698739917
            },
            {
                "failure": null,
                "num_bytes": 62,
                "operation": "read",
                "t": 0.721336625
            },
            {
                "failure": null,
                "num_bytes": 31,
                "operation": "write",
                "t": 0.721372708
            },
            {
                "failure": null,
                "num_bytes": 31,
                "operation": "read",
                "t": 0.722357417
            },
            {
                "failure": null,
                "num_bytes": 134,
                "operation": "read",
                "t": 0.737644208
            },
            {
                "failure": null,
                "num_bytes": 39,
                "operation": "write",
                "t": 0.737754083
            },
            {
                "failure": null,
                "operation": "http_transaction_done",
                "t": 0.737829833
            },
            {
                "failure": null,
                "num_bytes": 24,
                "operation": "write",
                "t": 0.737890708
            },
            {
                "failure": "connection_already_closed",
                "operation": "read",
                "t": 0.737938
            },
            {
                "failure": null,
                "operation": "http_transaction_start",
                "t": 0.739746875
            },
            {
                "failure": null,
                "operation": "resolve_start",
                "t": 0.739830792
            },
            {
                "failure": null,
                "operation": "resolve_done",
                "t": 0.741935958
            },
            {
                "address": "172.217.16.179:443",
                "failure": null,
                "operation": "connect",
                "proto": "tcp",
                "t": 0.7645755
            },
            {
                "failure": null,
                "operation": "tls_handshake_start",
                "t": 0.764617792
            },
            {
                "failure": null,
                "num_bytes": 284,
                "operation": "write",
                "t": 0.76480375
            },
            {
                "failure": null,
                "num_bytes": 576,
                "operation": "read",
                "t": 0.803988333
            },
            {
                "failure": null,
                "num_bytes": 2583,
                "operation": "read",
                "t": 0.804132083
            },
            {
                "failure": null,
                "num_bytes": 64,
                "operation": "write",
                "t": 0.807166542
            },
            {
                "failure": null,
                "operation": "tls_handshake_done",
                "t": 0.807194417
            },
            {
                "failure": null,
                "num_bytes": 86,
                "operation": "write",
                "t": 0.807248875
            },
            {
                "failure": null,
                "num_bytes": 199,
                "operation": "write",
                "t": 0.80733075
            },
            {
                "failure": null,
                "num_bytes": 93,
                "operation": "read",
                "t": 0.845701083
            },
            {
                "failure": null,
                "num_bytes": 31,
                "operation": "write",
                "t": 0.845773625
            },
            {
                "failure": null,
                "num_bytes": 240,
                "operation": "read",
                "t": 0.955018958
            },
            {
                "failure": null,
                "operation": "http_transaction_done",
                "t": 0.955164917
            },
            {
                "failure": null,
                "num_bytes": 39,
                "operation": "write",
                "t": 0.955195208
            },
            {
                "failure": null,
                "num_bytes": 24,
                "operation": "write",
                "t": 0.95528775
            },
            {
                "failure": "connection_already_closed",
                "operation": "read",
                "t": 0.95533475
            },
            {
                "failure": null,
                "operation": "http_transaction_start",
                "t": 0.545612958
            },
            {
                "failure": null,
                "operation": "resolve_start",
                "t": 0.545709042
            },
            {
                "failure": null,
                "operation": "resolve_done",
                "t": 0.567583042
            },
            {
                "address": "13.248.212.111:443",
                "failure": null,
                "operation": "connect",
                "proto": "tcp",
                "t": 0.5867585
            },
            {
                "failure": null,
                "operation": "tls_handshake_start",
                "t": 0.58680125
            },
            {
                "failure": null,
                "num_bytes": 281,
                "operation": "write",
                "t": 0.587097292
            },
            {
                "failure": null,
                "num_bytes": 576,
                "operation": "read",
                "t": 0.807190208
            },
            {
                "failure": null,
                "num_bytes": 3073,
                "operation": "read",
                "t": 0.807209042
            },
            {
                "failure": null,
                "num_bytes": 126,
                "operation": "write",
                "t": 0.810844625
            },
            {
                "failure": null,
                "num_bytes": 120,
                "operation": "read",
                "t": 0.9549635
            },
            {
                "failure": null,
                "operation": "tls_handshake_done",
                "t": 0.95505975
            },
            {
                "failure": null,
                "num_bytes": 93,
                "operation": "write",
                "t": 0.955150792
            },
            {
                "failure": null,
                "num_bytes": 204,
                "operation": "write",
                "t": 0.955231833
            },
            {
                "failure": null,
                "num_bytes": 38,
                "operation": "write",
                "t": 0.955252292
            },
            {
                "failure": null,
                "num_bytes": 38,
                "operation": "read",
                "t": 1.072318583
            },
            {
                "failure": null,
                "num_bytes": 196,
                "operation": "read",
                "t": 1.073670083
            },
            {
                "failure": null,
                "operation": "http_transaction_done",
                "t": 1.0739855
            },
            {
                "failure": null,
                "num_bytes": 31,
                "operation": "write",
                "t": 1.074163292
            },
            {
                "failure": "connection_already_closed",
                "operation": "read",
                "t": 1.074307833
            },
            {
                "failure": null,
                "operation": "http_transaction_start",
                "t": 0.545116958
            },
            {
                "failure": null,
                "operation": "resolve_start",
                "t": 0.5452925
            },
            {
                "failure": null,
                "operation": "resolve_done",
                "t": 0.572669667
            },
            {
                "address": "40.122.45.194:443",
                "failure": null,
                "operation": "connect",
                "proto": "tcp",
                "t": 0.717252583
            },
            {
                "failure": null,
                "operation": "tls_handshake_start",
                "t": 0.7172755
            },
            {
                "failure": null,
                "num_bytes": 281,
                "operation": "write",
                "t": 0.717474125
            },
            {
                "failure": null,
                "num_bytes": 576,
                "operation": "read",
                "t": 0.867048375
            },
            {
                "failure": null,
                "num_bytes": 3177,
                "operation": "read",
                "t": 0.867275708
            },
            {
                "failure": null,
                "num_bytes": 80,
                "operation": "write",
                "t": 0.871365458
            },
            {
                "failure": null,
                "operation": "tls_handshake_done",
                "t": 0.87140925
            },
            {
                "failure": null,
                "num_bytes": 86,
                "operation": "write",
                "t": 0.871469625
            },
            {
                "failure": null,
                "num_bytes": 197,
                "operation": "write",
                "t": 0.871541583
            },
            {
                "failure": null,
                "num_bytes": 933,
                "operation": "read",
                "t": 1.097744833
            },
            {
                "failure": null,
                "num_bytes": 31,
                "operation": "write",
                "t": 1.097826542
            },
            {
                "failure": null,
                "operation": "http_transaction_done",
                "t": 1.097984917
            },
            {
                "failure": null,
                "num_bytes": 24,
                "operation": "write",
                "t": 1.098042667
            },
            {
                "failure": "connection_already_closed",
                "operation": "read",
                "t": 1.09809375
            },
            {
                "failure": null,
                "operation": "http_transaction_start",
                "t": 1.099063958
            },
            {
                "failure": null,
                "operation": "resolve_start",
                "t": 1.099151333
            },
            {
                "failure": null,
                "operation": "resolve_done",
                "t": 1.140374208
            },
            {
                "address": "104.18.32.118:443",
                "failure": null,
                "operation": "connect",
                "proto": "tcp",
                "t": 1.168257583
            },
            {
                "failure": null,
                "operation": "tls_handshake_start",
                "t": 1.168281333
            },
            {
                "failure": null,
                "num_bytes": 284,
                "operation": "write",
                "t": 1.1684755
            },
            {
                "failure": null,
                "num_bytes": 576,
                "operation": "read",
                "t": 1.2007908330000001
            },
            {
                "failure": null,
                "num_bytes": 2323,
                "operation": "read",
                "t": 1.200937
            },
            {
                "failure": null,
                "num_bytes": 64,
                "operation": "write",
                "t": 1.201728667
            },
            {
                "failure": null,
                "operation": "tls_handshake_done",
                "t": 1.201748875
            },
            {
                "failure": null,
                "num_bytes": 86,
                "operation": "write",
                "t": 1.201810708
            },
            {
                "failure": null,
                "num_bytes": 199,
                "operation": "write",
                "t": 1.201889708
            },
            {
                "failure": null,
                "num_bytes": 71,
                "operation": "read",
                "t": 1.229760542
            },
            {
                "failure": null,
                "num_bytes": 31,
                "operation": "write",
                "t": 1.229805875
            },
            {
                "failure": null,
                "num_bytes": 511,
                "operation": "read",
                "t": 1.479329375
            },
            {
                "failure": null,
                "operation": "http_transaction_done",
                "t": 1.480029292
            },
            {
                "failure": null,
                "num_bytes": 24,
                "operation": "write",
                "t": 1.4801602919999999
            },
            {
                "failure": "connection_already_closed",
                "operation": "read",
                "t": 1.480238458
            },
            {
                "failure": null,
                "operation": "http_transaction_start",
                "t": 0.957694542
            },
            {
                "failure": null,
                "operation": "resolve_start",
                "t": 0.957790083
            },
            {
                "failure": null,
                "operation": "resolve_done",
                "t": 1.056993292
            },
            {
                "address": "20.104.52.125:443",
                "failure": null,
                "operation": "connect",
                "proto": "tcp",
                "t": 1.180286292
            },
            {
                "failure": null,
                "operation": "tls_handshake_start",
                "t": 1.180326083
            },
            {
                "failure": null,
                "num_bytes": 281,
                "operation": "write",
                "t": 1.180497875
            },
            {
                "failure": null,
                "num_bytes": 576,
                "operation": "read",
                "t": 1.31056025
            },
            {
                "failure": null,
                "num_bytes": 3177,
                "operation": "read",
                "t": 1.311294958
            },
            {
                "failure": null,
                "num_bytes": 80,
                "operation": "write",
                "t": 1.319098083
            },
            {
                "failure": null,
                "operation": "tls_handshake_done",
                "t": 1.319207125
            },
            {
                "failure": null,
                "num_bytes": 86,
                "operation": "write",
                "t": 1.3193134579999999
            },
            {
                "failure": null,
                "num_bytes": 197,
                "operation": "write",
                "t": 1.319427875
            },
            {
                "failure": null,
                "num_bytes": 955,
                "operation": "read",
                "t": 1.479510083
            },
            {
                "failure": null,
                "num_bytes": 31,
                "operation": "write",
                "t": 1.4796236249999999
            },
            {
                "failure": null,
                "operation": "http_transaction_done",
                "t": 1.480366125
            },
            {
                "failure": null,
                "num_bytes": 24,
                "operation": "write",
                "t": 1.480437167
            },
            {
                "failure": "connection_already_closed",
                "operation": "read",
                "t": 1.480490083
            },
            {
                "failure": null,
                "operation": "resolve_start",
                "t": 1.480685083
            },
            {
                "failure": null,
                "operation": "resolve_done",
                "t": 1.482339125
            },
            {
                "failure": null,
                "operation": "http_transaction_start",
                "t": 1.075574542
            },
            {
                "failure": null,
                "operation": "resolve_start",
                "t": 1.075744542
            },
            {
                "failure": null,
                "operation": "resolve_done",
                "t": 1.103160708
            },
            {
                "address": "13.248.212.111:443",
                "failure": null,
                "operation": "connect",
                "proto": "tcp",
                "t": 1.122808292
            },
            {
                "failure": null,
                "operation": "tls_handshake_start",
                "t": 1.122846417
            },
            {
                "failure": null,
                "num_bytes": 284,
                "operation": "write",
                "t": 1.12313
            },
            {
                "failure": null,
                "num_bytes": 576,
                "operation": "read",
                "t": 1.344076833
            },
            {
                "failure": null,
                "num_bytes": 3077,
                "operation": "read",
                "t": 1.344116333
            },
            {
                "failure": null,
                "num_bytes": 126,
                "operation": "write",
                "t": 1.348421917
            },
            {
                "failure": null,
                "num_bytes": 120,
                "operation": "read",
                "t": 1.479388625
            },
            {
                "failure": null,
                "operation": "tls_handshake_done",
                "t": 1.4795880829999999
            },
            {
                "failure": null,
                "num_bytes": 93,
                "operation": "write",
                "t": 1.479757917
            },
            {
                "failure": null,
                "num_bytes": 206,
                "operation": "write",
                "t": 1.480188542
            },
            {
                "failure": null,
                "num_bytes": 38,
                "operation": "write",
                "t": 1.4802255
            },
            {
                "failure": null,
                "num_bytes": 38,
                "operation": "read",
                "t": 1.598446542
            },
            {
                "failure": null,
                "num_bytes": 196,
                "operation": "read",
                "t": 1.605605
            },
            {
                "failure": null,
                "operation": "http_transaction_done",
                "t": 1.605710958
            },
            {
                "failure": null,
                "num_bytes": 31,
                "operation": "write",
                "t": 1.60577375
            },
            {
                "failure": "connection_already_closed",
                "operation": "read",
                "t": 1.6058154999999998
            },
            {
                "failure": null,
                "operation": "http_transaction_start",
                "t": 1.480573792
            },
            {
                "failure": null,
                "operation": "resolve_start",
                "t": 1.480761083
            },
            {
                "failure": null,
                "operation": "resolve_done",
                "t": 1.5107087080000001
            },
            {
                "address": "104.18.43.97:443",
                "failure": null,
                "operation": "connect",
                "proto": "tcp",
                "t": 1.529726625
            },
            {
                "failure": null,
                "operation": "tls_handshake_start",
                "t": 1.529766917
            },
            {
                "failure": null,
                "num_bytes": 285,
                "operation": "write",
                "t": 1.5300176250000002
            },
            {
                "failure": null,
                "num_bytes": 576,
                "operation": "read",
                "t": 1.577362292
            },
            {
                "failure": null,
                "num_bytes": 3099,
                "operation": "read",
                "t": 1.57752475
            },
            {
                "failure": null,
                "num_bytes": 64,
                "operation": "write",
                "t": 1.582037417
            },
            {
                "failure": null,
                "operation": "tls_handshake_done",
                "t": 1.582086167
            },
            {
                "failure": null,
                "num_bytes": 86,
                "operation": "write",
                "t": 1.58215025
            },
            {
                "failure": null,
                "num_bytes": 200,
                "operation": "write",
                "t": 1.582235792
            },
            {
                "failure": null,
                "num_bytes": 71,
                "operation": "read",
                "t": 1.600906875
            },
            {
                "failure": null,
                "num_bytes": 31,
                "operation": "write",
                "t": 1.600941167
            },
            {
                "failure": null,
                "num_bytes": 511,
                "operation": "read",
                "t": 1.616829542
            },
            {
                "failure": null,
                "operation": "http_transaction_done",
                "t": 1.616991917
            },
            {
                "failure": null,
                "num_bytes": 24,
                "operation": "write",
                "t": 1.617042917
            },
            {
                "failure": "connection_already_closed",
                "operation": "read",
                "t": 1.6170819170000001
            }
        ],
        "queries": [
            {
                "answers": [
                    {
                        "asn": 16509,
                        "as_org_name": "Amazon.com, Inc.",
                        "answer_type": "A",
                        "ipv4": "13.32.121.94",
                        "ttl": null
                    },
                    {
                        "asn": 16509,
                        "as_org_name": "Amazon.com, Inc.",
                        "answer_type": "A",
                        "ipv4": "13.32.121.78",
                        "ttl": null
                    },
                    {
                        "asn": 16509,
                        "as_org_name": "Amazon.com, Inc.",
                        "answer_type": "A",
                        "ipv4": "13.32.121.104",
                        "ttl": null
                    },
                    {
                        "asn": 16509,
                        "as_org_name": "Amazon.com, Inc.",
                        "answer_type": "A",
                        "ipv4": "13.32.121.14",
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
                "t": 0.028635875,
                "tags": null
            },
            {
                "answers": [
                    {
                        "asn": 16509,
                        "as_org_name": "Amazon.com, Inc.",
                        "answer_type": "AAAA",
                        "ipv6": "2600:9000:236e:4400:1d:4f32:50c0:93a1",
                        "ttl": null
                    },
                    {
                        "asn": 16509,
                        "as_org_name": "Amazon.com, Inc.",
                        "answer_type": "AAAA",
                        "ipv6": "2600:9000:236e:c200:1d:4f32:50c0:93a1",
                        "ttl": null
                    },
                    {
                        "asn": 16509,
                        "as_org_name": "Amazon.com, Inc.",
                        "answer_type": "AAAA",
                        "ipv6": "2600:9000:2240:1600:1d:4f32:50c0:93a1",
                        "ttl": null
                    },
                    {
                        "asn": 16509,
                        "as_org_name": "Amazon.com, Inc.",
                        "answer_type": "AAAA",
                        "ipv6": "2600:9000:236e:6e00:1d:4f32:50c0:93a1",
                        "ttl": null
                    },
                    {
                        "asn": 16509,
                        "as_org_name": "Amazon.com, Inc.",
                        "answer_type": "AAAA",
                        "ipv6": "2600:9000:2240:0:1d:4f32:50c0:93a1",
                        "ttl": null
                    },
                    {
                        "asn": 16509,
                        "as_org_name": "Amazon.com, Inc.",
                        "answer_type": "AAAA",
                        "ipv6": "2600:9000:2240:9800:1d:4f32:50c0:93a1",
                        "ttl": null
                    },
                    {
                        "asn": 16509,
                        "as_org_name": "Amazon.com, Inc.",
                        "answer_type": "AAAA",
                        "ipv6": "2600:9000:2240:c00:1d:4f32:50c0:93a1",
                        "ttl": null
                    },
                    {
                        "asn": 16509,
                        "as_org_name": "Amazon.com, Inc.",
                        "answer_type": "AAAA",
                        "ipv6": "2600:9000:2240:d800:1d:4f32:50c0:93a1",
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
                "t": 0.028635875,
                "tags": null
            },
            {
                "answers": [
                    {
                        "asn": 13335,
                        "as_org_name": "Cloudflare Inc",
                        "answer_type": "A",
                        "ipv4": "104.18.37.148",
                        "ttl": null
                    },
                    {
                        "asn": 13335,
                        "as_org_name": "Cloudflare Inc",
                        "answer_type": "A",
                        "ipv4": "172.64.150.108",
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
                "t": 0.02212725,
                "tags": null
            },
            {
                "answers": [
                    {
                        "asn": 13335,
                        "as_org_name": "Cloudflare Inc",
                        "answer_type": "AAAA",
                        "ipv6": "2606:4700:4400::6812:2594",
                        "ttl": null
                    },
                    {
                        "asn": 13335,
                        "as_org_name": "Cloudflare Inc",
                        "answer_type": "AAAA",
                        "ipv6": "2606:4700:4400::ac40:966c",
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
                "t": 0.02212725,
                "tags": null
            },
            {
                "answers": [
                    {
                        "asn": 16509,
                        "as_org_name": "Amazon.com, Inc.",
                        "answer_type": "A",
                        "ipv4": "13.32.121.64",
                        "ttl": null
                    },
                    {
                        "asn": 16509,
                        "as_org_name": "Amazon.com, Inc.",
                        "answer_type": "A",
                        "ipv4": "13.32.121.50",
                        "ttl": null
                    },
                    {
                        "asn": 16509,
                        "as_org_name": "Amazon.com, Inc.",
                        "answer_type": "A",
                        "ipv4": "13.32.121.32",
                        "ttl": null
                    },
                    {
                        "asn": 16509,
                        "as_org_name": "Amazon.com, Inc.",
                        "answer_type": "A",
                        "ipv4": "13.32.121.121",
                        "ttl": null
                    }
                ],
                "engine": "system",
                "failure": null,
                "hostname": "api.backup.signal.org",
                "query_type": "A",
                "resolver_hostname": null,
                "resolver_port": null,
                "resolver_address": "",
                "t": 0.04332925,
                "tags": null
            },
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
                "t": 0.644540417,
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
                "t": 0.644540417,
                "tags": null
            },
            {
                "answers": [
                    {
                        "asn": 15169,
                        "as_org_name": "Google LLC",
                        "answer_type": "A",
                        "ipv4": "172.217.16.179",
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
                "t": 0.741935958,
                "tags": null
            },
            {
                "answers": [
                    {
                        "asn": 15169,
                        "as_org_name": "Google LLC",
                        "answer_type": "AAAA",
                        "ipv6": "2a00:1450:4016:809::2013",
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
                "t": 0.741935958,
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
                "t": 0.567583042,
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
                "t": 0.567583042,
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
                "t": 0.572669667,
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
                "t": 0.572669667,
                "tags": null
            },
            {
                "answers": [
                    {
                        "asn": 13335,
                        "as_org_name": "Cloudflare Inc",
                        "answer_type": "A",
                        "ipv4": "104.18.32.118",
                        "ttl": null
                    },
                    {
                        "asn": 13335,
                        "as_org_name": "Cloudflare Inc",
                        "answer_type": "A",
                        "ipv4": "172.64.155.138",
                        "ttl": null
                    }
                ],
                "engine": "system",
                "failure": null,
                "hostname": "updates.signal.org",
                "query_type": "A",
                "resolver_hostname": null,
                "resolver_port": null,
                "resolver_address": "",
                "t": 1.140374208,
                "tags": null
            },
            {
                "answers": [
                    {
                        "asn": 13335,
                        "as_org_name": "Cloudflare Inc",
                        "answer_type": "AAAA",
                        "ipv6": "2606:4700:4400::6812:2076",
                        "ttl": null
                    },
                    {
                        "asn": 13335,
                        "as_org_name": "Cloudflare Inc",
                        "answer_type": "AAAA",
                        "ipv6": "2606:4700:4400::ac40:9b8a",
                        "ttl": null
                    }
                ],
                "engine": "system",
                "failure": null,
                "hostname": "updates.signal.org",
                "query_type": "AAAA",
                "resolver_hostname": null,
                "resolver_port": null,
                "resolver_address": "",
                "t": 1.140374208,
                "tags": null
            },
            {
                "answers": [
                    {
                        "asn": 8075,
                        "as_org_name": "Microsoft Corporation",
                        "answer_type": "A",
                        "ipv4": "20.104.52.125",
                        "ttl": null
                    }
                ],
                "engine": "system",
                "failure": null,
                "hostname": "svr2.signal.org",
                "query_type": "A",
                "resolver_hostname": null,
                "resolver_port": null,
                "resolver_address": "",
                "t": 1.056993292,
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
                "t": 1.482339125,
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
                "hostname": "ud-chat.signal.org",
                "query_type": "A",
                "resolver_hostname": null,
                "resolver_port": null,
                "resolver_address": "",
                "t": 1.103160708,
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
                "hostname": "ud-chat.signal.org",
                "query_type": "AAAA",
                "resolver_hostname": null,
                "resolver_port": null,
                "resolver_address": "",
                "t": 1.103160708,
                "tags": null
            },
            {
                "answers": [
                    {
                        "asn": 13335,
                        "as_org_name": "Cloudflare Inc",
                        "answer_type": "A",
                        "ipv4": "104.18.43.97",
                        "ttl": null
                    },
                    {
                        "asn": 13335,
                        "as_org_name": "Cloudflare Inc",
                        "answer_type": "A",
                        "ipv4": "172.64.144.159",
                        "ttl": null
                    }
                ],
                "engine": "system",
                "failure": null,
                "hostname": "updates2.signal.org",
                "query_type": "A",
                "resolver_hostname": null,
                "resolver_port": null,
                "resolver_address": "",
                "t": 1.5107087080000001,
                "tags": null
            },
            {
                "answers": [
                    {
                        "asn": 13335,
                        "as_org_name": "Cloudflare Inc",
                        "answer_type": "AAAA",
                        "ipv6": "2606:4700:4400::ac40:909f",
                        "ttl": null
                    },
                    {
                        "asn": 13335,
                        "as_org_name": "Cloudflare Inc",
                        "answer_type": "AAAA",
                        "ipv6": "2606:4700:4400::6812:2b61",
                        "ttl": null
                    }
                ],
                "engine": "system",
                "failure": null,
                "hostname": "updates2.signal.org",
                "query_type": "AAAA",
                "resolver_hostname": null,
                "resolver_port": null,
                "resolver_address": "",
                "t": 1.5107087080000001,
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
                        ["Accept-Language", "en-US,en;q=0.9"],
                        ["Host", "cdn.signal.org"],
                        [
                            "User-Agent",
                            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/[scrubbed] Safari/537.36"
                        ]
                    ],
                    "headers": {
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                        "Accept-Language": "en-US,en;q=0.9",
                        "Host": "cdn.signal.org",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/[scrubbed] Safari/537.36"
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
                    "body": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<Error><Code>AccessDenied</Code><Message>Access Denied</Message><RequestId>7W612PKWKAZ9PZQW</RequestId><HostId>QX6HpbUKp86+da4flVnIjAEJ8ORuLtFMVbrvrs+ef4H7G58sDqk0esS+9+mhqa3a9VGn2QfFbWE=</HostId></Error>",
                    "body_is_truncated": false,
                    "code": 403,
                    "headers_list": [
                        ["Content-Type", "application/xml"],
                        ["Date", "Mon, 13 Nov 2023 07:35:50 GMT"],
                        ["Server", "AmazonS3"],
                        [
                            "Via",
                            "1.1 9ef1b108656dc6d0707b168b862883dc.cloudfront.net (CloudFront)"
                        ],
                        ["X-Amz-Bucket-Region", "us-east-1"],
                        [
                            "X-Amz-Cf-Id",
                            "HdkUgQG1TObJZVyack8f6rXkCXcKk1wViyINA-zQZW4jZ1xB3a79Zg=="
                        ],
                        ["X-Amz-Cf-Pop", "FRA60-P1"],
                        ["X-Cache", "Error from cloudfront"]
                    ],
                    "headers": {
                        "Content-Type": "application/xml",
                        "Date": "Mon, 13 Nov 2023 07:35:50 GMT",
                        "Server": "AmazonS3",
                        "Via": "1.1 9ef1b108656dc6d0707b168b862883dc.cloudfront.net (CloudFront)",
                        "X-Amz-Bucket-Region": "us-east-1",
                        "X-Amz-Cf-Id": "HdkUgQG1TObJZVyack8f6rXkCXcKk1wViyINA-zQZW4jZ1xB3a79Zg==",
                        "X-Amz-Cf-Pop": "FRA60-P1",
                        "X-Cache": "Error from cloudfront"
                    }
                },
                "t": 0.541969292,
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
                        ["Accept-Language", "en-US,en;q=0.9"],
                        ["Host", "cdn2.signal.org"],
                        [
                            "User-Agent",
                            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/[scrubbed] Safari/537.36"
                        ]
                    ],
                    "headers": {
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                        "Accept-Language": "en-US,en;q=0.9",
                        "Host": "cdn2.signal.org",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/[scrubbed] Safari/537.36"
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
                        ["Alt-Svc", "h3=\":443\"; ma=86400"],
                        ["Cache-Control", "private, max-age=0"],
                        ["Cf-Cache-Status", "MISS"],
                        ["Cf-Ray", "8255571b7ed665cf-FRA"],
                        ["Content-Length", "111"],
                        ["Content-Type", "application/xml; charset=UTF-8"],
                        ["Date", "Mon, 13 Nov 2023 07:35:50 GMT"],
                        ["Expires", "Mon, 13 Nov 2023 07:35:50 GMT"],
                        ["Server", "cloudflare"],
                        [
                            "X-Guploader-Uploadid",
                            "ABPtcPoeFjaBrFQHlzZzimqUWrQJlT9sYUaliRGOr6SGjEjjsq_Mig4HdpKYMcCpmdMS7aAX3i1H-cm5Ug"
                        ]
                    ],
                    "headers": {
                        "Alt-Svc": "h3=\":443\"; ma=86400",
                        "Cache-Control": "private, max-age=0",
                        "Cf-Cache-Status": "MISS",
                        "Cf-Ray": "8255571b7ed665cf-FRA",
                        "Content-Length": "111",
                        "Content-Type": "application/xml; charset=UTF-8",
                        "Date": "Mon, 13 Nov 2023 07:35:50 GMT",
                        "Expires": "Mon, 13 Nov 2023 07:35:50 GMT",
                        "Server": "cloudflare",
                        "X-Guploader-Uploadid": "ABPtcPoeFjaBrFQHlzZzimqUWrQJlT9sYUaliRGOr6SGjEjjsq_Mig4HdpKYMcCpmdMS7aAX3i1H-cm5Ug"
                    }
                },
                "t": 0.54201425,
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
                        ["Accept-Language", "en-US,en;q=0.9"],
                        ["Host", "api.backup.signal.org"],
                        [
                            "User-Agent",
                            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/[scrubbed] Safari/537.36"
                        ]
                    ],
                    "headers": {
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                        "Accept-Language": "en-US,en;q=0.9",
                        "Host": "api.backup.signal.org",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/[scrubbed] Safari/537.36"
                    },
                    "method": "GET",
                    "tor": {
                        "exit_ip": null,
                        "exit_name": null,
                        "is_tor": false
                    },
                    "x_transport": "tcp",
                    "url": "https://api.backup.signal.org/"
                },
                "response": {
                    "body": "<!DOCTYPE html>\n<html><body>404</body></html>\n",
                    "body_is_truncated": false,
                    "code": 404,
                    "headers_list": [
                        ["Accept-Ranges", "bytes"],
                        ["Age", "2253"],
                        ["Content-Length", "46"],
                        ["Content-Type", "application/octet-stream"],
                        ["Date", "Mon, 13 Nov 2023 07:21:11 GMT"],
                        ["Etag", "\"af3cf70b4fccdb496da0f8d19bf68c78\""],
                        ["Last-Modified", "Fri, 13 Oct 2023 16:24:21 GMT"],
                        ["Server", "AmazonS3"],
                        [
                            "Via",
                            "1.1 857b0dca772798c338c78a1be69c955c.cloudfront.net (CloudFront)"
                        ],
                        [
                            "X-Amz-Cf-Id",
                            "EjNXs5W16EyTfgneXBsB0seMLD0oGP0c3KVx9TzLXBH-2itwyo87cQ=="
                        ],
                        ["X-Amz-Cf-Pop", "FRA60-P1"],
                        ["X-Amz-Server-Side-Encryption", "AES256"],
                        ["X-Cache", "Error from cloudfront"]
                    ],
                    "headers": {
                        "Accept-Ranges": "bytes",
                        "Age": "2253",
                        "Content-Length": "46",
                        "Content-Type": "application/octet-stream",
                        "Date": "Mon, 13 Nov 2023 07:21:11 GMT",
                        "Etag": "\"af3cf70b4fccdb496da0f8d19bf68c78\"",
                        "Last-Modified": "Fri, 13 Oct 2023 16:24:21 GMT",
                        "Server": "AmazonS3",
                        "Via": "1.1 857b0dca772798c338c78a1be69c955c.cloudfront.net (CloudFront)",
                        "X-Amz-Cf-Id": "EjNXs5W16EyTfgneXBsB0seMLD0oGP0c3KVx9TzLXBH-2itwyo87cQ==",
                        "X-Amz-Cf-Pop": "FRA60-P1",
                        "X-Amz-Server-Side-Encryption": "AES256",
                        "X-Cache": "Error from cloudfront"
                    }
                },
                "t": 0.612210292,
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
                        ["Accept-Language", "en-US,en;q=0.9"],
                        ["Host", "sfu.voip.signal.org"],
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
                        ["Content-Length", "0"],
                        ["Date", "Mon, 13 Nov 2023 07:35:50 GMT"],
                        ["Via", "1.1 google"]
                    ],
                    "headers": {
                        "Alt-Svc": "h3=\":443\"; ma=2592000,h3-29=\":443\"; ma=2592000",
                        "Content-Length": "0",
                        "Date": "Mon, 13 Nov 2023 07:35:50 GMT",
                        "Via": "1.1 google"
                    }
                },
                "t": 0.737829833,
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
                        ["Accept-Language", "en-US,en;q=0.9"],
                        ["Host", "storage.signal.org"],
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
                        ["Content-Length", "43"],
                        ["Content-Type", "application/json"],
                        ["Date", "Mon, 13 Nov 2023 07:35:51 GMT"],
                        ["Vary", "Accept-Encoding"],
                        ["Via", "1.1 google"]
                    ],
                    "headers": {
                        "Content-Length": "43",
                        "Content-Type": "application/json",
                        "Date": "Mon, 13 Nov 2023 07:35:51 GMT",
                        "Vary": "Accept-Encoding",
                        "Via": "1.1 google"
                    }
                },
                "t": 0.955164917,
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
                        ["Accept-Language", "en-US,en;q=0.9"],
                        ["Host", "chat.signal.org"],
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
                        ["Content-Length", "43"],
                        ["Content-Type", "application/json"],
                        ["Date", "Mon, 13 Nov 2023 07:35:51 GMT"],
                        ["X-Signal-Timestamp", "1699860951194"]
                    ],
                    "headers": {
                        "Content-Length": "43",
                        "Content-Type": "application/json",
                        "Date": "Mon, 13 Nov 2023 07:35:51 GMT",
                        "X-Signal-Timestamp": "1699860951194"
                    }
                },
                "t": 1.0739855,
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
                        ["Accept-Language", "en-US,en;q=0.9"],
                        ["Host", "cdsi.signal.org"],
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
                        ["Content-Length", "548"],
                        ["Content-Type", "text/html"],
                        ["Date", "Mon, 13 Nov 2023 07:35:51 GMT"],
                        [
                            "Strict-Transport-Security",
                            "max-age=15724800; includeSubDomains"
                        ]
                    ],
                    "headers": {
                        "Content-Length": "548",
                        "Content-Type": "text/html",
                        "Date": "Mon, 13 Nov 2023 07:35:51 GMT",
                        "Strict-Transport-Security": "max-age=15724800; includeSubDomains"
                    }
                },
                "t": 1.097984917,
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
                        ["Accept-Language", "en-US,en;q=0.9"],
                        ["Host", "updates.signal.org"],
                        [
                            "User-Agent",
                            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/[scrubbed] Safari/537.36"
                        ]
                    ],
                    "headers": {
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                        "Accept-Language": "en-US,en;q=0.9",
                        "Host": "updates.signal.org",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/[scrubbed] Safari/537.36"
                    },
                    "method": "GET",
                    "tor": {
                        "exit_ip": null,
                        "exit_name": null,
                        "is_tor": false
                    },
                    "x_transport": "tcp",
                    "url": "https://updates.signal.org/"
                },
                "response": {
                    "body": "",
                    "body_is_truncated": false,
                    "code": 200,
                    "headers_list": [
                        ["Accept-Ranges", "bytes"],
                        ["Alt-Svc", "h3=\":443\"; ma=86400"],
                        ["Cache-Control", "public, max-age=300"],
                        ["Cf-Cache-Status", "MISS"],
                        ["Cf-Ray", "8255572238d82be4-FRA"],
                        ["Content-Length", "0"],
                        ["Content-Type", "inode/x-empty"],
                        ["Date", "Mon, 13 Nov 2023 07:35:51 GMT"],
                        ["Etag", "\"d41d8cd98f00b204e9800998ecf8427e\""],
                        ["Expires", "Mon, 13 Nov 2023 07:40:51 GMT"],
                        ["Last-Modified", "Tue, 28 Feb 2017 07:00:06 GMT"],
                        ["Server", "cloudflare"],
                        [
                            "Via",
                            "1.1 21da0a66bafe2c8de8be4a4d8039346a.cloudfront.net (CloudFront)"
                        ],
                        [
                            "X-Amz-Cf-Id",
                            "XC5WNFb7pf2C6oUUG4FgA6Q7hIQ-bd9t9hxwSREB6F1kLe04uxOa-w=="
                        ],
                        ["X-Amz-Cf-Pop", "FRA6-C1"],
                        [
                            "X-Amz-Meta-S3cmd-Attrs",
                            "uid:1000/gname:moxie/uname:moxie/gid:1000/mode:33204/mtime:1488265189/atime:1488265189/md5:d41d8cd98f00b204e9800998ecf8427e/ctime:1488265189"
                        ],
                        ["X-Cache", "RefreshHit from cloudfront"]
                    ],
                    "headers": {
                        "Accept-Ranges": "bytes",
                        "Alt-Svc": "h3=\":443\"; ma=86400",
                        "Cache-Control": "public, max-age=300",
                        "Cf-Cache-Status": "MISS",
                        "Cf-Ray": "8255572238d82be4-FRA",
                        "Content-Length": "0",
                        "Content-Type": "inode/x-empty",
                        "Date": "Mon, 13 Nov 2023 07:35:51 GMT",
                        "Etag": "\"d41d8cd98f00b204e9800998ecf8427e\"",
                        "Expires": "Mon, 13 Nov 2023 07:40:51 GMT",
                        "Last-Modified": "Tue, 28 Feb 2017 07:00:06 GMT",
                        "Server": "cloudflare",
                        "Via": "1.1 21da0a66bafe2c8de8be4a4d8039346a.cloudfront.net (CloudFront)",
                        "X-Amz-Cf-Id": "XC5WNFb7pf2C6oUUG4FgA6Q7hIQ-bd9t9hxwSREB6F1kLe04uxOa-w==",
                        "X-Amz-Cf-Pop": "FRA6-C1",
                        "X-Amz-Meta-S3cmd-Attrs": "uid:1000/gname:moxie/uname:moxie/gid:1000/mode:33204/mtime:1488265189/atime:1488265189/md5:d41d8cd98f00b204e9800998ecf8427e/ctime:1488265189",
                        "X-Cache": "RefreshHit from cloudfront"
                    }
                },
                "t": 1.480029292,
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
                        ["Accept-Language", "en-US,en;q=0.9"],
                        ["Host", "svr2.signal.org"],
                        [
                            "User-Agent",
                            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/[scrubbed] Safari/537.36"
                        ]
                    ],
                    "headers": {
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                        "Accept-Language": "en-US,en;q=0.9",
                        "Host": "svr2.signal.org",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/[scrubbed] Safari/537.36"
                    },
                    "method": "GET",
                    "tor": {
                        "exit_ip": null,
                        "exit_name": null,
                        "is_tor": false
                    },
                    "x_transport": "tcp",
                    "url": "https://svr2.signal.org/"
                },
                "response": {
                    "body": "<html>\r\n<head><title>404 Not Found</title></head>\r\n<body>\r\n<center><h1>404 Not Found</h1></center>\r\n<hr><center>nginx</center>\r\n</body>\r\n</html>\r\n<!-- a padding to disable MSIE and Chrome friendly error page -->\r\n<!-- a padding to disable MSIE and Chrome friendly error page -->\r\n<!-- a padding to disable MSIE and Chrome friendly error page -->\r\n<!-- a padding to disable MSIE and Chrome friendly error page -->\r\n<!-- a padding to disable MSIE and Chrome friendly error page -->\r\n<!-- a padding to disable MSIE and Chrome friendly error page -->\r\n",
                    "body_is_truncated": false,
                    "code": 404,
                    "headers_list": [
                        ["Content-Length", "548"],
                        ["Content-Type", "text/html"],
                        ["Date", "Mon, 13 Nov 2023 07:35:51 GMT"],
                        [
                            "Strict-Transport-Security",
                            "max-age=15724800; includeSubDomains"
                        ]
                    ],
                    "headers": {
                        "Content-Length": "548",
                        "Content-Type": "text/html",
                        "Date": "Mon, 13 Nov 2023 07:35:51 GMT",
                        "Strict-Transport-Security": "max-age=15724800; includeSubDomains"
                    }
                },
                "t": 1.480366125,
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
                        ["Accept-Language", "en-US,en;q=0.9"],
                        ["Host", "ud-chat.signal.org"],
                        [
                            "User-Agent",
                            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/[scrubbed] Safari/537.36"
                        ]
                    ],
                    "headers": {
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                        "Accept-Language": "en-US,en;q=0.9",
                        "Host": "ud-chat.signal.org",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/[scrubbed] Safari/537.36"
                    },
                    "method": "GET",
                    "tor": {
                        "exit_ip": null,
                        "exit_name": null,
                        "is_tor": false
                    },
                    "x_transport": "tcp",
                    "url": "https://ud-chat.signal.org/"
                },
                "response": {
                    "body": "{\"code\":404,\"message\":\"HTTP 404 Not Found\"}",
                    "body_is_truncated": false,
                    "code": 404,
                    "headers_list": [
                        ["Content-Length", "43"],
                        ["Content-Type", "application/json"],
                        ["Date", "Mon, 13 Nov 2023 07:35:51 GMT"],
                        ["X-Signal-Timestamp", "1699860951725"]
                    ],
                    "headers": {
                        "Content-Length": "43",
                        "Content-Type": "application/json",
                        "Date": "Mon, 13 Nov 2023 07:35:51 GMT",
                        "X-Signal-Timestamp": "1699860951725"
                    }
                },
                "t": 1.605710958,
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
                        ["Accept-Language", "en-US,en;q=0.9"],
                        ["Host", "updates2.signal.org"],
                        [
                            "User-Agent",
                            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/[scrubbed] Safari/537.36"
                        ]
                    ],
                    "headers": {
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                        "Accept-Language": "en-US,en;q=0.9",
                        "Host": "updates2.signal.org",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/[scrubbed] Safari/537.36"
                    },
                    "method": "GET",
                    "tor": {
                        "exit_ip": null,
                        "exit_name": null,
                        "is_tor": false
                    },
                    "x_transport": "tcp",
                    "url": "https://updates2.signal.org/"
                },
                "response": {
                    "body": "",
                    "body_is_truncated": false,
                    "code": 200,
                    "headers_list": [
                        ["Accept-Ranges", "bytes"],
                        ["Age", "4113"],
                        ["Alt-Svc", "h3=\":443\"; ma=86400"],
                        ["Cache-Control", "public, max-age=300"],
                        ["Cf-Cache-Status", "HIT"],
                        ["Cf-Ray", "825557249bd25d50-FRA"],
                        ["Content-Length", "0"],
                        ["Content-Type", "inode/x-empty"],
                        ["Date", "Mon, 13 Nov 2023 07:35:51 GMT"],
                        ["Etag", "\"d41d8cd98f00b204e9800998ecf8427e\""],
                        ["Expires", "Mon, 13 Nov 2023 07:40:51 GMT"],
                        ["Last-Modified", "Tue, 28 Feb 2017 07:00:06 GMT"],
                        ["Server", "cloudflare"],
                        [
                            "Via",
                            "1.1 e7e7960d7731a7583cedd8f1ff1aca38.cloudfront.net (CloudFront)"
                        ],
                        [
                            "X-Amz-Cf-Id",
                            "J2txdeM_9WrImRZUs4qssD9LV6CekHkkUPc1S8T-dcRCUR2PMOVhGw=="
                        ],
                        ["X-Amz-Cf-Pop", "FRA6-C1"],
                        [
                            "X-Amz-Meta-S3cmd-Attrs",
                            "uid:1000/gname:moxie/uname:moxie/gid:1000/mode:33204/mtime:1488265189/atime:1488265189/md5:d41d8cd98f00b204e9800998ecf8427e/ctime:1488265189"
                        ],
                        ["X-Cache", "Miss from cloudfront"]
                    ],
                    "headers": {
                        "Accept-Ranges": "bytes",
                        "Age": "4113",
                        "Alt-Svc": "h3=\":443\"; ma=86400",
                        "Cache-Control": "public, max-age=300",
                        "Cf-Cache-Status": "HIT",
                        "Cf-Ray": "825557249bd25d50-FRA",
                        "Content-Length": "0",
                        "Content-Type": "inode/x-empty",
                        "Date": "Mon, 13 Nov 2023 07:35:51 GMT",
                        "Etag": "\"d41d8cd98f00b204e9800998ecf8427e\"",
                        "Expires": "Mon, 13 Nov 2023 07:40:51 GMT",
                        "Last-Modified": "Tue, 28 Feb 2017 07:00:06 GMT",
                        "Server": "cloudflare",
                        "Via": "1.1 e7e7960d7731a7583cedd8f1ff1aca38.cloudfront.net (CloudFront)",
                        "X-Amz-Cf-Id": "J2txdeM_9WrImRZUs4qssD9LV6CekHkkUPc1S8T-dcRCUR2PMOVhGw==",
                        "X-Amz-Cf-Pop": "FRA6-C1",
                        "X-Amz-Meta-S3cmd-Attrs": "uid:1000/gname:moxie/uname:moxie/gid:1000/mode:33204/mtime:1488265189/atime:1488265189/md5:d41d8cd98f00b204e9800998ecf8427e/ctime:1488265189",
                        "X-Cache": "Miss from cloudfront"
                    }
                },
                "t": 1.616991917,
                "tags": null
            }
        ],
        "tcp_connect": [
            {
                "ip": "13.32.121.94",
                "port": 443,
                "status": {
                    "failure": null,
                    "success": true
                },
                "t": 0.072114292,
                "tags": null
            },
            {
                "ip": "104.18.37.148",
                "port": 443,
                "status": {
                    "failure": null,
                    "success": true
                },
                "t": 0.072151042,
                "tags": null
            },
            {
                "ip": "13.32.121.64",
                "port": 443,
                "status": {
                    "failure": null,
                    "success": true
                },
                "t": 0.072173542,
                "tags": null
            },
            {
                "ip": "35.186.192.249",
                "port": 443,
                "status": {
                    "failure": null,
                    "success": true
                },
                "t": 0.668444042,
                "tags": null
            },
            {
                "ip": "172.217.16.179",
                "port": 443,
                "status": {
                    "failure": null,
                    "success": true
                },
                "t": 0.7645755,
                "tags": null
            },
            {
                "ip": "13.248.212.111",
                "port": 443,
                "status": {
                    "failure": null,
                    "success": true
                },
                "t": 0.5867585,
                "tags": null
            },
            {
                "ip": "40.122.45.194",
                "port": 443,
                "status": {
                    "failure": null,
                    "success": true
                },
                "t": 0.717252583,
                "tags": null
            },
            {
                "ip": "104.18.32.118",
                "port": 443,
                "status": {
                    "failure": null,
                    "success": true
                },
                "t": 1.168257583,
                "tags": null
            },
            {
                "ip": "20.104.52.125",
                "port": 443,
                "status": {
                    "failure": null,
                    "success": true
                },
                "t": 1.180286292,
                "tags": null
            },
            {
                "ip": "13.248.212.111",
                "port": 443,
                "status": {
                    "failure": null,
                    "success": true
                },
                "t": 1.122808292,
                "tags": null
            },
            {
                "ip": "104.18.43.97",
                "port": 443,
                "status": {
                    "failure": null,
                    "success": true
                },
                "t": 1.529726625,
                "tags": null
            }
        ],
        "tls_handshakes": [
            {
                "network": "",
                "address": "13.32.121.94:443",
                "cipher_suite": "TLS_AES_128_GCM_SHA256",
                "failure": null,
                "negotiated_protocol": "h2",
                "no_tls_verify": false,
                "peer_certificates": [
                    {
                        "data": "MIIEhzCCAm+gAwIBAgITFuP5ujWQNPC+GgNu4KQuvGiVXTANBgkqhkiG9w0BAQsFADB1MQswCQYDVQQGEwJVUzETMBEGA1UECBMKQ2FsaWZvcm5pYTEWMBQGA1UEBxMNTW91bnRhaW4gVmlldzEeMBwGA1UEChMVU2lnbmFsIE1lc3NlbmdlciwgTExDMRkwFwYDVQQDExBTaWduYWwgTWVzc2VuZ2VyMB4XDTIzMTAyNzE1MzE1NVoXDTI0MTEyNjIxMjA0MFowADCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAL2R9er96Vg4ql3zJLfBJAXo1C3fZUcDLKYM8nIQAqazxdVljZ31aaU41jtULd3Ytb5wTgIZPMS/WIYkKQBc/ddB42EBb5QWyZTcCaVJNax6YFCiLmKvC5IDgx7hUvon8EnCoVlnnh8edZyfKTvRmOMI1FgCbOGpkPuMU6bzwZUz8b9cSSoqqDKIsE7ySw+ZZhQyr3ZlRok89JNyXXTZGkzbw1lasm3Ren8dRb5zAf7YkhQHujPFGIqW3InrM5YqSozzUF4aG/KC2P0Vc7akz6yDbFH/oDboh9mBogg+JV3vgbgt4NwL7HnXHetp7/PQCEm2acK8KFM0WvAfZQnG4ycCAwEAAaOBhDCBgTATBgNVHSUEDDAKBggrBgEFBQcDATAMBgNVHRMBAf8EAjAAMB0GA1UdDgQWBBSFVv+BIBXF8Ve5YqGQOmUTMXsmUjAfBgNVHSMEGDAWgBS180vG5dZL0OWAa4xQw2dbvLHzcTAcBgNVHREBAf8EEjAQgg5jZG4uc2lnbmFsLm9yZzANBgkqhkiG9w0BAQsFAAOCAgEAqVy0rVIx+GlDSfIHoHq8BV4Z+PUjLErGdWb6jwEsIXA0NrADXCsKvG6kgfB3gwRqAA3K9inrLzZGmnqLr7z51XItaE9+7ZbbnIzrYgbBfCTwM4px/r/w/QCmPbB63teclmkdirYypvYDUWck4j7slnN2dp3ox5mwryjD27G5p+XzX2DvwEA4Ge1T1QO4aBoM9onurYLm8/f4OCacANEzkBnS8fpU0Z66nUeLLoGe14bOv7kIzhve7MDYgmeIO/6V1vjwEffCAT/EA6fm+4IB9N+nOxAgjIYQIzH1EcSZLNPwSUV41XKS6HVEZi72qdEuJKVQNcH63ruAot8wHA3jE69or2lXx30J9UD5xDAJrldfowdygyxx2R6V+1VMIUvb9sEqMOPlnoow66xleJCjlz860Xna/f/TXAAkIjHHeHpbmjuQSID1TZTP3hrQQiozShvyCkoWialivmHcbGtgTGPSr6Lzpdau9U1l1Ku8dkeBfOtEik/5hZZC6vkKUO4Mfjd7OYg4Io+kM4krvru6LPNFDEKxM1e8P+B3TF3iTaS3/IGGq2OYL8fusR3xHJ7R+jUf5446piG2B2q/PU0gLYda5W+EAhwdqApQEVEldH5d3wwfWcCzQQeBXc0oPtdln/xKwQ9/Jo+k3p2UO0CnwTdckfpLRvMFQCdPxk7NDYk=",
                        "format": "base64"
                    },
                    {
                        "data": "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",
                        "format": "base64"
                    }
                ],
                "server_name": "cdn.signal.org",
                "t": 0.114484917,
                "tags": null,
                "tls_version": "TLSv1.3"
            },
            {
                "network": "",
                "address": "104.18.37.148:443",
                "cipher_suite": "TLS_AES_128_GCM_SHA256",
                "failure": null,
                "negotiated_protocol": "h2",
                "no_tls_verify": false,
                "peer_certificates": [
                    {
                        "data": "MIIFiDCCA3CgAwIBAgITHWnyIiWbmS/6tOIoWMnkc4VAvDANBgkqhkiG9w0BAQsFADB1MQswCQYDVQQGEwJVUzETMBEGA1UECBMKQ2FsaWZvcm5pYTEWMBQGA1UEBxMNTW91bnRhaW4gVmlldzEeMBwGA1UEChMVU2lnbmFsIE1lc3NlbmdlciwgTExDMRkwFwYDVQQDExBTaWduYWwgTWVzc2VuZ2VyMB4XDTIzMTAwMzE1MzYyMVoXDTI0MTEwMjIxMjUwNlowADCCAiIwDQYJKoZIhvcNAQEBBQADggIPADCCAgoCggIBALbyqePp7UXssu+/FLpK5ooZfnd8qOxppabyEjTpfINxhLgelDl/2VSaRyMETXWZhUvnAeXN2PLAv9fPHjxHNHgn6H0hl8oDRP0HIiG2cBZRwPpicHNOWpTlGF2Lfl0puIkI9rbgE+uTnLcnQjMUkcbpycSlJ8ydSEta4ovlFgN6/DdbwYug3vE8cI29OskqsMZEyxKaLAMWQ62UeodGrtI/ZembUOBSJDQHW+L8mHJmVf5Jb6GG08W8lvWWaMTIjfMXciLwgsTvsR7oi5f+a6w0vIbYwKZwypLivKh0Q7hut683HKh2TITGTmVv7+fElKsnzaDAYhWHmxryn4h9p3MYDC685Pocze3SZwwKXfA85UkcOED9Lc9xOMUGiXvsgKF/57m4vykot7CyTFplLhIHoLNAk2NKPSPppLzwJ57H3w2BcHYN620PeKr8bFvyfEHFujix88HLWiT0zPYd10AKQQDeuKT1ZZSHsjBE3qU+y8f8EQ17M2351fnZH/d6kHyxhLzczsOWv7EclWqLkMx/wF+SfVK51UqiOAOZ48QFTYbW7W4CawItMIUc3i6WICcOwD+hx5bAOeUpkgXE+Oy4uzHMGOLaliAQSPVBQzjFglRABk8Sww/sE4f9NRO2cJR9oHnWQQAaFO4MdZ10zJB4oArDbvWiWu6JssF5Iu2VAgMBAAGjgYUwgYIwEwYDVR0lBAwwCgYIKwYBBQUHAwEwDAYDVR0TAQH/BAIwADAdBgNVHQ4EFgQU+qaaDgBtMMUl/9KTzXMigZUJIvgwHwYDVR0jBBgwFoAUtfNLxuXWS9DlgGuMUMNnW7yx83EwHQYDVR0RAQH/BBMwEYIPY2RuMi5zaWduYWwub3JnMA0GCSqGSIb3DQEBCwUAA4ICAQB3sFxGz12nBSOtWtZ/5nrQacH8s5HPzmpO3XHPwQzBKoKWM2Q3fPbwnKY5l/mAV+I7hqQZFfFXVxjApnaU7ETcSBHdobguDwpLWxP3PLWf/CdBwaOmhnN4EMdxksNfn1hkewyzdEgVlAYtMk8IL2PyZNFWuX+BcHvto+U+xjSvXUaQ/3epGKgK0FsYfnTwW/PscMJdxymbQFdKWS6YGHNoYlEfu75Ur7O0j2Fq88NBsaJX4YK6x9A/LXiy5mzmM3eGbbhcI21F8fhyck5BYycYEYOVYfNon08lvHmuwjcOYafUG/CfapEzaXXzInl0x1T85pdPrxwGhBo5R9y8IUPTaeRFDeC3tLAOnW5/nEfcjpexm/rxxOPCaEgSVE3tRVqP7GgBoBpGJhBlViKaEMOoWJn7pU9hOzF3ZFRgfn/Ao8o4AA3drjDLer+ORA3PkY6byBLrOh7XTdzk0rQMgniyecWymhpDgBQnMxBmS1M1UqELdTY1Xp25cIgHI2Jb2d7Nd3Y97UEz2CYvU5rJ9mza8RBcU5KPiZYuewBL8CV//Gk5HktXn679Fw61PsXzx3xotLbHS+CaJa4smj7qqCHHaqU6+SnF7B88F3ipCnQW2ZThNR6on89cM1ZUQxZMFW/mtw9WlbX/KoIqb2R8XZ9PafyBo4zxSoIC5MXea6zS0A==",
                        "format": "base64"
                    },
                    {
                        "data": "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",
                        "format": "base64"
                    }
                ],
                "server_name": "cdn2.signal.org",
                "t": 0.117355583,
                "tags": null,
                "tls_version": "TLSv1.3"
            },
            {
                "network": "",
                "address": "13.32.121.64:443",
                "cipher_suite": "TLS_AES_128_GCM_SHA256",
                "failure": null,
                "negotiated_protocol": "h2",
                "no_tls_verify": false,
                "peer_certificates": [
                    {
                        "data": "MIIErTCCApWgAwIBAgITa6fzbj+Tyyb/6yp8KiPS8aufSTANBgkqhkiG9w0BAQsFADB1MQswCQYDVQQGEwJVUzETMBEGA1UECBMKQ2FsaWZvcm5pYTEWMBQGA1UEBxMNTW91bnRhaW4gVmlldzEeMBwGA1UEChMVU2lnbmFsIE1lc3NlbmdlciwgTExDMRkwFwYDVQQDExBTaWduYWwgTWVzc2VuZ2VyMB4XDTIzMTAxMzE4MTU1NloXDTI0MTExMzAwMDQ0MVowADCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAOeebINlfg1r9uySXhAvjCUuoBSsws55SZHo0b/AT4aHwYCBDL3eUQeyM3JaJfUzqgEc9DV/LaKn50PHKRKOm5A5yS24eRh5z8jGQZwv4Gxz6pmq/yO95SwV8eOhCW1vd0SC0I8ian7uTmVUXTKiWMx9m/vEKafJm0olXduxGkuLSIzF5c3gw6i9RpV3zYDW5LhujRru2J72ine4muldLPc/yqd3wCT2LX/HJCQFmsflUGfI569sxhq1HGMjmnVqkzAUy8zlPV3YL+6eb9MoSoLhWJMUYu+ET0cLWRtefOkyyUfzTBfIAORl8cr4vmxzI3mQia5yFqzveMuz/DtmaHUCAwEAAaOBqjCBpzATBgNVHSUEDDAKBggrBgEFBQcDATAMBgNVHRMBAf8EAjAAMB0GA1UdDgQWBBRNqz78847J1V/N/5Hj3RuO9EE08TAfBgNVHSMEGDAWgBS180vG5dZL0OWAa4xQw2dbvLHzcTBCBgNVHREBAf8EODA2ghVhcGkuYmFja3VwLnNpZ25hbC5vcmeCHWFwaS1zdGFnaW5nLmJhY2t1cC5zaWduYWwub3JnMA0GCSqGSIb3DQEBCwUAA4ICAQB9FZSep9+8p/hdP+zp6QdPTOUEYIys1r9hRS+O4DLkCuc9YYf6LyJ72C1N4c5ThDwVIu7Yeh0MNapmGG+UzZyNkJWVZ/R8ZvHtHRGEQqmMJ1DBErfeupI5YqOQrgfbi5nPLl0AhZfG0HajAg5pfOOg36WnLIkmQkBfYm+Q2fi9Dx8/HBHj/Ve520nslTDjxATBIYFTfX68Y8lSokkrQEEBm1T7julrZj3P3NBZWMc1k9gi3pRvLlrzWcEOVu8dNskSE31YVByYucCWeDTOO0brcCd5yM9oE6OozgmIMzsfZK0hqSIb70lhcjxuJ+82NWRs2Jc/dhKpgzHSb7Mqpxc+7LxaJzdZLCQPSlF9FF0pQNVK8A50OLV2yyThM68DJiEovCdyhLtDr5a067KfxGHBRa0Gq4tcYhQMV+kKGCX+lHGqziLJrLloritgGY13z4fAle+Cdis+DD2O2AaDOX7Fb4UvBxxqUKftcd2/pPaNToX6NxKjpoh47S/miYKUY18p0xhHVlhqI3DVVf9eU9HtsZDe7gDhmy8jqg3UyviDs/ltF6lVPWKyRmbOOQLACEpKLllJW/I+sY0ju+RryM3I2UmRJl7EccLI9Vu/iOWyaxUhRZo+ojBT6HjMoUViSaodmf3sVnyJoJ0zLBSecPGNrn1kAaGPjpQCqsK8CFdUwQ==",
                        "format": "base64"
                    },
                    {
                        "data": "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",
                        "format": "base64"
                    }
                ],
                "server_name": "api.backup.signal.org",
                "t": 0.114521708,
                "tags": null,
                "tls_version": "TLSv1.3"
            },
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
                "t": 0.698501417,
                "tags": null,
                "tls_version": "TLSv1.3"
            },
            {
                "network": "",
                "address": "172.217.16.179:443",
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
                "t": 0.807194417,
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
                        "data": "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",
                        "format": "base64"
                    }
                ],
                "server_name": "chat.signal.org",
                "t": 0.95505975,
                "tags": null,
                "tls_version": "TLSv1.2"
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
                "t": 0.87140925,
                "tags": null,
                "tls_version": "TLSv1.3"
            },
            {
                "network": "",
                "address": "104.18.32.118:443",
                "cipher_suite": "TLS_AES_128_GCM_SHA256",
                "failure": null,
                "negotiated_protocol": "h2",
                "no_tls_verify": false,
                "peer_certificates": [
                    {
                        "data": "MIIFKzCCBNGgAwIBAgIQDLXt3e4SVl0zh0eFyMMoJTAKBggqhkjOPQQDAjBKMQswCQYDVQQGEwJVUzEZMBcGA1UEChMQQ2xvdWRmbGFyZSwgSW5jLjEgMB4GA1UEAxMXQ2xvdWRmbGFyZSBJbmMgRUNDIENBLTMwHhcNMjMwMTIxMDAwMDAwWhcNMjQwMTIwMjM1OTU5WjB1MQswCQYDVQQGEwJVUzETMBEGA1UECBMKQ2FsaWZvcm5pYTEWMBQGA1UEBxMNU2FuIEZyYW5jaXNjbzEZMBcGA1UEChMQQ2xvdWRmbGFyZSwgSW5jLjEeMBwGA1UEAxMVc25pLmNsb3VkZmxhcmVzc2wuY29tMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEGCL740kLpj0wbCAf9lX5N3rdLVC71i7fWQxkCP2A9m2cRnF3N1vL4X9c1Akx45aszAu/XO8cCLFc+Oj6nNywJqOCA2wwggNoMB8GA1UdIwQYMBaAFKXON+rrsHUOlGeItEX62SQQh5YfMB0GA1UdDgQWBBQPhoxqLiJJzH3G8JDRXT6cq6dZcjA0BgNVHREELTArghVzbmkuY2xvdWRmbGFyZXNzbC5jb22CEnVwZGF0ZXMuc2lnbmFsLm9yZzAOBgNVHQ8BAf8EBAMCB4AwHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMHsGA1UdHwR0MHIwN6A1oDOGMWh0dHA6Ly9jcmwzLmRpZ2ljZXJ0LmNvbS9DbG91ZGZsYXJlSW5jRUNDQ0EtMy5jcmwwN6A1oDOGMWh0dHA6Ly9jcmw0LmRpZ2ljZXJ0LmNvbS9DbG91ZGZsYXJlSW5jRUNDQ0EtMy5jcmwwPgYDVR0gBDcwNTAzBgZngQwBAgIwKTAnBggrBgEFBQcCARYbaHR0cDovL3d3dy5kaWdpY2VydC5jb20vQ1BTMHYGCCsGAQUFBwEBBGowaDAkBggrBgEFBQcwAYYYaHR0cDovL29jc3AuZGlnaWNlcnQuY29tMEAGCCsGAQUFBzAChjRodHRwOi8vY2FjZXJ0cy5kaWdpY2VydC5jb20vQ2xvdWRmbGFyZUluY0VDQ0NBLTMuY3J0MAwGA1UdEwEB/wQCMAAwggF8BgorBgEEAdZ5AgQCBIIBbASCAWgBZgB1AO7N0GTV2xrOxVy3nbTNE6Iyh0Z8vOzew1FIWUZxH7WbAAABhdMpSH0AAAQDAEYwRAIgX2WmFtIElHCJQGWTkwtniUArk417cxGr59sPwmFM5e0CIDjGd01+8E2xo9CFbfPwX00I8z4+pLLX/cKbLJohPZSTAHUAc9meiRtMlnigIH1HneayxhzQUV5xGSqMa4AQesF3crUAAAGF0ylIyQAABAMARjBEAiBo6kRA/2Trg+ptLSYGq7pAa0Mqa9npkQjxbqbtwC3nRQIgd2BkE/z+Pd+xwJ+sCf5seNtfgZYElS3r1A9FBt/ppxoAdgBIsONr2qZHNA/lagL6nTDrHFIBy1bdLIHZu7+rOdiEcwAAAYXTKUhWAAAEAwBHMEUCIAdE1IhV9Z7iramoFTFrggeQJdrkcEafYZL8dCJxP1mdAiEAhJcHOcFgn/RbEvfBeToV/smYir2qn/U8pQRBJBSGKAUwCgYIKoZIzj0EAwIDSAAwRQIhAOAMo0YUIkMH/FAeqZiJy5nBqyVGX2ptOl4GZr1fCuFbAiBCZg0eXXHAo2B8tMGlX9uI/8DoDH1igF4UKChK9g5UYg==",
                        "format": "base64"
                    },
                    {
                        "data": "MIIDzTCCArWgAwIBAgIQCjeHZF5ftIwiTv0b7RQMPDANBgkqhkiG9w0BAQsFADBaMQswCQYDVQQGEwJJRTESMBAGA1UEChMJQmFsdGltb3JlMRMwEQYDVQQLEwpDeWJlclRydXN0MSIwIAYDVQQDExlCYWx0aW1vcmUgQ3liZXJUcnVzdCBSb290MB4XDTIwMDEyNzEyNDgwOFoXDTI0MTIzMTIzNTk1OVowSjELMAkGA1UEBhMCVVMxGTAXBgNVBAoTEENsb3VkZmxhcmUsIEluYy4xIDAeBgNVBAMTF0Nsb3VkZmxhcmUgSW5jIEVDQyBDQS0zMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEua1NZpkUC0bsH4HRKlAenQMVLzQSfS2WuIg4m4Vfj7+7Te9hRsTJc9QkT+DuHM5ss1FxL2ruTAUJd9NyYqSb16OCAWgwggFkMB0GA1UdDgQWBBSlzjfq67B1DpRniLRF+tkkEIeWHzAfBgNVHSMEGDAWgBTlnVkwgkdYzKz6CFQ2hns6tQRN8DAOBgNVHQ8BAf8EBAMCAYYwHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMBIGA1UdEwEB/wQIMAYBAf8CAQAwNAYIKwYBBQUHAQEEKDAmMCQGCCsGAQUFBzABhhhodHRwOi8vb2NzcC5kaWdpY2VydC5jb20wOgYDVR0fBDMwMTAvoC2gK4YpaHR0cDovL2NybDMuZGlnaWNlcnQuY29tL09tbmlyb290MjAyNS5jcmwwbQYDVR0gBGYwZDA3BglghkgBhv1sAQEwKjAoBggrBgEFBQcCARYcaHR0cHM6Ly93d3cuZGlnaWNlcnQuY29tL0NQUzALBglghkgBhv1sAQIwCAYGZ4EMAQIBMAgGBmeBDAECAjAIBgZngQwBAgMwDQYJKoZIhvcNAQELBQADggEBAAUkHd0bsCrrmNaF4zlNXmtXnYJX/OvoMaJXkGUFvhZEOFp3ArnPEELG4ZKk40Un+ABHLGioVplTVI+tnkDB0A+21w0LOEhsUCxJkAZbZB2LzEgwLt4I4ptJIsCSDBFelpKU1fwg3FZs5ZKTv3ocwDfjhUkV+ivhdDkYD7fa86JXWGBPzI6UAPxGezQxPk1HgoE6y/SJXQ7vTQ1unBuCJN0yJV0ReFEQPaA1IwQvZW+cwdFD19Ae8zFnWSfda9J1CZMRJCQUzym+5iPDuI9yP+kHyCREU3qzuWFloUwOxkgAyXVjBYdwRVKD05WdRerw6DEdfgkfCv4+3ao8XnTSrLE=",
                        "format": "base64"
                    }
                ],
                "server_name": "updates.signal.org",
                "t": 1.201748875,
                "tags": null,
                "tls_version": "TLSv1.3"
            },
            {
                "network": "",
                "address": "20.104.52.125:443",
                "cipher_suite": "TLS_AES_256_GCM_SHA384",
                "failure": null,
                "negotiated_protocol": "h2",
                "no_tls_verify": false,
                "peer_certificates": [
                    {
                        "data": "MIIFiDCCA3CgAwIBAgITKuiqmzU2/MzkZvAkzg1HkJi3ATANBgkqhkiG9w0BAQsFADB1MQswCQYDVQQGEwJVUzETMBEGA1UECBMKQ2FsaWZvcm5pYTEWMBQGA1UEBxMNTW91bnRhaW4gVmlldzEeMBwGA1UEChMVU2lnbmFsIE1lc3NlbmdlciwgTExDMRkwFwYDVQQDExBTaWduYWwgTWVzc2VuZ2VyMB4XDTIzMDQxMzIwMDQxOFoXDTI0MDUxNDAxNTMwM1owADCCAiIwDQYJKoZIhvcNAQEBBQADggIPADCCAgoCggIBAN11j+Lsqttl7ngOGt0Ket2920Oz1rw5uVyYXIfkKUbI8xL7ANh1AbCv8bV32yISE8HMSU18rY3nGNQP2O2BQjuaxUZ3MVqrHsldeMExk/gcGq0kg59cddR2YAfetuho67QSVXuH3yDDaY9fZUEfSmHBFsXHrQ0ifHbTmEs5JRxDZ/M8lqEK9gWnKJJ/eBToP4edYsh4vvG57T0QUNB7YqNh85WKTISRYf/wVxt8rq4bMMWqLKkG4Xh04syARsxyIp6ucPfGaJPGamEO9ZR/7YuSUbSZNgjhDohR9AzSBZAS+UJBLDfRI8Y6tW//Xkb3C1x1oCiig/UBSY6ru5xLMVBHvxf0mOjhibMup0JfXfFbeLWykD95+/hebMNeRkY76XmudaJSZCfavDBsWd5RcIbR9Wjhrv9VbLuyfoEvo+k0hHCLXgknKyJ1emq1EDd3pYKm352qrS4W2qmYnsg6m4/3HLlVfy+N86iXAyVVCmpnNr9ZG0lXUMcg4rzRnwS1WkAHsSgHq/GPlRydi6h3pkardWVA9mMgmDqxrWmk9+AZgZ6SGkqnLnEeeMxQtYv0Pu+wZxNgze8kwYwRcdx8j1QjwXYh/wgsl4YQT+HwZOWpae8e6SUcv0+w6QBt4LmltFmjsTXNoWBZiJPCYxrBDIUm/AqGmBMuWXIvC0VYlyi/AgMBAAGjgYUwgYIwEwYDVR0lBAwwCgYIKwYBBQUHAwEwDAYDVR0TAQH/BAIwADAdBgNVHQ4EFgQUnktNPl5PJVUk4YzeINPwvV2oNEQwHwYDVR0jBBgwFoAUtfNLxuXWS9DlgGuMUMNnW7yx83EwHQYDVR0RAQH/BBMwEYIPc3ZyMi5zaWduYWwub3JnMA0GCSqGSIb3DQEBCwUAA4ICAQCM1Awyae+Sy1mmYnV8R6lD3I1aHPALAe40xx8VSp/2MncuuyITrhcffSqojeRj4O4KgM+LrJc/MDLS1FtBvZMMiqpiNqi1kxpJbGKA2fldZU3ihdUQ24Hdz4p1VxX+qwdYhCXjbPtG2GAq9EcrNa41fV6ZPYrXxchztUD+V+NneGYu5SSSRjryzePLOYSnYfqwNjlGDinS0WGhIRJtbsbIaTK1B9fr9ZRHoiQl/+afpPwzShdCut1cax9kKvFTK3+6gnGUW7RoROXOUUXeuwmaChT+WYWJ7YzYSPUxbPRz1qHO3F3oS15CN9hhTunAhlsdw8+TBUC8V5ah9ww7B3oXr4vo6+ZtwecYHeuFM5TESWOveFHE8cCE0O7htDrTv/Ua0Wbdze5UR7ScIOvwpMeVhiVRIDkjtcblKalJRQrcWk6Q4QUFRk2f1WRGmRkE57KsTLDvpyyWCI6uuxh8JsrmQ86/cH7UQEyCh7IhcG9CfHQ2eILLhgvOfT1R+/+CVz7N4YdcFQb3iZtizs2HwsejdPYp4q5nSG5eqV+04B+qpfk+d19WmqXgbDXQvb6tSJ9FlBkS0VH5awfonxBGc6ur4mg/t8rW2HBKI1supY5qWYkPLyJ+0v6HUz6WFe17fOnkRZO7E82zRuoTHKVZ29NVgH3UTNcTtpE81zJn5yXYsg==",
                        "format": "base64"
                    },
                    {
                        "data": "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",
                        "format": "base64"
                    }
                ],
                "server_name": "svr2.signal.org",
                "t": 1.319207125,
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
                        "data": "MIIFjDCCA3SgAwIBAgIUAMLShdazHGAIYb+DDZoPYOoP/6gwDQYJKoZIhvcNAQELBQAwdTELMAkGA1UEBhMCVVMxEzARBgNVBAgTCkNhbGlmb3JuaWExFjAUBgNVBAcTDU1vdW50YWluIFZpZXcxHjAcBgNVBAoTFVNpZ25hbCBNZXNzZW5nZXIsIExMQzEZMBcGA1UEAxMQU2lnbmFsIE1lc3NlbmdlcjAeFw0yMzEwMjcxNTMxMzdaFw0yNDExMjYyMTIwMjJaMAAwggIiMA0GCSqGSIb3DQEBAQUAA4ICDwAwggIKAoICAQDG29huWvrwcG/3q8fM0g1R+qftJvfFPV+9WRCG4KI+T7nETW7Hv1QwoUgWYR+eA+8aIEvEFvo276RNqSlrIWwUme0CmXkhVucMZTIqCvuDlrPjVfcU0xwsUAcw6HAqs2E6aij2sxEWTx5NJf2yZCIuqtP8Gm3lOI9kh2VTtjrR/Bkewe9eBtBpCBFwa+qd6E9AbGpH735aQCnpNwL7JuhNeXyt3B3rV9xqmnNW+GnyKPZa3ZW2dQd2u1qnGfLjycnxZrWATWUqKiJR9/S84YSEsDPRG+M0+dbuyAHrb98BmGYZIHrVQo6uz5HYAw1Fjou7zcbl4uoBA8Y5EQ9jGqjZCI2FPh+HbUFHNRPGx5SUGe+x9UVv46/A3MtKfqoVrlJh+22lXhWEqmsMe0DT6Uz6KITM0MsI1nr5FOuhLq1nds3i7lRPC+KG5aTBNRCqJI27YDRMY+3NDCWDBp0+loG0cZnOHtgo5JvJ/VAwNLYyd3zpkfphtm4DAYp6MOI8nfmKZZ/0SZF6m/Mu2S9igbxnc37ndjEM7aVedLj0sAe9vzlnFiarVzotlyg1JsbciAnFynA708yQxcpUId183lYspMYTDLbBwnlvnUGMZxGorwVeK9hJaAnd9urd6ikcYr6iPmv/JMKk7e3wygbjSDxtEsb3+v8V1cyOWDbuuB457QIDAQABo4GIMIGFMBMGA1UdJQQMMAoGCCsGAQUFBwMBMAwGA1UdEwEB/wQCMAAwHQYDVR0OBBYEFPptm9z5QqhQyMIY00EDLl52zgj3MB8GA1UdIwQYMBaAFLXzS8bl1kvQ5YBrjFDDZ1u8sfNxMCAGA1UdEQEB/wQWMBSCEnVkLWNoYXQuc2lnbmFsLm9yZzANBgkqhkiG9w0BAQsFAAOCAgEArVFAFgQ4ZROHEzBcoKS76XlZ/lgdPYF7SX/noQIGBxAINWVfadWKMkdjNFTbGmrtxQ0Xshm3wmYK5HmkupkiWbqW65Mvn0Pg8C/81p4I24JspEnAd2yvf8+h/Hajd7N6XQK7bOLZjCzGBTd+BxqUoyPNiaUPhkbvTLeEKJoGTrtXQiwM3HZ5VK5XDGiAiWHg3ni+3FJFJ83FSvwfi30IxK22MfZsxc03zT3eSw0uIN6PhhfDKvKnfk5+/remm22O2jRzjy6Xy+7iPM1D9cqTW6jDSwG/XU5uuEUnbFZoLqkKweXBnRNYbe/RVL8Ju0ZawuX8LtHB8RI28xG+dZOC0gA3WhCxTaVy4jNj7K87ps/5i5tZFwdYDazk+Tok0ic5yt7zd/UGKn6PTDa9LW6vas/fzDrnw1pS1Zjv1sZkFlFjDQMKrGfAunJLG0afi0hiqLEo9Hu9Bf2k/jBlz47/stfiynHA4Ak1pUc7167DYpY/ZdjXsjVjO5jDmCyrdpx4TjEn5D+4l1CoaP89F1UVjA7VBGhMeQckl7Hs01QLJaVyDdgwa4zFL6fMVNihIbcXiZZuxF71XheeoHPPJImxmsKYMG9RUkNU8UBl9OErVykOJ2zE/7qXh9wxaHzTFnJ541eeExZ9zJG/xaJ5/5NVDQR/pfZLX5jlv/QyoJiuAuQ=",
                        "format": "base64"
                    },
                    {
                        "data": "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",
                        "format": "base64"
                    }
                ],
                "server_name": "ud-chat.signal.org",
                "t": 1.4795880829999999,
                "tags": null,
                "tls_version": "TLSv1.2"
            },
            {
                "network": "",
                "address": "104.18.43.97:443",
                "cipher_suite": "TLS_AES_128_GCM_SHA256",
                "failure": null,
                "negotiated_protocol": "h2",
                "no_tls_verify": false,
                "peer_certificates": [
                    {
                        "data": "MIIFjDCCA3SgAwIBAgITcOZXIdzJbXbC6mSXyFIY98/+jDANBgkqhkiG9w0BAQsFADB1MQswCQYDVQQGEwJVUzETMBEGA1UECBMKQ2FsaWZvcm5pYTEWMBQGA1UEBxMNTW91bnRhaW4gVmlldzEeMBwGA1UEChMVU2lnbmFsIE1lc3NlbmdlciwgTExDMRkwFwYDVQQDExBTaWduYWwgTWVzc2VuZ2VyMB4XDTIzMTAwMzE1MjUxOFoXDTI0MTEwMjIxMTQwM1owADCCAiIwDQYJKoZIhvcNAQEBBQADggIPADCCAgoCggIBAOgnyN/uniuUaO0kEaC+2qGvn3rEvO9EqT8Xr3VBsCjVB4WAae3qPJBdjLlv/iAUOrqkYAd9vcWD0j1hGU0JAJDZ8B0kFmOjUvidXcH3OnZUgO6XW3xQGPV7p3uOWc09o7QoTAUXNzuVCaUXM+S/yoDheF/Sais6Aj65m9RUvFDYk7PximXY3gWJZPtrpCXfcwJyMogZQmenRNJfuKRpywwpE2JiEhKnUgPoWaLHlz+VoOSRFTC/4lsYeQpA8a9oF6eBvBTVD6gCW94nC0oHf+s4gAh6mI2qt2yl74Gg8ujRSSb9vPoiJBKw0ie1Zj2tDEO7Wx90oOHyGdWCGgwp7QeDYlU0NgYXVSKSi4FBkq0MibfjxlkaRL8+TFL12atAYYN8OOpuDYImxGtv4UuhcCF8x0qyLhv8aBAYz8XXWSE1/UuMNA14B2Zx5+LOWJLC8pcTjviKZoWzsXJ/n5uAvpMN0cFyqryT5ZTMdlyntasCm7OkMd36Gu23nFusKZLW7wrnd8IzKlX/eTmYVzr1V8s9QBZPczr7HkcVf/OCc8CdFxmycgTusevFEVo9hvOngPoUAuflzKw2M5kl5i1JGxw0oI5781FMPB6s9+syRyzvFXV/BtMxvQ6+g0oNjLJ8dPil7Y7XuyqHqSDQ4juPPYxJTWFtozDOyWlWqxm/zwrBAgMBAAGjgYkwgYYwEwYDVR0lBAwwCgYIKwYBBQUHAwEwDAYDVR0TAQH/BAIwADAdBgNVHQ4EFgQUe/QkWO2oiFsUGKwDbYroNmdlOdYwHwYDVR0jBBgwFoAUtfNLxuXWS9DlgGuMUMNnW7yx83EwIQYDVR0RAQH/BBcwFYITdXBkYXRlczIuc2lnbmFsLm9yZzANBgkqhkiG9w0BAQsFAAOCAgEALzfdJjSYsG1xg2uLmbjN4k3ypB3nMltZzMSsw98cbhp++CW42R6IW/B6LJQO72gUY3o9SS5Rd9ugOuQQ7QytCdjy7RdVieJrsYYm0DdSB7p8cEub9Rm166jD/n7LEzNeT/j7Tg9B94/8RZZy93iW9DQ6A5O3ggaogUJFWLf48RP/9B7XRUbQQTZKdTRXecRGa+w2cvpZkmZ8ly53otAZOH3vIdxJlOzfPhrVRFKLCa91c1Zvfv6djrpXJ62j8/bGWTi6qVI6vVYOpCZSEuGCjnlv1QNTybLgkjqK+GU7qtQNHrYEABj4bXY5lcOIAdCtnB1QNbdnVI3L6ZKq51Hl3QnD9kp/CxHESMzMCUoJxyioOQhTNfW4Qn3xK2D23OHhRHXy35XCWD0efrDVpQ4CdoIiSpHo7QDBwu7unOaPeFAy0GMXYpoTVlQbdFL6sXnOSxUAvUxG1FX59zvsJtr762YsR5pc3yk7KrgrhgmvvJOr5Oj86rvcGPApEhx3k0pCNjNUEnFM+7qGrmI5YHcv4HDcWTfo/GE1OmIaHfT5KHu7OIB73s7uDElEnRl+QX0i9sf635PQdRm/Vw3yI4PgD6+gLqbp43qsLkvTjN0nCPo5dOkUgqdUNscSqATYjfMcSQR4cp5KdmdANRh7S3Ot+4T//q9qfk1m27RW+ouoQMI=",
                        "format": "base64"
                    },
                    {
                        "data": "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",
                        "format": "base64"
                    }
                ],
                "server_name": "updates2.signal.org",
                "t": 1.582086167,
                "tags": null,
                "tls_version": "TLSv1.3"
            }
        ],
        "signal_backend_status": "ok",
        "signal_backend_failure": null
    },
    "test_name": "signal",
    "test_runtime": 1.61902425,
    "test_start_time": "2023-11-13 07:35:50",
    "test_version": "0.2.3"
}
```

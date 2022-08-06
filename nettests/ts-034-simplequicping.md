# Specification version number

2022-08-06

* _status_: experimental

# Specification name

`simplequicping` (simple QUIC ping)

# Test preconditions

* An internet connection

# Expected impact

The possibility of pinging a QUIC endpoint.

(The `ts-032-quicping` experiment measures _whether_ QUIC is blocked at the UDP
or TLS level, while this experiment is simpler and just checks for whether we could
establish a QUIC connection to a given QUIC endpoint.)

# Expected inputs

* A URL like `quichandshake://<host>:<port>`.

* An optional SNI to use (`-O SNI=value` with `miniooni`).

# Test description

The experiment will attempt to handshake to the given QUIC endpoint every
second for ten times and return the results.

# Expected output

## Parent data format

* `df-005-tcpconnect`
* `df-008-netevents`

## Semantics

```JSON
{
    "pings": []
}
```

where:

- `pings` contains `SinglePing` results which look like:

```JSON
{
  "network_events": [],
  "quic_handshake": {}
}
```

where:

- `network_events` contains zero or more `df-008-netevents`

- `quic_handshake` contains a single `df-006-tlshandshake` entry

Before 2022-08-06, `quic_handshake` was a list but we
changed that because this is an experimental nettest and it seems better
to avoid suggesting there could be more than a single QUIC handshake for 
each ping

## Possible conclusions

This experiment is an exploratory tool. There is no immediate conclusion
from its results but it is useful to perform censorship research.

## Example output sample

```JSON
{
  "annotations": {
    "architecture": "amd64",
    "engine_name": "ooniprobe-engine",
    "engine_version": "3.16.0-alpha",
    "platform": "linux"
  },
  "data_format_version": "0.2.0",
  "input": "quichandshake://8.8.8.8:443",
  "measurement_start_time": "2022-08-06 10:21:44",
  "probe_asn": "AS24560",
  "probe_cc": "IN",
  "probe_ip": "127.0.0.1",
  "probe_network_name": "Bharti Airtel Limited",
  "report_id": "",
  "resolver_asn": "AS13335",
  "resolver_ip": "162.158.45.17",
  "resolver_network_name": "Cloudflare, Inc.",
  "software_name": "miniooni",
  "software_version": "3.16.0-alpha",
  "test_keys": {
    "pings": [
      {
        "network_events": [
          {
            "failure": null,
            "operation": "quic_handshake_start",
            "t": 0.004950962
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "udp",
            "t": 0.005319903
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 0.011812899
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "udp",
            "t": 0.012253587
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "udp",
            "t": 0.032884981
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 0.041183141
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "udp",
            "t": 0.078792192
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 0.079868436
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 0.079896193
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 0.080070541
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1248,
            "operation": "read_from",
            "proto": "udp",
            "t": 0.080088236
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 65,
            "operation": "read_from",
            "proto": "udp",
            "t": 0.080101777
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 44,
            "operation": "write_to",
            "proto": "udp",
            "t": 0.080121783
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 44,
            "operation": "write_to",
            "proto": "udp",
            "t": 0.080318088
          },
          {
            "failure": null,
            "operation": "quic_handshake_done",
            "t": 0.082728334
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 83,
            "operation": "write_to",
            "proto": "udp",
            "t": 0.082736494
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 33,
            "operation": "write_to",
            "proto": "udp",
            "t": 0.082761565
          }
        ],
        "quic_handshakes": {
          "network": "quic",
          "address": "8.8.8.8:443",
          "cipher_suite": "TLS_AES_128_GCM_SHA256",
          "failure": null,
          "negotiated_protocol": "h3",
          "no_tls_verify": false,
          "peer_certificates": [
            {
              "data": "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",
              "format": "base64"
            },
            {
              "data": "MIIFljCCA36gAwIBAgINAgO8U1lrNMcY9QFQZjANBgkqhkiG9w0BAQsFADBHMQswCQYDVQQGEwJVUzEiMCAGA1UEChMZR29vZ2xlIFRydXN0IFNlcnZpY2VzIExMQzEUMBIGA1UEAxMLR1RTIFJvb3QgUjEwHhcNMjAwODEzMDAwMDQyWhcNMjcwOTMwMDAwMDQyWjBGMQswCQYDVQQGEwJVUzEiMCAGA1UEChMZR29vZ2xlIFRydXN0IFNlcnZpY2VzIExMQzETMBEGA1UEAxMKR1RTIENBIDFDMzCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAPWI3+dijB43+DdCkH9sh9D7ZYIl/ejLa6T/belaI+KZ9hzpkgOZE3wJCor6QtZeViSqejOEH9Hpabu5dOxXTGZok3c3VVP+ORBNtzS7XyV3NzsXlOo85Z3VvMO0Q+sup0fvsEQRY9i0QYXdQTBIkxu/t/bgRQIh4JZCF8/ZK2VWNAcmBA2o/X3KLu/qSHw3TT8An4Pf73WELnlXXPxXbhqW//yMmqaZviXZf5YsBvcRKgKAgOtjGDxQSYflispfGStZloEAoPtR28p3CwvJlk/vcEnHXG0g/Zm0tOLKLnf9LdwLtmsTDIwZKxeWmLnwi/agJ7u2441Rj72ux5uxiZ0CAwEAAaOCAYAwggF8MA4GA1UdDwEB/wQEAwIBhjAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwEgYDVR0TAQH/BAgwBgEB/wIBADAdBgNVHQ4EFgQUinR/r4XN7pXNPZzQ4kYU83E1HScwHwYDVR0jBBgwFoAU5K8rJnEaK0gnhS9SZizv8IkTcT4waAYIKwYBBQUHAQEEXDBaMCYGCCsGAQUFBzABhhpodHRwOi8vb2NzcC5wa2kuZ29vZy9ndHNyMTAwBggrBgEFBQcwAoYkaHR0cDovL3BraS5nb29nL3JlcG8vY2VydHMvZ3RzcjEuZGVyMDQGA1UdHwQtMCswKaAnoCWGI2h0dHA6Ly9jcmwucGtpLmdvb2cvZ3RzcjEvZ3RzcjEuY3JsMFcGA1UdIARQME4wOAYKKwYBBAHWeQIFAzAqMCgGCCsGAQUFBwIBFhxodHRwczovL3BraS5nb29nL3JlcG9zaXRvcnkvMAgGBmeBDAECATAIBgZngQwBAgIwDQYJKoZIhvcNAQELBQADggIBAIl9rCBcDDy+mqhXlRu0rvqrpXJxtDaV/d9AEQNMwkYUuxQkq/BQcSLbrcRuf8/xam/IgxvYzolfh2yHuKkMo5uhYpSTld9brmYZCwKWnvy15xBpPnrLRklfRuFBsdeYTWU0AIAaP0+fbH9JAIFTQaSSIYKCGvGjRFsqUBITTcFTNvNCCK9U+o53UxtkOCcXCb1YyRt8OS1b887U7ZfbFAO/CVMkH8IMBHmYJvJh8VNS/UKMG2YrPxWhu//2m+OBmgEGcYk1KCTd4b3rGS3hSMs9WYNRtHTGnXzGsYZbr8w0xNPM1IERlQCh9BIiAfq0g3GvjLeMcySsN1PCAJA/Ef5c7TaUEDu9Ka7ixzpiO2xj2YC/WXGsYye5TBeg2vZzFb8q3o/zpWwygTMD0IZRcZk0upONXbVRWPeyk+gB9lm+cZv9TSjOz23HFtz30dZGm6fKa+l3D/2gthsjgx0QGtkJAITgRNOidSOzNIb2ILCkXhAd4FJGAJ2xDx8hcFH1mt0G/FX0Kw4zd8NLQsLxdxP8c4CU6x+7Nz/OAipmsHMdMqUybDKwjuDEI/9bfU1lcKwrmz3O2+BtjjKAvpafkmO8l7tdufThcV4q5O8DIrGKZTqPwJNl1IXNDw9bg1kWRxYtnCQ6yICmJhSFm/Y3m6xv+cXDBlHz4n/FsRC6UfTd",
              "format": "base64"
            },
            {
              "data": "MIIFYjCCBEqgAwIBAgIQd70NbNs2+RrqIQ/E8FjTDTANBgkqhkiG9w0BAQsFADBXMQswCQYDVQQGEwJCRTEZMBcGA1UEChMQR2xvYmFsU2lnbiBudi1zYTEQMA4GA1UECxMHUm9vdCBDQTEbMBkGA1UEAxMSR2xvYmFsU2lnbiBSb290IENBMB4XDTIwMDYxOTAwMDA0MloXDTI4MDEyODAwMDA0MlowRzELMAkGA1UEBhMCVVMxIjAgBgNVBAoTGUdvb2dsZSBUcnVzdCBTZXJ2aWNlcyBMTEMxFDASBgNVBAMTC0dUUyBSb290IFIxMIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAthECix7joXebO9y/lD63ladAPKH9gvl9MgaCcfb2jH/76Nu8ai6Xl6OMS/kr9rH5zoQdsfnFl97vufKj6bwSiV6nqlKr+CMny6SxnGPb15l+8Ape62im9MZaRw1NEDPjTrETo8gYbEvs/AmQ351kKSUjB6G00j0uYODP0gmHu81I8E3CwnqIiru6z1kZ1q+PsAewnjHxgsHA3y6mbWwZDrXYfiYaRQM9sHmklCitD38m5agI/pboPGiUU+6DOogrFZYJsuB6jC511pzrp1Zkj5ZPaK49l8KEj8C8QMALXL32h7M1bKwYUH+E4EzNktMg6TO8UpmvMrUpsyUqtEj5cuHKZPfmghCN6J3Cioj6OGaK/GP5Afl4/Xtcd/p2h/rs37EOeZVXtL0m79YB0esWCruOC7XFxYpVq9Os6pFLKcwZpDIlTirxZUTQAs6qzkm06p98g7BAe+dDq6dso499iYH6TKX/1Y7DzkvgtdizjkXPdsDtQCv9Uw+wp9U7DbGKogPeMa3Md+pvez7W35EiEua++tgy/BBjFFFy3l3WFpO9KWgz7zpm7AeKJt8T11dleCfeXkkUAKIAf5qoIbapsZWwpbkNFhHax2xIPEDgfg1azVY80ZcFuctL7TlLnMQ/0lUTbiSw1nH69MG6zO0b9f6BQdgAmD06yK56mDcYBZUCAwEAAaOCATgwggE0MA4GA1UdDwEB/wQEAwIBhjAPBgNVHRMBAf8EBTADAQH/MB0GA1UdDgQWBBTkrysmcRorSCeFL1JmLO/wiRNxPjAfBgNVHSMEGDAWgBRge2YaRQ2XyolQL30EzTSo//z9SzBgBggrBgEFBQcBAQRUMFIwJQYIKwYBBQUHMAGGGWh0dHA6Ly9vY3NwLnBraS5nb29nL2dzcjEwKQYIKwYBBQUHMAKGHWh0dHA6Ly9wa2kuZ29vZy9nc3IxL2dzcjEuY3J0MDIGA1UdHwQrMCkwJ6AloCOGIWh0dHA6Ly9jcmwucGtpLmdvb2cvZ3NyMS9nc3IxLmNybDA7BgNVHSAENDAyMAgGBmeBDAECATAIBgZngQwBAgIwDQYLKwYBBAHWeQIFAwIwDQYLKwYBBAHWeQIFAwMwDQYJKoZIhvcNAQELBQADggEBADSkHrEoo9C0dhemMXoh6dFSPsjbdBZBiLg9NR3t5P+T4Vxfq7vqfM/b5A3Ri1fyJm9bvhdGaJQ3b2t6yMAYN/olUazsaL+yyEn9WprKASOshIArAoyZl+tJaox118fessmXn1hIVw41oeQa1v1vg4Fv74zPl6/AhSrw9U5pCZEt4Wi4wStz6dTZ/CLANx8LZh1J7QJVj2fhMtfTJr9w4z30Z209fOU0iOMy+qduBmpvvYuR7hZL6Dupszfnw0Skfths18dG9ZKb59UhvmaSGZRVbNQpsg3BZlvid0lIKO2d1xozclOzgjXPYovJJIultzkMu34qQb9Sz/yilrbCgj8=",
              "format": "base64"
            }
          ],
          "server_name": "8.8.8.8",
          "t": 0.082728334,
          "tags": [],
          "tls_version": "TLSv1.3"
        }
      },
      {
        "network_events": [
          {
            "failure": null,
            "operation": "quic_handshake_start",
            "t": 1.008431869
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "udp",
            "t": 1.009091216
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 1.015728046
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "udp",
            "t": 1.0163045
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "udp",
            "t": 1.037092262
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 1.050299975
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 1.08239286
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 1.0824261609999999
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 44,
            "operation": "write_to",
            "proto": "udp",
            "t": 1.082727461
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 1.082747446
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 1.08278075
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 116,
            "operation": "read_from",
            "proto": "udp",
            "t": 1.082789664
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 44,
            "operation": "write_to",
            "proto": "udp",
            "t": 1.083872621
          },
          {
            "failure": null,
            "operation": "quic_handshake_done",
            "t": 1.086645955
          }
        ],
        "quic_handshakes": {
          "network": "quic",
          "address": "8.8.8.8:443",
          "cipher_suite": "TLS_AES_128_GCM_SHA256",
          "failure": null,
          "negotiated_protocol": "h3",
          "no_tls_verify": false,
          "peer_certificates": [
            {
              "data": "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",
              "format": "base64"
            },
            {
              "data": "MIIFljCCA36gAwIBAgINAgO8U1lrNMcY9QFQZjANBgkqhkiG9w0BAQsFADBHMQswCQYDVQQGEwJVUzEiMCAGA1UEChMZR29vZ2xlIFRydXN0IFNlcnZpY2VzIExMQzEUMBIGA1UEAxMLR1RTIFJvb3QgUjEwHhcNMjAwODEzMDAwMDQyWhcNMjcwOTMwMDAwMDQyWjBGMQswCQYDVQQGEwJVUzEiMCAGA1UEChMZR29vZ2xlIFRydXN0IFNlcnZpY2VzIExMQzETMBEGA1UEAxMKR1RTIENBIDFDMzCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAPWI3+dijB43+DdCkH9sh9D7ZYIl/ejLa6T/belaI+KZ9hzpkgOZE3wJCor6QtZeViSqejOEH9Hpabu5dOxXTGZok3c3VVP+ORBNtzS7XyV3NzsXlOo85Z3VvMO0Q+sup0fvsEQRY9i0QYXdQTBIkxu/t/bgRQIh4JZCF8/ZK2VWNAcmBA2o/X3KLu/qSHw3TT8An4Pf73WELnlXXPxXbhqW//yMmqaZviXZf5YsBvcRKgKAgOtjGDxQSYflispfGStZloEAoPtR28p3CwvJlk/vcEnHXG0g/Zm0tOLKLnf9LdwLtmsTDIwZKxeWmLnwi/agJ7u2441Rj72ux5uxiZ0CAwEAAaOCAYAwggF8MA4GA1UdDwEB/wQEAwIBhjAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwEgYDVR0TAQH/BAgwBgEB/wIBADAdBgNVHQ4EFgQUinR/r4XN7pXNPZzQ4kYU83E1HScwHwYDVR0jBBgwFoAU5K8rJnEaK0gnhS9SZizv8IkTcT4waAYIKwYBBQUHAQEEXDBaMCYGCCsGAQUFBzABhhpodHRwOi8vb2NzcC5wa2kuZ29vZy9ndHNyMTAwBggrBgEFBQcwAoYkaHR0cDovL3BraS5nb29nL3JlcG8vY2VydHMvZ3RzcjEuZGVyMDQGA1UdHwQtMCswKaAnoCWGI2h0dHA6Ly9jcmwucGtpLmdvb2cvZ3RzcjEvZ3RzcjEuY3JsMFcGA1UdIARQME4wOAYKKwYBBAHWeQIFAzAqMCgGCCsGAQUFBwIBFhxodHRwczovL3BraS5nb29nL3JlcG9zaXRvcnkvMAgGBmeBDAECATAIBgZngQwBAgIwDQYJKoZIhvcNAQELBQADggIBAIl9rCBcDDy+mqhXlRu0rvqrpXJxtDaV/d9AEQNMwkYUuxQkq/BQcSLbrcRuf8/xam/IgxvYzolfh2yHuKkMo5uhYpSTld9brmYZCwKWnvy15xBpPnrLRklfRuFBsdeYTWU0AIAaP0+fbH9JAIFTQaSSIYKCGvGjRFsqUBITTcFTNvNCCK9U+o53UxtkOCcXCb1YyRt8OS1b887U7ZfbFAO/CVMkH8IMBHmYJvJh8VNS/UKMG2YrPxWhu//2m+OBmgEGcYk1KCTd4b3rGS3hSMs9WYNRtHTGnXzGsYZbr8w0xNPM1IERlQCh9BIiAfq0g3GvjLeMcySsN1PCAJA/Ef5c7TaUEDu9Ka7ixzpiO2xj2YC/WXGsYye5TBeg2vZzFb8q3o/zpWwygTMD0IZRcZk0upONXbVRWPeyk+gB9lm+cZv9TSjOz23HFtz30dZGm6fKa+l3D/2gthsjgx0QGtkJAITgRNOidSOzNIb2ILCkXhAd4FJGAJ2xDx8hcFH1mt0G/FX0Kw4zd8NLQsLxdxP8c4CU6x+7Nz/OAipmsHMdMqUybDKwjuDEI/9bfU1lcKwrmz3O2+BtjjKAvpafkmO8l7tdufThcV4q5O8DIrGKZTqPwJNl1IXNDw9bg1kWRxYtnCQ6yICmJhSFm/Y3m6xv+cXDBlHz4n/FsRC6UfTd",
              "format": "base64"
            },
            {
              "data": "MIIFYjCCBEqgAwIBAgIQd70NbNs2+RrqIQ/E8FjTDTANBgkqhkiG9w0BAQsFADBXMQswCQYDVQQGEwJCRTEZMBcGA1UEChMQR2xvYmFsU2lnbiBudi1zYTEQMA4GA1UECxMHUm9vdCBDQTEbMBkGA1UEAxMSR2xvYmFsU2lnbiBSb290IENBMB4XDTIwMDYxOTAwMDA0MloXDTI4MDEyODAwMDA0MlowRzELMAkGA1UEBhMCVVMxIjAgBgNVBAoTGUdvb2dsZSBUcnVzdCBTZXJ2aWNlcyBMTEMxFDASBgNVBAMTC0dUUyBSb290IFIxMIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAthECix7joXebO9y/lD63ladAPKH9gvl9MgaCcfb2jH/76Nu8ai6Xl6OMS/kr9rH5zoQdsfnFl97vufKj6bwSiV6nqlKr+CMny6SxnGPb15l+8Ape62im9MZaRw1NEDPjTrETo8gYbEvs/AmQ351kKSUjB6G00j0uYODP0gmHu81I8E3CwnqIiru6z1kZ1q+PsAewnjHxgsHA3y6mbWwZDrXYfiYaRQM9sHmklCitD38m5agI/pboPGiUU+6DOogrFZYJsuB6jC511pzrp1Zkj5ZPaK49l8KEj8C8QMALXL32h7M1bKwYUH+E4EzNktMg6TO8UpmvMrUpsyUqtEj5cuHKZPfmghCN6J3Cioj6OGaK/GP5Afl4/Xtcd/p2h/rs37EOeZVXtL0m79YB0esWCruOC7XFxYpVq9Os6pFLKcwZpDIlTirxZUTQAs6qzkm06p98g7BAe+dDq6dso499iYH6TKX/1Y7DzkvgtdizjkXPdsDtQCv9Uw+wp9U7DbGKogPeMa3Md+pvez7W35EiEua++tgy/BBjFFFy3l3WFpO9KWgz7zpm7AeKJt8T11dleCfeXkkUAKIAf5qoIbapsZWwpbkNFhHax2xIPEDgfg1azVY80ZcFuctL7TlLnMQ/0lUTbiSw1nH69MG6zO0b9f6BQdgAmD06yK56mDcYBZUCAwEAAaOCATgwggE0MA4GA1UdDwEB/wQEAwIBhjAPBgNVHRMBAf8EBTADAQH/MB0GA1UdDgQWBBTkrysmcRorSCeFL1JmLO/wiRNxPjAfBgNVHSMEGDAWgBRge2YaRQ2XyolQL30EzTSo//z9SzBgBggrBgEFBQcBAQRUMFIwJQYIKwYBBQUHMAGGGWh0dHA6Ly9vY3NwLnBraS5nb29nL2dzcjEwKQYIKwYBBQUHMAKGHWh0dHA6Ly9wa2kuZ29vZy9nc3IxL2dzcjEuY3J0MDIGA1UdHwQrMCkwJ6AloCOGIWh0dHA6Ly9jcmwucGtpLmdvb2cvZ3NyMS9nc3IxLmNybDA7BgNVHSAENDAyMAgGBmeBDAECATAIBgZngQwBAgIwDQYLKwYBBAHWeQIFAwIwDQYLKwYBBAHWeQIFAwMwDQYJKoZIhvcNAQELBQADggEBADSkHrEoo9C0dhemMXoh6dFSPsjbdBZBiLg9NR3t5P+T4Vxfq7vqfM/b5A3Ri1fyJm9bvhdGaJQ3b2t6yMAYN/olUazsaL+yyEn9WprKASOshIArAoyZl+tJaox118fessmXn1hIVw41oeQa1v1vg4Fv74zPl6/AhSrw9U5pCZEt4Wi4wStz6dTZ/CLANx8LZh1J7QJVj2fhMtfTJr9w4z30Z209fOU0iOMy+qduBmpvvYuR7hZL6Dupszfnw0Skfths18dG9ZKb59UhvmaSGZRVbNQpsg3BZlvid0lIKO2d1xozclOzgjXPYovJJIultzkMu34qQb9Sz/yilrbCgj8=",
              "format": "base64"
            }
          ],
          "server_name": "8.8.8.8",
          "t": 1.086645955,
          "tags": [],
          "tls_version": "TLSv1.3"
        }
      },
      {
        "network_events": [
          {
            "failure": null,
            "operation": "quic_handshake_start",
            "t": 2.008442629
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "udp",
            "t": 2.00917576
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 2.033215776
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "udp",
            "t": 2.033914372
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 2.098895028
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 2.099016975
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 2.099037821
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 44,
            "operation": "write_to",
            "proto": "udp",
            "t": 2.099202127
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 44,
            "operation": "write_to",
            "proto": "udp",
            "t": 2.099224043
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 2.09929381
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 123,
            "operation": "read_from",
            "proto": "udp",
            "t": 2.099318502
          },
          {
            "failure": null,
            "operation": "quic_handshake_done",
            "t": 2.102363616
          }
        ],
        "quic_handshakes": {
          "network": "quic",
          "address": "8.8.8.8:443",
          "cipher_suite": "TLS_AES_128_GCM_SHA256",
          "failure": null,
          "negotiated_protocol": "h3",
          "no_tls_verify": false,
          "peer_certificates": [
            {
              "data": "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",
              "format": "base64"
            },
            {
              "data": "MIIFljCCA36gAwIBAgINAgO8U1lrNMcY9QFQZjANBgkqhkiG9w0BAQsFADBHMQswCQYDVQQGEwJVUzEiMCAGA1UEChMZR29vZ2xlIFRydXN0IFNlcnZpY2VzIExMQzEUMBIGA1UEAxMLR1RTIFJvb3QgUjEwHhcNMjAwODEzMDAwMDQyWhcNMjcwOTMwMDAwMDQyWjBGMQswCQYDVQQGEwJVUzEiMCAGA1UEChMZR29vZ2xlIFRydXN0IFNlcnZpY2VzIExMQzETMBEGA1UEAxMKR1RTIENBIDFDMzCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAPWI3+dijB43+DdCkH9sh9D7ZYIl/ejLa6T/belaI+KZ9hzpkgOZE3wJCor6QtZeViSqejOEH9Hpabu5dOxXTGZok3c3VVP+ORBNtzS7XyV3NzsXlOo85Z3VvMO0Q+sup0fvsEQRY9i0QYXdQTBIkxu/t/bgRQIh4JZCF8/ZK2VWNAcmBA2o/X3KLu/qSHw3TT8An4Pf73WELnlXXPxXbhqW//yMmqaZviXZf5YsBvcRKgKAgOtjGDxQSYflispfGStZloEAoPtR28p3CwvJlk/vcEnHXG0g/Zm0tOLKLnf9LdwLtmsTDIwZKxeWmLnwi/agJ7u2441Rj72ux5uxiZ0CAwEAAaOCAYAwggF8MA4GA1UdDwEB/wQEAwIBhjAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwEgYDVR0TAQH/BAgwBgEB/wIBADAdBgNVHQ4EFgQUinR/r4XN7pXNPZzQ4kYU83E1HScwHwYDVR0jBBgwFoAU5K8rJnEaK0gnhS9SZizv8IkTcT4waAYIKwYBBQUHAQEEXDBaMCYGCCsGAQUFBzABhhpodHRwOi8vb2NzcC5wa2kuZ29vZy9ndHNyMTAwBggrBgEFBQcwAoYkaHR0cDovL3BraS5nb29nL3JlcG8vY2VydHMvZ3RzcjEuZGVyMDQGA1UdHwQtMCswKaAnoCWGI2h0dHA6Ly9jcmwucGtpLmdvb2cvZ3RzcjEvZ3RzcjEuY3JsMFcGA1UdIARQME4wOAYKKwYBBAHWeQIFAzAqMCgGCCsGAQUFBwIBFhxodHRwczovL3BraS5nb29nL3JlcG9zaXRvcnkvMAgGBmeBDAECATAIBgZngQwBAgIwDQYJKoZIhvcNAQELBQADggIBAIl9rCBcDDy+mqhXlRu0rvqrpXJxtDaV/d9AEQNMwkYUuxQkq/BQcSLbrcRuf8/xam/IgxvYzolfh2yHuKkMo5uhYpSTld9brmYZCwKWnvy15xBpPnrLRklfRuFBsdeYTWU0AIAaP0+fbH9JAIFTQaSSIYKCGvGjRFsqUBITTcFTNvNCCK9U+o53UxtkOCcXCb1YyRt8OS1b887U7ZfbFAO/CVMkH8IMBHmYJvJh8VNS/UKMG2YrPxWhu//2m+OBmgEGcYk1KCTd4b3rGS3hSMs9WYNRtHTGnXzGsYZbr8w0xNPM1IERlQCh9BIiAfq0g3GvjLeMcySsN1PCAJA/Ef5c7TaUEDu9Ka7ixzpiO2xj2YC/WXGsYye5TBeg2vZzFb8q3o/zpWwygTMD0IZRcZk0upONXbVRWPeyk+gB9lm+cZv9TSjOz23HFtz30dZGm6fKa+l3D/2gthsjgx0QGtkJAITgRNOidSOzNIb2ILCkXhAd4FJGAJ2xDx8hcFH1mt0G/FX0Kw4zd8NLQsLxdxP8c4CU6x+7Nz/OAipmsHMdMqUybDKwjuDEI/9bfU1lcKwrmz3O2+BtjjKAvpafkmO8l7tdufThcV4q5O8DIrGKZTqPwJNl1IXNDw9bg1kWRxYtnCQ6yICmJhSFm/Y3m6xv+cXDBlHz4n/FsRC6UfTd",
              "format": "base64"
            },
            {
              "data": "MIIFYjCCBEqgAwIBAgIQd70NbNs2+RrqIQ/E8FjTDTANBgkqhkiG9w0BAQsFADBXMQswCQYDVQQGEwJCRTEZMBcGA1UEChMQR2xvYmFsU2lnbiBudi1zYTEQMA4GA1UECxMHUm9vdCBDQTEbMBkGA1UEAxMSR2xvYmFsU2lnbiBSb290IENBMB4XDTIwMDYxOTAwMDA0MloXDTI4MDEyODAwMDA0MlowRzELMAkGA1UEBhMCVVMxIjAgBgNVBAoTGUdvb2dsZSBUcnVzdCBTZXJ2aWNlcyBMTEMxFDASBgNVBAMTC0dUUyBSb290IFIxMIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAthECix7joXebO9y/lD63ladAPKH9gvl9MgaCcfb2jH/76Nu8ai6Xl6OMS/kr9rH5zoQdsfnFl97vufKj6bwSiV6nqlKr+CMny6SxnGPb15l+8Ape62im9MZaRw1NEDPjTrETo8gYbEvs/AmQ351kKSUjB6G00j0uYODP0gmHu81I8E3CwnqIiru6z1kZ1q+PsAewnjHxgsHA3y6mbWwZDrXYfiYaRQM9sHmklCitD38m5agI/pboPGiUU+6DOogrFZYJsuB6jC511pzrp1Zkj5ZPaK49l8KEj8C8QMALXL32h7M1bKwYUH+E4EzNktMg6TO8UpmvMrUpsyUqtEj5cuHKZPfmghCN6J3Cioj6OGaK/GP5Afl4/Xtcd/p2h/rs37EOeZVXtL0m79YB0esWCruOC7XFxYpVq9Os6pFLKcwZpDIlTirxZUTQAs6qzkm06p98g7BAe+dDq6dso499iYH6TKX/1Y7DzkvgtdizjkXPdsDtQCv9Uw+wp9U7DbGKogPeMa3Md+pvez7W35EiEua++tgy/BBjFFFy3l3WFpO9KWgz7zpm7AeKJt8T11dleCfeXkkUAKIAf5qoIbapsZWwpbkNFhHax2xIPEDgfg1azVY80ZcFuctL7TlLnMQ/0lUTbiSw1nH69MG6zO0b9f6BQdgAmD06yK56mDcYBZUCAwEAAaOCATgwggE0MA4GA1UdDwEB/wQEAwIBhjAPBgNVHRMBAf8EBTADAQH/MB0GA1UdDgQWBBTkrysmcRorSCeFL1JmLO/wiRNxPjAfBgNVHSMEGDAWgBRge2YaRQ2XyolQL30EzTSo//z9SzBgBggrBgEFBQcBAQRUMFIwJQYIKwYBBQUHMAGGGWh0dHA6Ly9vY3NwLnBraS5nb29nL2dzcjEwKQYIKwYBBQUHMAKGHWh0dHA6Ly9wa2kuZ29vZy9nc3IxL2dzcjEuY3J0MDIGA1UdHwQrMCkwJ6AloCOGIWh0dHA6Ly9jcmwucGtpLmdvb2cvZ3NyMS9nc3IxLmNybDA7BgNVHSAENDAyMAgGBmeBDAECATAIBgZngQwBAgIwDQYLKwYBBAHWeQIFAwIwDQYLKwYBBAHWeQIFAwMwDQYJKoZIhvcNAQELBQADggEBADSkHrEoo9C0dhemMXoh6dFSPsjbdBZBiLg9NR3t5P+T4Vxfq7vqfM/b5A3Ri1fyJm9bvhdGaJQ3b2t6yMAYN/olUazsaL+yyEn9WprKASOshIArAoyZl+tJaox118fessmXn1hIVw41oeQa1v1vg4Fv74zPl6/AhSrw9U5pCZEt4Wi4wStz6dTZ/CLANx8LZh1J7QJVj2fhMtfTJr9w4z30Z209fOU0iOMy+qduBmpvvYuR7hZL6Dupszfnw0Skfths18dG9ZKb59UhvmaSGZRVbNQpsg3BZlvid0lIKO2d1xozclOzgjXPYovJJIultzkMu34qQb9Sz/yilrbCgj8=",
              "format": "base64"
            }
          ],
          "server_name": "8.8.8.8",
          "t": 2.102363616,
          "tags": [],
          "tls_version": "TLSv1.3"
        }
      },
      {
        "network_events": [
          {
            "failure": null,
            "operation": "quic_handshake_start",
            "t": 3.00324862
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "udp",
            "t": 3.003568881
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 3.021455754
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "udp",
            "t": 3.02208131
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "udp",
            "t": 3.077059095
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 3.084783124
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 3.085638049
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 44,
            "operation": "write_to",
            "proto": "udp",
            "t": 3.085844816
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 3.086282195
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 3.086305943
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 3.08631663
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 108,
            "operation": "read_from",
            "proto": "udp",
            "t": 3.08634119
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 44,
            "operation": "write_to",
            "proto": "udp",
            "t": 3.086614604
          },
          {
            "failure": null,
            "operation": "quic_handshake_done",
            "t": 3.090623112
          }
        ],
        "quic_handshakes": {
          "network": "quic",
          "address": "8.8.8.8:443",
          "cipher_suite": "TLS_AES_128_GCM_SHA256",
          "failure": null,
          "negotiated_protocol": "h3",
          "no_tls_verify": false,
          "peer_certificates": [
            {
              "data": "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",
              "format": "base64"
            },
            {
              "data": "MIIFljCCA36gAwIBAgINAgO8U1lrNMcY9QFQZjANBgkqhkiG9w0BAQsFADBHMQswCQYDVQQGEwJVUzEiMCAGA1UEChMZR29vZ2xlIFRydXN0IFNlcnZpY2VzIExMQzEUMBIGA1UEAxMLR1RTIFJvb3QgUjEwHhcNMjAwODEzMDAwMDQyWhcNMjcwOTMwMDAwMDQyWjBGMQswCQYDVQQGEwJVUzEiMCAGA1UEChMZR29vZ2xlIFRydXN0IFNlcnZpY2VzIExMQzETMBEGA1UEAxMKR1RTIENBIDFDMzCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAPWI3+dijB43+DdCkH9sh9D7ZYIl/ejLa6T/belaI+KZ9hzpkgOZE3wJCor6QtZeViSqejOEH9Hpabu5dOxXTGZok3c3VVP+ORBNtzS7XyV3NzsXlOo85Z3VvMO0Q+sup0fvsEQRY9i0QYXdQTBIkxu/t/bgRQIh4JZCF8/ZK2VWNAcmBA2o/X3KLu/qSHw3TT8An4Pf73WELnlXXPxXbhqW//yMmqaZviXZf5YsBvcRKgKAgOtjGDxQSYflispfGStZloEAoPtR28p3CwvJlk/vcEnHXG0g/Zm0tOLKLnf9LdwLtmsTDIwZKxeWmLnwi/agJ7u2441Rj72ux5uxiZ0CAwEAAaOCAYAwggF8MA4GA1UdDwEB/wQEAwIBhjAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwEgYDVR0TAQH/BAgwBgEB/wIBADAdBgNVHQ4EFgQUinR/r4XN7pXNPZzQ4kYU83E1HScwHwYDVR0jBBgwFoAU5K8rJnEaK0gnhS9SZizv8IkTcT4waAYIKwYBBQUHAQEEXDBaMCYGCCsGAQUFBzABhhpodHRwOi8vb2NzcC5wa2kuZ29vZy9ndHNyMTAwBggrBgEFBQcwAoYkaHR0cDovL3BraS5nb29nL3JlcG8vY2VydHMvZ3RzcjEuZGVyMDQGA1UdHwQtMCswKaAnoCWGI2h0dHA6Ly9jcmwucGtpLmdvb2cvZ3RzcjEvZ3RzcjEuY3JsMFcGA1UdIARQME4wOAYKKwYBBAHWeQIFAzAqMCgGCCsGAQUFBwIBFhxodHRwczovL3BraS5nb29nL3JlcG9zaXRvcnkvMAgGBmeBDAECATAIBgZngQwBAgIwDQYJKoZIhvcNAQELBQADggIBAIl9rCBcDDy+mqhXlRu0rvqrpXJxtDaV/d9AEQNMwkYUuxQkq/BQcSLbrcRuf8/xam/IgxvYzolfh2yHuKkMo5uhYpSTld9brmYZCwKWnvy15xBpPnrLRklfRuFBsdeYTWU0AIAaP0+fbH9JAIFTQaSSIYKCGvGjRFsqUBITTcFTNvNCCK9U+o53UxtkOCcXCb1YyRt8OS1b887U7ZfbFAO/CVMkH8IMBHmYJvJh8VNS/UKMG2YrPxWhu//2m+OBmgEGcYk1KCTd4b3rGS3hSMs9WYNRtHTGnXzGsYZbr8w0xNPM1IERlQCh9BIiAfq0g3GvjLeMcySsN1PCAJA/Ef5c7TaUEDu9Ka7ixzpiO2xj2YC/WXGsYye5TBeg2vZzFb8q3o/zpWwygTMD0IZRcZk0upONXbVRWPeyk+gB9lm+cZv9TSjOz23HFtz30dZGm6fKa+l3D/2gthsjgx0QGtkJAITgRNOidSOzNIb2ILCkXhAd4FJGAJ2xDx8hcFH1mt0G/FX0Kw4zd8NLQsLxdxP8c4CU6x+7Nz/OAipmsHMdMqUybDKwjuDEI/9bfU1lcKwrmz3O2+BtjjKAvpafkmO8l7tdufThcV4q5O8DIrGKZTqPwJNl1IXNDw9bg1kWRxYtnCQ6yICmJhSFm/Y3m6xv+cXDBlHz4n/FsRC6UfTd",
              "format": "base64"
            },
            {
              "data": "MIIFYjCCBEqgAwIBAgIQd70NbNs2+RrqIQ/E8FjTDTANBgkqhkiG9w0BAQsFADBXMQswCQYDVQQGEwJCRTEZMBcGA1UEChMQR2xvYmFsU2lnbiBudi1zYTEQMA4GA1UECxMHUm9vdCBDQTEbMBkGA1UEAxMSR2xvYmFsU2lnbiBSb290IENBMB4XDTIwMDYxOTAwMDA0MloXDTI4MDEyODAwMDA0MlowRzELMAkGA1UEBhMCVVMxIjAgBgNVBAoTGUdvb2dsZSBUcnVzdCBTZXJ2aWNlcyBMTEMxFDASBgNVBAMTC0dUUyBSb290IFIxMIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAthECix7joXebO9y/lD63ladAPKH9gvl9MgaCcfb2jH/76Nu8ai6Xl6OMS/kr9rH5zoQdsfnFl97vufKj6bwSiV6nqlKr+CMny6SxnGPb15l+8Ape62im9MZaRw1NEDPjTrETo8gYbEvs/AmQ351kKSUjB6G00j0uYODP0gmHu81I8E3CwnqIiru6z1kZ1q+PsAewnjHxgsHA3y6mbWwZDrXYfiYaRQM9sHmklCitD38m5agI/pboPGiUU+6DOogrFZYJsuB6jC511pzrp1Zkj5ZPaK49l8KEj8C8QMALXL32h7M1bKwYUH+E4EzNktMg6TO8UpmvMrUpsyUqtEj5cuHKZPfmghCN6J3Cioj6OGaK/GP5Afl4/Xtcd/p2h/rs37EOeZVXtL0m79YB0esWCruOC7XFxYpVq9Os6pFLKcwZpDIlTirxZUTQAs6qzkm06p98g7BAe+dDq6dso499iYH6TKX/1Y7DzkvgtdizjkXPdsDtQCv9Uw+wp9U7DbGKogPeMa3Md+pvez7W35EiEua++tgy/BBjFFFy3l3WFpO9KWgz7zpm7AeKJt8T11dleCfeXkkUAKIAf5qoIbapsZWwpbkNFhHax2xIPEDgfg1azVY80ZcFuctL7TlLnMQ/0lUTbiSw1nH69MG6zO0b9f6BQdgAmD06yK56mDcYBZUCAwEAAaOCATgwggE0MA4GA1UdDwEB/wQEAwIBhjAPBgNVHRMBAf8EBTADAQH/MB0GA1UdDgQWBBTkrysmcRorSCeFL1JmLO/wiRNxPjAfBgNVHSMEGDAWgBRge2YaRQ2XyolQL30EzTSo//z9SzBgBggrBgEFBQcBAQRUMFIwJQYIKwYBBQUHMAGGGWh0dHA6Ly9vY3NwLnBraS5nb29nL2dzcjEwKQYIKwYBBQUHMAKGHWh0dHA6Ly9wa2kuZ29vZy9nc3IxL2dzcjEuY3J0MDIGA1UdHwQrMCkwJ6AloCOGIWh0dHA6Ly9jcmwucGtpLmdvb2cvZ3NyMS9nc3IxLmNybDA7BgNVHSAENDAyMAgGBmeBDAECATAIBgZngQwBAgIwDQYLKwYBBAHWeQIFAwIwDQYLKwYBBAHWeQIFAwMwDQYJKoZIhvcNAQELBQADggEBADSkHrEoo9C0dhemMXoh6dFSPsjbdBZBiLg9NR3t5P+T4Vxfq7vqfM/b5A3Ri1fyJm9bvhdGaJQ3b2t6yMAYN/olUazsaL+yyEn9WprKASOshIArAoyZl+tJaox118fessmXn1hIVw41oeQa1v1vg4Fv74zPl6/AhSrw9U5pCZEt4Wi4wStz6dTZ/CLANx8LZh1J7QJVj2fhMtfTJr9w4z30Z209fOU0iOMy+qduBmpvvYuR7hZL6Dupszfnw0Skfths18dG9ZKb59UhvmaSGZRVbNQpsg3BZlvid0lIKO2d1xozclOzgjXPYovJJIultzkMu34qQb9Sz/yilrbCgj8=",
              "format": "base64"
            }
          ],
          "server_name": "8.8.8.8",
          "t": 3.090623112,
          "tags": [],
          "tls_version": "TLSv1.3"
        }
      },
      {
        "network_events": [
          {
            "failure": null,
            "operation": "quic_handshake_start",
            "t": 4.003826861
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "udp",
            "t": 4.004164297
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 4.020191375
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "udp",
            "t": 4.020823752
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "udp",
            "t": 4.070228486
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 4.081728314
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 4.087528496
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 4.087566104
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 4.087684585
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1249,
            "operation": "read_from",
            "proto": "udp",
            "t": 4.087711426
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 63,
            "operation": "read_from",
            "proto": "udp",
            "t": 4.087722943
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 44,
            "operation": "write_to",
            "proto": "udp",
            "t": 4.087934272
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 44,
            "operation": "write_to",
            "proto": "udp",
            "t": 4.08795555
          },
          {
            "failure": null,
            "operation": "quic_handshake_done",
            "t": 4.090551059
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 83,
            "operation": "write_to",
            "proto": "udp",
            "t": 4.09061
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 33,
            "operation": "write_to",
            "proto": "udp",
            "t": 4.090637458
          }
        ],
        "quic_handshakes": {
          "network": "quic",
          "address": "8.8.8.8:443",
          "cipher_suite": "TLS_AES_128_GCM_SHA256",
          "failure": null,
          "negotiated_protocol": "h3",
          "no_tls_verify": false,
          "peer_certificates": [
            {
              "data": "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",
              "format": "base64"
            },
            {
              "data": "MIIFljCCA36gAwIBAgINAgO8U1lrNMcY9QFQZjANBgkqhkiG9w0BAQsFADBHMQswCQYDVQQGEwJVUzEiMCAGA1UEChMZR29vZ2xlIFRydXN0IFNlcnZpY2VzIExMQzEUMBIGA1UEAxMLR1RTIFJvb3QgUjEwHhcNMjAwODEzMDAwMDQyWhcNMjcwOTMwMDAwMDQyWjBGMQswCQYDVQQGEwJVUzEiMCAGA1UEChMZR29vZ2xlIFRydXN0IFNlcnZpY2VzIExMQzETMBEGA1UEAxMKR1RTIENBIDFDMzCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAPWI3+dijB43+DdCkH9sh9D7ZYIl/ejLa6T/belaI+KZ9hzpkgOZE3wJCor6QtZeViSqejOEH9Hpabu5dOxXTGZok3c3VVP+ORBNtzS7XyV3NzsXlOo85Z3VvMO0Q+sup0fvsEQRY9i0QYXdQTBIkxu/t/bgRQIh4JZCF8/ZK2VWNAcmBA2o/X3KLu/qSHw3TT8An4Pf73WELnlXXPxXbhqW//yMmqaZviXZf5YsBvcRKgKAgOtjGDxQSYflispfGStZloEAoPtR28p3CwvJlk/vcEnHXG0g/Zm0tOLKLnf9LdwLtmsTDIwZKxeWmLnwi/agJ7u2441Rj72ux5uxiZ0CAwEAAaOCAYAwggF8MA4GA1UdDwEB/wQEAwIBhjAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwEgYDVR0TAQH/BAgwBgEB/wIBADAdBgNVHQ4EFgQUinR/r4XN7pXNPZzQ4kYU83E1HScwHwYDVR0jBBgwFoAU5K8rJnEaK0gnhS9SZizv8IkTcT4waAYIKwYBBQUHAQEEXDBaMCYGCCsGAQUFBzABhhpodHRwOi8vb2NzcC5wa2kuZ29vZy9ndHNyMTAwBggrBgEFBQcwAoYkaHR0cDovL3BraS5nb29nL3JlcG8vY2VydHMvZ3RzcjEuZGVyMDQGA1UdHwQtMCswKaAnoCWGI2h0dHA6Ly9jcmwucGtpLmdvb2cvZ3RzcjEvZ3RzcjEuY3JsMFcGA1UdIARQME4wOAYKKwYBBAHWeQIFAzAqMCgGCCsGAQUFBwIBFhxodHRwczovL3BraS5nb29nL3JlcG9zaXRvcnkvMAgGBmeBDAECATAIBgZngQwBAgIwDQYJKoZIhvcNAQELBQADggIBAIl9rCBcDDy+mqhXlRu0rvqrpXJxtDaV/d9AEQNMwkYUuxQkq/BQcSLbrcRuf8/xam/IgxvYzolfh2yHuKkMo5uhYpSTld9brmYZCwKWnvy15xBpPnrLRklfRuFBsdeYTWU0AIAaP0+fbH9JAIFTQaSSIYKCGvGjRFsqUBITTcFTNvNCCK9U+o53UxtkOCcXCb1YyRt8OS1b887U7ZfbFAO/CVMkH8IMBHmYJvJh8VNS/UKMG2YrPxWhu//2m+OBmgEGcYk1KCTd4b3rGS3hSMs9WYNRtHTGnXzGsYZbr8w0xNPM1IERlQCh9BIiAfq0g3GvjLeMcySsN1PCAJA/Ef5c7TaUEDu9Ka7ixzpiO2xj2YC/WXGsYye5TBeg2vZzFb8q3o/zpWwygTMD0IZRcZk0upONXbVRWPeyk+gB9lm+cZv9TSjOz23HFtz30dZGm6fKa+l3D/2gthsjgx0QGtkJAITgRNOidSOzNIb2ILCkXhAd4FJGAJ2xDx8hcFH1mt0G/FX0Kw4zd8NLQsLxdxP8c4CU6x+7Nz/OAipmsHMdMqUybDKwjuDEI/9bfU1lcKwrmz3O2+BtjjKAvpafkmO8l7tdufThcV4q5O8DIrGKZTqPwJNl1IXNDw9bg1kWRxYtnCQ6yICmJhSFm/Y3m6xv+cXDBlHz4n/FsRC6UfTd",
              "format": "base64"
            },
            {
              "data": "MIIFYjCCBEqgAwIBAgIQd70NbNs2+RrqIQ/E8FjTDTANBgkqhkiG9w0BAQsFADBXMQswCQYDVQQGEwJCRTEZMBcGA1UEChMQR2xvYmFsU2lnbiBudi1zYTEQMA4GA1UECxMHUm9vdCBDQTEbMBkGA1UEAxMSR2xvYmFsU2lnbiBSb290IENBMB4XDTIwMDYxOTAwMDA0MloXDTI4MDEyODAwMDA0MlowRzELMAkGA1UEBhMCVVMxIjAgBgNVBAoTGUdvb2dsZSBUcnVzdCBTZXJ2aWNlcyBMTEMxFDASBgNVBAMTC0dUUyBSb290IFIxMIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAthECix7joXebO9y/lD63ladAPKH9gvl9MgaCcfb2jH/76Nu8ai6Xl6OMS/kr9rH5zoQdsfnFl97vufKj6bwSiV6nqlKr+CMny6SxnGPb15l+8Ape62im9MZaRw1NEDPjTrETo8gYbEvs/AmQ351kKSUjB6G00j0uYODP0gmHu81I8E3CwnqIiru6z1kZ1q+PsAewnjHxgsHA3y6mbWwZDrXYfiYaRQM9sHmklCitD38m5agI/pboPGiUU+6DOogrFZYJsuB6jC511pzrp1Zkj5ZPaK49l8KEj8C8QMALXL32h7M1bKwYUH+E4EzNktMg6TO8UpmvMrUpsyUqtEj5cuHKZPfmghCN6J3Cioj6OGaK/GP5Afl4/Xtcd/p2h/rs37EOeZVXtL0m79YB0esWCruOC7XFxYpVq9Os6pFLKcwZpDIlTirxZUTQAs6qzkm06p98g7BAe+dDq6dso499iYH6TKX/1Y7DzkvgtdizjkXPdsDtQCv9Uw+wp9U7DbGKogPeMa3Md+pvez7W35EiEua++tgy/BBjFFFy3l3WFpO9KWgz7zpm7AeKJt8T11dleCfeXkkUAKIAf5qoIbapsZWwpbkNFhHax2xIPEDgfg1azVY80ZcFuctL7TlLnMQ/0lUTbiSw1nH69MG6zO0b9f6BQdgAmD06yK56mDcYBZUCAwEAAaOCATgwggE0MA4GA1UdDwEB/wQEAwIBhjAPBgNVHRMBAf8EBTADAQH/MB0GA1UdDgQWBBTkrysmcRorSCeFL1JmLO/wiRNxPjAfBgNVHSMEGDAWgBRge2YaRQ2XyolQL30EzTSo//z9SzBgBggrBgEFBQcBAQRUMFIwJQYIKwYBBQUHMAGGGWh0dHA6Ly9vY3NwLnBraS5nb29nL2dzcjEwKQYIKwYBBQUHMAKGHWh0dHA6Ly9wa2kuZ29vZy9nc3IxL2dzcjEuY3J0MDIGA1UdHwQrMCkwJ6AloCOGIWh0dHA6Ly9jcmwucGtpLmdvb2cvZ3NyMS9nc3IxLmNybDA7BgNVHSAENDAyMAgGBmeBDAECATAIBgZngQwBAgIwDQYLKwYBBAHWeQIFAwIwDQYLKwYBBAHWeQIFAwMwDQYJKoZIhvcNAQELBQADggEBADSkHrEoo9C0dhemMXoh6dFSPsjbdBZBiLg9NR3t5P+T4Vxfq7vqfM/b5A3Ri1fyJm9bvhdGaJQ3b2t6yMAYN/olUazsaL+yyEn9WprKASOshIArAoyZl+tJaox118fessmXn1hIVw41oeQa1v1vg4Fv74zPl6/AhSrw9U5pCZEt4Wi4wStz6dTZ/CLANx8LZh1J7QJVj2fhMtfTJr9w4z30Z209fOU0iOMy+qduBmpvvYuR7hZL6Dupszfnw0Skfths18dG9ZKb59UhvmaSGZRVbNQpsg3BZlvid0lIKO2d1xozclOzgjXPYovJJIultzkMu34qQb9Sz/yilrbCgj8=",
              "format": "base64"
            }
          ],
          "server_name": "8.8.8.8",
          "t": 4.090551059,
          "tags": [],
          "tls_version": "TLSv1.3"
        }
      },
      {
        "network_events": [
          {
            "failure": null,
            "operation": "quic_handshake_start",
            "t": 5.007043224
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "udp",
            "t": 5.007261082
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 5.017874613
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "udp",
            "t": 5.018085196
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "udp",
            "t": 5.050926513
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 5.058526227
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 5.083785046
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 5.083917018
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 44,
            "operation": "write_to",
            "proto": "udp",
            "t": 5.084071656
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 5.08411849
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 5.08414175
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 119,
            "operation": "read_from",
            "proto": "udp",
            "t": 5.084150756
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 44,
            "operation": "write_to",
            "proto": "udp",
            "t": 5.084337061
          },
          {
            "failure": null,
            "operation": "quic_handshake_done",
            "t": 5.086838298
          }
        ],
        "quic_handshakes": {
          "network": "quic",
          "address": "8.8.8.8:443",
          "cipher_suite": "TLS_AES_128_GCM_SHA256",
          "failure": null,
          "negotiated_protocol": "h3",
          "no_tls_verify": false,
          "peer_certificates": [
            {
              "data": "MIIF4jCCBMqgAwIBAgIQYLacZz2eOBASS1n19sZtajANBgkqhkiG9w0BAQsFADBGMQswCQYDVQQGEwJVUzEiMCAGA1UEChMZR29vZ2xlIFRydXN0IFNlcnZpY2VzIExMQzETMBEGA1UEAxMKR1RTIENBIDFDMzAeFw0yMjA3MTgwODI1MzhaFw0yMjEwMTAwODI1MzdaMBUxEzARBgNVBAMTCmRucy5nb29nbGUwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCyQAmKj3EM0gCcEqbJIj9u/rU0VoKglt90M8TyLLPm5Y7ziAeqE49G1tMKy8B8M1GhFIhDxu4jIE2xly86iDrZqghY9nz8FszJe0Gy8vk4wzoBYimHqHghn0WXvoNoqQRuRGgy13PxMvj20lAD9h4cFJEWw/VYdGTwK4vS5j4SDoQGQcj/X7eZq36i5NbuAIZfD4cOdWj8dcCuNwU7xmwBMhS33zP2IFa2MlL45/VJTsvNwbSA6VwdxFTF69gA/drsEfRs22LzEWfKOi3kgWrmKlkz1ZTk7pWZ3ydyA6o7OOOCkQ72kXzjBRMU30IreQv3hI1fMFzzI576/hjOs6v1AgMBAAGjggL7MIIC9zAOBgNVHQ8BAf8EBAMCBaAwEwYDVR0lBAwwCgYIKwYBBQUHAwEwDAYDVR0TAQH/BAIwADAdBgNVHQ4EFgQUObcc6349QC6ltN92PEMzbu1l59swHwYDVR0jBBgwFoAUinR/r4XN7pXNPZzQ4kYU83E1HScwagYIKwYBBQUHAQEEXjBcMCcGCCsGAQUFBzABhhtodHRwOi8vb2NzcC5wa2kuZ29vZy9ndHMxYzMwMQYIKwYBBQUHMAKGJWh0dHA6Ly9wa2kuZ29vZy9yZXBvL2NlcnRzL2d0czFjMy5kZXIwgawGA1UdEQSBpDCBoYIKZG5zLmdvb2dsZYIOZG5zLmdvb2dsZS5jb22CECouZG5zLmdvb2dsZS5jb22CCzg4ODguZ29vZ2xlghBkbnM2NC5kbnMuZ29vZ2xlhwQICAgIhwQICAQEhxAgAUhgSGAAAAAAAAAAAIiIhxAgAUhgSGAAAAAAAAAAAIhEhxAgAUhgSGAAAAAAAAAAAGRkhxAgAUhgSGAAAAAAAAAAAABkMCEGA1UdIAQaMBgwCAYGZ4EMAQIBMAwGCisGAQQB1nkCBQMwPAYDVR0fBDUwMzAxoC+gLYYraHR0cDovL2NybHMucGtpLmdvb2cvZ3RzMWMzL2ZWSnhiVi1LdG1rLmNybDCCAQQGCisGAQQB1nkCBAIEgfUEgfIA8AB3ACl5vvCeOTkh8FZzn2Old+W+V32cYAr4+U1dJlwlXceEAAABghCgpxAAAAQDAEgwRgIhAO5HAX3da12frKcZhcLh5UxT1W143pWlSbne+tXu9VrwAiEAtdx4+kwTS+0WFIyFDX3am/x+WrePng+fs1LK7gXypdUAdQBByMqx3yJGShDGoToJQodeTjGLGwPr60vHaPCQYpYG9gAAAYIQoKdMAAAEAwBGMEQCIBBdqQ/j6neM28KghIIijNnuHS5HhApFrOq4XiF4t/OqAiAuxt+yqVOLQJgiFAJl4aVFhlssmMAN3Hp9rKuNFg82AjANBgkqhkiG9w0BAQsFAAOCAQEAbIma470MX0QA9vkdEA1LHm4H5ybom3igN3Or8nERpic2FtTrK3hOfm3WPn3Z0uDE5QPne4GiOnkAwfrzVkhwfcQXMDrzj0eONWh0T+8a7C75lGuBiDu2/bvcgrxRERih3DaO1pqPMasDoK/jsi/K364yafmzX9rdZcq3XP+sIRbusGjCma8R4YzrQuRcZ4XICrieTIK73WNQ3zdbFjZPKzKtUDvVP37k/9FGx8bDw1vQb0BoDFeBVtPr/p2B0uIal0UL7qHO+CKOsJuReDPM1x/AXhH/IAyzq26sliAZ/jZGbYocOLwLV1iIzgsfIM7JkhG2odbuySnrcQ4tnYozTA==",
              "format": "base64"
            },
            {
              "data": "MIIFljCCA36gAwIBAgINAgO8U1lrNMcY9QFQZjANBgkqhkiG9w0BAQsFADBHMQswCQYDVQQGEwJVUzEiMCAGA1UEChMZR29vZ2xlIFRydXN0IFNlcnZpY2VzIExMQzEUMBIGA1UEAxMLR1RTIFJvb3QgUjEwHhcNMjAwODEzMDAwMDQyWhcNMjcwOTMwMDAwMDQyWjBGMQswCQYDVQQGEwJVUzEiMCAGA1UEChMZR29vZ2xlIFRydXN0IFNlcnZpY2VzIExMQzETMBEGA1UEAxMKR1RTIENBIDFDMzCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAPWI3+dijB43+DdCkH9sh9D7ZYIl/ejLa6T/belaI+KZ9hzpkgOZE3wJCor6QtZeViSqejOEH9Hpabu5dOxXTGZok3c3VVP+ORBNtzS7XyV3NzsXlOo85Z3VvMO0Q+sup0fvsEQRY9i0QYXdQTBIkxu/t/bgRQIh4JZCF8/ZK2VWNAcmBA2o/X3KLu/qSHw3TT8An4Pf73WELnlXXPxXbhqW//yMmqaZviXZf5YsBvcRKgKAgOtjGDxQSYflispfGStZloEAoPtR28p3CwvJlk/vcEnHXG0g/Zm0tOLKLnf9LdwLtmsTDIwZKxeWmLnwi/agJ7u2441Rj72ux5uxiZ0CAwEAAaOCAYAwggF8MA4GA1UdDwEB/wQEAwIBhjAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwEgYDVR0TAQH/BAgwBgEB/wIBADAdBgNVHQ4EFgQUinR/r4XN7pXNPZzQ4kYU83E1HScwHwYDVR0jBBgwFoAU5K8rJnEaK0gnhS9SZizv8IkTcT4waAYIKwYBBQUHAQEEXDBaMCYGCCsGAQUFBzABhhpodHRwOi8vb2NzcC5wa2kuZ29vZy9ndHNyMTAwBggrBgEFBQcwAoYkaHR0cDovL3BraS5nb29nL3JlcG8vY2VydHMvZ3RzcjEuZGVyMDQGA1UdHwQtMCswKaAnoCWGI2h0dHA6Ly9jcmwucGtpLmdvb2cvZ3RzcjEvZ3RzcjEuY3JsMFcGA1UdIARQME4wOAYKKwYBBAHWeQIFAzAqMCgGCCsGAQUFBwIBFhxodHRwczovL3BraS5nb29nL3JlcG9zaXRvcnkvMAgGBmeBDAECATAIBgZngQwBAgIwDQYJKoZIhvcNAQELBQADggIBAIl9rCBcDDy+mqhXlRu0rvqrpXJxtDaV/d9AEQNMwkYUuxQkq/BQcSLbrcRuf8/xam/IgxvYzolfh2yHuKkMo5uhYpSTld9brmYZCwKWnvy15xBpPnrLRklfRuFBsdeYTWU0AIAaP0+fbH9JAIFTQaSSIYKCGvGjRFsqUBITTcFTNvNCCK9U+o53UxtkOCcXCb1YyRt8OS1b887U7ZfbFAO/CVMkH8IMBHmYJvJh8VNS/UKMG2YrPxWhu//2m+OBmgEGcYk1KCTd4b3rGS3hSMs9WYNRtHTGnXzGsYZbr8w0xNPM1IERlQCh9BIiAfq0g3GvjLeMcySsN1PCAJA/Ef5c7TaUEDu9Ka7ixzpiO2xj2YC/WXGsYye5TBeg2vZzFb8q3o/zpWwygTMD0IZRcZk0upONXbVRWPeyk+gB9lm+cZv9TSjOz23HFtz30dZGm6fKa+l3D/2gthsjgx0QGtkJAITgRNOidSOzNIb2ILCkXhAd4FJGAJ2xDx8hcFH1mt0G/FX0Kw4zd8NLQsLxdxP8c4CU6x+7Nz/OAipmsHMdMqUybDKwjuDEI/9bfU1lcKwrmz3O2+BtjjKAvpafkmO8l7tdufThcV4q5O8DIrGKZTqPwJNl1IXNDw9bg1kWRxYtnCQ6yICmJhSFm/Y3m6xv+cXDBlHz4n/FsRC6UfTd",
              "format": "base64"
            },
            {
              "data": "MIIFYjCCBEqgAwIBAgIQd70NbNs2+RrqIQ/E8FjTDTANBgkqhkiG9w0BAQsFADBXMQswCQYDVQQGEwJCRTEZMBcGA1UEChMQR2xvYmFsU2lnbiBudi1zYTEQMA4GA1UECxMHUm9vdCBDQTEbMBkGA1UEAxMSR2xvYmFsU2lnbiBSb290IENBMB4XDTIwMDYxOTAwMDA0MloXDTI4MDEyODAwMDA0MlowRzELMAkGA1UEBhMCVVMxIjAgBgNVBAoTGUdvb2dsZSBUcnVzdCBTZXJ2aWNlcyBMTEMxFDASBgNVBAMTC0dUUyBSb290IFIxMIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAthECix7joXebO9y/lD63ladAPKH9gvl9MgaCcfb2jH/76Nu8ai6Xl6OMS/kr9rH5zoQdsfnFl97vufKj6bwSiV6nqlKr+CMny6SxnGPb15l+8Ape62im9MZaRw1NEDPjTrETo8gYbEvs/AmQ351kKSUjB6G00j0uYODP0gmHu81I8E3CwnqIiru6z1kZ1q+PsAewnjHxgsHA3y6mbWwZDrXYfiYaRQM9sHmklCitD38m5agI/pboPGiUU+6DOogrFZYJsuB6jC511pzrp1Zkj5ZPaK49l8KEj8C8QMALXL32h7M1bKwYUH+E4EzNktMg6TO8UpmvMrUpsyUqtEj5cuHKZPfmghCN6J3Cioj6OGaK/GP5Afl4/Xtcd/p2h/rs37EOeZVXtL0m79YB0esWCruOC7XFxYpVq9Os6pFLKcwZpDIlTirxZUTQAs6qzkm06p98g7BAe+dDq6dso499iYH6TKX/1Y7DzkvgtdizjkXPdsDtQCv9Uw+wp9U7DbGKogPeMa3Md+pvez7W35EiEua++tgy/BBjFFFy3l3WFpO9KWgz7zpm7AeKJt8T11dleCfeXkkUAKIAf5qoIbapsZWwpbkNFhHax2xIPEDgfg1azVY80ZcFuctL7TlLnMQ/0lUTbiSw1nH69MG6zO0b9f6BQdgAmD06yK56mDcYBZUCAwEAAaOCATgwggE0MA4GA1UdDwEB/wQEAwIBhjAPBgNVHRMBAf8EBTADAQH/MB0GA1UdDgQWBBTkrysmcRorSCeFL1JmLO/wiRNxPjAfBgNVHSMEGDAWgBRge2YaRQ2XyolQL30EzTSo//z9SzBgBggrBgEFBQcBAQRUMFIwJQYIKwYBBQUHMAGGGWh0dHA6Ly9vY3NwLnBraS5nb29nL2dzcjEwKQYIKwYBBQUHMAKGHWh0dHA6Ly9wa2kuZ29vZy9nc3IxL2dzcjEuY3J0MDIGA1UdHwQrMCkwJ6AloCOGIWh0dHA6Ly9jcmwucGtpLmdvb2cvZ3NyMS9nc3IxLmNybDA7BgNVHSAENDAyMAgGBmeBDAECATAIBgZngQwBAgIwDQYLKwYBBAHWeQIFAwIwDQYLKwYBBAHWeQIFAwMwDQYJKoZIhvcNAQELBQADggEBADSkHrEoo9C0dhemMXoh6dFSPsjbdBZBiLg9NR3t5P+T4Vxfq7vqfM/b5A3Ri1fyJm9bvhdGaJQ3b2t6yMAYN/olUazsaL+yyEn9WprKASOshIArAoyZl+tJaox118fessmXn1hIVw41oeQa1v1vg4Fv74zPl6/AhSrw9U5pCZEt4Wi4wStz6dTZ/CLANx8LZh1J7QJVj2fhMtfTJr9w4z30Z209fOU0iOMy+qduBmpvvYuR7hZL6Dupszfnw0Skfths18dG9ZKb59UhvmaSGZRVbNQpsg3BZlvid0lIKO2d1xozclOzgjXPYovJJIultzkMu34qQb9Sz/yilrbCgj8=",
              "format": "base64"
            }
          ],
          "server_name": "8.8.8.8",
          "t": 5.086838298,
          "tags": [],
          "tls_version": "TLSv1.3"
        }
      },
      {
        "network_events": [
          {
            "failure": null,
            "operation": "quic_handshake_start",
            "t": 6.010118227
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "udp",
            "t": 6.010844207
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 6.021071288
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "udp",
            "t": 6.021751674
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "udp",
            "t": 6.053691037
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 6.063204804
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 6.089235709
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 6.089442295
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 44,
            "operation": "write_to",
            "proto": "udp",
            "t": 6.089458063
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 6.089514245
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 44,
            "operation": "write_to",
            "proto": "udp",
            "t": 6.089728818
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 6.089786492
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 114,
            "operation": "read_from",
            "proto": "udp",
            "t": 6.089813793
          },
          {
            "failure": null,
            "operation": "quic_handshake_done",
            "t": 6.092577355
          }
        ],
        "quic_handshakes": {
          "network": "quic",
          "address": "8.8.8.8:443",
          "cipher_suite": "TLS_AES_128_GCM_SHA256",
          "failure": null,
          "negotiated_protocol": "h3",
          "no_tls_verify": false,
          "peer_certificates": [
            {
              "data": "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",
              "format": "base64"
            },
            {
              "data": "MIIFljCCA36gAwIBAgINAgO8U1lrNMcY9QFQZjANBgkqhkiG9w0BAQsFADBHMQswCQYDVQQGEwJVUzEiMCAGA1UEChMZR29vZ2xlIFRydXN0IFNlcnZpY2VzIExMQzEUMBIGA1UEAxMLR1RTIFJvb3QgUjEwHhcNMjAwODEzMDAwMDQyWhcNMjcwOTMwMDAwMDQyWjBGMQswCQYDVQQGEwJVUzEiMCAGA1UEChMZR29vZ2xlIFRydXN0IFNlcnZpY2VzIExMQzETMBEGA1UEAxMKR1RTIENBIDFDMzCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAPWI3+dijB43+DdCkH9sh9D7ZYIl/ejLa6T/belaI+KZ9hzpkgOZE3wJCor6QtZeViSqejOEH9Hpabu5dOxXTGZok3c3VVP+ORBNtzS7XyV3NzsXlOo85Z3VvMO0Q+sup0fvsEQRY9i0QYXdQTBIkxu/t/bgRQIh4JZCF8/ZK2VWNAcmBA2o/X3KLu/qSHw3TT8An4Pf73WELnlXXPxXbhqW//yMmqaZviXZf5YsBvcRKgKAgOtjGDxQSYflispfGStZloEAoPtR28p3CwvJlk/vcEnHXG0g/Zm0tOLKLnf9LdwLtmsTDIwZKxeWmLnwi/agJ7u2441Rj72ux5uxiZ0CAwEAAaOCAYAwggF8MA4GA1UdDwEB/wQEAwIBhjAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwEgYDVR0TAQH/BAgwBgEB/wIBADAdBgNVHQ4EFgQUinR/r4XN7pXNPZzQ4kYU83E1HScwHwYDVR0jBBgwFoAU5K8rJnEaK0gnhS9SZizv8IkTcT4waAYIKwYBBQUHAQEEXDBaMCYGCCsGAQUFBzABhhpodHRwOi8vb2NzcC5wa2kuZ29vZy9ndHNyMTAwBggrBgEFBQcwAoYkaHR0cDovL3BraS5nb29nL3JlcG8vY2VydHMvZ3RzcjEuZGVyMDQGA1UdHwQtMCswKaAnoCWGI2h0dHA6Ly9jcmwucGtpLmdvb2cvZ3RzcjEvZ3RzcjEuY3JsMFcGA1UdIARQME4wOAYKKwYBBAHWeQIFAzAqMCgGCCsGAQUFBwIBFhxodHRwczovL3BraS5nb29nL3JlcG9zaXRvcnkvMAgGBmeBDAECATAIBgZngQwBAgIwDQYJKoZIhvcNAQELBQADggIBAIl9rCBcDDy+mqhXlRu0rvqrpXJxtDaV/d9AEQNMwkYUuxQkq/BQcSLbrcRuf8/xam/IgxvYzolfh2yHuKkMo5uhYpSTld9brmYZCwKWnvy15xBpPnrLRklfRuFBsdeYTWU0AIAaP0+fbH9JAIFTQaSSIYKCGvGjRFsqUBITTcFTNvNCCK9U+o53UxtkOCcXCb1YyRt8OS1b887U7ZfbFAO/CVMkH8IMBHmYJvJh8VNS/UKMG2YrPxWhu//2m+OBmgEGcYk1KCTd4b3rGS3hSMs9WYNRtHTGnXzGsYZbr8w0xNPM1IERlQCh9BIiAfq0g3GvjLeMcySsN1PCAJA/Ef5c7TaUEDu9Ka7ixzpiO2xj2YC/WXGsYye5TBeg2vZzFb8q3o/zpWwygTMD0IZRcZk0upONXbVRWPeyk+gB9lm+cZv9TSjOz23HFtz30dZGm6fKa+l3D/2gthsjgx0QGtkJAITgRNOidSOzNIb2ILCkXhAd4FJGAJ2xDx8hcFH1mt0G/FX0Kw4zd8NLQsLxdxP8c4CU6x+7Nz/OAipmsHMdMqUybDKwjuDEI/9bfU1lcKwrmz3O2+BtjjKAvpafkmO8l7tdufThcV4q5O8DIrGKZTqPwJNl1IXNDw9bg1kWRxYtnCQ6yICmJhSFm/Y3m6xv+cXDBlHz4n/FsRC6UfTd",
              "format": "base64"
            },
            {
              "data": "MIIFYjCCBEqgAwIBAgIQd70NbNs2+RrqIQ/E8FjTDTANBgkqhkiG9w0BAQsFADBXMQswCQYDVQQGEwJCRTEZMBcGA1UEChMQR2xvYmFsU2lnbiBudi1zYTEQMA4GA1UECxMHUm9vdCBDQTEbMBkGA1UEAxMSR2xvYmFsU2lnbiBSb290IENBMB4XDTIwMDYxOTAwMDA0MloXDTI4MDEyODAwMDA0MlowRzELMAkGA1UEBhMCVVMxIjAgBgNVBAoTGUdvb2dsZSBUcnVzdCBTZXJ2aWNlcyBMTEMxFDASBgNVBAMTC0dUUyBSb290IFIxMIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAthECix7joXebO9y/lD63ladAPKH9gvl9MgaCcfb2jH/76Nu8ai6Xl6OMS/kr9rH5zoQdsfnFl97vufKj6bwSiV6nqlKr+CMny6SxnGPb15l+8Ape62im9MZaRw1NEDPjTrETo8gYbEvs/AmQ351kKSUjB6G00j0uYODP0gmHu81I8E3CwnqIiru6z1kZ1q+PsAewnjHxgsHA3y6mbWwZDrXYfiYaRQM9sHmklCitD38m5agI/pboPGiUU+6DOogrFZYJsuB6jC511pzrp1Zkj5ZPaK49l8KEj8C8QMALXL32h7M1bKwYUH+E4EzNktMg6TO8UpmvMrUpsyUqtEj5cuHKZPfmghCN6J3Cioj6OGaK/GP5Afl4/Xtcd/p2h/rs37EOeZVXtL0m79YB0esWCruOC7XFxYpVq9Os6pFLKcwZpDIlTirxZUTQAs6qzkm06p98g7BAe+dDq6dso499iYH6TKX/1Y7DzkvgtdizjkXPdsDtQCv9Uw+wp9U7DbGKogPeMa3Md+pvez7W35EiEua++tgy/BBjFFFy3l3WFpO9KWgz7zpm7AeKJt8T11dleCfeXkkUAKIAf5qoIbapsZWwpbkNFhHax2xIPEDgfg1azVY80ZcFuctL7TlLnMQ/0lUTbiSw1nH69MG6zO0b9f6BQdgAmD06yK56mDcYBZUCAwEAAaOCATgwggE0MA4GA1UdDwEB/wQEAwIBhjAPBgNVHRMBAf8EBTADAQH/MB0GA1UdDgQWBBTkrysmcRorSCeFL1JmLO/wiRNxPjAfBgNVHSMEGDAWgBRge2YaRQ2XyolQL30EzTSo//z9SzBgBggrBgEFBQcBAQRUMFIwJQYIKwYBBQUHMAGGGWh0dHA6Ly9vY3NwLnBraS5nb29nL2dzcjEwKQYIKwYBBQUHMAKGHWh0dHA6Ly9wa2kuZ29vZy9nc3IxL2dzcjEuY3J0MDIGA1UdHwQrMCkwJ6AloCOGIWh0dHA6Ly9jcmwucGtpLmdvb2cvZ3NyMS9nc3IxLmNybDA7BgNVHSAENDAyMAgGBmeBDAECATAIBgZngQwBAgIwDQYLKwYBBAHWeQIFAwIwDQYLKwYBBAHWeQIFAwMwDQYJKoZIhvcNAQELBQADggEBADSkHrEoo9C0dhemMXoh6dFSPsjbdBZBiLg9NR3t5P+T4Vxfq7vqfM/b5A3Ri1fyJm9bvhdGaJQ3b2t6yMAYN/olUazsaL+yyEn9WprKASOshIArAoyZl+tJaox118fessmXn1hIVw41oeQa1v1vg4Fv74zPl6/AhSrw9U5pCZEt4Wi4wStz6dTZ/CLANx8LZh1J7QJVj2fhMtfTJr9w4z30Z209fOU0iOMy+qduBmpvvYuR7hZL6Dupszfnw0Skfths18dG9ZKb59UhvmaSGZRVbNQpsg3BZlvid0lIKO2d1xozclOzgjXPYovJJIultzkMu34qQb9Sz/yilrbCgj8=",
              "format": "base64"
            }
          ],
          "server_name": "8.8.8.8",
          "t": 6.092577355,
          "tags": [],
          "tls_version": "TLSv1.3"
        }
      },
      {
        "network_events": [
          {
            "failure": null,
            "operation": "quic_handshake_start",
            "t": 7.003360563
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "udp",
            "t": 7.003673547
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 7.011959809
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "udp",
            "t": 7.012290748
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "udp",
            "t": 7.038208836
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 7.049088312
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 7.077864269
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 7.077902258
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 7.077920707
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 7.077961526
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 110,
            "operation": "read_from",
            "proto": "udp",
            "t": 7.077972156
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 44,
            "operation": "write_to",
            "proto": "udp",
            "t": 7.07832336
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 44,
            "operation": "write_to",
            "proto": "udp",
            "t": 7.078348752
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 83,
            "operation": "write_to",
            "proto": "udp",
            "t": 7.080901131
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 33,
            "operation": "write_to",
            "proto": "udp",
            "t": 7.080919587
          },
          {
            "failure": null,
            "operation": "quic_handshake_done",
            "t": 7.080906477
          }
        ],
        "quic_handshakes": {
          "network": "quic",
          "address": "8.8.8.8:443",
          "cipher_suite": "TLS_AES_128_GCM_SHA256",
          "failure": null,
          "negotiated_protocol": "h3",
          "no_tls_verify": false,
          "peer_certificates": [
            {
              "data": "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",
              "format": "base64"
            },
            {
              "data": "MIIFljCCA36gAwIBAgINAgO8U1lrNMcY9QFQZjANBgkqhkiG9w0BAQsFADBHMQswCQYDVQQGEwJVUzEiMCAGA1UEChMZR29vZ2xlIFRydXN0IFNlcnZpY2VzIExMQzEUMBIGA1UEAxMLR1RTIFJvb3QgUjEwHhcNMjAwODEzMDAwMDQyWhcNMjcwOTMwMDAwMDQyWjBGMQswCQYDVQQGEwJVUzEiMCAGA1UEChMZR29vZ2xlIFRydXN0IFNlcnZpY2VzIExMQzETMBEGA1UEAxMKR1RTIENBIDFDMzCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAPWI3+dijB43+DdCkH9sh9D7ZYIl/ejLa6T/belaI+KZ9hzpkgOZE3wJCor6QtZeViSqejOEH9Hpabu5dOxXTGZok3c3VVP+ORBNtzS7XyV3NzsXlOo85Z3VvMO0Q+sup0fvsEQRY9i0QYXdQTBIkxu/t/bgRQIh4JZCF8/ZK2VWNAcmBA2o/X3KLu/qSHw3TT8An4Pf73WELnlXXPxXbhqW//yMmqaZviXZf5YsBvcRKgKAgOtjGDxQSYflispfGStZloEAoPtR28p3CwvJlk/vcEnHXG0g/Zm0tOLKLnf9LdwLtmsTDIwZKxeWmLnwi/agJ7u2441Rj72ux5uxiZ0CAwEAAaOCAYAwggF8MA4GA1UdDwEB/wQEAwIBhjAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwEgYDVR0TAQH/BAgwBgEB/wIBADAdBgNVHQ4EFgQUinR/r4XN7pXNPZzQ4kYU83E1HScwHwYDVR0jBBgwFoAU5K8rJnEaK0gnhS9SZizv8IkTcT4waAYIKwYBBQUHAQEEXDBaMCYGCCsGAQUFBzABhhpodHRwOi8vb2NzcC5wa2kuZ29vZy9ndHNyMTAwBggrBgEFBQcwAoYkaHR0cDovL3BraS5nb29nL3JlcG8vY2VydHMvZ3RzcjEuZGVyMDQGA1UdHwQtMCswKaAnoCWGI2h0dHA6Ly9jcmwucGtpLmdvb2cvZ3RzcjEvZ3RzcjEuY3JsMFcGA1UdIARQME4wOAYKKwYBBAHWeQIFAzAqMCgGCCsGAQUFBwIBFhxodHRwczovL3BraS5nb29nL3JlcG9zaXRvcnkvMAgGBmeBDAECATAIBgZngQwBAgIwDQYJKoZIhvcNAQELBQADggIBAIl9rCBcDDy+mqhXlRu0rvqrpXJxtDaV/d9AEQNMwkYUuxQkq/BQcSLbrcRuf8/xam/IgxvYzolfh2yHuKkMo5uhYpSTld9brmYZCwKWnvy15xBpPnrLRklfRuFBsdeYTWU0AIAaP0+fbH9JAIFTQaSSIYKCGvGjRFsqUBITTcFTNvNCCK9U+o53UxtkOCcXCb1YyRt8OS1b887U7ZfbFAO/CVMkH8IMBHmYJvJh8VNS/UKMG2YrPxWhu//2m+OBmgEGcYk1KCTd4b3rGS3hSMs9WYNRtHTGnXzGsYZbr8w0xNPM1IERlQCh9BIiAfq0g3GvjLeMcySsN1PCAJA/Ef5c7TaUEDu9Ka7ixzpiO2xj2YC/WXGsYye5TBeg2vZzFb8q3o/zpWwygTMD0IZRcZk0upONXbVRWPeyk+gB9lm+cZv9TSjOz23HFtz30dZGm6fKa+l3D/2gthsjgx0QGtkJAITgRNOidSOzNIb2ILCkXhAd4FJGAJ2xDx8hcFH1mt0G/FX0Kw4zd8NLQsLxdxP8c4CU6x+7Nz/OAipmsHMdMqUybDKwjuDEI/9bfU1lcKwrmz3O2+BtjjKAvpafkmO8l7tdufThcV4q5O8DIrGKZTqPwJNl1IXNDw9bg1kWRxYtnCQ6yICmJhSFm/Y3m6xv+cXDBlHz4n/FsRC6UfTd",
              "format": "base64"
            },
            {
              "data": "MIIFYjCCBEqgAwIBAgIQd70NbNs2+RrqIQ/E8FjTDTANBgkqhkiG9w0BAQsFADBXMQswCQYDVQQGEwJCRTEZMBcGA1UEChMQR2xvYmFsU2lnbiBudi1zYTEQMA4GA1UECxMHUm9vdCBDQTEbMBkGA1UEAxMSR2xvYmFsU2lnbiBSb290IENBMB4XDTIwMDYxOTAwMDA0MloXDTI4MDEyODAwMDA0MlowRzELMAkGA1UEBhMCVVMxIjAgBgNVBAoTGUdvb2dsZSBUcnVzdCBTZXJ2aWNlcyBMTEMxFDASBgNVBAMTC0dUUyBSb290IFIxMIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAthECix7joXebO9y/lD63ladAPKH9gvl9MgaCcfb2jH/76Nu8ai6Xl6OMS/kr9rH5zoQdsfnFl97vufKj6bwSiV6nqlKr+CMny6SxnGPb15l+8Ape62im9MZaRw1NEDPjTrETo8gYbEvs/AmQ351kKSUjB6G00j0uYODP0gmHu81I8E3CwnqIiru6z1kZ1q+PsAewnjHxgsHA3y6mbWwZDrXYfiYaRQM9sHmklCitD38m5agI/pboPGiUU+6DOogrFZYJsuB6jC511pzrp1Zkj5ZPaK49l8KEj8C8QMALXL32h7M1bKwYUH+E4EzNktMg6TO8UpmvMrUpsyUqtEj5cuHKZPfmghCN6J3Cioj6OGaK/GP5Afl4/Xtcd/p2h/rs37EOeZVXtL0m79YB0esWCruOC7XFxYpVq9Os6pFLKcwZpDIlTirxZUTQAs6qzkm06p98g7BAe+dDq6dso499iYH6TKX/1Y7DzkvgtdizjkXPdsDtQCv9Uw+wp9U7DbGKogPeMa3Md+pvez7W35EiEua++tgy/BBjFFFy3l3WFpO9KWgz7zpm7AeKJt8T11dleCfeXkkUAKIAf5qoIbapsZWwpbkNFhHax2xIPEDgfg1azVY80ZcFuctL7TlLnMQ/0lUTbiSw1nH69MG6zO0b9f6BQdgAmD06yK56mDcYBZUCAwEAAaOCATgwggE0MA4GA1UdDwEB/wQEAwIBhjAPBgNVHRMBAf8EBTADAQH/MB0GA1UdDgQWBBTkrysmcRorSCeFL1JmLO/wiRNxPjAfBgNVHSMEGDAWgBRge2YaRQ2XyolQL30EzTSo//z9SzBgBggrBgEFBQcBAQRUMFIwJQYIKwYBBQUHMAGGGWh0dHA6Ly9vY3NwLnBraS5nb29nL2dzcjEwKQYIKwYBBQUHMAKGHWh0dHA6Ly9wa2kuZ29vZy9nc3IxL2dzcjEuY3J0MDIGA1UdHwQrMCkwJ6AloCOGIWh0dHA6Ly9jcmwucGtpLmdvb2cvZ3NyMS9nc3IxLmNybDA7BgNVHSAENDAyMAgGBmeBDAECATAIBgZngQwBAgIwDQYLKwYBBAHWeQIFAwIwDQYLKwYBBAHWeQIFAwMwDQYJKoZIhvcNAQELBQADggEBADSkHrEoo9C0dhemMXoh6dFSPsjbdBZBiLg9NR3t5P+T4Vxfq7vqfM/b5A3Ri1fyJm9bvhdGaJQ3b2t6yMAYN/olUazsaL+yyEn9WprKASOshIArAoyZl+tJaox118fessmXn1hIVw41oeQa1v1vg4Fv74zPl6/AhSrw9U5pCZEt4Wi4wStz6dTZ/CLANx8LZh1J7QJVj2fhMtfTJr9w4z30Z209fOU0iOMy+qduBmpvvYuR7hZL6Dupszfnw0Skfths18dG9ZKb59UhvmaSGZRVbNQpsg3BZlvid0lIKO2d1xozclOzgjXPYovJJIultzkMu34qQb9Sz/yilrbCgj8=",
              "format": "base64"
            }
          ],
          "server_name": "8.8.8.8",
          "t": 7.080906477,
          "tags": [],
          "tls_version": "TLSv1.3"
        }
      },
      {
        "network_events": [
          {
            "failure": null,
            "operation": "quic_handshake_start",
            "t": 8.007821924
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "udp",
            "t": 8.008028556
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 8.016433214
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "udp",
            "t": 8.016668242
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "udp",
            "t": 8.042378633
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 8.050643131
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 8.084451492
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 8.084513563
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 44,
            "operation": "write_to",
            "proto": "udp",
            "t": 8.084775082
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 8.084807443
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 8.084840767
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 123,
            "operation": "read_from",
            "proto": "udp",
            "t": 8.084856627
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 44,
            "operation": "write_to",
            "proto": "udp",
            "t": 8.085075136
          },
          {
            "failure": null,
            "operation": "quic_handshake_done",
            "t": 8.087711639
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 83,
            "operation": "write_to",
            "proto": "udp",
            "t": 8.08776711
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 33,
            "operation": "write_to",
            "proto": "udp",
            "t": 8.08780511
          }
        ],
        "quic_handshakes": {
          "network": "quic",
          "address": "8.8.8.8:443",
          "cipher_suite": "TLS_AES_128_GCM_SHA256",
          "failure": null,
          "negotiated_protocol": "h3",
          "no_tls_verify": false,
          "peer_certificates": [
            {
              "data": "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",
              "format": "base64"
            },
            {
              "data": "MIIFljCCA36gAwIBAgINAgO8U1lrNMcY9QFQZjANBgkqhkiG9w0BAQsFADBHMQswCQYDVQQGEwJVUzEiMCAGA1UEChMZR29vZ2xlIFRydXN0IFNlcnZpY2VzIExMQzEUMBIGA1UEAxMLR1RTIFJvb3QgUjEwHhcNMjAwODEzMDAwMDQyWhcNMjcwOTMwMDAwMDQyWjBGMQswCQYDVQQGEwJVUzEiMCAGA1UEChMZR29vZ2xlIFRydXN0IFNlcnZpY2VzIExMQzETMBEGA1UEAxMKR1RTIENBIDFDMzCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAPWI3+dijB43+DdCkH9sh9D7ZYIl/ejLa6T/belaI+KZ9hzpkgOZE3wJCor6QtZeViSqejOEH9Hpabu5dOxXTGZok3c3VVP+ORBNtzS7XyV3NzsXlOo85Z3VvMO0Q+sup0fvsEQRY9i0QYXdQTBIkxu/t/bgRQIh4JZCF8/ZK2VWNAcmBA2o/X3KLu/qSHw3TT8An4Pf73WELnlXXPxXbhqW//yMmqaZviXZf5YsBvcRKgKAgOtjGDxQSYflispfGStZloEAoPtR28p3CwvJlk/vcEnHXG0g/Zm0tOLKLnf9LdwLtmsTDIwZKxeWmLnwi/agJ7u2441Rj72ux5uxiZ0CAwEAAaOCAYAwggF8MA4GA1UdDwEB/wQEAwIBhjAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwEgYDVR0TAQH/BAgwBgEB/wIBADAdBgNVHQ4EFgQUinR/r4XN7pXNPZzQ4kYU83E1HScwHwYDVR0jBBgwFoAU5K8rJnEaK0gnhS9SZizv8IkTcT4waAYIKwYBBQUHAQEEXDBaMCYGCCsGAQUFBzABhhpodHRwOi8vb2NzcC5wa2kuZ29vZy9ndHNyMTAwBggrBgEFBQcwAoYkaHR0cDovL3BraS5nb29nL3JlcG8vY2VydHMvZ3RzcjEuZGVyMDQGA1UdHwQtMCswKaAnoCWGI2h0dHA6Ly9jcmwucGtpLmdvb2cvZ3RzcjEvZ3RzcjEuY3JsMFcGA1UdIARQME4wOAYKKwYBBAHWeQIFAzAqMCgGCCsGAQUFBwIBFhxodHRwczovL3BraS5nb29nL3JlcG9zaXRvcnkvMAgGBmeBDAECATAIBgZngQwBAgIwDQYJKoZIhvcNAQELBQADggIBAIl9rCBcDDy+mqhXlRu0rvqrpXJxtDaV/d9AEQNMwkYUuxQkq/BQcSLbrcRuf8/xam/IgxvYzolfh2yHuKkMo5uhYpSTld9brmYZCwKWnvy15xBpPnrLRklfRuFBsdeYTWU0AIAaP0+fbH9JAIFTQaSSIYKCGvGjRFsqUBITTcFTNvNCCK9U+o53UxtkOCcXCb1YyRt8OS1b887U7ZfbFAO/CVMkH8IMBHmYJvJh8VNS/UKMG2YrPxWhu//2m+OBmgEGcYk1KCTd4b3rGS3hSMs9WYNRtHTGnXzGsYZbr8w0xNPM1IERlQCh9BIiAfq0g3GvjLeMcySsN1PCAJA/Ef5c7TaUEDu9Ka7ixzpiO2xj2YC/WXGsYye5TBeg2vZzFb8q3o/zpWwygTMD0IZRcZk0upONXbVRWPeyk+gB9lm+cZv9TSjOz23HFtz30dZGm6fKa+l3D/2gthsjgx0QGtkJAITgRNOidSOzNIb2ILCkXhAd4FJGAJ2xDx8hcFH1mt0G/FX0Kw4zd8NLQsLxdxP8c4CU6x+7Nz/OAipmsHMdMqUybDKwjuDEI/9bfU1lcKwrmz3O2+BtjjKAvpafkmO8l7tdufThcV4q5O8DIrGKZTqPwJNl1IXNDw9bg1kWRxYtnCQ6yICmJhSFm/Y3m6xv+cXDBlHz4n/FsRC6UfTd",
              "format": "base64"
            },
            {
              "data": "MIIFYjCCBEqgAwIBAgIQd70NbNs2+RrqIQ/E8FjTDTANBgkqhkiG9w0BAQsFADBXMQswCQYDVQQGEwJCRTEZMBcGA1UEChMQR2xvYmFsU2lnbiBudi1zYTEQMA4GA1UECxMHUm9vdCBDQTEbMBkGA1UEAxMSR2xvYmFsU2lnbiBSb290IENBMB4XDTIwMDYxOTAwMDA0MloXDTI4MDEyODAwMDA0MlowRzELMAkGA1UEBhMCVVMxIjAgBgNVBAoTGUdvb2dsZSBUcnVzdCBTZXJ2aWNlcyBMTEMxFDASBgNVBAMTC0dUUyBSb290IFIxMIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAthECix7joXebO9y/lD63ladAPKH9gvl9MgaCcfb2jH/76Nu8ai6Xl6OMS/kr9rH5zoQdsfnFl97vufKj6bwSiV6nqlKr+CMny6SxnGPb15l+8Ape62im9MZaRw1NEDPjTrETo8gYbEvs/AmQ351kKSUjB6G00j0uYODP0gmHu81I8E3CwnqIiru6z1kZ1q+PsAewnjHxgsHA3y6mbWwZDrXYfiYaRQM9sHmklCitD38m5agI/pboPGiUU+6DOogrFZYJsuB6jC511pzrp1Zkj5ZPaK49l8KEj8C8QMALXL32h7M1bKwYUH+E4EzNktMg6TO8UpmvMrUpsyUqtEj5cuHKZPfmghCN6J3Cioj6OGaK/GP5Afl4/Xtcd/p2h/rs37EOeZVXtL0m79YB0esWCruOC7XFxYpVq9Os6pFLKcwZpDIlTirxZUTQAs6qzkm06p98g7BAe+dDq6dso499iYH6TKX/1Y7DzkvgtdizjkXPdsDtQCv9Uw+wp9U7DbGKogPeMa3Md+pvez7W35EiEua++tgy/BBjFFFy3l3WFpO9KWgz7zpm7AeKJt8T11dleCfeXkkUAKIAf5qoIbapsZWwpbkNFhHax2xIPEDgfg1azVY80ZcFuctL7TlLnMQ/0lUTbiSw1nH69MG6zO0b9f6BQdgAmD06yK56mDcYBZUCAwEAAaOCATgwggE0MA4GA1UdDwEB/wQEAwIBhjAPBgNVHRMBAf8EBTADAQH/MB0GA1UdDgQWBBTkrysmcRorSCeFL1JmLO/wiRNxPjAfBgNVHSMEGDAWgBRge2YaRQ2XyolQL30EzTSo//z9SzBgBggrBgEFBQcBAQRUMFIwJQYIKwYBBQUHMAGGGWh0dHA6Ly9vY3NwLnBraS5nb29nL2dzcjEwKQYIKwYBBQUHMAKGHWh0dHA6Ly9wa2kuZ29vZy9nc3IxL2dzcjEuY3J0MDIGA1UdHwQrMCkwJ6AloCOGIWh0dHA6Ly9jcmwucGtpLmdvb2cvZ3NyMS9nc3IxLmNybDA7BgNVHSAENDAyMAgGBmeBDAECATAIBgZngQwBAgIwDQYLKwYBBAHWeQIFAwIwDQYLKwYBBAHWeQIFAwMwDQYJKoZIhvcNAQELBQADggEBADSkHrEoo9C0dhemMXoh6dFSPsjbdBZBiLg9NR3t5P+T4Vxfq7vqfM/b5A3Ri1fyJm9bvhdGaJQ3b2t6yMAYN/olUazsaL+yyEn9WprKASOshIArAoyZl+tJaox118fessmXn1hIVw41oeQa1v1vg4Fv74zPl6/AhSrw9U5pCZEt4Wi4wStz6dTZ/CLANx8LZh1J7QJVj2fhMtfTJr9w4z30Z209fOU0iOMy+qduBmpvvYuR7hZL6Dupszfnw0Skfths18dG9ZKb59UhvmaSGZRVbNQpsg3BZlvid0lIKO2d1xozclOzgjXPYovJJIultzkMu34qQb9Sz/yilrbCgj8=",
              "format": "base64"
            }
          ],
          "server_name": "8.8.8.8",
          "t": 8.087711639,
          "tags": [],
          "tls_version": "TLSv1.3"
        }
      },
      {
        "network_events": [
          {
            "failure": null,
            "operation": "quic_handshake_start",
            "t": 9.006384335
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "udp",
            "t": 9.00668989
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 9.019503545
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "udp",
            "t": 9.019707149
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "udp",
            "t": 9.059537084
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 9.069987825
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 9.089452271
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 9.089666139
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 9.089701089
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 44,
            "operation": "write_to",
            "proto": "udp",
            "t": 9.089701572
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 44,
            "operation": "write_to",
            "proto": "udp",
            "t": 9.089948482
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 9.089949902
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 107,
            "operation": "read_from",
            "proto": "udp",
            "t": 9.089970599
          },
          {
            "failure": null,
            "operation": "quic_handshake_done",
            "t": 9.092487118
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 83,
            "operation": "write_to",
            "proto": "udp",
            "t": 9.092544666
          }
        ],
        "quic_handshakes": {
          "network": "quic",
          "address": "8.8.8.8:443",
          "cipher_suite": "TLS_AES_128_GCM_SHA256",
          "failure": null,
          "negotiated_protocol": "h3",
          "no_tls_verify": false,
          "peer_certificates": [
            {
              "data": "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",
              "format": "base64"
            },
            {
              "data": "MIIFljCCA36gAwIBAgINAgO8U1lrNMcY9QFQZjANBgkqhkiG9w0BAQsFADBHMQswCQYDVQQGEwJVUzEiMCAGA1UEChMZR29vZ2xlIFRydXN0IFNlcnZpY2VzIExMQzEUMBIGA1UEAxMLR1RTIFJvb3QgUjEwHhcNMjAwODEzMDAwMDQyWhcNMjcwOTMwMDAwMDQyWjBGMQswCQYDVQQGEwJVUzEiMCAGA1UEChMZR29vZ2xlIFRydXN0IFNlcnZpY2VzIExMQzETMBEGA1UEAxMKR1RTIENBIDFDMzCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAPWI3+dijB43+DdCkH9sh9D7ZYIl/ejLa6T/belaI+KZ9hzpkgOZE3wJCor6QtZeViSqejOEH9Hpabu5dOxXTGZok3c3VVP+ORBNtzS7XyV3NzsXlOo85Z3VvMO0Q+sup0fvsEQRY9i0QYXdQTBIkxu/t/bgRQIh4JZCF8/ZK2VWNAcmBA2o/X3KLu/qSHw3TT8An4Pf73WELnlXXPxXbhqW//yMmqaZviXZf5YsBvcRKgKAgOtjGDxQSYflispfGStZloEAoPtR28p3CwvJlk/vcEnHXG0g/Zm0tOLKLnf9LdwLtmsTDIwZKxeWmLnwi/agJ7u2441Rj72ux5uxiZ0CAwEAAaOCAYAwggF8MA4GA1UdDwEB/wQEAwIBhjAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwEgYDVR0TAQH/BAgwBgEB/wIBADAdBgNVHQ4EFgQUinR/r4XN7pXNPZzQ4kYU83E1HScwHwYDVR0jBBgwFoAU5K8rJnEaK0gnhS9SZizv8IkTcT4waAYIKwYBBQUHAQEEXDBaMCYGCCsGAQUFBzABhhpodHRwOi8vb2NzcC5wa2kuZ29vZy9ndHNyMTAwBggrBgEFBQcwAoYkaHR0cDovL3BraS5nb29nL3JlcG8vY2VydHMvZ3RzcjEuZGVyMDQGA1UdHwQtMCswKaAnoCWGI2h0dHA6Ly9jcmwucGtpLmdvb2cvZ3RzcjEvZ3RzcjEuY3JsMFcGA1UdIARQME4wOAYKKwYBBAHWeQIFAzAqMCgGCCsGAQUFBwIBFhxodHRwczovL3BraS5nb29nL3JlcG9zaXRvcnkvMAgGBmeBDAECATAIBgZngQwBAgIwDQYJKoZIhvcNAQELBQADggIBAIl9rCBcDDy+mqhXlRu0rvqrpXJxtDaV/d9AEQNMwkYUuxQkq/BQcSLbrcRuf8/xam/IgxvYzolfh2yHuKkMo5uhYpSTld9brmYZCwKWnvy15xBpPnrLRklfRuFBsdeYTWU0AIAaP0+fbH9JAIFTQaSSIYKCGvGjRFsqUBITTcFTNvNCCK9U+o53UxtkOCcXCb1YyRt8OS1b887U7ZfbFAO/CVMkH8IMBHmYJvJh8VNS/UKMG2YrPxWhu//2m+OBmgEGcYk1KCTd4b3rGS3hSMs9WYNRtHTGnXzGsYZbr8w0xNPM1IERlQCh9BIiAfq0g3GvjLeMcySsN1PCAJA/Ef5c7TaUEDu9Ka7ixzpiO2xj2YC/WXGsYye5TBeg2vZzFb8q3o/zpWwygTMD0IZRcZk0upONXbVRWPeyk+gB9lm+cZv9TSjOz23HFtz30dZGm6fKa+l3D/2gthsjgx0QGtkJAITgRNOidSOzNIb2ILCkXhAd4FJGAJ2xDx8hcFH1mt0G/FX0Kw4zd8NLQsLxdxP8c4CU6x+7Nz/OAipmsHMdMqUybDKwjuDEI/9bfU1lcKwrmz3O2+BtjjKAvpafkmO8l7tdufThcV4q5O8DIrGKZTqPwJNl1IXNDw9bg1kWRxYtnCQ6yICmJhSFm/Y3m6xv+cXDBlHz4n/FsRC6UfTd",
              "format": "base64"
            },
            {
              "data": "MIIFYjCCBEqgAwIBAgIQd70NbNs2+RrqIQ/E8FjTDTANBgkqhkiG9w0BAQsFADBXMQswCQYDVQQGEwJCRTEZMBcGA1UEChMQR2xvYmFsU2lnbiBudi1zYTEQMA4GA1UECxMHUm9vdCBDQTEbMBkGA1UEAxMSR2xvYmFsU2lnbiBSb290IENBMB4XDTIwMDYxOTAwMDA0MloXDTI4MDEyODAwMDA0MlowRzELMAkGA1UEBhMCVVMxIjAgBgNVBAoTGUdvb2dsZSBUcnVzdCBTZXJ2aWNlcyBMTEMxFDASBgNVBAMTC0dUUyBSb290IFIxMIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAthECix7joXebO9y/lD63ladAPKH9gvl9MgaCcfb2jH/76Nu8ai6Xl6OMS/kr9rH5zoQdsfnFl97vufKj6bwSiV6nqlKr+CMny6SxnGPb15l+8Ape62im9MZaRw1NEDPjTrETo8gYbEvs/AmQ351kKSUjB6G00j0uYODP0gmHu81I8E3CwnqIiru6z1kZ1q+PsAewnjHxgsHA3y6mbWwZDrXYfiYaRQM9sHmklCitD38m5agI/pboPGiUU+6DOogrFZYJsuB6jC511pzrp1Zkj5ZPaK49l8KEj8C8QMALXL32h7M1bKwYUH+E4EzNktMg6TO8UpmvMrUpsyUqtEj5cuHKZPfmghCN6J3Cioj6OGaK/GP5Afl4/Xtcd/p2h/rs37EOeZVXtL0m79YB0esWCruOC7XFxYpVq9Os6pFLKcwZpDIlTirxZUTQAs6qzkm06p98g7BAe+dDq6dso499iYH6TKX/1Y7DzkvgtdizjkXPdsDtQCv9Uw+wp9U7DbGKogPeMa3Md+pvez7W35EiEua++tgy/BBjFFFy3l3WFpO9KWgz7zpm7AeKJt8T11dleCfeXkkUAKIAf5qoIbapsZWwpbkNFhHax2xIPEDgfg1azVY80ZcFuctL7TlLnMQ/0lUTbiSw1nH69MG6zO0b9f6BQdgAmD06yK56mDcYBZUCAwEAAaOCATgwggE0MA4GA1UdDwEB/wQEAwIBhjAPBgNVHRMBAf8EBTADAQH/MB0GA1UdDgQWBBTkrysmcRorSCeFL1JmLO/wiRNxPjAfBgNVHSMEGDAWgBRge2YaRQ2XyolQL30EzTSo//z9SzBgBggrBgEFBQcBAQRUMFIwJQYIKwYBBQUHMAGGGWh0dHA6Ly9vY3NwLnBraS5nb29nL2dzcjEwKQYIKwYBBQUHMAKGHWh0dHA6Ly9wa2kuZ29vZy9nc3IxL2dzcjEuY3J0MDIGA1UdHwQrMCkwJ6AloCOGIWh0dHA6Ly9jcmwucGtpLmdvb2cvZ3NyMS9nc3IxLmNybDA7BgNVHSAENDAyMAgGBmeBDAECATAIBgZngQwBAgIwDQYLKwYBBAHWeQIFAwIwDQYLKwYBBAHWeQIFAwMwDQYJKoZIhvcNAQELBQADggEBADSkHrEoo9C0dhemMXoh6dFSPsjbdBZBiLg9NR3t5P+T4Vxfq7vqfM/b5A3Ri1fyJm9bvhdGaJQ3b2t6yMAYN/olUazsaL+yyEn9WprKASOshIArAoyZl+tJaox118fessmXn1hIVw41oeQa1v1vg4Fv74zPl6/AhSrw9U5pCZEt4Wi4wStz6dTZ/CLANx8LZh1J7QJVj2fhMtfTJr9w4z30Z209fOU0iOMy+qduBmpvvYuR7hZL6Dupszfnw0Skfths18dG9ZKb59UhvmaSGZRVbNQpsg3BZlvid0lIKO2d1xozclOzgjXPYovJJIultzkMu34qQb9Sz/yilrbCgj8=",
              "format": "base64"
            }
          ],
          "server_name": "8.8.8.8",
          "t": 9.092487118,
          "tags": [],
          "tls_version": "TLSv1.3"
        }
      }
    ]
  },
  "test_name": "simplequicping",
  "test_runtime": 9.092578798,
  "test_start_time": "2022-08-06 10:21:35",
  "test_version": "0.1.0"
}
```
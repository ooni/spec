# Specification version number

2022-05-09

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

- `pings` contains a list of `df-006-tlshandhsake`, and `df-008-netevents` results.

## Possible conclusions

This experiment is an exploratory tool. There is no immediate conclusion
from its results but it is useful to perform censorship research.

## Example output sample

```JSON
{
  "annotations": {
    "architecture": "arm64",
    "engine_name": "ooniprobe-engine",
    "engine_version": "3.15.0-alpha",
    "platform": "macos"
  },
  "data_format_version": "0.2.0",
  "input": "quichandshake://8.8.8.8:443",
  "measurement_start_time": "2022-05-09 08:57:43",
  "options": [
    "SNI=dns.google"
  ],
  "probe_asn": "AS30722",
  "probe_cc": "IT",
  "probe_ip": "127.0.0.1",
  "probe_network_name": "Vodafone Italia S.p.A.",
  "report_id": "20220509T085744Z_simplequicping_IT_30722_n1_f5vAYRi4KrvSWDno",
  "resolver_asn": "AS30722",
  "resolver_ip": "91.80.36.92",
  "resolver_network_name": "Vodafone Italia S.p.A.",
  "software_name": "miniooni",
  "software_version": "3.15.0-alpha",
  "test_keys": {
    "pings": [
      {
        "network_events": [
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "quic",
            "t": 0.005243417,
            "started": 0.005098084
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "quic",
            "t": 0.022103792,
            "started": 0.004514167
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "quic",
            "t": 0.022579084,
            "started": 0.022500917
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "quic",
            "t": 0.038119834,
            "started": 0.022119084
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "quic",
            "t": 0.038136084,
            "started": 0.038129584
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "quic",
            "t": 0.038145084,
            "started": 0.038139959
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "quic",
            "t": 0.038152625,
            "started": 0.038148292
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 117,
            "operation": "read_from",
            "proto": "quic",
            "t": 0.038158,
            "started": 0.038153917
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 44,
            "operation": "write_to",
            "proto": "quic",
            "t": 0.038406834,
            "started": 0.038357709
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 44,
            "operation": "write_to",
            "proto": "quic",
            "t": 0.0384265,
            "started": 0.038411375
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 83,
            "operation": "write_to",
            "proto": "quic",
            "t": 0.039876209,
            "started": 0.039839792
          }
        ],
        "quic_handshakes": [
          {
            "cipher_suite": "TLS_CHACHA20_POLY1305_SHA256",
            "failure": null,
            "negotiated_proto": "h3",
            "tls_version": "TLSv1.3",
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
            "t": 0.039839625,
            "address": "8.8.8.8:443",
            "server_name": "dns.google",
            "alpn": [
              "h3"
            ],
            "no_tls_verify": false,
            "proto": "quic",
            "started": 0.004255792
          }
        ]
      },
      {
        "network_events": [
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "quic",
            "t": 1.007740542,
            "started": 1.007607792
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "quic",
            "t": 1.024162542,
            "started": 1.007077709
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "quic",
            "t": 1.024637792,
            "started": 1.024592459
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "quic",
            "t": 1.040605917,
            "started": 1.024187667
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "quic",
            "t": 1.040622417,
            "started": 1.0406155
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "quic",
            "t": 1.040633125,
            "started": 1.040626667
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "quic",
            "t": 1.040662792,
            "started": 1.040657584
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 115,
            "operation": "read_from",
            "proto": "quic",
            "t": 1.040671625,
            "started": 1.040665334
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 44,
            "operation": "write_to",
            "proto": "quic",
            "t": 1.040879292,
            "started": 1.04082625
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 44,
            "operation": "write_to",
            "proto": "quic",
            "t": 1.040901084,
            "started": 1.040882542
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 83,
            "operation": "write_to",
            "proto": "quic",
            "t": 1.042761792,
            "started": 1.042716334
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 33,
            "operation": "write_to",
            "proto": "quic",
            "t": 1.042786167,
            "started": 1.042766292
          }
        ],
        "quic_handshakes": [
          {
            "cipher_suite": "TLS_CHACHA20_POLY1305_SHA256",
            "failure": null,
            "negotiated_proto": "h3",
            "tls_version": "TLSv1.3",
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
            "t": 1.0427260839999999,
            "address": "8.8.8.8:443",
            "server_name": "dns.google",
            "alpn": [
              "h3"
            ],
            "no_tls_verify": false,
            "proto": "quic",
            "started": 1.006765375
          }
        ]
      },
      {
        "network_events": [
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "quic",
            "t": 2.009436,
            "started": 2.009307709
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "quic",
            "t": 2.026164417,
            "started": 2.008734334
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "quic",
            "t": 2.0267135,
            "started": 2.026653292
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "quic",
            "t": 2.043212959,
            "started": 2.026181625
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "quic",
            "t": 2.043235,
            "started": 2.043224542
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "quic",
            "t": 2.043251125,
            "started": 2.043239292
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "quic",
            "t": 2.043259459,
            "started": 2.043253709
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 117,
            "operation": "read_from",
            "proto": "quic",
            "t": 2.043295959,
            "started": 2.043290125
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 44,
            "operation": "write_to",
            "proto": "quic",
            "t": 2.043528792,
            "started": 2.043479584
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 44,
            "operation": "write_to",
            "proto": "quic",
            "t": 2.043550209,
            "started": 2.0435325
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 83,
            "operation": "write_to",
            "proto": "quic",
            "t": 2.045380084,
            "started": 2.045355875
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 33,
            "operation": "write_to",
            "proto": "quic",
            "t": 2.045410334,
            "started": 2.045385084
          }
        ],
        "quic_handshakes": [
          {
            "cipher_suite": "TLS_CHACHA20_POLY1305_SHA256",
            "failure": null,
            "negotiated_proto": "h3",
            "tls_version": "TLSv1.3",
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
            "t": 2.045370667,
            "address": "8.8.8.8:443",
            "server_name": "dns.google",
            "alpn": [
              "h3"
            ],
            "no_tls_verify": false,
            "proto": "quic",
            "started": 2.008397709
          }
        ]
      },
      {
        "network_events": [
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "quic",
            "t": 3.008320542,
            "started": 3.0082105
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "quic",
            "t": 3.034615792,
            "started": 3.007805292
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "quic",
            "t": 3.035186417,
            "started": 3.035118792
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "quic",
            "t": 3.050836209,
            "started": 3.03464475
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "quic",
            "t": 3.050869584,
            "started": 3.05086
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 44,
            "operation": "write_to",
            "proto": "quic",
            "t": 3.051307417,
            "started": 3.051136584
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "quic",
            "t": 3.053056375,
            "started": 3.050877542
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "quic",
            "t": 3.05308625,
            "started": 3.053075167
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 121,
            "operation": "read_from",
            "proto": "quic",
            "t": 3.053118459,
            "started": 3.053092209
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 44,
            "operation": "write_to",
            "proto": "quic",
            "t": 3.053374334,
            "started": 3.053293042
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 83,
            "operation": "write_to",
            "proto": "quic",
            "t": 3.055937292,
            "started": 3.055883875
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 33,
            "operation": "write_to",
            "proto": "quic",
            "t": 3.05598075,
            "started": 3.055941792
          }
        ],
        "quic_handshakes": [
          {
            "cipher_suite": "TLS_CHACHA20_POLY1305_SHA256",
            "failure": null,
            "negotiated_proto": "h3",
            "tls_version": "TLSv1.3",
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
            "t": 3.055895709,
            "address": "8.8.8.8:443",
            "server_name": "dns.google",
            "alpn": [
              "h3"
            ],
            "no_tls_verify": false,
            "proto": "quic",
            "started": 3.007550792
          }
        ]
      },
      {
        "network_events": [
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "quic",
            "t": 4.0079495,
            "started": 4.007845917
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "quic",
            "t": 4.028193125,
            "started": 4.007434
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "quic",
            "t": 4.028732334,
            "started": 4.028674834
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "quic",
            "t": 4.043755834,
            "started": 4.0282245
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "quic",
            "t": 4.043788834,
            "started": 4.043779084
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 44,
            "operation": "write_to",
            "proto": "quic",
            "t": 4.044139875,
            "started": 4.044060834
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "quic",
            "t": 4.044336417,
            "started": 4.043794709
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 44,
            "operation": "write_to",
            "proto": "quic",
            "t": 4.044479625,
            "started": 4.044441959
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "quic",
            "t": 4.044606167,
            "started": 4.0443465
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 117,
            "operation": "read_from",
            "proto": "quic",
            "t": 4.0452439590000004,
            "started": 4.044615584
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 83,
            "operation": "write_to",
            "proto": "quic",
            "t": 4.047179334,
            "started": 4.047123417
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 33,
            "operation": "write_to",
            "proto": "quic",
            "t": 4.047201542,
            "started": 4.047183125
          }
        ],
        "quic_handshakes": [
          {
            "cipher_suite": "TLS_CHACHA20_POLY1305_SHA256",
            "failure": null,
            "negotiated_proto": "h3",
            "tls_version": "TLSv1.3",
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
            "t": 4.047139667,
            "address": "8.8.8.8:443",
            "server_name": "dns.google",
            "alpn": [
              "h3"
            ],
            "no_tls_verify": false,
            "proto": "quic",
            "started": 4.007187709
          }
        ]
      },
      {
        "network_events": [
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "quic",
            "t": 5.008398792,
            "started": 5.008290334
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "quic",
            "t": 5.036004167,
            "started": 5.007840167
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "quic",
            "t": 5.03652575,
            "started": 5.036481709
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "quic",
            "t": 5.051925792,
            "started": 5.036033625
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "quic",
            "t": 5.05198025,
            "started": 5.051969625
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 44,
            "operation": "write_to",
            "proto": "quic",
            "t": 5.052345459,
            "started": 5.052276917
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "quic",
            "t": 5.053939667,
            "started": 5.051986209
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "quic",
            "t": 5.053972834,
            "started": 5.053961417
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 121,
            "operation": "read_from",
            "proto": "quic",
            "t": 5.053985875,
            "started": 5.053976084
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 44,
            "operation": "write_to",
            "proto": "quic",
            "t": 5.054199542,
            "started": 5.054134375
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 83,
            "operation": "write_to",
            "proto": "quic",
            "t": 5.05699975,
            "started": 5.05692875
          }
        ],
        "quic_handshakes": [
          {
            "cipher_suite": "TLS_CHACHA20_POLY1305_SHA256",
            "failure": null,
            "negotiated_proto": "h3",
            "tls_version": "TLSv1.3",
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
            "t": 5.056945,
            "address": "8.8.8.8:443",
            "server_name": "dns.google",
            "alpn": [
              "h3"
            ],
            "no_tls_verify": false,
            "proto": "quic",
            "started": 5.007570959
          }
        ]
      },
      {
        "network_events": [
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "quic",
            "t": 6.00710225,
            "started": 6.006978292
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "quic",
            "t": 6.026403667,
            "started": 6.006515417
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "quic",
            "t": 6.026949709,
            "started": 6.026896834
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "quic",
            "t": 6.041891584,
            "started": 6.026423959
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "quic",
            "t": 6.041910875,
            "started": 6.041902959
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 44,
            "operation": "write_to",
            "proto": "quic",
            "t": 6.042197875,
            "started": 6.042137375
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "quic",
            "t": 6.042338334,
            "started": 6.041916959
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 44,
            "operation": "write_to",
            "proto": "quic",
            "t": 6.042433167,
            "started": 6.042408834
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1251,
            "operation": "read_from",
            "proto": "quic",
            "t": 6.043456375,
            "started": 6.042344959
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 67,
            "operation": "read_from",
            "proto": "quic",
            "t": 6.043473417,
            "started": 6.043463709
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 83,
            "operation": "write_to",
            "proto": "quic",
            "t": 6.045342167,
            "started": 6.045309667
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 33,
            "operation": "write_to",
            "proto": "quic",
            "t": 6.045404667,
            "started": 6.045360834
          }
        ],
        "quic_handshakes": [
          {
            "cipher_suite": "TLS_CHACHA20_POLY1305_SHA256",
            "failure": null,
            "negotiated_proto": "h3",
            "tls_version": "TLSv1.3",
            "peer_certificates": [
              {
                "data": "MIIF4TCCBMmgAwIBAgIQK1nI+guW9KcS+CyMwVj8bDANBgkqhkiG9w0BAQsFADBGMQswCQYDVQQGEwJVUzEiMCAGA1UEChMZR29vZ2xlIFRydXN0IFNlcnZpY2VzIExMQzETMBEGA1UEAxMKR1RTIENBIDFDMzAeFw0yMjA0MTgwOTUwMDdaFw0yMjA3MTEwOTUwMDZaMBUxEzARBgNVBAMTCmRucy5nb29nbGUwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDhohcmdtAJBtIV63Wcyy/j1ofavVYrVhB2wXfft0AR8d79KIi9+LERbq5fiszPJfdnYy2Gu084h1QUrSNj7kefCTCNejqh7b/ZOBe+6TXDcq5dnDzSJ6oEcACZ5l2YoWwNUybZlJnTkHq5auq6Ybl2oSdZW7pCGmJhdPE+UKo/WBiQoUhY3Kl/5lv9OZJyDxoo1zH5naEGaD+XKIEiR9MK8pBSBTvZy/Edx4Ye0Pz4jiHsZNz3dQMQtZ1MQPKt/tupv5/TMcVry9S+l9/7Az0ADarQifmvQ/E7KrP8Kf4LsXVhIAAjgqlzPvs8VY48LXSKHW096xnwuk4EdTMvysQdAgMBAAGjggL6MIIC9jAOBgNVHQ8BAf8EBAMCBaAwEwYDVR0lBAwwCgYIKwYBBQUHAwEwDAYDVR0TAQH/BAIwADAdBgNVHQ4EFgQU4JgpRpc9FNS17OeaNE4BtUP/j8UwHwYDVR0jBBgwFoAUinR/r4XN7pXNPZzQ4kYU83E1HScwagYIKwYBBQUHAQEEXjBcMCcGCCsGAQUFBzABhhtodHRwOi8vb2NzcC5wa2kuZ29vZy9ndHMxYzMwMQYIKwYBBQUHMAKGJWh0dHA6Ly9wa2kuZ29vZy9yZXBvL2NlcnRzL2d0czFjMy5kZXIwgawGA1UdEQSBpDCBoYIKZG5zLmdvb2dsZYIOZG5zLmdvb2dsZS5jb22CECouZG5zLmdvb2dsZS5jb22CCzg4ODguZ29vZ2xlghBkbnM2NC5kbnMuZ29vZ2xlhwQICAgIhwQICAQEhxAgAUhgSGAAAAAAAAAAAIiIhxAgAUhgSGAAAAAAAAAAAIhEhxAgAUhgSGAAAAAAAAAAAGRkhxAgAUhgSGAAAAAAAAAAAABkMCEGA1UdIAQaMBgwCAYGZ4EMAQIBMAwGCisGAQQB1nkCBQMwPAYDVR0fBDUwMzAxoC+gLYYraHR0cDovL2NybHMucGtpLmdvb2cvZ3RzMWMzL1FPdkowTjFzVDJBLmNybDCCAQMGCisGAQQB1nkCBAIEgfQEgfEA7wB2AN+lXqtogk8fbK3uuF9OPlrqzaISpGpejjsSwCBEXCpzAAABgDxLS9gAAAQDAEcwRQIhAL57jC9O5a7r/L2Noow1xRYh2jzGNNNBD4b01ucsaT9AAiAt9X4qnFNva4XvE+GMyXkXA1Ks3wM6NVTZIkyPWeNyfQB1ACl5vvCeOTkh8FZzn2Old+W+V32cYAr4+U1dJlwlXceEAAABgDxLS80AAAQDAEYwRAIgQ5eLjqeVwBRtShi6lItYyzpQQjj3agOTvngsqC9CaIICICrfk2DjhZTkZtEZXkobeDdUROud7bvUFy2+ejY0JDa8MA0GCSqGSIb3DQEBCwUAA4IBAQCSNfOlk6TJiV4FQO6syu1ap8elb73PGqJjVI2Q8c9akDv4zY9F2YqVQyG74sODKsD1uhMWKQrCOJra1uq+TNWzhtHOEE7TGNyfXdle0GAMsS8j+zJbfnfWfr7EtGHODfyZl+VGDFK/CpmGnDGol19/Dmw/bnEPQqv55c/1UvuM1hGDn+EMcvjsIpYdG8ypQlGRDQ6NoCv6wZLjfmAixqTNoW+5RYbKHWa5BYykLpcIk62i1yMQJIjTI44YzM7uQqNoUz1K++7iIvb8bHfya7uMz5cOfgavzv108QXO6Nb756yhPqOc3kVuh9JcnsoRVgihKd8dFwbO5NAFJUFbfGdX",
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
            "t": 6.0453765839999996,
            "address": "8.8.8.8:443",
            "server_name": "dns.google",
            "alpn": [
              "h3"
            ],
            "no_tls_verify": false,
            "proto": "quic",
            "started": 6.006132459
          }
        ]
      },
      {
        "network_events": [
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "quic",
            "t": 7.007598792,
            "started": 7.007461375
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "quic",
            "t": 7.033784917,
            "started": 7.006873834
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "quic",
            "t": 7.0343725,
            "started": 7.034313
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "quic",
            "t": 7.049205709,
            "started": 7.033804542
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "quic",
            "t": 7.04923,
            "started": 7.04921975
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "quic",
            "t": 7.049244542,
            "started": 7.049235542
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "quic",
            "t": 7.0492609999999996,
            "started": 7.049253459
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 119,
            "operation": "read_from",
            "proto": "quic",
            "t": 7.049276,
            "started": 7.049269375
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 44,
            "operation": "write_to",
            "proto": "quic",
            "t": 7.049555917,
            "started": 7.04948125
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 44,
            "operation": "write_to",
            "proto": "quic",
            "t": 7.049589459,
            "started": 7.049561084
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 83,
            "operation": "write_to",
            "proto": "quic",
            "t": 7.052086875,
            "started": 7.052042334
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 33,
            "operation": "write_to",
            "proto": "quic",
            "t": 7.05211075,
            "started": 7.052090459
          }
        ],
        "quic_handshakes": [
          {
            "cipher_suite": "TLS_CHACHA20_POLY1305_SHA256",
            "failure": null,
            "negotiated_proto": "h3",
            "tls_version": "TLSv1.3",
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
            "t": 7.052060417,
            "address": "8.8.8.8:443",
            "server_name": "dns.google",
            "alpn": [
              "h3"
            ],
            "no_tls_verify": false,
            "proto": "quic",
            "started": 7.006575334
          }
        ]
      },
      {
        "network_events": [
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "quic",
            "t": 8.008200084,
            "started": 8.008090792
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "quic",
            "t": 8.034468084,
            "started": 8.0076125
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "quic",
            "t": 8.034967917,
            "started": 8.034914042
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "quic",
            "t": 8.051006334,
            "started": 8.034489167
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "quic",
            "t": 8.051031417,
            "started": 8.051022625
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "quic",
            "t": 8.051043292,
            "started": 8.051037042
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "quic",
            "t": 8.051055167,
            "started": 8.05105025
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 44,
            "operation": "write_to",
            "proto": "quic",
            "t": 8.051333917,
            "started": 8.05127625
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 44,
            "operation": "write_to",
            "proto": "quic",
            "t": 8.051359917,
            "started": 8.051339709
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 116,
            "operation": "read_from",
            "proto": "quic",
            "t": 8.051508084,
            "started": 8.051057167
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 83,
            "operation": "write_to",
            "proto": "quic",
            "t": 8.053081042,
            "started": 8.053057959
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 33,
            "operation": "write_to",
            "proto": "quic",
            "t": 8.053097459,
            "started": 8.053083459
          }
        ],
        "quic_handshakes": [
          {
            "cipher_suite": "TLS_CHACHA20_POLY1305_SHA256",
            "failure": null,
            "negotiated_proto": "h3",
            "tls_version": "TLSv1.3",
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
            "t": 8.053070334,
            "address": "8.8.8.8:443",
            "server_name": "dns.google",
            "alpn": [
              "h3"
            ],
            "no_tls_verify": false,
            "proto": "quic",
            "started": 8.007340584
          }
        ]
      },
      {
        "network_events": [
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "quic",
            "t": 9.007747209,
            "started": 9.007600084
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "quic",
            "t": 9.035038167,
            "started": 9.006991792
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "quic",
            "t": 9.035618334,
            "started": 9.035565709
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "quic",
            "t": 9.051023334,
            "started": 9.035056917
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "quic",
            "t": 9.051047584,
            "started": 9.051037959
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 44,
            "operation": "write_to",
            "proto": "quic",
            "t": 9.051342625,
            "started": 9.051264792
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "quic",
            "t": 9.051531625,
            "started": 9.05105275
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 44,
            "operation": "write_to",
            "proto": "quic",
            "t": 9.051640292,
            "started": 9.051604542
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "quic",
            "t": 9.052558334,
            "started": 9.051541292
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 120,
            "operation": "read_from",
            "proto": "quic",
            "t": 9.052582209,
            "started": 9.052570334
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 83,
            "operation": "write_to",
            "proto": "quic",
            "t": 9.055192917,
            "started": 9.055137584
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 33,
            "operation": "write_to",
            "proto": "quic",
            "t": 9.055223042,
            "started": 9.055198459
          }
        ],
        "quic_handshakes": [
          {
            "cipher_suite": "TLS_CHACHA20_POLY1305_SHA256",
            "failure": null,
            "negotiated_proto": "h3",
            "tls_version": "TLSv1.3",
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
            "t": 9.055151584,
            "address": "8.8.8.8:443",
            "server_name": "dns.google",
            "alpn": [
              "h3"
            ],
            "no_tls_verify": false,
            "proto": "quic",
            "started": 9.00669725
          }
        ]
      }
    ]
  },
  "test_name": "simplequicping",
  "test_runtime": 9.055608292,
  "test_start_time": "2022-05-09 08:57:34",
  "test_version": "0.1.0"
}
```

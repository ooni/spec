# Specification version number

2022-06-22

* _status_: experimental

# Specification name

`tlsping` (TLS ping)

# Test preconditions

* An internet connection

# Expected impact

The possibility of pinging a TLS endpoint.

# Expected inputs

* A URL like `tlshandshake://<host>:<port>`.

* An optional SNI to use (`-O SNI=value` with `miniooni`).

# Test description

The experiment will attempt to connect and handshake to the given TLS
endpoint every second for ten times and return the results.

# Expected output

## Parent data format

* `df-005-tcpconnect`
* `df-006-tlshandshake`
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
	"tcp_connect": {},
	"tls_handshake": {},
	"network_events": []
}
```

where:

- `tcp_connect` contains a single `df-005-tcpconnect` entry;

- `tls_handshake` is `null` or contains a single `df-006-tlshandhsake` entry;

- `network_events` contains zero or more `df-008-netevents`.

Before 2022-06-22, `tcp_connect` and `tls_handshake` were lists but we
changed that because this is an experimental nettest and it seems better
to avoid suggesting there could be more than a single TCP connect or
TLS handshake for each ping.

## Possible conclusions

This experiment is an exploratory tool. There is no immediate conclusion
from its results but it is useful to perform censorship research.

## Example output sample

```JSON
{
  "annotations": {
    "architecture": "arm64",
    "engine_name": "ooniprobe-engine",
    "engine_version": "3.16.0-alpha",
    "platform": "macos"
  },
  "data_format_version": "0.2.0",
  "input": "tlshandshake://8.8.8.8:443",
  "measurement_start_time": "2022-06-22 13:35:52",
  "probe_asn": "AS30722",
  "probe_cc": "IT",
  "probe_ip": "127.0.0.1",
  "probe_network_name": "Vodafone Italia S.p.A.",
  "report_id": "20220622T133553Z_tlsping_IT_30722_n1_0JetDxlZogmOkyl1",
  "resolver_asn": "AS30722",
  "resolver_ip": "91.80.36.88",
  "resolver_network_name": "Vodafone Italia S.p.A.",
  "software_name": "miniooni",
  "software_version": "3.16.0-alpha",
  "test_keys": {
    "pings": [
      {
        "network_events": [
          {
            "failure": null,
            "operation": "tls_handshake_start",
            "t": 0.023754
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 257,
            "operation": "write",
            "proto": "tcp",
            "t": 0.024266
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 517,
            "operation": "read",
            "proto": "tcp",
            "t": 0.059809
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 4304,
            "operation": "read",
            "proto": "tcp",
            "t": 0.060063
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 64,
            "operation": "write",
            "proto": "tcp",
            "t": 0.061227
          },
          {
            "failure": null,
            "operation": "tls_handshake_done",
            "t": 0.061253
          }
        ],
        "tcp_connect": {
          "ip": "8.8.8.8",
          "port": 443,
          "status": {
            "failure": null,
            "success": true
          },
          "t": 0.01757
        },
        "tls_handshake": {
          "address": "8.8.8.8:443",
          "cipher_suite": "TLS_AES_128_GCM_SHA256",
          "failure": null,
          "negotiated_protocol": "h2",
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
          "t": 0.061253,
          "tags": [],
          "tls_version": "TLSv1.3"
        }
      },
      {
        "network_events": [
          {
            "failure": null,
            "operation": "tls_handshake_start",
            "t": 1.024821
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 257,
            "operation": "write",
            "proto": "tcp",
            "t": 1.025331
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 517,
            "operation": "read",
            "proto": "tcp",
            "t": 1.05986
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 4304,
            "operation": "read",
            "proto": "tcp",
            "t": 1.060392
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 64,
            "operation": "write",
            "proto": "tcp",
            "t": 1.062634
          },
          {
            "failure": null,
            "operation": "tls_handshake_done",
            "t": 1.062659
          }
        ],
        "tcp_connect": {
          "ip": "8.8.8.8",
          "port": 443,
          "status": {
            "failure": null,
            "success": true
          },
          "t": 1.019463
        },
        "tls_handshake": {
          "address": "8.8.8.8:443",
          "cipher_suite": "TLS_AES_128_GCM_SHA256",
          "failure": null,
          "negotiated_protocol": "h2",
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
          "t": 1.062659,
          "tags": [],
          "tls_version": "TLSv1.3"
        }
      },
      {
        "network_events": [
          {
            "failure": null,
            "operation": "tls_handshake_start",
            "t": 2.034682
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 257,
            "operation": "write",
            "proto": "tcp",
            "t": 2.035223
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 517,
            "operation": "read",
            "proto": "tcp",
            "t": 2.069912
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 4304,
            "operation": "read",
            "proto": "tcp",
            "t": 2.07037
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 64,
            "operation": "write",
            "proto": "tcp",
            "t": 2.072617
          },
          {
            "failure": null,
            "operation": "tls_handshake_done",
            "t": 2.072641
          }
        ],
        "tcp_connect": {
          "ip": "8.8.8.8",
          "port": 443,
          "status": {
            "failure": null,
            "success": true
          },
          "t": 2.028202
        },
        "tls_handshake": {
          "address": "8.8.8.8:443",
          "cipher_suite": "TLS_AES_128_GCM_SHA256",
          "failure": null,
          "negotiated_protocol": "h2",
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
          "t": 2.072641,
          "tags": [],
          "tls_version": "TLSv1.3"
        }
      },
      {
        "network_events": [
          {
            "failure": null,
            "operation": "tls_handshake_start",
            "t": 3.035112
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 257,
            "operation": "write",
            "proto": "tcp",
            "t": 3.035578
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 517,
            "operation": "read",
            "proto": "tcp",
            "t": 3.072859
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 4304,
            "operation": "read",
            "proto": "tcp",
            "t": 3.073364
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 64,
            "operation": "write",
            "proto": "tcp",
            "t": 3.076889
          },
          {
            "failure": null,
            "operation": "tls_handshake_done",
            "t": 3.076914
          }
        ],
        "tcp_connect": {
          "ip": "8.8.8.8",
          "port": 443,
          "status": {
            "failure": null,
            "success": true
          },
          "t": 3.028897
        },
        "tls_handshake": {
          "address": "8.8.8.8:443",
          "cipher_suite": "TLS_AES_128_GCM_SHA256",
          "failure": null,
          "negotiated_protocol": "h2",
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
          "t": 3.076914,
          "tags": [],
          "tls_version": "TLSv1.3"
        }
      },
      {
        "network_events": [
          {
            "failure": null,
            "operation": "tls_handshake_start",
            "t": 4.031179
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 257,
            "operation": "write",
            "proto": "tcp",
            "t": 4.031771
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 517,
            "operation": "read",
            "proto": "tcp",
            "t": 4.069636
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 4304,
            "operation": "read",
            "proto": "tcp",
            "t": 4.070171
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 64,
            "operation": "write",
            "proto": "tcp",
            "t": 4.072599
          },
          {
            "failure": null,
            "operation": "tls_handshake_done",
            "t": 4.072637
          }
        ],
        "tcp_connect": {
          "ip": "8.8.8.8",
          "port": 443,
          "status": {
            "failure": null,
            "success": true
          },
          "t": 4.025
        },
        "tls_handshake": {
          "address": "8.8.8.8:443",
          "cipher_suite": "TLS_AES_128_GCM_SHA256",
          "failure": null,
          "negotiated_protocol": "h2",
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
          "t": 4.072637,
          "tags": [],
          "tls_version": "TLSv1.3"
        }
      },
      {
        "network_events": [
          {
            "failure": null,
            "operation": "tls_handshake_start",
            "t": 5.02619
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 257,
            "operation": "write",
            "proto": "tcp",
            "t": 5.026739
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 517,
            "operation": "read",
            "proto": "tcp",
            "t": 5.061697
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 4304,
            "operation": "read",
            "proto": "tcp",
            "t": 5.062132
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 64,
            "operation": "write",
            "proto": "tcp",
            "t": 5.064267
          },
          {
            "failure": null,
            "operation": "tls_handshake_done",
            "t": 5.064293
          }
        ],
        "tcp_connect": {
          "ip": "8.8.8.8",
          "port": 443,
          "status": {
            "failure": null,
            "success": true
          },
          "t": 5.019761
        },
        "tls_handshake": {
          "address": "8.8.8.8:443",
          "cipher_suite": "TLS_AES_128_GCM_SHA256",
          "failure": null,
          "negotiated_protocol": "h2",
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
          "t": 5.064293,
          "tags": [],
          "tls_version": "TLSv1.3"
        }
      },
      {
        "network_events": [
          {
            "failure": null,
            "operation": "tls_handshake_start",
            "t": 6.025224
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 257,
            "operation": "write",
            "proto": "tcp",
            "t": 6.025806
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 517,
            "operation": "read",
            "proto": "tcp",
            "t": 6.0595040000000004
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 4304,
            "operation": "read",
            "proto": "tcp",
            "t": 6.060012
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 64,
            "operation": "write",
            "proto": "tcp",
            "t": 6.062242
          },
          {
            "failure": null,
            "operation": "tls_handshake_done",
            "t": 6.062265
          }
        ],
        "tcp_connect": {
          "ip": "8.8.8.8",
          "port": 443,
          "status": {
            "failure": null,
            "success": true
          },
          "t": 6.01936
        },
        "tls_handshake": {
          "address": "8.8.8.8:443",
          "cipher_suite": "TLS_AES_128_GCM_SHA256",
          "failure": null,
          "negotiated_protocol": "h2",
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
          "t": 6.062265,
          "tags": [],
          "tls_version": "TLSv1.3"
        }
      },
      {
        "network_events": [
          {
            "failure": null,
            "operation": "tls_handshake_start",
            "t": 7.033425
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 257,
            "operation": "write",
            "proto": "tcp",
            "t": 7.034106
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 517,
            "operation": "read",
            "proto": "tcp",
            "t": 7.070456
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 4304,
            "operation": "read",
            "proto": "tcp",
            "t": 7.070924
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 64,
            "operation": "write",
            "proto": "tcp",
            "t": 7.073219
          },
          {
            "failure": null,
            "operation": "tls_handshake_done",
            "t": 7.073242
          }
        ],
        "tcp_connect": {
          "ip": "8.8.8.8",
          "port": 443,
          "status": {
            "failure": null,
            "success": true
          },
          "t": 7.02748
        },
        "tls_handshake": {
          "address": "8.8.8.8:443",
          "cipher_suite": "TLS_AES_128_GCM_SHA256",
          "failure": null,
          "negotiated_protocol": "h2",
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
          "t": 7.073242,
          "tags": [],
          "tls_version": "TLSv1.3"
        }
      },
      {
        "network_events": [
          {
            "failure": null,
            "operation": "tls_handshake_start",
            "t": 8.034922
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 257,
            "operation": "write",
            "proto": "tcp",
            "t": 8.035452
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 517,
            "operation": "read",
            "proto": "tcp",
            "t": 8.070928
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 4304,
            "operation": "read",
            "proto": "tcp",
            "t": 8.071444
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 64,
            "operation": "write",
            "proto": "tcp",
            "t": 8.073655
          },
          {
            "failure": null,
            "operation": "tls_handshake_done",
            "t": 8.073683
          }
        ],
        "tcp_connect": {
          "ip": "8.8.8.8",
          "port": 443,
          "status": {
            "failure": null,
            "success": true
          },
          "t": 8.028687
        },
        "tls_handshake": {
          "address": "8.8.8.8:443",
          "cipher_suite": "TLS_AES_128_GCM_SHA256",
          "failure": null,
          "negotiated_protocol": "h2",
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
          "t": 8.073683,
          "tags": [],
          "tls_version": "TLSv1.3"
        }
      },
      {
        "network_events": [
          {
            "failure": null,
            "operation": "tls_handshake_start",
            "t": 9.031239
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 257,
            "operation": "write",
            "proto": "tcp",
            "t": 9.031806
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 517,
            "operation": "read",
            "proto": "tcp",
            "t": 9.068548
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 4304,
            "operation": "read",
            "proto": "tcp",
            "t": 9.068981
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 64,
            "operation": "write",
            "proto": "tcp",
            "t": 9.071266
          },
          {
            "failure": null,
            "operation": "tls_handshake_done",
            "t": 9.071298
          }
        ],
        "tcp_connect": {
          "ip": "8.8.8.8",
          "port": 443,
          "status": {
            "failure": null,
            "success": true
          },
          "t": 9.025478
        },
        "tls_handshake": {
          "address": "8.8.8.8:443",
          "cipher_suite": "TLS_AES_128_GCM_SHA256",
          "failure": null,
          "negotiated_protocol": "h2",
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
          "t": 9.071298,
          "tags": [],
          "tls_version": "TLSv1.3"
        }
      }
    ]
  },
  "test_name": "tlsping",
  "test_runtime": 9.071732,
  "test_start_time": "2022-06-22 13:35:43",
  "test_version": "0.2.0"
}
```

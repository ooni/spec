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
    "architecture": "arm64",
    "engine_name": "ooniprobe-engine",
    "engine_version": "3.16.0-alpha",
    "platform": "macos"
  },
  "data_format_version": "0.2.0",
  "input": "quichandshake://8.8.8.8:443",
  "measurement_start_time": "2022-08-17 07:02:49",
  "options": [
    "SNI=dns.google.com"
  ],
  "probe_asn": "AS30722",
  "probe_cc": "IT",
  "probe_ip": "127.0.0.1",
  "probe_network_name": "Vodafone Italia S.p.A.",
  "report_id": "",
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
            "operation": "quic_handshake_start",
            "t": 0.003335
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "udp",
            "t": 0.004701
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 0.021249
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "udp",
            "t": 0.021635
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 0.036429
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 0.036462
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 0.036478
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 0.036488
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 123,
            "operation": "read_from",
            "proto": "udp",
            "t": 0.036498
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 44,
            "operation": "write_to",
            "proto": "udp",
            "t": 0.036766
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 44,
            "operation": "write_to",
            "proto": "udp",
            "t": 0.036793
          },
          {
            "failure": null,
            "operation": "quic_handshake_done",
            "t": 0.039165
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 83,
            "operation": "write_to",
            "proto": "udp",
            "t": 0.039233
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 33,
            "operation": "write_to",
            "proto": "udp",
            "t": 0.039255
          }
        ],
        "quic_handshake": {
          "network": "udp",
          "address": "8.8.8.8:443",
          "cipher_suite": "TLS_CHACHA20_POLY1305_SHA256",
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
          "server_name": "dns.google.com",
          "t": 0.039165,
          "tags": [],
          "tls_version": "TLSv1.3"
        }
      },
      {
        "network_events": [
          {
            "failure": null,
            "operation": "quic_handshake_start",
            "t": 1.007368
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "udp",
            "t": 1.008084
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 1.02436
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "udp",
            "t": 1.024864
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 1.039606
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 1.039626
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 1.039637
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 1.039646
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 118,
            "operation": "read_from",
            "proto": "udp",
            "t": 1.039654
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 44,
            "operation": "write_to",
            "proto": "udp",
            "t": 1.0398830000000001
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 44,
            "operation": "write_to",
            "proto": "udp",
            "t": 1.039911
          },
          {
            "failure": null,
            "operation": "quic_handshake_done",
            "t": 1.042331
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 83,
            "operation": "write_to",
            "proto": "udp",
            "t": 1.042383
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 33,
            "operation": "write_to",
            "proto": "udp",
            "t": 1.042416
          }
        ],
        "quic_handshake": {
          "network": "udp",
          "address": "8.8.8.8:443",
          "cipher_suite": "TLS_CHACHA20_POLY1305_SHA256",
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
          "server_name": "dns.google.com",
          "t": 1.042331,
          "tags": [],
          "tls_version": "TLSv1.3"
        }
      },
      {
        "network_events": [
          {
            "failure": null,
            "operation": "quic_handshake_start",
            "t": 2.008042
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "udp",
            "t": 2.008891
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 2.033807
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "udp",
            "t": 2.034456
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 2.049356
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 2.049403
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 2.049418
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1250,
            "operation": "read_from",
            "proto": "udp",
            "t": 2.049429
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 67,
            "operation": "read_from",
            "proto": "udp",
            "t": 2.049439
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 44,
            "operation": "write_to",
            "proto": "udp",
            "t": 2.049783
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 44,
            "operation": "write_to",
            "proto": "udp",
            "t": 2.04993
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 83,
            "operation": "write_to",
            "proto": "udp",
            "t": 2.052212
          },
          {
            "failure": null,
            "operation": "quic_handshake_done",
            "t": 2.0521760000000002
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 33,
            "operation": "write_to",
            "proto": "udp",
            "t": 2.052277
          }
        ],
        "quic_handshake": {
          "network": "udp",
          "address": "8.8.8.8:443",
          "cipher_suite": "TLS_CHACHA20_POLY1305_SHA256",
          "failure": null,
          "negotiated_protocol": "h3",
          "no_tls_verify": false,
          "peer_certificates": [
            {
              "data": "MIIF4jCCBMqgAwIBAgIRAOGrSs5AUr+eCpPWC6H6QqkwDQYJKoZIhvcNAQELBQAwRjELMAkGA1UEBhMCVVMxIjAgBgNVBAoTGUdvb2dsZSBUcnVzdCBTZXJ2aWNlcyBMTEMxEzARBgNVBAMTCkdUUyBDQSAxQzMwHhcNMjIwODAxMDgyNTI1WhcNMjIxMDI0MDgyNTI0WjAVMRMwEQYDVQQDEwpkbnMuZ29vZ2xlMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAt6rR6OrPzvoHAYOoJKrHlICotv6L+wyqxGHmZ0R3BH3ZrwreQGKpYRpwmqcElIo49E/XfUpKPYF+N3lqx862OcQar1BR5j2nODklVGuGA7zcekSeDDOpw2vrVvz4ozfsTzmFNRL4oIjhqRf3sThbNPriwBP+Ojis0xJPbQxYl1JNZHSlVIpQbT7U0Tc/fc0K4dDyTFtfVKWn/ZW1T7F91U4Dp7cI8dd73LCPgDluX3r2KiooRBD9QonjNOEDsiA646RxKiduI3oVjPFnPKkGRl9IXvDByPksK6y+2/buYDoilcB2JE6yavfNvWiEaE+2naGUdSxzu8UteEHi2hYufQIDAQABo4IC+jCCAvYwDgYDVR0PAQH/BAQDAgWgMBMGA1UdJQQMMAoGCCsGAQUFBwMBMAwGA1UdEwEB/wQCMAAwHQYDVR0OBBYEFKKpCGiPqTCDxkO8P4v/6gaWUYYjMB8GA1UdIwQYMBaAFIp0f6+Fze6VzT2c0OJGFPNxNR0nMGoGCCsGAQUFBwEBBF4wXDAnBggrBgEFBQcwAYYbaHR0cDovL29jc3AucGtpLmdvb2cvZ3RzMWMzMDEGCCsGAQUFBzAChiVodHRwOi8vcGtpLmdvb2cvcmVwby9jZXJ0cy9ndHMxYzMuZGVyMIGsBgNVHREEgaQwgaGCCmRucy5nb29nbGWCDmRucy5nb29nbGUuY29tghAqLmRucy5nb29nbGUuY29tggs4ODg4Lmdvb2dsZYIQZG5zNjQuZG5zLmdvb2dsZYcECAgICIcECAgEBIcQIAFIYEhgAAAAAAAAAACIiIcQIAFIYEhgAAAAAAAAAACIRIcQIAFIYEhgAAAAAAAAAABkZIcQIAFIYEhgAAAAAAAAAAAAZDAhBgNVHSAEGjAYMAgGBmeBDAECATAMBgorBgEEAdZ5AgUDMDwGA1UdHwQ1MDMwMaAvoC2GK2h0dHA6Ly9jcmxzLnBraS5nb29nL2d0czFjMy9RcUZ4Ymk5TTQ4Yy5jcmwwggEDBgorBgEEAdZ5AgQCBIH0BIHxAO8AdQBGpVXrdfqRIDC1oolp9PN9ESxBdL79SbiFq/L8cP5tRwAAAYJYuYOOAAAEAwBGMEQCIGynE2sRsMd6+1M5GdXGHViybpu2ahX3TFvl1pcJWCCBAiBotS0w2e+wglFpUYc+GXIgTb1wXTc7+jvuPCSooJWBLwB2AAWcAdMg4AeEE5WASY0RfJAyZq+vclC1rztGpD4RhA1KAAABgli5gykAAAQDAEcwRQIgTZZQSJ+jX+yf7R3UOlWVin30Q5AcbHPEmHYgcLUBLGECIQDpWP//j9aPWqS4XaLfrPL2r8vhU/MqEZGnQXZuQ9OhRTANBgkqhkiG9w0BAQsFAAOCAQEAFTFNlpYGPsUAlLVuAEK/otUyIP691dka+06kMNLu27bcaS/ENd+x5pN8oTaJkhbbRR7UxonwThJRsXt6L3JrK9mrsDmgd8pimj6uuHEAAC/dAsVp6JcWOq+/DY9MGOjhpI2ZyOgeQwrPN8aHOLOdzC+xnCt5vxn6L4N+B2VOebSD3JzduNHCRMLQZR7B72Xqp0wp0t7xnjKaPfVLt6WUUNTnRyKb1XkHGDFfRGbGRwgIDJbKqo2phUCMQK+58Uw7XGT2mc3IIZOwYmLEH3zzP/BXozWzXU7GxjJyGam1dCcKKhOd2nJYAbJWaTcLJwpRQAejMkCs/BguB7inuQyDDQ==",
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
          "server_name": "dns.google.com",
          "t": 2.0521760000000002,
          "tags": [],
          "tls_version": "TLSv1.3"
        }
      },
      {
        "network_events": [
          {
            "failure": null,
            "operation": "quic_handshake_start",
            "t": 3.007032
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "udp",
            "t": 3.007806
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 3.034307
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "udp",
            "t": 3.034943
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 3.049653
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 3.049674
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 44,
            "operation": "write_to",
            "proto": "udp",
            "t": 3.049882
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 3.050053
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 44,
            "operation": "write_to",
            "proto": "udp",
            "t": 3.050167
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 3.050311
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 112,
            "operation": "read_from",
            "proto": "udp",
            "t": 3.050879
          },
          {
            "failure": null,
            "operation": "quic_handshake_done",
            "t": 3.052741
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 83,
            "operation": "write_to",
            "proto": "udp",
            "t": 3.052787
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 33,
            "operation": "write_to",
            "proto": "udp",
            "t": 3.05281
          }
        ],
        "quic_handshake": {
          "network": "udp",
          "address": "8.8.8.8:443",
          "cipher_suite": "TLS_CHACHA20_POLY1305_SHA256",
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
          "server_name": "dns.google.com",
          "t": 3.052741,
          "tags": [],
          "tls_version": "TLSv1.3"
        }
      },
      {
        "network_events": [
          {
            "failure": null,
            "operation": "quic_handshake_start",
            "t": 4.007468
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "udp",
            "t": 4.008063
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 4.026252
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "udp",
            "t": 4.026699
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 4.042093
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 4.042118
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 44,
            "operation": "write_to",
            "proto": "udp",
            "t": 4.042329
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 4.042497
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1249,
            "operation": "read_from",
            "proto": "udp",
            "t": 4.042517
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 44,
            "operation": "write_to",
            "proto": "udp",
            "t": 4.042669
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 66,
            "operation": "read_from",
            "proto": "udp",
            "t": 4.042791
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 83,
            "operation": "write_to",
            "proto": "udp",
            "t": 4.044674
          },
          {
            "failure": null,
            "operation": "quic_handshake_done",
            "t": 4.044655
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 33,
            "operation": "write_to",
            "proto": "udp",
            "t": 4.044726
          }
        ],
        "quic_handshake": {
          "network": "udp",
          "address": "8.8.8.8:443",
          "cipher_suite": "TLS_CHACHA20_POLY1305_SHA256",
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
          "server_name": "dns.google.com",
          "t": 4.044655,
          "tags": [],
          "tls_version": "TLSv1.3"
        }
      },
      {
        "network_events": [
          {
            "failure": null,
            "operation": "quic_handshake_start",
            "t": 5.006062
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "udp",
            "t": 5.006859
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 5.030939
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "udp",
            "t": 5.031952
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 5.046867
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 5.046898
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 5.046914
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 5.046924
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 121,
            "operation": "read_from",
            "proto": "udp",
            "t": 5.046933
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 44,
            "operation": "write_to",
            "proto": "udp",
            "t": 5.047195
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 44,
            "operation": "write_to",
            "proto": "udp",
            "t": 5.047224
          },
          {
            "failure": null,
            "operation": "quic_handshake_done",
            "t": 5.049355
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 83,
            "operation": "write_to",
            "proto": "udp",
            "t": 5.049391
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 33,
            "operation": "write_to",
            "proto": "udp",
            "t": 5.049409
          }
        ],
        "quic_handshake": {
          "network": "udp",
          "address": "8.8.8.8:443",
          "cipher_suite": "TLS_CHACHA20_POLY1305_SHA256",
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
          "server_name": "dns.google.com",
          "t": 5.049355,
          "tags": [],
          "tls_version": "TLSv1.3"
        }
      },
      {
        "network_events": [
          {
            "failure": null,
            "operation": "quic_handshake_start",
            "t": 6.006135
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "udp",
            "t": 6.006759
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 6.033162
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "udp",
            "t": 6.033756
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 6.049427
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 6.049449
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 6.04946
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 6.049479
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 44,
            "operation": "write_to",
            "proto": "udp",
            "t": 6.049691
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 44,
            "operation": "write_to",
            "proto": "udp",
            "t": 6.049724
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 112,
            "operation": "read_from",
            "proto": "udp",
            "t": 6.049852
          },
          {
            "failure": null,
            "operation": "quic_handshake_done",
            "t": 6.052058
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 83,
            "operation": "write_to",
            "proto": "udp",
            "t": 6.052114
          }
        ],
        "quic_handshake": {
          "network": "udp",
          "address": "8.8.8.8:443",
          "cipher_suite": "TLS_CHACHA20_POLY1305_SHA256",
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
          "server_name": "dns.google.com",
          "t": 6.052058,
          "tags": [],
          "tls_version": "TLSv1.3"
        }
      },
      {
        "network_events": [
          {
            "failure": null,
            "operation": "quic_handshake_start",
            "t": 7.007972
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "udp",
            "t": 7.008648
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 7.026599
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "udp",
            "t": 7.027102
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 7.041764
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 7.041781
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 44,
            "operation": "write_to",
            "proto": "udp",
            "t": 7.041964
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 7.042114
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 44,
            "operation": "write_to",
            "proto": "udp",
            "t": 7.042236
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 7.043151
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 115,
            "operation": "read_from",
            "proto": "udp",
            "t": 7.04317
          },
          {
            "failure": null,
            "operation": "quic_handshake_done",
            "t": 7.045537
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 83,
            "operation": "write_to",
            "proto": "udp",
            "t": 7.045594
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 33,
            "operation": "write_to",
            "proto": "udp",
            "t": 7.045615
          }
        ],
        "quic_handshake": {
          "network": "udp",
          "address": "8.8.8.8:443",
          "cipher_suite": "TLS_CHACHA20_POLY1305_SHA256",
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
          "server_name": "dns.google.com",
          "t": 7.045537,
          "tags": [],
          "tls_version": "TLSv1.3"
        }
      },
      {
        "network_events": [
          {
            "failure": null,
            "operation": "quic_handshake_start",
            "t": 8.007323
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "udp",
            "t": 8.008004
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 8.032325
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "udp",
            "t": 8.032996
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 8.048141
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 8.048162
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 8.048175
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 8.048207
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 120,
            "operation": "read_from",
            "proto": "udp",
            "t": 8.048217
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 44,
            "operation": "write_to",
            "proto": "udp",
            "t": 8.04848
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 44,
            "operation": "write_to",
            "proto": "udp",
            "t": 8.04851
          },
          {
            "failure": null,
            "operation": "quic_handshake_done",
            "t": 8.051096
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 83,
            "operation": "write_to",
            "proto": "udp",
            "t": 8.05115
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 33,
            "operation": "write_to",
            "proto": "udp",
            "t": 8.051177
          }
        ],
        "quic_handshake": {
          "network": "udp",
          "address": "8.8.8.8:443",
          "cipher_suite": "TLS_CHACHA20_POLY1305_SHA256",
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
          "server_name": "dns.google.com",
          "t": 8.051096,
          "tags": [],
          "tls_version": "TLSv1.3"
        }
      },
      {
        "network_events": [
          {
            "failure": null,
            "operation": "quic_handshake_start",
            "t": 9.00743
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "udp",
            "t": 9.00814
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 9.03142
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "write_to",
            "proto": "udp",
            "t": 9.031964
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 9.047808
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 9.04784
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 9.047859
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 1252,
            "operation": "read_from",
            "proto": "udp",
            "t": 9.047869
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 122,
            "operation": "read_from",
            "proto": "udp",
            "t": 9.04788
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 44,
            "operation": "write_to",
            "proto": "udp",
            "t": 9.048148
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 44,
            "operation": "write_to",
            "proto": "udp",
            "t": 9.048224
          },
          {
            "failure": null,
            "operation": "quic_handshake_done",
            "t": 9.050672
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 83,
            "operation": "write_to",
            "proto": "udp",
            "t": 9.050718
          },
          {
            "address": "8.8.8.8:443",
            "failure": null,
            "num_bytes": 33,
            "operation": "write_to",
            "proto": "udp",
            "t": 9.050743
          }
        ],
        "quic_handshake": {
          "network": "udp",
          "address": "8.8.8.8:443",
          "cipher_suite": "TLS_CHACHA20_POLY1305_SHA256",
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
          "server_name": "dns.google.com",
          "t": 9.050672,
          "tags": [],
          "tls_version": "TLSv1.3"
        }
      }
    ]
  },
  "test_name": "simplequicping",
  "test_runtime": 9.051085541,
  "test_start_time": "2022-08-17 07:02:40",
  "test_version": "0.2.0"
}
```

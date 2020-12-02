# Specification version number

2020-12-02-000

# Specification name

urlgetter

# Test preconditions

* An internet connection

# Expected impact

The ability to perform custom, exploratory measurements.

# Expected inputs

This experiment takes in input a list of URLs. The following URL
templates are supported:

1. `http://<domain>/<path>`;

2. `https://<domain>/<path>`;

3. `dnslookup://<domain>`;

4. `tcpconnect://<domain>:<port>`;

5. `tlshandshake://<domain>:<port>`.

The first and the second URL templates cause urlgetter to fetch the
corresponding resource over, respectively, HTTP and HTTPS.

The third URL template causes urlgetter to perform a DNS lookup.

The fourth URL template causes urlgetter to perform a TCP connect
to the specified TCP endpoint.

The fifth URL template causes urlgetter to perform a TLS handshake
to the specified endpoint.

In all the above cases but the third, `<domain>` could actually also
be an IP address. A `<port>` could of course also be added to the
first and the second URLs, otherwise we'll use `80` and `443`.

The urlgetter experiment also supports a rich set of options that
allow you to tweak several aspects of the experiment via the command
line. (As of this writing, urlgetter is only available through the
research client `miniooni`.) Documenting these options is beyond the
scope of this specification. Since urlgetter is meant to be used
for researching new tests and for investigating new censorship
conditions, we expect the set of such options to change over time.

# Test description

This test will loop over the provided URLs. The performed action
depends on the URL schema, as documented above. The specified options
will be added to the measurement into the toplevel `options` field
(as documented in the example below).

Analysing a urlgetter measurement without taking into account the
options that were provided is not recommended.

# Expected output

## Parent data format

* `df-001-httpt`
* `df-002-dnst`
* `df-005-tcpconnect`
* `df-006-tlshandshake`
* `df-008-netevents`
* `df-009-tunnel`

## Semantics

This is the minimal set of keys supported by urlgetter inside
the toplevel `test_keys` key of the measurement:

```JSON
{
    "agent": "",
    "answers": [],
    "failure": null,
    "network_events": [],
    "requests": [],
    "socksproxy": "",
    "tcp_connect": [],
    "tls_handshakes": [],
}
```

Where:

- `agent`, `requests`, `socksproxy` conform to `df-001-httpt`;

- `answers` conforms to `df-002-dnst`;

- `failure` conforms to `df-007-errors`;

- `network_events` conforms to `df-008-netevents`;

- `tcp_connect` conforms to `df-005-tcpconnect`;

- `tls_handshake` conforms to `df-006-tlshandshake`.

## Possible conclusions

It heavily depends on what is being tested.

## Example output sample

```JSON
{
  "data_format_version": "0.2.0",
  "extensions": {
    "dnst": 0,
    "httpt": 0,
    "netevents": 0,
    "tcpconnect": 0,
    "tlshandshake": 0,
    "tunnel": 0
  },
  "input": "https://www.example.com",
  "measurement_start_time": "2020-12-02 11:35:39",
  "options": [
    "ResolverURL=udp://8.8.8.8:53"
  ],
  "probe_asn": "AS30722",
  "probe_cc": "IT",
  "probe_ip": "127.0.0.1",
  "probe_network_name": "Vodafone Italia S.p.A.",
  "report_id": "20201202T113539Z_urlgetter_IT_30722_n1_c42SmSf6rGmss4XP",
  "resolver_asn": "AS30722",
  "resolver_ip": "91.80.36.84",
  "resolver_network_name": "Vodafone Italia S.p.A.",
  "software_name": "miniooni",
  "software_version": "0.21.0-alpha",
  "test_keys": {
    "agent": "redirect",
    "failed_operation": null,
    "failure": null,
    "network_events": [
      {
        "failure": null,
        "operation": "http_transaction_start",
        "t": 7.1487e-05
      },
      {
        "failure": null,
        "operation": "http_request_metadata",
        "t": 8.0611e-05
      },
      {
        "failure": null,
        "operation": "resolve_start",
        "t": 0.000315444
      },
      {
        "failure": null,
        "operation": "dns_round_trip_start",
        "t": 0.000371921
      },
      {
        "address": "8.8.8.8:53",
        "failure": null,
        "operation": "connect",
        "proto": "udp",
        "t": 0.000553384
      },
      {
        "failure": null,
        "num_bytes": 33,
        "operation": "write",
        "t": 0.000623424
      },
      {
        "failure": null,
        "num_bytes": 49,
        "operation": "read",
        "t": 0.002880351
      },
      {
        "failure": null,
        "operation": "dns_round_trip_done",
        "t": 0.002923513
      },
      {
        "failure": null,
        "operation": "dns_round_trip_start",
        "t": 0.002947776
      },
      {
        "address": "8.8.8.8:53",
        "failure": null,
        "operation": "connect",
        "proto": "udp",
        "t": 0.003107118
      },
      {
        "failure": null,
        "num_bytes": 33,
        "operation": "write",
        "t": 0.00315497
      },
      {
        "failure": null,
        "num_bytes": 61,
        "operation": "read",
        "t": 0.005240764
      },
      {
        "failure": null,
        "operation": "dns_round_trip_done",
        "t": 0.005282692
      },
      {
        "failure": null,
        "operation": "resolve_done",
        "t": 0.0053319
      },
      {
        "address": "93.184.216.34:443",
        "failure": null,
        "operation": "connect",
        "proto": "tcp",
        "t": 0.117211317
      },
      {
        "failure": null,
        "operation": "tls_handshake_start",
        "t": 0.117224381
      },
      {
        "failure": null,
        "num_bytes": 285,
        "operation": "write",
        "t": 0.117431559
      },
      {
        "failure": null,
        "num_bytes": 99,
        "operation": "read",
        "t": 0.229206014
      },
      {
        "failure": null,
        "num_bytes": 6,
        "operation": "write",
        "t": 0.229258361
      },
      {
        "failure": null,
        "num_bytes": 318,
        "operation": "write",
        "t": 0.229372467
      },
      {
        "failure": null,
        "num_bytes": 517,
        "operation": "read",
        "t": 0.341612798
      },
      {
        "failure": null,
        "num_bytes": 3579,
        "operation": "read",
        "t": 0.342327195
      },
      {
        "failure": null,
        "num_bytes": 947,
        "operation": "read",
        "t": 0.343752074
      },
      {
        "failure": null,
        "num_bytes": 74,
        "operation": "write",
        "t": 0.345996672
      },
      {
        "failure": null,
        "operation": "tls_handshake_done",
        "t": 0.346018496
      },
      {
        "failure": null,
        "num_bytes": 86,
        "operation": "write",
        "t": 0.346215634
      },
      {
        "failure": null,
        "num_bytes": 206,
        "operation": "write",
        "t": 0.346327698
      },
      {
        "failure": null,
        "operation": "http_wrote_headers",
        "t": 0.346329376
      },
      {
        "failure": null,
        "operation": "http_wrote_request",
        "t": 0.346329753
      },
      {
        "failure": null,
        "num_bytes": 255,
        "operation": "read",
        "t": 0.457220236
      },
      {
        "failure": null,
        "num_bytes": 255,
        "operation": "read",
        "t": 0.457427977
      },
      {
        "failure": null,
        "num_bytes": 127,
        "operation": "read",
        "t": 0.457591673
      },
      {
        "failure": null,
        "num_bytes": 31,
        "operation": "write",
        "t": 0.457665351
      },
      {
        "failure": null,
        "num_bytes": 1440,
        "operation": "read",
        "t": 0.458069759
      },
      {
        "failure": null,
        "operation": "http_first_response_byte",
        "t": 0.458217799
      },
      {
        "failure": null,
        "operation": "http_response_metadata",
        "t": 0.458304478
      },
      {
        "failure": null,
        "num_bytes": 76,
        "operation": "read",
        "t": 0.458366819
      },
      {
        "failure": null,
        "operation": "http_response_body_snapshot",
        "t": 0.458438134
      },
      {
        "failure": null,
        "operation": "http_transaction_done",
        "t": 0.458439328
      },
      {
        "failure": null,
        "num_bytes": 24,
        "operation": "write",
        "t": 0.45850991
      }
    ],
    "queries": [
      {
        "answers": [
          {
            "asn": 15133,
            "as_org_name": "MCI Communications Services, Inc. d/b/a Verizon Business",
            "answer_type": "A",
            "ipv4": "93.184.216.34",
            "ttl": null
          }
        ],
        "engine": "udp",
        "failure": null,
        "hostname": "www.example.com",
        "query_type": "A",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "8.8.8.8:53",
        "t": 0.0053319
      },
      {
        "answers": [
          {
            "asn": 15133,
            "as_org_name": "MCI Communications Services, Inc. d/b/a Verizon Business",
            "answer_type": "AAAA",
            "ipv6": "2606:2800:220:1:248:1893:25c8:1946",
            "ttl": null
          }
        ],
        "engine": "udp",
        "failure": null,
        "hostname": "www.example.com",
        "query_type": "AAAA",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "8.8.8.8:53",
        "t": 0.0053319
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
              "www.example.com"
            ],
            [
              "User-Agent",
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
            ]
          ],
          "headers": {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US;q=0.8,en;q=0.5",
            "Host": "www.example.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
          },
          "method": "GET",
          "tor": {
            "exit_ip": null,
            "exit_name": null,
            "is_tor": false
          },
          "x_transport": "h2 / http/1.1",
          "url": "https://www.example.com"
        },
        "response": {
          "body": "<!doctype html>\n<html>\n<head>\n    <title>Example Domain</title>\n\n    <meta charset=\"utf-8\" />\n    <meta http-equiv=\"Content-type\" content=\"text/html; charset=utf-8\" />\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />\n    <style type=\"text/css\">\n    body {\n        background-color: #f0f0f2;\n        margin: 0;\n        padding: 0;\n        font-family: -apple-system, system-ui, BlinkMacSystemFont, \"Segoe UI\", \"Open Sans\", \"Helvetica Neue\", Helvetica, Arial, sans-serif;\n        \n    }\n    div {\n        width: 600px;\n        margin: 5em auto;\n        padding: 2em;\n        background-color: #fdfdff;\n        border-radius: 0.5em;\n        box-shadow: 2px 3px 7px 2px rgba(0,0,0,0.02);\n    }\n    a:link, a:visited {\n        color: #38488f;\n        text-decoration: none;\n    }\n    @media (max-width: 700px) {\n        div {\n            margin: 0 auto;\n            width: auto;\n        }\n    }\n    </style>    \n</head>\n\n<body>\n<div>\n    <h1>Example Domain</h1>\n    <p>This domain is for use in illustrative examples in documents. You may use this\n    domain in literature without prior coordination or asking for permission.</p>\n    <p><a href=\"https://www.iana.org/domains/example\">More information...</a></p>\n</div>\n</body>\n</html>\n",
          "body_is_truncated": false,
          "code": 200,
          "headers_list": [
            [
              "Accept-Ranges",
              "bytes"
            ],
            [
              "Age",
              "443014"
            ],
            [
              "Cache-Control",
              "max-age=604800"
            ],
            [
              "Content-Length",
              "1256"
            ],
            [
              "Content-Type",
              "text/html; charset=UTF-8"
            ],
            [
              "Date",
              "Wed, 02 Dec 2020 11:35:40 GMT"
            ],
            [
              "Etag",
              "\"3147526947\""
            ],
            [
              "Expires",
              "Wed, 09 Dec 2020 11:35:40 GMT"
            ],
            [
              "Last-Modified",
              "Thu, 17 Oct 2019 07:18:26 GMT"
            ],
            [
              "Server",
              "ECS (dcb/7EA7)"
            ],
            [
              "Vary",
              "Accept-Encoding"
            ],
            [
              "X-Cache",
              "HIT"
            ]
          ],
          "headers": {
            "Accept-Ranges": "bytes",
            "Age": "443014",
            "Cache-Control": "max-age=604800",
            "Content-Length": "1256",
            "Content-Type": "text/html; charset=UTF-8",
            "Date": "Wed, 02 Dec 2020 11:35:40 GMT",
            "Etag": "\"3147526947\"",
            "Expires": "Wed, 09 Dec 2020 11:35:40 GMT",
            "Last-Modified": "Thu, 17 Oct 2019 07:18:26 GMT",
            "Server": "ECS (dcb/7EA7)",
            "Vary": "Accept-Encoding",
            "X-Cache": "HIT"
          }
        },
        "t": 7.1487e-05
      }
    ],
    "tcp_connect": [
      {
        "ip": "8.8.8.8",
        "port": 53,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.000553384
      },
      {
        "ip": "8.8.8.8",
        "port": 53,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.003107118
      },
      {
        "ip": "93.184.216.34",
        "port": 443,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.117211317
      }
    ],
    "tls_handshakes": [
      {
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
            "data": "MIIE6jCCA9KgAwIBAgIQCjUI1VwpKwF9+K1lwA/35DANBgkqhkiG9w0BAQsFADBhMQswCQYDVQQGEwJVUzEVMBMGA1UEChMMRGlnaUNlcnQgSW5jMRkwFwYDVQQLExB3d3cuZGlnaWNlcnQuY29tMSAwHgYDVQQDExdEaWdpQ2VydCBHbG9iYWwgUm9vdCBDQTAeFw0yMDA5MjQwMDAwMDBaFw0zMDA5MjMyMzU5NTlaME8xCzAJBgNVBAYTAlVTMRUwEwYDVQQKEwxEaWdpQ2VydCBJbmMxKTAnBgNVBAMTIERpZ2lDZXJ0IFRMUyBSU0EgU0hBMjU2IDIwMjAgQ0ExMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwUuzZUdwvN1PWNvsnO3DZuUfMRNUrUpmRh8sCuxkB+Uu3Ny5CiDt3+PE0J6aqXodgojlEVbbHp9YwlHnLDQNLtKS4VbL8Xlfs7uHyiUDe5pSQWYQYE9XE0nw6Ddng9/n00tnTCJRpt8OmRDtV1F0JuJ9x8piLhMbfyOIJVNvwTRYAIuE//i+p1hJInuWraKImxW8oHzf6VGo1bDtN+I2tIJLYrVJmuzHZ9bjPvXj1hJeRPG/cUJ9WIQDgLGBAfr5yjK7tI4nhyfFK3TUqNaX3sNk+crOU6JWvHgXjkkDKa77SU+kFbnO8lwZV21reacroicgE7XQPUDTITAHk+qZ9QIDAQABo4IBrjCCAaowHQYDVR0OBBYEFLdrouqoqoSMeeq02g+YssWVdrn0MB8GA1UdIwQYMBaAFAPeUDVW0Uy7ZvCj4hsbw5eyPdFVMA4GA1UdDwEB/wQEAwIBhjAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwEgYDVR0TAQH/BAgwBgEB/wIBADB2BggrBgEFBQcBAQRqMGgwJAYIKwYBBQUHMAGGGGh0dHA6Ly9vY3NwLmRpZ2ljZXJ0LmNvbTBABggrBgEFBQcwAoY0aHR0cDovL2NhY2VydHMuZGlnaWNlcnQuY29tL0RpZ2lDZXJ0R2xvYmFsUm9vdENBLmNydDB7BgNVHR8EdDByMDegNaAzhjFodHRwOi8vY3JsMy5kaWdpY2VydC5jb20vRGlnaUNlcnRHbG9iYWxSb290Q0EuY3JsMDegNaAzhjFodHRwOi8vY3JsNC5kaWdpY2VydC5jb20vRGlnaUNlcnRHbG9iYWxSb290Q0EuY3JsMDAGA1UdIAQpMCcwBwYFZ4EMAQEwCAYGZ4EMAQIBMAgGBmeBDAECAjAIBgZngQwBAgMwDQYJKoZIhvcNAQELBQADggEBAHert3onPa679n/gWlbJhKrKW3EX3SJH/E6f7tDBpATho+vFScH90cnfjK+URSxGKqNjOSD5nkoklEHIqdninFQFBstcHL4AGw+oWv8Zu2XHFq8hVt1hBcnpj5h232sb0HIMULkwKXq/YFkQZhM6LawVEWwtIwwCPgU7/uWhnOKK24fXSuhe50gG66sSmvKvhMNbg0qZgYOrAKHKCjxMoiWJKiKnpPMzTFuMLhoClw+dj20tlQj7T9rxkTgl4ZxuYRiHas6xuwAwapu3r9rxxZf+ingkquqTgLozZXq8oXfpf2kUCwA/d5KxTVtzhwoT0JzI8ks5T1KESaZMkE4f97Q=",
            "format": "base64"
          },
          {
            "data": "MIIDrzCCApegAwIBAgIQCDvgVpBCRrGhdWrJWZHHSjANBgkqhkiG9w0BAQUFADBhMQswCQYDVQQGEwJVUzEVMBMGA1UEChMMRGlnaUNlcnQgSW5jMRkwFwYDVQQLExB3d3cuZGlnaWNlcnQuY29tMSAwHgYDVQQDExdEaWdpQ2VydCBHbG9iYWwgUm9vdCBDQTAeFw0wNjExMTAwMDAwMDBaFw0zMTExMTAwMDAwMDBaMGExCzAJBgNVBAYTAlVTMRUwEwYDVQQKEwxEaWdpQ2VydCBJbmMxGTAXBgNVBAsTEHd3dy5kaWdpY2VydC5jb20xIDAeBgNVBAMTF0RpZ2lDZXJ0IEdsb2JhbCBSb290IENBMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA4jvhEXLeqKTTo1eqUKKPC3eQyaKl7hLOllsBCSDMAZOnTjC3U/dDxGkAV53ijSLdhwZAAIEJzs4bg7/fzTtxRuLWZscFs3YnFo97nh6Vfe63SKMI2tavegw5BmV/Sl0fvBf4q77uKNd0f3p4mVmFaG5cIzJLv07A6Fpt43C/dxC//AH2hdmoRBBYMql1GNXRor5H4idq9Joz+EkIYIvUX7Q6hL+hqkpMfT7PT19sdl6gSzeRntwi5m3OFBqOasv+zbMUZBfHWymeMr/y7vrTC0LUq7dBMtoM1O/4gdW7jVg/tRvoSSiicNoxBN33shbyTApOB6jtSj1etX+jkMOvJwIDAQABo2MwYTAOBgNVHQ8BAf8EBAMCAYYwDwYDVR0TAQH/BAUwAwEB/zAdBgNVHQ4EFgQUA95QNVbRTLtm8KPiGxvDl7I90VUwHwYDVR0jBBgwFoAUA95QNVbRTLtm8KPiGxvDl7I90VUwDQYJKoZIhvcNAQEFBQADggEBAMucN6pIExIK+t1EnE9SsPTfrgT1eXkIoyQY/EsrhMAtudXH/vTBH1jLuG2cenTnmCmrEbXjcKChzUyImZOMkXDiqw8cvpOp/2PV5Adg06O/nVsJ8dWO41P0jmP6P6fbtGbfYmbW0W5BjfIttep3Sp+dWOIrWcBAI+0tKIJFPnlUkiaY4IBIqDfv8NZ5YBberOgOzW6sRBc4L0na4UU+Krk2U886UAb3LujEV0lsYSEY1QSteDwsOoBrp+uvFRTp2InBuThs4pFsiv9kuXclVzDAGySj4dzp30d8tbQkCAUw7C29C79Fv1C5qfPrmAESrciIxpg0X40KPMbp1ZWVbd4=",
            "format": "base64"
          }
        ],
        "server_name": "www.example.com",
        "t": 0.346018496,
        "tls_version": "TLSv1.3"
      }
    ]
  },
  "test_name": "urlgetter",
  "test_runtime": 0.459312974,
  "test_start_time": "2020-12-02 11:35:39",
  "test_version": "0.1.0"
}
```

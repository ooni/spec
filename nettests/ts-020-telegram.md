# Specification version number

2022-12-07-001

* _status_: current

# Specification name

Telegram

# Test preconditions

* An internet connection

# Expected impact

Ability to detect if the Telegram instant messaging platform and the web
version are working, by checking if it's possible to establish a TCP connection
with the IPs of the access points or receive a response back from a HTTPS GET
request.

# Expected inputs

None

# Test description

This test will check if 2 services are working as they should:

1. The Telegram access points (DCs) (the addresses used by the Telegram desktop client)

2. The Telegram web version

## Telegram access points check

The Telegram access points (DCs) are those used by the [Telegram desktop client](https://github.com/telegramdesktop/tdesktop/blob/e6d94b5ee7d96a97ee5976dacb87bafd00beac1d/Telegram/SourceFiles/config.h#L205).

These access points have the following IP addresses:

* 149.154.175.50
* 149.154.167.51
* 149.154.175.100
* 149.154.167.91
* 149.154.171.5

The test establishes TCP connection to all the access point IP addresses and
then attempts to issue a POST request to each of them.

If all TCP connections on ports 80 and 443 to Telegram’s access point IPs fail
we consider Telegram to be blocked. The key `telegram_tcp_blocking` is used
to indicate if we believe telegram to be blocked at the TCP level.

If at least an HTTP request returns back a response, we consider Telegram to
not be blocked. The key `telegram_http_blocking` is used to indicate if we believe
telegram to be blocked at the HTTP level.

## Telegram web version test

Telegram’s web version is likely blocked if an HTTPS GET request on port
443 to `web.telegram.org` does not send back a response to OONI Probe.

If the TLS handshake fails or we cannot get back a response (e.g., because
we get an error when reading the body), we consider the web version of
Telegram to be blocked.

Until 2022-12-07, we also tested `http://web.telegram.org/` and we had
heuristics concerning the returned webpage's title. After that date, we
have simplified the check in [ooni/probe-cli#999](https://github.com/ooni/probe-cli/pull/999)
to increase robustness against false positives.

If the HTTPS URL is blocked then we write in
the report:

```json
{
    "telegram_web_failure": "FAILURE STRING",
    "telegram_web_status": "blocked"
}
```

Otherwise, we write:

```json
{
    "telegram_web_failure": null,
    "telegram_web_status": "ok"
}
```

# Expected output

## Parent data format

* `df-001-httpt`
* `df-002-dnst` (since 2020-01-09 in ooni/probe-engine)
* `df-005-tcpconnect`
* `df-006-tlshandshake` (since 2020-01-11 in ooni/probe-engine)

## Semantics

```
{
    "telegram_http_blocking": true | false,
    "telegram_tcp_blocking": true | false,

    "telegram_web_failure": "failure_string" | null,
    "telegram_web_status": "blocked" | "ok" | null,
}
```

The meaning of the various keys is described in the above section.

## Possible conclusions

* If it is possible for users to use the Telegram software

* If it is possible for users to use the web version of Telegram

## Example output sample

```JSON
{
  "annotations": {
    "architecture": "arm64",
    "engine_name": "ooniprobe-engine",
    "engine_version": "3.17.0-alpha",
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
  "measurement_start_time": "2022-12-07 10:51:55",
  "probe_asn": "AS30722",
  "probe_cc": "IT",
  "probe_ip": "127.0.0.1",
  "probe_network_name": "Vodafone Italia S.p.A.",
  "report_id": "20221207T105155Z_telegram_IT_30722_n1_epDRF015yWFhSlX4",
  "resolver_asn": "AS30722",
  "resolver_ip": "91.80.36.88",
  "resolver_network_name": "Vodafone Italia S.p.A.",
  "software_name": "miniooni",
  "software_version": "3.17.0-alpha",
  "test_keys": {
    "agent": "redirect",
    "failed_operation": null,
    "failure": null,
    "network_events": [
      {
        "failure": null,
        "operation": "http_transaction_start",
        "t": 0.0003635
      },
      {
        "address": "149.154.167.51:80",
        "failure": null,
        "operation": "connect",
        "proto": "tcp",
        "t": 0.032989958
      },
      {
        "failure": null,
        "num_bytes": 291,
        "operation": "write",
        "t": 0.033442833
      },
      {
        "failure": null,
        "num_bytes": 324,
        "operation": "read",
        "t": 0.065323167
      },
      {
        "failure": null,
        "operation": "http_transaction_done",
        "t": 0.065531792
      },
      {
        "failure": "connection_already_closed",
        "operation": "read",
        "t": 0.065774292
      },
      {
        "failure": null,
        "operation": "http_transaction_start",
        "t": 0.065902333
      },
      {
        "address": "149.154.167.91:80",
        "failure": null,
        "operation": "connect",
        "proto": "tcp",
        "t": 0.097723167
      },
      {
        "failure": null,
        "num_bytes": 291,
        "operation": "write",
        "t": 0.098003917
      },
      {
        "failure": null,
        "num_bytes": 337,
        "operation": "read",
        "t": 0.128046292
      },
      {
        "failure": null,
        "operation": "http_transaction_done",
        "t": 0.128262792
      },
      {
        "failure": null,
        "operation": "http_transaction_start",
        "t": 0.000366625
      },
      {
        "address": "149.154.175.100:80",
        "failure": null,
        "operation": "connect",
        "proto": "tcp",
        "t": 0.128092292
      },
      {
        "failure": null,
        "num_bytes": 292,
        "operation": "write",
        "t": 0.128347958
      },
      {
        "failure": null,
        "num_bytes": 324,
        "operation": "read",
        "t": 0.255231792
      },
      {
        "failure": null,
        "operation": "http_transaction_done",
        "t": 0.255456792
      },
      {
        "failure": "connection_already_closed",
        "operation": "read",
        "t": 0.255612
      },
      {
        "failure": null,
        "operation": "http_transaction_start",
        "t": 0.000363417
      },
      {
        "address": "149.154.175.50:80",
        "failure": null,
        "operation": "connect",
        "proto": "tcp",
        "t": 0.133035125
      },
      {
        "failure": null,
        "num_bytes": 291,
        "operation": "write",
        "t": 0.133178833
      },
      {
        "failure": null,
        "num_bytes": 324,
        "operation": "read",
        "t": 0.263978875
      },
      {
        "failure": null,
        "operation": "http_transaction_done",
        "t": 0.264080292
      },
      {
        "failure": "connection_already_closed",
        "operation": "read",
        "t": 0.264176042
      },
      {
        "failure": null,
        "operation": "http_transaction_start",
        "t": 0.2558325
      },
      {
        "address": "95.161.76.100:80",
        "failure": null,
        "operation": "connect",
        "proto": "tcp",
        "t": 0.288492667
      },
      {
        "failure": null,
        "num_bytes": 290,
        "operation": "write",
        "t": 0.288761583
      },
      {
        "failure": null,
        "num_bytes": 367,
        "operation": "read",
        "t": 0.324089958
      },
      {
        "failure": null,
        "operation": "http_transaction_done",
        "t": 0.324298208
      },
      {
        "failure": "connection_already_closed",
        "operation": "read",
        "t": 0.324408208
      },
      {
        "failure": null,
        "operation": "http_transaction_start",
        "t": 0.32451775
      },
      {
        "address": "149.154.167.51:443",
        "failure": null,
        "operation": "connect",
        "proto": "tcp",
        "t": 0.357794333
      },
      {
        "failure": null,
        "num_bytes": 295,
        "operation": "write",
        "t": 0.35806625
      },
      {
        "failure": null,
        "num_bytes": 324,
        "operation": "read",
        "t": 0.390229125
      },
      {
        "failure": null,
        "operation": "http_transaction_done",
        "t": 0.390327458
      },
      {
        "failure": "connection_already_closed",
        "operation": "read",
        "t": 0.390398958
      },
      {
        "failure": null,
        "operation": "http_transaction_start",
        "t": 0.128418792
      },
      {
        "address": "149.154.171.5:80",
        "failure": null,
        "operation": "connect",
        "proto": "tcp",
        "t": 0.288569375
      },
      {
        "failure": null,
        "num_bytes": 290,
        "operation": "write",
        "t": 0.288778292
      },
      {
        "failure": null,
        "num_bytes": 324,
        "operation": "read",
        "t": 0.449944667
      },
      {
        "failure": null,
        "operation": "http_transaction_done",
        "t": 0.45012375
      },
      {
        "failure": "connection_already_closed",
        "operation": "read",
        "t": 0.450319333
      },
      {
        "failure": null,
        "operation": "http_transaction_start",
        "t": 0.2642485
      },
      {
        "address": "149.154.175.50:443",
        "failure": null,
        "operation": "connect",
        "proto": "tcp",
        "t": 0.390228625
      },
      {
        "failure": null,
        "num_bytes": 295,
        "operation": "write",
        "t": 0.390414125
      },
      {
        "failure": null,
        "num_bytes": 324,
        "operation": "read",
        "t": 0.516954125
      },
      {
        "failure": null,
        "operation": "http_transaction_done",
        "t": 0.517173667
      },
      {
        "failure": "connection_already_closed",
        "operation": "read",
        "t": 0.51735175
      },
      {
        "failure": null,
        "operation": "http_transaction_start",
        "t": 0.450432167
      },
      {
        "address": "149.154.167.91:443",
        "failure": null,
        "operation": "connect",
        "proto": "tcp",
        "t": 0.483508667
      },
      {
        "failure": null,
        "num_bytes": 295,
        "operation": "write",
        "t": 0.483750875
      },
      {
        "failure": null,
        "num_bytes": 367,
        "operation": "read",
        "t": 0.519915208
      },
      {
        "failure": null,
        "operation": "http_transaction_done",
        "t": 0.520009792
      },
      {
        "failure": "connection_already_closed",
        "operation": "read",
        "t": 0.520082083
      },
      {
        "failure": null,
        "operation": "http_transaction_start",
        "t": 0.520151375
      },
      {
        "address": "95.161.76.100:443",
        "failure": null,
        "operation": "connect",
        "proto": "tcp",
        "t": 0.552242458
      },
      {
        "failure": null,
        "num_bytes": 294,
        "operation": "write",
        "t": 0.552504583
      },
      {
        "failure": null,
        "num_bytes": 324,
        "operation": "read",
        "t": 0.587025667
      },
      {
        "failure": null,
        "operation": "http_transaction_done",
        "t": 0.58719875
      },
      {
        "failure": "connection_already_closed",
        "operation": "read",
        "t": 0.587306833
      },
      {
        "failure": null,
        "operation": "http_transaction_start",
        "t": 0.390487375
      },
      {
        "address": "149.154.175.100:443",
        "failure": null,
        "operation": "connect",
        "proto": "tcp",
        "t": 0.522328292
      },
      {
        "failure": null,
        "num_bytes": 296,
        "operation": "write",
        "t": 0.522468375
      },
      {
        "failure": null,
        "num_bytes": 324,
        "operation": "read",
        "t": 0.653976958
      },
      {
        "failure": null,
        "operation": "http_transaction_done",
        "t": 0.654157167
      },
      {
        "failure": "connection_already_closed",
        "operation": "read",
        "t": 0.654261208
      },
      {
        "failure": null,
        "operation": "http_transaction_start",
        "t": 0.587507833
      },
      {
        "failure": null,
        "operation": "resolve_start",
        "t": 0.58769825
      },
      {
        "failure": null,
        "operation": "resolve_done",
        "t": 0.605714375
      },
      {
        "address": "149.154.167.99:443",
        "failure": null,
        "operation": "connect",
        "proto": "tcp",
        "t": 0.639481417
      },
      {
        "failure": null,
        "operation": "tls_handshake_start",
        "t": 0.639499292
      },
      {
        "failure": null,
        "num_bytes": 282,
        "operation": "write",
        "t": 0.6406325
      },
      {
        "failure": null,
        "num_bytes": 517,
        "operation": "read",
        "t": 0.672845917
      },
      {
        "failure": null,
        "num_bytes": 3167,
        "operation": "read",
        "t": 0.673358583
      },
      {
        "failure": null,
        "num_bytes": 2012,
        "operation": "read",
        "t": 0.673643875
      },
      {
        "failure": null,
        "num_bytes": 80,
        "operation": "write",
        "t": 0.674915458
      },
      {
        "failure": null,
        "operation": "tls_handshake_done",
        "t": 0.674971042
      },
      {
        "failure": null,
        "num_bytes": 86,
        "operation": "write",
        "t": 0.675093208
      },
      {
        "failure": null,
        "num_bytes": 198,
        "operation": "write",
        "t": 0.675250458
      },
      {
        "failure": null,
        "num_bytes": 2534,
        "operation": "read",
        "t": 0.708365542
      },
      {
        "failure": null,
        "num_bytes": 31,
        "operation": "write",
        "t": 0.708437583
      },
      {
        "failure": null,
        "operation": "http_transaction_done",
        "t": 0.708596583
      },
      {
        "failure": null,
        "num_bytes": 24,
        "operation": "write",
        "t": 0.708685625
      },
      {
        "failure": "connection_already_closed",
        "operation": "read",
        "t": 0.708748
      },
      {
        "failure": null,
        "operation": "http_transaction_start",
        "t": 0.517482083
      },
      {
        "address": "149.154.171.5:443",
        "failure": null,
        "operation": "connect",
        "proto": "tcp",
        "t": 0.676968083
      },
      {
        "failure": null,
        "num_bytes": 294,
        "operation": "write",
        "t": 0.677103875
      },
      {
        "failure": null,
        "num_bytes": 337,
        "operation": "read",
        "t": 0.837133958
      },
      {
        "failure": null,
        "operation": "http_transaction_done",
        "t": 0.837388667
      }
    ],
    "queries": [
      {
        "answers": [
          {
            "asn": 62041,
            "as_org_name": "Telegram Messenger Inc",
            "answer_type": "A",
            "ipv4": "149.154.167.99",
            "ttl": null
          }
        ],
        "engine": "system",
        "failure": null,
        "hostname": "web.telegram.org",
        "query_type": "A",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "",
        "t": 0.605714375
      },
      {
        "answers": [
          {
            "asn": 62041,
            "as_org_name": "Telegram Messenger Inc",
            "answer_type": "AAAA",
            "ipv6": "2001:67c:4e8:f004::9",
            "ttl": null
          }
        ],
        "engine": "system",
        "failure": null,
        "hostname": "web.telegram.org",
        "query_type": "AAAA",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "",
        "t": 0.605714375
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
              "149.154.167.51"
            ],
            [
              "User-Agent",
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
            ]
          ],
          "headers": {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
            "Host": "149.154.167.51",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
          },
          "method": "POST",
          "tor": {
            "exit_ip": null,
            "exit_name": null,
            "is_tor": false
          },
          "x_transport": "tcp",
          "url": "http://149.154.167.51/"
        },
        "response": {
          "body": "<html>\r\n<head><title>404 Not Found</title></head>\r\n<body bgcolor=\"white\">\r\n<center><h1>404 Not Found</h1></center>\r\n<hr><center>nginx/0.3.33</center>\r\n</body>\r\n</html>\r\n",
          "body_is_truncated": false,
          "code": 404,
          "headers_list": [
            [
              "Connection",
              "keep-alive"
            ],
            [
              "Content-Length",
              "169"
            ],
            [
              "Content-Type",
              "text/html"
            ],
            [
              "Date",
              "Wed, 07 Dec 2022 10:51:54 GMT"
            ],
            [
              "Server",
              "nginx/0.3.33"
            ]
          ],
          "headers": {
            "Connection": "keep-alive",
            "Content-Length": "169",
            "Content-Type": "text/html",
            "Date": "Wed, 07 Dec 2022 10:51:54 GMT",
            "Server": "nginx/0.3.33"
          }
        },
        "t": 0.065531792
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
              "149.154.167.91"
            ],
            [
              "User-Agent",
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
            ]
          ],
          "headers": {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
            "Host": "149.154.167.91",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
          },
          "method": "POST",
          "tor": {
            "exit_ip": null,
            "exit_name": null,
            "is_tor": false
          },
          "x_transport": "tcp",
          "url": "http://149.154.167.91/"
        },
        "response": {
          "body": "<html>\r\n<head><title>501 Not Implemented</title></head>\r\n<body bgcolor=\"white\">\r\n<center><h1>501 Not Implemented</h1></center>\r\n<hr><center>nginx/0.3.33</center>\r\n</body>\r\n</html>\r\n",
          "body_is_truncated": false,
          "code": 501,
          "headers_list": [
            [
              "Content-Length",
              "181"
            ],
            [
              "Content-Type",
              "text/html"
            ],
            [
              "Date",
              "Wed, 07 Dec 2022 10:51:54 GMT"
            ],
            [
              "Server",
              "nginx/0.3.33"
            ]
          ],
          "headers": {
            "Content-Length": "181",
            "Content-Type": "text/html",
            "Date": "Wed, 07 Dec 2022 10:51:54 GMT",
            "Server": "nginx/0.3.33"
          }
        },
        "t": 0.128262792
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
              "149.154.175.100"
            ],
            [
              "User-Agent",
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
            ]
          ],
          "headers": {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
            "Host": "149.154.175.100",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
          },
          "method": "POST",
          "tor": {
            "exit_ip": null,
            "exit_name": null,
            "is_tor": false
          },
          "x_transport": "tcp",
          "url": "http://149.154.175.100/"
        },
        "response": {
          "body": "<html>\r\n<head><title>404 Not Found</title></head>\r\n<body bgcolor=\"white\">\r\n<center><h1>404 Not Found</h1></center>\r\n<hr><center>nginx/0.3.33</center>\r\n</body>\r\n</html>\r\n",
          "body_is_truncated": false,
          "code": 404,
          "headers_list": [
            [
              "Connection",
              "keep-alive"
            ],
            [
              "Content-Length",
              "169"
            ],
            [
              "Content-Type",
              "text/html"
            ],
            [
              "Date",
              "Wed, 07 Dec 2022 10:51:54 GMT"
            ],
            [
              "Server",
              "nginx/0.3.33"
            ]
          ],
          "headers": {
            "Connection": "keep-alive",
            "Content-Length": "169",
            "Content-Type": "text/html",
            "Date": "Wed, 07 Dec 2022 10:51:54 GMT",
            "Server": "nginx/0.3.33"
          }
        },
        "t": 0.255456792
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
              "149.154.175.50"
            ],
            [
              "User-Agent",
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
            ]
          ],
          "headers": {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
            "Host": "149.154.175.50",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
          },
          "method": "POST",
          "tor": {
            "exit_ip": null,
            "exit_name": null,
            "is_tor": false
          },
          "x_transport": "tcp",
          "url": "http://149.154.175.50/"
        },
        "response": {
          "body": "<html>\r\n<head><title>404 Not Found</title></head>\r\n<body bgcolor=\"white\">\r\n<center><h1>404 Not Found</h1></center>\r\n<hr><center>nginx/0.3.33</center>\r\n</body>\r\n</html>\r\n",
          "body_is_truncated": false,
          "code": 404,
          "headers_list": [
            [
              "Connection",
              "keep-alive"
            ],
            [
              "Content-Length",
              "169"
            ],
            [
              "Content-Type",
              "text/html"
            ],
            [
              "Date",
              "Wed, 07 Dec 2022 10:51:54 GMT"
            ],
            [
              "Server",
              "nginx/0.3.33"
            ]
          ],
          "headers": {
            "Connection": "keep-alive",
            "Content-Length": "169",
            "Content-Type": "text/html",
            "Date": "Wed, 07 Dec 2022 10:51:54 GMT",
            "Server": "nginx/0.3.33"
          }
        },
        "t": 0.264080292
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
              "95.161.76.100"
            ],
            [
              "User-Agent",
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
            ]
          ],
          "headers": {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
            "Host": "95.161.76.100",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
          },
          "method": "POST",
          "tor": {
            "exit_ip": null,
            "exit_name": null,
            "is_tor": false
          },
          "x_transport": "tcp",
          "url": "http://95.161.76.100/"
        },
        "response": {
          "body": "<html>\r\n<head><title>404 Not Found</title></head>\r\n<body bgcolor=\"white\">\r\n<center><h1>404 Not Found</h1></center>\r\n<hr><center>nginx/0.3.33</center>\r\n</body>\r\n</html>\r\n",
          "body_is_truncated": false,
          "code": 404,
          "headers_list": [
            [
              "Cache-Control",
              "no-store"
            ],
            [
              "Connection",
              "keep-alive"
            ],
            [
              "Content-Length",
              "169"
            ],
            [
              "Content-Type",
              "text/html"
            ],
            [
              "Date",
              "Wed, 07 Dec 2022 10:51:54 GMT"
            ],
            [
              "Pragma",
              "no-cache"
            ],
            [
              "Server",
              "nginx/0.3.33"
            ]
          ],
          "headers": {
            "Cache-Control": "no-store",
            "Connection": "keep-alive",
            "Content-Length": "169",
            "Content-Type": "text/html",
            "Date": "Wed, 07 Dec 2022 10:51:54 GMT",
            "Pragma": "no-cache",
            "Server": "nginx/0.3.33"
          }
        },
        "t": 0.324298208
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
              "149.154.167.51:443"
            ],
            [
              "User-Agent",
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
            ]
          ],
          "headers": {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
            "Host": "149.154.167.51:443",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
          },
          "method": "POST",
          "tor": {
            "exit_ip": null,
            "exit_name": null,
            "is_tor": false
          },
          "x_transport": "tcp",
          "url": "http://149.154.167.51:443/"
        },
        "response": {
          "body": "<html>\r\n<head><title>404 Not Found</title></head>\r\n<body bgcolor=\"white\">\r\n<center><h1>404 Not Found</h1></center>\r\n<hr><center>nginx/0.3.33</center>\r\n</body>\r\n</html>\r\n",
          "body_is_truncated": false,
          "code": 404,
          "headers_list": [
            [
              "Connection",
              "keep-alive"
            ],
            [
              "Content-Length",
              "169"
            ],
            [
              "Content-Type",
              "text/html"
            ],
            [
              "Date",
              "Wed, 07 Dec 2022 10:51:54 GMT"
            ],
            [
              "Server",
              "nginx/0.3.33"
            ]
          ],
          "headers": {
            "Connection": "keep-alive",
            "Content-Length": "169",
            "Content-Type": "text/html",
            "Date": "Wed, 07 Dec 2022 10:51:54 GMT",
            "Server": "nginx/0.3.33"
          }
        },
        "t": 0.390327458
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
              "149.154.171.5"
            ],
            [
              "User-Agent",
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
            ]
          ],
          "headers": {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
            "Host": "149.154.171.5",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
          },
          "method": "POST",
          "tor": {
            "exit_ip": null,
            "exit_name": null,
            "is_tor": false
          },
          "x_transport": "tcp",
          "url": "http://149.154.171.5/"
        },
        "response": {
          "body": "<html>\r\n<head><title>404 Not Found</title></head>\r\n<body bgcolor=\"white\">\r\n<center><h1>404 Not Found</h1></center>\r\n<hr><center>nginx/0.3.33</center>\r\n</body>\r\n</html>\r\n",
          "body_is_truncated": false,
          "code": 404,
          "headers_list": [
            [
              "Connection",
              "keep-alive"
            ],
            [
              "Content-Length",
              "169"
            ],
            [
              "Content-Type",
              "text/html"
            ],
            [
              "Date",
              "Wed, 07 Dec 2022 10:51:54 GMT"
            ],
            [
              "Server",
              "nginx/0.3.33"
            ]
          ],
          "headers": {
            "Connection": "keep-alive",
            "Content-Length": "169",
            "Content-Type": "text/html",
            "Date": "Wed, 07 Dec 2022 10:51:54 GMT",
            "Server": "nginx/0.3.33"
          }
        },
        "t": 0.45012375
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
              "149.154.175.50:443"
            ],
            [
              "User-Agent",
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
            ]
          ],
          "headers": {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
            "Host": "149.154.175.50:443",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
          },
          "method": "POST",
          "tor": {
            "exit_ip": null,
            "exit_name": null,
            "is_tor": false
          },
          "x_transport": "tcp",
          "url": "http://149.154.175.50:443/"
        },
        "response": {
          "body": "<html>\r\n<head><title>404 Not Found</title></head>\r\n<body bgcolor=\"white\">\r\n<center><h1>404 Not Found</h1></center>\r\n<hr><center>nginx/0.3.33</center>\r\n</body>\r\n</html>\r\n",
          "body_is_truncated": false,
          "code": 404,
          "headers_list": [
            [
              "Connection",
              "keep-alive"
            ],
            [
              "Content-Length",
              "169"
            ],
            [
              "Content-Type",
              "text/html"
            ],
            [
              "Date",
              "Wed, 07 Dec 2022 10:51:54 GMT"
            ],
            [
              "Server",
              "nginx/0.3.33"
            ]
          ],
          "headers": {
            "Connection": "keep-alive",
            "Content-Length": "169",
            "Content-Type": "text/html",
            "Date": "Wed, 07 Dec 2022 10:51:54 GMT",
            "Server": "nginx/0.3.33"
          }
        },
        "t": 0.517173667
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
              "149.154.167.91:443"
            ],
            [
              "User-Agent",
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
            ]
          ],
          "headers": {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
            "Host": "149.154.167.91:443",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
          },
          "method": "POST",
          "tor": {
            "exit_ip": null,
            "exit_name": null,
            "is_tor": false
          },
          "x_transport": "tcp",
          "url": "http://149.154.167.91:443/"
        },
        "response": {
          "body": "<html>\r\n<head><title>404 Not Found</title></head>\r\n<body bgcolor=\"white\">\r\n<center><h1>404 Not Found</h1></center>\r\n<hr><center>nginx/0.3.33</center>\r\n</body>\r\n</html>\r\n",
          "body_is_truncated": false,
          "code": 404,
          "headers_list": [
            [
              "Cache-Control",
              "no-store"
            ],
            [
              "Connection",
              "keep-alive"
            ],
            [
              "Content-Length",
              "169"
            ],
            [
              "Content-Type",
              "text/html"
            ],
            [
              "Date",
              "Wed, 07 Dec 2022 10:51:54 GMT"
            ],
            [
              "Pragma",
              "no-cache"
            ],
            [
              "Server",
              "nginx/0.3.33"
            ]
          ],
          "headers": {
            "Cache-Control": "no-store",
            "Connection": "keep-alive",
            "Content-Length": "169",
            "Content-Type": "text/html",
            "Date": "Wed, 07 Dec 2022 10:51:54 GMT",
            "Pragma": "no-cache",
            "Server": "nginx/0.3.33"
          }
        },
        "t": 0.520009792
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
              "95.161.76.100:443"
            ],
            [
              "User-Agent",
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
            ]
          ],
          "headers": {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
            "Host": "95.161.76.100:443",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
          },
          "method": "POST",
          "tor": {
            "exit_ip": null,
            "exit_name": null,
            "is_tor": false
          },
          "x_transport": "tcp",
          "url": "http://95.161.76.100:443/"
        },
        "response": {
          "body": "<html>\r\n<head><title>404 Not Found</title></head>\r\n<body bgcolor=\"white\">\r\n<center><h1>404 Not Found</h1></center>\r\n<hr><center>nginx/0.3.33</center>\r\n</body>\r\n</html>\r\n",
          "body_is_truncated": false,
          "code": 404,
          "headers_list": [
            [
              "Connection",
              "keep-alive"
            ],
            [
              "Content-Length",
              "169"
            ],
            [
              "Content-Type",
              "text/html"
            ],
            [
              "Date",
              "Wed, 07 Dec 2022 10:51:55 GMT"
            ],
            [
              "Server",
              "nginx/0.3.33"
            ]
          ],
          "headers": {
            "Connection": "keep-alive",
            "Content-Length": "169",
            "Content-Type": "text/html",
            "Date": "Wed, 07 Dec 2022 10:51:55 GMT",
            "Server": "nginx/0.3.33"
          }
        },
        "t": 0.58719875
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
              "149.154.175.100:443"
            ],
            [
              "User-Agent",
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
            ]
          ],
          "headers": {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
            "Host": "149.154.175.100:443",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
          },
          "method": "POST",
          "tor": {
            "exit_ip": null,
            "exit_name": null,
            "is_tor": false
          },
          "x_transport": "tcp",
          "url": "http://149.154.175.100:443/"
        },
        "response": {
          "body": "<html>\r\n<head><title>404 Not Found</title></head>\r\n<body bgcolor=\"white\">\r\n<center><h1>404 Not Found</h1></center>\r\n<hr><center>nginx/0.3.33</center>\r\n</body>\r\n</html>\r\n",
          "body_is_truncated": false,
          "code": 404,
          "headers_list": [
            [
              "Connection",
              "keep-alive"
            ],
            [
              "Content-Length",
              "169"
            ],
            [
              "Content-Type",
              "text/html"
            ],
            [
              "Date",
              "Wed, 07 Dec 2022 10:51:55 GMT"
            ],
            [
              "Server",
              "nginx/0.3.33"
            ]
          ],
          "headers": {
            "Connection": "keep-alive",
            "Content-Length": "169",
            "Content-Type": "text/html",
            "Date": "Wed, 07 Dec 2022 10:51:55 GMT",
            "Server": "nginx/0.3.33"
          }
        },
        "t": 0.654157167
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
              "web.telegram.org"
            ],
            [
              "User-Agent",
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
            ]
          ],
          "headers": {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
            "Host": "web.telegram.org",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
          },
          "method": "GET",
          "tor": {
            "exit_ip": null,
            "exit_name": null,
            "is_tor": false
          },
          "x_transport": "tcp",
          "url": "https://web.telegram.org/"
        },
        "response": {
          "body": "<!doctype html><html lang=en manifest=webogram.appcache ng-csp xmlns:ng=http://angularjs.org id=ng-app style=\"display: none;\"><head><meta charset=utf-8><meta name=viewport content=\"width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no\"><title>Telegram Web</title><link rel=stylesheet href=css/app.css><link rel=manifest href=manifest.webapp.json><link rel=icon href=favicon.ico type=image/x-icon><link rel=apple-touch-icon href=img/iphone_home120.png><link rel=apple-touch-icon sizes=120x120 href=img/iphone_home120.png><link rel=apple-touch-startup-image media=\"(device-width: 320px)\" href=img/iphone_startup.png><meta name=apple-mobile-web-app-title content=\"Telegram Web\"><meta name=mobile-web-app-capable content=yes><meta name=apple-mobile-web-app-capable content=yes><meta name=apple-mobile-web-app-status-bar-style content=black-translucent><meta name=theme-color content=#497495><meta name=google content=notranslate><meta property=og:title content=\"Telegram Web\"><meta property=og:url content=\"https://web.telegram.org/\"><meta property=og:image:width content=236><meta property=og:image:height content=236><meta property=og:image content=https://web.telegram.org/img/logo_share.png><meta property=og:site_name content=\"Telegram Web\"><meta property=description content=\"Welcome to the Web application of Telegram messenger. See https://github.com/zhukov/webogram for more info.\"><meta property=og:description content=\"Welcome to the Web application of Telegram messenger. See https://github.com/zhukov/webogram for more info.\"></head><body><div class=page_wrap ng-view></div><div id=notify_sound></div><script src=js/app.js></script></body></html>",
          "body_is_truncated": false,
          "code": 200,
          "headers_list": [
            [
              "Accept-Ranges",
              "bytes"
            ],
            [
              "Cache-Control",
              "max-age=3600"
            ],
            [
              "Content-Length",
              "1672"
            ],
            [
              "Content-Type",
              "text/html"
            ],
            [
              "Date",
              "Wed, 07 Dec 2022 10:51:55 GMT"
            ],
            [
              "Etag",
              "\"5fdcb452-688\""
            ],
            [
              "Expires",
              "Wed, 07 Dec 2022 11:51:55 GMT"
            ],
            [
              "Last-Modified",
              "Fri, 18 Dec 2020 13:53:22 GMT"
            ],
            [
              "Server",
              "nginx/1.18.0"
            ],
            [
              "X-Frame-Options",
              "deny"
            ]
          ],
          "headers": {
            "Accept-Ranges": "bytes",
            "Cache-Control": "max-age=3600",
            "Content-Length": "1672",
            "Content-Type": "text/html",
            "Date": "Wed, 07 Dec 2022 10:51:55 GMT",
            "Etag": "\"5fdcb452-688\"",
            "Expires": "Wed, 07 Dec 2022 11:51:55 GMT",
            "Last-Modified": "Fri, 18 Dec 2020 13:53:22 GMT",
            "Server": "nginx/1.18.0",
            "X-Frame-Options": "deny"
          }
        },
        "t": 0.708596583
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
              "149.154.171.5:443"
            ],
            [
              "User-Agent",
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
            ]
          ],
          "headers": {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
            "Host": "149.154.171.5:443",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
          },
          "method": "POST",
          "tor": {
            "exit_ip": null,
            "exit_name": null,
            "is_tor": false
          },
          "x_transport": "tcp",
          "url": "http://149.154.171.5:443/"
        },
        "response": {
          "body": "<html>\r\n<head><title>501 Not Implemented</title></head>\r\n<body bgcolor=\"white\">\r\n<center><h1>501 Not Implemented</h1></center>\r\n<hr><center>nginx/0.3.33</center>\r\n</body>\r\n</html>\r\n",
          "body_is_truncated": false,
          "code": 501,
          "headers_list": [
            [
              "Content-Length",
              "181"
            ],
            [
              "Content-Type",
              "text/html"
            ],
            [
              "Date",
              "Wed, 07 Dec 2022 10:51:55 GMT"
            ],
            [
              "Server",
              "nginx/0.3.33"
            ]
          ],
          "headers": {
            "Content-Length": "181",
            "Content-Type": "text/html",
            "Date": "Wed, 07 Dec 2022 10:51:55 GMT",
            "Server": "nginx/0.3.33"
          }
        },
        "t": 0.837388667
      }
    ],
    "tcp_connect": [
      {
        "ip": "149.154.167.51",
        "port": 80,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.032989958
      },
      {
        "ip": "149.154.167.91",
        "port": 80,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.097723167
      },
      {
        "ip": "149.154.175.100",
        "port": 80,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.128092292
      },
      {
        "ip": "149.154.175.50",
        "port": 80,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.133035125
      },
      {
        "ip": "95.161.76.100",
        "port": 80,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.288492667
      },
      {
        "ip": "149.154.167.51",
        "port": 443,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.357794333
      },
      {
        "ip": "149.154.171.5",
        "port": 80,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.288569375
      },
      {
        "ip": "149.154.175.50",
        "port": 443,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.390228625
      },
      {
        "ip": "149.154.167.91",
        "port": 443,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.483508667
      },
      {
        "ip": "95.161.76.100",
        "port": 443,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.552242458
      },
      {
        "ip": "149.154.175.100",
        "port": 443,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.522328292
      },
      {
        "ip": "149.154.167.99",
        "port": 443,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.639481417
      },
      {
        "ip": "149.154.171.5",
        "port": 443,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.676968083
      }
    ],
    "tls_handshakes": [
      {
        "network": "",
        "address": "149.154.167.99:443",
        "cipher_suite": "TLS_AES_256_GCM_SHA384",
        "failure": null,
        "negotiated_protocol": "h2",
        "no_tls_verify": false,
        "peer_certificates": [
          {
            "data": "MIIGmzCCBYOgAwIBAgIJAKgeOknmnMZLMA0GCSqGSIb3DQEBCwUAMIG0MQswCQYDVQQGEwJVUzEQMA4GA1UECBMHQXJpem9uYTETMBEGA1UEBxMKU2NvdHRzZGFsZTEaMBgGA1UEChMRR29EYWRkeS5jb20sIEluYy4xLTArBgNVBAsTJGh0dHA6Ly9jZXJ0cy5nb2RhZGR5LmNvbS9yZXBvc2l0b3J5LzEzMDEGA1UEAxMqR28gRGFkZHkgU2VjdXJlIENlcnRpZmljYXRlIEF1dGhvcml0eSAtIEcyMB4XDTIyMDgyOTAwMzkzNFoXDTIzMDkzMDAwMzkzNFowHTEbMBkGA1UEAwwSKi53ZWIudGVsZWdyYW0ub3JnMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA1wRkux0GOYCXvEKeQDgPgdKgfXvXr8omUUj9uJh0+cOd8sfeVyBaxXfhZNAAWqJnOrkYPTxEvkHPQa7jS/aVd3MrUDMSRNGG6LuYWOGjGI700TBrPY5f64ApVwHMznP6r27z6wktyW5HzoEu/tU+XjeLneMvXT9kO3edX5v92dBLn7qRlkijHTol08prkr9hW1WO0atj5WmdyCuEaPbPmu08Gf29ygE1l1s3yJBjPdFccUB/qR67kWknTolnjU+QH8Hm4BRQsu1s7eRmDiuJNM2Aztp1/n5rOGHnspzMB9YAppb0aDiUljT+rH8IASQnRZKATiX66eEkY8b5+Od5KwIDAQABo4IDRDCCA0AwDAYDVR0TAQH/BAIwADAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwDgYDVR0PAQH/BAQDAgWgMDgGA1UdHwQxMC8wLaAroCmGJ2h0dHA6Ly9jcmwuZ29kYWRkeS5jb20vZ2RpZzJzMS00NDE4LmNybDBdBgNVHSAEVjBUMEgGC2CGSAGG/W0BBxcBMDkwNwYIKwYBBQUHAgEWK2h0dHA6Ly9jZXJ0aWZpY2F0ZXMuZ29kYWRkeS5jb20vcmVwb3NpdG9yeS8wCAYGZ4EMAQIBMHYGCCsGAQUFBwEBBGowaDAkBggrBgEFBQcwAYYYaHR0cDovL29jc3AuZ29kYWRkeS5jb20vMEAGCCsGAQUFBzAChjRodHRwOi8vY2VydGlmaWNhdGVzLmdvZGFkZHkuY29tL3JlcG9zaXRvcnkvZ2RpZzIuY3J0MB8GA1UdIwQYMBaAFEDCvSeOzDSDMKIz1/tss/C0LIDOMC8GA1UdEQQoMCaCEioud2ViLnRlbGVncmFtLm9yZ4IQd2ViLnRlbGVncmFtLm9yZzAdBgNVHQ4EFgQUR4ePZ7oUGAyMUSZM6BlIsW0jx5kwggF9BgorBgEEAdZ5AgQCBIIBbQSCAWkBZwB3AOg+0No+9QY1MudXKLyJa8kD08vREWvs62nhd31tBr1uAAABgucKGZUAAAQDAEgwRgIhAJ3lLLSdKsNtZAzzUpXh2u5dO4sz4Br19oeL6q6gaAkdAiEA0s0T0beLOBxwfBqIU1WQw+xAAX6YlLUX+iVgdNJHiHUAdQA1zxkbv7FsV78PrUxtQsu7ticgJlHqP+Eq76gDwzvWTAAAAYLnChrBAAAEAwBGMEQCIBsedQTSIPrKMe2GqDrSWNjb/ciKfqdAqLPzGEdKvf1OAiBnEJrMaeTLQqxHQfHmtl6o6P7G8E/GD+jwT7FuxNABgAB1AHoyjFTYty22IOo44FIe6YQWcDIThU070ivBOlejUutSAAABgucKG4MAAAQDAEYwRAIgfFvJYommOgz4mOLVCQrQwFqAYEIjrQmMkRwAJbbPHLUCIDHtqNXAmmNJlQL4Bc5pFOMH2HeQtjWOT/c1zIlgtY0NMA0GCSqGSIb3DQEBCwUAA4IBAQA2eUth3t2YKQwDp1M0pdqIiR7hWu3H+4Yv5hsvOnrGBoz8VNqt1AIUBd7GdOLPKPiMsTSTZL7fQU+YxMvIg+GD15sbHQ+KuaqQP2wBua+zfZ8EthuZ32Dwaq/m0fLAp+WVScDYG/x8QVC2DClD2UwKV7L6J7ReyR72IsXI6fEMFYnlMQTHK9DOA77f7+Q652Scd9yERTtY2SgTnTuBc1AthRQnmGv316WvI7Rv/MTxX3fNtwkfdGXOpPKP25cZ9nmlz4REOCZMoEoXYl6i9yzRyfRWR/hPMb1DDoT+QZz98GeIiUqdgsXEXFeMHnakFfnKuT34U2kxl7ZJdfA2Ryi6",
            "format": "base64"
          },
          {
            "data": "MIIE0DCCA7igAwIBAgIBBzANBgkqhkiG9w0BAQsFADCBgzELMAkGA1UEBhMCVVMxEDAOBgNVBAgTB0FyaXpvbmExEzARBgNVBAcTClNjb3R0c2RhbGUxGjAYBgNVBAoTEUdvRGFkZHkuY29tLCBJbmMuMTEwLwYDVQQDEyhHbyBEYWRkeSBSb290IENlcnRpZmljYXRlIEF1dGhvcml0eSAtIEcyMB4XDTExMDUwMzA3MDAwMFoXDTMxMDUwMzA3MDAwMFowgbQxCzAJBgNVBAYTAlVTMRAwDgYDVQQIEwdBcml6b25hMRMwEQYDVQQHEwpTY290dHNkYWxlMRowGAYDVQQKExFHb0RhZGR5LmNvbSwgSW5jLjEtMCsGA1UECxMkaHR0cDovL2NlcnRzLmdvZGFkZHkuY29tL3JlcG9zaXRvcnkvMTMwMQYDVQQDEypHbyBEYWRkeSBTZWN1cmUgQ2VydGlmaWNhdGUgQXV0aG9yaXR5IC0gRzIwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQC54MsQ1K92vdSTYuswZLiBCGzDBNliF44v/z5lz4/OYuY8UhzaFkVLVat4a2ODYpDOD2lsmcgaFItMzEUz6ojcnqOvK/6AYZ15V8TPLvQ/MDxdR/yaFrzDN5ZBUY4RS1T4KL7QjL7wMDge87Am+GZHY23ecSZHjzhHU9FGHbTj3ADqRay9vHHZqm8A29vNMDp5T19MR/gd71vCxJ1gO7GyQ5HYpDNO6rPWJ0+tJYqlxvTV0KaudAVkV4i1RFXULSo6Pvi4vekyCgKUZMQWOlDxSq7neTOvDCAHf+jfBDnCaQJsY1L6d8EbyHSHyLmTGFBUNUtpTrw700kuH9zB0lL7AgMBAAGjggEaMIIBFjAPBgNVHRMBAf8EBTADAQH/MA4GA1UdDwEB/wQEAwIBBjAdBgNVHQ4EFgQUQMK9J47MNIMwojPX+2yz8LQsgM4wHwYDVR0jBBgwFoAUOpqFBxBnKLbv9r0FQW4gwZTaD94wNAYIKwYBBQUHAQEEKDAmMCQGCCsGAQUFBzABhhhodHRwOi8vb2NzcC5nb2RhZGR5LmNvbS8wNQYDVR0fBC4wLDAqoCigJoYkaHR0cDovL2NybC5nb2RhZGR5LmNvbS9nZHJvb3QtZzIuY3JsMEYGA1UdIAQ/MD0wOwYEVR0gADAzMDEGCCsGAQUFBwIBFiVodHRwczovL2NlcnRzLmdvZGFkZHkuY29tL3JlcG9zaXRvcnkvMA0GCSqGSIb3DQEBCwUAA4IBAQAIfmyTEMg4uJapkEv/oV9PBO9sPpyIBslQj6Zz91cxG7685C/b+LrTW+C05+Z5Yg4MotdqY3MxtfWoSKQ7CC2iXZDXtHwlTxFWMMS2RJ17LJ3lXubvDGGqv+QqG+6EnriDfcFDzkSnE3ANkR/0yBOtg2DZ2HKocyQetawiDsoXiWJYRBuriSUBAA/NxBti21G00w9RKpv0vHP8ds42pM3Z2Czqrpv1KrKQ0U11GIo/ikGQI31bS/6kA1ibRrLDYGCD+H1QQc7CoZDDu+8CL9IVVO5EFdkKrqeKM+2xLXY2JtwE65/3YR8V3Idv7kaWKK2hJn0KCacuBKONvPi8BDAB",
            "format": "base64"
          },
          {
            "data": "MIIEfTCCA2WgAwIBAgIDG+cVMA0GCSqGSIb3DQEBCwUAMGMxCzAJBgNVBAYTAlVTMSEwHwYDVQQKExhUaGUgR28gRGFkZHkgR3JvdXAsIEluYy4xMTAvBgNVBAsTKEdvIERhZGR5IENsYXNzIDIgQ2VydGlmaWNhdGlvbiBBdXRob3JpdHkwHhcNMTQwMTAxMDcwMDAwWhcNMzEwNTMwMDcwMDAwWjCBgzELMAkGA1UEBhMCVVMxEDAOBgNVBAgTB0FyaXpvbmExEzARBgNVBAcTClNjb3R0c2RhbGUxGjAYBgNVBAoTEUdvRGFkZHkuY29tLCBJbmMuMTEwLwYDVQQDEyhHbyBEYWRkeSBSb290IENlcnRpZmljYXRlIEF1dGhvcml0eSAtIEcyMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAv3FiCPH6WTT3G8kYo/eASVjpIoMTpsUgQwE7hPHmhUmfJ+r2hBtOoLTbcJjHMgGxBT4HTu70+k8vWTAi56sZVmvigAf88xZ1gDlRe+X5NbZ0TqmNghPktj+pA4P6or6KFWp/3gvDthkUBcrqw6gElDtGfDIN8wBmIsiNaW02jBEYt9OyHGC0OPoCjM7T3UYH3go+6118yHz7sCtTpJJiaVElBWEaRIGMLKlDliPfrDqBmg4pxRyp6V0etp6eMAo5zvGIgPtLXcwy7IViQyU0AlYnAZG0O3AqP26x6JyIAX2f1PnbU21gnb8s51iruF9G/M7EGwM8CetJMVxpRrPgRwIDAQABo4IBFzCCARMwDwYDVR0TAQH/BAUwAwEB/zAOBgNVHQ8BAf8EBAMCAQYwHQYDVR0OBBYEFDqahQcQZyi27/a9BUFuIMGU2g/eMB8GA1UdIwQYMBaAFNLEsNKR1EwRcbNhyz2h/t2oatTjMDQGCCsGAQUFBwEBBCgwJjAkBggrBgEFBQcwAYYYaHR0cDovL29jc3AuZ29kYWRkeS5jb20vMDIGA1UdHwQrMCkwJ6AloCOGIWh0dHA6Ly9jcmwuZ29kYWRkeS5jb20vZ2Ryb290LmNybDBGBgNVHSAEPzA9MDsGBFUdIAAwMzAxBggrBgEFBQcCARYlaHR0cHM6Ly9jZXJ0cy5nb2RhZGR5LmNvbS9yZXBvc2l0b3J5LzANBgkqhkiG9w0BAQsFAAOCAQEAWQtTvZKGEacke+1bMc8dH2xwxbhuvk679r6XUOEwf7ooXGKUwuN+M/f7QnaF25UcjCJYdQkMiGVnOQoWCcWgOJekxSOTP7QYpgEGRJHjp2kntFolfzq3Ms3dhP8qOCkzpN1nsoX+oYggHFCJyNwq9kIDN0zmiN/VryTyscPfzLXs4Jlet0lUIDyUGAzHHFIYSaRt4bNYC8nY7NmuHDKOKHAN4v6mF56ED71XcLNa6R+ghlO773z/aQvgSMO3kwvIClTErF0UZzdsyqUvMQg3qm5vjLyb4lddJIGvl5echK1srDdMZvNhkREg5L4wn3qkKQmw4TRfZHcYQFHfjDCmrw==",
            "format": "base64"
          },
          {
            "data": "MIIEADCCAuigAwIBAgIBADANBgkqhkiG9w0BAQUFADBjMQswCQYDVQQGEwJVUzEhMB8GA1UEChMYVGhlIEdvIERhZGR5IEdyb3VwLCBJbmMuMTEwLwYDVQQLEyhHbyBEYWRkeSBDbGFzcyAyIENlcnRpZmljYXRpb24gQXV0aG9yaXR5MB4XDTA0MDYyOTE3MDYyMFoXDTM0MDYyOTE3MDYyMFowYzELMAkGA1UEBhMCVVMxITAfBgNVBAoTGFRoZSBHbyBEYWRkeSBHcm91cCwgSW5jLjExMC8GA1UECxMoR28gRGFkZHkgQ2xhc3MgMiBDZXJ0aWZpY2F0aW9uIEF1dGhvcml0eTCCASAwDQYJKoZIhvcNAQEBBQADggENADCCAQgCggEBAN6d1+pXGEmhW+vXX0iG6r7d/+TvZxz0ZWizV3GgXne77ZtJ6XCAPVYYYwhv2vLM0D9/AlQiVBDYsoHUwHU9S3/Hd8M+eKsaA7Ugay9qK7HFiH7Eux6wwdhFJ2+qN1j3hybX2C32qRe3H3I2TqYXP2WYktsqbl2i/ojgC95/5Y0V4evLOtXiEqITLdiOr18SPaAIBQi2XKVlOARFmR6jYGB0xUGlcmIbYsUfb18aQr4CUWWoriMYavx4A6lNf4DD+qta/KFApMoZFv6yyO9ecw3ud72a9nmYvLEHZ6IVDd2gWMZEewo+YihfukEHU1jPEX44dMX4/7VpkI+EdOqXG68CAQOjgcAwgb0wHQYDVR0OBBYEFNLEsNKR1EwRcbNhyz2h/t2oatTjMIGNBgNVHSMEgYUwgYKAFNLEsNKR1EwRcbNhyz2h/t2oatTjoWekZTBjMQswCQYDVQQGEwJVUzEhMB8GA1UEChMYVGhlIEdvIERhZGR5IEdyb3VwLCBJbmMuMTEwLwYDVQQLEyhHbyBEYWRkeSBDbGFzcyAyIENlcnRpZmljYXRpb24gQXV0aG9yaXR5ggEAMAwGA1UdEwQFMAMBAf8wDQYJKoZIhvcNAQEFBQADggEBADJL87LKPpH8EsahB4yOd6AzBhRckB4Y9wimPQoZ+YeAEW5p5JYXMP80kWNyOO7MHAGjHZQopDH2esRU1/blMVgDoszOYtuURXO1v0XJJLXVggKtI3lpjbi2Tc7PTMozI+gciKqdi0FuFskg5YmezTvacPd+mSYgFFQlq25zheabIZ0KbIIOqPjCDPoQHmyW74cNxA9hi63ugyuV+I6ShHI56yDqg+2DzZduCLzrTia2cyvk0/ZM/iZx4mERdEr/VxqHD3VILs9RaRegAhJhldXRQLIQTO7ErBBDpqWeCtWVYpoNz4iCxTIM5CufReYNnyicsbkqWletNw+vHX/bvZ8=",
            "format": "base64"
          }
        ],
        "server_name": "web.telegram.org",
        "t": 0.674971042,
        "tags": null,
        "tls_version": "TLSv1.3"
      }
    ],
    "telegram_http_blocking": false,
    "telegram_tcp_blocking": false,
    "telegram_web_failure": null,
    "telegram_web_status": "ok"
  },
  "test_name": "telegram",
  "test_runtime": 0.83760625,
  "test_start_time": "2022-12-07 10:51:54",
  "test_version": "0.3.0"
}
```

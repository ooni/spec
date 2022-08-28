# Specification version number

2020-01-11-001

* _status_: current

# Specification name

Telegram

# Test preconditions

* An internet connection

# Expected impact

Ability to detect if the Telegram instant messaging platform and the web
version are working, by checking if it's possible to establish a TCP connection
with the IPs of the access points or receive a response back from a HTTP GET
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

The test establishes TCP connection to all the access point IP addresses.
If all TCP connections on ports 80 and 443 to Telegram’s access point IPs fail
we consider Telegram to be blocked. The key `telegram_tcp_blocking` is used
to indicate if we believe telegram to be blocked at the TCP level.

Regardless of the status of the TCP connectivity this test sends HTTP POST
requests on ports 80 and 443 to all access points. If at least an HTTP request
returns back a response, we consider Telegram to not be blocked. The key
`telegram_http_blocking` is used to indicate if we believe telegram to be
blocked at the HTTP level.

## Telegram web version test

Telegram’s web version is likely blocked if HTTP GET requests on ports 80 and
443 to `web.telegram.org` do not send back a consistent response to OONI Probe.

We check to see if Telegram web version is working properly by doing a HTTP GET
request to the following URLs:

* https://web.telegram.org/
* http://web.telegram.org/

If the HTTP(S) requests fail or the HTML `<title>` tag text is not "Telegram
Web" we consider the web version of Telegram to be blocked.

If either one of the HTTP or HTTPS access points are blocked then we write in
the report:

```json
{
    "telegram_web_failure": "FAILURE STRING",
    "telegram_web_status": "blocked"
}
```

If none of the access points are blocked then we write:

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
  "data_format_version": "0.3.4",
  "measurement_start_time": "2020-01-11 17:04:33",
  "test_runtime": 4.960266515,
  "probe_asn": "AS30722",
  "probe_cc": "IT",
  "probe_ip": "127.0.0.1",
  "report_id": "20200111T170433Z_AS30722_6WkpFRNMqrKHAP638WGioX8NQmSdxflluCoKKBGCgPcqDFPLrH",
  "resolver_asn": "AS15169",
  "resolver_ip": "172.217.33.130",
  "resolver_network_name": "Google LLC",
  "software_name": "miniooni",
  "software_version": "0.1.0-dev",
  "test_keys": {
    "agent": "redirect",
    "queries": [
      {
        "answers": [
          {
            "answer_type": "A",
            "ipv4": "149.154.167.99",
            "ttl": null
          }
        ],
        "dial_id": 7,
        "engine": "system",
        "failure": null,
        "hostname": "web.telegram.org",
        "query_type": "A",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "",
        "t": 3.113215,
        "transaction_id": 7
      },
      {
        "answers": [
          {
            "answer_type": "AAAA",
            "ipv6": "2001:67c:4e8:1033:2:100:0:a",
            "ttl": null
          },
          {
            "answer_type": "AAAA",
            "ipv6": "2001:67c:4e8:1033:3:100:0:a",
            "ttl": null
          },
          {
            "answer_type": "AAAA",
            "ipv6": "2001:67c:4e8:1033:5:100:0:a",
            "ttl": null
          },
          {
            "answer_type": "AAAA",
            "ipv6": "2001:67c:4e8:1033:6:100:0:a",
            "ttl": null
          }
        ],
        "dial_id": 7,
        "engine": "system",
        "failure": null,
        "hostname": "web.telegram.org",
        "query_type": "AAAA",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "",
        "t": 3.113215,
        "transaction_id": 7
      },
      {
        "answers": [
          {
            "answer_type": "A",
            "ipv4": "149.154.167.99",
            "ttl": null
          }
        ],
        "dial_id": 11,
        "engine": "system",
        "failure": null,
        "hostname": "web.telegram.org",
        "query_type": "A",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "",
        "t": 4.6675640000000005,
        "transaction_id": 11
      },
      {
        "answers": [
          {
            "answer_type": "AAAA",
            "ipv6": "2001:67c:4e8:1033:2:100:0:a",
            "ttl": null
          },
          {
            "answer_type": "AAAA",
            "ipv6": "2001:67c:4e8:1033:3:100:0:a",
            "ttl": null
          },
          {
            "answer_type": "AAAA",
            "ipv6": "2001:67c:4e8:1033:5:100:0:a",
            "ttl": null
          },
          {
            "answer_type": "AAAA",
            "ipv6": "2001:67c:4e8:1033:6:100:0:a",
            "ttl": null
          }
        ],
        "dial_id": 11,
        "engine": "system",
        "failure": null,
        "hostname": "web.telegram.org",
        "query_type": "AAAA",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "",
        "t": 4.6675640000000005,
        "transaction_id": 11
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
              "Content-Length",
              "0"
            ],
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
              "149.154.167.51"
            ],
            [
              "User-Agent",
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
            ]
          ],
          "headers": {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US;q=0.8,en;q=0.5",
            "Content-Length": "0",
            "Host": "149.154.167.51",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
          },
          "method": "POST",
          "tor": {
            "exit_ip": null,
            "exit_name": null,
            "is_tor": false
          },
          "url": "http://149.154.167.51/"
        },
        "response": {
          "body": "<html>\r\n<head><title>501 Not Implemented</title></head>\r\n<body bgcolor=\"white\">\r\n<center><h1>501 Not Implemented</h1></center>\r\n<hr><center>nginx/0.3.33</center>\r\n</body>\r\n</html>\r\n",
          "body_is_truncated": false,
          "code": 501,
          "headers_list": [
            [
              "Server",
              "nginx/0.3.33"
            ],
            [
              "Date",
              "Sat, 11 Jan 2020 17:04:34 GMT"
            ],
            [
              "Content-Type",
              "text/html"
            ],
            [
              "Content-Length",
              "181"
            ]
          ],
          "headers": {
            "Content-Length": "181",
            "Content-Type": "text/html",
            "Date": "Sat, 11 Jan 2020 17:04:34 GMT",
            "Server": "nginx/0.3.33"
          }
        },
        "transaction_id": 3
      },
      {
        "failure": null,
        "request": {
          "body": "",
          "body_is_truncated": false,
          "headers_list": [
            [
              "Host",
              "149.154.175.100"
            ],
            [
              "User-Agent",
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
            ],
            [
              "Content-Length",
              "0"
            ],
            [
              "Accept",
              "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
            ],
            [
              "Accept-Language",
              "en-US;q=0.8,en;q=0.5"
            ]
          ],
          "headers": {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US;q=0.8,en;q=0.5",
            "Content-Length": "0",
            "Host": "149.154.175.100",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
          },
          "method": "POST",
          "tor": {
            "exit_ip": null,
            "exit_name": null,
            "is_tor": false
          },
          "url": "http://149.154.175.100/"
        },
        "response": {
          "body": "<html>\r\n<head><title>501 Not Implemented</title></head>\r\n<body bgcolor=\"white\">\r\n<center><h1>501 Not Implemented</h1></center>\r\n<hr><center>nginx/0.3.33</center>\r\n</body>\r\n</html>\r\n",
          "body_is_truncated": false,
          "code": 501,
          "headers_list": [
            [
              "Server",
              "nginx/0.3.33"
            ],
            [
              "Date",
              "Sat, 11 Jan 2020 17:04:38 GMT"
            ],
            [
              "Content-Type",
              "text/html"
            ],
            [
              "Content-Length",
              "181"
            ]
          ],
          "headers": {
            "Content-Length": "181",
            "Content-Type": "text/html",
            "Date": "Sat, 11 Jan 2020 17:04:38 GMT",
            "Server": "nginx/0.3.33"
          }
        },
        "transaction_id": 12
      },
      {
        "failure": null,
        "request": {
          "body": "",
          "body_is_truncated": false,
          "headers_list": [
            [
              "Host",
              "149.154.167.91"
            ],
            [
              "User-Agent",
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
            ],
            [
              "Content-Length",
              "0"
            ],
            [
              "Accept",
              "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
            ],
            [
              "Accept-Language",
              "en-US;q=0.8,en;q=0.5"
            ]
          ],
          "headers": {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US;q=0.8,en;q=0.5",
            "Content-Length": "0",
            "Host": "149.154.167.91",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
          },
          "method": "POST",
          "tor": {
            "exit_ip": null,
            "exit_name": null,
            "is_tor": false
          },
          "url": "http://149.154.167.91/"
        },
        "response": {
          "body": "<html>\r\n<head><title>501 Not Implemented</title></head>\r\n<body bgcolor=\"white\">\r\n<center><h1>501 Not Implemented</h1></center>\r\n<hr><center>nginx/0.3.33</center>\r\n</body>\r\n</html>\r\n",
          "body_is_truncated": false,
          "code": 501,
          "headers_list": [
            [
              "Server",
              "nginx/0.3.33"
            ],
            [
              "Date",
              "Sat, 11 Jan 2020 17:04:37 GMT"
            ],
            [
              "Content-Type",
              "text/html"
            ],
            [
              "Content-Length",
              "181"
            ]
          ],
          "headers": {
            "Content-Length": "181",
            "Content-Type": "text/html",
            "Date": "Sat, 11 Jan 2020 17:04:37 GMT",
            "Server": "nginx/0.3.33"
          }
        },
        "transaction_id": 9
      },
      {
        "failure": null,
        "request": {
          "body": "",
          "body_is_truncated": false,
          "headers_list": [
            [
              "Host",
              "149.154.171.5"
            ],
            [
              "User-Agent",
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
            ],
            [
              "Content-Length",
              "0"
            ],
            [
              "Accept",
              "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
            ],
            [
              "Accept-Language",
              "en-US;q=0.8,en;q=0.5"
            ]
          ],
          "headers": {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US;q=0.8,en;q=0.5",
            "Content-Length": "0",
            "Host": "149.154.171.5",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
          },
          "method": "POST",
          "tor": {
            "exit_ip": null,
            "exit_name": null,
            "is_tor": false
          },
          "url": "http://149.154.171.5/"
        },
        "response": {
          "body": "<html>\r\n<head><title>501 Not Implemented</title></head>\r\n<body bgcolor=\"white\">\r\n<center><h1>501 Not Implemented</h1></center>\r\n<hr><center>nginx/0.3.33</center>\r\n</body>\r\n</html>\r\n",
          "body_is_truncated": false,
          "code": 501,
          "headers_list": [
            [
              "Content-Type",
              "text/html"
            ],
            [
              "Content-Length",
              "181"
            ],
            [
              "Server",
              "nginx/0.3.33"
            ],
            [
              "Date",
              "Sat, 11 Jan 2020 17:04:38 GMT"
            ]
          ],
          "headers": {
            "Content-Length": "181",
            "Content-Type": "text/html",
            "Date": "Sat, 11 Jan 2020 17:04:38 GMT",
            "Server": "nginx/0.3.33"
          }
        },
        "transaction_id": 10
      },
      {
        "failure": null,
        "request": {
          "body": "",
          "body_is_truncated": false,
          "headers_list": [
            [
              "Accept-Language",
              "en-US;q=0.8,en;q=0.5"
            ],
            [
              "Host",
              "149.154.175.100:443"
            ],
            [
              "User-Agent",
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
            ],
            [
              "Content-Length",
              "0"
            ],
            [
              "Accept",
              "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
            ]
          ],
          "headers": {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US;q=0.8,en;q=0.5",
            "Content-Length": "0",
            "Host": "149.154.175.100:443",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
          },
          "method": "POST",
          "tor": {
            "exit_ip": null,
            "exit_name": null,
            "is_tor": false
          },
          "url": "http://149.154.175.100:443/"
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
              "Server",
              "nginx/0.3.33"
            ],
            [
              "Date",
              "Sat, 11 Jan 2020 17:04:35 GMT"
            ],
            [
              "Content-Type",
              "text/html"
            ]
          ],
          "headers": {
            "Content-Length": "181",
            "Content-Type": "text/html",
            "Date": "Sat, 11 Jan 2020 17:04:35 GMT",
            "Server": "nginx/0.3.33"
          }
        },
        "transaction_id": 4
      },
      {
        "failure": null,
        "request": {
          "body": "",
          "body_is_truncated": false,
          "headers_list": [
            [
              "Host",
              "149.154.167.91:443"
            ],
            [
              "User-Agent",
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
            ],
            [
              "Content-Length",
              "0"
            ],
            [
              "Accept",
              "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
            ],
            [
              "Accept-Language",
              "en-US;q=0.8,en;q=0.5"
            ]
          ],
          "headers": {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US;q=0.8,en;q=0.5",
            "Content-Length": "0",
            "Host": "149.154.167.91:443",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
          },
          "method": "POST",
          "tor": {
            "exit_ip": null,
            "exit_name": null,
            "is_tor": false
          },
          "url": "http://149.154.167.91:443/"
        },
        "response": {
          "body": "<html>\r\n<head><title>501 Not Implemented</title></head>\r\n<body bgcolor=\"white\">\r\n<center><h1>501 Not Implemented</h1></center>\r\n<hr><center>nginx/0.3.33</center>\r\n</body>\r\n</html>\r\n",
          "body_is_truncated": false,
          "code": 501,
          "headers_list": [
            [
              "Server",
              "nginx/0.3.33"
            ],
            [
              "Date",
              "Sat, 11 Jan 2020 17:04:35 GMT"
            ],
            [
              "Content-Type",
              "text/html"
            ],
            [
              "Content-Length",
              "181"
            ]
          ],
          "headers": {
            "Content-Length": "181",
            "Content-Type": "text/html",
            "Date": "Sat, 11 Jan 2020 17:04:35 GMT",
            "Server": "nginx/0.3.33"
          }
        },
        "transaction_id": 2
      },
      {
        "failure": null,
        "request": {
          "body": "",
          "body_is_truncated": false,
          "headers_list": [
            [
              "Host",
              "149.154.175.50"
            ],
            [
              "User-Agent",
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
            ],
            [
              "Content-Length",
              "0"
            ],
            [
              "Accept",
              "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
            ],
            [
              "Accept-Language",
              "en-US;q=0.8,en;q=0.5"
            ]
          ],
          "headers": {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US;q=0.8,en;q=0.5",
            "Content-Length": "0",
            "Host": "149.154.175.50",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
          },
          "method": "POST",
          "tor": {
            "exit_ip": null,
            "exit_name": null,
            "is_tor": false
          },
          "url": "http://149.154.175.50/"
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
              "Server",
              "nginx/0.3.33"
            ],
            [
              "Date",
              "Sat, 11 Jan 2020 17:04:34 GMT"
            ],
            [
              "Content-Type",
              "text/html"
            ]
          ],
          "headers": {
            "Content-Length": "181",
            "Content-Type": "text/html",
            "Date": "Sat, 11 Jan 2020 17:04:34 GMT",
            "Server": "nginx/0.3.33"
          }
        },
        "transaction_id": 1
      },
      {
        "failure": null,
        "request": {
          "body": "",
          "body_is_truncated": false,
          "headers_list": [
            [
              "Host",
              "149.154.175.50:443"
            ],
            [
              "User-Agent",
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
            ],
            [
              "Content-Length",
              "0"
            ],
            [
              "Accept",
              "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
            ],
            [
              "Accept-Language",
              "en-US;q=0.8,en;q=0.5"
            ]
          ],
          "headers": {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US;q=0.8,en;q=0.5",
            "Content-Length": "0",
            "Host": "149.154.175.50:443",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
          },
          "method": "POST",
          "tor": {
            "exit_ip": null,
            "exit_name": null,
            "is_tor": false
          },
          "url": "http://149.154.175.50:443/"
        },
        "response": {
          "body": "<html>\r\n<head><title>501 Not Implemented</title></head>\r\n<body bgcolor=\"white\">\r\n<center><h1>501 Not Implemented</h1></center>\r\n<hr><center>nginx/0.3.33</center>\r\n</body>\r\n</html>\r\n",
          "body_is_truncated": false,
          "code": 501,
          "headers_list": [
            [
              "Server",
              "nginx/0.3.33"
            ],
            [
              "Date",
              "Sat, 11 Jan 2020 17:04:36 GMT"
            ],
            [
              "Content-Type",
              "text/html"
            ],
            [
              "Content-Length",
              "181"
            ]
          ],
          "headers": {
            "Content-Length": "181",
            "Content-Type": "text/html",
            "Date": "Sat, 11 Jan 2020 17:04:36 GMT",
            "Server": "nginx/0.3.33"
          }
        },
        "transaction_id": 6
      },
      {
        "failure": null,
        "request": {
          "body": "",
          "body_is_truncated": false,
          "headers_list": [
            [
              "Accept-Language",
              "en-US;q=0.8,en;q=0.5"
            ],
            [
              "Host",
              "149.154.167.51:443"
            ],
            [
              "User-Agent",
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
            ],
            [
              "Content-Length",
              "0"
            ],
            [
              "Accept",
              "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
            ]
          ],
          "headers": {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US;q=0.8,en;q=0.5",
            "Content-Length": "0",
            "Host": "149.154.167.51:443",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
          },
          "method": "POST",
          "tor": {
            "exit_ip": null,
            "exit_name": null,
            "is_tor": false
          },
          "url": "http://149.154.167.51:443/"
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
              "Server",
              "nginx/0.3.33"
            ],
            [
              "Date",
              "Sat, 11 Jan 2020 17:04:37 GMT"
            ],
            [
              "Content-Type",
              "text/html"
            ]
          ],
          "headers": {
            "Content-Length": "181",
            "Content-Type": "text/html",
            "Date": "Sat, 11 Jan 2020 17:04:37 GMT",
            "Server": "nginx/0.3.33"
          }
        },
        "transaction_id": 8
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
              "149.154.171.5:443"
            ],
            [
              "User-Agent",
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
            ],
            [
              "Content-Length",
              "0"
            ]
          ],
          "headers": {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US;q=0.8,en;q=0.5",
            "Content-Length": "0",
            "Host": "149.154.171.5:443",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
          },
          "method": "POST",
          "tor": {
            "exit_ip": null,
            "exit_name": null,
            "is_tor": false
          },
          "url": "http://149.154.171.5:443/"
        },
        "response": {
          "body": "<html>\r\n<head><title>501 Not Implemented</title></head>\r\n<body bgcolor=\"white\">\r\n<center><h1>501 Not Implemented</h1></center>\r\n<hr><center>nginx/0.3.33</center>\r\n</body>\r\n</html>\r\n",
          "body_is_truncated": false,
          "code": 501,
          "headers_list": [
            [
              "Content-Type",
              "text/html"
            ],
            [
              "Content-Length",
              "181"
            ],
            [
              "Server",
              "nginx/0.3.33"
            ],
            [
              "Date",
              "Sat, 11 Jan 2020 17:04:35 GMT"
            ]
          ],
          "headers": {
            "Content-Length": "181",
            "Content-Type": "text/html",
            "Date": "Sat, 11 Jan 2020 17:04:35 GMT",
            "Server": "nginx/0.3.33"
          }
        },
        "transaction_id": 5
      },
      {
        "failure": null,
        "request": {
          "body": "",
          "body_is_truncated": false,
          "headers_list": [
            [
              "Accept-Language",
              "en-US;q=0.8,en;q=0.5"
            ],
            [
              "Host",
              "web.telegram.org"
            ],
            [
              "User-Agent",
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
            ],
            [
              "Accept",
              "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
            ]
          ],
          "headers": {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US;q=0.8,en;q=0.5",
            "Host": "web.telegram.org",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
          },
          "method": "GET",
          "tor": {
            "exit_ip": null,
            "exit_name": null,
            "is_tor": false
          },
          "url": "http://web.telegram.org/"
        },
        "response": {
          "body": "<!doctype html><html lang=en manifest=webogram.appcache ng-csp xmlns:ng=http://angularjs.org id=ng-app style=\"display: none;\"><head><meta charset=utf-8><meta name=viewport content=\"width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no\"><title>Telegram Web</title><link rel=stylesheet href=css/app.css><link rel=manifest href=manifest.webapp.json><link rel=icon href=favicon.ico type=image/x-icon><link rel=apple-touch-icon href=img/iphone_home120.png><link rel=apple-touch-icon sizes=120x120 href=img/iphone_home120.png><link rel=apple-touch-startup-image media=\"(device-width: 320px)\" href=img/iphone_startup.png><meta name=apple-mobile-web-app-title content=\"Telegram Web\"><meta name=mobile-web-app-capable content=yes><meta name=apple-mobile-web-app-capable content=yes><meta name=apple-mobile-web-app-status-bar-style content=black-translucent><meta name=theme-color content=#497495><meta name=google content=notranslate><meta property=og:title content=\"Telegram Web\"><meta property=og:url content=\"https://web.telegram.org/\"><meta property=og:image content=https://web.telegram.org/img/logo_share.png><meta property=og:site_name content=\"Telegram Web\"><meta property=description content=\"Welcome to the Web application of Telegram messenger. See https://github.com/zhukov/webogram for more info.\"><meta property=og:description content=\"Welcome to the Web application of Telegram messenger. See https://github.com/zhukov/webogram for more info.\"></head><body><div class=page_wrap ng-view></div><div id=notify_sound></div><script src=js/app.js></script></body></html>",
          "body_is_truncated": false,
          "code": 200,
          "headers_list": [
            [
              "Cache-Control",
              "max-age=3600"
            ],
            [
              "Date",
              "Sat, 11 Jan 2020 17:04:36 GMT"
            ],
            [
              "Content-Type",
              "text/html"
            ],
            [
              "Content-Length",
              "1587"
            ],
            [
              "Last-Modified",
              "Thu, 19 Sep 2019 21:44:08 GMT"
            ],
            [
              "Expires",
              "Sat, 11 Jan 2020 18:04:36 GMT"
            ],
            [
              "Server",
              "nginx/1.16.1"
            ],
            [
              "Connection",
              "keep-alive"
            ],
            [
              "Etag",
              "\"5d83f6a8-633\""
            ],
            [
              "X-Frame-Options",
              "deny"
            ],
            [
              "Accept-Ranges",
              "bytes"
            ]
          ],
          "headers": {
            "Accept-Ranges": "bytes",
            "Cache-Control": "max-age=3600",
            "Connection": "keep-alive",
            "Content-Length": "1587",
            "Content-Type": "text/html",
            "Date": "Sat, 11 Jan 2020 17:04:36 GMT",
            "Etag": "\"5d83f6a8-633\"",
            "Expires": "Sat, 11 Jan 2020 18:04:36 GMT",
            "Last-Modified": "Thu, 19 Sep 2019 21:44:08 GMT",
            "Server": "nginx/1.16.1",
            "X-Frame-Options": "deny"
          }
        },
        "transaction_id": 7
      },
      {
        "failure": null,
        "request": {
          "body": "",
          "body_is_truncated": false,
          "headers_list": [
            [
              "Host",
              "web.telegram.org"
            ],
            [
              "User-Agent",
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
            ],
            [
              "Accept",
              "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
            ],
            [
              "Accept-Language",
              "en-US;q=0.8,en;q=0.5"
            ]
          ],
          "headers": {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US;q=0.8,en;q=0.5",
            "Host": "web.telegram.org",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
          },
          "method": "GET",
          "tor": {
            "exit_ip": null,
            "exit_name": null,
            "is_tor": false
          },
          "url": "https://web.telegram.org/"
        },
        "response": {
          "body": "<!doctype html><html lang=en manifest=webogram.appcache ng-csp xmlns:ng=http://angularjs.org id=ng-app style=\"display: none;\"><head><meta charset=utf-8><meta name=viewport content=\"width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no\"><title>Telegram Web</title><link rel=stylesheet href=css/app.css><link rel=manifest href=manifest.webapp.json><link rel=icon href=favicon.ico type=image/x-icon><link rel=apple-touch-icon href=img/iphone_home120.png><link rel=apple-touch-icon sizes=120x120 href=img/iphone_home120.png><link rel=apple-touch-startup-image media=\"(device-width: 320px)\" href=img/iphone_startup.png><meta name=apple-mobile-web-app-title content=\"Telegram Web\"><meta name=mobile-web-app-capable content=yes><meta name=apple-mobile-web-app-capable content=yes><meta name=apple-mobile-web-app-status-bar-style content=black-translucent><meta name=theme-color content=#497495><meta name=google content=notranslate><meta property=og:title content=\"Telegram Web\"><meta property=og:url content=\"https://web.telegram.org/\"><meta property=og:image content=https://web.telegram.org/img/logo_share.png><meta property=og:site_name content=\"Telegram Web\"><meta property=description content=\"Welcome to the Web application of Telegram messenger. See https://github.com/zhukov/webogram for more info.\"><meta property=og:description content=\"Welcome to the Web application of Telegram messenger. See https://github.com/zhukov/webogram for more info.\"></head><body><div class=page_wrap ng-view></div><div id=notify_sound></div><script src=js/app.js></script></body></html>",
          "body_is_truncated": false,
          "code": 200,
          "headers_list": [
            [
              "Connection",
              "keep-alive"
            ],
            [
              "Etag",
              "\"5d83f6a8-633\""
            ],
            [
              "Cache-Control",
              "max-age=3600"
            ],
            [
              "Accept-Ranges",
              "bytes"
            ],
            [
              "Server",
              "nginx/1.16.1"
            ],
            [
              "Content-Type",
              "text/html"
            ],
            [
              "Content-Length",
              "1587"
            ],
            [
              "X-Frame-Options",
              "deny"
            ],
            [
              "Date",
              "Sat, 11 Jan 2020 17:04:38 GMT"
            ],
            [
              "Last-Modified",
              "Thu, 19 Sep 2019 21:44:08 GMT"
            ],
            [
              "Expires",
              "Sat, 11 Jan 2020 18:04:38 GMT"
            ]
          ],
          "headers": {
            "Accept-Ranges": "bytes",
            "Cache-Control": "max-age=3600",
            "Connection": "keep-alive",
            "Content-Length": "1587",
            "Content-Type": "text/html",
            "Date": "Sat, 11 Jan 2020 17:04:38 GMT",
            "Etag": "\"5d83f6a8-633\"",
            "Expires": "Sat, 11 Jan 2020 18:04:38 GMT",
            "Last-Modified": "Thu, 19 Sep 2019 21:44:08 GMT",
            "Server": "nginx/1.16.1",
            "X-Frame-Options": "deny"
          }
        },
        "transaction_id": 11
      }
    ],
    "tcp_connect": [
      {
        "conn_id": 2,
        "dial_id": 3,
        "ip": "149.154.167.51",
        "port": 80,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 1.121284,
        "transaction_id": 3
      },
      {
        "conn_id": 12,
        "dial_id": 12,
        "ip": "149.154.175.100",
        "port": 80,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 4.816708,
        "transaction_id": 12
      },
      {
        "conn_id": 9,
        "dial_id": 9,
        "ip": "149.154.167.91",
        "port": 80,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 4.277217,
        "transaction_id": 9
      },
      {
        "conn_id": 10,
        "dial_id": 10,
        "ip": "149.154.171.5",
        "port": 80,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 4.477224,
        "transaction_id": 10
      },
      {
        "conn_id": 3,
        "dial_id": 4,
        "ip": "149.154.175.100",
        "port": 443,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 1.8291520000000001,
        "transaction_id": 4
      },
      {
        "conn_id": 4,
        "dial_id": 2,
        "ip": "149.154.167.91",
        "port": 443,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 1.84943,
        "transaction_id": 2
      },
      {
        "conn_id": 1,
        "dial_id": 1,
        "ip": "149.154.175.50",
        "port": 80,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.676892,
        "transaction_id": 1
      },
      {
        "conn_id": 6,
        "dial_id": 6,
        "ip": "149.154.175.50",
        "port": 443,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 2.64445,
        "transaction_id": 6
      },
      {
        "conn_id": 8,
        "dial_id": 8,
        "ip": "149.154.167.51",
        "port": 443,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 4.160087,
        "transaction_id": 8
      },
      {
        "conn_id": 5,
        "dial_id": 5,
        "ip": "149.154.171.5",
        "port": 443,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 2.288224,
        "transaction_id": 5
      },
      {
        "conn_id": 7,
        "dial_id": 7,
        "ip": "149.154.167.99",
        "port": 80,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 3.153261,
        "transaction_id": 7
      },
      {
        "conn_id": 11,
        "dial_id": 11,
        "ip": "149.154.167.99",
        "port": 443,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 4.7072389999999995,
        "transaction_id": 11
      }
    ],
    "telegram_http_blocking": false,
    "telegram_tcp_blocking": false,
    "telegram_web_failure": null,
    "telegram_web_status": "ok",
    "tls_handshakes": [
      {
        "cipher_suite": "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256",
        "failure": null,
        "negotiated_protocol": "http/1.1",
        "peer_certificates": [
          {
            "data": "MIIFPDCCBCSgAwIBAgIJAJnXpwlYmeKBMA0GCSqGSIb3DQEBCwUAMIG0MQswCQYDVQQGEwJVUzEQMA4GA1UECBMHQXJpem9uYTETMBEGA1UEBxMKU2NvdHRzZGFsZTEaMBgGA1UEChMRR29EYWRkeS5jb20sIEluYy4xLTArBgNVBAsTJGh0dHA6Ly9jZXJ0cy5nb2RhZGR5LmNvbS9yZXBvc2l0b3J5LzEzMDEGA1UEAxMqR28gRGFkZHkgU2VjdXJlIENlcnRpZmljYXRlIEF1dGhvcml0eSAtIEcyMB4XDTE3MTAyMzEyMjkwMFoXDTIwMTAyNzE2MDQzN1owQDEhMB8GA1UECxMYRG9tYWluIENvbnRyb2wgVmFsaWRhdGVkMRswGQYDVQQDDBIqLndlYi50ZWxlZ3JhbS5vcmcwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDXBGS7HQY5gJe8Qp5AOA+B0qB9e9evyiZRSP24mHT5w53yx95XIFrFd+Fk0ABaomc6uRg9PES+Qc9BruNL9pV3cytQMxJE0Ybou5hY4aMYjvTRMGs9jl/rgClXAczOc/qvbvPrCS3JbkfOgS7+1T5eN4ud4y9dP2Q7d51fm/3Z0EufupGWSKMdOiXTymuSv2FbVY7Rq2PlaZ3IK4Ro9s+a7TwZ/b3KATWXWzfIkGM90VxxQH+pHruRaSdOiWeNT5AfwebgFFCy7Wzt5GYOK4k0zYDO2nX+fms4YeeynMwH1gCmlvRoOJSWNP6sfwgBJCdFkoBOJfrp4SRjxvn453krAgMBAAGjggHCMIIBvjAMBgNVHRMBAf8EAjAAMB0GA1UdJQQWMBQGCCsGAQUFBwMBBggrBgEFBQcDAjAOBgNVHQ8BAf8EBAMCBaAwNwYDVR0fBDAwLjAsoCqgKIYmaHR0cDovL2NybC5nb2RhZGR5LmNvbS9nZGlnMnMxLTc1OS5jcmwwXQYDVR0gBFYwVDBIBgtghkgBhv1tAQcXATA5MDcGCCsGAQUFBwIBFitodHRwOi8vY2VydGlmaWNhdGVzLmdvZGFkZHkuY29tL3JlcG9zaXRvcnkvMAgGBmeBDAECATB2BggrBgEFBQcBAQRqMGgwJAYIKwYBBQUHMAGGGGh0dHA6Ly9vY3NwLmdvZGFkZHkuY29tLzBABggrBgEFBQcwAoY0aHR0cDovL2NlcnRpZmljYXRlcy5nb2RhZGR5LmNvbS9yZXBvc2l0b3J5L2dkaWcyLmNydDAfBgNVHSMEGDAWgBRAwr0njsw0gzCiM9f7bLPwtCyAzjAvBgNVHREEKDAmghIqLndlYi50ZWxlZ3JhbS5vcmeCEHdlYi50ZWxlZ3JhbS5vcmcwHQYDVR0OBBYEFEeHj2e6FBgMjFEmTOgZSLFtI8eZMA0GCSqGSIb3DQEBCwUAA4IBAQCvRBAnnq02614m5Xgroam1i7JB2bMZVMrwCejwY9otLkM3tnjE0q6ZFQYtawImkfBgJZ7nWxho4JOU1DTXDsjjr9VulbsTo8YhUAWC+rMcygkCmEjzRv7mNOmQ/hsLSLNZejLqAPRCuzX7dfTAZ+f4gJqbeA0FOuN50NQiJEFPWu2bkQsC9G1bHAQs6e3lwP6RvCzsQxUocx+Q36TiwIH1Jm81oxkQQetQQ01nlcExV0knLAQ3ZyDyVO/5Off+j3viquUQas9HtudFbyIPPsbvCD+hs2KO+PLjqLLTiSammhN1qZy9R89GEd8CdY4U8tdfuqhvKrabIdiNwBsqPo3f",
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
        "t": 4.796171,
        "tls_version": "TLSv1.2",
        "transaction_id": 11
      }
    ]
  },
  "test_name": "telegram",
  "test_start_time": "2020-01-11 17:04:33",
  "test_version": "0.0.5"
}
```

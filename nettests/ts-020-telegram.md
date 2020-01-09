# Specification version number

2020-01-09-001

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
we consider Telegram to be blocked:

```json
{
  "tcp_connect": [
    {
      "ip": "149.154.167.50",
      "port": 443,
      "status": {
        "failure": "generic_timeout_error",
        "success": false
      }
    }
  ]
}
```
The key `telegram_tcp_blocking` is used to indicate if we believe telegram to be blocked at
the TCP level.

Regardless of the status of the TCP connectivity this test sends HTTP POST
requests on ports 80 and 443 to all access points. If at least an HTTP request
returns back a response, we consider Telegram to not be blocked:

```json
{
    "failure": "generic_timeout_error",
    "request": {
        "body": null,
        "headers": {},
        "method": "POST",
        "tor": {
            "exit_ip": null,
            "exit_name": null,
            "is_tor": false
        },
        "url": "http://149.154.167.50:80"
    },
    "response": null
}
```

The key `telegram_http_blocking` is used to indicate if we believe telegram to be blocked at
the HTTP level.

## Telegram web version test

Telegram’s web version is likely blocked if HTTP GET requests on ports 80 and
443 to `web.telegram.org` do not send back a consistent response to OONI’s
servers.

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

* df-001-httpt
* df-002-dnst

## Semantics

```
{
    "telegram_http_blocking": true | false,
    "telegram_tcp_blocking": true | false,

    "telegram_web_failure": "failure_string" | null,
    "telegram_web_status": "blocked" | "ok" | null,

    "tcp_connect": [
        {
            "ip": "xxx.xxx.xxx.xxx",
            "port": 80 | 443,
            "status": {
                "success": true | false,
                "failure": "FAILURE STRING"
            }
        }
    ],
}
```

The meaning of the various keys is described in the above section.

## Possible conclusions

* If it is possible for users to use the Telegram software

* If it is possible for users to use the web version of Telegram

## Example output sample

```json
{
  "data_format_version": "0.3.1",
  "measurement_start_time": "2020-01-09 10:47:18",
  "test_runtime": 5.180580507,
  "probe_asn": "AS30722",
  "probe_cc": "IT",
  "probe_ip": "127.0.0.1",
  "report_id": "20200109T104718Z_AS30722_mziQrgknAZXPk13DgIV3CVNdoVQaxQFqIXiP0scW6r1nTgBfdM",
  "resolver_asn": "AS15169",
  "resolver_ip": "172.217.34.3",
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
        "engine": "system",
        "failure": null,
        "hostname": "web.telegram.org",
        "query_type": "A",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": ""
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
        "engine": "system",
        "failure": null,
        "hostname": "web.telegram.org",
        "query_type": "AAAA",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": ""
      },
      {
        "answers": [
          {
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
        "resolver_address": ""
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
        "engine": "system",
        "failure": null,
        "hostname": "web.telegram.org",
        "query_type": "AAAA",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": ""
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
              "149.154.167.51"
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
              "Date",
              "Thu, 09 Jan 2020 10:47:21 GMT"
            ],
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
            ]
          ],
          "headers": {
            "Content-Length": "181",
            "Content-Type": "text/html",
            "Date": "Thu, 09 Jan 2020 10:47:21 GMT",
            "Server": "nginx/0.3.33"
          }
        }
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
              "149.154.167.91"
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
              "Content-Length",
              "181"
            ],
            [
              "Server",
              "nginx/0.3.33"
            ],
            [
              "Date",
              "Thu, 09 Jan 2020 10:47:21 GMT"
            ],
            [
              "Content-Type",
              "text/html"
            ]
          ],
          "headers": {
            "Content-Length": "181",
            "Content-Type": "text/html",
            "Date": "Thu, 09 Jan 2020 10:47:21 GMT",
            "Server": "nginx/0.3.33"
          }
        }
      },
      {
        "failure": null,
        "request": {
          "body": "",
          "body_is_truncated": false,
          "headers_list": [
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
            ],
            [
              "Host",
              "149.154.171.5"
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
              "Date",
              "Thu, 09 Jan 2020 10:47:23 GMT"
            ],
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
            ]
          ],
          "headers": {
            "Content-Length": "181",
            "Content-Type": "text/html",
            "Date": "Thu, 09 Jan 2020 10:47:23 GMT",
            "Server": "nginx/0.3.33"
          }
        }
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
              "Date",
              "Thu, 09 Jan 2020 10:47:23 GMT"
            ],
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
            ]
          ],
          "headers": {
            "Content-Length": "181",
            "Content-Type": "text/html",
            "Date": "Thu, 09 Jan 2020 10:47:23 GMT",
            "Server": "nginx/0.3.33"
          }
        }
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
              "Thu, 09 Jan 2020 10:47:18 GMT"
            ]
          ],
          "headers": {
            "Content-Length": "181",
            "Content-Type": "text/html",
            "Date": "Thu, 09 Jan 2020 10:47:18 GMT",
            "Server": "nginx/0.3.33"
          }
        }
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
              "Server",
              "nginx/1.16.1"
            ],
            [
              "Date",
              "Thu, 09 Jan 2020 10:47:23 GMT"
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
              "Connection",
              "keep-alive"
            ],
            [
              "Expires",
              "Thu, 09 Jan 2020 11:47:23 GMT"
            ],
            [
              "X-Frame-Options",
              "deny"
            ]
          ],
          "headers": {
            "Accept-Ranges": "bytes",
            "Cache-Control": "max-age=3600",
            "Connection": "keep-alive",
            "Content-Length": "1587",
            "Content-Type": "text/html",
            "Date": "Thu, 09 Jan 2020 10:47:23 GMT",
            "Etag": "\"5d83f6a8-633\"",
            "Expires": "Thu, 09 Jan 2020 11:47:23 GMT",
            "Last-Modified": "Thu, 19 Sep 2019 21:44:08 GMT",
            "Server": "nginx/1.16.1",
            "X-Frame-Options": "deny"
          }
        }
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
              "Server",
              "nginx/0.3.33"
            ],
            [
              "Date",
              "Thu, 09 Jan 2020 10:47:21 GMT"
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
            "Date": "Thu, 09 Jan 2020 10:47:21 GMT",
            "Server": "nginx/0.3.33"
          }
        }
      },
      {
        "failure": null,
        "request": {
          "body": "",
          "body_is_truncated": false,
          "headers_list": [
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
              "Server",
              "nginx/0.3.33"
            ],
            [
              "Date",
              "Thu, 09 Jan 2020 10:47:22 GMT"
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
            "Date": "Thu, 09 Jan 2020 10:47:22 GMT",
            "Server": "nginx/0.3.33"
          }
        }
      },
      {
        "failure": null,
        "request": {
          "body": "",
          "body_is_truncated": false,
          "headers_list": [
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
            ],
            [
              "Host",
              "149.154.175.100:443"
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
              "Server",
              "nginx/0.3.33"
            ],
            [
              "Date",
              "Thu, 09 Jan 2020 10:47:23 GMT"
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
            "Date": "Thu, 09 Jan 2020 10:47:23 GMT",
            "Server": "nginx/0.3.33"
          }
        }
      },
      {
        "failure": null,
        "request": {
          "body": "",
          "body_is_truncated": false,
          "headers_list": [
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
              "Server",
              "nginx/0.3.33"
            ],
            [
              "Date",
              "Thu, 09 Jan 2020 10:47:23 GMT"
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
            "Date": "Thu, 09 Jan 2020 10:47:23 GMT",
            "Server": "nginx/0.3.33"
          }
        }
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
          "url": "http://web.telegram.org/"
        },
        "response": {
          "body": "<!doctype html><html lang=en manifest=webogram.appcache ng-csp xmlns:ng=http://angularjs.org id=ng-app style=\"display: none;\"><head><meta charset=utf-8><meta name=viewport content=\"width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no\"><title>Telegram Web</title><link rel=stylesheet href=css/app.css><link rel=manifest href=manifest.webapp.json><link rel=icon href=favicon.ico type=image/x-icon><link rel=apple-touch-icon href=img/iphone_home120.png><link rel=apple-touch-icon sizes=120x120 href=img/iphone_home120.png><link rel=apple-touch-startup-image media=\"(device-width: 320px)\" href=img/iphone_startup.png><meta name=apple-mobile-web-app-title content=\"Telegram Web\"><meta name=mobile-web-app-capable content=yes><meta name=apple-mobile-web-app-capable content=yes><meta name=apple-mobile-web-app-status-bar-style content=black-translucent><meta name=theme-color content=#497495><meta name=google content=notranslate><meta property=og:title content=\"Telegram Web\"><meta property=og:url content=\"https://web.telegram.org/\"><meta property=og:image content=https://web.telegram.org/img/logo_share.png><meta property=og:site_name content=\"Telegram Web\"><meta property=description content=\"Welcome to the Web application of Telegram messenger. See https://github.com/zhukov/webogram for more info.\"><meta property=og:description content=\"Welcome to the Web application of Telegram messenger. See https://github.com/zhukov/webogram for more info.\"></head><body><div class=page_wrap ng-view></div><div id=notify_sound></div><script src=js/app.js></script></body></html>",
          "body_is_truncated": false,
          "code": 200,
          "headers_list": [
            [
              "Accept-Ranges",
              "bytes"
            ],
            [
              "Content-Length",
              "1587"
            ],
            [
              "Etag",
              "\"5d83f6a8-633\""
            ],
            [
              "Expires",
              "Thu, 09 Jan 2020 11:47:23 GMT"
            ],
            [
              "Last-Modified",
              "Thu, 19 Sep 2019 21:44:08 GMT"
            ],
            [
              "Connection",
              "keep-alive"
            ],
            [
              "Cache-Control",
              "max-age=3600"
            ],
            [
              "X-Frame-Options",
              "deny"
            ],
            [
              "Server",
              "nginx/1.16.1"
            ],
            [
              "Date",
              "Thu, 09 Jan 2020 10:47:23 GMT"
            ],
            [
              "Content-Type",
              "text/html"
            ]
          ],
          "headers": {
            "Accept-Ranges": "bytes",
            "Cache-Control": "max-age=3600",
            "Connection": "keep-alive",
            "Content-Length": "1587",
            "Content-Type": "text/html",
            "Date": "Thu, 09 Jan 2020 10:47:23 GMT",
            "Etag": "\"5d83f6a8-633\"",
            "Expires": "Thu, 09 Jan 2020 11:47:23 GMT",
            "Last-Modified": "Thu, 19 Sep 2019 21:44:08 GMT",
            "Server": "nginx/1.16.1",
            "X-Frame-Options": "deny"
          }
        }
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
              "Thu, 09 Jan 2020 10:47:21 GMT"
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
            "Date": "Thu, 09 Jan 2020 10:47:21 GMT",
            "Server": "nginx/0.3.33"
          }
        }
      }
    ],
    "tcp_connect": [
      {
        "ip": "149.154.167.51",
        "port": 80,
        "status": {
          "failure": null,
          "success": true
        }
      },
      {
        "ip": "149.154.167.91",
        "port": 80,
        "status": {
          "failure": null,
          "success": true
        }
      },
      {
        "ip": "149.154.171.5",
        "port": 80,
        "status": {
          "failure": null,
          "success": true
        }
      },
      {
        "ip": "149.154.175.50",
        "port": 443,
        "status": {
          "failure": null,
          "success": true
        }
      },
      {
        "ip": "149.154.167.91",
        "port": 443,
        "status": {
          "failure": null,
          "success": true
        }
      },
      {
        "ip": "149.154.167.99",
        "port": 443,
        "status": {
          "failure": null,
          "success": true
        }
      },
      {
        "ip": "149.154.175.50",
        "port": 80,
        "status": {
          "failure": null,
          "success": true
        }
      },
      {
        "ip": "149.154.167.51",
        "port": 443,
        "status": {
          "failure": null,
          "success": true
        }
      },
      {
        "ip": "149.154.175.100",
        "port": 443,
        "status": {
          "failure": null,
          "success": true
        }
      },
      {
        "ip": "149.154.171.5",
        "port": 443,
        "status": {
          "failure": null,
          "success": true
        }
      },
      {
        "ip": "149.154.167.99",
        "port": 80,
        "status": {
          "failure": null,
          "success": true
        }
      },
      {
        "ip": "149.154.175.100",
        "port": 80,
        "status": {
          "failure": null,
          "success": true
        }
      }
    ],
    "telegram_http_blocking": false,
    "telegram_tcp_blocking": false,
    "telegram_web_failure": null,
    "telegram_web_status": "ok"
  },
  "test_name": "telegram",
  "test_start_time": "2020-01-09 10:47:18",
  "test_version": "0.0.4"
}
```

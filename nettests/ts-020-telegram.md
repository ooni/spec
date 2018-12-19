# Specification version number

2016-04-04-001

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

Regardless of the status of the TCP connectivity this test sends HTTP POST
requests on ports 80 and 443 to all access points. If any HTTP requests do
not get back a response from an access point IP then it is considered as
blocked:

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

## Semantics

```json
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
    "annotations": {
        "platform": "linux"
    },
    "data_format_version": "0.2.0",
    "id": "70b17d09-2d63-4639-a7a1-9101def471af",
    "input": null,
    "input_hashes": [],
    "measurement_start_time": "2017-04-07 01:33:25",
    "options": [],
    "probe_asn": "AS3320",
    "probe_cc": "DE",
    "probe_city": null,
    "probe_ip": "127.0.0.1",
    "report_id": "91Ug70AUS4LTLahA6XVZW2QhcHxgEZS4ydYEjwzEtM3iIgL3MHt29kth3oBO5BES",
    "software_name": "ooniprobe",
    "software_version": "2.2.0",
    "test_helpers": {},
    "test_keys": {
        "agent": "redirect",
        "requests": [
            {
                "failure": "connection_refused_error",
                "request": {
                    "body": null,
                    "headers": {},
                    "method": "GET",
                    "tor": {
                        "exit_ip": null,
                        "exit_name": null,
                        "is_tor": false
                    },
                    "url": "https://web.telegram.org/"
                },
                "response": null
            },
            {
                "failure": "connection_refused_error",
                "request": {
                    "body": null,
                    "headers": {},
                    "method": "GET",
                    "tor": {
                        "exit_ip": null,
                        "exit_name": null,
                        "is_tor": false
                    },
                    "url": "http://web.telegram.org/"
                },
                "response": null
            },
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
                    "url": "http://149.154.175.50:80"
                },
                "response": null
            },
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
                    "url": "http://149.154.175.50:443"
                },
                "response": null
            },
            {
                "failure": null,
                "request": {
                    "body": null,
                    "headers": {},
                    "method": "POST",
                    "tor": {
                        "exit_ip": null,
                        "exit_name": null,
                        "is_tor": false
                    },
                    "url": "http://149.154.167.51:80"
                },
                "response": {
                    "body": "<html>\r\n<head><title>501 Not Implemented</title></head>\r\n<body bgcolor=\"white\">\r\n<center><h1>501 Not Implemented</h1></center>\r\n<hr><center>nginx/0.3.33</center>\r\n</body>\r\n</html>\r\n",
                    "code": 501,
                    "headers": {
                        "Content-Type": "text/html",
                        "Date": "Fri, 07 Apr 2017 01:34:26 GMT",
                        "Server": "nginx/0.3.33"
                    }
                }
            }
        ],
        "socksproxy": null,
        "tcp_connect": [
            {
                "ip": "149.154.167.51",
                "port": 443,
                "status": {
                    "failure": false,
                    "success": true
                }
            },
            {
                "ip": "149.154.167.51",
                "port": 80,
                "status": {
                    "failure": false,
                    "success": true
                }
            },
            {
                "ip": "149.154.167.91",
                "port": 443,
                "status": {
                    "failure": false,
                    "success": true
                }
            },
            {
                "ip": "149.154.167.91",
                "port": 80,
                "status": {
                    "failure": false,
                    "success": true
                }
            },
            {
                "ip": "149.154.175.100",
                "port": 443,
                "status": {
                    "failure": false,
                    "success": true
                }
            },
            {
                "ip": "149.154.175.100",
                "port": 80,
                "status": {
                    "failure": false,
                    "success": true
                }
            },
            {
                "ip": "149.154.171.5",
                "port": 80,
                "status": {
                    "failure": false,
                    "success": true
                }
            },
            {
                "ip": "149.154.171.5",
                "port": 443,
                "status": {
                    "failure": false,
                    "success": true
                }
            },
            {
                "ip": "149.154.175.50",
                "port": 443,
                "status": {
                    "failure": "generic_timeout_error",
                    "success": false
                }
            },
            {
                "ip": "149.154.175.50",
                "port": 80,
                "status": {
                    "failure": "generic_timeout_error",
                    "success": false
                }
            }
        ],
        "telegram_http_blocking": false,
        "telegram_tcp_blocking": false,
        "telegram_web_failure": "connection_refused_error",
        "telegram_web_status": "blocked"
    },
    "test_name": "telegram",
    "test_runtime": 60.416918992996216,
    "test_start_time": "2017-04-07 01:33:25",
    "test_version": "0.3.0"
}
```

# Specification version number

2016-10-25-001

# Specification name

WhatsApp

# Test preconditions

* An internet connection

# Expected impact

Ability to detect if the WhatsApp instant messaging platform is working, by
checking if the DNS resolutions are consistent and if it's possible to
establish a TCP connection with the IPs of the endpoints.


# Expected inputs

None

# Test description

This test will check if 3 services are working as they should:

1. The whatsapp endpoints (the addresses used by the WhatsApp mobile client to work)

2. The registration service

3. The whatsapp web interface

## WhatsApp endpoints check

The WhatsApp endpoints are those used by the WhatsApp app to send and receive
messages.
These endpoints have the following hostnames:

* e1.whatsapp.net
* e2.whatsapp.net
* e3.whatsapp.net
* e4.whatsapp.net
* e5.whatsapp.net
* e6.whatsapp.net
* e7.whatsapp.net
* e8.whatsapp.net
* e9.whatsapp.net
* e10.whatsapp.net
* e11.whatsapp.net
* e12.whatsapp.net
* e13.whatsapp.net
* e14.whatsapp.net
* e15.whatsapp.net
* e16.whatsapp.net

When the `--all-endpoints` option is **not** specified we will be testing one
of this endpoints picked at random, while when that option is specified we
will be testing all of the ones listed above.

To check if they work properly we will first do a DNS A lookup to the
endpoint in question. We then check if any of the returned IPs (we ignore
anything that is not an IPv4 address, like a CNAME) are part of the address
space used by whatsapp.

As a reference point to know if a certain IP is part of the WhatsApp network
we use the list of IP blocks published by WhatsApp here:
https://www.whatsapp.com/cidr.txt.
The test contains a harcoded version of the cirdr list with a timestamp of when
it was last retrieved from the URL.

If any of the returned IPs are part of any network block listed in `cidr.txt`
we consider the DNS response to be consistent. If that is not the case we
consider the endpoint to be blocked and write in the report:

```json
{
    "whatsapp_endpoints_status": "blocked",
    "whatsapp_endpoints_dns_inconsistent": ["eN.whatsapp.net"]
}
```

For every IP, both consistent and inconsistent, we then try to establish a TCP session to port `443`
and `5222`.

For a given IP address we consider the connection successful if either connecting to `IP:443` or `IP:5222` succeeds.

If ANY of the connections to consistent endpoints (i.e. within the net blocks
assigned to WhatsApp) succeed then we consider the endpoint to not be
blocked.

Conversely if any attempts fail then we consider the endpoint to be blocked
and mark is as such in the report:

```json
{
    "whatsapp_endpoints_status": "blocked",
    "whatsapp_endpoints_blocked": ["eN.whatsapp.net"]
}
```

Note: Not every WhatsApp endpoint actually listens on both port `5222` and
`443` and the behavior of the whatsapp client it to attempt to connect to
both `5222` and `443` on each endpoint until it manages to connect.

## Registration service check

The registration service is used by WhatsApp to register a number to a
whatsapp account. As such blocking the registration service inhibits new
account creations.

The registration service is a `HTTPS` service at the following URL:
https://v.whatsapp.net/v2/register.

To check if it is working properly we do a HTTP GET request to
`https://v.whatsapp.net/v2/register` and if it succeeds we consider the
endpoint to be working and write in the report:

```json
{
    "registration_server_status": "ok",
    "registration_server_failure": null
}
```

When it fails we write:

```json
{
    "registration_server_status": "blocked",
    "registration_server_failure": "FAILURE STRING" 
}
```

## WhatApp web check

WhatsApp web is the service by which users are able to use WhatsApp from a
web browser on their computer.
When using WhatsApp web users scan a QR code displayed in the browser from
their phone to authenticate the web app.

For the service to work a user needs to have whatsapp be working properly
from their phone (it needs to be unblocked there) and if the "Keep me signed
in" option is unticked their phone needs to be connected to the internet and
be able to reach the whatsapp endpoints for the duration of the session.

We check to see if WhatsApp web is working properly by doing a HTTPS GET request to the following URLs:

* https://web.whatsapp.com/
* http://web.whatsapp.com/

If the HTTP(s) requests fail or the HTML `<title>` tag text is not "WhatsApp
Web" we consider the endpoint to be blocked.

If either one of the HTTP or HTTPS endpoints are blocked then we write in the
report:

```json
{
    "whatsapp_web_status": "blocked",
    "whatsapp_web_failure": "FAILURE STRING"
}
```

If none of the endpoints are blocked then we write:

```json
{
    "whatsapp_web_status": "ok",
    "whatsapp_web_failure": null
}
```

# Expected output

## Parent data format

* df-001-httpt

* df-002-dnst

## Semantics

```json
{
    "whatsapp_endpoints_status": "blocked" | "ok" | null,
    "whatsapp_endpoints_dns_inconsistent": ["e[1-16].whatsapp.net"],
    "whatsapp_endpoints_blocked": ["e[1-16].whatsapp.net"],

    "whatsapp_web_status": "blocked" | "ok" | null,
    "whatsapp_web_failure": "FAILURE STRING",

    "registration_server_status": "blocked" | "ok" | null,

    "registration_server_failure": "FAILURE STRING (since 0.5.0)",
    "registratison_server_failure": "FAILURE STRING (note: up until 0.4.0 name of the key was mispelled)",

    "tcp_connect": [
        {
            "ip": "xxx.xxx.xxx.xxx",
            "port": 5222 | 443,
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


* If it is possible for users to create new accounts via WhatsApp

* If it is possible for users to use whatsapp web

* If it is possible for users to use the WhatsApp software

## Example output sample

```json
{
    "annotations": {
        "platform": "macos"
    },
    "data_format_version": "0.2.0",
    "id": "3efd4e05-be03-46b7-a21d-034cb03bdde9",
    "input": null,
    "input_hashes": [],
    "measurement_start_time": "2016-11-25 12:33:30",
    "options": [],
    "probe_asn": "AS30722",
    "probe_cc": "IT",
    "probe_city": null,
    "probe_ip": "127.0.0.1",
    "report_id": "m2fUNCj20WEaAHZaiNBf1vIUFkytNqCLQboP0XJrSFPpDpy5me7tDfEaAQktPHDe",
    "software_name": "ooniprobe",
    "software_version": "2.0.3.dev0",
    "test_helpers": {},
    "test_keys": {
        "agent": "redirect",
        "queries": [
            {
                "answers": [
                    {
                        "answer_type": "A",
                        "ipv4": "169.47.5.199"
                    },
                    {
                        "answer_type": "A",
                        "ipv4": "174.36.208.132"
                    },
                    {
                        "answer_type": "A",
                        "ipv4": "173.192.231.41"
                    },
                    {
                        "answer_type": "A",
                        "ipv4": "174.37.217.84"
                    },
                    {
                        "answer_type": "A",
                        "ipv4": "169.45.214.245"
                    },
                    {
                        "answer_type": "A",
                        "ipv4": "169.45.219.230"
                    },
                    {
                        "answer_type": "A",
                        "ipv4": "169.45.248.175"
                    },
                    {
                        "answer_type": "A",
                        "ipv4": "169.45.248.107"
                    }
                ],
                "failure": null,
                "hostname": "e14.whatsapp.net",
                "query_type": "A",
                "resolver_hostname": null,
                "resolver_port": null
            }
        ],
        "registration_server_failure": null,
        "registration_server_status": "ok",
        "requests": [
            {
                "failure": null,
                "request": {
                    "body": null,
                    "headers": {},
                    "method": "GET",
                    "tor": {
                        "exit_ip": null,
                        "exit_name": null,
                        "is_tor": false
                    },
                    "url": "https://web.whatsapp.com/"
                },
                "response": {
                    "body": "<!DOCTYPE html>\n<!--[if lt IE 7]>      <html class=\"no-js lt-ie9 lt-ie8 lt-ie7\"> <![endif]-->\n<!--[if IE 7]>         <html class=\"no-js lt-ie9 lt-ie8\"> <![endif]-->\n<!--[if IE 8]>         <html class=\"no-js lt-ie9\"> <![endif]-->\n<!--[if gt IE 8]><!-->\n<html class=\"no-js\" dir=\"ltr\">\n<!--<![endif]-->\n\n<head>\n    <meta charset=\"utf-8\">\n    <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge,chrome=1\">\n    <title>WhatsApp Web</title>\n    <meta name=\"viewport\" content=\"width=device-width\">\n    <meta name=\"google\" content=\"notranslate\">\n\n    <meta name=\"description\" content=\"Quickly send and receive WhatsApp messages right from your computer.\"/>\n    <meta name=\"og:description\" content=\"Quickly send and receive WhatsApp messages right from your computer.\"/>\n    <meta name=\"og:url\" content=\"https://web.whatsapp.com/\"/>\n    <meta name=\"og:title\" content=\"WhatsApp Web\"/>\n    <meta name=\"og:image\" content=\"https://www.whatsapp.com/img/fb-post.jpg\"/>\n\n    <link id=\"favicon\" rel=\"icon\" href=\"/favicon.ico\" type=\"image/x-icon\" />\n    <link rel=\"stylesheet\" href=\"/browsers_15ddf4e13bd4ffb48b8b78ddbc6c0c27.css\">\n    <link href='//fonts.googleapis.com/css?family=Roboto:300,400' rel='stylesheet' type='text/css'>\n\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com\" hreflang=\"x-default\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/aa\" hreflang=\"aa\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/ar\" hreflang=\"ar\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/az\" hreflang=\"az\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/bg\" hreflang=\"bg\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/bn\" hreflang=\"bn\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/ca\" hreflang=\"ca\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/cs\" hreflang=\"cs\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/da\" hreflang=\"da\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/de\" hreflang=\"de\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/el\" hreflang=\"el\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/en\" hreflang=\"en\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/es\" hreflang=\"es\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/fa\" hreflang=\"fa\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/fi\" hreflang=\"fi\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/fil\" hreflang=\"fil\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/fr\" hreflang=\"fr\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/he\" hreflang=\"he\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/hi\" hreflang=\"hi\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/hr\" hreflang=\"hr\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/hu\" hreflang=\"hu\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/id\" hreflang=\"id\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/it\" hreflang=\"it\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/kk\" hreflang=\"kk\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/kn\" hreflang=\"kn\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/lt\" hreflang=\"lt\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/lv\" hreflang=\"lv\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/mk\" hreflang=\"mk\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/ml\" hreflang=\"ml\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/mr\" hreflang=\"mr\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/ms\" hreflang=\"ms\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/nb\" hreflang=\"nb\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/nl\" hreflang=\"nl\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/pl\" hreflang=\"pl\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/pt\" hreflang=\"pt\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/pt-br\" hreflang=\"pt-BR\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/ro\" hreflang=\"ro\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/ru\" hreflang=\"ru\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/sk\" hreflang=\"sk\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/sl\" hreflang=\"sl\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/sn\" hreflang=\"sn\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/sq\" hreflang=\"sq\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/sr\" hreflang=\"sr\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/sv\" hreflang=\"sv\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/sw\" hreflang=\"sw\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/ta\" hreflang=\"ta\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/th\" hreflang=\"th\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/tr\" hreflang=\"tr\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/uk\" hreflang=\"uk\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/ur\" hreflang=\"ur\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/uz\" hreflang=\"uz\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/vi\" hreflang=\"vi\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/zh-cn\" hreflang=\"zh-CN\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/zh-tw\" hreflang=\"zh-TW\">\n</head>\n\n<body>\n    <div class=\"app-wrapper\">\n        <div id=\"wrapper\">\n            <div id=\"window\">\n                <div class=\"window-body\">\n                    <div class=\"window-text\">\n                        <h1 class=\"window-title\">WhatsApp Web</h1>\n                        <div class=\"window-subtitle\">Send and receive WhatsApp messages right from your computer.</div>\n                        <div class=\"text-tip\">We recommend using WhatsApp with one of the following browsers:</div>\n                        <div class=\"browsers\">\n                            <div class=\"browser\">\n                                <a class=\"image\" href=\"http://www.google.com/chrome/\" target=\"_blank\">\n                                    <span class=\"icon-chrome\"></span>\n                                </a>\n                                <a href=\"http://www.google.com/chrome/\" class=\"browser-title\" target=\"_blank\">Google Chrome</a>\n                            </div>\n                            <div class=\"browser\">\n                                <a class=\"image\" href=\"http://www.firefox.com\" target=\"_blank\">\n                                    <span class=\"icon-firefox\"></span>\n                                </a>\n                                <a href=\"http://www.firefox.com\" class=\"browser-title\" target=\"_blank\">Mozilla Firefox</a>\n                            </div>\n                            <div class=\"browser\">\n                                <a class=\"image\" href=\"http://www.opera.com\" target=\"_blank\">\n                                    <span class=\"icon-opera\"></span>\n                                </a>\n                                <a href=\"http://www.opera.com\" class=\"browser-title\" target=\"_blank\">Opera</a>\n                            </div>\n                        </div>\n                        <div class=\"text-tip\">WhatsApp also supports:</div>\n                        <div class=\"browsers\">\n                            <div class=\"browser\">\n                                <a class=\"image\" href=\"https://www.microsoft.com/en-us/windows/microsoft-edge\" target=\"_blank\">\n                                    <span class=\"icon-edge\"></span>\n                                </a>\n                                <a href=\"https://www.microsoft.com/en-us/windows/microsoft-edge\" class=\"browser-title\" target=\"_blank\">Microsoft Edge</a>\n                            </div>\n                            <div class=\"browser browser-safari\">\n                                <a class=\"image\" href=\"https://support.apple.com/downloads/#safari\" target=\"_blank\">\n                                    <span class=\"icon-safari\"></span>\n                                </a>\n                                <a href=\"https://support.apple.com/downloads/#safari\" class=\"browser-title\" target=\"_blank\">Safari (MacOS 10.8+ Only)</a>\n                            </div>\n                        </div>\n                    </div>\n                </div>\n            </div>\n        </div>\n    </div>\n</body>\n\n</html>\n",
                    "code": 200,
                    "headers": {
                        "Cache-Control": "no-cache",
                        "Content-Security-Policy": "default-src 'self'; report-uri https://dyn.web.whatsapp.com/cspv; script-src 'self' 'unsafe-eval' https://ajax.googleapis.com; connect-src 'self' wss://*.web.whatsapp.com https://*.whatsapp.net https://dyn.web.whatsapp.com https://*.giphy.com https://*.tenor.co blob:; img-src * data: blob:; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src 'self' data: https://fonts.googleapis.com https://fonts.gstatic.com; media-src 'self' https://*.whatsapp.net https://*.giphy.com https://*.tenor.co blob: mediastream:; child-src 'self' blob:",
                        "Content-Type": "text/html; charset=UTF-8",
                        "Date": "Fri, 25 Nov 2016 12:33:30 GMT",
                        "Last-Modified": "Wed, 23 Nov 2016 22:52:39 GMT",
                        "Pragma": "no-cache",
                        "Server": "Yaws 2.0",
                        "Strict-Transport-Security": "max-age=15552000; includeSubDomains; preload",
                        "Vary": "Accept-Encoding, User-Agent, Accept-Language",
                        "Via": "HTTP/1.1 169.55.74.40:443 (fwdproxy2/152 66.220.156.103)",
                        "X-Connected-To": "169.55.74.40",
                        "X-Content-Type-Options": "nosniff",
                        "X-FB-IP-Type": "allowed",
                        "X-Frame-Options": "DENY"
                    }
                }
            },
            {
                "failure": null,
                "request": {
                    "body": null,
                    "headers": {},
                    "method": "GET",
                    "tor": {
                        "exit_ip": null,
                        "exit_name": null,
                        "is_tor": false
                    },
                    "url": "https://v.whatsapp.net/v2/register"
                },
                "response": {
                    "body": "{\"status\":\"fail\",\"reason\":\"missing_param\",\"param\":\"code\"}\n",
                    "code": 200,
                    "headers": {
                        "Content-Type": "text/json ; charset=utf-8",
                        "Date": "Fri, 25 Nov 2016 12:33:31 GMT",
                        "Server": "Yaws 2.0"
                    }
                }
            },
            {
                "failure": null,
                "request": {
                    "body": null,
                    "headers": {},
                    "method": "GET",
                    "tor": {
                        "exit_ip": null,
                        "exit_name": null,
                        "is_tor": false
                    },
                    "url": "https://web.whatsapp.com/"
                },
                "response": {
                    "body": "<!DOCTYPE html>\n<!--[if lt IE 7]>      <html class=\"no-js lt-ie9 lt-ie8 lt-ie7\"> <![endif]-->\n<!--[if IE 7]>         <html class=\"no-js lt-ie9 lt-ie8\"> <![endif]-->\n<!--[if IE 8]>         <html class=\"no-js lt-ie9\"> <![endif]-->\n<!--[if gt IE 8]><!-->\n<html class=\"no-js\" dir=\"ltr\">\n<!--<![endif]-->\n\n<head>\n    <meta charset=\"utf-8\">\n    <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge,chrome=1\">\n    <title>WhatsApp Web</title>\n    <meta name=\"viewport\" content=\"width=device-width\">\n    <meta name=\"google\" content=\"notranslate\">\n\n    <meta name=\"description\" content=\"Quickly send and receive WhatsApp messages right from your computer.\"/>\n    <meta name=\"og:description\" content=\"Quickly send and receive WhatsApp messages right from your computer.\"/>\n    <meta name=\"og:url\" content=\"https://web.whatsapp.com/\"/>\n    <meta name=\"og:title\" content=\"WhatsApp Web\"/>\n    <meta name=\"og:image\" content=\"https://www.whatsapp.com/img/fb-post.jpg\"/>\n\n    <link id=\"favicon\" rel=\"icon\" href=\"/favicon.ico\" type=\"image/x-icon\" />\n    <link rel=\"stylesheet\" href=\"/browsers_15ddf4e13bd4ffb48b8b78ddbc6c0c27.css\">\n    <link href='//fonts.googleapis.com/css?family=Roboto:300,400' rel='stylesheet' type='text/css'>\n\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com\" hreflang=\"x-default\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/aa\" hreflang=\"aa\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/ar\" hreflang=\"ar\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/az\" hreflang=\"az\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/bg\" hreflang=\"bg\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/bn\" hreflang=\"bn\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/ca\" hreflang=\"ca\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/cs\" hreflang=\"cs\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/da\" hreflang=\"da\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/de\" hreflang=\"de\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/el\" hreflang=\"el\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/en\" hreflang=\"en\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/es\" hreflang=\"es\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/fa\" hreflang=\"fa\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/fi\" hreflang=\"fi\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/fil\" hreflang=\"fil\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/fr\" hreflang=\"fr\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/he\" hreflang=\"he\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/hi\" hreflang=\"hi\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/hr\" hreflang=\"hr\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/hu\" hreflang=\"hu\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/id\" hreflang=\"id\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/it\" hreflang=\"it\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/kk\" hreflang=\"kk\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/kn\" hreflang=\"kn\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/lt\" hreflang=\"lt\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/lv\" hreflang=\"lv\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/mk\" hreflang=\"mk\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/ml\" hreflang=\"ml\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/mr\" hreflang=\"mr\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/ms\" hreflang=\"ms\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/nb\" hreflang=\"nb\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/nl\" hreflang=\"nl\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/pl\" hreflang=\"pl\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/pt\" hreflang=\"pt\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/pt-br\" hreflang=\"pt-BR\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/ro\" hreflang=\"ro\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/ru\" hreflang=\"ru\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/sk\" hreflang=\"sk\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/sl\" hreflang=\"sl\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/sn\" hreflang=\"sn\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/sq\" hreflang=\"sq\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/sr\" hreflang=\"sr\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/sv\" hreflang=\"sv\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/sw\" hreflang=\"sw\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/ta\" hreflang=\"ta\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/th\" hreflang=\"th\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/tr\" hreflang=\"tr\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/uk\" hreflang=\"uk\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/ur\" hreflang=\"ur\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/uz\" hreflang=\"uz\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/vi\" hreflang=\"vi\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/zh-cn\" hreflang=\"zh-CN\">\n    <link rel=\"alternate\" href=\"https://web.whatsapp.com/%F0%9F%8C%90/zh-tw\" hreflang=\"zh-TW\">\n</head>\n\n<body>\n    <div class=\"app-wrapper\">\n        <div id=\"wrapper\">\n            <div id=\"window\">\n                <div class=\"window-body\">\n                    <div class=\"window-text\">\n                        <h1 class=\"window-title\">WhatsApp Web</h1>\n                        <div class=\"window-subtitle\">Send and receive WhatsApp messages right from your computer.</div>\n                        <div class=\"text-tip\">We recommend using WhatsApp with one of the following browsers:</div>\n                        <div class=\"browsers\">\n                            <div class=\"browser\">\n                                <a class=\"image\" href=\"http://www.google.com/chrome/\" target=\"_blank\">\n                                    <span class=\"icon-chrome\"></span>\n                                </a>\n                                <a href=\"http://www.google.com/chrome/\" class=\"browser-title\" target=\"_blank\">Google Chrome</a>\n                            </div>\n                            <div class=\"browser\">\n                                <a class=\"image\" href=\"http://www.firefox.com\" target=\"_blank\">\n                                    <span class=\"icon-firefox\"></span>\n                                </a>\n                                <a href=\"http://www.firefox.com\" class=\"browser-title\" target=\"_blank\">Mozilla Firefox</a>\n                            </div>\n                            <div class=\"browser\">\n                                <a class=\"image\" href=\"http://www.opera.com\" target=\"_blank\">\n                                    <span class=\"icon-opera\"></span>\n                                </a>\n                                <a href=\"http://www.opera.com\" class=\"browser-title\" target=\"_blank\">Opera</a>\n                            </div>\n                        </div>\n                        <div class=\"text-tip\">WhatsApp also supports:</div>\n                        <div class=\"browsers\">\n                            <div class=\"browser\">\n                                <a class=\"image\" href=\"https://www.microsoft.com/en-us/windows/microsoft-edge\" target=\"_blank\">\n                                    <span class=\"icon-edge\"></span>\n                                </a>\n                                <a href=\"https://www.microsoft.com/en-us/windows/microsoft-edge\" class=\"browser-title\" target=\"_blank\">Microsoft Edge</a>\n                            </div>\n                            <div class=\"browser browser-safari\">\n                                <a class=\"image\" href=\"https://support.apple.com/downloads/#safari\" target=\"_blank\">\n                                    <span class=\"icon-safari\"></span>\n                                </a>\n                                <a href=\"https://support.apple.com/downloads/#safari\" class=\"browser-title\" target=\"_blank\">Safari (MacOS 10.8+ Only)</a>\n                            </div>\n                        </div>\n                    </div>\n                </div>\n            </div>\n        </div>\n    </div>\n</body>\n\n</html>\n",
                    "code": 200,
                    "headers": {
                        "Cache-Control": "no-cache",
                        "Content-Security-Policy": "default-src 'self'; report-uri https://dyn.web.whatsapp.com/cspv; script-src 'self' 'unsafe-eval' https://ajax.googleapis.com; connect-src 'self' wss://*.web.whatsapp.com https://*.whatsapp.net https://dyn.web.whatsapp.com https://*.giphy.com https://*.tenor.co blob:; img-src * data: blob:; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src 'self' data: https://fonts.googleapis.com https://fonts.gstatic.com; media-src 'self' https://*.whatsapp.net https://*.giphy.com https://*.tenor.co blob: mediastream:; child-src 'self' blob:",
                        "Content-Type": "text/html; charset=UTF-8",
                        "Date": "Fri, 25 Nov 2016 12:33:31 GMT",
                        "Last-Modified": "Wed, 23 Nov 2016 22:52:39 GMT",
                        "Pragma": "no-cache",
                        "Server": "Yaws 2.0",
                        "Strict-Transport-Security": "max-age=15552000; includeSubDomains; preload",
                        "Vary": "Accept-Encoding, User-Agent, Accept-Language",
                        "Via": "HTTP/1.1 169.55.74.40:443 (fwdproxy2/152 66.220.156.113)",
                        "X-Connected-To": "169.55.74.40",
                        "X-Content-Type-Options": "nosniff",
                        "X-FB-IP-Type": "allowed",
                        "X-Frame-Options": "DENY"
                    }
                }
            },
            {
                "failure": null,
                "request": {
                    "body": null,
                    "headers": {},
                    "method": "GET",
                    "tor": {
                        "exit_ip": null,
                        "exit_name": null,
                        "is_tor": false
                    },
                    "url": "http://web.whatsapp.com/"
                },
                "response": {
                    "body": null,
                    "code": 302,
                    "headers": {
                        "Content-Type": "text/plain",
                        "Date": "Fri, 25 Nov 2016 12:33:30 GMT",
                        "Location": "https://web.whatsapp.com/",
                        "Server": "proxygen"
                    }
                }
            }
        ],
        "socksproxy": null,
        "tcp_connect": [
            {
                "ip": "173.192.231.41",
                "port": 443,
                "status": {
                    "failure": false,
                    "success": true
                }
            },
            {
                "ip": "169.45.214.245",
                "port": 443,
                "status": {
                    "failure": false,
                    "success": true
                }
            },
            {
                "ip": "169.45.248.107",
                "port": 443,
                "status": {
                    "failure": false,
                    "success": true
                }
            },
            {
                "ip": "169.47.5.199",
                "port": 443,
                "status": {
                    "failure": false,
                    "success": true
                }
            },
            {
                "ip": "174.37.217.84",
                "port": 443,
                "status": {
                    "failure": false,
                    "success": true
                }
            },
            {
                "ip": "174.36.208.132",
                "port": 443,
                "status": {
                    "failure": false,
                    "success": true
                }
            },
            {
                "ip": "169.45.219.230",
                "port": 443,
                "status": {
                    "failure": false,
                    "success": true
                }
            },
            {
                "ip": "169.45.248.175",
                "port": 443,
                "status": {
                    "failure": false,
                    "success": true
                }
            },
            {
                "ip": "169.45.214.245",
                "port": 5222,
                "status": {
                    "failure": false,
                    "success": true
                }
            },
            {
                "ip": "169.45.248.107",
                "port": 5222,
                "status": {
                    "failure": false,
                    "success": true
                }
            },
            {
                "ip": "169.47.5.199",
                "port": 5222,
                "status": {
                    "failure": false,
                    "success": true
                }
            },
            {
                "ip": "169.45.219.230",
                "port": 5222,
                "status": {
                    "failure": false,
                    "success": true
                }
            },
            {
                "ip": "173.192.231.41",
                "port": 5222,
                "status": {
                    "failure": false,
                    "success": true
                }
            },
            {
                "ip": "174.37.217.84",
                "port": 5222,
                "status": {
                    "failure": false,
                    "success": true
                }
            },
            {
                "ip": "169.45.248.175",
                "port": 5222,
                "status": {
                    "failure": false,
                    "success": true
                }
            },
            {
                "ip": "174.36.208.132",
                "port": 5222,
                "status": {
                    "failure": false,
                    "success": true
                }
            }
        ],
        "whatsapp_endpoints_blocked": [],
        "whatsapp_endpoints_dns_inconsistent": [],
        "whatsapp_endpoints_status": "ok",
        "whatsapp_web_failure": null,
        "whatsapp_web_status": "ok"
    },
    "test_name": "whatsapp",
    "test_runtime": 0.7117400169372559,
    "test_start_time": "2016-11-25 12:33:30",
    "test_version": "0.5.0"
}
```

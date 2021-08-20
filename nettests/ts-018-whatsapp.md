# Specification version number

2020-07-09-002

* _status_: current

# Specification name

WhatsApp

# Test preconditions

* An internet connection

# Expected impact

Ability to detect whether specific services used by WhatsApp are
accessible and working as intended. Even if this test does not detect
any issue, WhatsApp may still be blocked in more complex ways.

# Expected inputs

None

# Test description

This test will check if 3 services are working as they should:

1. The whatsapp endpoints used by the WhatsApp mobile app;

2. The registration service, i.e. the service used to register a new account;

3. The WhatsApp web interface.

## WhatsApp endpoints check

The WhatsApp endpoints are those used by the WhatsApp app to send and receive
messages. These endpoints have the following hostnames:

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

The behaviour of the WhatsApp app is to attempt to connect to each of the
following hostnames on ports 443 and 5222 until one succeeds. A previous
version of this specification checked only just one of the above endpoints,
but since 2020-07-09 we check all the endpoints on ports 443 and 5222.

We lookup every domain name and record the ASN of each returned IP, deferring to
OONI data processing pipeline to determine whether the IP is legitimate.

If we can connect to at least one endpoint, we set:

```JSON
{
    "whatsapp_endpoints_status": "ok",
}
```

If all endpoints fail, we set:

```JSON
{
    "whatsapp_endpoints_status": "blocked",
}
```

Therefore, this specific key tells us whether the WhatsApp would work by
attempting with each of the hardcoded endpoints on ports 443 and 5222.

As of 2020-07-09, all endpoints work with ports 443 and 5222 from an
unfiltered network connection. If an endpoint fails for both ports, then
we consider it blocked and we add it to the list of blocked endpoints
as follows:

```JSON
{
    "whatsapp_endpoints_blocked": [
        "e1.whatsapp.net"
    ]
}
```

If only a single port of an endpoint fails, we do not include the
endpoint in the list of blocked endpoints. (This specific choice
retains backwards compatibility with previous versions of this spec.)

If all endpoints work for at least one port, we simply do not
insert any endpoint inside the list, as follows:

```JSON
{
    "whatsapp_endpoints_blocked": []
}
```

We always additionally write into the report:

```JSON
{
    "whatsapp_endpoints_dns_inconsistent": []
}
```

The `whatsapp_endpoints_dns_inconsistent` key is a legacy key that we
used to compute whether an endpoint was part of the WhatsApp address
space, but this check has been broken since at least 2020-02-17, so we
first disabled the check and then updated the spec to not mention it.

## Registration service check

The registration service is used by WhatsApp to register a number to a
whatsapp account. As such blocking the registration service inhibits new
account creations.

The registration service is a `HTTPS` service at the following URL:
https://v.whatsapp.net/v2/register.

To check if it is working properly we do a HTTP GET request to
`https://v.whatsapp.net/v2/register`. We conside this request to
be successful if we don't see any DNS, TCP connect, TLS, or I/O
error. We don't rely on the HTTP status code to determine whether
this request succeeded, because we assume it is enough to determine
whether we could have an HTTPS conversation with this service.

If there is no failure, we write in the report:

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
web browser on their computer. When using WhatsApp web users scan a QR code
displayed in the browser from their phone to authenticate the web app.

For the service to work a user needs to have whatsapp be working properly
from their phone (it needs to be unblocked there) and if the "Keep me signed
in" option is unticked their phone needs to be connected to the internet and
be able to reach the whatsapp endpoints for the duration of the session.

We check to see if WhatsApp web is working properly by doing a HTTPS GET request
to the following URLs:

* https://web.whatsapp.com/

* http://web.whatsapp.com/

We consider the GET for the HTTPS URL successful if we do not see any
DNS, TCP connect, TLS, or I/O errors when fetching the URL. WhatsApp may
return an 400 Bad Request response if the User-Agent header we use does
not seem to be consistent with our ClientHello.

The GET for the HTTP URL should not follow redirects. We consider it
successful if the response redirects us to the HTTPS URL.

If either one of the HTTP or HTTPS endpoints are blocked then we write
in the report:

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

* df-005-tcpconnect

* df-006-tlshandshake

* df-008-netevents

* df-009-tunnel

## Semantics

The `test_keys` emitted by this nettest include the following keys:

```JSON
{
    "network_events": [],
    "queries": [],
    "requests": [],
    "tcp_connect": [],
    "tls_handshakes": [],

    "registration_server_failure": null,
    "registration_server_status": "ok",
    "whatsapp_endpoints_blocked": [],
    "whatsapp_endpoints_dns_inconsistent": [],
    "whatsapp_endpoints_status": "ok",
    "whatsapp_web_failure": null,
    "whatsapp_web_status": "ok"
}
```

where:

- `network_events` (`[]NetworkEvent`; nullable): see `df-008-netevents`;

- `queries` (`[]Query`; nullable): see `df-002-dnst`;

- `requests` (`[]Transaction`; nullable): see `df-001-httpt`;

- `tcp_connect` (`[]TCPConnect`; nullable): see `df-005-tcpconnect`;

- `tls_handshakes` (`[]Handshake`; nullable): see `df-006-tlshandshake`;

- `registration_server_failure` (`string`; nullable): the failure when
accessing the registration server (see `df-007-errors.md`);

- `registration_server_status` (`string`): one of `"ok"` and `"blocked"`;

- `whatsapp_endpoints_blocked` (`[]string`): list of blocked endpoints;

- `whatsapp_endpoints_dns_inconsistent` (`[]string`): legacy key
that is always empty;

- `whatsapp_endpoints_status` (`string`): one of `"ok"` and `"blocked"`;

- `whatsapp_web_failure` (`string`; nullable): the failure when
accessing the WhatsApp web interface (see `df-007-errors.md`);

- `whatsapp_web_status` (`string`): one of `"ok"` and `"blocked"`.

## Possible conclusions

* If it is possible for users to create new accounts via WhatsApp

* If it is possible for users to use whatsapp web

* If it is possible for users to use the WhatsApp software

## Example output sample

```json
{
  "annotations": {
    "assets_version": "20200619115947",
    "engine_name": "ooniprobe-engine",
    "engine_version": "0.14.0",
    "platform": "macos"
  },
  "data_format_version": "0.2.0",
  "extensions": {
    "dnst": 0,
    "httpt": 0,
    "netevents": 0,
    "tlshandshake": 0,
    "tunnel": 0
  },
  "input": null,
  "measurement_start_time": "2020-07-09 11:02:41",
  "probe_asn": "AS30722",
  "probe_cc": "IT",
  "probe_ip": "127.0.0.1",
  "probe_network_name": "Vodafone Italia S.p.A.",
  "report_id": "20200709T110241Z_AS30722_CIaQmE3CBdzrf1oIh7F3DwALQtjl4PrTaQxXlsNP7C011453ea",
  "resolver_asn": "AS30722",
  "resolver_ip": "91.80.36.84",
  "resolver_network_name": "Vodafone Italia S.p.A.",
  "software_name": "miniooni",
  "software_version": "0.14.0",
  "test_keys": {
    "agent": "redirect",
    "failed_operation": null,
    "failure": null,
    "network_events": [
      {
        "failure": null,
        "operation": "http_transaction_start",
        "t": 0.001153697
      },
      {
        "failure": null,
        "operation": "http_request_metadata",
        "t": 0.001157765
      },
      {
        "failure": null,
        "operation": "resolve_start",
        "t": 0.001227361
      },
      {
        "failure": null,
        "operation": "resolve_done",
        "t": 0.055199778
      },
      {
        "address": "69.171.250.60:443",
        "failure": null,
        "operation": "connect",
        "proto": "tcp",
        "t": 0.079603245
      },
      {
        "failure": null,
        "operation": "tls_handshake_start",
        "t": 0.079654268
      },
      {
        "failure": null,
        "num_bytes": 286,
        "operation": "write",
        "t": 0.079957156
      },
      {
        "failure": null,
        "num_bytes": 517,
        "operation": "read",
        "t": 0.104859831
      },
      {
        "failure": null,
        "num_bytes": 1800,
        "operation": "read",
        "t": 0.105431746
      },
      {
        "failure": null,
        "num_bytes": 747,
        "operation": "read",
        "t": 0.105475141
      },
      {
        "failure": null,
        "num_bytes": 64,
        "operation": "write",
        "t": 0.107882362
      },
      {
        "failure": null,
        "operation": "tls_handshake_done",
        "t": 0.107907192
      },
      {
        "failure": null,
        "num_bytes": 86,
        "operation": "write",
        "t": 0.108139396
      },
      {
        "failure": null,
        "num_bytes": 206,
        "operation": "write",
        "t": 0.109137636
      },
      {
        "failure": null,
        "operation": "http_wrote_headers",
        "t": 0.109141745
      },
      {
        "failure": null,
        "operation": "http_wrote_request",
        "t": 0.109142604
      },
      {
        "failure": null,
        "num_bytes": 74,
        "operation": "read",
        "t": 0.131422583
      },
      {
        "failure": null,
        "num_bytes": 31,
        "operation": "write",
        "t": 0.131530094
      },
      {
        "failure": null,
        "num_bytes": 31,
        "operation": "read",
        "t": 0.132357428
      },
      {
        "failure": null,
        "num_bytes": 35,
        "operation": "read",
        "t": 0.134856016
      },
      {
        "failure": null,
        "num_bytes": 1388,
        "operation": "read",
        "t": 0.178145709
      },
      {
        "failure": null,
        "num_bytes": 383,
        "operation": "read",
        "t": 0.178193064
      },
      {
        "failure": null,
        "operation": "http_first_response_byte",
        "t": 0.178348521
      },
      {
        "failure": null,
        "operation": "http_response_metadata",
        "t": 0.178471921
      },
      {
        "failure": null,
        "operation": "http_response_body_snapshot",
        "t": 0.178485775
      },
      {
        "failure": null,
        "operation": "http_transaction_done",
        "t": 0.178486692
      },
      {
        "failure": null,
        "num_bytes": 24,
        "operation": "write",
        "t": 0.178593354
      },
      {
        "failure": null,
        "operation": "resolve_start",
        "t": 0.001173242
      },
      {
        "failure": null,
        "operation": "resolve_done",
        "t": 0.093193011
      },
      {
        "address": "34.194.71.217:443",
        "failure": null,
        "operation": "connect",
        "proto": "tcp",
        "t": 0.207018418
      },
      {
        "failure": null,
        "operation": "http_transaction_start",
        "t": 0.179558692
      },
      {
        "failure": null,
        "operation": "http_request_metadata",
        "t": 0.179570108
      },
      {
        "failure": null,
        "operation": "resolve_start",
        "t": 0.180708632
      },
      {
        "failure": null,
        "operation": "resolve_done",
        "t": 0.182215501
      },
      {
        "address": "69.171.250.60:80",
        "failure": null,
        "operation": "connect",
        "proto": "tcp",
        "t": 0.207763367
      },
      {
        "failure": null,
        "operation": "http_wrote_headers",
        "t": 0.208031246
      },
      {
        "failure": null,
        "operation": "http_wrote_request",
        "t": 0.208033326
      },
      {
        "failure": null,
        "num_bytes": 282,
        "operation": "write",
        "t": 0.208117192
      },
      {
        "failure": null,
        "num_bytes": 242,
        "operation": "read",
        "t": 0.232560865
      },
      {
        "failure": null,
        "operation": "http_first_response_byte",
        "t": 0.232572517
      },
      {
        "failure": null,
        "operation": "http_response_metadata",
        "t": 0.232644304
      },
      {
        "failure": null,
        "operation": "http_response_body_snapshot",
        "t": 0.23266589
      },
      {
        "failure": null,
        "operation": "http_transaction_done",
        "t": 0.232666803
      },
      {
        "failure": null,
        "operation": "http_transaction_start",
        "t": 0.001150339
      },
      {
        "failure": null,
        "operation": "http_request_metadata",
        "t": 0.00115765
      },
      {
        "failure": null,
        "operation": "resolve_start",
        "t": 0.001227368
      },
      {
        "failure": null,
        "operation": "resolve_done",
        "t": 0.071238074
      },
      {
        "address": "69.171.250.60:443",
        "failure": null,
        "operation": "connect",
        "proto": "tcp",
        "t": 0.096787583
      },
      {
        "failure": null,
        "operation": "tls_handshake_start",
        "t": 0.096826301
      },
      {
        "failure": null,
        "num_bytes": 284,
        "operation": "write",
        "t": 0.097124463
      },
      {
        "failure": null,
        "num_bytes": 517,
        "operation": "read",
        "t": 0.122612789
      },
      {
        "failure": null,
        "num_bytes": 1800,
        "operation": "read",
        "t": 0.122967996
      },
      {
        "failure": null,
        "num_bytes": 747,
        "operation": "read",
        "t": 0.12299006
      },
      {
        "failure": null,
        "num_bytes": 64,
        "operation": "write",
        "t": 0.124585528
      },
      {
        "failure": null,
        "operation": "tls_handshake_done",
        "t": 0.124645709
      },
      {
        "failure": null,
        "num_bytes": 86,
        "operation": "write",
        "t": 0.124800198
      },
      {
        "failure": null,
        "num_bytes": 214,
        "operation": "write",
        "t": 0.125082793
      },
      {
        "failure": null,
        "operation": "http_wrote_headers",
        "t": 0.125085502
      },
      {
        "failure": null,
        "operation": "http_wrote_request",
        "t": 0.125086283
      },
      {
        "failure": null,
        "num_bytes": 74,
        "operation": "read",
        "t": 0.14885878
      },
      {
        "failure": null,
        "num_bytes": 31,
        "operation": "write",
        "t": 0.148993236
      },
      {
        "failure": null,
        "num_bytes": 44,
        "operation": "read",
        "t": 0.1490235
      },
      {
        "failure": null,
        "num_bytes": 161,
        "operation": "read",
        "t": 0.630222125
      },
      {
        "failure": null,
        "operation": "http_first_response_byte",
        "t": 0.630348977
      },
      {
        "failure": null,
        "operation": "http_response_metadata",
        "t": 0.63050614
      },
      {
        "failure": null,
        "operation": "http_response_body_snapshot",
        "t": 0.630518627
      },
      {
        "failure": null,
        "operation": "http_transaction_done",
        "t": 0.630519479
      },
      {
        "failure": null,
        "num_bytes": 24,
        "operation": "write",
        "t": 0.630606143
      }
    ],
    "queries": [
      {
        "answers": [
          {
            "asn": 32934,
            "as_org_name": "Facebook, Inc.",
            "answer_type": "A",
            "ipv4": "69.171.250.60",
            "ttl": null
          }
        ],
        "engine": "system",
        "failure": null,
        "hostname": "web.whatsapp.com",
        "query_type": "A",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "",
        "t": 0.055199778
      },
      {
        "answers": [
          {
            "asn": 32934,
            "as_org_name": "Facebook, Inc.",
            "answer_type": "AAAA",
            "ipv6": "2a03:2880:f2ff:c0:face:b00c:0:167",
            "ttl": null
          }
        ],
        "engine": "system",
        "failure": null,
        "hostname": "web.whatsapp.com",
        "query_type": "AAAA",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "",
        "t": 0.055199778
      },
      {
        "answers": [
          {
            "asn": 14618,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "34.194.71.217",
            "ttl": null
          },
          {
            "asn": 14618,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "34.192.181.12",
            "ttl": null
          },
          {
            "asn": 14618,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "34.194.255.230",
            "ttl": null
          },
          {
            "asn": 14618,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "34.193.38.112",
            "ttl": null
          }
        ],
        "engine": "system",
        "failure": null,
        "hostname": "e3.whatsapp.net",
        "query_type": "A",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "",
        "t": 0.093193011
      },
      {
        "answers": [
          {
            "asn": 32934,
            "as_org_name": "Facebook, Inc.",
            "answer_type": "A",
            "ipv4": "69.171.250.60",
            "ttl": null
          }
        ],
        "engine": "system",
        "failure": null,
        "hostname": "web.whatsapp.com",
        "query_type": "A",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "",
        "t": 0.182215501
      },
      {
        "answers": [
          {
            "asn": 32934,
            "as_org_name": "Facebook, Inc.",
            "answer_type": "AAAA",
            "ipv6": "2a03:2880:f2ff:c0:face:b00c:0:167",
            "ttl": null
          }
        ],
        "engine": "system",
        "failure": null,
        "hostname": "web.whatsapp.com",
        "query_type": "AAAA",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "",
        "t": 0.182215501
      },
      {
        "answers": [
          {
            "asn": 32934,
            "as_org_name": "Facebook, Inc.",
            "answer_type": "A",
            "ipv4": "69.171.250.60",
            "ttl": null
          }
        ],
        "engine": "system",
        "failure": null,
        "hostname": "v.whatsapp.net",
        "query_type": "A",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "",
        "t": 0.071238074
      },
      {
        "answers": [
          {
            "asn": 32934,
            "as_org_name": "Facebook, Inc.",
            "answer_type": "AAAA",
            "ipv6": "2a03:2880:f2ff:c0:face:b00c:0:167",
            "ttl": null
          }
        ],
        "engine": "system",
        "failure": null,
        "hostname": "v.whatsapp.net",
        "query_type": "AAAA",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "",
        "t": 0.071238074
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
              "User-Agent",
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
            ],
            [
              "Host",
              "web.whatsapp.com"
            ]
          ],
          "headers": {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US;q=0.8,en;q=0.5",
            "Host": "web.whatsapp.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
          },
          "method": "GET",
          "tor": {
            "exit_ip": null,
            "exit_name": null,
            "is_tor": false
          },
          "url": "https://web.whatsapp.com/"
        },
        "response": {
          "body": "<!DOCTYPE html><html lang=\"en\" id=\"facebook\"><head><title>Error</title><meta charset=\"utf-8\" /><meta http-equiv=\"Cache-Control\" content=\"no-cache\" /><meta name=\"robots\" content=\"noindex,nofollow\" /><style nonce=\"vfG4CTtZ\">html, body { color: #333; font-family: 'Lucida Grande', 'Tahoma', 'Verdana', 'Arial', sans-serif; margin: 0; padding: 0; text-align: center;}\n#header { height: 30px; padding-bottom: 10px; padding-top: 10px; text-align: center;}\n#icon { width: 30px;}\n.core { margin: auto; padding: 1em 0; text-align: left; width: 904px;}\nh1 { font-size: 18px;}\np { font-size: 13px;}\n.footer { border-top: 1px solid #ddd; color: #777; float: left; font-size: 11px; padding: 5px 8px 6px 0; width: 904px;}</style></head><body><div id=\"header\"><a href=\"//www.facebook.com/\"><img id=\"icon\" src=\"//static.facebook.com/images/logos/facebook_2x.png\" /></a></div><div class=\"core\"><h1>Sorry, something went wrong.</h1><p>We&#039;re working on getting this fixed as soon as we can.</p><p><a id=\"back\" href=\"//www.facebook.com/\">Go Back</a></p><div class=\"footer\"> Facebook &#169; 2020 &#183; <a href=\"//www.facebook.com/help/\">Help</a></div></div><script nonce=\"vfG4CTtZ\">\n              document.getElementById(\"back\").onclick = function() {\n                if (history.length > 1) {\n                  history.back();\n                  return false;\n                }\n              };\n            </script></body></html><!-- @generated SignedSource<<2baec119ad3d09b22a5215de1d307cd9>> -->",
          "body_is_truncated": false,
          "code": 400,
          "headers_list": [
            [
              "Vary",
              "Accept-Encoding"
            ],
            [
              "Strict-Transport-Security",
              "max-age=31536000; preload; includeSubDomains"
            ],
            [
              "Content-Type",
              "text/html; charset=\"utf-8\""
            ],
            [
              "X-Fb-Debug",
              "z3AxVIx+0nZtvAcEP3QZkA1QTPOskCJ1GgdHzsMWzfE6l5KOFww4dfZCcEwn9dWXMjVHu6sTcNZwFI0zBsRt5Q=="
            ],
            [
              "Content-Length",
              "1483"
            ],
            [
              "Date",
              "Thu, 09 Jul 2020 11:02:41 GMT"
            ],
            [
              "Alt-Svc",
              "h3-29=\":443\"; ma=3600,h3-27=\":443\"; ma=3600"
            ]
          ],
          "headers": {
            "Alt-Svc": "h3-29=\":443\"; ma=3600,h3-27=\":443\"; ma=3600",
            "Content-Length": "1483",
            "Content-Type": "text/html; charset=\"utf-8\"",
            "Date": "Thu, 09 Jul 2020 11:02:41 GMT",
            "Strict-Transport-Security": "max-age=31536000; preload; includeSubDomains",
            "Vary": "Accept-Encoding",
            "X-Fb-Debug": "z3AxVIx+0nZtvAcEP3QZkA1QTPOskCJ1GgdHzsMWzfE6l5KOFww4dfZCcEwn9dWXMjVHu6sTcNZwFI0zBsRt5Q=="
          }
        },
        "t": 0.001153697
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
              "User-Agent",
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
            ],
            [
              "Host",
              "web.whatsapp.com"
            ]
          ],
          "headers": {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US;q=0.8,en;q=0.5",
            "Host": "web.whatsapp.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
          },
          "method": "GET",
          "tor": {
            "exit_ip": null,
            "exit_name": null,
            "is_tor": false
          },
          "url": "http://web.whatsapp.com/"
        },
        "response": {
          "body": "",
          "body_is_truncated": false,
          "code": 302,
          "headers_list": [
            [
              "Location",
              "https://web.whatsapp.com/"
            ],
            [
              "Content-Type",
              "text/plain"
            ],
            [
              "Server",
              "proxygen-bolt"
            ],
            [
              "Date",
              "Thu, 09 Jul 2020 11:02:41 GMT"
            ],
            [
              "Alt-Svc",
              "h3-29=\":443\"; ma=3600,h3-27=\":443\"; ma=3600"
            ],
            [
              "Connection",
              "keep-alive"
            ],
            [
              "Content-Length",
              "0"
            ]
          ],
          "headers": {
            "Alt-Svc": "h3-29=\":443\"; ma=3600,h3-27=\":443\"; ma=3600",
            "Connection": "keep-alive",
            "Content-Length": "0",
            "Content-Type": "text/plain",
            "Date": "Thu, 09 Jul 2020 11:02:41 GMT",
            "Location": "https://web.whatsapp.com/",
            "Server": "proxygen-bolt"
          }
        },
        "t": 0.179558692
      },
      {
        "failure": null,
        "request": {
          "body": "",
          "body_is_truncated": false,
          "headers_list": [
            [
              "User-Agent",
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
            ],
            [
              "Host",
              "v.whatsapp.net"
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
            "Host": "v.whatsapp.net",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
          },
          "method": "GET",
          "tor": {
            "exit_ip": null,
            "exit_name": null,
            "is_tor": false
          },
          "url": "https://v.whatsapp.net/v2/register"
        },
        "response": {
          "body": "{\"status\":\"fail\",\"reason\":\"missing_param\",\"param\":\"authkey\"}\n",
          "body_is_truncated": false,
          "code": 200,
          "headers_list": [
            [
              "Server",
              "Yaws 2.0.6"
            ],
            [
              "Date",
              "Thu, 09 Jul 2020 11:02:41 GMT"
            ],
            [
              "Content-Length",
              "61"
            ],
            [
              "Content-Type",
              "text/json ; charset=utf-8"
            ]
          ],
          "headers": {
            "Content-Length": "61",
            "Content-Type": "text/json ; charset=utf-8",
            "Date": "Thu, 09 Jul 2020 11:02:41 GMT",
            "Server": "Yaws 2.0.6"
          }
        },
        "t": 0.001150339
      }
    ],
    "tcp_connect": [
      {
        "ip": "69.171.250.60",
        "port": 443,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.079603245
      },
      {
        "ip": "34.194.71.217",
        "port": 443,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.207018418
      },
      {
        "ip": "69.171.250.60",
        "port": 80,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.207763367
      },
      {
        "ip": "69.171.250.60",
        "port": 443,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.096787583
      }
    ],
    "tls_handshakes": [
      {
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
            "data": "MIIEsTCCA5mgAwIBAgIQBOHnpNxc8vNtwCtCuF0VnzANBgkqhkiG9w0BAQsFADBsMQswCQYDVQQGEwJVUzEVMBMGA1UEChMMRGlnaUNlcnQgSW5jMRkwFwYDVQQLExB3d3cuZGlnaWNlcnQuY29tMSswKQYDVQQDEyJEaWdpQ2VydCBIaWdoIEFzc3VyYW5jZSBFViBSb290IENBMB4XDTEzMTAyMjEyMDAwMFoXDTI4MTAyMjEyMDAwMFowcDELMAkGA1UEBhMCVVMxFTATBgNVBAoTDERpZ2lDZXJ0IEluYzEZMBcGA1UECxMQd3d3LmRpZ2ljZXJ0LmNvbTEvMC0GA1UEAxMmRGlnaUNlcnQgU0hBMiBIaWdoIEFzc3VyYW5jZSBTZXJ2ZXIgQ0EwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQC24C/CJAbIbQRf1+8KZAayfSImZRauQkCbztyfn3YHPsMwVYcZuU+UDlqUH1VWtMICKq/QmO4LQNfE0DtyyBSe75CxEamu0si4QzrZCwvV1ZX1QK/IHe1NnF9Xt4ZQaJn1itrSxwUfqJfJ3KSxgoQtxq2lnMcZgqaFD15EWCo3j/018QsIJzJa9buLnqS9UdAn4t07QjOjBSjEuyjMmqwrIw14xnvmXnG3Sj4I+4G3FhahnSMSTeXXkgisdaScus0Xsh5ENWV/UyU50RwKmmMbGZJ0aAo3wsJSSMs5WqK24V3B3aAguCGikyZvFEohQcftbZvySC/zA/WiaJJTL17jAgMBAAGjggFJMIIBRTASBgNVHRMBAf8ECDAGAQH/AgEAMA4GA1UdDwEB/wQEAwIBhjAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwNAYIKwYBBQUHAQEEKDAmMCQGCCsGAQUFBzABhhhodHRwOi8vb2NzcC5kaWdpY2VydC5jb20wSwYDVR0fBEQwQjBAoD6gPIY6aHR0cDovL2NybDQuZGlnaWNlcnQuY29tL0RpZ2lDZXJ0SGlnaEFzc3VyYW5jZUVWUm9vdENBLmNybDA9BgNVHSAENjA0MDIGBFUdIAAwKjAoBggrBgEFBQcCARYcaHR0cHM6Ly93d3cuZGlnaWNlcnQuY29tL0NQUzAdBgNVHQ4EFgQUUWj/kK8CB3U8zNllZGKiErhZcjswHwYDVR0jBBgwFoAUsT7DaQP4v0cB1JgmGggC72NkK8MwDQYJKoZIhvcNAQELBQADggEBABiKlYkD5m3fXPwdaOpKj4PWUS+Na0QWnqxj9dJubISZi6qBcYRb7TROsLd5kinMLYBq8I4g4Xmk/gNHE+r1hspZcX30BJZr01lYPf7TMSVcGDiEo+afgv2MW5gxTs14nhr9hctJqvIni5ly/D6q1UEL2tU2ob8cbkdJf17ZSHwD2f2LSaCYJkJA69aSEaRkCldUxPUd1gJea6zuxICaEnL6VpPX/78whQYwvwt/Tv9XBZ0k7YXDK/umdaisLRbvfXknsuvCnQsH6qqF0wGjIChBWUMo0oHjqvbsezt3tkBigAVBRQHvFwY+3sAzm2fTYS5yh+Rp/BIAV0AecPUeybQ=",
            "format": "base64"
          }
        ],
        "server_name": "web.whatsapp.com",
        "t": 0.107907192,
        "tls_version": "TLSv1.3"
      },
      {
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
            "data": "MIIEsTCCA5mgAwIBAgIQBOHnpNxc8vNtwCtCuF0VnzANBgkqhkiG9w0BAQsFADBsMQswCQYDVQQGEwJVUzEVMBMGA1UEChMMRGlnaUNlcnQgSW5jMRkwFwYDVQQLExB3d3cuZGlnaWNlcnQuY29tMSswKQYDVQQDEyJEaWdpQ2VydCBIaWdoIEFzc3VyYW5jZSBFViBSb290IENBMB4XDTEzMTAyMjEyMDAwMFoXDTI4MTAyMjEyMDAwMFowcDELMAkGA1UEBhMCVVMxFTATBgNVBAoTDERpZ2lDZXJ0IEluYzEZMBcGA1UECxMQd3d3LmRpZ2ljZXJ0LmNvbTEvMC0GA1UEAxMmRGlnaUNlcnQgU0hBMiBIaWdoIEFzc3VyYW5jZSBTZXJ2ZXIgQ0EwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQC24C/CJAbIbQRf1+8KZAayfSImZRauQkCbztyfn3YHPsMwVYcZuU+UDlqUH1VWtMICKq/QmO4LQNfE0DtyyBSe75CxEamu0si4QzrZCwvV1ZX1QK/IHe1NnF9Xt4ZQaJn1itrSxwUfqJfJ3KSxgoQtxq2lnMcZgqaFD15EWCo3j/018QsIJzJa9buLnqS9UdAn4t07QjOjBSjEuyjMmqwrIw14xnvmXnG3Sj4I+4G3FhahnSMSTeXXkgisdaScus0Xsh5ENWV/UyU50RwKmmMbGZJ0aAo3wsJSSMs5WqK24V3B3aAguCGikyZvFEohQcftbZvySC/zA/WiaJJTL17jAgMBAAGjggFJMIIBRTASBgNVHRMBAf8ECDAGAQH/AgEAMA4GA1UdDwEB/wQEAwIBhjAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwNAYIKwYBBQUHAQEEKDAmMCQGCCsGAQUFBzABhhhodHRwOi8vb2NzcC5kaWdpY2VydC5jb20wSwYDVR0fBEQwQjBAoD6gPIY6aHR0cDovL2NybDQuZGlnaWNlcnQuY29tL0RpZ2lDZXJ0SGlnaEFzc3VyYW5jZUVWUm9vdENBLmNybDA9BgNVHSAENjA0MDIGBFUdIAAwKjAoBggrBgEFBQcCARYcaHR0cHM6Ly93d3cuZGlnaWNlcnQuY29tL0NQUzAdBgNVHQ4EFgQUUWj/kK8CB3U8zNllZGKiErhZcjswHwYDVR0jBBgwFoAUsT7DaQP4v0cB1JgmGggC72NkK8MwDQYJKoZIhvcNAQELBQADggEBABiKlYkD5m3fXPwdaOpKj4PWUS+Na0QWnqxj9dJubISZi6qBcYRb7TROsLd5kinMLYBq8I4g4Xmk/gNHE+r1hspZcX30BJZr01lYPf7TMSVcGDiEo+afgv2MW5gxTs14nhr9hctJqvIni5ly/D6q1UEL2tU2ob8cbkdJf17ZSHwD2f2LSaCYJkJA69aSEaRkCldUxPUd1gJea6zuxICaEnL6VpPX/78whQYwvwt/Tv9XBZ0k7YXDK/umdaisLRbvfXknsuvCnQsH6qqF0wGjIChBWUMo0oHjqvbsezt3tkBigAVBRQHvFwY+3sAzm2fTYS5yh+Rp/BIAV0AecPUeybQ=",
            "format": "base64"
          }
        ],
        "server_name": "v.whatsapp.net",
        "t": 0.124645709,
        "tls_version": "TLSv1.3"
      }
    ],
    "registration_server_failure": null,
    "registration_server_status": "ok",
    "whatsapp_endpoints_blocked": [],
    "whatsapp_endpoints_dns_inconsistent": [],
    "whatsapp_endpoints_status": "ok",
    "whatsapp_web_status": "ok",
    "whatsapp_web_failure": null
  },
  "test_name": "whatsapp",
  "test_runtime": 0.631774013,
  "test_start_time": "2020-07-09 11:02:41",
  "test_version": "0.8.0"
}
```

## History

Since 2020-02-17, the heristics for checking whether a netblock belongs to
WhatsApp as described in version 2016-10-25-001 of this specification is
fundamentally broken (see [ooni/probe-engine#341](
https://github.com/ooni/probe-engine/issues/341)). This issue affected
ooni/probe-legacy <= 2.3.0, ooni/probe-ios <= 2.2.0, ooni/probe-android
<= 2.2.0. The `test_version` was 0.6.0 for ooni/probe-legacy and 0.6.1
for the mobile apps. Since Measurement Kit 0.10.10 (`test_version`
0.7.0) we will completely disable such check. Since 2020-07-09 the spec
does not mention anymore the CIDR check.

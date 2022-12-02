# HTTP Data Format

This document describes the keys with `test_keys` that all experiments
using HTTP SHOULD populate, possibly using directly the specific template
code. See this directory's [README](README.md) for the basic concepts.

| Name       | `httpt` |
|------------|---------|
| Version    | 0       |

## Specification

```JSON
{
  "agent": "redirect",
  "requests": [],
  "socksproxy": null
}
```

- `agent` (`string`): set to `agent` if the HTTP client code doesn't
follow redirects, set to `redirect` otherwise.

- `request` (`[]Transaction`): list of transaction objects. See below.

- `socksproxy` (`string`; optional; legacy): address of the SOCKS proxy being
used in a nettest. Note that this proxy is different from the one used to contact the backend. Omit or set to `null` if no SOCKS proxy is being used. The format
to be used is `1.2.3.4:54321` for IPv4 and `[::1234]:54321` for IPv6. Modern
probes always set this field to `null`.

## Transaction

```JSON
{
    "network": "tcp",
    "address": "1.1.1.1:443",
    "alpn": "h2",
    "failure": "dns_nxdomain_error",
    "request": {},
    "response": {},
    "response_length": 1234,
    "t0": 0.9,
    "t": 1.0,
    "transaction_id": 1
}
```

- `network` (`string`; optional): if available, the network of the
underlying connection we are using: either `"tcp"` or `"udp"`. Until 2022-09-08, we used
`"tcp"` or `"quic"` but we realized that using `"udp"` instead of `"quic"` would
be more consistent, so we also changed `"quic"` to always become `"udp"`. These
changes occurred during the OONI Probe v3.16.0 release cycle in
[ooni/probe-cli#946](https://github.com/ooni/probe-cli/pull/946).

- `address` (`string`; optional): if available, the endpoint of the
underlying connection we are using (e.g., `"[::1]:443"`).

- `alpn` (`string`; optional): if available and applicable, the ALPN
that was negotiated with the server, typically `"http/1.1"`, `"h2"` or `"h3"`.

- `failure` (`string`; nullable): if there was an error, this field is
a string indicating the error, otherwise it MUST be `null`.

- `request` (`Request`): object describing the request.

- `response` (`Response`): object describing the response.

- `response_length` (`int`; optional; deprecated): this is a legacy field that
contains the response length and is typically set to `null` or directly
omitted by modern clients (e.g. from Measurement Kit onwards).

- `t0` (`float`): number of seconds elapsed since `measurement_start_time`
measured in the moment in which we started the operation (`t - t0` gives you
the amount of time spent performing the operation);

- `t` (`float`): number of seconds elapsed since `measurement_start_time`
measured in the moment in which `failure` is determined (`t - t0` gives you
the amount of time spent performing the operation);

- `transaction_id` (`int`; optional; since 2020-01-11): the set of operations
to which this event belongs to (typically an HTTP transaction or a DNS
round trip). A zero or missing value means we don't know the transaction
to which this code belongs to.

## Request

```JavaScript
{
    "url": "https://example.com/",
    "body": MaybeBinaryData(),
    "body_is_truncated": false,
    "headers": {},
    "headers_list": [],
    "method": "GET",
    "tor": {},
    "x_transport": "tcp"
}
```

- `url` (`string`): this is the URL that was used for issuing the request.

- `body` (`string` or `BinaryData`): this is the request body. The body is a
`string` if it can be represented using UTF-8. Otherwise it is a `BinaryData`
instance, as described below. See also `MaybeBinaryData` below.

- `body_is_truncated` (`bool`; optional; since 2019-12-02): `true` if the body
has been truncated, `false` or omitted otherwise.

- `headers` (`map[string]MaybeBinaryData`): legacy map containing HTTP headers
where the value is `string` if it can be represented using UTF-8 and a
`BinaryData` instance otherwise. In case multiple headers have the same key,
the map SHOULD only contain the first value.

- `headers_list` (`[]HeaderValue`); since 2019-12-02): this is a better
representation of headers that allows us to represent the case where there
are multiple values for the same header key. See below the definition of
`HeaderValue`, which in the value-is-UTF-8 case boils down to the
`[string, string]` tuple.

- `method` (`string`): the request method.

- `tor` (`TorInfo`): this is an object containing information on the
instance of `tor` that we may be using for measuring.

- `vpn` (`VPNInfo`): similarly to `tor`, this is an object containing
  information on any `vpn` instance that we may be using for
  measuring.

- `x_transport` (`string`; deprecated): indicates what transports was used for
issuing the request. Typically `"tcp"` or `"udp"`. Until 2022-09-08, we used
`"tcp"` or `"quic"` but we realized that using `"udp"` instead of `"quic"` would
be more consistent, so we also changed `"quic"` to always become `"udp"`. These
changes occurred during the OONI Probe v3.16.0 release cycle in
[ooni/probe-cli#946](https://github.com/ooni/probe-cli/pull/946).

In case we have the following headers:

```bash
> Foo: bar
> Foo: <binary-data-here>
```

consistently with `MaybeBinaryData`'s definition,
the headers representation would be:

```JSON
{
  "headers": {
    "Foo": "bar"
  },
  "headers_list": [[
    "Foo", "bar",
  ], [
    "Foo", {"format": "base64", "data": "..."}
  ]]
}
```

Note how the `headers` map only gets the first value.

## HeaderValue

```JavaScript
[
  "key",
  MaybeBinaryData() // value
]
```

The first element is the header key. The second element is the header
value. Because the value may in principle be binary, we use
`MaybeBinaryData` (see below).

## Response

```JavaScript
{
    "body": MaybeBinaryData(),
    "body_is_truncated": false,
    "code": 501,
    "headers": {},
    "headers_list": [],
}
```

- `body`: like `Request.body`.

- `body_is_truncated`: like `Request.body_is_truncated`.

- `code` (`int`): response status code.

- `headers`: like `Request.headers`.

- `headers_list`: like `Request.headers_list`.

## MaybeBinaryData

This is either `string`, if the value can be represented using `UTF-8`, or
a `BinaryData` instance otherwise.

## BinaryData

```JSON
{"format": "base64", "data": "AQI="}
```

- `format` (`string`): MUST be `base64`.

- `data` (`string`): the `base64` representation of the value that
we could not represent using `UTF-8`.

## TorInfo

```JSON
{
    "exit_ip": null,
    "exit_name": null,
    "is_tor": false
}
```

- `exit_ip` (`string`; nullable): the IP of the exit node or `null`
if we're not using tor or this information is not available.

- `exit_name` (`string`; nullable): the name of the exit node or `null`
if we're not using tor or this information is not available.

- `is_tor` (`bool`): true if we're using tor, false otherwise.
 
## VPNInfo

```JSON
{
    "exit_ip": null,
    "provider": null,
    "is_vpn": false
}

- `exit_ip` (`string`; nullable): the egress IP for the VPN gateway, or `null`
  if we're not using a VPN or this information is not available.

- `provider` (`string`; nullable): the name of the provider to which this VPN
  gateway belongs to, or `null` if we're not using a VPN or this information is
  not available.

- `is_vpn` (`bool`): true if we're using a VPN, false otherwise.

## Example

In the following example we've omitted all the keys that are
not relevant to the HTTP data format:

```JSON
{
  "network": "tcp",
  "address": "93.184.216.34:443",
  "alpn": "h2",
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
        "example.com"
      ],
      [
        "Referer",
        ""
      ],
      [
        "User-Agent",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
      ]
    ],
    "headers": {
      "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
      "Accept-Language": "en-US,en;q=0.9",
      "Host": "example.com",
      "Referer": "",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
    },
    "method": "GET",
    "tor": {
      "exit_ip": null,
      "exit_name": null,
      "is_tor": false
    },
    "vpn": {
      "exit_ip": null,
      "provider": null,
      "is_vpn": false
    },
    "x_transport": "tcp",
    "url": "https://example.com"
  },
  "response": {
    "body": "<!doctype html>\n<html>\n<head>\n    <title>Example Domain</title>\n\n    <meta charset=\"utf-8\" />\n    <meta http-equiv=\"Content-type\" content=\"text/html; charset=utf-8\" />\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />\n    <style type=\"text/css\">\n    body {\n        background-color: #f0f0f2;\n        margin: 0;\n        padding: 0;\n        font-family: -apple-system, system-ui, BlinkMacSystemFont, \"Segoe UI\", \"Open Sans\", \"Helvetica Neue\", Helvetica, Arial, sans-serif;\n        \n    }\n    div {\n        width: 600px;\n        margin: 5em auto;\n        padding: 2em;\n        background-color: #fdfdff;\n        border-radius: 0.5em;\n        box-shadow: 2px 3px 7px 2px rgba(0,0,0,0.02);\n    }\n    a:link, a:visited {\n        color: #38488f;\n        text-decoration: none;\n    }\n    @media (max-width: 700px) {\n        div {\n            margin: 0 auto;\n            width: auto;\n        }\n    }\n    </style>    \n</head>\n\n<body>\n<div>\n    <h1>Example Domain</h1>\n    <p>This domain is for use in illustrative examples in documents. You may use this\n    domain in literature without prior coordination or asking for permission.</p>\n    <p><a href=\"https://www.iana.org/domains/example\">More information...</a></p>\n</div>\n</body>\n</html>\n",
    "body_is_truncated": false,
    "code": 200,
    "headers_list": [
      [
        "Age",
        "590050"
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
        "Thu, 08 Sep 2022 09:47:49 GMT"
      ],
      [
        "Etag",
        "\"3147526947+ident\""
      ],
      [
        "Expires",
        "Thu, 15 Sep 2022 09:47:49 GMT"
      ],
      [
        "Last-Modified",
        "Thu, 17 Oct 2019 07:18:26 GMT"
      ],
      [
        "Server",
        "ECS (dcb/7F5B)"
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
      "Age": "590050",
      "Cache-Control": "max-age=604800",
      "Content-Length": "1256",
      "Content-Type": "text/html; charset=UTF-8",
      "Date": "Thu, 08 Sep 2022 09:47:49 GMT",
      "Etag": "\"3147526947+ident\"",
      "Expires": "Thu, 15 Sep 2022 09:47:49 GMT",
      "Last-Modified": "Thu, 17 Oct 2019 07:18:26 GMT",
      "Server": "ECS (dcb/7F5B)",
      "Vary": "Accept-Encoding",
      "X-Cache": "HIT"
    }
  },
  "t0": 0.900978,
  "t": 1.051177,
  "transaction_id": 4
}
```

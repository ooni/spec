# HTTP Data Format

This document describes the keys with `test_keys` that all experiments
using HTTP SHOULD populate, possibly using directly the specific template
code. See this directory's [README](README.md) for the basic concepts.

## Specification

```JSON
{
  "agent": "redirect",
  "requests": [],
  "socksproxy": "127.0.0.1:54321"
}
```

- `agent` (`string`): set to `agent` if the HTTP client code doesn't
follow redirects, set to `redirect` otherwise.

- `request` (`[]Transaction`): list of transaction objects. See below.

- `socksproxy` (`string`; optional): address of the SOCKS proxy being
used. Omit or set to `null` if no SOCKS proxy is being used. The format
to be used is `1.2.3.4:54321` for IPv4 and `[::1234]:54321` for IPv6.

## Transaction

```JSON
{
    "failure": "dns_nxdomain_error",
    "request": {},
    "response": {},
    "response_lenght": 1234
}
```

- `failure` (`string`; nullable): if there was an error, this field is
a string indicating the error, otherwise it MUST be `null`.

- `request` (`Request`): object describing the request.

- `response` (`Response`): object describing the response.

- `response_length` (`int`; deprecated): this is a legacy field that
contains the response length and is typically set to `null` or directly
omitted by modern clients.

## Request

```JavaScript
{
    "body": MaybeBinaryData(),
    "body_is_truncated": false,
    "headers": {},
    "headers_list": [],
    "method": "GET",
    "tor": {}
}
```

- `body` (`string` or `BinaryData`): this is the request body. The body is a
`string` if it can be represented using UTF-8. Otherwise it is a `BinaryData`
instance, as described below.

- `body_is_truncated` (`bool`; optional; since v0.3.0): `true` if the body
has been truncated, `false` or omitted otherwise.

- `headers` (`map[string]MaybeBinaryData`): legacy map containing HTTP headers
where the value is `string` if it can be represented using UTF-8 and a
`BinaryData` instance otherwise. In case multiple headers have the same key,
the map SHOULD only contain the first value.

- `headers_list` (`[]struct{key string, value MaybeBinaryData}`; since
v0.3.0): this is a better representation of headers that allows us to
represent the case where there are multple values for the same header key. As
for `headers`, the value is a string or a `BinaryData` instance depending on
whether it can be represented using UTF-8 or not.

- `method` (`string`): the request method.

- `tor` (`TorInfo`): this is an object containing information on the
instance of `tor` that we may be using for measuring.

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

## Example

In the following example we've omitted all the keys that are
not relevant to the HTTP data format:

```JSON
{
  "test_keys": {
    "agent": "redirect",
    "requests": [
      {
        "failure": null,
        "request": {
          "body": "",
          "body_is_truncated": false,
          "headers_list": [[
              "Host", "149.154.171.5"
            ], [
              "User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
            ], [
              "Content-Length", "0"
            ], [
              "Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
            ], [
              "Accept-Language", "en-US;q=0.8,en;q=0.5"
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
          "headers_list": [[
              "Content-Length", "181"
            ], [
              "Server", "nginx/0.3.33"
            ], [
              "Date", "Fri, 10 Jan 2020 17:25:20 GMT"
            ], [
              "Content-Type", "text/html"
            ]
          ],
          "headers": {
            "Content-Length": "181",
            "Content-Type": "text/html",
            "Date": "Fri, 10 Jan 2020 17:25:20 GMT",
            "Server": "nginx/0.3.33"
          }
        }
      }
    ]
  }
}
```

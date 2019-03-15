# OONI bouncer specification

* version: 2.0.0
* date: 2019-03-15
* author: Simone Basso

This document aims at providing a functional specification of the
OONI bouncer. We keep a description of the _legacy_ bouncer behaviour
in [bk-001-ooni-backend.md](bk-001-ooni-backend.md).

# 1.0 System overview

The bouncer exposes an HTTP API allowing OONI probes to discover
active collectors and test helpers. A collector is an HTTP endpoint
used to submit measurements. A test helper is a server that helps
a specific network test to do its job.

The bouncer client and the bouncer server MUST NOT assume a keep
alive semantics for the HTTP connections.

New implementations MUST properly set `Content-Type`. Server side
implementatons MUST be able to deal with legacy clients that possibly
do not correctly set the `Content-Type`.

The bouncer MUST be exposed as an HTTPS service. It MUST also be exposed as
a Tor onion service as long as legacy OONI probe clients use it. The need
to expose an onion service will be rediscussed when legacy OONI probe
clients will no longer be relevant. A [legacy document](
https://ooni.torproject.org/docs/architecture.html)
explains why the OONI project originally chose to allow for both HTTPS
and Tor onion service services (henceforth, Onion).

# 2.0 Threat model

The bouncer transport MUST guarantee some reasonable level of encryption
and authentication between the OONI probe and itself. Therefore, a malicious
lazy actor won't be able to easily see and/or modify the exchanged data.

It is outside of the scope of the bouncer to provide blocking resistance or
to conceal to a passive network observer the fact that they are communicating to
a bouncer. Such properties are to be provided by other software, e.g. Tor.

Therefore a client implementation of the bouncer protocol SHOULD allow one
to specify a [SOCKS5](https://tools.ietf.org/html/rfc1928) proxy where the
name resolution is performed by the circumvention tool (`socks5h`).

# 3.0 API

The same API is available via HTTP and Onion.

## 3.1 Legacy API

As long as we have legacy clients, a bouncer MUST implement the legacy
API defined in [bk-001-ooni-backend.md](bk-001-ooni-backend.md). In
this document we only describe the new API.

## 3.2 Discovering collectors

A probe will send the following request:

    GET /collectors

On success, the bouncer will reply with status `200` and a body
containing a JSON document following this spec:

    {results: [{
      "address":
        `string` containing the service URL. The semantics depends
        also on the value of type.
      
      "type":
        `string` indicating the type. One of "https", "cloudfront",
        or "onion". When type is "https" or "onion", "address" is
        the HTTPS or Onion URL to use. When it's "cloudfront", the
        URL hostname is the hostname to pass to the cloudfront
        service, while the real hostname to connect to is provided
        in the optional "front" field.
      
      "front":
        (optional) `string` indicating the real host to connect
        to when using a cloudfronting service.
    }]}

On failure, the bouncer MUST return `5xx`.

The following example shows how getting the collectors looks like from
the point of view of a modern bouncer client (where the JSON
messages have been edited for readability):

```
> GET /collectors HTTP/1.1
> Host: bouncer.ooni.io
>
< HTTP/1.1 200 OK
< Server: nginx
< Date: Wed, 13 Mar 2019 13:19:42 GMT
< Content-Type: application/json; charset=utf-8
< Content-Length: 152
< Connection: keep-alive
< 
< {"results": [{
<   "address": "httpo://ihiderha53f36lsd.onion",
<   "type": "onion",
< }, {
<   "address": "https://a.collector.ooni.io:4441",
<   "type": "https"
< }, {
<   "address": "https://das0y2z2ribx3.cloudfront.net",
<   "front": "a0.awsstatic.com",
<   "type": "cloudfront"
< }]}
```

## 3.3 Discovering test helpers

A probe will send the following request:

    GET /test-helpers

On success, the bouncer will reply with status `200` and a body
containing a JSON document following this spec:

    {results: {
      "<test-helper-name>": [{
        "address":
          `string` containing the service URL or address. The semantics
          depends also on the value of type.
      
        "type":
          `string` indicating the type. One of "legacy", "https", and
          "cloudfronted". For "https" and "cloudfronted" we use the
          same semantics of the one described for /collectors.

          With "legacy" we indicate whatever was the default returned
          by the legacy bouncer as the primary test helper. In this
          case, the meaning of the value returned in "address" depends
          on the type of helper requested. The client is expected to
          already know what is the proper semantic for "address" given
          a specific test helper.
      
        "front":
          (optional) `string` indicating the real host to connect
          to when using a cloudfronting service.
    }]}}

On failure, the bouncer MUST return `5xx`.

The following example shows how getting the tst helpers looks like from
the point of view of a modern bouncer client (where the JSON
messages have been edited for readability):

```
> GET /test-helpers HTTP/1.1
> Host: bouncer.ooni.io
>
< HTTP/1.1 200 OK
< Server: nginx
< Date: Wed, 13 Mar 2019 13:19:42 GMT
< Content-Type: application/json; charset=utf-8
< Content-Length: 152
< Connection: keep-alive
< 
< {"results": {
<   "dns": [{"type": "legacy", "address": "213.138.109.232:57004"}],
<   "http-return-json-headers": [{
<     "type": "legacy",
<     "address": "http://38.107.216.10:80"
<   }],
<   ssl": [{
<     "type": "legacy",
<     "address": "https://213.138.109.232"
<   }],
<   "tcp-echo": [{
<     "type": "legacy",
<     "address": "213.138.109.232"
<   }],
<   "traceroute": [{
<     "type": "legacy",
<     "address": "213.138.109.232"
<   }],
<   "web-connectivity": [{
<     "type": "legacy",
<     "address": "httpo://7jne2rpg5lsaqs6b.onion"
<   }, {
<     "address": "https://a.web-connectivity.th.ooni.io:4442",
<     "type": "https",
<   }, {
<     "address": "https://d2vt18apel48hw.cloudfront.net",
<     "front": "a0.awsstatic.com",
<     "type": "cloudfront",
<   }]}}
```

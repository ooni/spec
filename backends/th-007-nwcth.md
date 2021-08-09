# New Web Connectivity Test Helper Spec

* _Author_: sbs
* _Version_: 202108.09.1555
* _Status_: alpha

This document describes a draft specification for the new web connectivity test
helper. We tentatively expose this new API as `/api/unstable/wcth`.

A future version of this document will also provide a design rationale.

## Semantics

This section defines the messages implementing the New Web
Connectivity Test Helper protocol.

### Endpoint

An endpoint is:

- an IPv4 address followed by `:` followed by a valid port number; or

- an IPv6 address quoted using `[` and `]` followed by `:`
followed by a valid port number.

For example, `1.2.3.4:5`, `[::1]:5`.

### Request message

*Implementation note*: all the field names changed since 2021-08-06-001!

The request message (`CtrlRequest`) contains these fields:

```
CtrlRequest = {
  "url": "",
  "headers": {},
  "endpoints": []
}
```

where:

- `url` is mandatory and contains the string-serialized URL we should measure;

- `headers` is an optional map from string to a list of strings containing the headers
the test helper should include when measuring;

- `endpoints` is an optional list of string-serialized endpoints for the
domain inside the `url`'s `authority` discovered by the client.

If the `url`'s authority contains an IP address rather than a domain, the client
should include the corresponding endpoint inside `endpoints`.

If the `url` is empty or invalid, the test helper should consider the message as invalid
and act accordingly (e.g., return a 400 error).

### Response message

The response message (`CtrlResponse`) contains these fields:

```
CtrlResponse = {
  "urls": []
}
```

where `urls` is a list of `URLMeasurement`s and `URLMeasurement` contains these fields:

```
URLMeasurement = {
  "url": "",
  "dns": {},
  "endpoint": []
}
```

where:

- `url` is a valid string-serialized URL and contains
the URL to which this `URLMeasurement` refers;

- `dns` is a `DNSMeasurement` structure and contains
the result of the DNS lookup of the domain in the `url`'s `authority`;

- `endpoint` contains an `EndpointMeasurement` for each endpoint
we discovered for the `url.authority`'s domain.

Note that `url`, and `dns` should always be present. The
`endpoint` field is empty if, e.g., there is an `NXDOMAIN` error.

If the `url`'s authority contains an IP address rather than a domain, we
should include the corresponding address inside `dns`.

The test helper guarantees that `CtrlResponse.urls[0]` is the measurement for `CtrlRequest.url`. Subsequent
measurements derive from HTTP redirection or from testing HTTP3 endpoints discovered parsing
`Alt-Svc` headers.

#### DNSMeasurement

The `DNSMeasurement` message contains these fields:

```
{
  "failure": null | "",
  "addrs": [],
}
```

where:

- `failure` is `null` on success or a OONI failure otherwise (see the
`df-007-errors.md` document for more information);

- `addrs` a possibly-empty list of IP addresses returned by the DNS lookup.

#### EndpointMeasurement

*Implementation note*: names changed since 2021-08-06-001!

The `EndpointMeasurement` messsages is the union of `HTTPMeasurement` and `H3Measurement`:

```
EndpointMeasurement = HTTPEndpointMeasurement | H3EndpointMeasurement
```

#### HTTPEndpointMeasurement

*Implementation note*: name changed since 2021-08-06-001!

`HTTPEndpointMeasurement` has the following structure:

```
{
  "endpoint": "",
  "protocol": "http" | "https",
  "tcp_connect": {},
  "tls_handshake": {},
  "http_request": {}
}
```

where:

- `endpoint` is a string containing an endpoint (as defined above);

- `protocol` is either `"http"` or `"https"`;

- `tcp_connect` is a `TCPConnectMeasurement`;

- `tls_handshake` is a `TLSHandshakeMeasurement`;

- `http_request` is an `HTTPRequestMeasurement`.

#### H3EndpointMeasurement

*Implementation note*: name changed since 2021-08-06-001!

`H3EndpointMeasurement` has the following structure:

```
{
  "endpoint": "/Endpoint/",
  "protocol": "h3" | "h3-29" | ...,
  "quic_handshake": TLSHandshakeMeasurement{},
  "http_request": HTTPRequestMeasurement{}
}
```

where:

- `endpoint` is a string containing an endpoint (as defined above);

- `protocol` is either `"h3"`, `"h3-29"`, or any other supported experimental QUIC protocol;

- `quic_handshake` is a `QUICHandshakeMeasurement`;

- `http_request` is an `HTTPRequestMeasurement`.

#### TCPConnectMeasurement

`TCPConnectMeasurement` is like:

```
{
  "failure": null | ""
}
```

where:

- `failure` is `null` on success or a OONI failure otherwise (see the
`df-007-errors.md` document for more information).

#### TLSHandshakeMeasurement

`TLSHandshakeMeasurement` is like:

```
{
  "failure": null | ""
}
```

where:

- `failure` is `null` on success or a OONI failure otherwise (see the
`df-007-errors.md` document for more information).

(*Note*: this structure will support more fields in the future.)

#### QUICHandshakeMeasurement

`QUICHandshakeMeasurement` is an alias for `TLSHandshakeMeasurement`.

#### HTTPRequestMeasurement

`HTTPRequestMeasurement` is like:

```
{
  "body_length": 0,
  "failure": null | "",
  "headers": {},
  "status_code": 0,
}
```

where:

- `body_length` is the optional body length in bytes;

- `failure` is `null` on success or a OONI failure otherwise (see the
`df-007-errors.md` document for more information);

- `headers` is an optional map from string to a list of strings
containing the response headers (if any);

- `status_code` is the optional response status code.

On failure, only `failure` is meaningful. On success, there must be
a valid HTTP status code, and all other fields may be empty.

## Algorithm

This section defines the algorithms implementing the New
Web Connectivity Test Helper.

### URLMeasurer

XXX

XXX

XXX

### HTTPEndpointMeasurer

`HTTPEndpointMeasurer` takes in input a parsed URL (`URL`), an
endpoint (`epnt`), the optional request headers (`hdrs`), and the
current cookie state (`jar`). It returns to the caller an
`HTTPEndpointMeasurement` structure (`m`).

The first step is to apply the `TCPConnector` algorithm using
`epnt` and saving the `TCPConnectMeasurement` (in `m.tcp_connect`)
and the TCP connection (in `tcpConn`).

If `tcpConn` is `nil`, we just return `m`.

Otherwise, if `URL.scheme` is `"https"`, we apply the `TLSHandshaker`
algorithm using `tcpConn`, using `URL.hostname` to configure the
SNI field, and supplying "h2", "http/1.1" as the ALPN. We store the
returned `TLSHandshakeMeasurement` as `m.tls_handshake`. If the returned
TLS connection is nil, we just return `m`, otherwise we fall through.

We send an HTTP request using the TLS connection (HTTPS case) or the
TCP connection (HTTP case), `URL`, `jar`, and `hdrs`. We only include `accept`,
`accept-language`, and `user-agent` into the outgoing request and
we ignore all other headers inside `hdrs`.

We fill `m` using the error that occurred (if any), the response status
code, the headers, and the body size. (We limit the maximum response body
size to `1<<24`, which is larger than all bodies in the test list.)

### H3EndpointMeasurer

`H3EndpointMeasurer` takes in input a parsed URL (`URL`), an
endpoint (`epnt`), the optional request headers (`hdrs`), the
current cookie state (`jar`). It returns to the caller an
`H3EndpointMeasurement` structure (`m`).

The first step is to apply the `QUICHandshaker` algorithm using
`epnt`, `URL.hostname` to configure the SNI field, and supplying
"h2", "http/1.1" as the ALPN. We store the returned
`QUICHandshakeMeasurement` as `m.quic_handshake`. If the returned
QUIC session is nil, we just return `m`, otherwise we fall through.

We send an HTTP request using the QUIC session, `URL`, `jar`, and `hdrs`. We
only include `accept`, `accept-language`, and `user-agent` into the
outgoing request and we ignore all other headers inside `hdrs`.

We fill `m` using the error that occurred (if any), the response status
code, the headers, and the body size. (We limit the maximum response body
size to `1<<24`, which is larger than all bodies in the test list.)

### DNSResolver

`DNSResolver` takes in input a string containing the domain to resolve (`domain`)
and returns a `DNSMeasurement` data structure (`m`).

If `domain` is an IP address, it appends `domain` to `m.addrs` and returns `m`.

Otherwise, it resolves `domain` using `https://dns.google/dns-query`.

If the resolution fails, it fills `m.failure` and returns `m`.

Otherwise, it fills `m.addrs` and returns `m`.

### TCPConnector

`TCPConnector` takes in input a string containing the TCP endpoint to
connect to (`epnt`), and returns a `TCPConnectMeasurement`
data structure (`m`) and an optional TCP connection.

`TCPConnect` attempts to connect to `epnt`.

On failure, it fills `m.failure` and returns a tuple containing
`m` and a `nil` TCP connection.

Otherwise, it returns `m` and the established TCP connection.

### TLSHandshaker

`TLSHandshaker` takes in input a TCP connection (`conn`), the SNI to use
(`sni`), and the ALPN to use (`alpn`). It returns to the caller a
`TLSHandshakeMeasurement` (`m`) and a TLS connection.

`TLSHandshaker` performs a TLS handshake using `conn`, `sni`, and `alpn`.

On failure, it fills `m.failure` and returns `m` and a `nil` TLS connection.

Otherwise, it returns `m` and the TLS connection.

### QUICHandshaker

`QUICHandshaker` takes in input the endpoint to use (`enpt`), the SNI to
use (`sni`), and the QUIC version to use (`version`). It returns to the caller a
`QUICHandshakeMeasurement` (`m`) and a QUIC session.

`QUICHandshaker` performs a QUIC handshake using `epnt`, `sni`, and `version`.

On failure, it fills `m.failure`, then returns `m` and a `nil` QUIC session.

Otherwise, it returns `m` and the QUIC session.


## OLD CONTENT

The test helper resolves the domain in the `"URL"` at `http_request`. If the
domain is an IPv4/IPv6 address, the test helper should return the same IP
address as if it was the result of the DNS resolution, like `getaddrinfo` does. If the
resolution fails, and the client has not provided any IP address, there are no
IP addresses we can use, so the test helper stops and returns a message.

Otherwise, the test helper merges the endpoints provided by the client inside
the `tcp_connect` field with endpoints derived from the domain name resolution
step. We extract the port to construct new endpoints from the `http_request`
`"URL"`: if there is an explicit port, we use it, otherwise we use the default
port for the protocol scheme (`80` for `http` and `443` for `https`).

At this stage, the test helper has constructed an `URLMeasurement{}` message
and initialized its `url` and `dns` fields.

For each endpoint obtained merging the client and the test helper endpoints, the
test helper will then perform an `EndpointMeasurement`. Because there is no
information concerning QUIC, the test helper will start off using TCP. (As we will
see later, QUIC is identified by the `h3://` or `h3-29://` scheme.)

The measurement will consist of the usual steps: TCP connect to the endpoint,
perform a TLS handshake, do the HTTP round trip and fetch the body.

These steps will generate an `EndpointMeasurement{}` for each endpoint.

When sending the request part of the HTTP round trip, the test helper WILL use
only the following headers from the request message:

* `user-agent`
* `accept`
* `accept-language`

When all the endpoints have been measured, the test helper will determine
whether it could perform additional follow-up measurements. Each new
follow-up measurement generates a new `URLMeasurement{}` struct that will
be appended to the top-level `urls` list.

To decide whether it could perform more measurements, or whether it should
stop here, the test helper will check the length of the `urls` array in
the top-level response message it is constructing. If the length exceeds
a reasonable threshold, the test helper should stop measuring.

Otherwise, the test helper will determine whether it could perform
additional measurements. To this end, it will extract new URLs to
measure from the results of the previous measurements.

To determine whether it should try QUIC endpoints, the test helper will
parse the `Alt-Svc` header of all the responses it received. The test
helper should of course merge equal `Alt-Svc` headers to perform a single
follow-up measurement, if all headers have the same value.

For a value of `Alt-Svc` equal to `h3-29=:443` the test helper should
manipulate the original URL, replacing the scheme to be `h3-29` and
the port to be `:443`. The code should be robust enough to handle the
case where `Alt-Svc` contains a complete endpoint like `[::1]:444`.

The value obtained from `Alt-Svc` is a new measurement to perform. The
main difference is that the `h3` or `h3-xxx` scheme causes the test
helper to use QUIC instead of HTTPS. The result of this measurement is
a new `URLMeasurement{}` entry to be appended to `urls`.

Likewise, for any `Location` header find in the response, the test
helper should compute a new full URL to fetch. Again, the code should
reduce equal `Location` headers discovered from multiple responses,
to avoid duplicating work.

We will not bother with caching the results of previous domain name
resolutions at this stage of this draft spec. Should we choose to
do that, it is quite trivial anyway.

As an implementation note, if it's possible to obtain better URLs for
follow-up QUIC or Location measurements using the Go API, then we should
do that when possible. (Consider, for example, the `Location` method
of the `Response`.)

## Limitations

This draft specification does not address these issues:

1. adding logic to the test helper to choose whether it is smart
to continue processing due to other considerations. For example, if
we're redirected from `http://facebook.com/` to `https://facebook.com/`,
it may be reasonable to stop the measurement instead of being
further redirected to, say, `https://facebook.com/en_US/login.php`.

2. whether the amount of information included in each `EndpointMeasurement{}`
is such that the OONI Probe can unambiguously redo the same operation.

3. because [recent measurements](https://github.com/ooni/probe/issues/1727) show that we can perform most
redirects in the test list without cookies, it seems fine to stash
this problem for the time being.

4. we may or may not choose to avoid reading the whole body of `https` and
`h3` responses for brevity. Also this problem is left for later.

These problems will be solved at a later time.

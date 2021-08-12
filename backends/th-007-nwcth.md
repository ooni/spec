# New Web Connectivity Test Helper Spec

* _Author_: sbs
* _Version_: 202108.12.1737
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
  "addrs": []
}
```

where:

- `url` is mandatory and contains the string-serialized URL we should measure;

- `headers` is an optional map from string to a list of strings containing the headers
the test helper should include when measuring;

- `addrs` is an optional list of string-serialized IP addresses for the
domain inside the `url`'s `authority` discovered by the client.

If the `url`'s authority contains an IP address rather than a domain, the client
should include the corresponding address inside `addrs`.

If the `url` is empty or invalid, the test helper should consider the message as invalid
and act accordingly (e.g., return a `400` error).

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
  "endpoints": []
}
```

where:

- `url` is a valid string-serialized URL and contains
the URL to which this `URLMeasurement` refers;

- `dns` is a `DNSMeasurement` structure and contains
the result of the DNS lookup of the domain in the `url`'s `authority`;

- `endpoints` contains an `EndpointMeasurement` for each endpoint
we discovered for the `url.authority`'s domain.

Note that `url`, and `dns` should always be present. The
`endpoints` field is empty if, e.g., there is an `NXDOMAIN` error.

If the `url`'s authority contains an IP address rather than a domain, we
should include the corresponding address inside `dns`.

The test helper guarantees that `CtrlResponse.urls[0]` is the measurement
for `CtrlRequest.url`. Subsequent measurements derive from HTTP redirections
or from testing HTTP3 endpoints discovered using a suitable discovery
mechanism (e.g., parsing `Alt-Svc` header).

#### DNSMeasurement

The `DNSMeasurement` message contains these fields:

```
{
  "failure": null | "",
  "addrs": [],
}
```

where:

- `failure` is `null` on success and a OONI failure otherwise (see the
`df-007-errors.md` document for more information);

- `addrs` is a possibly-empty list of IP addresses returned by the DNS lookup.

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
  "endpoint": "",
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

`TCPConnectMeasurement` has the following structure:

```
{
  "failure": null | ""
}
```

where:

- `failure` is `null` on success and a OONI failure otherwise (see the
`df-007-errors.md` document for more information).

#### TLSHandshakeMeasurement

`TLSHandshakeMeasurement` has the following structure:

```
{
  "failure": null | ""
}
```

where:

- `failure` is `null` on success and a OONI failure otherwise (see the
`df-007-errors.md` document for more information).

(*Note*: this structure will support more fields in the future.)

#### QUICHandshakeMeasurement

`QUICHandshakeMeasurement` is (currently) an alias for `TLSHandshakeMeasurement`.

#### HTTPRequestMeasurement

`HTTPRequestMeasurement` has the following structure:

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

- `failure` is `null` on success and a OONI failure otherwise (see the
`df-007-errors.md` document for more information);

- `headers` is an optional map from string to a list of strings
containing the response headers (if any);

- `status_code` is the optional response status code.

On failure, only the `failure` field is meaningful. On success, there must be
a valid HTTP status code, and all other fields may be empty.

*Note*: it may be worthwhile to use a list of string pairs for headers
but the representation of map from string to strings seems more robust to
parse because it's really not ambiguous.

## Algorithm

This section defines the algorithms implementing the New
Web Connectivity Test Helper.

### TopLevel

- input:
    - `creq`: a `CtrlRequest`
- output:
    - `cresp`: a `CtrlResponse`
    - `err`: hard error that should cause a `400`
- algorithm:
    1. if `creq.url` is empty or does not parse, return error
    2. let `URL` be the parsed URL
    3. let `jar` be the mutable cookie state
    4. let `headers` be `creq.headers`
    5. for `i` in `1..20`
        1. call `URL` measurer with obvious mappings and `""` as QUIC version
        2. [...] XXX XXX XXX

### URLMeasurer

- input:
    - `URL`: already parsed HTTP URL
    - `headers`: map containing optional request headers
    - `jar`: current cookie state (mutable)
    - `clientResolutions`: map from string (domain name) to list of strings (IP addresses resolved by the client)
    - `version`: QUIC version or empty string to mean "use TCP"
- output:
    - `m`: a `URLMeasurement`
- algorithm:
    1. save `m.url` immediately
    2. call `DNSResolver`
         - input:
             - `URL.hostname` 
         - output:
             - `DNSMeasurement` as `url.dns`
    3. init `addrs` as *a copy of* `url.dns.addrs`
    4. if `clientResolutions` contains an entry for `URL.hostname` merge its addresses with `addrs` and remove duplicates
    5. create list of endpoints `endpoints` using `addrs` and `URL.port` or the default port for `URL.scheme`
    6. for each `endpoint` in `endpoints`:
        1. if `URL.scheme` is `https` and `version` is set, call `H3EndpointMeasurer`
        2. else if `URL.scheme` is `https`, call `HTTPSEndpointMeasurer`
        3. else if `URL.scheme` is `http`, call `HTTPEndpointMeasurer`

### HTTPEndpointMeasurer

- input:
    - `URL`: already parsed HTTP URL
    - `headers`: map containing optional request headers
    - `endpoint`: TCP endpoint to use
    - `jar`: current cookie state (mutable)
- output:
    - `m`: a `H3EndpointMeasurement`
- algorithm:
    1. save `m.protocol` and `m.endpoint` immediately
    2. call `TCPConnector`
        - input:
            - `endpoint`
        - output:
            - `TCPConnectMeasurement` as `m.tcp_connect`
            - TCP connection as `tcpConn`
    3. if `tcpConn` is `nil`, return
    4. construct HTTP client (`clnt`) using `tcpConn` and `jar`
    5. call `HTTPGetter`
        - input:
            - `URL`
            - suitable `maxBodySize`
            - `clnt`
            - `headers`
        - output:
            - `HTTPRequestMeasurement` as `m.http_request`
    6. return

### HTTPSEndpointMeasurer

- input:
    - `URL`: already parsed HTTPS URL
    - `headers`: map containing optional request headers
    - `endpoint`: TCP endpoint to use
    - `jar`: current cookie state (mutable)
- output:
    - `m`: a `H3EndpointMeasurement`
- algorithm:
    1. save `m.protocol` and `m.endpoint` immediately
    2. call `TCPConnector`
        - input:
            - `endpoint`
        - output:
            - `TCPConnectMeasurement` as `m.tcp_connect`
            - TCP connection as `tcpConn`
    3. if `tcpConn` is `nil`, return
    4. call `TLSHandshaker`
        - input:
            - `tcpConn`
            - `["h2", "http/1.1"]` as `alpn`
            - `URL.hostname` as `sni`
        - output:
            - `TLSHandshakeMeasurement` as `m.tls_handshake`
            - TLS connection as `tlsConn`
    5. if `tlsConn` is `nil`, return
    6. construct HTTP client (`clnt`) using `tlsConn` and `jar`
    7. call `HTTPGetter`
        - input:
            - `URL`
            - suitable `maxBodySize`
            - `clnt`
            - `headers`
        - output:
            - `HTTPRequestMeasurement` as `m.http_request`
    8. return

### H3EndpointMeasurer

- input:
    - `URL`: already parsed HTTPS URL
    - `headers`: map containing optional request headers
    - `endpoint`: UDP endpoint to use
    - `version`: QUIC version to use
    - `jar`: current cookie state (mutable)
- output:
    - `m`: a `H3EndpointMeasurement`
- algorithm:
    1. save `m.protocol` and `m.endpoint` immediately
    2. call `QUICHandshaker`
        - input:
            - `endpoint`
            - `version`
            - `URL.hostname` as `sni`
        - output:
            - `QUICHandshakeMeasurement` as `m.quic_handshake`
            - QUIC session as `sess`
    3. if `sess` is `nil`, return
    4. construct HTTP client (`clnt`) using `sess` and `jar`
    5. call `HTTPGetter`
        - input:
            - `URL`
            - suitable `maxBodySize`
            - `clnt`
            - `headers`
        - output:
            - `HTTPRequestMeasurement` as `m.http_request`
    6. return

### HTTPGetter

- input:
    - `URL`: already parsed HTTP/HTTPS URL
    - `headers`: map containing optional request headers
    - `clnt`: HTTP/HTTP3 client possibly configured to use specific TLS/QUIC conn
    - `maxBodySize`: maximum response body size (bytes)
- output:
    - `m`: a `HTTPRequestMeasurement`
- algorithm:
    1. construct GET request `req` using URL
    2. add `accept`, `accept-language`, `user-agent` from `headers` to `req`
    3. issue `req` using `clnt`
    4. on failure, set `m.failure` and return
    5. set `m.status_code`, `m.headers`
    6. read body up to `maxBodySize`
    7. on failure, set `m.failure` and return
    8. set `m.body_size`
    9. return

### DNSResolver

- input:
    - `domain`: domain to resolve (or IP address)
- output:
    - `m`: a `DNSMeasurement`
- algorithm:
    1. if `domain` is an IP address, add it to `m.addrs` and return
    2. perform DNS resolution for `domain` using `https://dns.google/dns-query`
    3. on failure, fill `m.failure` and return
    4. save resolved addresses using `m.addrs`
    5. return

### TCPConnector

- input:
    - `epnt`: TCP endpoint
- output:
    - `m`: a `TCPConnectMeasurement`
    - `tcpConn`: TCP connection
- algorithm:
    1. perform TCP connect using `epnt`
    2. on failure, fill `m.failure` and return
    3. save TCP connection using `tcpConn`
    4. return

### TLSHandshaker

- input:
    - `tcpConn`: TCP connection
    - `sni`: SNI to use
    - `alpn`: ALPN to use 
- output:
    - `m`: a `TLSHandshakeMeasurement`
    - `tlsConn`: TLS connection
- algorithm:
    1. perform TLS handshake using `tcpConn`, `sni`, and `alpn`
    2. on failure, fill `m.failure` and return
    3. save TLS connection using `tlsConn`
    4. return

### QUICHandshaker

- input:
    - `endpoint`: UDP endpoint
    - `sni`: SNI to use
    - `version`: QUIC version to use 
- output:
    - `m`: a `QUICHandshakeMeasurement`
    - `sess`: QUIC session
- algorithm:
    1. perform QUIC handshake using `endpoint`, `sni`, and `version`
    2. on failure, fill `m.failure` and return
    3. save QUIC session using `sess`
    4. return

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

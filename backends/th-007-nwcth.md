# New Web Connectivity Test Helper Spec

* _Author_: sbs
* _Version_: 202108.13.1700
* _Status_: alpha

This document contains a draft specification for the new web connectivity test
helper. We tentatively expose this new API as `/api/unstable/wcth`.

## Design

The test helper should help OONI Probe to discover all the relevant TCP/UDP endpoints
deriving from the input URL coming from the test lists or from user input.
The Probe will then test all the endpoints indicated by the test helper.

This discovery process includes finding out HTTPS URLs corresponding to HTTP URLs
in case of redirections. It also includes discovering whether there are
HTTP/3 endpoints associated to HTTPS URLs.

Since we perform this discovery, we also cover the case where a Probe
cannot continue to perform a measurement because it receives a `NXDOMAIN`
error when performing DNS lookups for the hostname in the URL.

This specification does not mean to imply that the new Web Connectivity
requires a test helper to function. It is out of the scope of this
spec to discuss this problem. We will discuss it in a companion spec
that covers the client side implementation of the new test.

## Semantics

This section defines the messages of the New Web
Connectivity Test Helper protocol.

### Endpoint

Before discussing messages, we need to define TCP and UDP _endpoints_.

In terms of syntax, an endpoint is

- an IPv4 address followed by `:` followed by a valid port number; or

- an IPv6 address quoted using `[` and `]` followed by `:`
followed by a valid port number.

For example, `1.2.3.4:5`, `[::1]:5`.

### URL

We also need to state what is perhaps obvious. An URL contains an
`authority` field. Such a field usually contains a domain name, e.g.,
`http://www.example.com` contains `www.example.com`. The authority
_could_ also contain an IP address, e.g., `http://8.8.8.8`. If
the IP address is an IPv6 address, it is quoted using the same rules
used for the endpoint, e.g., `http://[::1]/`. The authority may
also contain a port, e.g., `http://[::1]:8080/`. If the port isn't
specified, we use the default port for the URL scheme.

Having clarified URL and endpoint semantics, we can now discuss messages.

### Request message

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
the test helper should include when measuring (which headers from this map will be used
is specified more in detail below);

- `addrs` is an optional list of string-serialized IP addresses for the
`url`'s domain discovered by the client.

If the `url`'s hostname is an IP address, the client should include the
corresponding address inside `addrs`.

Example:

```JSON
{
  "url": "http://www.example.com",
  "headers": {
    "User-Agent": [
      "curl/7.64.1"
    ]
  },
  "addrs": [
    "93.184.216.34",
    "2606:2800:220:1:248:1893:25c8:1946"
  ]
}
```

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
the result of the DNS lookup of the domain in the `url`;

- `endpoints` contains an `EndpointMeasurement` for each endpoint
we discovered for the `url`'s domain.

Note that `url`, and `dns` should always be present. The
`endpoints` field is empty if, e.g., there is an `NXDOMAIN` error.

If the `url`'s authority contains an IP address rather than a domain, we
should include the corresponding address inside `dns`.

The order of the `CtrlResponse.urls` field is the order in which the
test helper wants the probe to perform measurements.

#### DNSMeasurement

The `DNSMeasurement` message contains these fields:

```
DNSMeasurement = {
  "domain": "",
  "failure": null | "",
  "addrs": [],
}
```

where:

- `domain` is the domain we tried to resolve;

- `failure` is `null` on success and a OONI failure otherwise (see the
`df-007-errors.md` document for more information);

- `addrs` is a possibly-empty list of IP addresses returned by the DNS lookup.

#### EndpointMeasurement

The `EndpointMeasurement` messsages is one of `HTTPEndpointMeasurement`,
`HTTPSEndpointMeasurement`, and `H3EndpointMeasurement`:

```
EndpointMeasurement = HTTPEndpointMeasurement | HTTPSEndpointMeasurement | H3EndpointMeasurement
```

#### HTTPEndpointMeasurement

`HTTPEndpointMeasurement` has the following structure:

```
HTTPEndpointMeasurement = {
  "endpoint": "",
  "protocol": "http",
  "tcp_connect": {},
  "http_round_trip": {}
}
```

where:

- `endpoint` is a string containing an endpoint (as defined above);

- `protocol` is `"http"`;

- `tcp_connect` is a `TCPConnectMeasurement`;

- `http_round_trip` is an `HTTPRoundTripMeasurement`.

#### HTTPSEndpointMeasurement

`HTTPSEndpointMeasurement` has the following structure:

```
HTTPSEndpointMeasurement = {
  "endpoint": "",
  "protocol": "https",
  "tcp_connect": {},
  "tls_handshake": {},
  "http_round_trip": {}
}
```

where:

- `endpoint` is a string containing an endpoint (as defined above);

- `protocol` is `"https"`;

- `tcp_connect` is a `TCPConnectMeasurement`;

- `tls_handshake` is a `TLSHandshakeMeasurement`;

- `http_request` is an `HTTPRoundTripMeasurement`.

#### H3EndpointMeasurement

`H3EndpointMeasurement` has the following structure:

```
H3EndpointMeasurement = {
  "endpoint": "",
  "protocol": "h3" | "h3-29" | ...,
  "quic_handshake": TLSHandshakeMeasurement{},
  "http_round_trip": HTTPRoundTripMeasurement{}
}
```

where:

- `endpoint` is a string containing an endpoint (as defined above);

- `protocol` is `"h3"`, `"h3-29"`, or any other supported experimental QUIC protocol;

- `quic_handshake` is a `QUICHandshakeMeasurement`;

- `http_round_trip` is an `HTTPRoundTripMeasurement`.

#### TCPConnectMeasurement

`TCPConnectMeasurement` has the following structure:

```
TCPConnectMeasurement = {
  "failure": null | ""
}
```

where:

- `failure` is `null` on success and a OONI failure otherwise (see the
`df-007-errors.md` document for more information).

A future draft of this specification may include more fields.

#### TLSHandshakeMeasurement

`TLSHandshakeMeasurement` has the following structure:

```
TLSHandshakeMeasurement = {
  "failure": null | ""
}
```

where:

- `failure` is `null` on success and a OONI failure otherwise (see the
`df-007-errors.md` document for more information).

A future draft of this specification may include more fields.

#### QUICHandshakeMeasurement

`QUICHandshakeMeasurement` is (currently) an alias for `TLSHandshakeMeasurement`.

```
QUICHandshakeMeasurement = TLSHandshakeMeasurement
```

#### HTTPRoundTripMeasurement

`HTTPRoundTripMeasurement` has the following structure:

```
HTTPRoundTripMeasurement = {
  "request": {},
  "response": {}
}
```

where `request` is an `HTTPRequestMeasurement` and `response` is an
`HTTPResponseMeasurement`.

`HTTPRequestMeasurement` has the following structure:

```
HTTPRequestMeasurement = {
  "method": "",
  "url": "",
  "headers": {}
}
```

where:

- `method` is the request method;

- `url` is the request URL;

- `headers` is an optional map from string to a list of strings
containing the request headers (if any);

`HTTPResponseMeasurement` has the following structure:

```
HTTPResponseMeasurement = {
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

A future draft of this specification may include more fields.

### Response example

TBD

## Algorithm

This section describes algorithms and data structures to implement the test helper. An
implementation is free to choose different algorithms and data structures
as long as the end result is functionally equivalent to what we describe in here.

The top-level algorithm consists of three major steps:

1. preliminary checks;
2. URLs discovery;
3. endpoints measurement.

We will discuss each step separately.

### Preliminary checks

The test helper returns `400` to the caller if:

1. the request method is not `POST`; or
2. it cannot read request body; or
3. it cannot parse request body as a JSON object; or
4. the `CtrlRequest.url` field is empty; or
5. the `CtrlRequest.url` field is not a valid URL.

The test helper will then resolve the domain inside the URL
using a DNS resolver. Such a resolver must not be the system
one. We should instead configure a DoH resolver with a well
known provider (e.g., Google or Cloudflare) and consistently
use that for all DNS operations. This design choice ensures
that the test helper behaves consistently regardless of its
deployment environment. Additionally, by using a secure
transport, we eliminate the risk of query tampering.

If the result of such a DNS resolution is an error, the test
helper returns to the caller a `CtrlResponse` indicating that
such an error occurred. Assuming the input URL is
`http://nonexistent.com` and the error is `dns_nxdomain_error`,
the `CtrlResponse` will be as follows in this case:

```JSON
{
  "urls": [{
    "url": "http://nonexistent.com",
    "dns": {
      "failure": "dns_nxdomain_error",
      "addrs": []
    },
    "endpoints": []
  }]
}
```

The reason why we check for a nonexisting domain immediately
is that around 1% of the domains in the test lists are not
registered anymore (according to [ooni/probe#1727](
https://github.com/ooni/probe/issues/1727)). Given the burden
of keeping the test lists _always_ up to date, the test
helper provides for this relatively common error case and
includes code to handle it in the most graceful way.

If the preliminary step complete successfully, the test
helper will then discover all the URLs that matter.

### URLs discovery

The test helper creates an ordinary HTTP client with
redirection enabled, support for cookies, and using the
same DoH resolver used in the previous step. With such
an HTTP client, the test helper follows any possible
redirection from the input URL. This step also
includes discovering HTTP/3 endpoints. We discover
them using `Alt-Svc`. In the future, we should
also consider using DNS SVCB.

This HTTP client will use the `accept`, `accept-language`,
and `user-agent` headers provided by the client in the
`headers` field of the `CtrlRequest`. All other headers
will be silently ignored.

The output of this step consists of three lists of requests, for
HTTP, HTTPS, and HTTP/3 respectively. Depending on the scheme
of the input URL and on discovery results, some lists may be
empty. For example, if the input URL is `https://www.example.com`
and there is no HTTP/3 availability, then only the HTTPS
list will contain information, and the other two will be empty.
If there is no redirection, a list will contain a
single request for the input URL.

The information stored for each redirection should be
enough to redo the same request with equal headers (including
cookies). We do not fetch bodies at this stage,
because doing that would slow down the operations.

At present, the test helper is not designed to cover the
case where the redirection chain fails midway. This would
happen, for example, if the input URL was a `bit.ly` URL
pointing to an URL containing a nonexistent domain. We will
revisit this decision if it turns out that this case is
quite common (currently, it's not). For now, if a chain fails
midway, we will just ignore it. If all the three chains
are empty at the end of the step, then we assume there was
an error in the test helper. This condition could occur, for
example, if there's an issue with our DNS resolver. In
such a case, we return a `500` error.

### Endpoints measurement

The test helper walks the HTTP, HTTPS, and HTTP/3 lists. For
each request in the list, the test helper executes this algorithm:

- input:
    - `URL`: already parsed HTTP URL (from the discovery step)
    - `headers`: map containing request headers (from the discovery step)
    - `clientResolutions`: map from string (domain name) to list of strings (IP addresses resolved by the client)
    - `version`: QUIC version or empty string to mean "use TCP"
- output:
    - `m`: a `URLMeasurement`
- algorithm:
    1. save `m.url` immediately
    2. call `DNSResolver` (see below) with
         - input:
             - `URL.hostname` 
         - output:
             - `DNSMeasurement` as `url.dns`
    3. init `addrs` as *a copy of* `url.dns.addrs`
    4. if `clientResolutions` contains an entry for `URL.hostname` merge its addresses with `addrs` and remove duplicates
    5. create a list of endpoints `endpoints` using `addrs` and `URL.port` or the default port for `URL.scheme`
    6. for each `endpoint` in `endpoints`:
        1. if `URL.scheme` is `https` and `version` is set, call `H3EndpointMeasurer` (see below)
        2. else if `URL.scheme` is `https`, call `HTTPSEndpointMeasurer` (see below)
        3. else if `URL.scheme` is `http`, call `HTTPEndpointMeasurer` (see below)

The output of this step is a list of `URLMeasurement`, one for
each previously discovered URL. In turn, each `URLMeasurement` contains
an `EndpointMeasurement` for each endpoint. We will reuse headers from the
previous step, where we used a cookie aware client. This means that we
will reuse previously discovered cookies. There is, in fact, a small fraction
of URLs in the test list that fail to properly redirect without the correct
cookies (0.09% according to [ooni/probe#1727](https://github.com/ooni/probe/issues/1727)).

### HTTPEndpointMeasurer

- input:
    - `URL`: already parsed HTTP URL
    - `headers`: map containing optional request headers
    - `endpoint`: TCP endpoint to use
- output:
    - `m`: a `HTTPEndpointMeasurement`
- algorithm:
    1. save `m.protocol` and `m.endpoint` immediately
    2. call `TCPConnector`
        - input:
            - `endpoint`
        - output:
            - `TCPConnectMeasurement` as `m.tcp_connect`
            - TCP connection as `tcpConn`
    3. if `tcpConn` is `nil`, return
    4. construct a single-use HTTP client (`clnt`) w/o redirection using `tcpConn`
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
- output:
    - `m`: a `HTTPEndpointMeasurement`
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
    6. construct a single-use HTTP client (`clnt`) w/o redirection using `tlsConn`
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
    4. construct a single-use HTTP client (`clnt`) w/o redirection using `sess`
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
    2. add `headers` to `req`
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
    2. perform DNS resolution for `domain` using the same DoH resolver of previous steps
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

## Limitations

This draft specification does not address these issues:

1. adding logic to the test helper to choose whether it is smart
to continue processing due to other considerations. For example, if
we're redirected from `http://facebook.com/` to `https://facebook.com/`,
it may be reasonable to stop the measurement instead of being
further redirected to, say, `https://facebook.com/en_US/login.php`. This
could be done by postprocessing the results of the discovery step.

2. whether the amount of information included in each `EndpointMeasurement{}`
is such that the OONI Probe can unambiguously redo the same operation.

3. how to choose whether the Probe should read whole response bodies (which
seems useful to detect throttling) or stop reading early.

4. we do not discuss how to treat IP addresses resolved by the client in a
more suspicious way, and which check we could perform directly inside of the
test helper to discover right away DNS censorship.

These problems will be solved at a later time.

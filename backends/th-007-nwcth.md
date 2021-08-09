# New Web Connectivity Test Helper Spec

* _Author_: sbs
* _Version_: 2021-08-09-005
* _Status_: alpha

This document describes a draft specification for the new web connectivity test
helper. We tentatively expose this new API as `/api/unstable/wcth`.

A future version of this document will also provide a design rationale.

## Common definitions

This section introduces the notation with which we define types.

### Null

We use `null` to indicate null.

### Integers

We use `0` to indicate any integer value.

### Strings

We use `""` to represent any string.

If a string can only assume the value `foo`, then we write `"foo"`.

If `Foo` is a more complex pattern, then we write `"/Foo/"`.

We define the following patterns:

- `/URL/` matches any valid URL;

- `/Endpoint/` matches any string containing a valid IPv4/IPv6
address followed by `:` and a port number. In this representation,
IPv6 addresses must be quote using `[` and `]`. For example,
`[::1]:443`;

- `/IPAddr/` matches any IPv4/IPv6 address.

### Arrays

We represent an array using `[]`. If an array contains only
a specific type, we append such type to `[]`. If `Foo` is
a type, `[]Foo` is an array of `Foo` types.

### Objects

We represent any object using `{}`. Object keys are always
strings. Object values could be of any type.

`Foo{}` means an object of type `Foo`. Whenever we define
an object, we also explicitly describe its structure.

### Union Types

We use `|` to indicate that a type is the
[union](https://en.wikipedia.org/wiki/Algebraic_data_type)
of two types.

### Errors

`OONIFailure` is either `null` or a OONI failure string:

```
OONIFailure = null | OONIFailureString
```

(See `df-007-errors` for more information on failures.)

### HTTP Headers

`HTTPHeaders` is a map from string (the header key) to
a list of strings (the header values).

## Request message

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

- `headers` is optional, its type is equivalent to a Go `map[string][]string`,
and contains HTTP headers the test helper should use in the measurement;

- `endpoints` is an optional list of string-serialized endpoints for the
domain inside `url` discovered by the client.

An endpoint is:

- an IPv4 address followed by `:` followed by a valid port number; or

- an IPv6 address quoted using `[` and `]` followed by `:`
followed by a valid port number.

For example, `1.2.3.4:5`, `[::1]:5`.

## Response message

The response message (`CtrlResponse`) contains these fields:

```
CtrlResponse = {
  "urls": []
}
```

where `urls` is a list of `URLMeasurement`s:

```
URLMeasurement = {
  "index": 0,
  "url": "",
  "dns": {},
  "endpoint": {}
}
```

where:

- `index` is the unsigned integer index (starting from zero) of this
`URLMeasurement` within the list in `CtrlResponse.urls`;

- `url` is a valid string-serialized URL and contains
the URL to which this `URLMeasurement` refers;

- `dns` is a `DNSMeasurement` structure (see below) and contains
the result of the DNS lookup of the domain inside `url`;

- `endpoint` contains an `EndpointMeasurement` for each endpoint
we discovered for the domain inside `url`.

Data consumers SHOULD NOT trust the order with which `URLMeasurement`
are presented inside `CtrlResponse.urls`. Instead, they should rely
on the `index` field to sort the list of `URLMeasurement`, knowing that
the first measurement has index zero the index is an unsugned int.

The `URLMeasurement` with index zero is the one originally requested
to the test helper. Subsequent measurements derive from HTTP redirection or
from follow up measurements (e.g., testing HTTP3 endpoints discovered
while performing HTTPS measurements).

### DNSMeasurement

The `DNSMeasurement` struct is as follows:

```
{
  "failure": OONIFailure,
  "addrs": []"/IPAddr/",
}
```

- `failure` is a `OONIFailure` as defined above and represent the error that occurred
when performing the DNS resolution (or `null` on success);

- `addrs` is a list of strings containing valid IPv4/IPv6 addresses and is the
(possibly empty) list of IP addresses returned by the DNS resolution.

### EndpointMeasurement

The `EndpointMeasurement` is the union of `HTTPMeasurement` and `H3Measurement`:

```
EndpointMeasurement = HTTPMeasurement | H3Measurement
```

`HTTPMeasurement` has the following structure:

```
{
  "endpoint": "/Endpoint/",
  "protocol": "http" | "https",
  "tcp_connect": TCPConnectMeasurement{},
  "tls_handshake": TLSHandshakeMeasurement{},
  "http_request": HTTPRequestMeasurement{}
}
```

- `endpoint` is a string containing an endpoint (as defined above);

- `protocol` is either `"http"` or `"https"`;

- the other fields are defined below.

`H3Measurement` has the following structure:

```
{
  "endpoint": "/Endpoint/",
  "protocol": "h3" | "h3-29" | ...,
  "quic_handshake": TLSHandshakeMeasurement{},
  "http_request": HTTPRequestMeasurement{}
}
```

- `endpoint` is a string containing an endpoint (as defined above);

- `protocol` is either `"h3"` or `"h3-29"` or any other supported HTTP/3 protocol;

- the other fields are defined below.

`TCPConnectMeasurement` is like:

```
{
  "failure": OONIFailure
}
```

`TLSHandshakeMeasurement` is like:

```
{
  "failure": OONIFailure
}
```

`HTTPRequestMeasurement` is like:

```
{
  "body_length": 0,
  "failure": OONIFailure,
  "headers": HTTPHeaders,
  "status_code": 0,
}
```

## Test Helper Algorithm

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

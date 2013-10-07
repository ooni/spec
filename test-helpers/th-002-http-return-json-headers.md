# Specification version number

2013-09-26-000

# Specification name

  HTTP Return JSON Headers Test Helper

# Helper preconditions

  * An Internet connection
  * An Internet-Reachable TCP Port, typically port 80.

# Expected impact

  Ability to help an ooni-probe client determine if the HTTP request headers
  have been modified in transit.

# Expected inputs

  An HTTP request.

## Required input data

  An HTTP Request with Headers.

## Semantics

  This helper processes the HTTP Request Line and the Request Headers and
  returns them in a JSON datastructure in the order it received them.  It is
  implemented as a twisted.basic.LineReceiver and expects the first line to
  contain the HTTP Request Line, and the following to contain the HTTP Request
  Headers. Once All of the Request Headers have been received the response is
  written and the transport closed. If an invalid header is received, it is
  not included in the response. Malformed or invalid requests will timeout
  after 12 hours.

# Helper description

  An HTTP Request Echo service.

# Expected output

  The HTTP Request and Request Headers as seen by the test helper.

## Required output data

  The HTTP Request line and HTTP Request Headers.

## Semantics

  The returned JSON dictionary contains the keys 'request_headers' and
  'request_line'. The value for 'request_line' is a string, and the value for
  'request_headers' is an ordered list of lists, where the sublists follow the
  format ['Header-Name', 'Header-Value'].

  e.g.

    {
      'request_headers':
        [['User-Agent', 'IE6'], ['Content-Length', 200]]
      'request_line':
        'GET / HTTP/1.1'
    }

## Possible conclusions

  The HTTP Return JSON Headers test helper can be used by ooni-probe tests to
  determine if the HTTP Headers or HTTP Request Line have been modified in
  transit. 

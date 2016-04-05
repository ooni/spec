# Specification version number

2013-10-08-000

# Specification name

HTTP Invalid Request Line test

# Test preconditions

  * An internet connection.
  * An ooni-backend providing the tcp-echo test helper.

# Expected impact

The goal of this test is to do some very basic and not very
noisy fuzzing on the HTTP request line. We generate a series
of requests that are not valid HTTP requests. If the data we get back is not what we have sent, then tampering is occurring.

# Expected inputs

An ooni-backend tcp-echo test helper must be provided with
option -b.

Optionally, a port other than the default (80) may be
specified with option -p.

# Test description

The goal of this test is to test sending invalid HTTP
requests in order to trick middleboxes, such as caching
proxies like squid, into revealing themselves.

This is for example what squid will return when performing
such request:

    HTTP/1.0 400 Bad Request
    Server: squid/2.6.STABLE21
    Date: Sat, 23 Jul 2011 02:22:44 GMT
    Content-Type: text/html
    Content-Length: 1178
    Expires: Sat, 23 Jul 2011 02:22:44 GMT
    X-Squid-Error: ERR_INVALID_REQ 0
    X-Cache: MISS from cache_server
    X-Cache-Lookup: NONE from cache_server:3128
    Via: 1.0 cache_server:3128 (squid/2.6.STABLE21)
    Proxy-Connection: close

The various types of invalid request that we do are:

## test_random_invalid_method

Performs a request with a HTTP method that is a random 4
character string. e.g.

    request_line = randomSTR(4) + " / HTTP/1.1\n\r"

## test_random_invalid_field_count

Performs a request with an invalid number of random fields, e.g.

    request_line = ' '.join(randomStr(5) for x in range(4)) + '\n\r'

## test_random_big_request_method

Send a 1024 byte request method, e.g.

    request-line = randomStr(1024) + ' / HTTP/1.1\n\r'

## test_random_invalid_version_number

Performs a request with an invalid version, e.g.

    request_line = 'GET / HTTP/' + randomStr(3)

Each of these tests may trigger some bugs in the HTTP parsers
of transparent HTTP proxies.

If the response is not what we have sent, then tampering is
occurring.

# Expected output

## Parent data format

df-xxx-tcpt

## Required output data

In addition to the parent data format, the key 'tampering' is
added to the report. If the sent data does not match the
received data from the test helper, 'tampering' is set to
True. Otherwise, it is set to False.

## Semantics

'tampering': true|false

## Possible conclusions

It may reveal the existance of a middlebox such as a
transparent HTTP proxy inbetween the ooni-probe and
ooni-backend.

## Example output sample

    ###########################################
    # OONI Probe Report for http_invalid_request_line (0.2)
    # Wed Oct  9 10:49:12 2013
    ###########################################
    ---
    input_hashes: []
    options: [-b, 12.34.56.78 ]
    probe_asn: AS1234
    probe_cc: US
    probe_ip: 127.0.0.1
    software_name: ooniprobe
    software_version: 1.0.0-rc3
    start_time: 1381315752.679267
    test_name: http_invalid_request_line
    test_version: '0.2'
    ...
    ---
    input: null
    received: ["706J / HTTP/1.1\n\r"]
    sent: ["706J / HTTP/1.1\n\r"]
    tampering: false
    ...
    ---
    input: null
    received: ["LfADmOTGDIpT5510eeqqc7CmQQy4KOZt2BYaVs1lU7he8Es9oF3ZlBrBaYGhho7s9kTbltLuR283nJwGxAcuaOQy601I2Fe7lOkc1U3pinDqhnQaoCl27jGQfVgTmJLi5eAnKyNUrM8ywDvCxo5PWUw3NKVi3eHkWdV475SkW7AeXGfIrtNsfWHkfoUOjjcGw5nvM97jzbGqMsP81EaF18TTCawnUR62X6WlSfo6Od9gM4WFj2G6z8tNlE9werVQIvh3bjApu6zrhJZZko6nmZz46IbAOA2StgUVp0j4CtliF5EVaWBymTXyxM0WiN3Lg13hAA1uDAbi5VzvjyTK3TUwuna6YAvZXLaM4cch4MV445eSWMuc6704PO6WUW9IzBrY84PK6JmIaWPZ0Sa7VFTF1ItgSeZKQp2Hnm8fqIjxKT9kxNppcPLW5opBbYnOEbYE2f29jxa2GbG6z8Q1rKTdtfZx90aMdjSHG6F6DHt9ZcQg8lAtYWyPtrhJKs0znnAMH2vZ5w69cIbsS101peQYUHizmTg34o1ORBAQIyWQot2HplvGtAqWlUcEu6KWnDbdlSJLAX5LAjmT8JULpyuh221n2DgGScat12IgxIIyBVYZ4mja3HPFE2T4ihcEM6EStt0aRcLm444BCxCORIditFggvlwXRcXLoYxmAkySoUPp8iZk6azk3pxZYiaPdhjmL6oszWlPwBsWzJyhnr9kiRfX6HQ9a2h2RZPTT2LdEVadmwd6V3xTnT84Mv3F61U9V8lajlXlW67PQYf1fjK2AwVAPRUsW8ulgWUeJYIrXrVIBvXxdQ5FxJjfw75M8h8ztRiy4e9T882gmSkCCBmmXkeiltlkcnjJ9uwyQ5hBW43s2nfWCCPEKAsRQbZXnJGdNEUgQWrM0Px6eHgrrDwJN8XJ8GaDF1s6Wq6ggptTleKnOouIoJIxEdyDxXSSGQVMRGNsvwlMc76KCPeutBMOPUdDd67Jry1VtNxRWQ4Qu6C2n2xJ9cDL2ElJX5EI\
        \ / HTTP/1.1\n\r"]
    sent: ["LfADmOTGDIpT5510eeqqc7CmQQy4KOZt2BYaVs1lU7he8Es9oF3ZlBrBaYGhho7s9kTbltLuR283nJwGxAcuaOQy601I2Fe7lOkc1U3pinDqhnQaoCl27jGQfVgTmJLi5eAnKyNUrM8ywDvCxo5PWUw3NKVi3eHkWdV475SkW7AeXGfIrtNsfWHkfoUOjjcGw5nvM97jzbGqMsP81EaF18TTCawnUR62X6WlSfo6Od9gM4WFj2G6z8tNlE9werVQIvh3bjApu6zrhJZZko6nmZz46IbAOA2StgUVp0j4CtliF5EVaWBymTXyxM0WiN3Lg13hAA1uDAbi5VzvjyTK3TUwuna6YAvZXLaM4cch4MV445eSWMuc6704PO6WUW9IzBrY84PK6JmIaWPZ0Sa7VFTF1ItgSeZKQp2Hnm8fqIjxKT9kxNppcPLW5opBbYnOEbYE2f29jxa2GbG6z8Q1rKTdtfZx90aMdjSHG6F6DHt9ZcQg8lAtYWyPtrhJKs0znnAMH2vZ5w69cIbsS101peQYUHizmTg34o1ORBAQIyWQot2HplvGtAqWlUcEu6KWnDbdlSJLAX5LAjmT8JULpyuh221n2DgGScat12IgxIIyBVYZ4mja3HPFE2T4ihcEM6EStt0aRcLm444BCxCORIditFggvlwXRcXLoYxmAkySoUPp8iZk6azk3pxZYiaPdhjmL6oszWlPwBsWzJyhnr9kiRfX6HQ9a2h2RZPTT2LdEVadmwd6V3xTnT84Mv3F61U9V8lajlXlW67PQYf1fjK2AwVAPRUsW8ulgWUeJYIrXrVIBvXxdQ5FxJjfw75M8h8ztRiy4e9T882gmSkCCBmmXkeiltlkcnjJ9uwyQ5hBW43s2nfWCCPEKAsRQbZXnJGdNEUgQWrM0Px6eHgrrDwJN8XJ8GaDF1s6Wq6ggptTleKnOouIoJIxEdyDxXSSGQVMRGNsvwlMc76KCPeutBMOPUdDd67Jry1VtNxRWQ4Qu6C2n2xJ9cDL2ElJX5EI\
        \ / HTTP/1.1\n\r"]
    tampering: false
    ...
    ---
    input: null
    received: ["7Mb5L DLVz6 4r2HB HIEfp\n\r"]
    sent: ["7Mb5L DLVz6 4r2HB HIEfp\n\r"]
    tampering: false
    ...
    ---
    input: null
    received: ["GET / HTTP/QGc\n\r"]
    sent: ["GET / HTTP/QGc\n\r"]
    tampering: false
    ...

# Privacy considerations

A middlebox could reveal the ooni-probe IP address by the
X_FORWARDED_FOR header.

# Specification version number

0.2.0

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

```
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
```

The various types of invalid request that we do are:

## test_random_invalid_method

Performs a request with a HTTP method that is a random 4
character string. e.g.

```
request_line = randomSTR(4) + " / HTTP/1.1\n\r"
```

## test_random_invalid_field_count

Performs a request with an invalid number of random fields, e.g.

```
request_line = ' '.join(randomStr(5) for x in range(4)) + '\n\r'
```

## test_random_big_request_method

Send a 1024 byte request method, e.g.

```
request-line = randomStr(1024) + ' / HTTP/1.1\n\r'
```

## test_random_invalid_version_number

Performs a request with an invalid version, e.g.

```
request_line = 'GET / HTTP/' + randomStr(3)
```

Each of these tests may trigger some bugs in the HTTP parsers
of transparent HTTP proxies.

If the response is not what we have sent, then tampering is
occurring.

## test_squid_cache_manager

Performs a request triggering a response from on-path squid
caching servers, particularly targeting the built-in
cache management functionality of the proxy.

```
request_line = 'GET cache_object://localhost/ HTTP/1.0\n\r'
```

If a squid proxy receives such a request it will generally
respond that the request has been denied, or depending
on the configuration may respond with an index of cache
management options, but without revealing sensitive
information about the proxy itself.

# Expected output

## Parent data format

df-004-tcpt

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

```
{
    "bucket_date": "2015-12-01",
    "data_format_version": "0.2.0",
    "id": "f116e9a4-a648-48c8-b3b7-cca7bd84d069",
    "input": null,
    "options": [],
    "probe_asn": "AS786",
    "probe_cc": "GB",
    "probe_ip": "127.0.0.1",
    "report_filename": "2015-12-01/20151201T072512Z-GB-AS786-http_invalid_request_line-ZXjsOzoy3gl0f71b35et9kLZsTkc3W1yLYMHSLVLN6buJvnXveywSBM24C2YPtfv-0.1.0-probe.json",
    "report_id": "ZXjsOzoy3gl0f71b35et9kLZsTkc3W1yLYMHSLVLN6buJvnXveywSBM24C2YPtfv",
    "software_name": "ooniprobe",
    "software_version": "1.3.1",
    "test_helpers": {
        "backend": "213.138.109.232"
    },
    "backend_version": "1.1.4",
    "input_hashes": [],
    "probe_city": null,
    "test_keys": {
        "received": [
            "53LC / HTTP/1.1\n\r",
            "",
            "dNnLP MHIdC s5vst k7Ir2\n\r",
            "yWoBwUKUnlMfZQ1BDFIHJsLAU9PNKUVOzOJ1s7BdXKlhAnALegIOkvEsq8QCHNKqFoMk5ndpSa3bE99hIVXZSK7hCGa6wk770C9WJoL7VLYDeGRYWEhoYF2eg8PERFK4CGYXuuCLkr0ScT3esnj66ypgzpuP85PpCSERP5qc0DNYzHF4edM9RcDxttfMU0X5HyQ0EzKCMX4dcKlB6DLianESEKFKE3VwRht2cwUdLs6IXG5fsUBLEiJUQEHzFENpr40dPvcnk1KoTc4UZr5EP9JlNJ9f7fx6Ps6m2QzxyXkVT8UjPYbx2Rk6EO27nfd21iKtzZyZzUhyHxVQtLS58hzeQumCwAMdOi5FmwiDG6vFS1THTODJdwovw7V0CsaXvFwkJmBagWVvRR3zWQ9o509BnK9bxvBIo5cgFdyBlVHSH3Bbq0kXyarVAoQjaOo0C8Tb8lr5Ug7FFelGnBmdKNmNQj1QmmiobrcUMY22JKdxp81Z0R1AoyjLjeJQ7NNlhpbM6REiHladSmVmgBPChjjFQJn2TGOmSAIQJAvnsREpdMyuRemTA5Vb0QMIUmEVvpIKV8HOhBaniz389ftxglIizaOF3pacUIBycUwLermpolNatVn6BbDSCNJGCwil8NVUBtfKQqTlEgQk1zo3LNfryrKEd5M4PBdOzqIFHb0zhsY8NsSy7geXOZfMnNRNfu0dsMDchiLYHzQD0qPg2heEsJ3w8usyH462eqUcNF5qNOt47tC53rnbChT8Tjktr55LrJQhvKg8QRqWg2HuTnM4eMxSjdF8iCUzxEhDHkoxah5v6iQPmRE7qCUxf2Jwyi404MLX0gGvoawukkrEiVlhcHrQo3yrnAqIRx7mYhp9izzmWw62e35xzpFD3rxhAlrLTBr3bJQPBXvMzkAY62UHt1pAQPCaDojEo1WrHKnb8TMsNUS8u5yYumvbuxsLSJFWIjkrqf2G6rm1aVo95jxx9Uvx665eJ9tWRAT6rD4A1QoXVg34m20ywW1n3voP / HTTP/1.1\n\r"
        ],
        "sent": [
            "53LC / HTTP/1.1\n\r",
            "GET / HTTP/g8z\n\r",
            "dNnLP MHIdC s5vst k7Ir2\n\r",
            "yWoBwUKUnlMfZQ1BDFIHJsLAU9PNKUVOzOJ1s7BdXKlhAnALegIOkvEsq8QCHNKqFoMk5ndpSa3bE99hIVXZSK7hCGa6wk770C9WJoL7VLYDeGRYWEhoYF2eg8PERFK4CGYXuuCLkr0ScT3esnj66ypgzpuP85PpCSERP5qc0DNYzHF4edM9RcDxttfMU0X5HyQ0EzKCMX4dcKlB6DLianESEKFKE3VwRht2cwUdLs6IXG5fsUBLEiJUQEHzFENpr40dPvcnk1KoTc4UZr5EP9JlNJ9f7fx6Ps6m2QzxyXkVT8UjPYbx2Rk6EO27nfd21iKtzZyZzUhyHxVQtLS58hzeQumCwAMdOi5FmwiDG6vFS1THTODJdwovw7V0CsaXvFwkJmBagWVvRR3zWQ9o509BnK9bxvBIo5cgFdyBlVHSH3Bbq0kXyarVAoQjaOo0C8Tb8lr5Ug7FFelGnBmdKNmNQj1QmmiobrcUMY22JKdxp81Z0R1AoyjLjeJQ7NNlhpbM6REiHladSmVmgBPChjjFQJn2TGOmSAIQJAvnsREpdMyuRemTA5Vb0QMIUmEVvpIKV8HOhBaniz389ftxglIizaOF3pacUIBycUwLermpolNatVn6BbDSCNJGCwil8NVUBtfKQqTlEgQk1zo3LNfryrKEd5M4PBdOzqIFHb0zhsY8NsSy7geXOZfMnNRNfu0dsMDchiLYHzQD0qPg2heEsJ3w8usyH462eqUcNF5qNOt47tC53rnbChT8Tjktr55LrJQhvKg8QRqWg2HuTnM4eMxSjdF8iCUzxEhDHkoxah5v6iQPmRE7qCUxf2Jwyi404MLX0gGvoawukkrEiVlhcHrQo3yrnAqIRx7mYhp9izzmWw62e35xzpFD3rxhAlrLTBr3bJQPBXvMzkAY62UHt1pAQPCaDojEo1WrHKnb8TMsNUS8u5yYumvbuxsLSJFWIjkrqf2G6rm1aVo95jxx9Uvx665eJ9tWRAT6rD4A1QoXVg34m20ywW1n3voP / HTTP/1.1\n\r"
        ],
        "tampering": true
    },
    "test_name": "http_invalid_request_line",
    "test_runtime": 5.7580039501,
    "test_start_time": "2015-12-01 07:25:12",
    "test_version": "0.2"
}
```

# UTF-8 considerations

A middlebox may respond with a purely or partially binary response that would not
be JSON serializable. If that happens, the related entry in the `sent` key must be
encoded using the same format used for binary HTTP response bodies, e.g.:

```json
{
        "received": [
            "",
            "",
            "",
            "",
            {
                "data": "AQ05bwxG+MIS9g9MCV8tzSk=",
                "format": "base64"
            }
        ],
}
```

# Privacy considerations

A middlebox could reveal the ooni-probe IP address by the
X_FORWARDED_FOR header.

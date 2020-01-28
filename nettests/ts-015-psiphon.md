# Specification version number

0.3.3

# Specification name

Psiphon

# Test preconditions

None

# Expected impact

Ability to measure whether Psiphon is working from the given network vantage point.

# Expected inputs

The nettest will fetch a Psiphon configuration file from OONI servers and MAY
possibly cache this configuration file for future reuse.

# Test description

This test creates a Psiphon tunnel and then uses it to fetch the
`https://www.google.com/humans.txt` webpage.

It is important to wipe the state directory to ensure that Psiphon
could bootstrap from scratch every time.

# Expected output

## Parent data format

- `df-001-httpt`
- `df-002-dnst` (since 2020-01-09 in ooni/probe-engine)
- `df-006-tlshandshake` (since 2020-01-11 in ooni/probe-engine)

Because of the way in which Psiphon works, we expect DNS queries
to always be `null`. If it's not `null`, this means we may be
performing DNS resolutions without using Psiphon.

## Required output data

- `bootstrap_time` (`float64`): time to bootstrap in seconds or
zero if the bootstrap did not succeed;

- `failure` (`string|null`): string indicating the error that occurred
or `null` if no error occurred;

- `max_runtime` (`float64`): timeout for the whole nettest.

## Possible conclusions

We can determine whether or not Psiphon is able to bootstrap. We can
determine whether or not a specific URL is reachable via Psiphon.

| `bootstrap_time` | `failure`     | Conclusion                     |
| :--------------: | ------------- | ------------------------------ |
| 0                | not `null`    | Error in bootstrapping Psiphon |
| > 0              | not `null`    | Error in using Psiphon         |
| > 0              | `null`        | Working                        |
| 0                | `null`        | Invalid (_should not happen_)  |

## Example output sample

```JSON
{
  "data_format_version": "0.3.4",
  "measurement_start_time": "2020-01-11 16:49:24",
  "test_runtime": 16.896564945,
  "probe_asn": "AS30722",
  "probe_cc": "IT",
  "probe_ip": "127.0.0.1",
  "report_id": "20200111T164924Z_AS30722_lKxNuG9w1Av9hyl49LSGIS0PxoaMq7aMarT8mwBjvnWVBAI5Hc",
  "resolver_asn": "AS15169",
  "resolver_ip": "172.217.34.2",
  "resolver_network_name": "Google LLC",
  "software_name": "miniooni",
  "software_version": "0.1.0-dev",
  "test_keys": {
    "agent": "redirect",
    "bootstrap_time": 6.604589285,
    "failure": null,
    "max_runtime": 60,
    "queries": null,
    "requests": [
      {
        "failure": null,
        "request": {
          "body": "",
          "body_is_truncated": false,
          "headers_list": [
            [
              ":path",
              "/humans.txt"
            ],
            [
              ":scheme",
              "https"
            ],
            [
              "Accept",
              "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
            ],
            [
              "Accept-Language",
              "en-US;q=0.8,en;q=0.5"
            ],
            [
              "User-Agent",
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
            ],
            [
              ":authority",
              "www.google.com"
            ],
            [
              ":method",
              "GET"
            ]
          ],
          "headers": {
            ":authority": "www.google.com",
            ":method": "GET",
            ":path": "/humans.txt",
            ":scheme": "https",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US;q=0.8,en;q=0.5",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
          },
          "method": "GET",
          "tor": {
            "exit_ip": null,
            "exit_name": null,
            "is_tor": false
          },
          "url": "https://www.google.com/humans.txt"
        },
        "response": {
          "body": "Google is built by a large team of engineers, designers, researchers, robots, and others in many different sites across the globe. It is updated continuously, and built with more tools and technologies than we can shake a stick at. If you'd like to help us out, see careers.google.com.\n",
          "body_is_truncated": false,
          "code": 200,
          "headers_list": [
            [
              "X-Content-Type-Options",
              "nosniff"
            ],
            [
              "Alt-Svc",
              "quic=\":443\"; ma=2592000; v=\"46,43\",h3-Q050=\":443\"; ma=2592000,h3-Q049=\":443\"; ma=2592000,h3-Q048=\":443\"; ma=2592000,h3-Q046=\":443\"; ma=2592000,h3-Q043=\":443\"; ma=2592000"
            ],
            [
              "Accept-Ranges",
              "bytes"
            ],
            [
              "Content-Length",
              "286"
            ],
            [
              "Date",
              "Sat, 11 Jan 2020 16:49:31 GMT"
            ],
            [
              "Expires",
              "Sat, 11 Jan 2020 16:49:31 GMT"
            ],
            [
              "Cache-Control",
              "private, max-age=0"
            ],
            [
              "Last-Modified",
              "Mon, 01 Jul 2019 19:30:00 GMT"
            ],
            [
              "Vary",
              "Accept-Encoding"
            ],
            [
              "Content-Type",
              "text/plain"
            ],
            [
              "Server",
              "sffe"
            ],
            [
              "X-Xss-Protection",
              "0"
            ]
          ],
          "headers": {
            "Accept-Ranges": "bytes",
            "Alt-Svc": "quic=\":443\"; ma=2592000; v=\"46,43\",h3-Q050=\":443\"; ma=2592000,h3-Q049=\":443\"; ma=2592000,h3-Q048=\":443\"; ma=2592000,h3-Q046=\":443\"; ma=2592000,h3-Q043=\":443\"; ma=2592000",
            "Cache-Control": "private, max-age=0",
            "Content-Length": "286",
            "Content-Type": "text/plain",
            "Date": "Sat, 11 Jan 2020 16:49:31 GMT",
            "Expires": "Sat, 11 Jan 2020 16:49:31 GMT",
            "Last-Modified": "Mon, 01 Jul 2019 19:30:00 GMT",
            "Server": "sffe",
            "Vary": "Accept-Encoding",
            "X-Content-Type-Options": "nosniff",
            "X-Xss-Protection": "0"
          }
        },
        "transaction_id": 1
      }
    ],
    "socksproxy": "127.0.0.1:50221",
    "tls_handshakes": [
      {
        "cipher_suite": "TLS_AES_128_GCM_SHA256",
        "failure": null,
        "negotiated_protocol": "h2",
        "peer_certificates": [
          {
            "data": "MIIEwDCCA6igAwIBAgIRANJ+xM2QlEbUAgAAAABRORQwDQYJKoZIhvcNAQELBQAwQjELMAkGA1UEBhMCVVMxHjAcBgNVBAoTFUdvb2dsZSBUcnVzdCBTZXJ2aWNlczETMBEGA1UEAxMKR1RTIENBIDFPMTAeFw0xOTEyMTAwODQzMTRaFw0yMDAzMDMwODQzMTRaMGgxCzAJBgNVBAYTAlVTMRMwEQYDVQQIEwpDYWxpZm9ybmlhMRYwFAYDVQQHEw1Nb3VudGFpbiBWaWV3MRMwEQYDVQQKEwpHb29nbGUgTExDMRcwFQYDVQQDEw53d3cuZ29vZ2xlLmNvbTBZMBMGByqGSM49AgEGCCqGSM49AwEHA0IABMpx8ep3woTouGHYiYs0afuOqwWWXmXH1EJAm0G+RuG/VaAXalSWEuGupSQ+rmuB556aOYWnKhB+ViDlkZDVaYijggJUMIICUDAOBgNVHQ8BAf8EBAMCB4AwEwYDVR0lBAwwCgYIKwYBBQUHAwEwDAYDVR0TAQH/BAIwADAdBgNVHQ4EFgQUhyR9TgfjiU83pQATkCGk1XZEIvAwHwYDVR0jBBgwFoAUmNH4bhDrz5vsYJ8YkBug630J/SswZAYIKwYBBQUHAQEEWDBWMCcGCCsGAQUFBzABhhtodHRwOi8vb2NzcC5wa2kuZ29vZy9ndHMxbzEwKwYIKwYBBQUHMAKGH2h0dHA6Ly9wa2kuZ29vZy9nc3IyL0dUUzFPMS5jcnQwGQYDVR0RBBIwEIIOd3d3Lmdvb2dsZS5jb20wIQYDVR0gBBowGDAIBgZngQwBAgIwDAYKKwYBBAHWeQIFAzAvBgNVHR8EKDAmMCSgIqAghh5odHRwOi8vY3JsLnBraS5nb29nL0dUUzFPMS5jcmwwggEEBgorBgEEAdZ5AgQCBIH1BIHyAPAAdgCyHgXMi6LNiiBOh2b5K7mKJSBna9r6cOeySVMt74uQXgAAAW7vMPqrAAAEAwBHMEUCIHWSr1GbcFx5LaNeZkuIHOxI7cjzq1/0TqnY2L4Y71+TAiEAko/r0kdm3zF0M4gt9aaqJ9sEwEcOM6DIp6qQCs+wEhsAdgBep3P531bA57U2SH3QSeAyepGaDIShEhKEGHWWgXFFWAAAAW7vMPrJAAAEAwBHMEUCIQCFe7984L3Du1yGoGvEdNe820n0rrQDDhUCb7wK4jqB1QIgEubhxrJzaLqbohk0FOGIhExeJu5YuGowNbLrR7kX9mUwDQYJKoZIhvcNAQELBQADggEBAEAavCiIf6VTlBilS3CXJDQobkMtkkbMcyEIf2Ks/WTVHEXpWRI3J0CVWEDtgycvwIKT8L5cf/F4nT3atR3Un6uq1YFxWl/GoG8T8bhRC982xxLUZLQQCMUIOXwUJ/Mcc48aFKDQrJ0jjX4xcrEahQxbzRS5t5U5F4LUuFxMc1GocdJLmdDnjnCwqsb2gcVu6Jqy3jNrWawbnHmpjHirGYZBMDI0cIQxqH+KDKvDnH5llCvbl7Bch7vgUuZ56EAkIGps0K2nbqrI6E9U+cB0ajhhWlgEGFQgCrt/0yPd+PHyLiS6dph6BHLVgH67isTRM94f7kRe5MIkXkhKCG+6kIQ=",
            "format": "base64"
          },
          {
            "data": "MIIESjCCAzKgAwIBAgINAeO0mqGNiqmBJWlQuDANBgkqhkiG9w0BAQsFADBMMSAwHgYDVQQLExdHbG9iYWxTaWduIFJvb3QgQ0EgLSBSMjETMBEGA1UEChMKR2xvYmFsU2lnbjETMBEGA1UEAxMKR2xvYmFsU2lnbjAeFw0xNzA2MTUwMDAwNDJaFw0yMTEyMTUwMDAwNDJaMEIxCzAJBgNVBAYTAlVTMR4wHAYDVQQKExVHb29nbGUgVHJ1c3QgU2VydmljZXMxEzARBgNVBAMTCkdUUyBDQSAxTzEwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDQGM9F1IvN05zkQO9+tN1pIRvJzzyOTHW5DzEZhD2ePCnvUA0Qk28FgICfKqC9EksC4T2fWBYk/jCfC3R3VZMdS/dN4ZKCEPZRrAzDsiKUDzRrmBBJ5wudgzndIMYcLe/RGGFl5yODIKgjEv/SJH/UL+dEaltN11BmsK+eQmMF++AcxGNhr59qM/9il71I2dN8FGfcddwuaej4bXhp0LcQBbjxMcI7JP0aM3T4I+DsaxmKFsbjzaTNC9uzpFlgOIg7rR25xoynUxv8vNmkq7zdPGHXkxWY7oG9j+JkRyBABk7XrJfoucBZEqFJJSPk7XA0LKW0Y3z5oz2D0c1tJKwHAgMBAAGjggEzMIIBLzAOBgNVHQ8BAf8EBAMCAYYwHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMBIGA1UdEwEB/wQIMAYBAf8CAQAwHQYDVR0OBBYEFJjR+G4Q68+b7GCfGJAboOt9Cf0rMB8GA1UdIwQYMBaAFJviB1dnHB7AagbeWbSaLd/cGYYuMDUGCCsGAQUFBwEBBCkwJzAlBggrBgEFBQcwAYYZaHR0cDovL29jc3AucGtpLmdvb2cvZ3NyMjAyBgNVHR8EKzApMCegJaAjhiFodHRwOi8vY3JsLnBraS5nb29nL2dzcjIvZ3NyMi5jcmwwPwYDVR0gBDgwNjA0BgZngQwBAgIwKjAoBggrBgEFBQcCARYcaHR0cHM6Ly9wa2kuZ29vZy9yZXBvc2l0b3J5LzANBgkqhkiG9w0BAQsFAAOCAQEAGoA+Nnn78y6pRjd9XlQWNa7HTgiZ/r3RNGkmUmYHPQq6Scti9PEajvwRT2iWTHQr02fesqOqBY2ETUwgZQ+lltoNFvhsO9tvBCOIazpswWC9aJ9xju4tWDQH8NVU6YZZ/XteDSGU9YzJqPjY8q3MDxrzmqepBCf5o8mw/wJ4a2G6xzUr6Fb6T8McDO22PLRL6u3M4Tzs3A2M1j6bykJYi8wWIRdAvKLWZu/axBVbzYmqmwkm5zLSDW5nIAJbELCQCZwMH56t2Dvqofxs6BBcCFIZUSpxu6x6td0V7SvJCCosirSmIatj/9dSSVDQibet8q/7UK4v4ZUN80atnZz1yg==",
            "format": "base64"
          }
        ],
        "t": 7.704202,
        "tls_version": "TLSv1.3",
        "transaction_id": 1
      }
    ]
  },
  "test_name": "psiphon",
  "test_start_time": "2020-01-11 16:49:23",
  "test_version": "0.3.2"
}
```

# Privacy considerations

Psiphon does not seek to provide anonymity. An adversary can observe that
a user is connecting to Psiphon servers. Psiphon servers can also determine
the users location.

# Packet capture considerations

This test does not capture packets by default.

# History

The original nettest implemented in ooni/probe-legacy was [v0.1.0](
https://github.com/ooni/spec/blob/696dcbf76e89ae32f53e7f552a524bed41ee0d05/nettests/ts-015-psiphon.md). The new
experiment implemented in ooni/probe-engine is v0.3.0. We briefly used
v0.2.0 while developing v0.3.0. The semantics and caveats of this nettest
have changed significantly with v0.3.0. Please, refer to [the v0.1.0 for
more specific information about the previous implementation of this nettest](
https://github.com/ooni/spec/blob/696dcbf76e89ae32f53e7f552a524bed41ee0d05/nettests/ts-015-psiphon.md).

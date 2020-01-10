# Specification version number

0.3.1

# Specification name

Psiphon

# Test preconditions

None

# Expected impact

Ability to measure whether Psiphon is working from the given network vantage point.

# Expected inputs

None.

# Test description

This test creates a Psiphon tunnel and then uses it to fetch the
`https://www.google.com/humans.txt` webpage.

# Expected output

## Parent data format

The following keys from df-001-httpt.md are used when Psiphon bootstraps:

- requests;
- socksproxy;
- agent.

Additionally, we include `queries` from df-002-dnst.md. Because of the way in
which Psiphon works, we expect this field to always be `null`. Yet, if it's not
`null`, this means we are performing DNS resolutions without using Psiphon.

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
  "data_format_version": "0.3.1",
  "measurement_start_time": "2020-01-09 11:18:13",
  "test_runtime": 15.25602748,
  "probe_asn": "AS30722",
  "probe_cc": "IT",
  "probe_ip": "127.0.0.1",
  "report_id": "20200109T111813Z_AS30722_RZeO9Ix6ET2LJzqGcinrDp1iqrhaGGDCHSwlOoybq2N9kZITQt",
  "resolver_asn": "AS15169",
  "resolver_ip": "172.217.33.193",
  "resolver_network_name": "Google LLC",
  "software_name": "miniooni",
  "software_version": "0.1.0-dev",
  "test_keys": {
    "agent": "redirect",
    "bootstrap_time": 5.532639553,
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
              "Last-Modified",
              "Mon, 01 Jul 2019 19:30:00 GMT"
            ],
            [
              "X-Content-Type-Options",
              "nosniff"
            ],
            [
              "Server",
              "sffe"
            ],
            [
              "X-Xss-Protection",
              "0"
            ],
            [
              "Accept-Ranges",
              "bytes"
            ],
            [
              "Vary",
              "Accept-Encoding"
            ],
            [
              "Content-Length",
              "286"
            ],
            [
              "Expires",
              "Thu, 09 Jan 2020 11:18:19 GMT"
            ],
            [
              "Content-Type",
              "text/plain"
            ],
            [
              "Date",
              "Thu, 09 Jan 2020 11:18:19 GMT"
            ],
            [
              "Cache-Control",
              "private, max-age=0"
            ],
            [
              "Alt-Svc",
              "quic=\":443\"; ma=2592000; v=\"46,43\",h3-Q050=\":443\"; ma=2592000,h3-Q049=\":443\"; ma=2592000,h3-Q048=\":443\"; ma=2592000,h3-Q046=\":443\"; ma=2592000,h3-Q043=\":443\"; ma=2592000"
            ]
          ],
          "headers": {
            "Accept-Ranges": "bytes",
            "Alt-Svc": "quic=\":443\"; ma=2592000; v=\"46,43\",h3-Q050=\":443\"; ma=2592000,h3-Q049=\":443\"; ma=2592000,h3-Q048=\":443\"; ma=2592000,h3-Q046=\":443\"; ma=2592000,h3-Q043=\":443\"; ma=2592000",
            "Cache-Control": "private, max-age=0",
            "Content-Length": "286",
            "Content-Type": "text/plain",
            "Date": "Thu, 09 Jan 2020 11:18:19 GMT",
            "Expires": "Thu, 09 Jan 2020 11:18:19 GMT",
            "Last-Modified": "Mon, 01 Jul 2019 19:30:00 GMT",
            "Server": "sffe",
            "Vary": "Accept-Encoding",
            "X-Content-Type-Options": "nosniff",
            "X-Xss-Protection": "0"
          }
        }
      }
    ],
    "socksproxy": "127.0.0.1:55686"
  },
  "test_name": "psiphon",
  "test_start_time": "2020-01-09 11:18:13",
  "test_version": "0.3.1"
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

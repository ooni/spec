# Specification version number

2020-01-28-001

# Specification name

SNI blocking (`sni_blocking`)

# Test preconditions

* An internet connection

# Expected impact

Understanding whether there is blocking triggered by
the content of the TLS Hello's SNI field.

# Expected inputs

- `control_sni` (`string`): a SNI to use as control (e.g. `example.com`)

- `testhelper` (`endpoint`; optional): endpoint where TLS is enabled
expressed as `IPv4:port`, `[IPv6]:port`, or `domain:port` (e.g. `1.1.1.1:443`)

- `targets` (`[]Target`) one or more SNIs to measure

If `testhelper` is not specified we use `${control_sni}:443`.

The default implementation will use `ps.ooni.io` as `control_sni`
and the empty string as testhelper endpoint. This will effectively
cause us to use `ps.ooni.io:443` as testhelper endpoint.  This is
a reasonable choice. Our probes need to access that endpoint to
work correctly. So, if it is not blocked, we can run this experiment.
If instead `ps.ooni.io:443` is blocked, by implementing circumvention
for it, we fix both ordinary probe operations and this experiment.

A valid `Target` is a valid domain name (e.g. `kernel.org`), a valid IP
address (e.g. `1.1.1.1`), or a valid URL (e.g. `http://x.org`). When the
input is a URL, the experiment will extract the domain from the URL and
use that as target SNI, ignoring any scheme, port, path, etc.

The user should be able to specify the above parameters from the CLI.

# Test description

For every `target`, this experiment will:

1. if `target` is a URL, parse it and set `target` as the URL's hostname

2. determine `testhelper` from `control_sni` if needed

3. connect to `testhelper` using `target` as SNI

4. connect to `testhelper` using `control_sni` as SNI

The implementation may (i) randomly delay the moment where steps 3. and 4. start
such that step 3. does not strictly run before 4.; (ii) cache the result of step 4.
to avoid repeating it for every input `target`.

# Expected output

```JSON
{
    "test_keys": {
        "control": {},
	"target": {}
    }
}
```

- `control` (`Subresult`): data collected by step 4 above

- `target` (`Subresult`): data collected by step 3 above

A `Subresult` data structure looks like:

```JSON
{
    "failure": null,
    "network_events": [],
    "queries": [],
    "sni": "",
    "tcp_connect": [],
    "th_address": "",
    "tls_handshakes": []
}
```

- `failure` (`string`; nullable): `null` on success, string on
error as documented in `df-007-errors.md`;

- `network_events` (`[]NetworkEvent`; nullable): see `df-008-netevents`;

- `queries` (`[]Query`; nullable): see `df-002-dnst`;

- `requests` (`[]Transaction`; nullable): see `df-001-httpt`;

- `sni` (`string`): SNI being used;

- `tcp_connect` (`[]TCPConnect`; nullable): see `df-005-tcpconnect`;

- `th_address` (`string`): address of the test helper;

- `tls_handshakes` (`[]Handshake`; nullable): see `df-006-tlshandshake`.

We expect `requests` to be `null` unless we're using DoH; `queries` to
be `null` when `testhelper` is an IP.

## Parent data format

See the above fields description.

## Required output data

Fields described above (mind that many are nullable).

## Possible conclusions

We examine the `failure` field of `control` and `target`. Because we're
performing a TLS handshake with a TLS server that may not support the
specified SNIs, we consider `null` and `ssl_invalid_hostname` as indicators
of success. We consider any other error as potentially an anomaly.

We cannot immediately exclude the presence of a MITM box that forwards
legitimate traffic and returns invalid certificates otherwise, thus causing
`ssl_invalid_hostname` replies. However, the sequence of network events
may possibly be useful to detect these specific cases.

For this reason, it is ideal to select as test helper endpoint one that
knows how to handle one the control SNI, which is what the implementation
of this experiment should be doing by default.

## Example output sample

```JSON
{
  "data_format_version": "0.3.4",
  "input": "blocked.com",
  "measurement_start_time": "2020-01-28 15:27:18",
  "test_runtime": 0.335919812,
  "probe_asn": "AS30722",
  "probe_cc": "IT",
  "probe_ip": "127.0.0.1",
  "report_id": "20200128T152718Z_AS30722_ppk81LCnhT5Ok1P6909MX9XG8L6jmgSZkJyhx8KTmN4LAVAgGX",
  "resolver_asn": "AS30722",
  "resolver_ip": "91.80.36.88",
  "resolver_network_name": "Vodafone Italia S.p.A.",
  "software_name": "miniooni",
  "software_version": "0.1.0-dev",
  "test_keys": {
    "control": {
      "failure": null,
      "network_events": [
        {
          "address": "37.218.245.90:443",
          "conn_id": 1,
          "dial_id": 1,
          "failure": null,
          "operation": "connect",
          "proto": "tcp",
          "t": 0.249971
        },
        {
          "conn_id": 1,
          "failure": null,
          "num_bytes": 262,
          "operation": "write",
          "proto": "tcp",
          "t": 0.250393
        },
        {
          "conn_id": 1,
          "failure": null,
          "num_bytes": 517,
          "operation": "read",
          "proto": "tcp",
          "t": 0.294079
        },
        {
          "conn_id": 1,
          "failure": null,
          "num_bytes": 923,
          "operation": "read",
          "proto": "tcp",
          "t": 0.294199
        },
        {
          "conn_id": 1,
          "failure": null,
          "num_bytes": 1440,
          "operation": "read",
          "proto": "tcp",
          "t": 0.294405
        },
        {
          "conn_id": 1,
          "failure": null,
          "num_bytes": 294,
          "operation": "read",
          "proto": "tcp",
          "t": 0.295752
        },
        {
          "conn_id": 1,
          "failure": null,
          "num_bytes": 85,
          "operation": "write",
          "proto": "tcp",
          "t": 0.296475
        },
        {
          "conn_id": 1,
          "failure": null,
          "num_bytes": 43,
          "operation": "read",
          "proto": "tcp",
          "t": 0.335268
        },
        {
          "conn_id": 1,
          "failure": null,
          "num_bytes": 23,
          "operation": "write",
          "proto": "tcp",
          "t": 0.335577
        }
      ],
      "queries": [
        {
          "answers": [
            {
              "answer_type": "A",
              "ipv4": "37.218.245.90",
              "ttl": null
            }
          ],
          "dial_id": 1,
          "engine": "system",
          "failure": null,
          "hostname": "ps.ooni.io",
          "query_type": "A",
          "resolver_hostname": null,
          "resolver_port": null,
          "resolver_address": "",
          "t": 0.211333
        },
        {
          "answers": null,
          "dial_id": 1,
          "engine": "system",
          "failure": null,
          "hostname": "ps.ooni.io",
          "query_type": "AAAA",
          "resolver_hostname": null,
          "resolver_port": null,
          "resolver_address": "",
          "t": 0.211333
        }
      ],
      "requests": null,
      "sni": "ps.ooni.io",
      "tcp_connect": [
        {
          "conn_id": 1,
          "dial_id": 1,
          "ip": "37.218.245.90",
          "port": 443,
          "status": {
            "failure": null,
            "success": true
          },
          "t": 0.249971
        }
      ],
      "th_address": "ps.ooni.io:443",
      "tls_handshakes": [
        {
          "cipher_suite": "TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305",
          "conn_id": 1,
          "failure": null,
          "negotiated_protocol": "",
          "peer_certificates": [
            {
              "data": "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",
              "format": "base64"
            },
            {
              "data": "MIIEkjCCA3qgAwIBAgIQCgFBQgAAAVOFc2oLheynCDANBgkqhkiG9w0BAQsFADA/MSQwIgYDVQQKExtEaWdpdGFsIFNpZ25hdHVyZSBUcnVzdCBDby4xFzAVBgNVBAMTDkRTVCBSb290IENBIFgzMB4XDTE2MDMxNzE2NDA0NloXDTIxMDMxNzE2NDA0NlowSjELMAkGA1UEBhMCVVMxFjAUBgNVBAoTDUxldCdzIEVuY3J5cHQxIzAhBgNVBAMTGkxldCdzIEVuY3J5cHQgQXV0aG9yaXR5IFgzMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAnNMM8FrlLke3cl03g7NoYzDq1zUmGSXhvb418XCSL7e4S0EFq6meNQhY7LEqxGiHC6PjdeTm86dicbp5gWAf15Gan/PQeGdxyGkOlZHP/uaZ6WA8SMx+yk13EiSdRxta67nsHjcAHJyse6cF6s5K671B5TaYucv9bTyWaN8jKkKQDIZ0Z8h/pZq4UmEUEz9l6YKHy9v6Dlb2honzhT+Xhq+w3Brvaw2VFn3EK6BlspkENnWAa6xK8xuQSXgvopZPKiAlKQTGdMDQMc2PMTiVFrqoM7hD8bEfwzB/onkxEz0tNvjj/PIzark5McWvxI0NHWQWM6r6hCm21AvA2H3DkwIDAQABo4IBfTCCAXkwEgYDVR0TAQH/BAgwBgEB/wIBADAOBgNVHQ8BAf8EBAMCAYYwfwYIKwYBBQUHAQEEczBxMDIGCCsGAQUFBzABhiZodHRwOi8vaXNyZy50cnVzdGlkLm9jc3AuaWRlbnRydXN0LmNvbTA7BggrBgEFBQcwAoYvaHR0cDovL2FwcHMuaWRlbnRydXN0LmNvbS9yb290cy9kc3Ryb290Y2F4My5wN2MwHwYDVR0jBBgwFoAUxKexpHsscfrb4UuQdf/EFWCFiRAwVAYDVR0gBE0wSzAIBgZngQwBAgEwPwYLKwYBBAGC3xMBAQEwMDAuBggrBgEFBQcCARYiaHR0cDovL2Nwcy5yb290LXgxLmxldHNlbmNyeXB0Lm9yZzA8BgNVHR8ENTAzMDGgL6AthitodHRwOi8vY3JsLmlkZW50cnVzdC5jb20vRFNUUk9PVENBWDNDUkwuY3JsMB0GA1UdDgQWBBSoSmpjBH3duubRObemRWXv86jsoTANBgkqhkiG9w0BAQsFAAOCAQEA3TPXEfNjWDjdGBX7CVW+dla5cEilaUcne8IkCJLxWh9KEik3JHRRHGJouM2VcGfl96S8TihRzZvoroed6ti6WqEBmtzw3Wodatg+VyOeph4EYpr/1wXKtx8/wApIvJSwtmVi4MFU5aMqrSDE6ea73Mj2tcMyo5jMd6jmeWUHK8so/joWUoHOUgwuX4Po1QYz+3dszkDqMp4fklxBwXRsW10KXzPMTZ+sOPAveyxindmjkW8lGy+QsRlGPfZ+G6Z6h7mjem0Y+iWlkYcV4PIWL1iwBi8saCbGS5jN2p8M+X+Q7UNKEkROb3N6KOqkqm57TH2H3eDJAkSnh6/DNFu0Qg==",
              "format": "base64"
            }
          ],
          "t": 0.335446,
          "tls_version": "TLSv1.2"
        }
      ]
    },
    "target": {
      "failure": "ssl_invalid_hostname",
      "network_events": [
        {
          "address": "37.218.245.90:443",
          "conn_id": 2,
          "dial_id": 2,
          "failure": null,
          "operation": "connect",
          "proto": "tcp",
          "t": 0.249802
        },
        {
          "conn_id": 2,
          "failure": null,
          "num_bytes": 263,
          "operation": "write",
          "proto": "tcp",
          "t": 0.250285
        },
        {
          "conn_id": 2,
          "failure": null,
          "num_bytes": 517,
          "operation": "read",
          "proto": "tcp",
          "t": 0.298164
        },
        {
          "conn_id": 2,
          "failure": null,
          "num_bytes": 923,
          "operation": "read",
          "proto": "tcp",
          "t": 0.298283
        },
        {
          "conn_id": 2,
          "failure": null,
          "num_bytes": 1440,
          "operation": "read",
          "proto": "tcp",
          "t": 0.298325
        },
        {
          "conn_id": 2,
          "failure": null,
          "num_bytes": 7,
          "operation": "write",
          "proto": "tcp",
          "t": 0.299192
        }
      ],
      "queries": [
        {
          "answers": [
            {
              "answer_type": "A",
              "ipv4": "37.218.245.90",
              "ttl": null
            }
          ],
          "dial_id": 2,
          "engine": "system",
          "failure": null,
          "hostname": "ps.ooni.io",
          "query_type": "A",
          "resolver_hostname": null,
          "resolver_port": null,
          "resolver_address": "",
          "t": 0.211333
        },
        {
          "answers": null,
          "dial_id": 2,
          "engine": "system",
          "failure": null,
          "hostname": "ps.ooni.io",
          "query_type": "AAAA",
          "resolver_hostname": null,
          "resolver_port": null,
          "resolver_address": "",
          "t": 0.211333
        }
      ],
      "requests": null,
      "sni": "blocked.com",
      "tcp_connect": [
        {
          "conn_id": 2,
          "dial_id": 2,
          "ip": "37.218.245.90",
          "port": 443,
          "status": {
            "failure": null,
            "success": true
          },
          "t": 0.249802
        }
      ],
      "th_address": "ps.ooni.io:443",
      "tls_handshakes": [
        {
          "cipher_suite": "",
          "conn_id": 2,
          "failure": "ssl_invalid_hostname",
          "negotiated_protocol": "",
          "peer_certificates": null,
          "t": 0.299247,
          "tls_version": ""
        }
      ]
    }
  },
  "test_name": "sni_blocking",
  "test_start_time": "2020-01-28 15:27:18",
  "test_version": "0.0.1"
}
```

# Privacy considerations                                     

This nettest may be less intrusive than other nettests that measure
blocking of a specific host by connecting directly to it.
                                                                
# Packet capture considerations                      

This test does not capture packets by default.

# Acknowledgments

In Autumn 2019, [@fortuna](https://github.com/fortuna) proposed, designed,
and implemented a comprehensive domain connectivity nettest. The nettest
presented here is a slightly modified version of the SNI blocking subtest
of @fortuna's nettest.

# Future work

This nettest is still experimental. We need to define top-level keys,
run measurements with blocking using Jafar, and further develop it.

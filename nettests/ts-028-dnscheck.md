# Specification version number

2020-12-14-000

# Specification name

dnscheck

# Test preconditions

* An internet connection

# Expected impact

The ability to say which DoT/DoH/Do53 services are working.

# Expected inputs

This experiment takes in input a list of URLs. The following URL
templates are supported:

1. `dot://<domain>:<port>`.

2. `https://<domain>/<path>`.

3. `udp://<domain>:<port>`.

4. `tcp://<domain>:<port>`.

The first template indicates that dnscheck should use DNS over TLS, the
second one indicates it should use DNS over HTTPS. The third and fourth
templates allow you to use DNS over UDP and DNS over TCP respectively.

In all cases `<domain>` could also be an IP address. In all cases, you
can safely omit the `<port>` and we will use the right default.

You can also optionally specify which domain to resolve. The default
is to resolve `example.org`.

You can also optionally specify the Host header to use (if applicable)
and the SNI to use (if applicable). If not specified, we will of course
use the value provided inside the input URL.

You can also optionally specify a list of valid IP addresses for
`<domain>`, whose utility is explained below.

# Test description

The purpose of this experiment is to test all the IP addresses of a 
given resolver for domain name resolution. The scheme of the URL indicates
the resolver type and implies the default port to use. This phase is the
experiment proper and is also called the "loopkup" phase.

Before the lookup, we need to discover what IP addresses to use. If
the URL already contains an IP address, we'll use such an address. Otherwise,
we use the system resolver to discover addresses for the domain in the
input URL. In any case, we merge this address (or addresses) with the ones
that the user supplied (if any) to obtain a list of unique IPs. This
preliminary phase of the experiment is called "bootstrap".

By manually supplying valid addresses for the domain, users can ensure
that we measure whether the specified resolver works also when the system
resolver fails with NXDOMAIN or return bogons. 

# Expected output

## Parent data format

The same of `ts-027-urlgetter`.

## Semantics

This is the minimal set of keys supported by dnscheck inside
the toplevel `test_keys` key of the measurement:

```JSON
{
   "domain": "",
   "bootstrap": {},
   "bootstrap_failure": null,
   "lookups": {}
}
```

Where:

- `domain` is the domain we're resolving;

- `bootstrap` is the result of invoking ts-027-urlgetter to resolve the
domain in the DNS server URL, or `nil`, if the URL contains an IP address;

- `bootstrap_failure` conforms to `df-007-errors` and is the failure
that occurred during the bootstrap (or `nil`);

- `lookups` is a map from string to ts-027-urlgetter result, where the keys are
the endpoints being used. We will have a single endpoint here in case the DNS
server URL contains an IP address; zero or more endpoints if, instead, it
contains a domain name. Each endpoint, in this case, will correspond to one
of the IP addresses discovered during the bootstrap phase.

## Possible conclusions

Whether specific DoT/DoH/Do53 servers work.

## Example output sample

```JSON
{
  "data_format_version": "0.2.0",
  "extensions": {
    "dnst": 0,
    "httpt": 0,
    "netevents": 0,
    "tcpconnect": 0,
    "tlshandshake": 0,
    "tunnel": 0
  },
  "input": "dot://dns.google:853",
  "measurement_start_time": "2020-12-02 12:36:37",
  "probe_asn": "AS30722",
  "probe_cc": "IT",
  "probe_ip": "127.0.0.1",
  "probe_network_name": "Vodafone Italia S.p.A.",
  "report_id": "20201202T123637Z_dnscheck_IT_30722_n1_Z4McaVskEAD6GNCn",
  "resolver_asn": "AS30722",
  "resolver_ip": "91.80.36.86",
  "resolver_network_name": "Vodafone Italia S.p.A.",
  "software_name": "miniooni",
  "software_version": "0.21.0-alpha",
  "test_keys": {
    "domain": "example.org",
    "bootstrap": {
      "agent": "",
      "failed_operation": null,
      "failure": null,
      "network_events": null,
      "queries": [
        {
          "answers": [
            {
              "asn": 15169,
              "as_org_name": "Google LLC",
              "answer_type": "A",
              "ipv4": "8.8.8.8",
              "ttl": null
            },
            {
              "asn": 15169,
              "as_org_name": "Google LLC",
              "answer_type": "A",
              "ipv4": "8.8.4.4",
              "ttl": null
            }
          ],
          "engine": "system",
          "failure": null,
          "hostname": "dns.google",
          "query_type": "A",
          "resolver_hostname": null,
          "resolver_port": null,
          "resolver_address": "",
          "t": 0.027286112
        },
        {
          "answers": [
            {
              "asn": 15169,
              "as_org_name": "Google LLC",
              "answer_type": "AAAA",
              "ipv6": "2001:4860:4860::8844",
              "ttl": null
            },
            {
              "asn": 15169,
              "as_org_name": "Google LLC",
              "answer_type": "AAAA",
              "ipv6": "2001:4860:4860::8888",
              "ttl": null
            }
          ],
          "engine": "system",
          "failure": null,
          "hostname": "dns.google",
          "query_type": "AAAA",
          "resolver_hostname": null,
          "resolver_port": null,
          "resolver_address": "",
          "t": 0.027286112
        }
      ],
      "requests": null,
      "tcp_connect": null,
      "tls_handshakes": null
    },
    "bootstrap_failure": null,
    "lookups": {
      "dot://8.8.4.4:853": {
        "agent": "redirect",
        "failed_operation": null,
        "failure": null,
        "network_events": [
          {
            "failure": null,
            "operation": "resolve_start",
            "t": 0.029592334
          },
          {
            "failure": null,
            "operation": "dns_round_trip_start",
            "t": 0.029629993
          },
          {
            "address": "8.8.4.4:853",
            "failure": null,
            "operation": "connect",
            "proto": "tcp",
            "t": 0.053041936
          },
          {
            "failure": null,
            "operation": "tls_handshake_start",
            "t": 0.053070829
          },
          {
            "failure": null,
            "num_bytes": 272,
            "operation": "write",
            "t": 0.053311061
          },
          {
            "failure": null,
            "num_bytes": 517,
            "operation": "read",
            "t": 0.0928994
          },
          {
            "failure": null,
            "num_bytes": 2639,
            "operation": "read",
            "t": 0.093055939
          },
          {
            "failure": null,
            "num_bytes": 64,
            "operation": "write",
            "t": 0.093829483
          },
          {
            "failure": null,
            "operation": "tls_handshake_done",
            "t": 0.093838397
          },
          {
            "failure": null,
            "num_bytes": 152,
            "operation": "write",
            "t": 0.093857911
          },
          {
            "failure": null,
            "num_bytes": 492,
            "operation": "read",
            "t": 0.116102488
          },
          {
            "failure": null,
            "num_bytes": 24,
            "operation": "write",
            "t": 0.116147464
          },
          {
            "failure": null,
            "operation": "dns_round_trip_done",
            "t": 0.116226127
          },
          {
            "failure": null,
            "operation": "dns_round_trip_start",
            "t": 0.11628245
          },
          {
            "address": "8.8.4.4:853",
            "failure": null,
            "operation": "connect",
            "proto": "tcp",
            "t": 0.138332349
          },
          {
            "failure": null,
            "operation": "tls_handshake_start",
            "t": 0.138360707
          },
          {
            "failure": null,
            "num_bytes": 272,
            "operation": "write",
            "t": 0.138559729
          },
          {
            "failure": null,
            "num_bytes": 517,
            "operation": "read",
            "t": 0.178150464
          },
          {
            "failure": null,
            "num_bytes": 2639,
            "operation": "read",
            "t": 0.178364245
          },
          {
            "failure": null,
            "num_bytes": 64,
            "operation": "write",
            "t": 0.179138455
          },
          {
            "failure": null,
            "operation": "tls_handshake_done",
            "t": 0.17918484
          },
          {
            "failure": null,
            "num_bytes": 152,
            "operation": "write",
            "t": 0.179258354
          },
          {
            "failure": null,
            "num_bytes": 492,
            "operation": "read",
            "t": 0.202972341
          },
          {
            "failure": null,
            "num_bytes": 24,
            "operation": "write",
            "t": 0.203018956
          },
          {
            "failure": null,
            "operation": "dns_round_trip_done",
            "t": 0.203060632
          },
          {
            "failure": null,
            "operation": "resolve_done",
            "t": 0.203105974
          }
        ],
        "queries": [
          {
            "answers": [
              {
                "asn": 15133,
                "as_org_name": "MCI Communications Services, Inc. d/b/a Verizon Business",
                "answer_type": "A",
                "ipv4": "93.184.216.34",
                "ttl": null
              }
            ],
            "engine": "dot",
            "failure": null,
            "hostname": "example.org",
            "query_type": "A",
            "resolver_hostname": null,
            "resolver_port": null,
            "resolver_address": "8.8.4.4:853",
            "t": 0.203105974
          },
          {
            "answers": [
              {
                "asn": 15133,
                "as_org_name": "MCI Communications Services, Inc. d/b/a Verizon Business",
                "answer_type": "AAAA",
                "ipv6": "2606:2800:220:1:248:1893:25c8:1946",
                "ttl": null
              }
            ],
            "engine": "dot",
            "failure": null,
            "hostname": "example.org",
            "query_type": "AAAA",
            "resolver_hostname": null,
            "resolver_port": null,
            "resolver_address": "8.8.4.4:853",
            "t": 0.203105974
          }
        ],
        "requests": null,
        "tcp_connect": [
          {
            "ip": "8.8.4.4",
            "port": 853,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 0.053041936
          },
          {
            "ip": "8.8.4.4",
            "port": 853,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 0.138332349
          }
        ],
        "tls_handshakes": [
          {
            "cipher_suite": "TLS_AES_128_GCM_SHA256",
            "failure": null,
            "negotiated_protocol": "",
            "no_tls_verify": false,
            "peer_certificates": [
              {
                "data": "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",
                "format": "base64"
              },
              {
                "data": "MIIESjCCAzKgAwIBAgINAeO0mqGNiqmBJWlQuDANBgkqhkiG9w0BAQsFADBMMSAwHgYDVQQLExdHbG9iYWxTaWduIFJvb3QgQ0EgLSBSMjETMBEGA1UEChMKR2xvYmFsU2lnbjETMBEGA1UEAxMKR2xvYmFsU2lnbjAeFw0xNzA2MTUwMDAwNDJaFw0yMTEyMTUwMDAwNDJaMEIxCzAJBgNVBAYTAlVTMR4wHAYDVQQKExVHb29nbGUgVHJ1c3QgU2VydmljZXMxEzARBgNVBAMTCkdUUyBDQSAxTzEwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDQGM9F1IvN05zkQO9+tN1pIRvJzzyOTHW5DzEZhD2ePCnvUA0Qk28FgICfKqC9EksC4T2fWBYk/jCfC3R3VZMdS/dN4ZKCEPZRrAzDsiKUDzRrmBBJ5wudgzndIMYcLe/RGGFl5yODIKgjEv/SJH/UL+dEaltN11BmsK+eQmMF++AcxGNhr59qM/9il71I2dN8FGfcddwuaej4bXhp0LcQBbjxMcI7JP0aM3T4I+DsaxmKFsbjzaTNC9uzpFlgOIg7rR25xoynUxv8vNmkq7zdPGHXkxWY7oG9j+JkRyBABk7XrJfoucBZEqFJJSPk7XA0LKW0Y3z5oz2D0c1tJKwHAgMBAAGjggEzMIIBLzAOBgNVHQ8BAf8EBAMCAYYwHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMBIGA1UdEwEB/wQIMAYBAf8CAQAwHQYDVR0OBBYEFJjR+G4Q68+b7GCfGJAboOt9Cf0rMB8GA1UdIwQYMBaAFJviB1dnHB7AagbeWbSaLd/cGYYuMDUGCCsGAQUFBwEBBCkwJzAlBggrBgEFBQcwAYYZaHR0cDovL29jc3AucGtpLmdvb2cvZ3NyMjAyBgNVHR8EKzApMCegJaAjhiFodHRwOi8vY3JsLnBraS5nb29nL2dzcjIvZ3NyMi5jcmwwPwYDVR0gBDgwNjA0BgZngQwBAgIwKjAoBggrBgEFBQcCARYcaHR0cHM6Ly9wa2kuZ29vZy9yZXBvc2l0b3J5LzANBgkqhkiG9w0BAQsFAAOCAQEAGoA+Nnn78y6pRjd9XlQWNa7HTgiZ/r3RNGkmUmYHPQq6Scti9PEajvwRT2iWTHQr02fesqOqBY2ETUwgZQ+lltoNFvhsO9tvBCOIazpswWC9aJ9xju4tWDQH8NVU6YZZ/XteDSGU9YzJqPjY8q3MDxrzmqepBCf5o8mw/wJ4a2G6xzUr6Fb6T8McDO22PLRL6u3M4Tzs3A2M1j6bykJYi8wWIRdAvKLWZu/axBVbzYmqmwkm5zLSDW5nIAJbELCQCZwMH56t2Dvqofxs6BBcCFIZUSpxu6x6td0V7SvJCCosirSmIatj/9dSSVDQibet8q/7UK4v4ZUN80atnZz1yg==",
                "format": "base64"
              }
            ],
            "server_name": "dns.google",
            "t": 0.093838397,
            "tls_version": "TLSv1.3"
          },
          {
            "cipher_suite": "TLS_AES_128_GCM_SHA256",
            "failure": null,
            "negotiated_protocol": "",
            "no_tls_verify": false,
            "peer_certificates": [
              {
                "data": "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",
                "format": "base64"
              },
              {
                "data": "MIIESjCCAzKgAwIBAgINAeO0mqGNiqmBJWlQuDANBgkqhkiG9w0BAQsFADBMMSAwHgYDVQQLExdHbG9iYWxTaWduIFJvb3QgQ0EgLSBSMjETMBEGA1UEChMKR2xvYmFsU2lnbjETMBEGA1UEAxMKR2xvYmFsU2lnbjAeFw0xNzA2MTUwMDAwNDJaFw0yMTEyMTUwMDAwNDJaMEIxCzAJBgNVBAYTAlVTMR4wHAYDVQQKExVHb29nbGUgVHJ1c3QgU2VydmljZXMxEzARBgNVBAMTCkdUUyBDQSAxTzEwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDQGM9F1IvN05zkQO9+tN1pIRvJzzyOTHW5DzEZhD2ePCnvUA0Qk28FgICfKqC9EksC4T2fWBYk/jCfC3R3VZMdS/dN4ZKCEPZRrAzDsiKUDzRrmBBJ5wudgzndIMYcLe/RGGFl5yODIKgjEv/SJH/UL+dEaltN11BmsK+eQmMF++AcxGNhr59qM/9il71I2dN8FGfcddwuaej4bXhp0LcQBbjxMcI7JP0aM3T4I+DsaxmKFsbjzaTNC9uzpFlgOIg7rR25xoynUxv8vNmkq7zdPGHXkxWY7oG9j+JkRyBABk7XrJfoucBZEqFJJSPk7XA0LKW0Y3z5oz2D0c1tJKwHAgMBAAGjggEzMIIBLzAOBgNVHQ8BAf8EBAMCAYYwHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMBIGA1UdEwEB/wQIMAYBAf8CAQAwHQYDVR0OBBYEFJjR+G4Q68+b7GCfGJAboOt9Cf0rMB8GA1UdIwQYMBaAFJviB1dnHB7AagbeWbSaLd/cGYYuMDUGCCsGAQUFBwEBBCkwJzAlBggrBgEFBQcwAYYZaHR0cDovL29jc3AucGtpLmdvb2cvZ3NyMjAyBgNVHR8EKzApMCegJaAjhiFodHRwOi8vY3JsLnBraS5nb29nL2dzcjIvZ3NyMi5jcmwwPwYDVR0gBDgwNjA0BgZngQwBAgIwKjAoBggrBgEFBQcCARYcaHR0cHM6Ly9wa2kuZ29vZy9yZXBvc2l0b3J5LzANBgkqhkiG9w0BAQsFAAOCAQEAGoA+Nnn78y6pRjd9XlQWNa7HTgiZ/r3RNGkmUmYHPQq6Scti9PEajvwRT2iWTHQr02fesqOqBY2ETUwgZQ+lltoNFvhsO9tvBCOIazpswWC9aJ9xju4tWDQH8NVU6YZZ/XteDSGU9YzJqPjY8q3MDxrzmqepBCf5o8mw/wJ4a2G6xzUr6Fb6T8McDO22PLRL6u3M4Tzs3A2M1j6bykJYi8wWIRdAvKLWZu/axBVbzYmqmwkm5zLSDW5nIAJbELCQCZwMH56t2Dvqofxs6BBcCFIZUSpxu6x6td0V7SvJCCosirSmIatj/9dSSVDQibet8q/7UK4v4ZUN80atnZz1yg==",
                "format": "base64"
              }
            ],
            "server_name": "dns.google",
            "t": 0.17918484,
            "tls_version": "TLSv1.3"
          }
        ]
      },
      "dot://8.8.8.8:853": {
        "agent": "redirect",
        "failed_operation": null,
        "failure": null,
        "network_events": [
          {
            "failure": null,
            "operation": "resolve_start",
            "t": 0.029397581
          },
          {
            "failure": null,
            "operation": "dns_round_trip_start",
            "t": 0.029437275
          },
          {
            "address": "8.8.8.8:853",
            "failure": null,
            "operation": "connect",
            "proto": "tcp",
            "t": 0.049968926
          },
          {
            "failure": null,
            "operation": "tls_handshake_start",
            "t": 0.049988585
          },
          {
            "failure": null,
            "num_bytes": 272,
            "operation": "write",
            "t": 0.050371743
          },
          {
            "failure": null,
            "num_bytes": 517,
            "operation": "read",
            "t": 0.090782753
          },
          {
            "failure": null,
            "num_bytes": 2319,
            "operation": "read",
            "t": 0.091044842
          },
          {
            "failure": null,
            "num_bytes": 320,
            "operation": "read",
            "t": 0.091563775
          },
          {
            "failure": null,
            "num_bytes": 64,
            "operation": "write",
            "t": 0.092772969
          },
          {
            "failure": null,
            "operation": "tls_handshake_done",
            "t": 0.092837601
          },
          {
            "failure": null,
            "num_bytes": 152,
            "operation": "write",
            "t": 0.092863999
          },
          {
            "failure": null,
            "num_bytes": 492,
            "operation": "read",
            "t": 0.112032878
          },
          {
            "failure": null,
            "num_bytes": 24,
            "operation": "write",
            "t": 0.112119816
          },
          {
            "failure": null,
            "operation": "dns_round_trip_done",
            "t": 0.112199683
          },
          {
            "failure": null,
            "operation": "dns_round_trip_start",
            "t": 0.112242002
          },
          {
            "address": "8.8.8.8:853",
            "failure": null,
            "operation": "connect",
            "proto": "tcp",
            "t": 0.132935119
          },
          {
            "failure": null,
            "operation": "tls_handshake_start",
            "t": 0.132941497
          },
          {
            "failure": null,
            "num_bytes": 272,
            "operation": "write",
            "t": 0.133196714
          },
          {
            "failure": null,
            "num_bytes": 517,
            "operation": "read",
            "t": 0.170112781
          },
          {
            "failure": null,
            "num_bytes": 2639,
            "operation": "read",
            "t": 0.170547504
          },
          {
            "failure": null,
            "num_bytes": 64,
            "operation": "write",
            "t": 0.171562395
          },
          {
            "failure": null,
            "operation": "tls_handshake_done",
            "t": 0.171597856
          },
          {
            "failure": null,
            "num_bytes": 152,
            "operation": "write",
            "t": 0.171644666
          },
          {
            "failure": null,
            "num_bytes": 492,
            "operation": "read",
            "t": 0.19136128
          },
          {
            "failure": null,
            "num_bytes": 24,
            "operation": "write",
            "t": 0.191434912
          },
          {
            "failure": null,
            "operation": "dns_round_trip_done",
            "t": 0.191490596
          },
          {
            "failure": null,
            "operation": "resolve_done",
            "t": 0.191707595
          }
        ],
        "queries": [
          {
            "answers": [
              {
                "asn": 15133,
                "as_org_name": "MCI Communications Services, Inc. d/b/a Verizon Business",
                "answer_type": "A",
                "ipv4": "93.184.216.34",
                "ttl": null
              }
            ],
            "engine": "dot",
            "failure": null,
            "hostname": "example.org",
            "query_type": "A",
            "resolver_hostname": null,
            "resolver_port": null,
            "resolver_address": "8.8.8.8:853",
            "t": 0.191707595
          },
          {
            "answers": [
              {
                "asn": 15133,
                "as_org_name": "MCI Communications Services, Inc. d/b/a Verizon Business",
                "answer_type": "AAAA",
                "ipv6": "2606:2800:220:1:248:1893:25c8:1946",
                "ttl": null
              }
            ],
            "engine": "dot",
            "failure": null,
            "hostname": "example.org",
            "query_type": "AAAA",
            "resolver_hostname": null,
            "resolver_port": null,
            "resolver_address": "8.8.8.8:853",
            "t": 0.191707595
          }
        ],
        "requests": null,
        "tcp_connect": [
          {
            "ip": "8.8.8.8",
            "port": 853,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 0.049968926
          },
          {
            "ip": "8.8.8.8",
            "port": 853,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 0.132935119
          }
        ],
        "tls_handshakes": [
          {
            "cipher_suite": "TLS_AES_128_GCM_SHA256",
            "failure": null,
            "negotiated_protocol": "",
            "no_tls_verify": false,
            "peer_certificates": [
              {
                "data": "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",
                "format": "base64"
              },
              {
                "data": "MIIESjCCAzKgAwIBAgINAeO0mqGNiqmBJWlQuDANBgkqhkiG9w0BAQsFADBMMSAwHgYDVQQLExdHbG9iYWxTaWduIFJvb3QgQ0EgLSBSMjETMBEGA1UEChMKR2xvYmFsU2lnbjETMBEGA1UEAxMKR2xvYmFsU2lnbjAeFw0xNzA2MTUwMDAwNDJaFw0yMTEyMTUwMDAwNDJaMEIxCzAJBgNVBAYTAlVTMR4wHAYDVQQKExVHb29nbGUgVHJ1c3QgU2VydmljZXMxEzARBgNVBAMTCkdUUyBDQSAxTzEwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDQGM9F1IvN05zkQO9+tN1pIRvJzzyOTHW5DzEZhD2ePCnvUA0Qk28FgICfKqC9EksC4T2fWBYk/jCfC3R3VZMdS/dN4ZKCEPZRrAzDsiKUDzRrmBBJ5wudgzndIMYcLe/RGGFl5yODIKgjEv/SJH/UL+dEaltN11BmsK+eQmMF++AcxGNhr59qM/9il71I2dN8FGfcddwuaej4bXhp0LcQBbjxMcI7JP0aM3T4I+DsaxmKFsbjzaTNC9uzpFlgOIg7rR25xoynUxv8vNmkq7zdPGHXkxWY7oG9j+JkRyBABk7XrJfoucBZEqFJJSPk7XA0LKW0Y3z5oz2D0c1tJKwHAgMBAAGjggEzMIIBLzAOBgNVHQ8BAf8EBAMCAYYwHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMBIGA1UdEwEB/wQIMAYBAf8CAQAwHQYDVR0OBBYEFJjR+G4Q68+b7GCfGJAboOt9Cf0rMB8GA1UdIwQYMBaAFJviB1dnHB7AagbeWbSaLd/cGYYuMDUGCCsGAQUFBwEBBCkwJzAlBggrBgEFBQcwAYYZaHR0cDovL29jc3AucGtpLmdvb2cvZ3NyMjAyBgNVHR8EKzApMCegJaAjhiFodHRwOi8vY3JsLnBraS5nb29nL2dzcjIvZ3NyMi5jcmwwPwYDVR0gBDgwNjA0BgZngQwBAgIwKjAoBggrBgEFBQcCARYcaHR0cHM6Ly9wa2kuZ29vZy9yZXBvc2l0b3J5LzANBgkqhkiG9w0BAQsFAAOCAQEAGoA+Nnn78y6pRjd9XlQWNa7HTgiZ/r3RNGkmUmYHPQq6Scti9PEajvwRT2iWTHQr02fesqOqBY2ETUwgZQ+lltoNFvhsO9tvBCOIazpswWC9aJ9xju4tWDQH8NVU6YZZ/XteDSGU9YzJqPjY8q3MDxrzmqepBCf5o8mw/wJ4a2G6xzUr6Fb6T8McDO22PLRL6u3M4Tzs3A2M1j6bykJYi8wWIRdAvKLWZu/axBVbzYmqmwkm5zLSDW5nIAJbELCQCZwMH56t2Dvqofxs6BBcCFIZUSpxu6x6td0V7SvJCCosirSmIatj/9dSSVDQibet8q/7UK4v4ZUN80atnZz1yg==",
                "format": "base64"
              }
            ],
            "server_name": "dns.google",
            "t": 0.092837601,
            "tls_version": "TLSv1.3"
          },
          {
            "cipher_suite": "TLS_AES_128_GCM_SHA256",
            "failure": null,
            "negotiated_protocol": "",
            "no_tls_verify": false,
            "peer_certificates": [
              {
                "data": "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",
                "format": "base64"
              },
              {
                "data": "MIIESjCCAzKgAwIBAgINAeO0mqGNiqmBJWlQuDANBgkqhkiG9w0BAQsFADBMMSAwHgYDVQQLExdHbG9iYWxTaWduIFJvb3QgQ0EgLSBSMjETMBEGA1UEChMKR2xvYmFsU2lnbjETMBEGA1UEAxMKR2xvYmFsU2lnbjAeFw0xNzA2MTUwMDAwNDJaFw0yMTEyMTUwMDAwNDJaMEIxCzAJBgNVBAYTAlVTMR4wHAYDVQQKExVHb29nbGUgVHJ1c3QgU2VydmljZXMxEzARBgNVBAMTCkdUUyBDQSAxTzEwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDQGM9F1IvN05zkQO9+tN1pIRvJzzyOTHW5DzEZhD2ePCnvUA0Qk28FgICfKqC9EksC4T2fWBYk/jCfC3R3VZMdS/dN4ZKCEPZRrAzDsiKUDzRrmBBJ5wudgzndIMYcLe/RGGFl5yODIKgjEv/SJH/UL+dEaltN11BmsK+eQmMF++AcxGNhr59qM/9il71I2dN8FGfcddwuaej4bXhp0LcQBbjxMcI7JP0aM3T4I+DsaxmKFsbjzaTNC9uzpFlgOIg7rR25xoynUxv8vNmkq7zdPGHXkxWY7oG9j+JkRyBABk7XrJfoucBZEqFJJSPk7XA0LKW0Y3z5oz2D0c1tJKwHAgMBAAGjggEzMIIBLzAOBgNVHQ8BAf8EBAMCAYYwHQYDVR0lBBYwFAYIKwYBBQUHAwEGCCsGAQUFBwMCMBIGA1UdEwEB/wQIMAYBAf8CAQAwHQYDVR0OBBYEFJjR+G4Q68+b7GCfGJAboOt9Cf0rMB8GA1UdIwQYMBaAFJviB1dnHB7AagbeWbSaLd/cGYYuMDUGCCsGAQUFBwEBBCkwJzAlBggrBgEFBQcwAYYZaHR0cDovL29jc3AucGtpLmdvb2cvZ3NyMjAyBgNVHR8EKzApMCegJaAjhiFodHRwOi8vY3JsLnBraS5nb29nL2dzcjIvZ3NyMi5jcmwwPwYDVR0gBDgwNjA0BgZngQwBAgIwKjAoBggrBgEFBQcCARYcaHR0cHM6Ly9wa2kuZ29vZy9yZXBvc2l0b3J5LzANBgkqhkiG9w0BAQsFAAOCAQEAGoA+Nnn78y6pRjd9XlQWNa7HTgiZ/r3RNGkmUmYHPQq6Scti9PEajvwRT2iWTHQr02fesqOqBY2ETUwgZQ+lltoNFvhsO9tvBCOIazpswWC9aJ9xju4tWDQH8NVU6YZZ/XteDSGU9YzJqPjY8q3MDxrzmqepBCf5o8mw/wJ4a2G6xzUr6Fb6T8McDO22PLRL6u3M4Tzs3A2M1j6bykJYi8wWIRdAvKLWZu/axBVbzYmqmwkm5zLSDW5nIAJbELCQCZwMH56t2Dvqofxs6BBcCFIZUSpxu6x6td0V7SvJCCosirSmIatj/9dSSVDQibet8q/7UK4v4ZUN80atnZz1yg==",
                "format": "base64"
              }
            ],
            "server_name": "dns.google",
            "t": 0.171597856,
            "tls_version": "TLSv1.3"
          }
        ]
      },
      "dot://[2001:4860:4860::8844]:853": {
        "agent": "redirect",
        "failed_operation": "connect",
        "failure": "unknown_failure: dial tcp [scrubbed]: connect: no route to host",
        "network_events": [
          {
            "failure": null,
            "operation": "resolve_start",
            "t": 0.029377042
          },
          {
            "failure": null,
            "operation": "dns_round_trip_start",
            "t": 0.029659253
          },
          {
            "address": "[2001:4860:4860::8844]:853",
            "failure": "unknown_failure: dial tcp [scrubbed]: connect: no route to host",
            "operation": "connect",
            "proto": "tcp",
            "t": 0.030893662
          },
          {
            "failure": "unknown_failure: dial tcp [scrubbed]: connect: no route to host",
            "operation": "dns_round_trip_done",
            "t": 0.030906606
          },
          {
            "failure": null,
            "operation": "dns_round_trip_start",
            "t": 0.030953565
          },
          {
            "address": "[2001:4860:4860::8844]:853",
            "failure": "unknown_failure: dial tcp [scrubbed]: connect: no route to host",
            "operation": "connect",
            "proto": "tcp",
            "t": 0.031477944
          },
          {
            "failure": "unknown_failure: dial tcp [scrubbed]: connect: no route to host",
            "operation": "dns_round_trip_done",
            "t": 0.031481117
          },
          {
            "failure": "unknown_failure: dial tcp [scrubbed]: connect: no route to host",
            "operation": "resolve_done",
            "t": 0.031490323
          }
        ],
        "queries": [
          {
            "answers": null,
            "engine": "dot",
            "failure": "unknown_failure: dial tcp [scrubbed]: connect: no route to host",
            "hostname": "example.org",
            "query_type": "A",
            "resolver_hostname": null,
            "resolver_port": null,
            "resolver_address": "[2001:4860:4860::8844]:853",
            "t": 0.031490323
          },
          {
            "answers": null,
            "engine": "dot",
            "failure": "unknown_failure: dial tcp [scrubbed]: connect: no route to host",
            "hostname": "example.org",
            "query_type": "AAAA",
            "resolver_hostname": null,
            "resolver_port": null,
            "resolver_address": "[2001:4860:4860::8844]:853",
            "t": 0.031490323
          }
        ],
        "requests": null,
        "tcp_connect": [
          {
            "ip": "2001:4860:4860::8844",
            "port": 853,
            "status": {
              "failure": "unknown_failure: dial tcp [scrubbed]: connect: no route to host",
              "success": false
            },
            "t": 0.030893662
          },
          {
            "ip": "2001:4860:4860::8844",
            "port": 853,
            "status": {
              "failure": "unknown_failure: dial tcp [scrubbed]: connect: no route to host",
              "success": false
            },
            "t": 0.031477944
          }
        ],
        "tls_handshakes": null
      },
      "dot://[2001:4860:4860::8888]:853": {
        "agent": "redirect",
        "failed_operation": "connect",
        "failure": "unknown_failure: dial tcp [scrubbed]: connect: no route to host",
        "network_events": [
          {
            "failure": null,
            "operation": "resolve_start",
            "t": 0.03156884
          },
          {
            "failure": null,
            "operation": "dns_round_trip_start",
            "t": 0.031582933
          },
          {
            "address": "[2001:4860:4860::8888]:853",
            "failure": "unknown_failure: dial tcp [scrubbed]: connect: no route to host",
            "operation": "connect",
            "proto": "tcp",
            "t": 0.032082161
          },
          {
            "failure": "unknown_failure: dial tcp [scrubbed]: connect: no route to host",
            "operation": "dns_round_trip_done",
            "t": 0.032086578
          },
          {
            "failure": null,
            "operation": "dns_round_trip_start",
            "t": 0.032096787
          },
          {
            "address": "[2001:4860:4860::8888]:853",
            "failure": "unknown_failure: dial tcp [scrubbed]: connect: no route to host",
            "operation": "connect",
            "proto": "tcp",
            "t": 0.032401266
          },
          {
            "failure": "unknown_failure: dial tcp [scrubbed]: connect: no route to host",
            "operation": "dns_round_trip_done",
            "t": 0.032404518
          },
          {
            "failure": "unknown_failure: dial tcp [scrubbed]: connect: no route to host",
            "operation": "resolve_done",
            "t": 0.0324134
          }
        ],
        "queries": [
          {
            "answers": null,
            "engine": "dot",
            "failure": "unknown_failure: dial tcp [scrubbed]: connect: no route to host",
            "hostname": "example.org",
            "query_type": "A",
            "resolver_hostname": null,
            "resolver_port": null,
            "resolver_address": "[2001:4860:4860::8888]:853",
            "t": 0.0324134
          },
          {
            "answers": null,
            "engine": "dot",
            "failure": "unknown_failure: dial tcp [scrubbed]: connect: no route to host",
            "hostname": "example.org",
            "query_type": "AAAA",
            "resolver_hostname": null,
            "resolver_port": null,
            "resolver_address": "[2001:4860:4860::8888]:853",
            "t": 0.0324134
          }
        ],
        "requests": null,
        "tcp_connect": [
          {
            "ip": "2001:4860:4860::8888",
            "port": 853,
            "status": {
              "failure": "unknown_failure: dial tcp [scrubbed]: connect: no route to host",
              "success": false
            },
            "t": 0.032082161
          },
          {
            "ip": "2001:4860:4860::8888",
            "port": 853,
            "status": {
              "failure": "unknown_failure: dial tcp [scrubbed]: connect: no route to host",
              "success": false
            },
            "t": 0.032401266
          }
        ],
        "tls_handshakes": null
      }
    }
  },
  "test_name": "dnscheck",
  "test_runtime": 0.203695918,
  "test_start_time": "2020-12-02 12:36:37",
  "test_version": "0.1.0"
}
```

# Specification version number

2022-08-24

*_status_: current

# Specification name

TLS middlebox

# Test preconditions

* An internet connection

# Expected impact

Ability to detect the presence of TLS middleboxes censoring requests based on the servername.

# Expected inputs

- `control_sni` (`string`): a SNI to use as control (e.g. `example.org`)

- `testhelper` (`endpoint`): a URL like `tlshandshake://<host>:<port>` or 
`https://<host>:<port>`

- `sni` (`string`; optional): a potentially blocked SNI to measure (e.g. `1337x.be`)

The default implementation will use a domain such as `example.org` as
the `control_sni` and the testhelper's hostname as the target.  

# Test description

This test is divided into multiple steps that will each ensure that we can successfully 
perform iterative tracing on the `target` and return early in case of failure.

The main steps of the experiment are:

1. **DNS lookup**
    Perform a A/AAAA query to the configured DoH resolver for the testhelper's hostname. Fall 
    back to the system resolver in case DoH fails and record the lst of DNS responses/records 
    under the "queried" key (see df-002-dnst.md).

2. **TCP Connect**
    Attempt to establish a TCP session on port 443 (default, overriden by the port in the 
    testhelper) for the list of IPs identified at step 1. The results of the connecting end up
    in the "tcp_connect" key. (see df-005-tcpconnect.md).

3. **TLS Handshake**
    Attempt to perform a tls handshake for the list of filtered IPs (for which the TCP session 
    can successfully established) obtained at step 2. The handshake is performed iteratively 
    for each IP with an increment in the TTL for each successive iteration. 

    The entire tracing is done twice: using the `control_sni` and the `target`. Each iteration
    records the handshake results along with the corresponding TTL. The results of the trace end
    up in the `trace` key which is divided into two: `control_trace` (the trace for the `control_sni`)
    and `target_trace` (the trace for the `target_sni`). Each `trace` field records the iterations
    for a single servername till we receive a `null` failure (a successful handshake) or a 
    `connection_reset`. The handshake results are recorded in the `handshake` field. (see 
    df-006-tlshandshake.md)

# Expected output

## Parent data format

We will include data following these data formats:

* `df-002-dnst`
* `df-005-tcpconnect`
* `df-006-tlshandshake`

## Semantics

```JSON
{
   "queries": [],
   "tcp_connect": [],
   "iterative_trace": {
      "address": "",
      "control_trace": {},
      "target_trace": {}
   }
}
```

where:

- `queries` contains a list of `df-002-dnst` instances

- `tcp_connect` contains a list of `df-005-tcpconnect` instances

- `iterative_trace` contains the SNI-based iterative trace of the form:

```JSON
{
   "ttl": ,
   "handshake": {}
}
```

where:

- `ttl` is a positive integer

- `handshake` follows the `df-006-tlshandshake` data format

## Possible conclusions

* If there is a middlebox attempting to censor content in the network route 

* If the blocking of a particular servername is due to the presence of a middlebox
in the network route.

## Example output sample

Response:

```JSON
{
  "annotations": {
    "architecture": "amd64",
    "engine_name": "ooniprobe-engine",
    "engine_version": "3.16.0-alpha.2",
    "platform": "linux"
  },
  "data_format_version": "0.2.0",
  "input": "tlstrace://1337x.be",
  "measurement_start_time": "2022-09-01 16:37:55",
  "options": [
    "TestHelper=tlshandshake://example.com"
  ],
  "probe_asn": "AS24560",
  "probe_cc": "IN",
  "probe_ip": "127.0.0.1",
  "probe_network_name": "Bharti Airtel Limited",
  "report_id": "20220901T163755Z_tlsmiddlebox_IN_24560_n1_zUFu0wK85oGNlnbG",
  "resolver_asn": "AS13335",
  "resolver_ip": "162.158.45.17",
  "resolver_network_name": "Cloudflare, Inc.",
  "software_name": "miniooni",
  "software_version": "3.16.0-alpha.2",
  "test_keys": {
    "queries": [
      {
        "answers": [
          {
            "asn": 13335,
            "as_org_name": "Cloudflare, Inc.",
            "answer_type": "A",
            "ipv4": "104.16.249.249",
            "ttl": null
          },
          {
            "asn": 13335,
            "as_org_name": "Cloudflare, Inc.",
            "answer_type": "A",
            "ipv4": "104.16.248.249",
            "ttl": null
          },
          {
            "asn": 13335,
            "as_org_name": "Cloudflare, Inc.",
            "answer_type": "AAAA",
            "ipv6": "2606:4700:83b3:8ced:8739:0:1827:bcee",
            "ttl": null
          },
          {
            "answer_type": "CNAME",
            "hostname": "mozilla.cloudflare-dns.com",
            "ttl": null
          }
        ],
        "engine": "getaddrinfo",
        "failure": null,
        "hostname": "mozilla.cloudflare-dns.com",
        "query_type": "ANY",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "",
        "t0": 0.000127901,
        "t": 0.000422598,
        "transaction_id": 0
      },
      {
        "answers": [
          {
            "asn": 15133,
            "as_org_name": "Edgecast Inc.",
            "answer_type": "A",
            "ipv4": "93.184.216.34",
            "ttl": null
          }
        ],
        "engine": "doh",
        "failure": null,
        "hostname": "example.com",
        "query_type": "A",
        "raw_response": "72KBoAABAAIAAAABB2V4YW1wbGUDY29tAAABAAHADAABAAEAAUMIAARduNgiwAwALgABAAFDCACfAAEIAgABUYBjHAvgYwDk6AaWB2V4YW1wbGUDY29tABKm/2/eVl7Xqf/0X1iKOlFbF8vNFewGZUvOEd/19pMMC4hzqmMz3wDbU4e/SoTUb6rRzKxciolbYu5tDCGuysl7bMBpduGW0vzXShus0J4sjRT1XZyWa9ahtDy9juNeen+3Szo+zJuGiS+TfbXhxk9NS1QrPK1n3+w1SDsINq0PAAApBNAAAIAAAPEADADtAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "https://mozilla.cloudflare-dns.com/dns-query",
        "t0": 0.000098138,
        "t": 0.121407471,
        "transaction_id": 0
      },
      {
        "answers": [
          {
            "asn": 15133,
            "as_org_name": "Edgecast Inc.",
            "answer_type": "AAAA",
            "ipv6": "2606:2800:220:1:248:1893:25c8:1946",
            "ttl": null
          }
        ],
        "engine": "doh",
        "failure": null,
        "hostname": "example.com",
        "query_type": "AAAA",
        "raw_response": "f4WBoAABAAIAAAABB2V4YW1wbGUDY29tAAAcAAHADAAcAAEAAVGAABAmBigAAiAAAQJIGJMlyBlGwAwALgABAAFRgACfABwIAgABUYBjHTHnYwEdKgaWB2V4YW1wbGUDY29tAGewwJzy9va8IhAIedDOGo0Ckq4k4m66WJgiJavq+aGEWEMzZOXYMv6B5em4fU0nLM/VHwXng9fVPJnORL0PAfRuM3y9ljlrmTPu+ymCCo2pzNI0XqGE9DglaoGyzPdctkT9EPFsD+pVSWoQEoANZCLPWPMblcBiDn24kY9OKbc6AAApBNAAAIAAAOUADADhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "https://mozilla.cloudflare-dns.com/dns-query",
        "t0": 0.000052631,
        "t": 0.34243427,
        "transaction_id": 0
      }
    ],
    "tcp_connect": [
      {
        "ip": "2606:2800:220:1:248:1893:25c8:1946",
        "port": 443,
        "status": {
          "failure": "network_unreachable",
          "success": false
        },
        "t0": 0.342688667,
        "t": 0.342975162,
        "transaction_id": 1
      },
      {
        "ip": "93.184.216.34",
        "port": 443,
        "status": {
          "failure": null,
          "success": true
        },
        "t0": 0.34271378,
        "t": 0.560168233,
        "transaction_id": 0
      }
    ],
    "iterative_trace": [
      {
        "address": "[2606:2800:220:1:248:1893:25c8:1946]:443",
        "control_trace": null,
        "target_trace": null
      },
      {
        "address": "93.184.216.34:443",
        "control_trace": {
          "server_name": "example.com",
          "iterations": [
            {
              "ttl": 1,
              "handshake": {
                "network": "tls",
                "address": "93.184.216.34:443",
                "cipher_suite": "",
                "failure": "generic_timeout_error",
                "so_error": "host_unreachable",
                "negotiated_protocol": "",
                "no_tls_verify": true,
                "peer_certificates": [],
                "server_name": "example.com",
                "t0": 0.806588718,
                "t": 10.807752529,
                "tags": [],
                "tls_version": "",
                "transaction_id": 0
              }
            },
            {
              "ttl": 2,
              "handshake": {
                "network": "tls",
                "address": "93.184.216.34:443",
                "cipher_suite": "",
                "failure": "generic_timeout_error",
                "so_error": "host_unreachable",
                "negotiated_protocol": "",
                "no_tls_verify": true,
                "peer_certificates": [],
                "server_name": "example.com",
                "t0": 0.914062501,
                "t": 10.915233266,
                "tags": [],
                "tls_version": "",
                "transaction_id": 0
              }
            },
            {
              "ttl": 3,
              "handshake": {
                "network": "tls",
                "address": "93.184.216.34:443",
                "cipher_suite": "",
                "failure": "generic_timeout_error",
                "so_error": "host_unreachable",
                "negotiated_protocol": "",
                "no_tls_verify": true,
                "peer_certificates": [],
                "server_name": "example.com",
                "t0": 1.01293851,
                "t": 11.013575444,
                "tags": [],
                "tls_version": "",
                "transaction_id": 0
              }
            },
            {
              "ttl": 4,
              "handshake": {
                "network": "tls",
                "address": "93.184.216.34:443",
                "cipher_suite": "",
                "failure": "generic_timeout_error",
                "so_error": "host_unreachable",
                "negotiated_protocol": "",
                "no_tls_verify": true,
                "peer_certificates": [],
                "server_name": "example.com",
                "t0": 1.080355309,
                "t": 11.080976051,
                "tags": [],
                "tls_version": "",
                "transaction_id": 0
              }
            },
            {
              "ttl": 5,
              "handshake": {
                "network": "tls",
                "address": "93.184.216.34:443",
                "cipher_suite": "",
                "failure": "generic_timeout_error",
                "so_error": "host_unreachable",
                "negotiated_protocol": "",
                "no_tls_verify": true,
                "peer_certificates": [],
                "server_name": "example.com",
                "t0": 1.185732563,
                "t": 11.186405305,
                "tags": [],
                "tls_version": "",
                "transaction_id": 0
              }
            },
            {
              "ttl": 6,
              "handshake": {
                "network": "tls",
                "address": "93.184.216.34:443",
                "cipher_suite": "",
                "failure": "generic_timeout_error",
                "so_error": "host_unreachable",
                "negotiated_protocol": "",
                "no_tls_verify": true,
                "peer_certificates": [],
                "server_name": "example.com",
                "t0": 1.30764149,
                "t": 11.308075848,
                "tags": [],
                "tls_version": "",
                "transaction_id": 0
              }
            },
            {
              "ttl": 7,
              "handshake": {
                "network": "tls",
                "address": "93.184.216.34:443",
                "cipher_suite": "",
                "failure": "generic_timeout_error",
                "so_error": "host_unreachable",
                "negotiated_protocol": "",
                "no_tls_verify": true,
                "peer_certificates": [],
                "server_name": "example.com",
                "t0": 1.408247724,
                "t": 11.408401526,
                "tags": [],
                "tls_version": "",
                "transaction_id": 0
              }
            },
            {
              "ttl": 8,
              "handshake": {
                "network": "tls",
                "address": "93.184.216.34:443",
                "cipher_suite": "",
                "failure": "generic_timeout_error",
                "so_error": "host_unreachable",
                "negotiated_protocol": "",
                "no_tls_verify": true,
                "peer_certificates": [],
                "server_name": "example.com",
                "t0": 1.483209508,
                "t": 11.483764881,
                "tags": [],
                "tls_version": "",
                "transaction_id": 0
              }
            },
            {
              "ttl": 9,
              "handshake": {
                "network": "tls",
                "address": "93.184.216.34:443",
                "cipher_suite": "",
                "failure": "generic_timeout_error",
                "so_error": "host_unreachable",
                "negotiated_protocol": "",
                "no_tls_verify": true,
                "peer_certificates": [],
                "server_name": "example.com",
                "t0": 1.592801069,
                "t": 11.593133327,
                "tags": [],
                "tls_version": "",
                "transaction_id": 0
              }
            },
            {
              "ttl": 10,
              "handshake": {
                "network": "tls",
                "address": "93.184.216.34:443",
                "cipher_suite": "",
                "failure": "generic_timeout_error",
                "so_error": "host_unreachable",
                "negotiated_protocol": "",
                "no_tls_verify": true,
                "peer_certificates": [],
                "server_name": "example.com",
                "t0": 1.681079291,
                "t": 11.681597026,
                "tags": [],
                "tls_version": "",
                "transaction_id": 0
              }
            },
            {
              "ttl": 11,
              "handshake": {
                "network": "tls",
                "address": "93.184.216.34:443",
                "cipher_suite": "",
                "failure": "generic_timeout_error",
                "so_error": "host_unreachable",
                "negotiated_protocol": "",
                "no_tls_verify": true,
                "peer_certificates": [],
                "server_name": "example.com",
                "t0": 1.80795438,
                "t": 11.808075717,
                "tags": [],
                "tls_version": "",
                "transaction_id": 0
              }
            },
            {
              "ttl": 12,
              "handshake": {
                "network": "tls",
                "address": "93.184.216.34:443",
                "cipher_suite": "TLS_AES_256_GCM_SHA384",
                "failure": null,
                "negotiated_protocol": "h2",
                "no_tls_verify": true,
                "peer_certificates": [
                  {
                    "data": "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",
                    "format": "base64"
                  },
                  {
                    "data": "MIIEvjCCA6agAwIBAgIQBtjZBNVYQ0b2ii+nVCJ+xDANBgkqhkiG9w0BAQsFADBhMQswCQYDVQQGEwJVUzEVMBMGA1UEChMMRGlnaUNlcnQgSW5jMRkwFwYDVQQLExB3d3cuZGlnaWNlcnQuY29tMSAwHgYDVQQDExdEaWdpQ2VydCBHbG9iYWwgUm9vdCBDQTAeFw0yMTA0MTQwMDAwMDBaFw0zMTA0MTMyMzU5NTlaME8xCzAJBgNVBAYTAlVTMRUwEwYDVQQKEwxEaWdpQ2VydCBJbmMxKTAnBgNVBAMTIERpZ2lDZXJ0IFRMUyBSU0EgU0hBMjU2IDIwMjAgQ0ExMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwUuzZUdwvN1PWNvsnO3DZuUfMRNUrUpmRh8sCuxkB+Uu3Ny5CiDt3+PE0J6aqXodgojlEVbbHp9YwlHnLDQNLtKS4VbL8Xlfs7uHyiUDe5pSQWYQYE9XE0nw6Ddng9/n00tnTCJRpt8OmRDtV1F0JuJ9x8piLhMbfyOIJVNvwTRYAIuE//i+p1hJInuWraKImxW8oHzf6VGo1bDtN+I2tIJLYrVJmuzHZ9bjPvXj1hJeRPG/cUJ9WIQDgLGBAfr5yjK7tI4nhyfFK3TUqNaX3sNk+crOU6JWvHgXjkkDKa77SU+kFbnO8lwZV21reacroicgE7XQPUDTITAHk+qZ9QIDAQABo4IBgjCCAX4wEgYDVR0TAQH/BAgwBgEB/wIBADAdBgNVHQ4EFgQUt2ui6qiqhIx56rTaD5iyxZV2ufQwHwYDVR0jBBgwFoAUA95QNVbRTLtm8KPiGxvDl7I90VUwDgYDVR0PAQH/BAQDAgGGMB0GA1UdJQQWMBQGCCsGAQUFBwMBBggrBgEFBQcDAjB2BggrBgEFBQcBAQRqMGgwJAYIKwYBBQUHMAGGGGh0dHA6Ly9vY3NwLmRpZ2ljZXJ0LmNvbTBABggrBgEFBQcwAoY0aHR0cDovL2NhY2VydHMuZGlnaWNlcnQuY29tL0RpZ2lDZXJ0R2xvYmFsUm9vdENBLmNydDBCBgNVHR8EOzA5MDegNaAzhjFodHRwOi8vY3JsMy5kaWdpY2VydC5jb20vRGlnaUNlcnRHbG9iYWxSb290Q0EuY3JsMD0GA1UdIAQ2MDQwCwYJYIZIAYb9bAIBMAcGBWeBDAEBMAgGBmeBDAECATAIBgZngQwBAgIwCAYGZ4EMAQIDMA0GCSqGSIb3DQEBCwUAA4IBAQCAMs5eC91uWg0Kr+HWhMvAjvqFcO3aXbMM9yt1QP6FCvrzMXi3cEsaiVi6gL3zax3pfs8LulicWdSQ0/1s/dCYbbdxglvPbQtaCdB73sRD2Cqk3p5BJl+7j5nL3a7hqG+fh/50tx8bIKuxT8b1Z11dmzzp/2n3YWzW2fP9NsarA4h20ksudYbj/NhVfSbCEXffPgK2fPOre3qGNm+499iTcc+G33Mw+nur7SpZyEKEOxEXGlLzyQ4UfaJbcme6ce1XR2bFuAJKZTRei9AqPCCcUZlM51Ke92sRKw2Sfh3oius2FkOH6ipjv3U/697EA7sKPPcw7+uvTPyLNhBzPvOk",
                    "format": "base64"
                  }
                ],
                "server_name": "example.com",
                "t0": 1.904429709,
                "t": 2.37451115,
                "tags": [],
                "tls_version": "TLSv1.3",
                "transaction_id": 0
              }
            }
          ]
        },
        "target_trace": {
          "server_name": "1337x.be",
          "iterations": [
            {
              "ttl": 1,
              "handshake": {
                "network": "tls",
                "address": "93.184.216.34:443",
                "cipher_suite": "",
                "failure": "generic_timeout_error",
                "so_error": "host_unreachable",
                "negotiated_protocol": "",
                "no_tls_verify": true,
                "peer_certificates": [],
                "server_name": "1337x.be",
                "t0": 12.057799537,
                "t": 22.058602821,
                "tags": [],
                "tls_version": "",
                "transaction_id": 0
              }
            },
            {
              "ttl": 2,
              "handshake": {
                "network": "tls",
                "address": "93.184.216.34:443",
                "cipher_suite": "",
                "failure": "generic_timeout_error",
                "so_error": "host_unreachable",
                "negotiated_protocol": "",
                "no_tls_verify": true,
                "peer_certificates": [],
                "server_name": "1337x.be",
                "t0": 12.158662773,
                "t": 22.159214986,
                "tags": [],
                "tls_version": "",
                "transaction_id": 0
              }
            },
            {
              "ttl": 3,
              "handshake": {
                "network": "tls",
                "address": "93.184.216.34:443",
                "cipher_suite": "",
                "failure": "generic_timeout_error",
                "so_error": "host_unreachable",
                "negotiated_protocol": "",
                "no_tls_verify": true,
                "peer_certificates": [],
                "server_name": "1337x.be",
                "t0": 12.262444805,
                "t": 22.263151325,
                "tags": [],
                "tls_version": "",
                "transaction_id": 0
              }
            },
            {
              "ttl": 4,
              "handshake": {
                "network": "tls",
                "address": "93.184.216.34:443",
                "cipher_suite": "",
                "failure": "connection_reset",
                "negotiated_protocol": "",
                "no_tls_verify": true,
                "peer_certificates": [],
                "server_name": "1337x.be",
                "t0": 12.361798829,
                "t": 12.451137716,
                "tags": [],
                "tls_version": "",
                "transaction_id": 0
              }
            }
          ]
        }
      }
    ]
  },
  "test_name": "tlsmiddlebox",
  "test_runtime": 22.457373373,
  "test_start_time": "2022-09-01 16:37:32",
  "test_version": "0.1.0"
}
```
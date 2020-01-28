# Specification version number

2020-01-27-002

# Specification name

Tor (`tor`)

# Test preconditions

* An internet connection

# Expected impact

Assess the reachability of selected Tor directory authorities
and bridges. Assess whether they are usable by performing target
specific actions (e.g. perform the obfs4 handshake).

# Expected inputs

The nettest will fetch the Tor targets to measure from OONI
servers and MAY cache such information for later reuse.

In JSON format the input targets have this structure:

```JSON
{
  "id": {
    "address": "",
    "fingerprint": "",
    "name": "",
    "params": {},
    "protocol": ""
  }
}
```

- `id` (`string`): the unique identifier of the target chosen
by who generated the input targets.

- `address` (`string`): the address of the target.

- `fingerprint` (`string`; optional): the fingerprint, if applicable.

- `name` (`string`; optional): the target name, if applicable.

- `params` (`map[string][]string`; optional): extra parameters,
e.g., to configure `obfs4`.

- `protocol` (`string`): the protocol to use with the
target (e.g. `obfs4`).

This specification defines the following protocols:

- `dir_port`: directory authority port (used by tor relays).

- `or_port`: OR port used by a bridge.

- `or_port_dirauth` (since 2020-01-27): OR port of a directory
authority (used by tor clients).

- `obfs4`: bridge speaking the OBFS4 protocol.

The following is a valid example:

```JSON
{
  "f372c264e9a470335d9ac79fe780847bda052aa3b6a9ee5ff497cb6501634f9f": {
    "address": "38.229.1.78:80",
    "fingerprint": "C8CBDB2464FC9804A69531437BCF2BE31FDD2EE4",
    "params": {
      "cert": [
        "Hmyfd2ev46gGY7NoVxA9ngrPF2zCZtzskRTzoWXbxNkzeVnGFPWmrTtILRyqCTjHR+s9dg"
      ],
      "iat-mode": ["1"],
    },
    "protocol": "obfs4"
  },
  "66.111.2.131:9030": {
    "address":  "66.111.2.131:9030",
    "protocol": "dir_port"
  },
  "66.111.2.131:9001": {
    "address":  "66.111.2.131:9001",
    "protocol": "or_port_dirauth"
  }
}
```

When fetching the targets from OONI orchestra, the experiment MUST
ensure that either said targets are not logged, or they are sanitized
before being logged. This is useful to avoid inadvertently leaking
bridge addresses, fingerprints, etc. when logs are posted on public forums.

This experiment currently does not handle input formatted as a Tor
bridge line. A future version of this specification will handle this
specific use case.

# Test description

The test loops through the list of targets measuring. The
measurement action depends on the target type:

- for `dir_port` targets, the nettest will `GET` the
`/tor/status-vote/current/consensus.z` resource using
the HTTP protocol;

- for `or_port` and `or_port_dirauth` targets, the nettest will
connect to the address and perform a TLS handshake;

- for `obfs4` targets, the nettest will connect to
the address and perform an OBFS4 handshake;

- otherwise, the nettest will TCP connect to the address.

When all measurements are completed, the experiment MUST
perform the data sanitization steps described in the section
discussing privacy considerations.

# Expected output

```JSON
{
    "test_keys": {
        "dir_port_total": 0,
        "dir_port_accessible": 0,
        "obfs4_total": 0,
        "obfs4_accessible": 0,
        "or_port_dirauth_total": 0,
        "or_port_dirauth_accessible": 0,
        "or_port_total": 0,
        "or_port_accessible": 0,
        "targets": {
          "<targetId>": {}
        }
    }
}
```

- `dir_port_total` (`int`; since 2020-01-27): total number of `dir_port` targets.

- `dir_port_accessible` (`int`; since 2020-01-27): number of accessible `dir_port` targets.

- `obfs4_total` (`int`; since 2020-01-27): total number of `obfs4` targets.

- `obfs4_accessible` (`int`; since 2020-01-27): number of accessible `obfs4` targets.

- `or_port_dirauth_total` (`int`; since 2020-01-27): total number of `or_port_dirauth` targets.

- `or_port_dirauth_accessible` (`int`; since 2020-01-27): number of accessible `or_port_dirauth` targets.

- `or_port_total` (`int`; since 2020-01-27): total number of `or_port` targets.

- `or_port_accessible` (`int`; since 2020-01-27): number of accessible `or_port` targets.

- `targets` (`map[string]Targets`): measurements by target where
the key is the `id` of the target.

A `Target` data structure looks like:

```JSON
{
    "agent": "",
    "failure": "",
    "network_events": [],
    "queries": [],
    "requests": [],
    "target_address": "",
    "target_name": "",
    "target_protocol": "",
    "tcp_connect": [],
    "tls_handshakes": []
}
```

- `agent` (`string`): see `df-001-httpt`;

- `failure` (`string`; nullable): `null` on success, string on
error as documented in `df-007-errors.md`;

- `network_events` (`[]NetworkEvent`; nullable): see `df-008-netevents`;

- `queries` (`[]Query`; nullable): see `df-002-dnst`;

- `requests` (`[]Transaction`; nullable): see `df-001-httpt`;

- `target_address` (`string`): address of the target, generally expressed
in the `1.1.1.1:555` or the `[::1]:555` or the `domain:555` forms;

- `target_name` (`string`; optional): name of the target;

- `target_protocol` (`string`): protocol to access the target;

- `tcp_connect` (`[]TCPConnect`; nullable): see `df-005-tcpconnect`;

- `tls_handshakes` (`[]Handshake`; nullable): see `df-006-tlshandshake`.

## Parent data format

See the above fields description.

## Required output data

Fields described above (mind that many are nullable).

## Possible conclusions

For each target, we determine whether it was working or not by
checking its `failure` field. The ancillary data included helps to
better understand the reason for failure.

A future version of this specification will investigate into how
to more precisely classify possible `obfs4` failures.

## Example output sample

```JSON
{
  "annotations": {
    "_probe_engine_sanitize_test_keys": "true"
  },
  "data_format_version": "0.3.4",
  "measurement_start_time": "2020-01-27 20:00:56",
  "test_runtime": 8.148149319,
  "probe_asn": "AS30722",
  "probe_cc": "IT",
  "probe_ip": "127.0.0.1",
  "report_id": "20200127T200056Z_AS30722_DprYlwZMAgpYDB7pcIuGHqQpfb2krLi24pzte4BvLwTQjXl6zR",
  "resolver_asn": "AS30722",
  "resolver_ip": "91.80.36.88",
  "resolver_network_name": "Vodafone Italia S.p.A.",
  "software_name": "miniooni",
  "software_version": "0.1.0-dev",
  "test_keys": {
    "dir_port_total": 10,
    "dir_port_accessible": 9,
    "obfs4_total": 14,
    "obfs4_accessible": 14,
    "or_port_dirauth_total": 10,
    "or_port_dirauth_accessible": 10,
    "or_port_total": 0,
    "or_port_accessible": 0,
    "targets": {
      "02b5951c0a1ffa86c9f1c2034990472364c3500ffc1bb5a58a9946350e2a03d2": {
        "agent": "redirect",
        "failure": null,
        "network_events": [
          {
            "address": "37.218.240.34:40035",
            "conn_id": 6,
            "dial_id": 6,
            "failure": null,
            "operation": "connect",
            "proto": "tcp",
            "t": 1.879559
          },
          {
            "conn_id": 6,
            "failure": null,
            "num_bytes": 2003,
            "operation": "write",
            "proto": "tcp",
            "t": 1.880522
          },
          {
            "conn_id": 6,
            "failure": null,
            "num_bytes": 4320,
            "operation": "read",
            "proto": "tcp",
            "t": 2.095783
          },
          {
            "conn_id": 6,
            "failure": null,
            "num_bytes": 266,
            "operation": "read",
            "proto": "tcp",
            "t": 2.096087
          }
        ],
        "queries": null,
        "requests": null,
        "target_address": "37.218.240.34:40035",
        "target_protocol": "obfs4",
        "tcp_connect": [
          {
            "conn_id": 6,
            "dial_id": 6,
            "ip": "37.218.240.34",
            "port": 40035,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 1.879559
          }
        ],
        "tls_handshakes": null
      },
      "0fded903f932e4a29aa494ca63816cf6e18684097227d41cc8820ef9859558aa": {
        "agent": "redirect",
        "failure": null,
        "network_events": [
          {
            "address": "193.11.166.194:27015",
            "conn_id": 13,
            "dial_id": 13,
            "failure": null,
            "operation": "connect",
            "proto": "tcp",
            "t": 2.756319
          },
          {
            "conn_id": 13,
            "failure": null,
            "num_bytes": 1183,
            "operation": "write",
            "proto": "tcp",
            "t": 2.756971
          },
          {
            "conn_id": 13,
            "failure": null,
            "num_bytes": 1452,
            "operation": "read",
            "proto": "tcp",
            "t": 2.811501
          },
          {
            "conn_id": 13,
            "failure": null,
            "num_bytes": 4356,
            "operation": "read",
            "proto": "tcp",
            "t": 2.811944
          },
          {
            "conn_id": 13,
            "failure": null,
            "num_bytes": 1452,
            "operation": "read",
            "proto": "tcp",
            "t": 2.81209
          },
          {
            "conn_id": 13,
            "failure": null,
            "num_bytes": 305,
            "operation": "read",
            "proto": "tcp",
            "t": 2.812577
          }
        ],
        "queries": null,
        "requests": null,
        "target_address": "193.11.166.194:27015",
        "target_protocol": "obfs4",
        "tcp_connect": [
          {
            "conn_id": 13,
            "dial_id": 13,
            "ip": "193.11.166.194",
            "port": 27015,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 2.756319
          }
        ],
        "tls_handshakes": null
      },
      "128.31.0.39:9101": {
        "agent": "redirect",
        "failure": null,
        "network_events": [
          {
            "address": "128.31.0.39:9101",
            "conn_id": 17,
            "dial_id": 17,
            "failure": null,
            "operation": "connect",
            "proto": "tcp",
            "t": 3.074852
          },
          {
            "conn_id": 17,
            "failure": null,
            "num_bytes": 243,
            "operation": "write",
            "proto": "tcp",
            "t": 3.075221
          },
          {
            "conn_id": 17,
            "failure": null,
            "num_bytes": 517,
            "operation": "read",
            "proto": "tcp",
            "t": 3.188952
          },
          {
            "conn_id": 17,
            "failure": null,
            "num_bytes": 490,
            "operation": "read",
            "proto": "tcp",
            "t": 3.189069
          },
          {
            "conn_id": 17,
            "failure": null,
            "num_bytes": 126,
            "operation": "write",
            "proto": "tcp",
            "t": 3.189941
          },
          {
            "conn_id": 17,
            "failure": null,
            "num_bytes": 51,
            "operation": "read",
            "proto": "tcp",
            "t": 3.301111
          },
          {
            "conn_id": 17,
            "failure": null,
            "num_bytes": 31,
            "operation": "write",
            "proto": "tcp",
            "t": 3.301335
          }
        ],
        "queries": null,
        "requests": null,
        "target_address": "128.31.0.39:9101",
        "target_name": "moria1",
        "target_protocol": "or_port_dirauth",
        "tcp_connect": [
          {
            "conn_id": 17,
            "dial_id": 17,
            "ip": "128.31.0.39",
            "port": 9101,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 3.074852
          }
        ],
        "tls_handshakes": [
          {
            "cipher_suite": "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384",
            "conn_id": 17,
            "failure": null,
            "negotiated_protocol": "",
            "peer_certificates": [
              {
                "data": "MIICQzCCAaygAwIBAgIIcUWaetb4E04wDQYJKoZIhvcNAQELBQAwJjEkMCIGA1UEAxMbd3d3LnF5cnMybHB4bWRxN3lkM2U3YnEuY29tMB4XDTE5MDkwMTAwMDAwMFoXDTIwMDcyMjIzNTk1OVowHjEcMBoGA1UEAxMTd3d3LnB5ZDRucWZjamZtLm5ldDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBANiVT4Nxrh0/3iELTF0jqSpVhNBB3a+f1/EwaClu+PfjtYlIfEyfJIFcj64DFyel0tJQpoJdIwJ4n4llWxTVtBH4/nga3rYJmw3tggwmKyNfZGzfu1UODR2umwCE6WlCipluhRw1jzOHAC0Zm5bhufJ7DqBWUGk0pvx0sx0/FWUkgSecBcG3FfXBHQVVOKs0ezd+TJILvKXaUxHZWiQkKw1pKpuQ3rHfw8NNCcGgWo7YauxLWs6ZHeqA0POVFJpcbKkAh9dBSI0E73Y6PN4MkPg9KvRzr6HmUbYaDeVFM4uM3UrH5CnXi18QsPmY5/o6R3+gQPkx1IacokFMBLgf2gkCAwEAATANBgkqhkiG9w0BAQsFAAOBgQAqrehLiME6MAJssfv2KPRmfhkxr3pzxq+fPnqr5xVlsW0xkj/p55SzwM+E/5QCgb/dHfTRcSfjZyqrKEIu4iOkViXVcOZjxI0Hop56rPc8paq+3G+Uh1exWvqGJn3AzGrHfjs1Qt6es48qBQ7a8Bjmx2mthOYCne0rnuwwY3E0Tw==",
                "format": "base64"
              }
            ],
            "t": 3.30121,
            "tls_version": "TLSv1.2"
          }
        ]
      },
      "128.31.0.39:9131": {
        "agent": "redirect",
        "failure": "Get http://128.31.0.39:9131/tor/status-vote/current/consensus.z: eof_error",
        "network_events": null,
        "queries": null,
        "requests": [
          {
            "failure": null,
            "request": {
              "body": "",
              "body_is_truncated": false,
              "headers_list": [
                [
                  "Accept-Language",
                  "en-US;q=0.8,en;q=0.5"
                ],
                [
                  "Host",
                  "128.31.0.39:9131"
                ],
                [
                  "User-Agent",
                  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
                ],
                [
                  "Accept",
                  "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
                ]
              ],
              "headers": {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-US;q=0.8,en;q=0.5",
                "Host": "128.31.0.39:9131",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
              },
              "method": "GET",
              "tor": {
                "exit_ip": null,
                "exit_name": null,
                "is_tor": false
              },
              "url": "http://128.31.0.39:9131/tor/status-vote/current/consensus.z"
            },
            "response": {
              "body": "",
              "body_is_truncated": false,
              "code": 503,
              "headers_list": [
                [
                  "Date",
                  "Mon, 27 Jan 2020 20:00:59 GMT"
                ]
              ],
              "headers": {
                "Date": "Mon, 27 Jan 2020 20:00:59 GMT"
              }
            },
            "transaction_id": 3
          }
        ],
        "target_address": "128.31.0.39:9131",
        "target_name": "moria1",
        "target_protocol": "dir_port",
        "tcp_connect": [
          {
            "conn_id": 7,
            "dial_id": 7,
            "ip": "128.31.0.39",
            "port": 9131,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 2.20902,
            "transaction_id": 3
          }
        ],
        "tls_handshakes": null
      },
      "131.188.40.189:443": {
        "agent": "redirect",
        "failure": null,
        "network_events": [
          {
            "address": "131.188.40.189:443",
            "conn_id": 2,
            "dial_id": 1,
            "failure": null,
            "operation": "connect",
            "proto": "tcp",
            "t": 1.493196
          },
          {
            "conn_id": 2,
            "failure": null,
            "num_bytes": 243,
            "operation": "write",
            "proto": "tcp",
            "t": 1.4935
          },
          {
            "conn_id": 2,
            "failure": null,
            "num_bytes": 99,
            "operation": "read",
            "proto": "tcp",
            "t": 1.535635
          },
          {
            "conn_id": 2,
            "failure": null,
            "num_bytes": 6,
            "operation": "write",
            "proto": "tcp",
            "t": 1.535855
          },
          {
            "conn_id": 2,
            "failure": null,
            "num_bytes": 276,
            "operation": "write",
            "proto": "tcp",
            "t": 1.536127
          },
          {
            "conn_id": 2,
            "failure": null,
            "num_bytes": 517,
            "operation": "read",
            "proto": "tcp",
            "t": 1.5791279999999999
          },
          {
            "conn_id": 2,
            "failure": null,
            "num_bytes": 651,
            "operation": "read",
            "proto": "tcp",
            "t": 1.580098
          },
          {
            "conn_id": 2,
            "failure": null,
            "num_bytes": 74,
            "operation": "write",
            "proto": "tcp",
            "t": 1.581019
          },
          {
            "conn_id": 2,
            "failure": null,
            "num_bytes": 24,
            "operation": "write",
            "proto": "tcp",
            "t": 1.581248
          }
        ],
        "queries": null,
        "requests": null,
        "target_address": "131.188.40.189:443",
        "target_name": "gabelmoo",
        "target_protocol": "or_port_dirauth",
        "tcp_connect": [
          {
            "conn_id": 2,
            "dial_id": 1,
            "ip": "131.188.40.189",
            "port": 443,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 1.493196
          }
        ],
        "tls_handshakes": [
          {
            "cipher_suite": "TLS_AES_256_GCM_SHA384",
            "conn_id": 2,
            "failure": null,
            "negotiated_protocol": "",
            "peer_certificates": [
              {
                "data": "MIICRTCCAa6gAwIBAgIIUxolEWB2INEwDQYJKoZIhvcNAQELBQAwJzElMCMGA1UEAwwcd3d3LnpsYzVidTVmb3V2eGJwdWpnajJiLmNvbTAeFw0xOTA3MTAwMDAwMDBaFw0yMDA0MDQyMzU5NTlaMB8xHTAbBgNVBAMMFHd3dy50ZGViN2dlM2h5bTYubmV0MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA1SYqxdMJ7CP6DpDi1qZQSk/aF4QNh06ZkFc7mxWVSNW5P2WX750o/P7ccEL9V4YWJ7j0JHj4Q5S2u/oVnwEkJgj75tSQbO/fJXZI7KP+wMi4TUDCQdF76mFilTRvzcw+e3rXgLqG/qzFrHvQZ0X5Muwc9S9hj04PlNJoMvYUTs20hlpbWCq82EakK0I3i6DBj5uhZF+nimuDiUF/n1j9/4K+8+aUoqPX9EnhMASB5dKrztr6JxmT4ZkwGL32szlLgkK39+oHdhzivJUFJk77CI7V7OPEhZxYBAjB+TbbjRTVzp4UUsW4IRyT4Tx60s+RwUfHPsR7KVvx2oQVGnxlwwIDAQABMA0GCSqGSIb3DQEBCwUAA4GBAI0/nCalvLJdtY3OeqMtUDv4fS2dYdgXJr6ZGLBhNsbCalMBmG7P1yZ+6SrTltYtdP4t4fgWtO0OBKqyHeu5tEW4LZ4SL2jXBiZ3y5yp8b4eslMej0OZZ81lwi2ndVfXq5AINk0VpGpPnJlNh4mtO3D/wFddGoyFneybTP+2OSSN",
                "format": "base64"
              }
            ],
            "t": 1.581081,
            "tls_version": "TLSv1.3"
          }
        ]
      },
      "131.188.40.189:80": {
        "agent": "redirect",
        "failure": null,
        "network_events": null,
        "queries": null,
        "requests": [
          {
            "failure": null,
            "request": {
              "body": "",
              "body_is_truncated": false,
              "headers_list": [
                [
                  "User-Agent",
                  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
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
                  "Host",
                  "131.188.40.189:80"
                ]
              ],
              "headers": {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-US;q=0.8,en;q=0.5",
                "Host": "131.188.40.189:80",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
              },
              "method": "GET",
              "tor": {
                "exit_ip": null,
                "exit_name": null,
                "is_tor": false
              },
              "url": "http://131.188.40.189:80/tor/status-vote/current/consensus.z"
            },
            "response": {
              "body": {
                "data": "eNrs/Wlz40a2NYx+71+Bj/cGbRGJxMh4+o0HE0mQBOcJvHHiBGaCGImBIPjrbyZUVS6hJLvt6nMs6W27ipJYEgVsZuae1l4rccs6zcNfi9Isq+LXm5sXQZoQ8B+3tHS/PEvYaVK4SVEV//j22a+xW55Th6CEf9zMKHB+Nb3SzQmKpMhfSfArxaFPByT+8w8vd4vzr1VSBtGLfwdf/v3553/8d/j139MySPxfHTcyGwKSJP77DzsK3KT8er0FQT7BJ+aJ++X5I//lo4A+0k/kE/PlI9t+BE/Ur2aUnc0vX8EXX9G/5vaXT5kvH7/+GPflI99+pJ7Adz9IvXhR6sWLUg==",
                "format": "base64"
              },
              "body_is_truncated": true,
              "code": 200,
              "headers_list": [
                [
                  "Date",
                  "Mon, 27 Jan 2020 20:00:58 GMT"
                ],
                [
                  "Content-Type",
                  "text/plain"
                ],
                [
                  "X-Your-Address-Is",
                  "[REDACTED]"
                ],
                [
                  "Content-Encoding",
                  "deflate"
                ],
                [
                  "Expires",
                  "Mon, 27 Jan 2020 21:00:00 GMT"
                ],
                [
                  "Vary",
                  "X-Or-Diff-From-Consensus"
                ]
              ],
              "headers": {
                "Content-Encoding": "deflate",
                "Content-Type": "text/plain",
                "Date": "Mon, 27 Jan 2020 20:00:58 GMT",
                "Expires": "Mon, 27 Jan 2020 21:00:00 GMT",
                "Vary": "X-Or-Diff-From-Consensus",
                "X-Your-Address-Is": "[REDACTED]"
              }
            },
            "transaction_id": 1
          }
        ],
        "target_address": "131.188.40.189:80",
        "target_name": "gabelmoo",
        "target_protocol": "dir_port",
        "tcp_connect": [
          {
            "conn_id": 3,
            "dial_id": 3,
            "ip": "131.188.40.189",
            "port": 80,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 1.614135,
            "transaction_id": 1
          }
        ],
        "tls_handshakes": null
      },
      "154.35.175.225:443": {
        "agent": "redirect",
        "failure": null,
        "network_events": [
          {
            "address": "154.35.175.225:443",
            "conn_id": 34,
            "dial_id": 34,
            "failure": null,
            "operation": "connect",
            "proto": "tcp",
            "t": 6.433886
          },
          {
            "conn_id": 34,
            "failure": null,
            "num_bytes": 243,
            "operation": "write",
            "proto": "tcp",
            "t": 6.43414
          },
          {
            "conn_id": 34,
            "failure": null,
            "num_bytes": 517,
            "operation": "read",
            "proto": "tcp",
            "t": 6.564444
          },
          {
            "conn_id": 34,
            "failure": null,
            "num_bytes": 478,
            "operation": "read",
            "proto": "tcp",
            "t": 6.564535
          },
          {
            "conn_id": 34,
            "failure": null,
            "num_bytes": 126,
            "operation": "write",
            "proto": "tcp",
            "t": 6.565893
          },
          {
            "conn_id": 34,
            "failure": null,
            "num_bytes": 51,
            "operation": "read",
            "proto": "tcp",
            "t": 6.69516
          },
          {
            "conn_id": 34,
            "failure": null,
            "num_bytes": 31,
            "operation": "write",
            "proto": "tcp",
            "t": 6.695382
          }
        ],
        "queries": null,
        "requests": null,
        "target_address": "154.35.175.225:443",
        "target_name": "Faravahar",
        "target_protocol": "or_port_dirauth",
        "tcp_connect": [
          {
            "conn_id": 34,
            "dial_id": 34,
            "ip": "154.35.175.225",
            "port": 443,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 6.433886
          }
        ],
        "tls_handshakes": [
          {
            "cipher_suite": "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384",
            "conn_id": 34,
            "failure": null,
            "negotiated_protocol": "",
            "peer_certificates": [
              {
                "data": "MIICNzCCAaCgAwIBAgIIflqmLNYhhJ0wDQYJKoZIhvcNAQELBQAwHTEbMBkGA1UEAwwSd3d3LnhqeGJxYmwyaXEuY29tMB4XDTE5MTEwNjAwMDAwMFoXDTIwMDkxODAwMDAwMFowGzEZMBcGA1UEAwwQd3d3LmF5a29vY3BqLm5ldDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAO1UWIAJAOjjNV68Z0oHSZDAauPAUP1NSuxQzEO3h1bb7Gv7+UusEbInuCi9AvxtVLh96In2tjUIVErwFREPE2TWAv/q3OHJdsrUYuLqjBn+68ICvT0N0GNL9Xc7m1vWK7roGK7aJowOQ1vQJLQVmz73pgs+izoDqJ1vASHPOfUA2GOH0Tg9AxqpXsbRllWJOIKkNuAu1HMtNC3iKqn/MuCSzikWjzpwec432vBi9P3o4m3eo07XMF1lmlRbQCUaIyN+Fm71twNJFIOsZa5aremJc7vYnYDQmqyMbgqXVC28G/DGXtA8HThuXsIXKDamINHzVnEMWf4K19er0PUc5dcCAwEAATANBgkqhkiG9w0BAQsFAAOBgQBbZ9jpOJV8W8JK8H4DuoMg3b/sI1Esmy7fwA6X7rBJxethxVauPOPVBf17ishQb6WrutZ0GpjtFNmZcR8bfoIipNC8k3856a8FrcxkYCPjvjENBYESbW0u1eydrRNBjp/+VlyhbkPYCENzfwRsqzKzW3aOW4kJuZgOqI4lxAc8rg==",
                "format": "base64"
              }
            ],
            "t": 6.695244,
            "tls_version": "TLSv1.2"
          }
        ]
      },
      "154.35.175.225:80": {
        "agent": "redirect",
        "failure": null,
        "network_events": null,
        "queries": null,
        "requests": [
          {
            "failure": null,
            "request": {
              "body": "",
              "body_is_truncated": false,
              "headers_list": [
                [
                  "Host",
                  "154.35.175.225:80"
                ],
                [
                  "User-Agent",
                  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
                ],
                [
                  "Accept",
                  "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
                ],
                [
                  "Accept-Language",
                  "en-US;q=0.8,en;q=0.5"
                ]
              ],
              "headers": {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-US;q=0.8,en;q=0.5",
                "Host": "154.35.175.225:80",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
              },
              "method": "GET",
              "tor": {
                "exit_ip": null,
                "exit_name": null,
                "is_tor": false
              },
              "url": "http://154.35.175.225:80/tor/status-vote/current/consensus.z"
            },
            "response": {
              "body": {
                "data": "eNrs/Wlz40a2NYx+71+Bj/cGbRGJxMh4+o0HE0mQBOcJvHHiBGaCGImBIPjrbyZUVS6hJLvt6nMs6W27ipJYEgVsZuae1l4rccs6zcNfi9Isq+LXm5sXQZoQ8B+3tHS/PEvYaVK4SVEV//j22a+xW55Th6CEf9zMKHB+Nb3SzQmKpMhfSfArxaFPByT+8w8vd4vzr1VSBtGLfwdf/v3553/8d/j139MySPxfHTcyGwKSJP77DzsK3KT8er0FQT7BJ+aJ++X5I//lo4A+0k/kE/PlI9t+BE/Ur2aUnc0vX8EXX9G/5vaXT5kvH7/+GPflI99+pJ7Adz9IvXhR6sWLUg==",
                "format": "base64"
              },
              "body_is_truncated": true,
              "code": 200,
              "headers_list": [
                [
                  "Content-Type",
                  "text/plain"
                ],
                [
                  "X-Your-Address-Is",
                  "[REDACTED]"
                ],
                [
                  "Content-Encoding",
                  "deflate"
                ],
                [
                  "Expires",
                  "Mon, 27 Jan 2020 21:00:00 GMT"
                ],
                [
                  "Vary",
                  "X-Or-Diff-From-Consensus"
                ],
                [
                  "Date",
                  "Mon, 27 Jan 2020 20:01:01 GMT"
                ]
              ],
              "headers": {
                "Content-Encoding": "deflate",
                "Content-Type": "text/plain",
                "Date": "Mon, 27 Jan 2020 20:01:01 GMT",
                "Expires": "Mon, 27 Jan 2020 21:00:00 GMT",
                "Vary": "X-Or-Diff-From-Consensus",
                "X-Your-Address-Is": "[REDACTED]"
              }
            },
            "transaction_id": 8
          }
        ],
        "target_address": "154.35.175.225:80",
        "target_name": "Faravahar",
        "target_protocol": "dir_port",
        "tcp_connect": [
          {
            "conn_id": 25,
            "dial_id": 24,
            "ip": "154.35.175.225",
            "port": 80,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 4.238872,
            "transaction_id": 8
          }
        ],
        "tls_handshakes": null
      },
      "171.25.193.9:443": {
        "agent": "redirect",
        "failure": null,
        "network_events": null,
        "queries": null,
        "requests": [
          {
            "failure": null,
            "request": {
              "body": "",
              "body_is_truncated": false,
              "headers_list": [
                [
                  "Host",
                  "171.25.193.9:443"
                ],
                [
                  "User-Agent",
                  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
                ],
                [
                  "Accept",
                  "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
                ],
                [
                  "Accept-Language",
                  "en-US;q=0.8,en;q=0.5"
                ]
              ],
              "headers": {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-US;q=0.8,en;q=0.5",
                "Host": "171.25.193.9:443",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
              },
              "method": "GET",
              "tor": {
                "exit_ip": null,
                "exit_name": null,
                "is_tor": false
              },
              "url": "http://171.25.193.9:443/tor/status-vote/current/consensus.z"
            },
            "response": {
              "body": {
                "data": "eNrs/Wlz40a2NYx+71+Bj/cGbRGJxMh4+o0HE0mQBOcJvHHiBGaCGImBIPjrbyZUVS6hJLvt6nMs6W27ipJYEgVsZuae1l4rccs6zcNfi9Isq+LXm5sXQZoQ8B+3tHS/PEvYaVK4SVEV//j22a+xW55Th6CEf9zMKHB+Nb3SzQmKpMhfSfArxaFPByT+8w8vd4vzr1VSBtGLfwdf/v3553/8d/j139MySPxfHTcyGwKSJP77DzsK3KT8er0FQT7BJ+aJ++X5I//lo4A+0k/kE/PlI9t+BE/Ur2aUnc0vX8EXX9G/5vaXT5kvH7/+GPflI99+pJ7Adz9IvXhR6sWLUg==",
                "format": "base64"
              },
              "body_is_truncated": true,
              "code": 200,
              "headers_list": [
                [
                  "Date",
                  "Mon, 27 Jan 2020 20:00:58 GMT"
                ],
                [
                  "Content-Type",
                  "text/plain"
                ],
                [
                  "X-Your-Address-Is",
                  "[REDACTED]"
                ],
                [
                  "Content-Encoding",
                  "deflate"
                ],
                [
                  "Expires",
                  "Mon, 27 Jan 2020 21:00:00 GMT"
                ],
                [
                  "Vary",
                  "X-Or-Diff-From-Consensus"
                ]
              ],
              "headers": {
                "Content-Encoding": "deflate",
                "Content-Type": "text/plain",
                "Date": "Mon, 27 Jan 2020 20:00:58 GMT",
                "Expires": "Mon, 27 Jan 2020 21:00:00 GMT",
                "Vary": "X-Or-Diff-From-Consensus",
                "X-Your-Address-Is": "[REDACTED]"
              }
            },
            "transaction_id": 2
          }
        ],
        "target_address": "171.25.193.9:443",
        "target_name": "maatuska",
        "target_protocol": "dir_port",
        "tcp_connect": [
          {
            "conn_id": 4,
            "dial_id": 4,
            "ip": "171.25.193.9",
            "port": 443,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 1.629615,
            "transaction_id": 2
          }
        ],
        "tls_handshakes": null
      },
      "171.25.193.9:80": {
        "agent": "redirect",
        "failure": null,
        "network_events": [
          {
            "address": "171.25.193.9:80",
            "conn_id": 26,
            "dial_id": 26,
            "failure": null,
            "operation": "connect",
            "proto": "tcp",
            "t": 4.352969
          },
          {
            "conn_id": 26,
            "failure": null,
            "num_bytes": 243,
            "operation": "write",
            "proto": "tcp",
            "t": 4.353302
          },
          {
            "conn_id": 26,
            "failure": null,
            "num_bytes": 99,
            "operation": "read",
            "proto": "tcp",
            "t": 4.402885
          },
          {
            "conn_id": 26,
            "failure": null,
            "num_bytes": 6,
            "operation": "write",
            "proto": "tcp",
            "t": 4.403055
          },
          {
            "conn_id": 26,
            "failure": null,
            "num_bytes": 276,
            "operation": "write",
            "proto": "tcp",
            "t": 4.403255
          },
          {
            "conn_id": 26,
            "failure": null,
            "num_bytes": 517,
            "operation": "read",
            "proto": "tcp",
            "t": 4.456783
          },
          {
            "conn_id": 26,
            "failure": null,
            "num_bytes": 650,
            "operation": "read",
            "proto": "tcp",
            "t": 4.45721
          },
          {
            "conn_id": 26,
            "failure": null,
            "num_bytes": 74,
            "operation": "write",
            "proto": "tcp",
            "t": 4.457774
          },
          {
            "conn_id": 26,
            "failure": null,
            "num_bytes": 24,
            "operation": "write",
            "proto": "tcp",
            "t": 4.457995
          }
        ],
        "queries": null,
        "requests": null,
        "target_address": "171.25.193.9:80",
        "target_name": "maatuska",
        "target_protocol": "or_port_dirauth",
        "tcp_connect": [
          {
            "conn_id": 26,
            "dial_id": 26,
            "ip": "171.25.193.9",
            "port": 80,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 4.352969
          }
        ],
        "tls_handshakes": [
          {
            "cipher_suite": "TLS_AES_256_GCM_SHA384",
            "conn_id": 26,
            "failure": null,
            "negotiated_protocol": "",
            "peer_certificates": [
              {
                "data": "MIICRDCCAa2gAwIBAgIJAKYcvL/e2Le7MA0GCSqGSIb3DQEBCwUAMCUxIzAhBgNVBAMMGnd3dy5wejVsYzU2M3V3cXFucW90bmsuY29tMB4XDTIwMDEwMjAwMDAwMFoXDTIwMDIxNDIzNTk1OVowHzEdMBsGA1UEAwwUd3d3LnpoamZpcjNweWFvei5uZXQwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCcvocrwoWofSd5JxW78lM2L5NQLpdCrBAKSpRisTrNBbD5i3D0Ts+Zbv/uDwjfggbcrYgcGu21V+4ZQl9f3j+l67wxQN4ski0qd3QBflQ04A5D2jT1ETZOFSqxsOISHT0LhyutFvVEcqgBJE6ihA2OA+kQcOLrvz/PkFvN5uVVtlisWfbE4HKXcAn+yz3Itjx4jJMe+ZXK7Y6TceaAlCLvf9S7IYI5KcOIZL+z9KOFXT5M82ukEsKFj3DU40Q028lRDIQLyx2VSjNQ6Nhj7z3VKQ+M8PzJO+3X+IVdvptXqMtfUT14ni0ZnF5mZ8VU6Z5FrIULUfcPdhns+BNpNbZlAgMBAAEwDQYJKoZIhvcNAQELBQADgYEAFoJ4pV7skxvtQNf9pScv8tW4doOSQwkmBqVBQEZg0cnOnukTUX8cTWwbljIf520FKePrsqC80RVQBHhg+IeqZGvzK23TMCZQifSPUXg/797TFFqHQbkfEaL9zoVv0U+ZtdTBFFF8NtbTvi944xPp5SdQ/sahfeyRSlS+ZwfN+GE=",
                "format": "base64"
              }
            ],
            "t": 4.457788,
            "tls_version": "TLSv1.3"
          }
        ]
      },
      "193.23.244.244:443": {
        "agent": "redirect",
        "failure": null,
        "network_events": [
          {
            "address": "193.23.244.244:443",
            "conn_id": 11,
            "dial_id": 11,
            "failure": null,
            "operation": "connect",
            "proto": "tcp",
            "t": 2.47631
          },
          {
            "conn_id": 11,
            "failure": null,
            "num_bytes": 243,
            "operation": "write",
            "proto": "tcp",
            "t": 2.4767989999999998
          },
          {
            "conn_id": 11,
            "failure": null,
            "num_bytes": 517,
            "operation": "read",
            "proto": "tcp",
            "t": 2.519022
          },
          {
            "conn_id": 11,
            "failure": null,
            "num_bytes": 491,
            "operation": "read",
            "proto": "tcp",
            "t": 2.519146
          },
          {
            "conn_id": 11,
            "failure": null,
            "num_bytes": 126,
            "operation": "write",
            "proto": "tcp",
            "t": 2.5201599999999997
          },
          {
            "conn_id": 11,
            "failure": null,
            "num_bytes": 51,
            "operation": "read",
            "proto": "tcp",
            "t": 2.55951
          },
          {
            "conn_id": 11,
            "failure": null,
            "num_bytes": 31,
            "operation": "write",
            "proto": "tcp",
            "t": 2.5597250000000003
          }
        ],
        "queries": null,
        "requests": null,
        "target_address": "193.23.244.244:443",
        "target_name": "dannenberg",
        "target_protocol": "or_port_dirauth",
        "tcp_connect": [
          {
            "conn_id": 11,
            "dial_id": 11,
            "ip": "193.23.244.244",
            "port": 443,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 2.47631
          }
        ],
        "tls_handshakes": [
          {
            "cipher_suite": "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384",
            "conn_id": 11,
            "failure": null,
            "negotiated_protocol": "",
            "peer_certificates": [
              {
                "data": "MIICRjCCAa+gAwIBAgIJAPF5DbNTzoYuMA0GCSqGSIb3DQEBCwUAMCUxIzAhBgNVBAMMGnd3dy5tem5qbmRlYnZybTV0dHZvc3UuY29tMB4XDTE5MTEyNjAwMDAwMFoXDTIwMDQwODAwMDAwMFowITEfMB0GA1UEAwwWd3d3LmIzdTIzY2tubTdnMnd6Lm5ldDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAOE3nTQ+0zMWPWWcyu4KniLB5Sat2rTTxuiUf38njsfcrJliIGUlx2e9AWfryuRzYibrEc09i2rYbIsjw9uErO38+0MNN121+dTnm4eg5D3Rdtmizf68Rg6TzTHHsu99yH58NuujNownCbRZVdjRj6xZkzYHAm3k84uDbow6lbxU1M7cYivhtRphnmHUINcmA43xlAd6tDyaMIqJvnxGi6johfHktl092tJQxLzKgDp/1APV8gdiKitB5VmMRZW/60D1UJsQNAptT+cyovSoZOkue37KK6rkxTjhO3tOm4wMLhT8nB+kh+hgRf7Ugf7i0vVEa8TPZm071/zn2TTkCg8CAwEAATANBgkqhkiG9w0BAQsFAAOBgQBloSujo0JHEV/7v6cNwmWqGKwlKqBUx5Wal9ULMF14jXBZFStPTghD1ZJ4zRoTeJEbjyU8srk4KABQ2DD1Q+CI0gf6gCv2BNjbSf++56b3we4wVPGvaHT7GlIyLMemzlPUIsqmVmUe3K2fh0up7Vil9AQtA1JRLCPl9v2znuyqPQ==",
                "format": "base64"
              }
            ],
            "t": 2.559591,
            "tls_version": "TLSv1.2"
          }
        ]
      },
      "193.23.244.244:80": {
        "agent": "redirect",
        "failure": null,
        "network_events": null,
        "queries": null,
        "requests": [
          {
            "failure": null,
            "request": {
              "body": "",
              "body_is_truncated": false,
              "headers_list": [
                [
                  "Accept-Language",
                  "en-US;q=0.8,en;q=0.5"
                ],
                [
                  "Host",
                  "193.23.244.244:80"
                ],
                [
                  "User-Agent",
                  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
                ],
                [
                  "Accept",
                  "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
                ]
              ],
              "headers": {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-US;q=0.8,en;q=0.5",
                "Host": "193.23.244.244:80",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
              },
              "method": "GET",
              "tor": {
                "exit_ip": null,
                "exit_name": null,
                "is_tor": false
              },
              "url": "http://193.23.244.244:80/tor/status-vote/current/consensus.z"
            },
            "response": {
              "body": {
                "data": "eNrs/Wlz40a2NYx+71+Bj/cGbRGJxMh4+o0HE0mQBOcJvHHiBGaCGImBIPjrbyZUVS6hJLvt6nMs6W27ipJYEgVsZuae1l4rccs6zcNfi9Isq+LXm5sXQZoQ8B+3tHS/PEvYaVK4SVEV//j22a+xW55Th6CEf9zMKHB+Nb3SzQmKpMhfSfArxaFPByT+8w8vd4vzr1VSBtGLfwdf/v3553/8d/j139MySPxfHTcyGwKSJP77DzsK3KT8er0FQT7BJ+aJ++X5I//lo4A+0k/kE/PlI9t+BE/Ur2aUnc0vX8EXX9G/5vaXT5kvH7/+GPflI99+pJ7Adz9IvXhR6sWLUg==",
                "format": "base64"
              },
              "body_is_truncated": true,
              "code": 200,
              "headers_list": [
                [
                  "Vary",
                  "X-Or-Diff-From-Consensus"
                ],
                [
                  "Date",
                  "Mon, 27 Jan 2020 20:00:59 GMT"
                ],
                [
                  "Content-Type",
                  "text/plain"
                ],
                [
                  "X-Your-Address-Is",
                  "[REDACTED]"
                ],
                [
                  "Content-Encoding",
                  "deflate"
                ],
                [
                  "Expires",
                  "Mon, 27 Jan 2020 21:00:00 GMT"
                ]
              ],
              "headers": {
                "Content-Encoding": "deflate",
                "Content-Type": "text/plain",
                "Date": "Mon, 27 Jan 2020 20:00:59 GMT",
                "Expires": "Mon, 27 Jan 2020 21:00:00 GMT",
                "Vary": "X-Or-Diff-From-Consensus",
                "X-Your-Address-Is": "[REDACTED]"
              }
            },
            "transaction_id": 4
          }
        ],
        "target_address": "193.23.244.244:80",
        "target_name": "dannenberg",
        "target_protocol": "dir_port",
        "tcp_connect": [
          {
            "conn_id": 8,
            "dial_id": 8,
            "ip": "193.23.244.244",
            "port": 80,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 2.267295,
            "transaction_id": 4
          }
        ],
        "tls_handshakes": null
      },
      "199.58.81.140:443": {
        "agent": "redirect",
        "failure": null,
        "network_events": [
          {
            "address": "199.58.81.140:443",
            "conn_id": 28,
            "dial_id": 28,
            "failure": null,
            "operation": "connect",
            "proto": "tcp",
            "t": 4.580539
          },
          {
            "conn_id": 28,
            "failure": null,
            "num_bytes": 243,
            "operation": "write",
            "proto": "tcp",
            "t": 4.580874
          },
          {
            "conn_id": 28,
            "failure": null,
            "num_bytes": 517,
            "operation": "read",
            "proto": "tcp",
            "t": 4.910435
          },
          {
            "conn_id": 28,
            "failure": null,
            "num_bytes": 489,
            "operation": "read",
            "proto": "tcp",
            "t": 4.910532
          },
          {
            "conn_id": 28,
            "failure": null,
            "num_bytes": 126,
            "operation": "write",
            "proto": "tcp",
            "t": 4.911205
          },
          {
            "conn_id": 28,
            "failure": null,
            "num_bytes": 51,
            "operation": "read",
            "proto": "tcp",
            "t": 5.114199
          },
          {
            "conn_id": 28,
            "failure": null,
            "num_bytes": 31,
            "operation": "write",
            "proto": "tcp",
            "t": 5.114412
          }
        ],
        "queries": null,
        "requests": null,
        "target_address": "199.58.81.140:443",
        "target_name": "longclaw",
        "target_protocol": "or_port_dirauth",
        "tcp_connect": [
          {
            "conn_id": 28,
            "dial_id": 28,
            "ip": "199.58.81.140",
            "port": 443,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 4.580539
          }
        ],
        "tls_handshakes": [
          {
            "cipher_suite": "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384",
            "conn_id": 28,
            "failure": null,
            "negotiated_protocol": "",
            "peer_certificates": [
              {
                "data": "MIICQjCCAaugAwIBAgIIJio5MNflyeYwDQYJKoZIhvcNAQELBQAwITEfMB0GA1UEAwwWd3d3LmN2MmR4ZzJpa3J1NmdzLmNvbTAeFw0xOTEwMTUwMDAwMDBaFw0yMDAyMjkwMDAwMDBaMCIxIDAeBgNVBAMMF3d3dy5oc2lxZ3FweDQ0N2hjbGIubmV0MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAynqGy9Tk9HVH8wbEKvI9QghWa45PJBIcIvr2NHVBuPCMJcoXPBDUh/ClYenBSAGfQuFoYFKWRs21WLNoI6AxVtFq8Pk3EegoCeC2kkuO+VWxh9wPy7DHFpFf2NRpVCn6wK6C+1hud9erHk6uDSau1gLMAb+ppfWS1qQ9iHCSrhsJGHyB85h3X64birarUh89QQBK7lhUigKEDx9Upg/jJG5zY3/odWqGdc+d6RQ+B3hwNoy4W7bZqi+ihYbxt5GZ7mAwzam6Z0YnWPBnbYgJdb7CaF1bkcOXJSBd3NlvSr9hlRCOv0ees/Gr6qbgaKnxy7lVyKxxZCnYY75mb6aDtQIDAQABMA0GCSqGSIb3DQEBCwUAA4GBAJOosVHVUnjM9Tr5DFuCuNcM/32ddnbl/dvjT1lAzcBkF1b0nev0pN3cqFrPj3Nh0lFH8BdcT724ZRuoW3pPz71t5s33FrPPfSatr4rbMbyR3ShIFz+8eMzpYqBUu0kuwOhQmi1FRBhmEI3faTXpnv7zRYeTcRo30zixbNG0ocLU",
                "format": "base64"
              }
            ],
            "t": 5.114303,
            "tls_version": "TLSv1.2"
          }
        ]
      },
      "199.58.81.140:80": {
        "agent": "redirect",
        "failure": null,
        "network_events": null,
        "queries": null,
        "requests": [
          {
            "failure": null,
            "request": {
              "body": "",
              "body_is_truncated": false,
              "headers_list": [
                [
                  "User-Agent",
                  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
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
                  "Host",
                  "199.58.81.140:80"
                ]
              ],
              "headers": {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-US;q=0.8,en;q=0.5",
                "Host": "199.58.81.140:80",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
              },
              "method": "GET",
              "tor": {
                "exit_ip": null,
                "exit_name": null,
                "is_tor": false
              },
              "url": "http://199.58.81.140:80/tor/status-vote/current/consensus.z"
            },
            "response": {
              "body": {
                "data": "eNrs/Wlz40a2NYx+71+Bj/cGbRGJxMh4+o0HE0mQBOcJvHHiBGaCGImBIPjrbyZUVS6hJLvt6nMs6W27ipJYEgVsZuae1l4rccs6zcNfi9Isq+LXm5sXQZoQ8B+3tHS/PEvYaVK4SVEV//j22a+xW55Th6CEf9zMKHB+Nb3SzQmKpMhfSfArxaFPByT+8w8vd4vzr1VSBtGLfwdf/v3553/8d/j139MySPxfHTcyGwKSJP77DzsK3KT8er0FQT7BJ+aJ++X5I//lo4A+0k/kE/PlI9t+BE/Ur2aUnc0vX8EXX9G/5vaXT5kvH7/+GPflI99+pJ7Adz9IvXhR6sWLUg==",
                "format": "base64"
              },
              "body_is_truncated": true,
              "code": 200,
              "headers_list": [
                [
                  "Expires",
                  "Mon, 27 Jan 2020 21:00:00 GMT"
                ],
                [
                  "Vary",
                  "X-Or-Diff-From-Consensus"
                ],
                [
                  "Date",
                  "Mon, 27 Jan 2020 20:01:04 GMT"
                ],
                [
                  "Content-Type",
                  "text/plain"
                ],
                [
                  "X-Your-Address-Is",
                  "[REDACTED]"
                ],
                [
                  "Content-Encoding",
                  "deflate"
                ]
              ],
              "headers": {
                "Content-Encoding": "deflate",
                "Content-Type": "text/plain",
                "Date": "Mon, 27 Jan 2020 20:01:04 GMT",
                "Expires": "Mon, 27 Jan 2020 21:00:00 GMT",
                "Vary": "X-Or-Diff-From-Consensus",
                "X-Your-Address-Is": "[REDACTED]"
              }
            },
            "transaction_id": 9
          }
        ],
        "target_address": "199.58.81.140:80",
        "target_name": "longclaw",
        "target_protocol": "dir_port",
        "tcp_connect": [
          {
            "conn_id": 29,
            "dial_id": 29,
            "ip": "199.58.81.140",
            "port": 80,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 4.605662,
            "transaction_id": 9
          }
        ],
        "tls_handshakes": null
      },
      "204.13.164.118:443": {
        "agent": "redirect",
        "failure": null,
        "network_events": [
          {
            "address": "204.13.164.118:443",
            "conn_id": 5,
            "dial_id": 5,
            "failure": null,
            "operation": "connect",
            "proto": "tcp",
            "t": 1.848193
          },
          {
            "conn_id": 5,
            "failure": null,
            "num_bytes": 243,
            "operation": "write",
            "proto": "tcp",
            "t": 1.848636
          },
          {
            "conn_id": 5,
            "failure": null,
            "num_bytes": 517,
            "operation": "read",
            "proto": "tcp",
            "t": 2.037487
          },
          {
            "conn_id": 5,
            "failure": null,
            "num_bytes": 488,
            "operation": "read",
            "proto": "tcp",
            "t": 2.037672
          },
          {
            "conn_id": 5,
            "failure": null,
            "num_bytes": 126,
            "operation": "write",
            "proto": "tcp",
            "t": 2.038658
          },
          {
            "conn_id": 5,
            "failure": null,
            "num_bytes": 51,
            "operation": "read",
            "proto": "tcp",
            "t": 2.22612
          },
          {
            "conn_id": 5,
            "failure": null,
            "num_bytes": 31,
            "operation": "write",
            "proto": "tcp",
            "t": 2.226325
          }
        ],
        "queries": null,
        "requests": null,
        "target_address": "204.13.164.118:443",
        "target_name": "bastet",
        "target_protocol": "or_port_dirauth",
        "tcp_connect": [
          {
            "conn_id": 5,
            "dial_id": 5,
            "ip": "204.13.164.118",
            "port": 443,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 1.848193
          }
        ],
        "tls_handshakes": [
          {
            "cipher_suite": "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384",
            "conn_id": 5,
            "failure": null,
            "negotiated_protocol": "",
            "peer_certificates": [
              {
                "data": "MIICQTCCAaqgAwIBAgIIYScWY8hMAdYwDQYJKoZIhvcNAQELBQAwIDEeMBwGA1UEAwwVd3d3LndsM3k2d3h5Z3FiYWsuY29tMB4XDTE5MTAwOTAwMDAwMFoXDTIwMDgyNjAwMDAwMFowIjEgMB4GA1UEAwwXd3d3LnhhbGFub2lubGJheG1lZS5uZXQwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDis1ZeGaj7dRCjG5ZCbXBOGvD0N3V/Pb2fBezmeyH3GTj3l3lmIkgCicQnKHmQBbwpuNCoyw7IqAhjbTYo3dbfcM70sHYVp+1Of90SVgFZM1n4gQ/RV5Kud5Zt2oJw7EotcBJj3egVXI8wgiDk4TngSt4eBMuWxQwL4MqxbdKRBo+4iZOtZgQvKrYX7uUpdk9Ns+lpFde60UT/OOo59K2562zn72QRKN7haB3IaZ435O6WIdhqOxTXXOCfgI9c769DpmMn9fLUADGXElhm1d2vo6mAl78kSrfh183jfHScqDEfIQIlbO/DsMGDzHxA6tftZ5ZFeOWrXBrAwSm0Xa7jAgMBAAEwDQYJKoZIhvcNAQELBQADgYEAZM6xesPp2JDrRYpsUGDyTtZf3sLzp/U3UGFR4YTmgBbIlrTGi0WVryF/c3SvSbm3+op9wempI9six6AG7gqBiZiEEjpnSwCEwtVLeYG1scpmSieO7dTfvnwraWujQZ/jZFqbv1ZlPDUgbQ82tABsNhwWyj7eupirItcVWj88MlQ=",
                "format": "base64"
              }
            ],
            "t": 2.226213,
            "tls_version": "TLSv1.2"
          }
        ]
      },
      "204.13.164.118:80": {
        "agent": "redirect",
        "failure": null,
        "network_events": null,
        "queries": null,
        "requests": [
          {
            "failure": null,
            "request": {
              "body": "",
              "body_is_truncated": false,
              "headers_list": [
                [
                  "Host",
                  "204.13.164.118:80"
                ],
                [
                  "User-Agent",
                  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
                ],
                [
                  "Accept",
                  "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
                ],
                [
                  "Accept-Language",
                  "en-US;q=0.8,en;q=0.5"
                ]
              ],
              "headers": {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-US;q=0.8,en;q=0.5",
                "Host": "204.13.164.118:80",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
              },
              "method": "GET",
              "tor": {
                "exit_ip": null,
                "exit_name": null,
                "is_tor": false
              },
              "url": "http://204.13.164.118:80/tor/status-vote/current/consensus.z"
            },
            "response": {
              "body": {
                "data": "eNrs/Wlz40a2NYx+71+Bj/cGbRGJxMh4+o0HE0mQBOcJvHHiBGaCGImBIPjrbyZUVS6hJLvt6nMs6W27ipJYEgVsZuae1l4rccs6zcNfi9Isq+LXm5sXQZoQ8B+3tHS/PEvYaVK4SVEV//j22a+xW55Th6CEf9zMKHB+Nb3SzQmKpMhfSfArxaFPByT+8w8vd4vzr1VSBtGLfwdf/v3553/8d/j139MySPxfHTcyGwKSJP77DzsK3KT8er0FQT7BJ+aJ++X5I//lo4A+0k/kE/PlI9t+BE/Ur2aUnc0vX8EXX9G/5vaXT5kvH7/+GPflI99+pJ7Adz9IvXhR6sWLUg==",
                "format": "base64"
              },
              "body_is_truncated": true,
              "code": 200,
              "headers_list": [
                [
                  "X-Your-Address-Is",
                  "[REDACTED]"
                ],
                [
                  "Content-Encoding",
                  "deflate"
                ],
                [
                  "Expires",
                  "Mon, 27 Jan 2020 21:00:00 GMT"
                ],
                [
                  "Vary",
                  "X-Or-Diff-From-Consensus"
                ],
                [
                  "Date",
                  "Mon, 27 Jan 2020 20:01:02 GMT"
                ],
                [
                  "Content-Type",
                  "text/plain"
                ]
              ],
              "headers": {
                "Content-Encoding": "deflate",
                "Content-Type": "text/plain",
                "Date": "Mon, 27 Jan 2020 20:01:02 GMT",
                "Expires": "Mon, 27 Jan 2020 21:00:00 GMT",
                "Vary": "X-Or-Diff-From-Consensus",
                "X-Your-Address-Is": "[REDACTED]"
              }
            },
            "transaction_id": 10
          }
        ],
        "target_address": "204.13.164.118:80",
        "target_name": "bastet",
        "target_protocol": "dir_port",
        "tcp_connect": [
          {
            "conn_id": 30,
            "dial_id": 30,
            "ip": "204.13.164.118",
            "port": 80,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 5.302902,
            "transaction_id": 10
          }
        ],
        "tls_handshakes": null
      },
      "31c395c157c08fd126dd6efb3baf33afd46b9605275bb92aedb1d0730fd152b8": {
        "agent": "redirect",
        "failure": null,
        "network_events": [
          {
            "address": "193.11.166.194:27020",
            "conn_id": 27,
            "dial_id": 27,
            "failure": null,
            "operation": "connect",
            "proto": "tcp",
            "t": 4.423417
          },
          {
            "conn_id": 27,
            "failure": null,
            "num_bytes": 2945,
            "operation": "write",
            "proto": "tcp",
            "t": 4.423984
          },
          {
            "conn_id": 27,
            "failure": null,
            "num_bytes": 1452,
            "operation": "read",
            "proto": "tcp",
            "t": 4.479167
          },
          {
            "conn_id": 27,
            "failure": null,
            "num_bytes": 1452,
            "operation": "read",
            "proto": "tcp",
            "t": 4.479415
          },
          {
            "conn_id": 27,
            "failure": null,
            "num_bytes": 1452,
            "operation": "read",
            "proto": "tcp",
            "t": 4.480102
          },
          {
            "conn_id": 27,
            "failure": null,
            "num_bytes": 1452,
            "operation": "read",
            "proto": "tcp",
            "t": 4.48061
          },
          {
            "conn_id": 27,
            "failure": null,
            "num_bytes": 1452,
            "operation": "read",
            "proto": "tcp",
            "t": 4.480978
          },
          {
            "conn_id": 27,
            "failure": null,
            "num_bytes": 167,
            "operation": "read",
            "proto": "tcp",
            "t": 4.4817409999999995
          }
        ],
        "queries": null,
        "requests": null,
        "target_address": "193.11.166.194:27020",
        "target_protocol": "obfs4",
        "tcp_connect": [
          {
            "conn_id": 27,
            "dial_id": 27,
            "ip": "193.11.166.194",
            "port": 27020,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 4.423417
          }
        ],
        "tls_handshakes": null
      },
      "3c3ec420923b5a3484607bc57d3e6fb8ca640c1e5ce0932cc6d2fa64fc2386e4": {
        "agent": "redirect",
        "failure": null,
        "network_events": [
          {
            "address": "37.218.245.14:38224",
            "conn_id": 9,
            "dial_id": 10,
            "failure": null,
            "operation": "connect",
            "proto": "tcp",
            "t": 2.35927
          },
          {
            "conn_id": 9,
            "failure": null,
            "num_bytes": 4776,
            "operation": "write",
            "proto": "tcp",
            "t": 2.360014
          },
          {
            "conn_id": 9,
            "failure": null,
            "num_bytes": 1440,
            "operation": "read",
            "proto": "tcp",
            "t": 2.436319
          },
          {
            "conn_id": 9,
            "failure": null,
            "num_bytes": 905,
            "operation": "read",
            "proto": "tcp",
            "t": 2.436517
          }
        ],
        "queries": null,
        "requests": null,
        "target_address": "37.218.245.14:38224",
        "target_protocol": "obfs4",
        "tcp_connect": [
          {
            "conn_id": 9,
            "dial_id": 10,
            "ip": "37.218.245.14",
            "port": 38224,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 2.35927
          }
        ],
        "tls_handshakes": null
      },
      "45.66.33.45:443": {
        "agent": "redirect",
        "failure": null,
        "network_events": [
          {
            "address": "45.66.33.45:443",
            "conn_id": 1,
            "dial_id": 2,
            "failure": null,
            "operation": "connect",
            "proto": "tcp",
            "t": 1.489957
          },
          {
            "conn_id": 1,
            "failure": null,
            "num_bytes": 243,
            "operation": "write",
            "proto": "tcp",
            "t": 1.490342
          },
          {
            "conn_id": 1,
            "failure": null,
            "num_bytes": 99,
            "operation": "read",
            "proto": "tcp",
            "t": 1.528371
          },
          {
            "conn_id": 1,
            "failure": null,
            "num_bytes": 6,
            "operation": "write",
            "proto": "tcp",
            "t": 1.528513
          },
          {
            "conn_id": 1,
            "failure": null,
            "num_bytes": 276,
            "operation": "write",
            "proto": "tcp",
            "t": 1.52869
          },
          {
            "conn_id": 1,
            "failure": null,
            "num_bytes": 517,
            "operation": "read",
            "proto": "tcp",
            "t": 1.568197
          },
          {
            "conn_id": 1,
            "failure": null,
            "num_bytes": 636,
            "operation": "read",
            "proto": "tcp",
            "t": 1.568769
          },
          {
            "conn_id": 1,
            "failure": null,
            "num_bytes": 74,
            "operation": "write",
            "proto": "tcp",
            "t": 1.5696080000000001
          },
          {
            "conn_id": 1,
            "failure": null,
            "num_bytes": 24,
            "operation": "write",
            "proto": "tcp",
            "t": 1.5697670000000001
          }
        ],
        "queries": null,
        "requests": null,
        "target_address": "45.66.33.45:443",
        "target_name": "dizum",
        "target_protocol": "or_port_dirauth",
        "tcp_connect": [
          {
            "conn_id": 1,
            "dial_id": 2,
            "ip": "45.66.33.45",
            "port": 443,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 1.489957
          }
        ],
        "tls_handshakes": [
          {
            "cipher_suite": "TLS_AES_256_GCM_SHA384",
            "conn_id": 1,
            "failure": null,
            "negotiated_protocol": "",
            "peer_certificates": [
              {
                "data": "MIICNjCCAZ+gAwIBAgIJAM0HnHC9RDKDMA0GCSqGSIb3DQEBCwUAMBsxGTAXBgNVBAMMEHd3dy40cHpmbG9qNi5jb20wHhcNMTkxMjA1MDAwMDAwWhcNMjAwMzMwMDAwMDAwWjAbMRkwFwYDVQQDDBB3d3cuNG5xdGdhbDMubmV0MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxDxjkml8OEfOVUTdrLollDDcSFY8VURzqDAGlgZ8g4cP6N3JHgiy5qQj6egWlIMq7vH19Y5xiIo/KFrQ4mhxYwpX11xOeTSGQd82GRPcCunCnHELwgomzfg4Pwoo4BL+KlpRlBeGpqIe2RMzBTGWlMoG7Z2hapmfLZNJhsbyiwiQFlbSH/jiz/BDhhycAdE88q6dd+o6iuTgXamd9yYTTNIJ0vwkG7gcvhEH5LMlFd1cw266+Ldhcwulv/NexRl7qw9iMxqV8UrmDiZQLNn+co4nYDpJseXsDXdfCMQ9D3CaPoipW+bPPCcaXL+g5DfL7x6FfnRksDHuB5aoDNz/OQIDAQABMA0GCSqGSIb3DQEBCwUAA4GBAKecGTeKazLAUnsUqZTRUzx+CgE4sptI8wxMRc1wXtSRm2IwJW+GvWueVGDe3ZyHcwm1nozcK8ykytuYZAxwHkC9eTI/GneiMEePx5WjHZJCXjHvcOllKf7ZNbsKEWZmmwqXKrYVZQyk5mHFaN0Pz00UkuA/iURVQoeBWbGNWODm",
                "format": "base64"
              }
            ],
            "t": 1.5696560000000002,
            "tls_version": "TLSv1.3"
          }
        ]
      },
      "45.66.33.45:80": {
        "agent": "redirect",
        "failure": null,
        "network_events": null,
        "queries": null,
        "requests": [
          {
            "failure": null,
            "request": {
              "body": "",
              "body_is_truncated": false,
              "headers_list": [
                [
                  "Accept",
                  "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
                ],
                [
                  "Accept-Language",
                  "en-US;q=0.8,en;q=0.5"
                ],
                [
                  "Host",
                  "45.66.33.45:80"
                ],
                [
                  "User-Agent",
                  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
                ]
              ],
              "headers": {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-US;q=0.8,en;q=0.5",
                "Host": "45.66.33.45:80",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
              },
              "method": "GET",
              "tor": {
                "exit_ip": null,
                "exit_name": null,
                "is_tor": false
              },
              "url": "http://45.66.33.45:80/tor/status-vote/current/consensus.z"
            },
            "response": {
              "body": {
                "data": "eNrs/Wlz40a2NYx+71+Bj/cGbRGJxMh4+o0HE0mQBOcJvHHiBGaCGImBIPjrbyZUVS6hJLvt6nMs6W27ipJYEgVsZuae1l4rccs6zcNfi9Isq+LXm5sXQZoQ8B+3tHS/PEvYaVK4SVEV//j22a+xW55Th6CEf9zMKHB+Nb3SzQmKpMhfSfArxaFPByT+8w8vd4vzr1VSBtGLfwdf/v3553/8d/j139MySPxfHTcyGwKSJP77DzsK3KT8er0FQT7BJ+aJ++X5I//lo4A+0k/kE/PlI9t+BE/Ur2aUnc0vX8EXX9G/5vaXT5kvH7/+GPflI99+pJ7Adz9IvXhR6sWLUg==",
                "format": "base64"
              },
              "body_is_truncated": true,
              "code": 200,
              "headers_list": [
                [
                  "Content-Encoding",
                  "deflate"
                ],
                [
                  "Expires",
                  "Mon, 27 Jan 2020 21:00:00 GMT"
                ],
                [
                  "Vary",
                  "X-Or-Diff-From-Consensus"
                ],
                [
                  "Date",
                  "Mon, 27 Jan 2020 20:01:01 GMT"
                ],
                [
                  "Content-Type",
                  "text/plain"
                ],
                [
                  "X-Your-Address-Is",
                  "[REDACTED]"
                ]
              ],
              "headers": {
                "Content-Encoding": "deflate",
                "Content-Type": "text/plain",
                "Date": "Mon, 27 Jan 2020 20:01:01 GMT",
                "Expires": "Mon, 27 Jan 2020 21:00:00 GMT",
                "Vary": "X-Or-Diff-From-Consensus",
                "X-Your-Address-Is": "[REDACTED]"
              }
            },
            "transaction_id": 7
          }
        ],
        "target_address": "45.66.33.45:80",
        "target_name": "dizum",
        "target_protocol": "dir_port",
        "tcp_connect": [
          {
            "conn_id": 23,
            "dial_id": 23,
            "ip": "45.66.33.45",
            "port": 80,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 4.093546,
            "transaction_id": 7
          }
        ],
        "tls_handshakes": null
      },
      "5454b05179ddc155c50d7d5ea0e199f352a19433e9e29629f9a998e848c042f5": {
        "agent": "redirect",
        "failure": null,
        "network_events": [
          {
            "address": "38.229.33.83:80",
            "conn_id": 10,
            "dial_id": 9,
            "failure": null,
            "operation": "connect",
            "proto": "tcp",
            "t": 2.437348
          },
          {
            "conn_id": 10,
            "failure": null,
            "num_bytes": 4537,
            "operation": "write",
            "proto": "tcp",
            "t": 2.438725
          },
          {
            "conn_id": 10,
            "failure": null,
            "num_bytes": 3894,
            "operation": "read",
            "proto": "tcp",
            "t": 2.69795
          },
          {
            "conn_id": 10,
            "failure": null,
            "num_bytes": 1298,
            "operation": "read",
            "proto": "tcp",
            "t": 2.6982239999999997
          },
          {
            "conn_id": 10,
            "failure": null,
            "num_bytes": 2741,
            "operation": "read",
            "proto": "tcp",
            "t": 2.698918
          }
        ],
        "queries": null,
        "requests": null,
        "target_address": "38.229.33.83:80",
        "target_protocol": "obfs4",
        "tcp_connect": [
          {
            "conn_id": 10,
            "dial_id": 9,
            "ip": "38.229.33.83",
            "port": 80,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 2.437348
          }
        ],
        "tls_handshakes": null
      },
      "66.111.2.131:9001": {
        "agent": "redirect",
        "failure": null,
        "network_events": [
          {
            "address": "66.111.2.131:9001",
            "conn_id": 18,
            "dial_id": 18,
            "failure": null,
            "operation": "connect",
            "proto": "tcp",
            "t": 3.356828
          },
          {
            "conn_id": 18,
            "failure": null,
            "num_bytes": 243,
            "operation": "write",
            "proto": "tcp",
            "t": 3.3572319999999998
          },
          {
            "conn_id": 18,
            "failure": null,
            "num_bytes": 517,
            "operation": "read",
            "proto": "tcp",
            "t": 3.481436
          },
          {
            "conn_id": 18,
            "failure": null,
            "num_bytes": 481,
            "operation": "read",
            "proto": "tcp",
            "t": 3.48151
          },
          {
            "conn_id": 18,
            "failure": null,
            "num_bytes": 126,
            "operation": "write",
            "proto": "tcp",
            "t": 3.482525
          },
          {
            "conn_id": 18,
            "failure": null,
            "num_bytes": 51,
            "operation": "read",
            "proto": "tcp",
            "t": 3.59735
          },
          {
            "conn_id": 18,
            "failure": null,
            "num_bytes": 31,
            "operation": "write",
            "proto": "tcp",
            "t": 3.597581
          }
        ],
        "queries": null,
        "requests": null,
        "target_address": "66.111.2.131:9001",
        "target_name": "Serge",
        "target_protocol": "or_port_dirauth",
        "tcp_connect": [
          {
            "conn_id": 18,
            "dial_id": 18,
            "ip": "66.111.2.131",
            "port": 9001,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 3.356828
          }
        ],
        "tls_handshakes": [
          {
            "cipher_suite": "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384",
            "conn_id": 18,
            "failure": null,
            "negotiated_protocol": "",
            "peer_certificates": [
              {
                "data": "MIICPDCCAaWgAwIBAgIJALiPYOvsyb8kMA0GCSqGSIb3DQEBCwUAMB4xHDAaBgNVBAMME3d3dy43NGVkMzZra3d1NS5jb20wHhcNMTkxMjAxMDAwMDAwWhcNMjAwMzE3MDAwMDAwWjAeMRwwGgYDVQQDDBN3d3cudDJqNnM2MjNhYWIubmV0MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAygzwm73Gfz9UOALGiNMXc3q6kiBJ44c4nIUa8PjGSRhantW2gtZXWDvwZn20Gxma4QAMHvzF0szHeC7do9/FdSw8UFEG6tD1CGzSjCBvMfHPBi22z2YG4bFu1Ziomm0sVb/v3cgdS0pTbhUsmsJrxWdDfPE5ppfhmL9q3MjYGni+tLcCD72ZgSXsBeLKjjUcQUEKqDUy12fRToD9BW9tYXkJc6DUYDweUPMXhM7/DiYVe9l/uZ9+hCVnl3QgKRp+0vyA4zbD7RcNv/9rLDUoT86a7HLnliBGlqekzQ+fup0he/WF6+zVQIVHPX7ZWlo1n0K/9J+KnrBtDb+494K1WQIDAQABMA0GCSqGSIb3DQEBCwUAA4GBAL9upL3j0H7lRNyZV5tWK92jnQnrcrgvmNsYja5OS1FxqTTots/XjHhEYXayG0FVxpnMFn25/gXE/kqNeF6/T1Q/J1iq3F6j33c05PSCUhfYiHMzzEmFWR20YDmMfzDMCm56KtLlIMSuqByy3tsEih7SRuRLtSzs8LFih5s/Kvpb",
                "format": "base64"
              }
            ],
            "t": 3.597424,
            "tls_version": "TLSv1.2"
          }
        ]
      },
      "66.111.2.131:9030": {
        "agent": "redirect",
        "failure": null,
        "network_events": null,
        "queries": null,
        "requests": [
          {
            "failure": null,
            "request": {
              "body": "",
              "body_is_truncated": false,
              "headers_list": [
                [
                  "Host",
                  "66.111.2.131:9030"
                ],
                [
                  "User-Agent",
                  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
                ],
                [
                  "Accept",
                  "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
                ],
                [
                  "Accept-Language",
                  "en-US;q=0.8,en;q=0.5"
                ]
              ],
              "headers": {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-US;q=0.8,en;q=0.5",
                "Host": "66.111.2.131:9030",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
              },
              "method": "GET",
              "tor": {
                "exit_ip": null,
                "exit_name": null,
                "is_tor": false
              },
              "url": "http://66.111.2.131:9030/tor/status-vote/current/consensus.z"
            },
            "response": {
              "body": {
                "data": "eNrs/Wlz40a2NYx+71+Bj/cGbRHIxMh4+o0HE0mQBOcJvHHiBGaCGImBIPjrbyZUVS6hJLvt8jkt6W27ipJYEgVsZuae1l4rccs6zcNfi9Isq+LXm5sXQZoQ8B+3tHS/PEvYaVK4SVEV//j22a+xW55ThwDCP25mFDi/ml7p5gQgAfkrSf0KOIISBiSJ/vzDy93i/GuVlEH0/b8D8su/P//8j/8Ovv57WgaJ/6vjRmZDQJLEf/9hR4GblF+vtyDIJ/jEPHG/PH/kv3wU0Ef6iXxivnxk24/UE/jVjLKz+eUr+OIr+tfc/vIp8+Xj1x/jvnzk24/gifruB8GLFwUvXg==",
                "format": "base64"
              },
              "body_is_truncated": true,
              "code": 200,
              "headers_list": [
                [
                  "Content-Type",
                  "text/plain"
                ],
                [
                  "X-Your-Address-Is",
                  "[REDACTED]"
                ],
                [
                  "Content-Encoding",
                  "deflate"
                ],
                [
                  "Pragma",
                  "no-cache"
                ],
                [
                  "Vary",
                  "X-Or-Diff-From-Consensus"
                ],
                [
                  "Cache-Control",
                  "no-cache"
                ],
                [
                  "Date",
                  "Mon, 27 Jan 2020 20:00:59 GMT"
                ]
              ],
              "headers": {
                "Cache-Control": "no-cache",
                "Content-Encoding": "deflate",
                "Content-Type": "text/plain",
                "Date": "Mon, 27 Jan 2020 20:00:59 GMT",
                "Pragma": "no-cache",
                "Vary": "X-Or-Diff-From-Consensus",
                "X-Your-Address-Is": "[REDACTED]"
              }
            },
            "transaction_id": 5
          }
        ],
        "target_address": "66.111.2.131:9030",
        "target_name": "Serge",
        "target_protocol": "dir_port",
        "tcp_connect": [
          {
            "conn_id": 12,
            "dial_id": 12,
            "ip": "66.111.2.131",
            "port": 9030,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 2.668727,
            "transaction_id": 5
          }
        ],
        "tls_handshakes": null
      },
      "6d226d9b5c819ca708eca23780c615361957b4a0a4addeb93c785b1fd4b548a6": {
        "agent": "redirect",
        "failure": null,
        "network_events": [
          {
            "address": "85.31.186.98:443",
            "conn_id": 32,
            "dial_id": 32,
            "failure": null,
            "operation": "connect",
            "proto": "tcp",
            "t": 6.009658
          },
          {
            "conn_id": 32,
            "failure": null,
            "num_bytes": 3560,
            "operation": "write",
            "proto": "tcp",
            "t": 6.010464
          },
          {
            "conn_id": 32,
            "failure": null,
            "num_bytes": 5814,
            "operation": "read",
            "proto": "tcp",
            "t": 6.064045
          }
        ],
        "queries": null,
        "requests": null,
        "target_address": "85.31.186.98:443",
        "target_protocol": "obfs4",
        "tcp_connect": [
          {
            "conn_id": 32,
            "dial_id": 32,
            "ip": "85.31.186.98",
            "port": 443,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 6.009658
          }
        ],
        "tls_handshakes": null
      },
      "748c1d8b0c70d243e626823f9b62905c2eaab8e342b80325e839bf1e1f703968": {
        "agent": "redirect",
        "failure": null,
        "network_events": [
          {
            "address": "38.229.1.78:80",
            "conn_id": 31,
            "dial_id": 31,
            "failure": null,
            "operation": "connect",
            "proto": "tcp",
            "t": 5.645914
          },
          {
            "conn_id": 31,
            "failure": null,
            "num_bytes": 4625,
            "operation": "write",
            "proto": "tcp",
            "t": 5.64673
          },
          {
            "conn_id": 31,
            "failure": null,
            "num_bytes": 406,
            "operation": "read",
            "proto": "tcp",
            "t": 5.95533
          }
        ],
        "queries": null,
        "requests": null,
        "target_address": "38.229.1.78:80",
        "target_protocol": "obfs4",
        "tcp_connect": [
          {
            "conn_id": 31,
            "dial_id": 31,
            "ip": "38.229.1.78",
            "port": 80,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 5.645914
          }
        ],
        "tls_handshakes": null
      },
      "86.59.21.38:443": {
        "agent": "redirect",
        "failure": null,
        "network_events": [
          {
            "address": "86.59.21.38:443",
            "conn_id": 15,
            "dial_id": 15,
            "failure": null,
            "operation": "connect",
            "proto": "tcp",
            "t": 2.8625730000000003
          },
          {
            "conn_id": 15,
            "failure": null,
            "num_bytes": 243,
            "operation": "write",
            "proto": "tcp",
            "t": 2.862802
          },
          {
            "conn_id": 15,
            "failure": null,
            "num_bytes": 99,
            "operation": "read",
            "proto": "tcp",
            "t": 2.911082
          },
          {
            "conn_id": 15,
            "failure": null,
            "num_bytes": 6,
            "operation": "write",
            "proto": "tcp",
            "t": 2.9111789999999997
          },
          {
            "conn_id": 15,
            "failure": null,
            "num_bytes": 276,
            "operation": "write",
            "proto": "tcp",
            "t": 2.9114269999999998
          },
          {
            "conn_id": 15,
            "failure": null,
            "num_bytes": 517,
            "operation": "read",
            "proto": "tcp",
            "t": 2.962361
          },
          {
            "conn_id": 15,
            "failure": null,
            "num_bytes": 655,
            "operation": "read",
            "proto": "tcp",
            "t": 2.96277
          },
          {
            "conn_id": 15,
            "failure": null,
            "num_bytes": 74,
            "operation": "write",
            "proto": "tcp",
            "t": 2.9632680000000002
          },
          {
            "conn_id": 15,
            "failure": null,
            "num_bytes": 24,
            "operation": "write",
            "proto": "tcp",
            "t": 2.963367
          }
        ],
        "queries": null,
        "requests": null,
        "target_address": "86.59.21.38:443",
        "target_name": "tor26",
        "target_protocol": "or_port_dirauth",
        "tcp_connect": [
          {
            "conn_id": 15,
            "dial_id": 15,
            "ip": "86.59.21.38",
            "port": 443,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 2.8625730000000003
          }
        ],
        "tls_handshakes": [
          {
            "cipher_suite": "TLS_AES_256_GCM_SHA384",
            "conn_id": 15,
            "failure": null,
            "negotiated_protocol": "",
            "peer_certificates": [
              {
                "data": "MIICSTCCAbKgAwIBAgIJANa1MuaZG3YyMA0GCSqGSIb3DQEBCwUAMCcxJTAjBgNVBAMMHHd3dy5teXl0bjZ6cmVrdjRybmFva3J6dS5jb20wHhcNMTkxMTIwMDAwMDAwWhcNMjAwNDIxMDAwMDAwWjAiMSAwHgYDVQQDDBd3d3cuaXVuYW1nYXFrZnlvcWw1Lm5ldDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAK8Kl6vfP7QR9cMjV4sUCGus783teZuSkEKSsjGAjiEmilH0jBkTTrosbvHySSPI4lAbdQuEEGRaWqNS5z+XoLmp43C+GxrE59EJpRb4skPmmzGL5WGYPjSQJpv/Ph0g5fhpXaax9Tr82/3DOJrgFiVErfv4noVOnYtlh63AKoWNa2M5kyzIcmEpNsqaYnD+ePJGjSyoUWLXIPT7kXY3XAg+gvAEoOE/YlOuZYVhec9v0VYYQC1pBBBGfbDmH7Yw6ZMY22Vjb7EFVFW+H+Ho3/kFh7LIabkhyla7Yj3DfdW/4ALPEg9tMABj4ZFWdVjjOAbLCqM55q2VSAtvK2aZrOkCAwEAATANBgkqhkiG9w0BAQsFAAOBgQABj6XIGkXe5YWDjuVQqPhEQsY8RM6IFSOBODbhNlHIAfQ6iS7PCf20Hfx1tIviGdrOprjsVzTSNpe2c3MX5McfHMpxFPCpuwQI+65D+zagT5HovluSd1+0faZEe3V1f5UmHKs/VxRzOxs37vjnDhhNsFuU64xOGbHKlLKgGdFCqA==",
                "format": "base64"
              }
            ],
            "t": 2.963306,
            "tls_version": "TLSv1.3"
          }
        ]
      },
      "86.59.21.38:80": {
        "agent": "redirect",
        "failure": null,
        "network_events": null,
        "queries": null,
        "requests": [
          {
            "failure": null,
            "request": {
              "body": "",
              "body_is_truncated": false,
              "headers_list": [
                [
                  "Host",
                  "86.59.21.38:80"
                ],
                [
                  "User-Agent",
                  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
                ],
                [
                  "Accept",
                  "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
                ],
                [
                  "Accept-Language",
                  "en-US;q=0.8,en;q=0.5"
                ]
              ],
              "headers": {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-US;q=0.8,en;q=0.5",
                "Host": "86.59.21.38:80",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
              },
              "method": "GET",
              "tor": {
                "exit_ip": null,
                "exit_name": null,
                "is_tor": false
              },
              "url": "http://86.59.21.38:80/tor/status-vote/current/consensus.z"
            },
            "response": {
              "body": {
                "data": "eNrs/Wlz40a2NYx+71+Bj/cGbRGJxMh4+o0HE0mQBOcJvHHiBGaCGImBIPjrbyZUVS6hJLvt6nMs6W27ipJYEgVsZuae1l4rccs6zcNfi9Isq+LXm5sXQZoQ8B+3tHS/PEvYaVK4SVEV//j22a+xW55Th6CEf9zMKHB+Nb3SzQmKpMhfSfArxaFPByT+8w8vd4vzr1VSBtGLfwdf/v3553/8d/j139MySPxfHTcyGwKSJP77DzsK3KT8er0FQT7BJ+aJ++X5I//lo4A+0k/kE/PlI9t+BE/Ur2aUnc0vX8EXX9G/5vaXT5kvH7/+GPflI99+pJ7Adz9IvXhR6sWLUg==",
                "format": "base64"
              },
              "body_is_truncated": true,
              "code": 200,
              "headers_list": [
                [
                  "Date",
                  "Mon, 27 Jan 2020 20:00:59 GMT"
                ],
                [
                  "Content-Type",
                  "text/plain"
                ],
                [
                  "X-Your-Address-Is",
                  "[REDACTED]"
                ],
                [
                  "Content-Encoding",
                  "deflate"
                ],
                [
                  "Expires",
                  "Mon, 27 Jan 2020 21:00:00 GMT"
                ],
                [
                  "Vary",
                  "X-Or-Diff-From-Consensus"
                ]
              ],
              "headers": {
                "Content-Encoding": "deflate",
                "Content-Type": "text/plain",
                "Date": "Mon, 27 Jan 2020 20:00:59 GMT",
                "Expires": "Mon, 27 Jan 2020 21:00:00 GMT",
                "Vary": "X-Or-Diff-From-Consensus",
                "X-Your-Address-Is": "[REDACTED]"
              }
            },
            "transaction_id": 6
          }
        ],
        "target_address": "86.59.21.38:80",
        "target_name": "tor26",
        "target_protocol": "dir_port",
        "tcp_connect": [
          {
            "conn_id": 14,
            "dial_id": 14,
            "ip": "86.59.21.38",
            "port": 80,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 2.837409,
            "transaction_id": 6
          }
        ],
        "tls_handshakes": null
      },
      "8a4df6d9e92da4b035ca0d5b56d14cc82719eca42536d06d04e5e05bb95ed1d7": {
        "agent": "redirect",
        "failure": null,
        "network_events": [
          {
            "address": "193.11.166.194:27025",
            "conn_id": 24,
            "dial_id": 25,
            "failure": null,
            "operation": "connect",
            "proto": "tcp",
            "t": 4.188453
          },
          {
            "conn_id": 24,
            "failure": null,
            "num_bytes": 5123,
            "operation": "write",
            "proto": "tcp",
            "t": 4.189198
          },
          {
            "conn_id": 24,
            "failure": null,
            "num_bytes": 940,
            "operation": "read",
            "proto": "tcp",
            "t": 4.30047
          }
        ],
        "queries": null,
        "requests": null,
        "target_address": "193.11.166.194:27025",
        "target_protocol": "obfs4",
        "tcp_connect": [
          {
            "conn_id": 24,
            "dial_id": 25,
            "ip": "193.11.166.194",
            "port": 27025,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 4.188453
          }
        ],
        "tls_handshakes": null
      },
      "8dcaab5e2b8a5fa9a73f3ff0f70aca8fb8b034836284336f29b1b594c56c607f": {
        "agent": "redirect",
        "failure": null,
        "network_events": [
          {
            "address": "146.57.248.225:22",
            "conn_id": 22,
            "dial_id": 22,
            "failure": null,
            "operation": "connect",
            "proto": "tcp",
            "t": 3.837669
          },
          {
            "conn_id": 22,
            "failure": null,
            "num_bytes": 6165,
            "operation": "write",
            "proto": "tcp",
            "t": 3.838522
          },
          {
            "conn_id": 22,
            "failure": null,
            "num_bytes": 1440,
            "operation": "read",
            "proto": "tcp",
            "t": 4.107005
          },
          {
            "conn_id": 22,
            "failure": null,
            "num_bytes": 1440,
            "operation": "read",
            "proto": "tcp",
            "t": 4.107198
          },
          {
            "conn_id": 22,
            "failure": null,
            "num_bytes": 740,
            "operation": "read",
            "proto": "tcp",
            "t": 4.107907
          }
        ],
        "queries": null,
        "requests": null,
        "target_address": "146.57.248.225:22",
        "target_protocol": "obfs4",
        "tcp_connect": [
          {
            "conn_id": 22,
            "dial_id": 22,
            "ip": "146.57.248.225",
            "port": 22,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 3.837669
          }
        ],
        "tls_handshakes": null
      },
      "a26e5ecab86eedc44b6f81e2e19482e63eb169e26da919e5a27bebc81807f078": {
        "agent": "redirect",
        "failure": null,
        "network_events": [
          {
            "address": "216.252.162.21:46089",
            "conn_id": 16,
            "dial_id": 16,
            "failure": null,
            "operation": "connect",
            "proto": "tcp",
            "t": 3.071783
          },
          {
            "conn_id": 16,
            "failure": null,
            "num_bytes": 782,
            "operation": "write",
            "proto": "tcp",
            "t": 3.072382
          },
          {
            "conn_id": 16,
            "failure": null,
            "num_bytes": 2880,
            "operation": "read",
            "proto": "tcp",
            "t": 3.246991
          },
          {
            "conn_id": 16,
            "failure": null,
            "num_bytes": 347,
            "operation": "read",
            "proto": "tcp",
            "t": 3.247432
          }
        ],
        "queries": null,
        "requests": null,
        "target_address": "216.252.162.21:46089",
        "target_protocol": "obfs4",
        "tcp_connect": [
          {
            "conn_id": 16,
            "dial_id": 16,
            "ip": "216.252.162.21",
            "port": 46089,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 3.071783
          }
        ],
        "tls_handshakes": null
      },
      "ac703097645b476bbc09a8c8a3e6de0cffd4e0d186cd048890ad09f4985c9e3d": {
        "agent": "redirect",
        "failure": null,
        "network_events": [
          {
            "address": "209.148.46.65:443",
            "conn_id": 33,
            "dial_id": 33,
            "failure": null,
            "operation": "connect",
            "proto": "tcp",
            "t": 6.183381
          },
          {
            "conn_id": 33,
            "failure": null,
            "num_bytes": 3303,
            "operation": "write",
            "proto": "tcp",
            "t": 6.18436
          },
          {
            "conn_id": 33,
            "failure": null,
            "num_bytes": 1370,
            "operation": "read",
            "proto": "tcp",
            "t": 6.303216
          }
        ],
        "queries": null,
        "requests": null,
        "target_address": "209.148.46.65:443",
        "target_protocol": "obfs4",
        "tcp_connect": [
          {
            "conn_id": 33,
            "dial_id": 33,
            "ip": "209.148.46.65",
            "port": 443,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 6.183381
          }
        ],
        "tls_handshakes": null
      },
      "d609809637788dbec8cfba23c79ba7b13c44353d66ae77fd6b32bce065093204": {
        "agent": "redirect",
        "failure": null,
        "network_events": [
          {
            "address": "85.31.186.26:443",
            "conn_id": 20,
            "dial_id": 20,
            "failure": null,
            "operation": "connect",
            "proto": "tcp",
            "t": 3.648323
          },
          {
            "conn_id": 20,
            "failure": null,
            "num_bytes": 2468,
            "operation": "write",
            "proto": "tcp",
            "t": 3.648991
          },
          {
            "conn_id": 20,
            "failure": null,
            "num_bytes": 2880,
            "operation": "read",
            "proto": "tcp",
            "t": 3.7008609999999997
          },
          {
            "conn_id": 20,
            "failure": null,
            "num_bytes": 1440,
            "operation": "read",
            "proto": "tcp",
            "t": 3.701178
          },
          {
            "conn_id": 20,
            "failure": null,
            "num_bytes": 1218,
            "operation": "read",
            "proto": "tcp",
            "t": 3.701531
          }
        ],
        "queries": null,
        "requests": null,
        "target_address": "85.31.186.26:443",
        "target_protocol": "obfs4",
        "tcp_connect": [
          {
            "conn_id": 20,
            "dial_id": 20,
            "ip": "85.31.186.26",
            "port": 443,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 3.648323
          }
        ],
        "tls_handshakes": null
      },
      "e908d2aee266d911ca877b08b76d6dbc3ec9ad0c173c63eee59f3041d5ad54d4": {
        "agent": "redirect",
        "failure": null,
        "network_events": [
          {
            "address": "192.95.36.142:443",
            "conn_id": 19,
            "dial_id": 19,
            "failure": null,
            "operation": "connect",
            "proto": "tcp",
            "t": 3.42609
          },
          {
            "conn_id": 19,
            "failure": null,
            "num_bytes": 7636,
            "operation": "write",
            "proto": "tcp",
            "t": 3.428295
          },
          {
            "conn_id": 19,
            "failure": null,
            "num_bytes": 1440,
            "operation": "read",
            "proto": "tcp",
            "t": 3.675839
          },
          {
            "conn_id": 19,
            "failure": null,
            "num_bytes": 2880,
            "operation": "read",
            "proto": "tcp",
            "t": 3.6762129999999997
          },
          {
            "conn_id": 19,
            "failure": null,
            "num_bytes": 1440,
            "operation": "read",
            "proto": "tcp",
            "t": 3.676483
          },
          {
            "conn_id": 19,
            "failure": null,
            "num_bytes": 234,
            "operation": "read",
            "proto": "tcp",
            "t": 3.676947
          }
        ],
        "queries": null,
        "requests": null,
        "target_address": "192.95.36.142:443",
        "target_protocol": "obfs4",
        "tcp_connect": [
          {
            "conn_id": 19,
            "dial_id": 19,
            "ip": "192.95.36.142",
            "port": 443,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 3.42609
          }
        ],
        "tls_handshakes": null
      },
      "fb50a5562be719a1f2f68b8859a0dd14393aa0ff41ee21b0bb38ba9e9956aa60": {
        "agent": "redirect",
        "failure": null,
        "network_events": [
          {
            "address": "144.217.20.138:80",
            "conn_id": 21,
            "dial_id": 21,
            "failure": null,
            "operation": "connect",
            "proto": "tcp",
            "t": 3.802276
          },
          {
            "conn_id": 21,
            "failure": null,
            "num_bytes": 7446,
            "operation": "write",
            "proto": "tcp",
            "t": 3.803009
          },
          {
            "conn_id": 21,
            "failure": null,
            "num_bytes": 1593,
            "operation": "read",
            "proto": "tcp",
            "t": 4.051927
          }
        ],
        "queries": null,
        "requests": null,
        "target_address": "144.217.20.138:80",
        "target_protocol": "obfs4",
        "tcp_connect": [
          {
            "conn_id": 21,
            "dial_id": 21,
            "ip": "144.217.20.138",
            "port": 80,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 3.802276
          }
        ],
        "tls_handshakes": null
      }
    }
  },
  "test_name": "tor",
  "test_start_time": "2020-01-27 20:00:56",
  "test_version": "0.1.0"
}
```

# Privacy considerations

This nettest does not provide anonymity. An adversary can observe that
the user is connecting to Tor servers and using obfs4.

A future version of this specification should describe how to handle the
case where the target bridges are not public. Until this functionality
has been specified, this experiment shall not be provided private targets.

# Packet capture considerations

This test does not capture packets by default.

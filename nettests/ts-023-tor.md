# Specification version number

2020-06-16-001

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
    "protocol": "",
    "source": ""
  }
}
```

- `id` (`string`): the unique identifier of the target, chosen by who generated
the input targets.  `id` is a SHA-256 hash over the concatenation of a
bridge's IP:port tuple and its fingerprint.  For example, the key of the
following bridge:

  ```
  1.2.3.4:1234 1234567890123456789012345678901234567890
  ```

  will be:

  ```
  hashlib.sha256(b'1.2.3.4:1234' + b'1234567890123456789012345678901234567890').hexdigest()
  '19bc59fa00d29729edea87368ceb062b9fad66759c0fcd6b7f8680ca14452fb8'
  ```

- `address` (`string`): the address of the target.

- `fingerprint` (`string`; optional): the fingerprint, if applicable.

- `name` (`string`; optional): the target name, if applicable.

- `params` (`map[string][]string`; optional): extra parameters,
e.g., to configure `obfs4`.

- `protocol` (`string`): the protocol to use with the
target (e.g. `obfs4`).

- `source` (`string`; optional): string indicating where this bridge
came from (e.g. `"bridgedb"`). When present and not empty, we say that
a specific bridge is _private_. For such bridges, the nettest
implementation MUST follow the scrubbing procedure described in the
privacy consideration section.

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
    "source": "",
    "summary": {},
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

- `summary` (`map[string]*string`): since 2020-01-30 this field contains
key-to-value string mappings instrumental to communicate the result of
the experiment to the user. The keys are the names of operations, e.g.,
`"connect"` for TCP connects. Likewise, `"handshake"` is used for TLS and
OBFS4 handshakes. The values are failures with the same `null` or string
semantics described also in `df-007-errors.md`.

- `target_address` (`string`): address of the target, generally expressed
in the `1.1.1.1:555` or the `[::1]:555` or the `domain:555` forms;

- `target_name` (`string`; optional): name of the target;

- `target_protocol` (`string`): protocol to access the target;

- `target_source` (`string`; optional): source of the target;

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
  "measurement_start_time": "2020-01-30 16:47:34",
  "test_runtime": 5.388864491,
  "probe_asn": "AS30722",
  "probe_cc": "IT",
  "probe_ip": "127.0.0.1",
  "report_id": "20200130T164734Z_AS30722_qZyUA04NmTSWTtS7x6yuTKjIa05wcf7ft7QKKNx9UV7YPNTwiX",
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
            "conn_id": 11,
            "dial_id": 10,
            "failure": null,
            "operation": "connect",
            "proto": "tcp",
            "t": 2.069283
          },
          {
            "conn_id": 11,
            "failure": null,
            "num_bytes": 6774,
            "operation": "write",
            "proto": "tcp",
            "t": 2.070624
          },
          {
            "conn_id": 11,
            "failure": null,
            "num_bytes": 1301,
            "operation": "read",
            "proto": "tcp",
            "t": 2.473517
          }
        ],
        "queries": null,
        "requests": null,
        "summary": {
          "connect": {
            "failure": null
          },
          "handshake": {
            "failure": null
          }
        },
        "target_address": "37.218.240.34:40035",
        "target_protocol": "obfs4",
        "tcp_connect": [
          {
            "conn_id": 11,
            "dial_id": 10,
            "ip": "37.218.240.34",
            "port": 40035,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 2.069283
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
            "conn_id": 10,
            "dial_id": 11,
            "failure": null,
            "operation": "connect",
            "proto": "tcp",
            "t": 2.040353
          },
          {
            "conn_id": 10,
            "failure": null,
            "num_bytes": 7320,
            "operation": "write",
            "proto": "tcp",
            "t": 2.041024
          },
          {
            "conn_id": 10,
            "failure": null,
            "num_bytes": 1452,
            "operation": "read",
            "proto": "tcp",
            "t": 2.151846
          },
          {
            "conn_id": 10,
            "failure": null,
            "num_bytes": 1452,
            "operation": "read",
            "proto": "tcp",
            "t": 2.152491
          },
          {
            "conn_id": 10,
            "failure": null,
            "num_bytes": 648,
            "operation": "read",
            "proto": "tcp",
            "t": 2.153175
          }
        ],
        "queries": null,
        "requests": null,
        "summary": {
          "connect": {
            "failure": null
          },
          "handshake": {
            "failure": null
          }
        },
        "target_address": "193.11.166.194:27015",
        "target_protocol": "obfs4",
        "tcp_connect": [
          {
            "conn_id": 10,
            "dial_id": 11,
            "ip": "193.11.166.194",
            "port": 27015,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 2.040353
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
            "conn_id": 6,
            "dial_id": 7,
            "failure": null,
            "operation": "connect",
            "proto": "tcp",
            "t": 1.520964
          },
          {
            "conn_id": 6,
            "failure": null,
            "num_bytes": 243,
            "operation": "write",
            "proto": "tcp",
            "t": 1.521277
          },
          {
            "conn_id": 6,
            "failure": null,
            "num_bytes": 517,
            "operation": "read",
            "proto": "tcp",
            "t": 1.6349399999999998
          },
          {
            "conn_id": 6,
            "failure": null,
            "num_bytes": 480,
            "operation": "read",
            "proto": "tcp",
            "t": 1.6350479999999998
          },
          {
            "conn_id": 6,
            "failure": null,
            "num_bytes": 126,
            "operation": "write",
            "proto": "tcp",
            "t": 1.6363180000000002
          },
          {
            "conn_id": 6,
            "failure": null,
            "num_bytes": 51,
            "operation": "read",
            "proto": "tcp",
            "t": 1.749946
          },
          {
            "conn_id": 6,
            "failure": null,
            "num_bytes": 31,
            "operation": "write",
            "proto": "tcp",
            "t": 1.750191
          }
        ],
        "queries": null,
        "requests": null,
        "summary": {
          "connect": {
            "failure": null
          },
          "handshake": {
            "failure": null
          }
        },
        "target_address": "128.31.0.39:9101",
        "target_name": "moria1",
        "target_protocol": "or_port_dirauth",
        "tcp_connect": [
          {
            "conn_id": 6,
            "dial_id": 7,
            "ip": "128.31.0.39",
            "port": 9101,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 1.520964
          }
        ],
        "tls_handshakes": [
          {
            "cipher_suite": "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384",
            "conn_id": 6,
            "failure": null,
            "negotiated_protocol": "",
            "peer_certificates": [
              {
                "data": "MIICOTCCAaKgAwIBAgIISGlEeLRsL6YwDQYJKoZIhvcNAQELBQAwHTEbMBkGA1UEAxMSd3d3LmtrbGg3ZXp4dGYuY29tMB4XDTE5MTIyMDAwMDAwMFoXDTIwMDQyOTIzNTk1OVowHTEbMBkGA1UEAxMSd3d3LnBrcWlndXoyNTQubmV0MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAyHKN6cIrskx3URTj21s+kt97rtUSzPC7QXnT/cLi2ihMUi9A/BgP+hXOY6PZnWoMZa4gvNFW9mMU1rRF3Q8f36cO8Zftcj8MhIxb6mIx3XezU/wMMv+9WWFyCmsdoh4t75F6s9YXIN+Qae76eGR48DPCXRd2KL89lY831PqXgQKfHOtgLTnr2qMeB6t3QSrYugX6+AlQ3UfbzcQUxPeCn3ZDefs0iDMytT6SvdA4ADeR/ghr4qOI9Myy/BNPiI0YYrc8JZOV/gcQSMnUSPbLwmpmvei97P6vLzP5EA9alAvOODgZt2UprmRGOc2pe+Wa49WhU/h9+cGBd26NuQuN0QIDAQABMA0GCSqGSIb3DQEBCwUAA4GBADs1ni19S+5994aZEZlKPCpoybUyCNKIYoZ2nw8OhlFo1JG0Z5jRAPKyhiJzU6wn2VGFC13V5q+QJp7kJpF+Za9f3XNrppcfWDmMwMqQVaeHe1viOte+8aK/YXcL7Wz/0wAzaGPXh4Cxo40FWMMYF9G5UhPMQa8YEFoYLZnXa1bW",
                "format": "base64"
              }
            ],
            "t": 1.750011,
            "tls_version": "TLSv1.2"
          }
        ]
      },
      "128.31.0.39:9131": {
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
                  "128.31.0.39:9131"
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
              "body": {
                "data": "eNrs/Vdz48i2LQq/r1+Bx/sFu0QgE5Zx1o0DS9CA3t/YsQOeICxhCJK//suEVNUlFNWu+uyWdFZ3FSWxJAqYzMzpxhwjccs6zcMvRWmWVfHl4uZFkCYE/NclLd2XZwk7TQo3KariX98++xK75TF1CCD862JGgfPF9Eo3JwAJyC8k9QWSBMX2SBL9+ZeXu8XxS5WUQfTq37mXf3/++R//Xfj672kZJP4Xx43MGwFJEv/9lx0FblJ+vd6CIJ/gE/PE/fL8kX/5KKCP9BP5xLx8ZJuP1BP4YkbZ0Xz5Cr76iv6S2y+fMi8fv/4Y9/KRbz6CJ+q7HwSvXhS8elHw64uClw==",
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
                  "Thu, 30 Jan 2020 17:00:00 GMT"
                ],
                [
                  "Vary",
                  "X-Or-Diff-From-Consensus"
                ],
                [
                  "Date",
                  "Thu, 30 Jan 2020 16:47:39 GMT"
                ],
                [
                  "Content-Type",
                  "text/plain"
                ]
              ],
              "headers": {
                "Content-Encoding": "deflate",
                "Content-Type": "text/plain",
                "Date": "Thu, 30 Jan 2020 16:47:39 GMT",
                "Expires": "Thu, 30 Jan 2020 17:00:00 GMT",
                "Vary": "X-Or-Diff-From-Consensus",
                "X-Your-Address-Is": "[REDACTED]"
              }
            },
            "transaction_id": 10
          }
        ],
        "summary": {
          "connect": {
            "failure": null
          }
        },
        "target_address": "128.31.0.39:9131",
        "target_name": "moria1",
        "target_protocol": "dir_port",
        "tcp_connect": [
          {
            "conn_id": 31,
            "dial_id": 31,
            "ip": "128.31.0.39",
            "port": 9131,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 4.6174859999999995,
            "transaction_id": 10
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
            "conn_id": 27,
            "dial_id": 27,
            "failure": null,
            "operation": "connect",
            "proto": "tcp",
            "t": 4.021172
          },
          {
            "conn_id": 27,
            "failure": null,
            "num_bytes": 243,
            "operation": "write",
            "proto": "tcp",
            "t": 4.021528
          },
          {
            "conn_id": 27,
            "failure": null,
            "num_bytes": 99,
            "operation": "read",
            "proto": "tcp",
            "t": 4.07828
          },
          {
            "conn_id": 27,
            "failure": null,
            "num_bytes": 6,
            "operation": "write",
            "proto": "tcp",
            "t": 4.078421
          },
          {
            "conn_id": 27,
            "failure": null,
            "num_bytes": 276,
            "operation": "write",
            "proto": "tcp",
            "t": 4.078699
          },
          {
            "conn_id": 27,
            "failure": null,
            "num_bytes": 517,
            "operation": "read",
            "proto": "tcp",
            "t": 4.136872
          },
          {
            "conn_id": 27,
            "failure": null,
            "num_bytes": 652,
            "operation": "read",
            "proto": "tcp",
            "t": 4.137291
          },
          {
            "conn_id": 27,
            "failure": null,
            "num_bytes": 74,
            "operation": "write",
            "proto": "tcp",
            "t": 4.137984
          },
          {
            "conn_id": 27,
            "failure": null,
            "num_bytes": 24,
            "operation": "write",
            "proto": "tcp",
            "t": 4.138135
          }
        ],
        "queries": null,
        "requests": null,
        "summary": {
          "connect": {
            "failure": null
          },
          "handshake": {
            "failure": null
          }
        },
        "target_address": "131.188.40.189:443",
        "target_name": "gabelmoo",
        "target_protocol": "or_port_dirauth",
        "tcp_connect": [
          {
            "conn_id": 27,
            "dial_id": 27,
            "ip": "131.188.40.189",
            "port": 443,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 4.021172
          }
        ],
        "tls_handshakes": [
          {
            "cipher_suite": "TLS_AES_256_GCM_SHA384",
            "conn_id": 27,
            "failure": null,
            "negotiated_protocol": "",
            "peer_certificates": [
              {
                "data": "MIICRjCCAa+gAwIBAgIJAJCdHhPJJ2LUMA0GCSqGSIb3DQEBCwUAMB8xHTAbBgNVBAMMFHd3dy5ra2RpbDZvanNtaTYuY29tMB4XDTE5MDYxMjAwMDAwMFoXDTIwMDMwNjAwMDAwMFowJzElMCMGA1UEAwwcd3d3LndrankzNjdydWZyaHhrbnFubXNiLm5ldDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAKXey1C5qSMf7aZHFj7R6hpo9TLTCD8vuikoR0IABUcctDXpKvnx03r+p2CUC0Q/x8FPhOgTh37jOWPFyfQWVNYos1uHeh7olw6m4WR5Wf9otBKnUz5uc/7QtjMwZXuNTnGp9b8gXyTNTYni0nHvm9XFsPfzK1A5CiN31pfNzJl5uYk+eozsKMb07raIpH//2B4UNydKo3G5iPXtjZyM/5Ly1292e5GLTCOAtkmHaXVPgdfYsGuVoqdjceSpKUkRvPt6cDPj3JnafC82qoZr6zgkXI3tB9+2CIl/AvVRY/msmxDK49URHnyqRe1Vhpjk69lwvNT9FaEaU9FL3fm/adkCAwEAATANBgkqhkiG9w0BAQsFAAOBgQB8PhOCV7wo3/mOEfYS03qPab+vRIOsufgs5pDPodyBBpAjxxqKpu/aOjgbnGE4kO09nXnC1BoXAvUMBJwULE/CzSOaxOLnr81hHsFK4Zinn8rFCj/IpWZmeiEWHtSmDBg+jVh9qIGo7du/lrexlLRPRoEZ+RijBQN949E+/258tQ==",
                "format": "base64"
              }
            ],
            "t": 4.138006,
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
                  "Host",
                  "131.188.40.189:80"
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
                "data": "eNrs/Vdz48i2LQq/r1+Bx/sFu0QgE5Zx1o0DS9CA3t/YsQOeICxhCJK//suEVNUlFNWu+uyWdFZ3FSWxJAqYzMzpxhwjccs6zcMvRWmWVfHl4uZFkCYE/NclLd2XZwk7TQo3KariX98++xK75TF1CCD862JGgfPF9Eo3JwAJyC8k9QWSBMX2SBL9+ZeXu8XxS5WUQfTq37mXf3/++R//Xfj672kZJP4Xx43MGwFJEv/9lx0FblJ+vd6CIJ/gE/PE/fL8kX/5KKCP9BP5xLx8ZJuP1BP4YkbZ0Xz5Cr76iv6S2y+fMi8fv/4Y9/KRbz6CJ+q7HwSvXhS8elHw64uClw==",
                "format": "base64"
              },
              "body_is_truncated": true,
              "code": 200,
              "headers_list": [
                [
                  "Date",
                  "Thu, 30 Jan 2020 16:47:35 GMT"
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
                  "Thu, 30 Jan 2020 17:00:00 GMT"
                ],
                [
                  "Vary",
                  "X-Or-Diff-From-Consensus"
                ]
              ],
              "headers": {
                "Content-Encoding": "deflate",
                "Content-Type": "text/plain",
                "Date": "Thu, 30 Jan 2020 16:47:35 GMT",
                "Expires": "Thu, 30 Jan 2020 17:00:00 GMT",
                "Vary": "X-Or-Diff-From-Consensus",
                "X-Your-Address-Is": "[REDACTED]"
              }
            },
            "transaction_id": 1
          }
        ],
        "summary": {
          "connect": {
            "failure": null
          }
        },
        "target_address": "131.188.40.189:80",
        "target_name": "gabelmoo",
        "target_protocol": "dir_port",
        "tcp_connect": [
          {
            "conn_id": 1,
            "dial_id": 2,
            "ip": "131.188.40.189",
            "port": 80,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 0.957678,
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
            "conn_id": 16,
            "dial_id": 15,
            "failure": null,
            "operation": "connect",
            "proto": "tcp",
            "t": 2.603238
          },
          {
            "conn_id": 16,
            "failure": null,
            "num_bytes": 243,
            "operation": "write",
            "proto": "tcp",
            "t": 2.603688
          },
          {
            "conn_id": 16,
            "failure": null,
            "num_bytes": 517,
            "operation": "read",
            "proto": "tcp",
            "t": 2.734684
          },
          {
            "conn_id": 16,
            "failure": null,
            "num_bytes": 478,
            "operation": "read",
            "proto": "tcp",
            "t": 2.734765
          },
          {
            "conn_id": 16,
            "failure": null,
            "num_bytes": 126,
            "operation": "write",
            "proto": "tcp",
            "t": 2.735533
          },
          {
            "conn_id": 16,
            "failure": null,
            "num_bytes": 51,
            "operation": "read",
            "proto": "tcp",
            "t": 2.86655
          },
          {
            "conn_id": 16,
            "failure": null,
            "num_bytes": 31,
            "operation": "write",
            "proto": "tcp",
            "t": 2.86687
          }
        ],
        "queries": null,
        "requests": null,
        "summary": {
          "connect": {
            "failure": null
          },
          "handshake": {
            "failure": null
          }
        },
        "target_address": "154.35.175.225:443",
        "target_name": "Faravahar",
        "target_protocol": "or_port_dirauth",
        "tcp_connect": [
          {
            "conn_id": 16,
            "dial_id": 15,
            "ip": "154.35.175.225",
            "port": 443,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 2.603238
          }
        ],
        "tls_handshakes": [
          {
            "cipher_suite": "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384",
            "conn_id": 16,
            "failure": null,
            "negotiated_protocol": "",
            "peer_certificates": [
              {
                "data": "MIICNzCCAaCgAwIBAgIJAP2Q0h+NygFTMA0GCSqGSIb3DQEBCwUAMBsxGTAXBgNVBAMMEHd3dy54cHducmthMy5jb20wHhcNMTkxMjIzMDAwMDAwWhcNMjAxMTA1MjM1OTU5WjAcMRowGAYDVQQDDBF3d3cueWxlbXgydDdtLm5ldDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAO7mTko+zvCVaRFLnARIHx2LvJEDiP4KhJzTw+tdRV++8WBzjzO4NCFEYZp/69csnyRKZMFLLKAbYJzxPAXAgFVLM/y/9ImRAVUhhF7sNTHe2sJ8q+BXoIZ157f8k6tYvT5n0iHkXUzbhWKoXGL8HcO4hquNk1IpIMTrc2FIbVRvULOIeI3xr/SqrN1SGArAzJeFo1qM9cf3iKnzoG0m7JU8A9Uoh35IajJ76T24UGdXRpz4FSgn6ckcmMhkGp3IYOeyKyWZy4Uf5sxGOHfmXENIgmWGtU1cAtS4IQOschSVBPI2hnbsRHFAnkdscEohCdiN9v5I1fQzvygZ7ktw7zUCAwEAATANBgkqhkiG9w0BAQsFAAOBgQCr6zUbyZeEF6NXAkGBmQ6xJqiJz+91NSDSzArzhRaVh78kzYDU/kGOeteX2rr0SBFFlqVGt10rGdOJm+V/V91lVb4nypBJWVesLCHnsM1d1sV0awxlEfvvY+YRSCYHYuPYFt3cSchcegqnQiFHOh0Y7sXLKl3La7u1jH5W+2WWJw==",
                "format": "base64"
              }
            ],
            "t": 2.866726,
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
                  "Accept-Language",
                  "en-US;q=0.8,en;q=0.5"
                ],
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
                "data": "eNrs/Vdz48i2LQq/r1+Bx/sFu0QgE5Zx1o0DS9CA3t/YsQOeICxhCJK//suEVNUlFNWu+uyWdFZ3FSWxJAqYzMzpxhwjccs6zcMvRWmWVfHl4uZFkCYE/NclLd2XZwk7TQo3KariX98++xK75TF1CCD862JGgfPF9Eo3JwAJyC8k9QWSBMX2SBL9+ZeXu8XxS5WUQfTq37mXf3/++R//Xfj672kZJP4Xx43MGwFJEv/9lx0FblJ+vd6CIJ/gE/PE/fL8kX/5KKCP9BP5xLx8ZJuP1BP4YkbZ0Xz5Cr76iv6S2y+fMi8fv/4Y9/KRbz6CJ+q7HwSvXhS8elHw64uClw==",
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
                  "Thu, 30 Jan 2020 16:47:38 GMT"
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
                  "Thu, 30 Jan 2020 17:00:00 GMT"
                ]
              ],
              "headers": {
                "Content-Encoding": "deflate",
                "Content-Type": "text/plain",
                "Date": "Thu, 30 Jan 2020 16:47:38 GMT",
                "Expires": "Thu, 30 Jan 2020 17:00:00 GMT",
                "Vary": "X-Or-Diff-From-Consensus",
                "X-Your-Address-Is": "[REDACTED]"
              }
            },
            "transaction_id": 9
          }
        ],
        "summary": {
          "connect": {
            "failure": null
          }
        },
        "target_address": "154.35.175.225:80",
        "target_name": "Faravahar",
        "target_protocol": "dir_port",
        "tcp_connect": [
          {
            "conn_id": 24,
            "dial_id": 24,
            "ip": "154.35.175.225",
            "port": 80,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 3.657081,
            "transaction_id": 9
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
                "data": "eNrs/Vdz48i2LQq/r1+Bx/sFu0QgE5Zx1o0DS9CA3t/YsQOeICxhCJK//suEVNUlFNWu+uyWdFZ3FSWxJAqYzMzpxhwjccs6zcMvRWmWVfHl4uZFkCYE/NclLd2XZwk7TQo3KariX98++xK75TF1CCD862JGgfPF9Eo3JwAJyC8k9QWSBMX2SBL9+ZeXu8XxS5WUQfTq37mXf3/++R//Xfj672kZJP4Xx43MGwFJEv/9lx0FblJ+vd6CIJ/gE/PE/fL8kX/5KKCP9BP5xLx8ZJuP1BP4YkbZ0Xz5Cr76iv6S2y+fMi8fv/4Y9/KRbz6CJ+q7HwSvXhS8elHw64uClw==",
                "format": "base64"
              },
              "body_is_truncated": true,
              "code": 200,
              "headers_list": [
                [
                  "Date",
                  "Thu, 30 Jan 2020 16:47:38 GMT"
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
                  "Thu, 30 Jan 2020 17:00:00 GMT"
                ],
                [
                  "Vary",
                  "X-Or-Diff-From-Consensus"
                ]
              ],
              "headers": {
                "Content-Encoding": "deflate",
                "Content-Type": "text/plain",
                "Date": "Thu, 30 Jan 2020 16:47:38 GMT",
                "Expires": "Thu, 30 Jan 2020 17:00:00 GMT",
                "Vary": "X-Or-Diff-From-Consensus",
                "X-Your-Address-Is": "[REDACTED]"
              }
            },
            "transaction_id": 8
          }
        ],
        "summary": {
          "connect": {
            "failure": null
          }
        },
        "target_address": "171.25.193.9:443",
        "target_name": "maatuska",
        "target_protocol": "dir_port",
        "tcp_connect": [
          {
            "conn_id": 23,
            "dial_id": 23,
            "ip": "171.25.193.9",
            "port": 443,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 3.506906,
            "transaction_id": 8
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
            "conn_id": 3,
            "dial_id": 3,
            "failure": null,
            "operation": "connect",
            "proto": "tcp",
            "t": 1.06528
          },
          {
            "conn_id": 3,
            "failure": null,
            "num_bytes": 243,
            "operation": "write",
            "proto": "tcp",
            "t": 1.065529
          },
          {
            "conn_id": 3,
            "failure": null,
            "num_bytes": 99,
            "operation": "read",
            "proto": "tcp",
            "t": 1.117225
          },
          {
            "conn_id": 3,
            "failure": null,
            "num_bytes": 6,
            "operation": "write",
            "proto": "tcp",
            "t": 1.117312
          },
          {
            "conn_id": 3,
            "failure": null,
            "num_bytes": 276,
            "operation": "write",
            "proto": "tcp",
            "t": 1.117433
          },
          {
            "conn_id": 3,
            "failure": null,
            "num_bytes": 517,
            "operation": "read",
            "proto": "tcp",
            "t": 1.173175
          },
          {
            "conn_id": 3,
            "failure": null,
            "num_bytes": 653,
            "operation": "read",
            "proto": "tcp",
            "t": 1.173517
          },
          {
            "conn_id": 3,
            "failure": null,
            "num_bytes": 74,
            "operation": "write",
            "proto": "tcp",
            "t": 1.173997
          },
          {
            "conn_id": 3,
            "failure": null,
            "num_bytes": 24,
            "operation": "write",
            "proto": "tcp",
            "t": 1.174063
          }
        ],
        "queries": null,
        "requests": null,
        "summary": {
          "connect": {
            "failure": null
          },
          "handshake": {
            "failure": null
          }
        },
        "target_address": "171.25.193.9:80",
        "target_name": "maatuska",
        "target_protocol": "or_port_dirauth",
        "tcp_connect": [
          {
            "conn_id": 3,
            "dial_id": 3,
            "ip": "171.25.193.9",
            "port": 80,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 1.06528
          }
        ],
        "tls_handshakes": [
          {
            "cipher_suite": "TLS_AES_256_GCM_SHA384",
            "conn_id": 3,
            "failure": null,
            "negotiated_protocol": "",
            "peer_certificates": [
              {
                "data": "MIICRzCCAbCgAwIBAgIJAPFp71v0j6t6MA0GCSqGSIb3DQEBCwUAMCMxITAfBgNVBAMMGHd3dy51ZGNpZHBtZ200bWJhanN4LmNvbTAeFw0xOTEyMTYwMDAwMDBaFw0yMDA2MDIyMzU5NTlaMCQxIjAgBgNVBAMMGXd3dy5obmtnZnh5bGhieXlsY21jci5uZXQwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDbLw7lLzQaOOkqE5qjIta7JYwGHV09ZVN5LZZPMpqexoWO68pjDQt7YTD/aMqRUa9SBVpmRe4GQXTf061/77BILLTNjwNcJ+XOVcpiPgGxMpYjg/an21ir8O5u0B3qg1lVz3RvO6H16D1xTWv95wtQm19YkESaRf+D2jnPOfJkMoXQINWtJWM3aWvjmlKJi/xfK7FB7Lir1bjSR5EaJ2eh/RyKWfBbbVP8hWR+ySelD/YHxG5j5FqGWkkflhkGviDonIjlphsEEFn0+tOdx1uoQbhGfXOGrROiYtdOTO/LoErxlIRXSbTELSlyNDvJBtuCeoQGnEdJN9hZvBqMgqBXAgMBAAEwDQYJKoZIhvcNAQELBQADgYEAjMwrAFz84LvSdSCwvCwTdhwgEFwRPZirZcxHbfSrox23jWDli9JQyfsCciVG+efmrv+S76zXQF4RNvAPqwUddxqMzKsXkzAjc241uLVotPlQE66hXyQjkd7ocJGoMc2L/TzT6GDzIp1q2M0S0rypNCso4PuBeH66clROhCstyQc=",
                "format": "base64"
              }
            ],
            "t": 1.174017,
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
            "conn_id": 21,
            "dial_id": 22,
            "failure": null,
            "operation": "connect",
            "proto": "tcp",
            "t": 3.362117
          },
          {
            "conn_id": 21,
            "failure": null,
            "num_bytes": 243,
            "operation": "write",
            "proto": "tcp",
            "t": 3.362379
          },
          {
            "conn_id": 21,
            "failure": null,
            "num_bytes": 517,
            "operation": "read",
            "proto": "tcp",
            "t": 3.408986
          },
          {
            "conn_id": 21,
            "failure": null,
            "num_bytes": 493,
            "operation": "read",
            "proto": "tcp",
            "t": 3.4090949999999998
          },
          {
            "conn_id": 21,
            "failure": null,
            "num_bytes": 126,
            "operation": "write",
            "proto": "tcp",
            "t": 3.409994
          },
          {
            "conn_id": 21,
            "failure": null,
            "num_bytes": 51,
            "operation": "read",
            "proto": "tcp",
            "t": 3.452845
          },
          {
            "conn_id": 21,
            "failure": null,
            "num_bytes": 31,
            "operation": "write",
            "proto": "tcp",
            "t": 3.453112
          }
        ],
        "queries": null,
        "requests": null,
        "summary": {
          "connect": {
            "failure": null
          },
          "handshake": {
            "failure": null
          }
        },
        "target_address": "193.23.244.244:443",
        "target_name": "dannenberg",
        "target_protocol": "or_port_dirauth",
        "tcp_connect": [
          {
            "conn_id": 21,
            "dial_id": 22,
            "ip": "193.23.244.244",
            "port": 443,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 3.362117
          }
        ],
        "tls_handshakes": [
          {
            "cipher_suite": "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384",
            "conn_id": 21,
            "failure": null,
            "negotiated_protocol": "",
            "peer_certificates": [
              {
                "data": "MIICSDCCAbGgAwIBAgIIY7hH+diY9rIwDQYJKoZIhvcNAQELBQAwJjEkMCIGA1UEAwwbd3d3LnR1d2RyempocXVyaXN0czZpZHkuY29tMB4XDTIwMDEwNDAwMDAwMFoXDTIwMDMxOTIzNTk1OVowIzEhMB8GA1UEAwwYd3d3LmlxaGJobTdzZmdhb2ZhY2QubmV0MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAswMFPyEE041U/EKKKtBiFTG2GUU4puiyyMOBPjENuGWi30lcb1Wamp//TYDoB2jvMtvOCnYdnqjR9Fwo7mSmTjEYBnfQ0RcIwNmGzyR2dVIyieXxOwdmVlZElrauEfFmM4hC8NsBa/Y4Lt2epHy7h4WJyu8wOsZItzPZLHZK+W+8ZGce4eIyEOf3ITRSuit94mjZ03emvVut3cHKtrJa3ZmmVlKEAYjUIuNaeJ8GNkbUtel5VO0CqBS54r/RZACBWd7nI+GSgA2YQ+l6N6CThczhC2DlI+khIYeS8obRny7iAwunrwOsyOO0WjfCcenrjE4uepdNEoRjPkMPBZSjAwIDAQABMA0GCSqGSIb3DQEBCwUAA4GBAB4snjvjhlkt54NBnf8O0orTc+JgGLjUmWa81bjo5pAhrz+sC27bcqbDqLGRE7/3pqyBhm2AchFoggKT4IU26SLQCEy7cBcK7K6q4pM+rQHZS3N0wSOadbnHcQZT/nYYAW3R4EOItPf3HCUDgqHZ2f/GcoPJLEXXMcMn8usXM0uX",
                "format": "base64"
              }
            ],
            "t": 3.453005,
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
                ],
                [
                  "Accept-Language",
                  "en-US;q=0.8,en;q=0.5"
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
                "data": "eNrs/Vdz48i2LQq/r1+Bx/sFu0QgE5Zx1o0DS9CA3t/YsQOeICxhCJK//suEVNUlFNWu+uyWdFZ3FSWxJAqYzMzpxhwjccs6zcMvRWmWVfHl4uZFkCYE/NclLd2XZwk7TQo3KariX98++xK75TF1CCD862JGgfPF9Eo3JwAJyC8k9QWSBMX2SBL9+ZeXu8XxS5WUQfTq37mXf3/++R//Xfj672kZJP4Xx43MGwFJEv/9lx0FblJ+vd6CIJ/gE/PE/fL8kX/5KKCP9BP5xLx8ZJuP1BP4YkbZ0Xz5Cr76iv6S2y+fMi8fv/4Y9/KRbz6CJ+q7HwSvXhS8elHw64uClw==",
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
                  "Thu, 30 Jan 2020 17:00:00 GMT"
                ],
                [
                  "Vary",
                  "X-Or-Diff-From-Consensus"
                ],
                [
                  "Date",
                  "Thu, 30 Jan 2020 16:47:37 GMT"
                ],
                [
                  "Content-Type",
                  "text/plain"
                ]
              ],
              "headers": {
                "Content-Encoding": "deflate",
                "Content-Type": "text/plain",
                "Date": "Thu, 30 Jan 2020 16:47:37 GMT",
                "Expires": "Thu, 30 Jan 2020 17:00:00 GMT",
                "Vary": "X-Or-Diff-From-Consensus",
                "X-Your-Address-Is": "[REDACTED]"
              }
            },
            "transaction_id": 5
          }
        ],
        "summary": {
          "connect": {
            "failure": null
          }
        },
        "target_address": "193.23.244.244:80",
        "target_name": "dannenberg",
        "target_protocol": "dir_port",
        "tcp_connect": [
          {
            "conn_id": 14,
            "dial_id": 14,
            "ip": "193.23.244.244",
            "port": 80,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 2.429078,
            "transaction_id": 5
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
            "conn_id": 15,
            "dial_id": 16,
            "failure": null,
            "operation": "connect",
            "proto": "tcp",
            "t": 2.598769
          },
          {
            "conn_id": 15,
            "failure": null,
            "num_bytes": 243,
            "operation": "write",
            "proto": "tcp",
            "t": 2.599126
          },
          {
            "conn_id": 15,
            "failure": null,
            "num_bytes": 517,
            "operation": "read",
            "proto": "tcp",
            "t": 2.726705
          },
          {
            "conn_id": 15,
            "failure": null,
            "num_bytes": 487,
            "operation": "read",
            "proto": "tcp",
            "t": 2.726791
          },
          {
            "conn_id": 15,
            "failure": null,
            "num_bytes": 126,
            "operation": "write",
            "proto": "tcp",
            "t": 2.727987
          },
          {
            "conn_id": 15,
            "failure": null,
            "num_bytes": 51,
            "operation": "read",
            "proto": "tcp",
            "t": 2.852612
          },
          {
            "conn_id": 15,
            "failure": null,
            "num_bytes": 31,
            "operation": "write",
            "proto": "tcp",
            "t": 2.853848
          }
        ],
        "queries": null,
        "requests": null,
        "summary": {
          "connect": {
            "failure": null
          },
          "handshake": {
            "failure": null
          }
        },
        "target_address": "199.58.81.140:443",
        "target_name": "longclaw",
        "target_protocol": "or_port_dirauth",
        "tcp_connect": [
          {
            "conn_id": 15,
            "dial_id": 16,
            "ip": "199.58.81.140",
            "port": 443,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 2.598769
          }
        ],
        "tls_handshakes": [
          {
            "cipher_suite": "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384",
            "conn_id": 15,
            "failure": null,
            "negotiated_protocol": "",
            "peer_certificates": [
              {
                "data": "MIICQDCCAamgAwIBAgIIZzXIDTAwUe4wDQYJKoZIhvcNAQELBQAwIzEhMB8GA1UEAwwYd3d3LjZyaXg1djN4cmR0YngyZTcuY29tMB4XDTIwMDEwNTAwMDAwMFoXDTIwMDcyOTAwMDAwMFowHjEcMBoGA1UEAwwTd3d3LjNhaGNnenZtdGJ2Lm5ldDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBALAMJbiK8IJVmOXLwwdTLA/RXcZtUYlP/Sbcqniiaj4fwjNZvwpyAen3hTosA/zFnjPqkau6KTfGiBdakxVeTiGDzc3sPqUP+AEIFIbn9zVSbqTP/du2NeaGWvBXZP/ni8Bkc/0SLaD2h5y6B765CB12NGPZ2Lt817IVCRf5x4aLI+CkxmghB0PYlg2NtxwV7kyfBrFc1MoX767h705MT4WWgcD4jV9pCg+KZbujrJlF3PTOBdodSMG+Aw9oeIDos/Av5TN3navh7BKSgPog9bz6H1PPiT0iqGTRq6eLOejQOeJ6GCZqOukEUdG64yHHnPKsbVhn2NzcVPIqWdG/GDMCAwEAATANBgkqhkiG9w0BAQsFAAOBgQA1kI4ua738YBeWN/h9iUI/aMlUX+GD+I0oqXn5rgkVdC8tifVnmQpu3M4ETyZr1JbFDmXY4Ff5j55XuD3Q7PXMOjgQsz8o8wpd0x4wbKKLQHYaV4G7qHjCg0rImnfWcFAuQyX+XZUkYS3GV3HuBBhM1S8ea52Cq5aq4XdmLKlrvg==",
                "format": "base64"
              }
            ],
            "t": 2.853654,
            "tls_version": "TLSv1.2"
          }
        ]
      },
      "199.58.81.140:80": {
        "agent": "redirect",
        "failure": "Get http://199.58.81.140:80/tor/status-vote/current/consensus.z: eof_error",
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
                  "199.58.81.140:80"
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
              "body": "",
              "body_is_truncated": false,
              "code": 503,
              "headers_list": [
                [
                  "Date",
                  "Thu, 30 Jan 2020 16:47:36 GMT"
                ]
              ],
              "headers": {
                "Date": "Thu, 30 Jan 2020 16:47:36 GMT"
              }
            },
            "transaction_id": 4
          }
        ],
        "summary": {
          "connect": {
            "failure": null
          }
        },
        "target_address": "199.58.81.140:80",
        "target_name": "longclaw",
        "target_protocol": "dir_port",
        "tcp_connect": [
          {
            "conn_id": 9,
            "dial_id": 8,
            "ip": "199.58.81.140",
            "port": 80,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 1.857672,
            "transaction_id": 4
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
            "conn_id": 33,
            "dial_id": 33,
            "failure": null,
            "operation": "connect",
            "proto": "tcp",
            "t": 5.008125
          },
          {
            "conn_id": 33,
            "failure": null,
            "num_bytes": 243,
            "operation": "write",
            "proto": "tcp",
            "t": 5.008459
          },
          {
            "conn_id": 33,
            "failure": null,
            "num_bytes": 517,
            "operation": "read",
            "proto": "tcp",
            "t": 5.198528
          },
          {
            "conn_id": 33,
            "failure": null,
            "num_bytes": 488,
            "operation": "read",
            "proto": "tcp",
            "t": 5.198597
          },
          {
            "conn_id": 33,
            "failure": null,
            "num_bytes": 126,
            "operation": "write",
            "proto": "tcp",
            "t": 5.199503
          },
          {
            "conn_id": 33,
            "failure": null,
            "num_bytes": 51,
            "operation": "read",
            "proto": "tcp",
            "t": 5.388409
          },
          {
            "conn_id": 33,
            "failure": null,
            "num_bytes": 31,
            "operation": "write",
            "proto": "tcp",
            "t": 5.388662
          }
        ],
        "queries": null,
        "requests": null,
        "summary": {
          "connect": {
            "failure": null
          },
          "handshake": {
            "failure": null
          }
        },
        "target_address": "204.13.164.118:443",
        "target_name": "bastet",
        "target_protocol": "or_port_dirauth",
        "tcp_connect": [
          {
            "conn_id": 33,
            "dial_id": 33,
            "ip": "204.13.164.118",
            "port": 443,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 5.008125
          }
        ],
        "tls_handshakes": [
          {
            "cipher_suite": "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384",
            "conn_id": 33,
            "failure": null,
            "negotiated_protocol": "",
            "peer_certificates": [
              {
                "data": "MIICQTCCAaqgAwIBAgIId0JMzicTviAwDQYJKoZIhvcNAQELBQAwJDEiMCAGA1UEAwwZd3d3Lmd6M3Byb2tta3lzc2x0ZmY3LmNvbTAeFw0xOTEyMzAwMDAwMDBaFw0yMDA3MDkwMDAwMDBaMB4xHDAaBgNVBAMME3d3dy40N3hycm5yc3UyYi5uZXQwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDVQz26AGYWWSW14tAbkvuRUn3HDWYoX8/2cMAc8LRcTfAG1MroV+Kh858Y1X/YWNOAnZ6+iEL9qySaxwTEosupDsELZvr4QAiQE2nNLODxyummYBNvK5VvPYkwdDhLDf9sHH3BLiKDM5Gf3rNGCSjNsl79v7xiivWc+wq5jwjAYy+Tv2rYFPM4W0OC5Zkry7v+piR1qcqrHOyYifSWjtLJ6Fi/2A65nfu+TihMpajA4l8/+Xp08ISloXZdDtdPwe1tgUhEpG5lPX8VHmaNbqbM3j44LMxWSDndaGayq7YR9LkvVhNUwRknmgY4oWbZVQwC6LCqhCZP7BlKFDj0xPlNAgMBAAEwDQYJKoZIhvcNAQELBQADgYEAa4rnQPMpvSqWOAsiP5V0DdaJ0Jgs+NtJHznDjh6D2inMjje9Glv7TYozWgbTXwFqcYjEDFT8Fy8crRJr+0yEdzET/9b4brL9JQZCP3YsZ9GSsMAWNc83JkzPGXuAyXlDNnEluDWH6+IwJ+Cg2sDGL4QKL366l6NgWWRCmap4AYs=",
                "format": "base64"
              }
            ],
            "t": 5.388532,
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
                  "Accept-Language",
                  "en-US;q=0.8,en;q=0.5"
                ],
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
                "data": "eNrs/Vdz48i2LQq/r1+Bx/sFu0QgE5Zx1o0DS9CA3t/YsQOeICxhCJK//suEVNUlFNWu+uyWdFZ3FSWxJAqYzMzpxhwjccs6zcMvRWmWVfHl4uZFkCYE/NclLd2XZwk7TQo3KariX98++xK75TF1CCD862JGgfPF9Eo3JwAJyC8k9QWSBMX2SBL9+ZeXu8XxS5WUQfTq37mXf3/++R//Xfj672kZJP4Xx43MGwFJEv/9lx0FblJ+vd6CIJ/gE/PE/fL8kX/5KKCP9BP5xLx8ZJuP1BP4YkbZ0Xz5Cr76iv6S2y+fMi8fv/4Y9/KRbz6CJ+q7HwSvXhS8elHw64uClw==",
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
                  "Thu, 30 Jan 2020 16:47:36 GMT"
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
                  "Thu, 30 Jan 2020 17:00:00 GMT"
                ]
              ],
              "headers": {
                "Content-Encoding": "deflate",
                "Content-Type": "text/plain",
                "Date": "Thu, 30 Jan 2020 16:47:36 GMT",
                "Expires": "Thu, 30 Jan 2020 17:00:00 GMT",
                "Vary": "X-Or-Diff-From-Consensus",
                "X-Your-Address-Is": "[REDACTED]"
              }
            },
            "transaction_id": 3
          }
        ],
        "summary": {
          "connect": {
            "failure": null
          }
        },
        "target_address": "204.13.164.118:80",
        "target_name": "bastet",
        "target_protocol": "dir_port",
        "tcp_connect": [
          {
            "conn_id": 7,
            "dial_id": 6,
            "ip": "204.13.164.118",
            "port": 80,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 1.531208,
            "transaction_id": 3
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
            "conn_id": 12,
            "dial_id": 12,
            "failure": null,
            "operation": "connect",
            "proto": "tcp",
            "t": 2.209119
          },
          {
            "conn_id": 12,
            "failure": null,
            "num_bytes": 1672,
            "operation": "write",
            "proto": "tcp",
            "t": 2.209689
          },
          {
            "conn_id": 12,
            "failure": null,
            "num_bytes": 7364,
            "operation": "read",
            "proto": "tcp",
            "t": 2.265815
          }
        ],
        "queries": null,
        "requests": null,
        "summary": {
          "connect": {
            "failure": null
          },
          "handshake": {
            "failure": null
          }
        },
        "target_address": "193.11.166.194:27020",
        "target_protocol": "obfs4",
        "tcp_connect": [
          {
            "conn_id": 12,
            "dial_id": 12,
            "ip": "193.11.166.194",
            "port": 27020,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 2.209119
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
            "conn_id": 17,
            "dial_id": 18,
            "failure": null,
            "operation": "connect",
            "proto": "tcp",
            "t": 2.907522
          },
          {
            "conn_id": 17,
            "failure": null,
            "num_bytes": 1707,
            "operation": "write",
            "proto": "tcp",
            "t": 2.908203
          },
          {
            "conn_id": 17,
            "failure": null,
            "num_bytes": 1440,
            "operation": "read",
            "proto": "tcp",
            "t": 2.948864
          },
          {
            "conn_id": 17,
            "failure": null,
            "num_bytes": 1440,
            "operation": "read",
            "proto": "tcp",
            "t": 2.948926
          },
          {
            "conn_id": 17,
            "failure": null,
            "num_bytes": 1440,
            "operation": "read",
            "proto": "tcp",
            "t": 2.949374
          },
          {
            "conn_id": 17,
            "failure": null,
            "num_bytes": 485,
            "operation": "read",
            "proto": "tcp",
            "t": 2.949602
          }
        ],
        "queries": null,
        "requests": null,
        "summary": {
          "connect": {
            "failure": null
          },
          "handshake": {
            "failure": null
          }
        },
        "target_address": "37.218.245.14:38224",
        "target_protocol": "obfs4",
        "tcp_connect": [
          {
            "conn_id": 17,
            "dial_id": 18,
            "ip": "37.218.245.14",
            "port": 38224,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 2.907522
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
            "conn_id": 5,
            "dial_id": 5,
            "failure": null,
            "operation": "connect",
            "proto": "tcp",
            "t": 1.328198
          },
          {
            "conn_id": 5,
            "failure": null,
            "num_bytes": 243,
            "operation": "write",
            "proto": "tcp",
            "t": 1.328871
          },
          {
            "conn_id": 5,
            "failure": null,
            "num_bytes": 99,
            "operation": "read",
            "proto": "tcp",
            "t": 1.366983
          },
          {
            "conn_id": 5,
            "failure": null,
            "num_bytes": 6,
            "operation": "write",
            "proto": "tcp",
            "t": 1.367037
          },
          {
            "conn_id": 5,
            "failure": null,
            "num_bytes": 276,
            "operation": "write",
            "proto": "tcp",
            "t": 1.36722
          },
          {
            "conn_id": 5,
            "failure": null,
            "num_bytes": 517,
            "operation": "read",
            "proto": "tcp",
            "t": 1.408498
          },
          {
            "conn_id": 5,
            "failure": null,
            "num_bytes": 641,
            "operation": "read",
            "proto": "tcp",
            "t": 1.408749
          },
          {
            "conn_id": 5,
            "failure": null,
            "num_bytes": 74,
            "operation": "write",
            "proto": "tcp",
            "t": 1.409086
          },
          {
            "conn_id": 5,
            "failure": null,
            "num_bytes": 24,
            "operation": "write",
            "proto": "tcp",
            "t": 1.409157
          }
        ],
        "queries": null,
        "requests": null,
        "summary": {
          "connect": {
            "failure": null
          },
          "handshake": {
            "failure": null
          }
        },
        "target_address": "45.66.33.45:443",
        "target_name": "dizum",
        "target_protocol": "or_port_dirauth",
        "tcp_connect": [
          {
            "conn_id": 5,
            "dial_id": 5,
            "ip": "45.66.33.45",
            "port": 443,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 1.328198
          }
        ],
        "tls_handshakes": [
          {
            "cipher_suite": "TLS_AES_256_GCM_SHA384",
            "conn_id": 5,
            "failure": null,
            "negotiated_protocol": "",
            "peer_certificates": [
              {
                "data": "MIICOzCCAaSgAwIBAgIJAOpLBGtZWUgfMA0GCSqGSIb3DQEBCwUAMB0xGzAZBgNVBAMMEnd3dy5naTZhYmhnbTJsLmNvbTAeFw0xOTA4MjIwMDAwMDBaFw0yMDA4MDYwMDAwMDBaMB4xHDAaBgNVBAMME3d3dy5jM241ZXA0ZHZyZC5uZXQwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDBgP3sA8/k6grV1pt0TS5wWrwao6AHcLE1/jrujSvo/Am+kUzA8aIaSISEl66zWPDVrd3EdMVe1w6RUzxDZlmmXXM7vgpk0hoHcsiSHPqmeA8Ue1ISYZIPu6wBNDHlRNJuROONxAurThV1yCpQ1PCf66LApJP8NDFpYGbYtll3i7SOAAwi6jlJu4ouDY8RQrX24lbBJSZQXE5M/d5yrSiZjq3nNUBLkxLRWIVW+IDum+1XRAIyMFMcvAaY3816l5ygW14bPWZvuzyORM1RtfDEqdlVhRT0ZXYkKZb+UQDmUnenNbozTjaH5ELA1o0vCpd6x2UgsbOnjGJE2PmQz1QHAgMBAAEwDQYJKoZIhvcNAQELBQADgYEAktVCd9bGYjzlbP8EfrIeXEyrQd8BdmrlCTGk6pH9AtJ5bUuK4bmnEkoL8cAdQLGU4YBmCaLEZLMA1+25t35citTrpIg0a4rkwJwsr94KU7tQAtlZTt01E8SGhkYOH8JwH7NmH0rsZfAEGqkpdRTq9g42K9NGaxSPJ47JB5GUnjM=",
                "format": "base64"
              }
            ],
            "t": 1.409095,
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
                  "Host",
                  "45.66.33.45:80"
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
                "data": "eNrs/Vdz48i2LQq/r1+Bx/sFu0QgE5Zx1o0DS9CA3t/YsQOeICxhCJK//suEVNUlFNWu+uyWdFZ3FSWxJAqYzMzpxhwjccs6zcMvRWmWVfHl4uZFkCYE/NclLd2XZwk7TQo3KariX98++xK75TF1CCD862JGgfPF9Eo3JwAJyC8k9QWSBMX2SBL9+ZeXu8XxS5WUQfTq37mXf3/++R//Xfj672kZJP4Xx43MGwFJEv/9lx0FblJ+vd6CIJ/gE/PE/fL8kX/5KKCP9BP5xLx8ZJuP1BP4YkbZ0Xz5Cr76iv6S2y+fMi8fv/4Y9/KRbz6CJ+q7HwSvXhS8elHw64uClw==",
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
                  "Thu, 30 Jan 2020 17:00:00 GMT"
                ],
                [
                  "Vary",
                  "X-Or-Diff-From-Consensus"
                ],
                [
                  "Date",
                  "Thu, 30 Jan 2020 16:47:38 GMT"
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
                "Date": "Thu, 30 Jan 2020 16:47:38 GMT",
                "Expires": "Thu, 30 Jan 2020 17:00:00 GMT",
                "Vary": "X-Or-Diff-From-Consensus",
                "X-Your-Address-Is": "[REDACTED]"
              }
            },
            "transaction_id": 6
          }
        ],
        "summary": {
          "connect": {
            "failure": null
          }
        },
        "target_address": "45.66.33.45:80",
        "target_name": "dizum",
        "target_protocol": "dir_port",
        "tcp_connect": [
          {
            "conn_id": 20,
            "dial_id": 20,
            "ip": "45.66.33.45",
            "port": 80,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 3.233094,
            "transaction_id": 6
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
            "conn_id": 25,
            "dial_id": 25,
            "failure": null,
            "operation": "connect",
            "proto": "tcp",
            "t": 3.69483
          },
          {
            "conn_id": 25,
            "failure": null,
            "num_bytes": 6819,
            "operation": "write",
            "proto": "tcp",
            "t": 3.695745
          },
          {
            "conn_id": 25,
            "failure": null,
            "num_bytes": 1298,
            "operation": "read",
            "proto": "tcp",
            "t": 3.9642429999999997
          },
          {
            "conn_id": 25,
            "failure": null,
            "num_bytes": 6108,
            "operation": "read",
            "proto": "tcp",
            "t": 3.964713
          }
        ],
        "queries": null,
        "requests": null,
        "summary": {
          "connect": {
            "failure": null
          },
          "handshake": {
            "failure": null
          }
        },
        "target_address": "38.229.33.83:80",
        "target_protocol": "obfs4",
        "tcp_connect": [
          {
            "conn_id": 25,
            "dial_id": 25,
            "ip": "38.229.33.83",
            "port": 80,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 3.69483
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
            "conn_id": 2,
            "dial_id": 1,
            "failure": null,
            "operation": "connect",
            "proto": "tcp",
            "t": 1.042941
          },
          {
            "conn_id": 2,
            "failure": null,
            "num_bytes": 243,
            "operation": "write",
            "proto": "tcp",
            "t": 1.043294
          },
          {
            "conn_id": 2,
            "failure": null,
            "num_bytes": 517,
            "operation": "read",
            "proto": "tcp",
            "t": 1.192781
          },
          {
            "conn_id": 2,
            "failure": null,
            "num_bytes": 490,
            "operation": "read",
            "proto": "tcp",
            "t": 1.192836
          },
          {
            "conn_id": 2,
            "failure": null,
            "num_bytes": 126,
            "operation": "write",
            "proto": "tcp",
            "t": 1.193491
          },
          {
            "conn_id": 2,
            "failure": null,
            "num_bytes": 51,
            "operation": "read",
            "proto": "tcp",
            "t": 1.340602
          },
          {
            "conn_id": 2,
            "failure": null,
            "num_bytes": 31,
            "operation": "write",
            "proto": "tcp",
            "t": 1.340725
          }
        ],
        "queries": null,
        "requests": null,
        "summary": {
          "connect": {
            "failure": null
          },
          "handshake": {
            "failure": null
          }
        },
        "target_address": "66.111.2.131:9001",
        "target_name": "Serge",
        "target_protocol": "or_port_dirauth",
        "tcp_connect": [
          {
            "conn_id": 2,
            "dial_id": 1,
            "ip": "66.111.2.131",
            "port": 9001,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 1.042941
          }
        ],
        "tls_handshakes": [
          {
            "cipher_suite": "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384",
            "conn_id": 2,
            "failure": null,
            "negotiated_protocol": "",
            "peer_certificates": [
              {
                "data": "MIICRTCCAa6gAwIBAgIIb5+niqaBlZUwDQYJKoZIhvcNAQELBQAwJzElMCMGA1UEAwwcd3d3LnF1YTY0cDNkNmhoZmF4azNvbG52LmNvbTAeFw0xOTExMjkwMDAwMDBaFw0yMDAzMDMwMDAwMDBaMB8xHTAbBgNVBAMMFHd3dy5kbmdpZnQzZ2ZlY3AubmV0MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAytTCsU1GqaMVJZyJwX4tzDZb95hckIlT9e1zcnms0Gz3uPRJccp61Z+kTRZv/RUrtdeoNWG7qKmv7hlIg/nop77r2t8SO+m+8Wsd8sEsWClvHpBXnNRS0+qBio7OH0wlnopqb0bGV+ieG/gSuIFB/SwhaIEWyg8YZsDlFexfT380NgDARSDQYh82mcpbglPbul/sAOtFDDeQBCNHCFI4WUc72DM5wQeJrbXTCITsXFiIrVO+nSnm5IwMEvyrLC/k64ddI1p0U1+bEAaVSqrShN7rJPKv22MEuyUhQllTznDLyPINln6+yqZPLQGtItRUoyQF8UnIiCSRi1B6z0u5nQIDAQABMA0GCSqGSIb3DQEBCwUAA4GBAF2WMl1pPMQaiteRN5iHeg2y3JbLH2MMft464pkumtUrbl7bNWLC2317lFVmu7bui6NOASlwO4LuhyFkKGUxZDeoqgCntVehZAgt7tuAD5JEoMKry5tIENsEoJ1vRI9mK0rjNbaYdK1zQq/ytWUNlzmPZKp9KiDJhRVlicOHP61d",
                "format": "base64"
              }
            ],
            "t": 1.34066,
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
                "data": "eNrs/Vdz48i2LQq/r1+Bx/sFu0QgE5Zx1o0DS9CA3t/YsQOeICxhCJK//suEVNUlFNWu+uyWdFZ3FSWxJAqYzMzpxhwjccs6zcMvRWmWVfHl4uZFkCYE/NclLd2XZwk7TQo3KariX98++xK75TF1CCD862JGgfPF9Eo3JwAJyC8k9QWSBMX2SBL9+ZeXu8XxS5WUQfTq37mXf3/++R//Xfj672kZJP4Xx43MGwFJEv/9lx0FblJ+vd6CIJ/gE/PE/fL8kX/5KKCP9BP5xLx8ZJuP1BP4YkbZ0Xz5Cr76iv6S2y+fMi8fv/4Y9/KRbz6CJ+q7HwSvXhS8elHw64uClw==",
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
                  "Thu, 30 Jan 2020 17:00:00 GMT"
                ],
                [
                  "Vary",
                  "X-Or-Diff-From-Consensus"
                ],
                [
                  "Date",
                  "Thu, 30 Jan 2020 16:47:38 GMT"
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
                "Date": "Thu, 30 Jan 2020 16:47:38 GMT",
                "Expires": "Thu, 30 Jan 2020 17:00:00 GMT",
                "Vary": "X-Or-Diff-From-Consensus",
                "X-Your-Address-Is": "[REDACTED]"
              }
            },
            "transaction_id": 7
          }
        ],
        "summary": {
          "connect": {
            "failure": null
          }
        },
        "target_address": "66.111.2.131:9030",
        "target_name": "Serge",
        "target_protocol": "dir_port",
        "tcp_connect": [
          {
            "conn_id": 22,
            "dial_id": 21,
            "ip": "66.111.2.131",
            "port": 9030,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 3.399466,
            "transaction_id": 7
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
            "conn_id": 8,
            "dial_id": 9,
            "failure": null,
            "operation": "connect",
            "proto": "tcp",
            "t": 1.808983
          },
          {
            "conn_id": 8,
            "failure": null,
            "num_bytes": 3516,
            "operation": "write",
            "proto": "tcp",
            "t": 1.8097569999999998
          },
          {
            "conn_id": 8,
            "failure": null,
            "num_bytes": 1440,
            "operation": "read",
            "proto": "tcp",
            "t": 1.866556
          },
          {
            "conn_id": 8,
            "failure": null,
            "num_bytes": 1440,
            "operation": "read",
            "proto": "tcp",
            "t": 1.866841
          },
          {
            "conn_id": 8,
            "failure": null,
            "num_bytes": 68,
            "operation": "read",
            "proto": "tcp",
            "t": 1.8672879999999998
          }
        ],
        "queries": null,
        "requests": null,
        "summary": {
          "connect": {
            "failure": null
          },
          "handshake": {
            "failure": null
          }
        },
        "target_address": "85.31.186.98:443",
        "target_protocol": "obfs4",
        "tcp_connect": [
          {
            "conn_id": 8,
            "dial_id": 9,
            "ip": "85.31.186.98",
            "port": 443,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 1.808983
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
            "conn_id": 18,
            "dial_id": 17,
            "failure": null,
            "operation": "connect",
            "proto": "tcp",
            "t": 3.009771
          },
          {
            "conn_id": 18,
            "failure": null,
            "num_bytes": 5747,
            "operation": "write",
            "proto": "tcp",
            "t": 3.01057
          },
          {
            "conn_id": 18,
            "failure": null,
            "num_bytes": 2596,
            "operation": "read",
            "proto": "tcp",
            "t": 3.320758
          },
          {
            "conn_id": 18,
            "failure": null,
            "num_bytes": 1298,
            "operation": "read",
            "proto": "tcp",
            "t": 3.321211
          },
          {
            "conn_id": 18,
            "failure": null,
            "num_bytes": 1203,
            "operation": "read",
            "proto": "tcp",
            "t": 3.321619
          }
        ],
        "queries": null,
        "requests": null,
        "summary": {
          "connect": {
            "failure": null
          },
          "handshake": {
            "failure": null
          }
        },
        "target_address": "38.229.1.78:80",
        "target_protocol": "obfs4",
        "tcp_connect": [
          {
            "conn_id": 18,
            "dial_id": 17,
            "ip": "38.229.1.78",
            "port": 80,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 3.009771
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
            "conn_id": 32,
            "dial_id": 32,
            "failure": null,
            "operation": "connect",
            "proto": "tcp",
            "t": 4.7872900000000005
          },
          {
            "conn_id": 32,
            "failure": null,
            "num_bytes": 243,
            "operation": "write",
            "proto": "tcp",
            "t": 4.787515
          },
          {
            "conn_id": 32,
            "failure": null,
            "num_bytes": 99,
            "operation": "read",
            "proto": "tcp",
            "t": 4.846764
          },
          {
            "conn_id": 32,
            "failure": null,
            "num_bytes": 6,
            "operation": "write",
            "proto": "tcp",
            "t": 4.846853
          },
          {
            "conn_id": 32,
            "failure": null,
            "num_bytes": 276,
            "operation": "write",
            "proto": "tcp",
            "t": 4.847025
          },
          {
            "conn_id": 32,
            "failure": null,
            "num_bytes": 517,
            "operation": "read",
            "proto": "tcp",
            "t": 4.904098
          },
          {
            "conn_id": 32,
            "failure": null,
            "num_bytes": 643,
            "operation": "read",
            "proto": "tcp",
            "t": 4.904354
          },
          {
            "conn_id": 32,
            "failure": null,
            "num_bytes": 74,
            "operation": "write",
            "proto": "tcp",
            "t": 4.904718
          },
          {
            "conn_id": 32,
            "failure": null,
            "num_bytes": 24,
            "operation": "write",
            "proto": "tcp",
            "t": 4.904799
          }
        ],
        "queries": null,
        "requests": null,
        "summary": {
          "connect": {
            "failure": null
          },
          "handshake": {
            "failure": null
          }
        },
        "target_address": "86.59.21.38:443",
        "target_name": "tor26",
        "target_protocol": "or_port_dirauth",
        "tcp_connect": [
          {
            "conn_id": 32,
            "dial_id": 32,
            "ip": "86.59.21.38",
            "port": 443,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 4.7872900000000005
          }
        ],
        "tls_handshakes": [
          {
            "cipher_suite": "TLS_AES_256_GCM_SHA384",
            "conn_id": 32,
            "failure": null,
            "negotiated_protocol": "",
            "peer_certificates": [
              {
                "data": "MIICPTCCAaagAwIBAgIIBQXYCKLPwLwwDQYJKoZIhvcNAQELBQAwHTEbMBkGA1UEAwwSd3d3LjdoM2hiYTNlb2kuY29tMB4XDTE5MTExMDAwMDAwMFoXDTIwMDIxNjIzNTk1OVowITEfMB0GA1UEAwwWd3d3Lmhxdndwdnl1eXVsZGw1Lm5ldDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAMIoJjnE2Z1nykFKoGHAcwrbwywOTKIxaF+0BkPWESCz+0COBG41AR0wPU4USI0ITAksm6DgNj6ldVjn0VDuJC4HiJw8dOFAqB4IMI0mJpPmF/GsHgvCLFk7aaH3E+6xCt/HEZeqr8DDt/pdf0OvbEsEbk/iaxqBIbZ+N0PeRvkrry41niopApNS/8jX7KrweSaDW++EM/YoA6AODC0UkoHfjKOEw65wpknE4smexPlqaRTExqY+wj87RYlROU3umA4vX/5Dgd9Ce6s+hxYLfp+71jpyVym/uIvwj1lHmg9hFSAw8BhL+75wgcmj2Ydnjz/TLX9zJtWzBQv7exX5eFkCAwEAATANBgkqhkiG9w0BAQsFAAOBgQAzKZNBPg8/TZk+3qFc5qzqBXnQlMSlSR21kzjTcfznue7wa/0/v6w89fex/5pFxqfc+n//3x1Kb0clXHv1f2V+myg5trRToE/Ul6RoH9noo7fbfoEVKUVNdX060nsFEkGxP+DMyun8XlMQ1IPjao6yGeGPB02+sIa1ZZ3Pnzv/rQ==",
                "format": "base64"
              }
            ],
            "t": 4.904739,
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
                "data": "eNrs/Vdz48i2LQq/r1+Bx/sFu0QgE5Zx1o0DS9CA3t/YsQOeICxhCJK//suEVNUlFNWu+uyWdFZ3FSWxJAqYzMzpxhwjccs6zcMvRWmWVfHl4uZFkCYE/NclLd2XZwk7TQo3KariX98++xK75TF1CCD862JGgfPF9Eo3JwAJyC8k9QWSBMX2SBL9+ZeXu8XxS5WUQfTq37mXf3/++R//Xfj672kZJP4Xx43MGwFJEv/9lx0FblJ+vd6CIJ/gE/PE/fL8kX/5KKCP9BP5xLx8ZJuP1BP4YkbZ0Xz5Cr76iv6S2y+fMi8fv/4Y9/KRbz6CJ+q7HwSvXhS8elHw64uClw==",
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
                  "Thu, 30 Jan 2020 17:00:00 GMT"
                ],
                [
                  "Vary",
                  "X-Or-Diff-From-Consensus"
                ],
                [
                  "Date",
                  "Thu, 30 Jan 2020 16:47:36 GMT"
                ],
                [
                  "Content-Type",
                  "text/plain"
                ]
              ],
              "headers": {
                "Content-Encoding": "deflate",
                "Content-Type": "text/plain",
                "Date": "Thu, 30 Jan 2020 16:47:36 GMT",
                "Expires": "Thu, 30 Jan 2020 17:00:00 GMT",
                "Vary": "X-Or-Diff-From-Consensus",
                "X-Your-Address-Is": "[REDACTED]"
              }
            },
            "transaction_id": 2
          }
        ],
        "summary": {
          "connect": {
            "failure": null
          }
        },
        "target_address": "86.59.21.38:80",
        "target_name": "tor26",
        "target_protocol": "dir_port",
        "tcp_connect": [
          {
            "conn_id": 4,
            "dial_id": 4,
            "ip": "86.59.21.38",
            "port": 80,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 1.231164,
            "transaction_id": 2
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
            "conn_id": 13,
            "dial_id": 13,
            "failure": null,
            "operation": "connect",
            "proto": "tcp",
            "t": 2.324393
          },
          {
            "conn_id": 13,
            "failure": null,
            "num_bytes": 4255,
            "operation": "write",
            "proto": "tcp",
            "t": 2.325227
          },
          {
            "conn_id": 13,
            "failure": null,
            "num_bytes": 1452,
            "operation": "read",
            "proto": "tcp",
            "t": 2.383437
          },
          {
            "conn_id": 13,
            "failure": null,
            "num_bytes": 1452,
            "operation": "read",
            "proto": "tcp",
            "t": 2.383714
          },
          {
            "conn_id": 13,
            "failure": null,
            "num_bytes": 1452,
            "operation": "read",
            "proto": "tcp",
            "t": 2.384238
          },
          {
            "conn_id": 13,
            "failure": null,
            "num_bytes": 196,
            "operation": "read",
            "proto": "tcp",
            "t": 2.384409
          }
        ],
        "queries": null,
        "requests": null,
        "summary": {
          "connect": {
            "failure": null
          },
          "handshake": {
            "failure": null
          }
        },
        "target_address": "193.11.166.194:27025",
        "target_protocol": "obfs4",
        "tcp_connect": [
          {
            "conn_id": 13,
            "dial_id": 13,
            "ip": "193.11.166.194",
            "port": 27025,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 2.324393
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
            "conn_id": 30,
            "dial_id": 30,
            "failure": null,
            "operation": "connect",
            "proto": "tcp",
            "t": 4.54028
          },
          {
            "conn_id": 30,
            "failure": null,
            "num_bytes": 5160,
            "operation": "write",
            "proto": "tcp",
            "t": 4.541231
          },
          {
            "conn_id": 30,
            "failure": null,
            "num_bytes": 2880,
            "operation": "read",
            "proto": "tcp",
            "t": 4.8166080000000004
          },
          {
            "conn_id": 30,
            "failure": null,
            "num_bytes": 1358,
            "operation": "read",
            "proto": "tcp",
            "t": 4.816876
          }
        ],
        "queries": null,
        "requests": null,
        "summary": {
          "connect": {
            "failure": null
          },
          "handshake": {
            "failure": null
          }
        },
        "target_address": "146.57.248.225:22",
        "target_protocol": "obfs4",
        "tcp_connect": [
          {
            "conn_id": 30,
            "dial_id": 30,
            "ip": "146.57.248.225",
            "port": 22,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 4.54028
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
            "conn_id": 26,
            "dial_id": 26,
            "failure": null,
            "operation": "connect",
            "proto": "tcp",
            "t": 3.968303
          },
          {
            "conn_id": 26,
            "failure": null,
            "num_bytes": 5219,
            "operation": "write",
            "proto": "tcp",
            "t": 3.969056
          },
          {
            "conn_id": 26,
            "failure": null,
            "num_bytes": 890,
            "operation": "read",
            "proto": "tcp",
            "t": 4.321937
          }
        ],
        "queries": null,
        "requests": null,
        "summary": {
          "connect": {
            "failure": null
          },
          "handshake": {
            "failure": null
          }
        },
        "target_address": "216.252.162.21:46089",
        "target_protocol": "obfs4",
        "tcp_connect": [
          {
            "conn_id": 26,
            "dial_id": 26,
            "ip": "216.252.162.21",
            "port": 46089,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 3.968303
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
            "conn_id": 19,
            "dial_id": 19,
            "failure": null,
            "operation": "connect",
            "proto": "tcp",
            "t": 3.070482
          },
          {
            "conn_id": 19,
            "failure": null,
            "num_bytes": 2184,
            "operation": "write",
            "proto": "tcp",
            "t": 3.071232
          },
          {
            "conn_id": 19,
            "failure": null,
            "num_bytes": 1440,
            "operation": "read",
            "proto": "tcp",
            "t": 3.190934
          },
          {
            "conn_id": 19,
            "failure": null,
            "num_bytes": 1440,
            "operation": "read",
            "proto": "tcp",
            "t": 3.191215
          },
          {
            "conn_id": 19,
            "failure": null,
            "num_bytes": 1430,
            "operation": "read",
            "proto": "tcp",
            "t": 3.191769
          }
        ],
        "queries": null,
        "requests": null,
        "summary": {
          "connect": {
            "failure": null
          },
          "handshake": {
            "failure": null
          }
        },
        "target_address": "209.148.46.65:443",
        "target_protocol": "obfs4",
        "tcp_connect": [
          {
            "conn_id": 19,
            "dial_id": 19,
            "ip": "209.148.46.65",
            "port": 443,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 3.070482
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
            "conn_id": 29,
            "dial_id": 29,
            "failure": null,
            "operation": "connect",
            "proto": "tcp",
            "t": 4.386795
          },
          {
            "conn_id": 29,
            "failure": null,
            "num_bytes": 8173,
            "operation": "write",
            "proto": "tcp",
            "t": 4.387676
          },
          {
            "conn_id": 29,
            "failure": null,
            "num_bytes": 2349,
            "operation": "read",
            "proto": "tcp",
            "t": 4.50394
          }
        ],
        "queries": null,
        "requests": null,
        "summary": {
          "connect": {
            "failure": null
          },
          "handshake": {
            "failure": null
          }
        },
        "target_address": "85.31.186.26:443",
        "target_protocol": "obfs4",
        "tcp_connect": [
          {
            "conn_id": 29,
            "dial_id": 29,
            "ip": "85.31.186.26",
            "port": 443,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 4.386795
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
            "conn_id": 28,
            "dial_id": 28,
            "failure": null,
            "operation": "connect",
            "proto": "tcp",
            "t": 4.268109
          },
          {
            "conn_id": 28,
            "failure": null,
            "num_bytes": 4113,
            "operation": "write",
            "proto": "tcp",
            "t": 4.269258
          },
          {
            "conn_id": 28,
            "failure": null,
            "num_bytes": 2880,
            "operation": "read",
            "proto": "tcp",
            "t": 4.399888
          },
          {
            "conn_id": 28,
            "failure": null,
            "num_bytes": 1440,
            "operation": "read",
            "proto": "tcp",
            "t": 4.400182
          },
          {
            "conn_id": 28,
            "failure": null,
            "num_bytes": 1440,
            "operation": "read",
            "proto": "tcp",
            "t": 4.400416
          },
          {
            "conn_id": 28,
            "failure": null,
            "num_bytes": 619,
            "operation": "read",
            "proto": "tcp",
            "t": 4.401291
          }
        ],
        "queries": null,
        "requests": null,
        "summary": {
          "connect": {
            "failure": null
          },
          "handshake": {
            "failure": null
          }
        },
        "target_address": "192.95.36.142:443",
        "target_protocol": "obfs4",
        "tcp_connect": [
          {
            "conn_id": 28,
            "dial_id": 28,
            "ip": "192.95.36.142",
            "port": 443,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 4.268109
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
            "conn_id": 34,
            "dial_id": 34,
            "failure": null,
            "operation": "connect",
            "proto": "tcp",
            "t": 5.035145
          },
          {
            "conn_id": 34,
            "failure": null,
            "num_bytes": 5502,
            "operation": "write",
            "proto": "tcp",
            "t": 5.035973
          },
          {
            "conn_id": 34,
            "failure": null,
            "num_bytes": 1440,
            "operation": "read",
            "proto": "tcp",
            "t": 5.293956
          },
          {
            "conn_id": 34,
            "failure": null,
            "num_bytes": 1440,
            "operation": "read",
            "proto": "tcp",
            "t": 5.294148
          },
          {
            "conn_id": 34,
            "failure": null,
            "num_bytes": 1309,
            "operation": "read",
            "proto": "tcp",
            "t": 5.294498
          }
        ],
        "queries": null,
        "requests": null,
        "summary": {
          "connect": {
            "failure": null
          },
          "handshake": {
            "failure": null
          }
        },
        "target_address": "144.217.20.138:80",
        "target_protocol": "obfs4",
        "tcp_connect": [
          {
            "conn_id": 34,
            "dial_id": 34,
            "ip": "144.217.20.138",
            "port": 80,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 5.035145
          }
        ],
        "tls_handshakes": null
      }
    }
  },
  "test_name": "tor",
  "test_start_time": "2020-01-30 16:47:33",
  "test_version": "0.1.0"
}
```

# Privacy considerations

This nettest does not provide anonymity. An adversary can observe that
the user is connecting to Tor servers and using obfs4.

Whenever a target refers to a private bridge, the implementation MUST scrub
the target address (with optional endpoint) from the measurement and from the
logs. For example, the following:

```JSON
{
	"network_events": [
	  {
		"address": "85.31.186.98:443",
		"conn_id": 19,
		"dial_id": 21,
		"failure": null,
		"operation": "connect",
		"proto": "tcp",
		"t": 8.639313
	  }
	],
	"target_address": "85.31.186.98:443",
	"tcp_connect": [
	  {
		"conn_id": 19,
		"dial_id": 21,
		"ip": "85.31.186.98",
		"port": 443,
		"status": {
		  "failure": null,
		  "success": true
		},
		"t": 8.639313
	  }
	]
}
```

MUST be scrubbed as:

```JSON
{
	"network_events": [
	  {
		"address": "[scrubbed]",
		"conn_id": 19,
		"dial_id": 21,
		"failure": null,
		"operation": "connect",
		"proto": "tcp",
		"t": 8.639313
	  }
	],
	"target_address": "[scrubbed]",
	"tcp_connect": [
	  {
		"conn_id": 19,
		"dial_id": 21,
		"ip": "[scrubbed]",
		"port": 443,
		"status": {
		  "failure": null,
		  "success": true
		},
		"t": 8.639313
	  }
	]
}
```

The scrubbing procedure SHOULD only be applied to the specific
results referring to private bridges. It SHOULD NOT be applied to
other results referring to non-private bridges.

# Packet capture considerations

This test does not capture packets by default.

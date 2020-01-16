# Specification version number

2020-01-16-001

# Specification name

Tor

# Test preconditions

None

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
    "params": {},
    "protocol": ""
  }
}
```

- `id` (`string`): the unique identifier of the target chosen
by who generated the input targets.

- `address` (`string`): the address of the target.

- `fingerprint` (`string`; optional): the fingerprint, if applicable.

- `params` (`map[string][]string`; optional): extra parameters,
e.g., to configure `obfs4`.

- `protocol` (`string`): the protocol to use with the
target (e.g. `obfs4`).

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
    "protocol": "or_port"
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

- for `or_port` targets, the nettest will connect to
the address and perform a TLS handshake;

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
        "targets": {
          "<targetId>": {}
        }
    }
}
```

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

- `target_protocol` (`string`): protocol to access the target;

- `tcp_connect` (`[]TCPConnect`; nullable): see `df-005-tcpconnect`;

- `tls_handshakes` (`[]Handshake`; nullable): see `df-006-tlshandshake`.

## Parent data format

See the above fields description.

## Required output data

Fields described above (mind that many are nullable).

## Possible conclusions

For each resource, we determine whether it was working or not by
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
  "measurement_start_time": "2020-01-16 15:12:30",
  "test_runtime": 0.767114298,
  "probe_asn": "AS30722",
  "probe_cc": "IT",
  "probe_ip": "127.0.0.1",
  "report_id": "20200116T151230Z_AS30722_bASaI9Siy5BjUnjAm6pjtdUpgXG9mspLBYs8L4Zt5AGQgmBLXh",
  "resolver_asn": "AS15169",
  "resolver_ip": "173.194.169.6",
  "resolver_network_name": "Google LLC",
  "software_name": "miniooni",
  "software_version": "0.1.0-dev",
  "test_keys": {
    "targets": {
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
            "t": 0.152448
          },
          {
            "conn_id": 2,
            "failure": null,
            "num_bytes": 243,
            "operation": "write",
            "proto": "tcp",
            "t": 0.15295
          },
          {
            "conn_id": 2,
            "failure": null,
            "num_bytes": 517,
            "operation": "read",
            "proto": "tcp",
            "t": 0.331539
          },
          {
            "conn_id": 2,
            "failure": null,
            "num_bytes": 488,
            "operation": "read",
            "proto": "tcp",
            "t": 0.331618
          },
          {
            "conn_id": 2,
            "failure": null,
            "num_bytes": 126,
            "operation": "write",
            "proto": "tcp",
            "t": 0.332482
          },
          {
            "conn_id": 2,
            "failure": null,
            "num_bytes": 51,
            "operation": "read",
            "proto": "tcp",
            "t": 0.46302
          },
          {
            "conn_id": 2,
            "failure": null,
            "num_bytes": 31,
            "operation": "write",
            "proto": "tcp",
            "t": 0.463199
          }
        ],
        "queries": null,
        "requests": null,
        "target_address": "66.111.2.131:9001",
        "target_protocol": "or_port",
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
            "t": 0.152448
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
                "data": "MIICQzCCAaygAwIBAgIJANpzUuufk+geMA0GCSqGSIb3DQEBCwUAMCUxIzAhBgNVBAMMGnd3dy42a2EzaGMzeGkzdXZmNWdxdnQuY29tMB4XDTE5MTIxMjAwMDAwMFoXDTIwMDIwOTAwMDAwMFowHjEcMBoGA1UEAwwTd3d3Lmd1bWthbnVrY2RtLm5ldDCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAL+NpfyU9BNKErPGHy1xE3MDptUfaWOfc1N0tI00T2tVui4RtIOv9bKWQW7wiaI89NtjG7TRSYicN1r2XfNfnqaotMLC4PDXIlWA0I4lsARDW13XE93OS8qSRXj3T72JxSXLqGK/fq9w2AR0VRERLTa/v76r0S8vLp+juFuXe5JVWyMwvSQ92b6q1QIhCGWNtQZdjt0HE3tBUqthat7wdxkDifVGlYR98CLEoVj1U3dy1uhaFXoYO8UW2caW0/A2LfVZWU7ImsxWFbhHS1xEdH2twRk7rfa6hX8Ar7g7tivqbO7RWFgJYvl5UqAev64kJuGLuoa6SFtJAZJZ8f1g+4ECAwEAATANBgkqhkiG9w0BAQsFAAOBgQC78diBdHYB6KXLP8y04pk9yirEkO2hX4AfA3HUZYe5CAr8nXIthbIcisEouHnoCNOGfWBFiXhDf0bMXwLRLDWyLdm+HRQnXuryCcXEeoxcAJkEBqnksmwraezW/XlezzxdCFohKffZYHH72j7gYJp9UWqbJisOOs6rnR00Al6MvQ==",
                "format": "base64"
              }
            ],
            "t": 0.463109,
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
                "data": "eNrs/Wdz48i2LYp+X78CH98LdolIJCxjrxsHjh40oAVf7NgBTxCWMATJX/8yIVV1CUW1qz67Jd3VXUVJLIkCJjNzujHHSNyyTvPwS1GaZVV8ubh5EaQJAf91SUv35VnCTpPCTYqq+Ne3z77EbnlMHYIS/nUxo8D5YnqlmxMUSZFfSPAFsASgeySJ/vzLy93i+KVKyiB69e/My78///yP/859/fe0DBL/i+NG5o2AJIn//suOAjcpv15vQZBP8Il54n55/si/fBTQR/qJfGJePrLNR/BEfTGj7Gi+fAVffUV/ye2XT5mXj19/jHv5yDcfqSfw3Q9Sr16UevWi1K8vSr28KPXyovDri/yrcHN0N+07+oh3EiZpnXzxItMvCLFCyyQPyhshmY56DUqieeibRUkMKjN3iOFKCXJilqqO/HVxEXqVJOg9J1alaUUu/hC5ilvYxJbC37zFK+ZfuWuncewmjut8eVkOWZ6WqZ1GBYFf69/gC0XgH3v+JMhl0z66/wbPv7L5OErKPP03RJ/p6IXQU9MgCf9NE1pg56nz9Ud1vPT+Tb36jTl+7v/+LzxXQf6/eH8vv+7xzb38rj/zm+CXV7/r5Teh3/mvzMzNGL1ykNtVUC7yoFklQzPyosBztcK1/432OdrtSrp6+SY5d80S7Q01wasC/w78b2mSuPZvPK2ZV/SFXeU5sqCconPm30zzqrrrVYW7QusscodpJjcmxhfv3i9phe93VsXo9tDLpPmtWawFukH0pIru9esTzXfN1mleLNx8LS7+DdA1r6osS/OSpKhh4DhuskJ7O7Dd4t8ksSlc/N1DM3GKoxliI6Kn5lkZxEFRBrZiliZ6zqpNtHOyAN+ObZWlW5ToHD2jVyeOxf8Uz6/3P7F5/Z/cufyPZwZRhY5Z9M3Hwgny/ykyZCvnfwp05S56uzPrf5ygwObJ7BJdBNpmTuz+jxsH5f/EQfI/L4cO+nFkERub2fXQDv03+S90jc2CQJf75cWGX9CBXbmEQNghrQ3WziRO+7tw2pedvWqcKP6cMCI1vZfW5Gas0nUCT0fy3/9CV/WlSKvcdgnHRO9NYrm5T5AUpMS+QAIZApGkVVXgaZ4RGPScJHEsRSq0zEiU+t3PPKF7wrZ5clwCCPCJQn9oGv8leJKgaYidVGnaJSEmDrqVgpi6x8TNnz2aE/jIlIQisFxfpOk+L1AK4ChOhiJQVK7PCGKfAiTD0EKfZ+TvLxv9Xgq7NRlAoPRlRmb7AmRpVlI5qi8CGt0ESYm80qdUXkIXwz4xwhOFDmX+9eevL3LhYr+5QOs+N53WVUoyy8mKoEiAlhiK4mmRB7BPyhL6xbLclyUB0DQvMN9fZZQmvh2ZNQ==",
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
                  "Cache-Control",
                  "no-cache"
                ],
                [
                  "Date",
                  "Thu, 16 Jan 2020 15:12:31 GMT"
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
                  "Pragma",
                  "no-cache"
                ]
              ],
              "headers": {
                "Cache-Control": "no-cache",
                "Content-Encoding": "deflate",
                "Content-Type": "text/plain",
                "Date": "Thu, 16 Jan 2020 15:12:31 GMT",
                "Pragma": "no-cache",
                "Vary": "X-Or-Diff-From-Consensus",
                "X-Your-Address-Is": "[REDACTED]"
              }
            },
            "transaction_id": 1
          }
        ],
        "target_address": "66.111.2.131:9030",
        "target_protocol": "dir_port",
        "tcp_connect": [
          {
            "conn_id": 1,
            "dial_id": 2,
            "ip": "66.111.2.131",
            "port": 9030,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 0.152408,
            "transaction_id": 1
          }
        ],
        "tls_handshakes": null
      },
      "f372c264e9a470335d9ac79fe780847bda052aa3b6a9ee5ff497cb6501634f9f": {
        "agent": "redirect",
        "failure": null,
        "network_events": [
          {
            "address": "38.229.1.78:80",
            "conn_id": 3,
            "dial_id": 3,
            "failure": null,
            "operation": "connect",
            "proto": "tcp",
            "t": 0.462918
          },
          {
            "conn_id": 3,
            "failure": null,
            "num_bytes": 5415,
            "operation": "write",
            "proto": "tcp",
            "t": 0.464379
          },
          {
            "conn_id": 3,
            "failure": null,
            "num_bytes": 1298,
            "operation": "read",
            "proto": "tcp",
            "t": 0.764535
          },
          {
            "conn_id": 3,
            "failure": null,
            "num_bytes": 2596,
            "operation": "read",
            "proto": "tcp",
            "t": 0.765818
          },
          {
            "conn_id": 3,
            "failure": null,
            "num_bytes": 2596,
            "operation": "read",
            "proto": "tcp",
            "t": 0.766056
          },
          {
            "conn_id": 3,
            "failure": null,
            "num_bytes": 816,
            "operation": "read",
            "proto": "tcp",
            "t": 0.766316
          }
        ],
        "queries": null,
        "requests": null,
        "target_address": "38.229.1.78:80",
        "target_protocol": "obfs4",
        "tcp_connect": [
          {
            "conn_id": 3,
            "dial_id": 3,
            "ip": "38.229.1.78",
            "port": 80,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 0.462918
          }
        ],
        "tls_handshakes": null
      }
    }
  },
  "test_name": "tor",
  "test_start_time": "2020-01-16 15:12:30",
  "test_version": "0.0.1"
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

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
    "params": {},
    "protocol": ""
  }
}

```

- `id` (`string`): the unique identifier of the target. For
bridges, this is the `sha256` of the fingerprint. A future
version of this specification will document how to compute the
`id` for other kind of input targets.

- `address` (`string`): the address of the target.

- `params` (`map[string][]string`; optional): extra parameters
to be used with the target (e.g. to configure `obfs4`).

- `protocol` (`string`): the protocol to use with the target. See
below for a description of how this field is handled.

The following is a valid example:

```JSON
{
  "f372c264e9a470335d9ac79fe780847bda052aa3b6a9ee5ff497cb6501634f9f": {
    "address": "38.229.1.78:80",
    "params": {
      "cert": [
        "Hmyfd2ev46gGY7NoVxA9ngrPF2zCZtzskRTzoWXbxNkzeVnGFPWmrTtILRyqCTjHR+s9dg"
      ],
      "iat-mode": [
        "1"
     ],
  }
}
```

When fetching the targets from OONI orchestra, the experiment MUST
ensure that either said targets are not logged, or they are sanitized
before being logged. This is useful to avoid inadvertently leaking
bridge addresses when logs are posted on public forums.

This experiment currently does not handle input formatted as a Tor
bridge line. A future version of this specification will handle this
specific use case.

# Test description

The test loops through the list of targets measuring each. The
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
perform the data sanitization steps described below.

# Expected output

```JSON
{
    "test_keys": {
        "targets": {}
    }
}
```

- `targets` (`map[string]Targets`): measurements by target where
the key is the `id` of the target, as described above.

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

- `target_protocol` (`string`): protocol to access the target, which
determines the action performed as described above;

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
  "measurement_start_time": "2020-01-12 10:32:46",
  "test_runtime": 3.267954277,
  "probe_asn": "AS30722",
  "probe_cc": "IT",
  "probe_ip": "127.0.0.1",
  "report_id": "20200112T103246Z_AS30722_YppBch5h3LxXgjFZ9ziVcQX89udUIcRFVbH5ar375mipxVlJVz",
  "resolver_asn": "AS15169",
  "resolver_ip": "172.253.197.2",
  "resolver_network_name": "Google LLC",
  "software_name": "miniooni",
  "software_version": "0.1.0-dev",
  "test_keys": {
    "targets": [
      {
        "agent": "redirect",
        "failure": null,
        "network_events": [
          {
            "address": "109.105.109.165:10527",
            "conn_id": 2,
            "dial_id": 2,
            "failure": null,
            "operation": "connect",
            "proto": "tcp",
            "t": 1.492101
          },
          {
            "conn_id": 2,
            "failure": null,
            "num_bytes": 3465,
            "operation": "write",
            "proto": "tcp",
            "t": 1.498227
          },
          {
            "conn_id": 2,
            "failure": null,
            "num_bytes": 2880,
            "operation": "read",
            "proto": "tcp",
            "t": 1.559525
          },
          {
            "conn_id": 2,
            "failure": null,
            "num_bytes": 1348,
            "operation": "read",
            "proto": "tcp",
            "t": 1.559858
          }
        ],
        "queries": null,
        "requests": null,
        "target_address": "109.105.109.165:10527",
        "target_protocol": "obfs4",
        "tcp_connect": [
          {
            "conn_id": 2,
            "dial_id": 2,
            "ip": "109.105.109.165",
            "port": 10527,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 1.492101
          }
        ],
        "tls_handshakes": null
      },
      {
        "agent": "redirect",
        "failure": null,
        "network_events": [
          {
            "address": "66.111.2.131:9001",
            "conn_id": 1,
            "dial_id": 1,
            "failure": null,
            "operation": "connect",
            "proto": "tcp",
            "t": 1.433779
          },
          {
            "conn_id": 1,
            "failure": null,
            "num_bytes": 243,
            "operation": "write",
            "proto": "tcp",
            "t": 1.434547
          },
          {
            "conn_id": 1,
            "failure": null,
            "num_bytes": 517,
            "operation": "read",
            "proto": "tcp",
            "t": 1.567884
          },
          {
            "conn_id": 1,
            "failure": null,
            "num_bytes": 489,
            "operation": "read",
            "proto": "tcp",
            "t": 1.5682779999999998
          },
          {
            "conn_id": 1,
            "failure": null,
            "num_bytes": 126,
            "operation": "write",
            "proto": "tcp",
            "t": 1.570798
          },
          {
            "conn_id": 1,
            "failure": null,
            "num_bytes": 51,
            "operation": "read",
            "proto": "tcp",
            "t": 1.691703
          },
          {
            "conn_id": 1,
            "failure": null,
            "num_bytes": 31,
            "operation": "write",
            "proto": "tcp",
            "t": 1.692134
          }
        ],
        "queries": null,
        "requests": null,
        "target_address": "66.111.2.131:9001",
        "target_protocol": "or_port",
        "tcp_connect": [
          {
            "conn_id": 1,
            "dial_id": 1,
            "ip": "66.111.2.131",
            "port": 9001,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 1.433779
          }
        ],
        "tls_handshakes": [
          {
            "cipher_suite": "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384",
            "conn_id": 1,
            "failure": null,
            "negotiated_protocol": "",
            "peer_certificates": [
              {
                "data": "MIICRDCCAa2gAwIBAgIJAKeJmASdShrvMA0GCSqGSIb3DQEBCwUAMCAxHjAcBgNVBAMMFXd3dy5xam92Z3doaGZ6MjQ3LmNvbTAeFw0xOTExMDMwMDAwMDBaFw0yMDEwMzAyMzU5NTlaMCQxIjAgBgNVBAMMGXd3dy5mcG5zYzJ3YWppYnRvbGVwMy5uZXQwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQD2ak9tV/LhT1KbHSVm7VfSLLOHiX4oskD9DmYS4fgTgY/6VLwwzqunkZ1jHhkyTvCczEc3uoZMY0npyeiRRrNFqG24QkQqcoHqQa6E53VUGK/jomzIGoLmXp48LrJe9DqCal5xaOao0+YRiQHRzTR0T6w2DP+ESO1yMon12hSUrHOd/7/+VeaCqvBgZ9Lb3dnj/9zVpWYhr1yJYzLY5qTZMoDGGbk0ad9mlbhtL7qhZnStPccRmxo2Rq6vIowE8K0fzBrl/s4j5ZnO+tMgPxcWy/NHy4IvMEalDm6Gw9hlc9lXA0YaEhK9qY/DzeVMmNxFnuOQmIS72irCCOaElr1rAgMBAAEwDQYJKoZIhvcNAQELBQADgYEAWpzW1f4qnmxMqAdgt2jxg+cCxUfVBATxHZZqnFnp8j7tnTok+zRbgT8/wGZmQCDQgmK2kGQ309jm9qwXGNyojsg1hjkhuqECTKKEvqyw/5N4MnMriHB3DZVk46LnYVSSlv3Oi6QKA/klN2kTNhz1kVwRfPP79YON57elRvX6P38=",
                "format": "base64"
              }
            ],
            "t": 1.691995,
            "tls_version": "TLSv1.2"
          }
        ]
      },
      {
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
                  "66.111.2.131:9030"
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
                "data": "eNrs/Wl34si2NYx+379CH+8dVBpFqGec/Y5HHSBAiL6744wz1EuoRQ3dr78RsjMrrcTVZT2nbL+7KhPbJGC0iFixmrnmTN3qkhXRl7Iyq7r8cnaLMsxSgvrXOavcl3sJO0tLNy3r8l/fvvuSuFWQOQQU/nU249D5YnqVWxCQhOQXEnwBkABkj8R//uUVbhl8qdMqjF/9O3j59+fn//jv1Nd/z6ow9b84bmzeCIok8d9/2XHoptXX91sS5BP1xDxxvzx/5V++Cugr/UQ+MS9f2eYreIJfzDgPzJefqFc/0V8K++Vb5uXr16dxL1/55it8At89Eb56UfjqReGvLwpfXhS+vCj19UX+VboFupr2FX3EK4nS7JJ+8WLTLwmxRsukCKsbIZmOeg0rornpm2VFDGqzcIjhUgkLYpqpjvx1cRGLOk3RZ04sK9OKXfwldhW3tIkNxA/e4BXzr8K1syRxU8d1vrwsh7zIqszO4pLAr/Vv8AUS+GnP34SFbNqB+2/w/Cubr1paFdm/KfTdAr0QumsSptG/aUIP7SJzvj51gZfev+Gr31jg+/7v/8JTHRb/i9f38useX9zL7/ozv4n68up3vfwm9Dv/lZuFmaBXDgu7DqtZETarZGjGXhx6rl669r/RPke7XcmWLw+SC9es0N5QU7wq8O/A/5alqWv/xt26eUU/2HVRIAvKGfIz/2aaV124Xl26S7TOYneY5XJjYvzm3fs5q/H1TusEXR56may4NYu1RBeI7lTRtX69o3nUdJUV5cwtVuLs3wC952Wd51lRkRAOQ8dx0yXa26Htlv8miXXp4kcPzdQpAzPCRkR3GXkVJmFZhbZiVia6z7qYaOfkIb4c26oqt6yQHz2hVyeC8n/K59f7n8S8/k/hnP/HM8O4Rm4WPTgonbD4nzJHtnL+p0Tv3EUfd279jxOW2Dy5XaE3gbaZk7j/4yZh9T9JmP7Pi9NBT0cWsbGZXQ/t0H+T/0LvsVkQ6O2i9eCewwyfEmZcu4RAXAS5vA25amWMqLtXTinvMAo9jrmbahJ5p2B7jcIsVkXjfvn3q1d6+TS+vRB9nmSTwXw5IfnxROTPjNrR9pPMnKVdfzdl9CSiwWQ81YUJ/e9/oev7UmZ1YbuEY6JPObXcwidISEGxL5BApoBI0qoq8DTPCAy6T5I4FpIKLTMSVL97zhOyDrbyk+MSQKCeIPpD0/gvwZMETVP4uKtMuyLE1EFGKYmJG6Ru8Xw2OqGPPhSCFmWFUdGvkQRG6As816f7fYVTGElRJE4WSInmWJ5Wv3/b6PdClgC0DCig9GVGZvsCxdKspHKwLwIaXQQJRV7pQ5WX0JthnxjhCSL3zr/+/vWbnLn4BJ6hHQ==",
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
                  "Sun, 12 Jan 2020 11:00:00 GMT"
                ],
                [
                  "Vary",
                  "X-Or-Diff-From-Consensus"
                ],
                [
                  "Date",
                  "Sun, 12 Jan 2020 10:32:49 GMT"
                ],
                [
                  "Content-Type",
                  "text/plain"
                ]
              ],
              "headers": {
                "Content-Encoding": "deflate",
                "Content-Type": "text/plain",
                "Date": "Sun, 12 Jan 2020 10:32:49 GMT",
                "Expires": "Sun, 12 Jan 2020 11:00:00 GMT",
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
            "conn_id": 3,
            "dial_id": 3,
            "ip": "66.111.2.131",
            "port": 9030,
            "status": {
              "failure": null,
              "success": true
            },
            "t": 3.148084,
            "transaction_id": 1
          }
        ],
        "tls_handshakes": null
      }
    ]
  },
  "test_name": "tor",
  "test_start_time": "2020-01-12 10:32:46",
  "test_version": "0.0.1"
}
```

# Privacy considerations

This nettest does not provide anonymity. An adversary can observe that
the user is connecting to Tor servers and using obfs4.

A future version of this specification should describe how to handle the
case where the target bridges are not public.

# Packet capture considerations

This test does not capture packets by default.

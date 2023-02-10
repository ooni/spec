# Specification version number

2023-02-10

* _status_: experimental.

# Specification name

`openvpn`

# Test preconditions

* An internet connection

# Expected impact

The ability to detect if a working OpenVPN connection can be established with a given host.

# Expected inputs

There are two categories of input to this experiment. Some of them are given as
part of the input `URI` for the experiment, and some others are passed as
options.

Altogether, they constitute a basic subset of the valid configuration
parameters for the reference openvpn implementation (`man 8 openvpn`).

## Input URI

The input `URI` encodes information for the protocol (`openvpn`, in this case),
provider, transport, obfuscation and the remote address.

```
vpn://{provider_name}.{protocol}/?transport=tcp&obfuscation=obfs4&address={ip}:{port}
```

Where:

- `provider` (`string`) is the entity that manages the endpoints. If it's not a
  provider known to OONI, it should be marked with a prefix starting with
  "unknown".
- `vpn_protocol` (`string`): should be `openvpn`.
- `transport` (`string`): underlying transport used by OpenVPN, one of `tcp|udp`.
- `remote` (`string`): IP address and port for the remote endpoint (`ipaddr:port`).
- `obfuscation` (`string`): type of obfuscation in use. Currently known
  obfuscation schemes include `none` and `obfs4`.


## Inline credentials (certificate-based)

For certificate-based authentication, the credentials to authenticate against
the tunnel endpoint need to be passed as an `options` object that will be
passed to the experiment, encoded as a base64 string.

For credentials, we use the `Safe` prefix to signal to the engine that we don't want those
options to be exported and indexed by the OONI backend:

```
"SafeCa": "base64:deadbeef",
"SafeCert": "base64:deadbeef",
"SafeKey": "base64:deadbeef",
```

Example:

```
{
   "test_name": "openvpn",
   "inputs": [
     "vpn://openvpn.unknown-gazel/?addr=1.1.1.1:1194&transport=tcp&obfs=none",
   ],
   "options": {
     "Cipher": "AES-256-GCM",
     "Auth": "SHA256",
     "Compress": "comp-lzo-no",
     "Obfuscation": "none",
     "SafeCert": "base64:<base64-encoded-pem-encoded-ca>",
     "SafeCert": "base64:<base64-encoded-pem-encoded-cert>",
     "SafeKey": "base64:<base64-encoded-pem-encoded-key>",
  }
}
```

### Authentication with username and password stored locally

Instead of `SafeCert` and `SafeKey`, if the option `SafeLocalCreds` is set to
`true`, the credentials will be looked up in a path relative to `$HOME`.
Specifically, this path is constructed from the name of the provider:
`$MINIOONI_HOME/.vpn/<provider>.txt`. This file is expected to contain username
and password in cleartext, in two separated lines ended by a line return.



## Other options


### OpenVPN configuration parameters

Other valid options, that will be passed to the minivpn invocation, are:

- `Cipher` (one of: `AES-256-GCM`, `AES-128-GCM`, `AES-256-CBC`,
  `AES-128-CBC`). The cipher to use for encrypting the data channel. Used to
select the cipher to be configured on the data channel. This is equivalent to
the old `--cipher` option in `openvpn`. Be aware the the underlying
implementation, on the contrary than the reference openvpn one, does not
support automatic cipher negotiation: you must configure the cipher
explicitely.
- `Auth` (one of: `SHA1`, `SHA512`). The message digest algorithm used to
  authenticate the data channel packets. If an AEAD cipher mode (e.g. GCM) is
selected, then the specified auth algorithm is ignored for the data channel. Be
aware that `tls-auth` is not yet supported.

### Obfuscation options

In case some type of obfuscation is used, the obfuscating proxy might
further authentication parameters. These can be passed using the `SafeProxyURI`
parameter.

Example:

```
{
  "test_name": "openvpn",
  "inputs": [
    "vpn://openvpn.unknown-onyx/?addr=2.2.2.2:443&transport=tcp&obfs=obfs4"
  ],
  "options": {
    "Cipher": "AES-256-GCM",
    "Auth": "SHA512",
    "Compress": "",
    "Obfuscation": "obfs4",
    "SafeProxyURI": "obfs4://2.2.2.2:443/?cert=8nuAbPJwFrKc%2F29KcCfL5LBuEWxQrjBASYXdUbwcm9d9pKseGK4r2Tg47e23%2Bt6WghxGGw&iat-mode=0"
  }
}
```

### Target URLs

Additionally, the user can specify any amount of comma-separated urls that
wants to be fetched through the tunnel. 

- `URLs` (`string`, optional).

# Test description

There are, at the moment, three distinct stages in the OpenVPN experiments:
`tunnel initialization`, `icmp ping`, and `urlgrabber`.

## 1. Tunnel initialization

An OpenVPN connection tries, sequentially, the following steps:

1. Initializes cryptographic material (local only, not expected to fail).

2. Creates an UDP or TCP socket and initializes the control channel (no network
   communication in the case of UDP)

3. Sends a client `hard-reset` packet, and waits for a `hard-reset` reset
   packet from the server.

4. Performs the TLS handshake over the control channel (can return a handshake
   error, including a timeout if a reply is not received after a reasonable
   amount of time).

5. Data channel initialization: client sends a control packet (expects a server
   ACK), and a request for the server to push options. Upon receiving options
   from the server, the data channel is initialized and ready to use.

Each of the steps above can fail (a timeout is considered a failure on each
step). Upon finishing the data channel initialization, we consider the initial
handshake to be finished and the tunnel ready to be used.


## 2. ICMP Pings

When we reach the data-chanel-done stage, we inject a number `n` of ICMP Echo
Request packets to different targets, and wait for their responses.

We gather statistics about TTL, RTT (measured in milliseconds), and packet loss.

By default, this experiment uses `n=10`.

As reference targets, we measure one cloud provider, the tunnel gateway itself,
and a box in a known geolocation.

## 3. URLGrabber

At the moment, the experiment is fetching a small payload from a
geolocation service via an http `GET` that retrieves a json payload.

If there are additional `URLs` specified via the `URLs` option, they will also be
fetched through the tunnel.


# Expected output

## Parent data format

We include data from the following parent formats:

- `df-000-base`: top-level keys.

- `df-001-httpt`: http data format, archived within the `requests` array.

- `df-005-tcpconnect`: for the `tcp_connect` key.

- `df-008-netevents`: for the `network_events` array.

## Semantics

These are the expected `test_keys` in the output measurement (arrays have been
abbreviated for clarity):


```JavaScript
{
    "provider": "riseup",
    "vpn_protocol": "openvpn",
    "transport": "tcp",
    "remote": "198.252.153.109:443",
    "obfuscation": "obfs4",
    "bootstrap_time": 1.5671859910000001,
    "network_events": [
      {
        "x_operation_id": 0,
        "operation": "ready",
        "t": 0.12
      },
      {
        "x_operation_id": 1,
        "operation": "dial_done",
        "t": 515.117
      },
      {
        "x_operation_id": 2,
        "operation": "vpn_handshake_start",
        "t": 515.118
      },
      {
        "x_operation_id": 3,
        "operation": "reset",
        "t": 515.119
      },
      {
        "x_operation_id": 5,
        "operation": "tls_handshake_start",
        "t": 771.98
      },
      {
        "x_operation_id": 6,
        "operation": "tls_handshake_done",
        "t": 1041.248
      },
      {
        "x_operation_id": 7,
        "operation": "data_init",
        "t": 1567.111
      },
      {
        "x_operation_id": 8,
        "operation": "vpn_handshake_done",
        "t": 1567.114
      }
    ],
    "last_handshake_x_operation_id": 8,
    "tcp_connect": {
      "ip": "198.252.153.109",
      "port": 443,
      "status": {
        "failure": null,
        "success": true
      },
      "t0": 0.000424974,
      "t": 0.258504018
    },
    "failure": null,
    "icmp_pings": [
      {
        "target": "8.8.8.8",
        "sequence": [
          {
            "seq": 1,
            "ttl": 121,
            "rtt": 255.168
          }
          // ... snip ...
        ],
        "pkt_rcv": 1,
        "pkt_snt": 1,
        "min_rtt": 255.168,
        "max_rtt": 255.168,
        "avg_rtt": 255.168,
        "std_rtt": 0,
        "failure": null
      }
    ],
    "requests": [
      // ... snip ...
    ],
    "minivpn_version": "(devel)",
    "obfs4_version": "(devel)",
    "success_handshake": true,
    "success_icmp": true,
    "success_urlgrab": true,
    "success": true
},
```

where:

- `provider`, `vpn_protocol`, `transport`, `remote` and `obfuscation` are
  parameters extracted by the probe from the input `URI` (and as such, they
  should match). However, the authoritative source is the entry in the
  test-keys.

- `provider` (`string`) is the entity that manages the endpoints. If it's not a
  provider known to OONI, it should be marked with a prefix starting with
  "unknown".

- `vpn_protocol` (`string`): should be `openvpn`.

- `transport` (`string`): underlying transport used by OpenVPN, one of `tcp|udp`.

- `remote` (`string`): IP address and port for the remote endpoint (`ipaddr:port`).

- `obfuscation` (`string`): type of obfuscation in use. Currently known
  obfuscation schemes include `none` and `obfs4`.

- `bootstrap_time` (`float`) is the time, in seconds, to bootstrap a VPN connection,

- `success` (`bool`) whether all the stages in the experiment were successful.

- `success_handshake` (`bool`) signals a successful openvpn handshake.

- `success_icmp` (`bool`) signals that all of the first two icmp pings replies returned
  "viable" responses (meaning, arbitrarily, < 50% packet loss).

- `success_urlgrab` (`bool`) signals that we got at least one successful url
  grab in the web-fetching part of the experiment.

- `minivpn_version` (`string`) contains the version of the `minivpn` library
  that is used in the ooni probe build used for the experiment.

- `obfs4_version` (`string`) contains the version of the `obfs4` library
  that is used in the ooni probe build used for the experiment.

- `failure` (`string`; nullable) conforms to `df-007-errors`.

- `network_events` is an array containing timing for different stages of the
  OpenVPN handshake, conforming to `df-008-netevents`:

    - `transaction_id` (`int`): sequential integer for the operation.

    - `operation` (`string`): the name for the operation.

    - `t` (`float`): time, in seconds, for the event marking this operation.

- `last_handshake_transaction_id` (`uint8`) integer that corresponds to the
  transaction id of the last received OpenVPN handshake event.

- `tcp_connect`: info about the TCP handshake (only when `transport` == `tcp`). Conforms to `df-005-tcpconnect`.

- `icmp_pings` is an array containing the result for a series of `icmp` pings through the tunnel:

    - `target` (`string`): the IP the ICMP trains were targeting,

    - `sequence` is an array with the ping responses:

        - `seq` (`int`): the sequence number for this response packet.

        - `rtts`: (`float`): raw rtt value.

        - `ttls`: (`int`): raw ttl value.

    - `pkt_rcv` (`int`): how many packets were received.

    - `pkt_snt` (`int`): how many packets were sent.

    - `min_rtt` (`float`): the minimum value for all the pings towards this target.

    - `max_rtt` (`float`): the maximum value for all the pings towards this target.

    - `avg_rtt` (`float`): the average of the rtt for all the pings towards this target.

    - `std_rtt` (`float`): the standard deviation of the rtt for all the pings towards this target.

    - `failure` (`string`; nullable): any error during the ping operation. Conforms to `df-007-errors`.

- `requests` is an array of results containing the request and response for a given
  `urlgrabber` operation through the tunnel. Conforms to `df-001-httpt`.
 

## Possible conclusions

- If the experiment successfully completed the tunnel-initialization stage, we
  can conclude that no mechanism interfered with the establishment of an
  OpenVPN tunnel (in UDP or TCP mode) against the particular combination of remote
  server and port used in our setup.

- If the experiment was able to receive `ECHO` replies, we conclude that the
  tunnel was functional, and the VPN remote correctly routed `n` replies from the
  target server to our client. There are few conclusions that can be extracted
  here about possible interference, other than perhaps confirming that the
  tunnel was working for a given period of time and a certain number of
  transmitted bytes or packets.


## Example output sample

```json
{
  "annotations": {
    "architecture": "amd64",
    "engine_name": "ooniprobe-engine",
    "engine_version": "3.17.0-alpha",
    "platform": "linux"
  },
  "data_format_version": "0.2.0",
  "extensions": {
    "httpt": 0
  },
  "input": "vpn://openvpn.riseup/?addr=198.252.153.109:443&transport=tcp&obfs=obfs4",
  "measurement_start_time": "2022-11-21 17:22:49",
  "options": [
    "Cipher=AES-256-GCM",
    "Auth=SHA512",
    "Compress=",
    "Obfuscation=obfs4"
  ],
  "probe_asn": "AS9009",
  "probe_cc": "RO",
  "probe_ip": "127.0.0.1",
  "probe_network_name": "M247 Ltd",
  "report_id": "",
  "resolver_asn": "AS9009",
  "resolver_ip": "185.45.15.210",
  "resolver_network_name": "M247 Ltd",
  "software_name": "miniooni",
  "software_version": "3.17.0-alpha",
  "test_keys": {
    "provider": "riseup",
    "vpn_protocol": "openvpn",
    "transport": "tcp",
    "remote": "198.252.153.109:443",
    "obfuscation": "obfs4",
    "bootstrap_time": 1.5671859910000001,
    "network_events": [
      {
        "transaction_id": 0,
        "operation": "ready",
        "t": 0.12
      },
      {
        "transaction_id": 1,
        "operation": "dial_done",
        "t": 515.117
      },
      {
        "transaction_id": 2,
        "operation": "vpn_handshake_start",
        "t": 515.118
      },
      {
        "transaction_id": 3,
        "operation": "reset",
        "t": 515.119
      },
      {
        "transaction_id": 5,
        "operation": "tls_handshake_start",
        "t": 771.98
      },
      {
        "transaction_id": 6,
        "operation": "tls_handshake_done",
        "t": 1041.248
      },
      {
        "transaction_id": 7,
        "operation": "data_init",
        "t": 1567.111
      },
      {
        "transaction_id": 8,
        "operation": "vpn_handshake_done",
        "t": 1567.114
      }
    ],
    "last_handshake_transaction_id": 8,
    "tcp_connect": {
      "ip": "198.252.153.109",
      "port": 443,
      "status": {
        "failure": null,
        "success": true
      },
      "t0": 0.000424974,
      "t": 0.258504018
    },
    "failure": null,
    "icmp_pings": [
      {
        "target": "8.8.8.8",
        "sequence": [
          {
            "seq": 1,
            "ttl": 121,
            "rtt": 255.168
          },
          {
            "seq": 2,
            "ttl": 121,
            "rtt": 257.614
          },
          {
            "seq": 4,
            "ttl": 121,
            "rtt": 256.957
          },
          {
            "seq": 5,
            "ttl": 121,
            "rtt": 257.894
          },
          {
            "seq": 6,
            "ttl": 121,
            "rtt": 1952.461
          },
          {
            "seq": 7,
            "ttl": 121,
            "rtt": 1382.493
          },
          {
            "seq": 8,
            "ttl": 121,
            "rtt": 429.14
          },
          {
            "seq": 9,
            "ttl": 121,
            "rtt": 433.099
          },
          {
            "seq": 10,
            "ttl": 121,
            "rtt": 1175.273
          }
        ],
        "pkt_rcv": 9,
        "pkt_snt": 10,
        "min_rtt": 255.168,
        "max_rtt": 1952.461,
        "avg_rtt": 711.122,
        "std_rtt": 595.274,
        "failure": null
      },
      {
        "target": "10.41.0.1",
        "sequence": [
          {
            "seq": 2,
            "ttl": 64,
            "rtt": 434.066
          },
          {
            "seq": 3,
            "ttl": 64,
            "rtt": 431.661
          },
          {
            "seq": 4,
            "ttl": 64,
            "rtt": 432.937
          },
          {
            "seq": 5,
            "ttl": 64,
            "rtt": 428.673
          },
          {
            "seq": 6,
            "ttl": 64,
            "rtt": 429.713
          },
          {
            "seq": 7,
            "ttl": 64,
            "rtt": 426.291
          },
          {
            "seq": 8,
            "ttl": 64,
            "rtt": 424.651
          },
          {
            "seq": 9,
            "ttl": 64,
            "rtt": 1091.933
          },
          {
            "seq": 10,
            "ttl": 64,
            "rtt": 421.675
          }
        ],
        "pkt_rcv": 9,
        "pkt_snt": 10,
        "min_rtt": 421.675,
        "max_rtt": 1091.933,
        "avg_rtt": 502.4,
        "std_rtt": 208.466,
        "failure": null
      },
      {
        "target": "163.7.134.112",
        "sequence": [
          {
            "seq": 1,
            "ttl": 56,
            "rtt": 562.198
          },
          {
            "seq": 2,
            "ttl": 56,
            "rtt": 557.722
          },
          {
            "seq": 3,
            "ttl": 56,
            "rtt": 557.061
          },
          {
            "seq": 4,
            "ttl": 56,
            "rtt": 539.17
          },
          {
            "seq": 5,
            "ttl": 56,
            "rtt": 541.216
          },
          {
            "seq": 6,
            "ttl": 56,
            "rtt": 526.353
          },
          {
            "seq": 7,
            "ttl": 56,
            "rtt": 523.954
          },
          {
            "seq": 8,
            "ttl": 56,
            "rtt": 515.543
          },
          {
            "seq": 9,
            "ttl": 56,
            "rtt": 512.221
          },
          {
            "seq": 10,
            "ttl": 56,
            "rtt": 528.066
          }
        ],
        "pkt_rcv": 10,
        "pkt_snt": 10,
        "min_rtt": 512.221,
        "max_rtt": 562.198,
        "avg_rtt": 536.35,
        "std_rtt": 17.096,
        "failure": null
      }
    ],
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
              "en-US,en;q=0.9"
            ],
            [
              "Host",
              "api.ipify.org"
            ],
            [
              "User-Agent",
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
            ]
          ],
          "headers": {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
            "Host": "api.ipify.org",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
          },
          "method": "GET",
          "tor": {
            "exit_ip": null,
            "exit_name": null,
            "is_tor": false
          },
          "x_transport": "tcp",
          "url": "https://api.ipify.org/?format=json"
        },
        "response": {
          "body": "{\"ip\":\"198.252.153.28\"}",
          "body_is_truncated": false,
          "code": 200,
          "headers_list": [
            [
              "Connection",
              "keep-alive"
            ],
            [
              "Content-Length",
              "23"
            ],
            [
              "Content-Type",
              "application/json"
            ],
            [
              "Date",
              "Mon, 21 Nov 2022 17:22:49 GMT"
            ],
            [
              "Server",
              "Cowboy"
            ],
            [
              "Vary",
              "Origin"
            ],
            [
              "Via",
              "1.1 vegur"
            ]
          ],
          "headers": {
            "Connection": "keep-alive",
            "Content-Length": "23",
            "Content-Type": "application/json",
            "Date": "Mon, 21 Nov 2022 17:22:49 GMT",
            "Server": "Cowboy",
            "Vary": "Origin",
            "Via": "1.1 vegur"
          }
        },
        "t": 1.742338739
      }
    ],
    "minivpn_version": "(devel)",
    "obfs4_version": "(devel)",
    "success_handshake": true,
    "success_icmp": true,
    "success_urlgrab": true,
    "success": true
  },
  "test_name": "openvpn",
  "test_runtime": 37.975210163,
  "test_start_time": "2022-11-21 17:22:11",
  "test_version": "0.0.19"
}
```

# Privacy considerations

OpenVPN does not seek to provide anonymity. An adversary can observe that a
user is connecting to OpenVPN servers. OpenVPN servers can also determine the
users location.

Besides this, the [https://github.com/ooni/minivpn](openvpn implementation used
in this experiment) is known to have several minor distinguisher features in
comparison to the reference OpenVPN implementation. While work is being done to
close the gap between the two implementations, a motivated adversary can in
theory infer the usage of probing activity by means of implementation quirks.
However, probing activity is already evident because of the traffic patterns
and timing, so this should not be a high-impact concern in practice.

# Packet capture considerations

This test does not capture packets by default.

# Status and future directions

This test is in experimental state.

One possible outcome, to be discussed, is the relationship of this experiment
with experiments that measure the behavior for concrete services (i.e.,
experiments adapted to the particularities of concrete VPN service providers).

To this end, it might be beneficial to turn the `openvpn` spec into a library
for implementing concrete openvpn probes. 

Also, we might want to abstract the openvpn and wireguard experiments as
different flavors of a single `vpn` experiment (possibly mapping some of the
possible errors at different stages of the connection).

Another potential for improvement includes adding bridge information to this
openvpn experiment (the only bridge we are aware of right now is obfs4). The
obfuscated vpn tunnel could be a different experiment, but it would make sense
to simply treat it as a different input variable so to be able to easily perform
comparisons.

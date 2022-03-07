# Specification version number

2022-10-20

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

The `URI` encodes information for the protocol (`openvpn`, in this case),
provider, transport, obfuscation and the remote address.

```
vpn://{provider_name}.{protocol}/?transport=tcp&obfuscation=obfs4&address={ip}:{port}
```

The credentials to authenticate against such endpoint need to be passed as
options to the experiment, encoded as a base64 string. We use the `Safe` prefix
to signal to the engine that we don't want those options to be exported and
indexed by the OONI backend:

```
"SafeCa": "base64:deadbeef",
"SafeCert": "base64:deadbeef",
"SafeKey": "base64:deadbeef",
```


Other valid options, that will be passed to the openvpn invocation, are:

- `cipher` (one of: `AES-256-GCM`, `AES-128-GCM`, `AES-256-CBC`, `AES-128-CBC`).
- `auth` (one of: `SHA1`, `SHA512`).

# Test description

There are, at the moment, three distinct stages in the OpenVPN experiments:
`tunnel initialization`, `icmp-ping`, and `urlgrabber`.

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


## 2. ICMP-Pings

When we reach the data-chanel-done stage, we inject a number `n` of ICMP Echo
Request packets to different targets, and wait for their responses.

We gather statistics about TTL, RTT (measured in milliseconds), and packet loss.

By default, this experiment uses `n=10`.

As reference targets, we measure one cloud provider, the tunnel gateway itself,
and a box in a known geolocation.

## 3. urlgrabber

At the moment, the experiment is fetching a small payload from a
geolocation service via an http `GET` that retrieves a json payload. We also
fetch a truncated payload from a well-known website that should be enough to
capture the language code in the html document.

# Expected output

## Parent data format

We include data from the following parent formats:


- `df-000-base`: top-level keys.
- `df-001-httpt`: http data format, archived within the `requests` array.
- `df-005-tcpconnect`: for the `tcp_connect` key.

## Semantics

These are the expected `test_keys` in the output measurement (arrays have been
abbreviated for clarity):


```JSON
{
  "test_keys": {
    "provider": "riseup",
    "vpn_protocol": "openvpn",
    "transport": "tcp",
    "remote": "51.158.144.32:80",
    "obfuscation": "none",
    "bootstrap_time": 0.37221659,
    "minivpn_version": "(devel)",
    "obfs4_version": "",
    "success": true
    "stages": [
      {
        "op_id": 0
        "operation": "ready",
        "t": 0.145
      },
      {
        "op_id": 8,
        "operation": "vpn_handshake_done",
        "t": 372.14
      }
    ],
    "tcp_connect": {
      "ip": "51.158.144.32",
      "port": 80,
      "status": {
        "failure": null,
        "success": true
      },
      "t0": 0.000239501,
      "t": 0.045310671,
      "transaction_id": 1
    },
    "failure": null,
    "error": null,
    "pings": [
      {
        "target": "8.8.8.8",
        "sequence": [
          {
            "seq": 9,
            "ttl": 113,
            "rtt": 60.208
          },
          {
            "seq": 10,
            "ttl": 113,
            "rtt": 57.909
          }
        ],
        "pkt_rcv": 10,
        "pkt_snt": 10,
        "min_rtt": 56.477,
        "max_rtt": 67.85,
        "avg_rtt": 60.926,
        "std_rtt": 3.717,
        "error": null
      },
      {
        "target": "10.41.0.1",
        "sequence": [
          {
            "seq": 10,
            "ttl": 64,
            "rtt": 107.01
          }
        ],
        "pkt_rcv": 10,
        "pkt_snt": 10,
        "min_rtt": 48.734,
        "max_rtt": 107.01,
        "avg_rtt": 58.518,
        "std_rtt": 16.43,
        "error": null
      },
      {
        "target": "163.7.134.112",
        "sequence": [
          {
            "seq": 10,
            "ttl": 54,
            "rtt": 334.934
          }
        ],
        "pkt_rcv": 10,
        "pkt_snt": 10,
        "min_rtt": 327.153,
        "max_rtt": 379.311,
        "avg_rtt": 338.438,
        "std_rtt": 14.347,
        "error": null
      }
    ],
    "requests": [
      {
        "failure": null,
        "request": {
          "method": "GET",
          "url": "https://api.ipify.org/?format=json",
          "headers": {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "accept-language": "en-US,en;q=0.9",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
          }
        },
        "response": {
          "code": 200,
          "headers": {
            "connection": "keep-alive",
            "content-length": "23",
            "content-type": "application/json",
            "date": "Fri, 21 Oct 2022 09:12:18 GMT",
            "server": "Cowboy",
            "vary": "Origin",
            "via": "1.1 vegur"
          },
          "body": {
            "data": "eyJpcCI6IjIxMi44My4xODIuMTI3In0=",
            "format": "base64"
          },
          "body_is_truncated": false,
          "x_body_length": 23,
          "x_body_is_utf8": true
        },
        "t": 0.558008438,
        "started": 8.3589e-05,
        "oddity": ""
      }
    ]
  }
}
```

where:

- `provider`, `vpn_protocol`, `transport`, `remote` and `obfuscation` are
  parameters extracted by the probe from the input `URI` (and as such, they
  should match). However, the authoritative source is the entry in the
  test-keys.
- `provider` (`string`) is the entity that manages the endpoints. If it's not a
  provider known to OONI, it should be marked as "unknown".
- `vpn_protocol` (`string`): should be `openvpn`.
- `transport` (`string`): underlying transport used by OpenVPN, one of `tcp|udp`,
- `remote` (`string`): IP address and port for the remote endpoint (`ip:port`).
- obfuscation": "none",
- `bootstrap_time` (`float`) is the time, in seconds, to bootstrap a VPN connection,
- `success` (`bool`) whether all the stages in the experiment were successful,
- `minivpn_version` (`string`) contains the version of the `minivpn` library
  that is used in the ooni probe build used for the experiment,
- `obfs4_version` (`string`) contains the version of the `obfs4` library
  that is used in the ooni probe build used for the experiment,
- `failure` (`string`; nullable) conforms to `df-007-errors`,
- `error` (`string`; nullable) raw error message, conforms to `df-007-errors`,
- `stages` is an array containing timing for different bootstrap stages:
    - `op_id` (`int`): sequential integer for the operation.
    - `operation` (`string`): the name for the operation.
    - `t` (`float`): time, in seconds, for the event marking this operation.
- `tcp_connect`: info about the TCP handshake (only when `transport` == `tcp`). Conforms to `df-005-tcpconnect`.
- `pings` is an array containing the result for a series of `icmp` pings through the tunnel:
    - `target` (`string`): the IP the ICMP trains were targeting,
    - `sequence` is an aray with the ping responses:
        - `seq` (`int`): the sequence number for this response packet,
        - `rtts`: (`float`): raw rtt value,
        - `ttls`: (`int`): raw ttl value,
    - `pkt_rcv` (`int`): how many packets were received,
    - `pkt_snt` (`int`): how many packets were sent,
    - `min_rtt` (`float`): the min value for all the pings,
    - `max_rtt` (`float`): the max value for all the pings,
    - `avg_rtt` (`float`): the avg value for all the pings,
    - `std_rtt` (`float`): the std value for all the pings,
    - `error` (`string`; nullable): any error during the ping operation. Conforms to `df-007-errors`.
- `requests` is an array containing the request and response for a given
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
  "input": "vpn://openvpn.riseup/?addr=51.158.144.32:80&transport=tcp&obfs=none",
  "measurement_start_time": "2022-10-21 09:12:18",
  "options": [
    "Obfuscation=none",
    "Cipher=AES-256-GCM",
    "Auth=SHA512",
    "Compress="
  ],
  "probe_asn": "AS9105",
  "probe_cc": "GB",
  "probe_ip": "127.0.0.1",
  "probe_network_name": "UltraLettuce Networks Limited",
  "report_id": "20221109T121906Z_openvpn_GB_9105_n1_QRVthZY6Pi9lYS7j",
  "resolver_asn": "AS9105",
  "resolver_ip": "81.1.72.35",
  "resolver_network_name": "TalkTalk Communications Limited",
  "software_name": "miniooni",
  "software_version": "3.17.0-alpha",
  "test_keys": {
    "provider": "riseup",
    "vpn_protocol": "openvpn",
    "transport": "tcp",
    "remote": "51.158.144.32:80",
    "obfuscation": "none",
    "bootstrap_time": 0.37221659,
    "stages": [
      {
        "op_id": 0,
        "operation": "ready",
        "t": 0.145
      },
      {
        "op_id": 1,
        "operation": "dial_done",
        "t": 45.381
      },
      {
        "op_id": 3,
        "operation": "reset",
        "t": 45.545
      },
      {
        "op_id": 4,
        "operation": "tls_conn",
        "t": 100.436
      },
      {
        "op_id": 5,
        "operation": "tls_handshake",
        "t": 100.437
      },
      {
        "op_id": 6,
        "operation": "tls_handshake_done",
        "t": 155.885
      },
      {
        "op_id": 7,
        "operation": "data_init",
        "t": 372.136
      },
      {
        "op_id": 8,
        "operation": "vpn_handshake_done",
        "t": 372.14
      }
    ],
    "tcp_connect": {
      "ip": "51.158.144.32",
      "port": 80,
      "status": {
        "failure": null,
        "success": true
      },
      "t0": 0.000239501,
      "t": 0.045310671,
      "transaction_id": 1
    },
    "failure": null,
    "error": null,
    "pings": [
      {
        "target": "8.8.8.8",
        "sequence": [
          {
            "seq": 1,
            "ttl": 113,
            "rtt": 62.61
          },
          {
            "seq": 2,
            "ttl": 113,
            "rtt": 56.555
          },
          {
            "seq": 3,
            "ttl": 113,
            "rtt": 57.764
          },
          {
            "seq": 4,
            "ttl": 113,
            "rtt": 67.85
          },
          {
            "seq": 5,
            "ttl": 113,
            "rtt": 64.811
          },
          {
            "seq": 6,
            "ttl": 113,
            "rtt": 60.47
          },
          {
            "seq": 7,
            "ttl": 113,
            "rtt": 64.607
          },
          {
            "seq": 8,
            "ttl": 113,
            "rtt": 56.477
          },
          {
            "seq": 9,
            "ttl": 113,
            "rtt": 60.208
          },
          {
            "seq": 10,
            "ttl": 113,
            "rtt": 57.909
          }
        ],
        "pkt_rcv": 10,
        "pkt_snt": 10,
        "min_rtt": 56.477,
        "max_rtt": 67.85,
        "avg_rtt": 60.926,
        "std_rtt": 3.717,
        "error": null
      },
      {
        "target": "10.41.0.1",
        "sequence": [
          {
            "seq": 1,
            "ttl": 64,
            "rtt": 51.771
          },
          {
            "seq": 2,
            "ttl": 64,
            "rtt": 51.983
          },
          {
            "seq": 3,
            "ttl": 64,
            "rtt": 56.588
          },
          {
            "seq": 4,
            "ttl": 64,
            "rtt": 60.096
          },
          {
            "seq": 5,
            "ttl": 64,
            "rtt": 51.718
          },
          {
            "seq": 6,
            "ttl": 64,
            "rtt": 48.734
          },
          {
            "seq": 7,
            "ttl": 64,
            "rtt": 52.531
          },
          {
            "seq": 8,
            "ttl": 64,
            "rtt": 52.642
          },
          {
            "seq": 9,
            "ttl": 64,
            "rtt": 52.106
          },
          {
            "seq": 10,
            "ttl": 64,
            "rtt": 107.01
          }
        ],
        "pkt_rcv": 10,
        "pkt_snt": 10,
        "min_rtt": 48.734,
        "max_rtt": 107.01,
        "avg_rtt": 58.518,
        "std_rtt": 16.43,
        "error": null
      },
      {
        "target": "163.7.134.112",
        "sequence": [
          {
            "seq": 1,
            "ttl": 54,
            "rtt": 329.409
          },
          {
            "seq": 2,
            "ttl": 54,
            "rtt": 333.689
          },
          {
            "seq": 3,
            "ttl": 54,
            "rtt": 340.251
          },
          {
            "seq": 4,
            "ttl": 54,
            "rtt": 379.311
          },
          {
            "seq": 5,
            "ttl": 54,
            "rtt": 327.153
          },
          {
            "seq": 6,
            "ttl": 54,
            "rtt": 331.392
          },
          {
            "seq": 7,
            "ttl": 54,
            "rtt": 330.347
          },
          {
            "seq": 8,
            "ttl": 54,
            "rtt": 335.409
          },
          {
            "seq": 9,
            "ttl": 54,
            "rtt": 342.488
          },
          {
            "seq": 10,
            "ttl": 54,
            "rtt": 334.934
          }
        ],
        "pkt_rcv": 10,
        "pkt_snt": 10,
        "min_rtt": 327.153,
        "max_rtt": 379.311,
        "avg_rtt": 338.438,
        "std_rtt": 14.347,
        "error": null
      }
    ],
    "requests": [
      {
        "failure": null,
        "request": {
          "method": "GET",
          "url": "https://api.ipify.org/?format=json",
          "headers": {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "accept-language": "en-US,en;q=0.9",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
          }
        },
        "response": {
          "code": 200,
          "headers": {
            "connection": "keep-alive",
            "content-length": "23",
            "content-type": "application/json",
            "date": "Fri, 21 Oct 2022 09:12:18 GMT",
            "server": "Cowboy",
            "vary": "Origin",
            "via": "1.1 vegur"
          },
          "body": {
            "data": "eyJpcCI6IjIxMi44My4xODIuMTI3In0=",
            "format": "base64"
          },
          "body_is_truncated": false,
          "x_body_length": 23,
          "x_body_is_utf8": true
        },
        "t": 0.558008438,
        "started": 8.3589e-05,
        "oddity": ""
      },
      {
        "failure": null,
        "request": {
          "method": "GET",
          "url": "https://www.google.com/",
          "headers": {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "accept-language": "en-US,en;q=0.9",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
          }
        },
        "response": {
          "code": 200,
          "headers": {
            "accept-ch": "Sec-CH-UA-Platform",
            "alt-svc": "h3=\":443\"; ma=2592000,h3-29=\":443\"; ma=2592000,h3-Q050=\":443\"; ma=2592000,h3-Q046=\":443\"; ma=2592000,h3-Q043=\":443\"; ma=2592000,quic=\":443\"; ma=2592000; v=\"46,43\"",
            "bfcache-opt-in": "unload",
            "cache-control": "private, max-age=0",
            "content-type": "text/html; charset=UTF-8",
            "date": "Fri, 21 Oct 2022 09:12:18 GMT",
            "expires": "-1",
            "p3p": "CP=\"This is not a P3P policy! See g.co/p3phelp for more info.\"",
            "server": "gws",
            "set-cookie": "AEC=AakniGMtY-ydpeSb5yT257GdEdNMWQOR4oobqcvRp4OtODlkSKzyPqeTkg; expires=Wed, 19-Apr-2023 09:12:18 GMT; path=/; domain=.google.com; Secure; HttpOnly; SameSite=lax",
            "strict-transport-security": "max-age=31536000",
            "x-frame-options": "SAMEORIGIN",
            "x-xss-protection": "0"
          },
          "body": {
            "data": "PCFkb2N0eXBlIGh0bWw+PGh0bWwgaXRlbXNjb3BlPSIiIGl0ZW10eXBlPSJodHRwOi8vc2NoZW1hLm9yZy9XZWJQYWdlIiBsYW5nPSJmciI+PGhlYWQ+PG1ldGEgY2hhcnNldA==",
            "format": "base64"
          },
          "body_is_truncated": true,
          "x_body_length": 100,
          "x_body_is_utf8": true
        },
        "t": 0.946926271,
        "started": 0.558104205,
        "oddity": ""
      }
    ],
    "minivpn_version": "(devel)",
    "obfs4_version": "",
    "success": true
  },
  "test_name": "openvpn",
  "test_runtime": 32.003161366,
  "test_start_time": "2022-10-21 09:11:46",
  "test_version": "0.0.12"
}
```

# Privacy considerations

OpenVPN does not seek to provide anonymity. An adversary can observe that a
user is connecting to OpenVPN servers. OpenVPN servers can also determine the
users location.

Besides this, the [https://github.com/ooni/minivpn](openvpn implementation used in this experiment)
is known to have several minor distinguisher features in
comparison to the reference openvpn implementation. While work is being done to
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


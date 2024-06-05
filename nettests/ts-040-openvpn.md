# Specification version number

2024-06-03

* _status_: experimental.

# Specification name

`openvpn`

# Test preconditions

* An internet connection
* Configuration and Inputs for the given targets; provided by any means like
  the OONI API, `miniooni` cli options, `oonirunv2` descriptors or Richer Input.

# Expected impact

The ability to detect if a working OpenVPN connection can be established with a given host.

# Expected inputs

There are two categories of input parameters to this experiment. Some of them are given as
part of the input `URI` for the experiment, and some others are passed as
options. For clarity, this document refers to "input" as in the context of input URLs.

Altogether, they constitute a basic subset of the valid configuration
parameters for the reference openvpn implementation (`man 8 openvpn`).

In its current state, the experiment is able to function without the user
passing any target input: valid credentials are still expected, either as user-supplied options
or via a request to the OONI API. In the case of no explicit input, we use a
pre-seeded list of endpoints, and we lookup credentials and configuration
options using the provider label to find valid values.

## Input URI

The input `URI` encodes information for the protocol (`openvpn`, in this case), obfuscation,
provider, remote address, and underlying transport.

```
{vpn_protocol}://{provider}.corp/?address={remote}&transport={transport}
```

Where:

- `vpn_protocol` (`string`): for the openvpn experiment, it should be `openvpn`, or `openvpn+obfs4`.
- `provider` (`string`) is the entity that manages the endpoints. If it's not a
  provider known to OONI, it should be marked with a prefix starting with
  "unknown".
- `remote` (`string`): IP address and port for the remote endpoint (`ipaddr:port`).
- `transport` (`string`): underlying transport used by OpenVPN, one of `tcp|udp`.

Examples:

```
openvpn://unknown.corp/?address=1.2.3.4:1194&transport=udp
openvpn+obfs4://unknown.corp/?address=1.2.3.4:1194&transport=tcp
```


# Test description

At this stage, the openvpn test does one single operation per input: attempt 
to complete a OpenVPN handshake against the given endpoint.

## Tunnel initialization

An OpenVPN connection tries, sequentially, the following steps:

0. Initialize cryptographic material (local only, not expected to fail). If we
   fail to validate that we meet any pre-requisites, we will abort the test by
   returning an error.

1. Create an UDP or TCP socket and initializes the control channel (no network
   communication in the case of UDP). In the case of TCP, we will add a
   `tcp_connect` record. If there's a failure, the handshake will be aborted.

2. The first step in the handshake is to send a client `hard-reset` packet,
   and wait for a `hard-reset` reset packet from the server.

3. Perform a TLS handshake over the control channel. This can make the handshake
   to return error, including a timeout if a reply is not received after a reasonable
   amount of time, which by default is 60 seconds.

4. Data channel initialization: client sends a control packet (expects a server
   ACK), and a request for the server to push options. Upon receiving options
   from the server, the data channel is initialized and ready to use.

Each of the steps above above the 0th step can fail (a timeout is considered a
failure). Upon finishing the data channel initialization, we consider the initial
handshake to be finished and the tunnel ready to be used.

# Expected output

## Parent data format

We include data from the following parent formats:

- `df-000-base`: top-level keys.

- `df-005-tcpconnect`: for the `tcp_connect` key.

- `df-008-netevents`: for the `network_events` array.

## Semantics

These are the expected `test_keys` in the output measurement (arrays have been
abbreviated for clarity):


```JavaScript
"test_keys": {
    "success": true,
    "openvpn_handshake": [...]
    "tcp_connect": [...]
    "network_events": [...]
}
```

Where:

- `success` (`bool`) marks whether the attempted connections returned a successful handshake.

- `openvpn_handshake` is an array containing the results for a connection attempt against a given endpoint.

- `tcp_connect`: info about the TCP handshake (only when `endpoint.transport` == `tcp`). Conforms to `df-005-tcpconnect`.
   The `transaction_id` refers to the matching handshake in the `openvpn_handshake` array.

- `network_events` is an array containing timing for different stages of the
   OpenVPN handshake, conforming to `df-008-netevents`. As in the case above,
  `transaction_id` contains an index that allows to reference
   events with the handshakes in the `openvpn_handshake` array. Do note that
   timing information is relative to the beginning of each handshake.

### openvpn_handshake

The `openvpn_handshake` entry contains information about the result of every
openvpn connection attempt performed during the experiment.

- `bootstrap_time` (`float`): the total time until successful handshake or
  failure, relative to the beginning of the handshake (`t - t0`). Do note that,
  for TCP, the effective time should include the time for the TCP connection.

- `endpoint` (`string`): a URI representing the probed endpoint. This is a different encoding than the input URI format.

- `failure` (`string|null`): any failure returned by the operation.

- `ip` (`string`): the IP address of the endpoint.

- `port` (`int`): the port of the endpoint.

- `transport` (`string`): the transport used (tcp or udp).

- `provider` (`string`): a label marking the provider associated with this endpoint. This label
   has been used to find suitable credentials and default openvpn options.

- `openvpn_options`: a map from `string` to `string`, containing the relevant
   subset of the openvpn options used in the connection, for comparison
   purposes.

- `t0` (`float`): the beginning of the openvpn handshake, in seconds, relative to `measurement_start_time`. In TCP
  mode, this is right after a successful TCP three-way-handhsake.

- `t` (`float`): the end of the handshake, in seconds, relative to `handshake_start_time`. 

- `transaction_id` (`int`): a sequential index that marks this particular connection attempt. This index can be used
  to cross-reference entries in other fields, like `tcp_connect` or `network_events`.

Example:

```JavaScript
"openvpn_handshake": [
  {
    "bootstrap_time": 0.177719632,
    "endpoint": "openvpn://51.15.187.53:1194/tcp",
    "failure": null,
    "ip": "51.15.187.53",
    "port": 1194,
    "transport": "tcp",
    "provider": "riseup",
    "openvpn_options": {
      "auth": "SHA512",
      "cipher": "AES-256-GCM"
    },
    "t0": 0.033876298,
    "t": 0.21159593,
    "tags": [],
    "transaction_id": 1
  }
]
```

### network_events

The `network_events` array follows `df-008-netevents` semantics, with some differences:

- `operation` (`string`) marks different types of events. Known events are:
  - `state`: for changes in the internal state machine.
  - `packet_out`: writes into the network.
  - `packet_in`: reads from the network.
  - `packet_dropped`: marks dropped packets, because failing to pass sanity checks, buffer fulls, or other reasons.

- `stage`: the state of the internal state machine. This can be used to compute duration of handshake stages, from one state change to the next (the `state` event can be considered as the `t0` for a given stage).

    The sequential list of states can be found in [https://github.com/ooni/minivpn/blob/main/internal/model/session.go#L8](the source code for minivpn):

    - INITIAL: initialized.
    - PRE_START: we're waiting for acknowledgment from the remote. 
    - START: we've done the three-way handshake.
    - SENT_KEY: we have sent the local part of the key_source2 random material.
    - GOT_KEY: we have got the remote part of key_source2.
    - ACTIVE: the control channel was established.
    - GENERATED_KEYS: the data channel keys have been generated.

    Some values mark inconsistent internal state:

    - ERROR: protocol error.
	- UNDEF: the state machine is in an ambiguous state.

- `tags`: contains annotations to some events. Right now, two values are used in tags:

    - `client_hello`: marks the sending of the TLS client hello packet.
    - `server_hello`: marks the receiving of the TLS server hello packet.

- `packet`: for the `packet_in` and `packet_out` events, we also include some metadata about the parsing of the packets:

    - `operation` (`string`): either `read` or `write`,
    - `opcode` (`string`): a representation of the packet Opcode.
    - `id` (`int`): the packet ID.
    - `acks` ([]`int`): an array of acks contained in this packet.
    - `payload_size` (`int`): the size of this packet's paylad, in bytes.
    - `send_attempts` (`int`, optional): only meaningful for outgoing packets: how many attempts to transmit have happened.

- As usual, `transaction_id` contains an index that can be cross-referenced with the results in the `openvpn_handshake` array.

```JavaScript
"network_events": [
  {
    "operation": "state",
    "stage": "PRE_START",
    "t": 0.001681356,
    "tags": [],
    "packet": null,
    "transaction_id": 1
  },
  {
    "operation": "packet_out",
    "stage": "PRE_START",
    "t": 0.001688121,
    "tags": [],
    "packet": {
      "operation": "write",
      "opcode": "P_CONTROL_HARD_RESET_CLIENT_V2",
      "id": 0,
      "acks": null,
      "payload_size": 0,
      "send_attempts": 1
    },
    "transaction_id": 1
  },
]
```


## Possible conclusions

- If the experiment successfully completed the tunnel-initialization stage, we
  can conclude that no mechanism interfered with the establishment of an
  OpenVPN tunnel (in UDP or TCP mode) against the particular combination of remote
  server and port used in our setup.


## Example output sample

```JavaScript
{
  "annotations": {
    "architecture": "amd64",
    "engine_name": "ooniprobe-engine",
    "engine_version": "3.22.0-alpha",
    "go_version": "go1.20.14",
    "platform": "linux",
    "vcs_modified": "true",
    "vcs_revision": "1100a70af74bb63fdef9656da6e22a8c8dfab0cd",
    "vcs_time": "2024-04-02T17:40:31Z",
    "vcs_tool": "git"
  },
  "data_format_version": "0.2.0",
  "input": "openvpn://riseup.corp/?address=51.15.187.53:1194&transport=tcp",
  "measurement_start_time": "2024-04-03 10:56:39",
  "probe_asn": "AS0001",
  "probe_cc": "IT",
  "probe_ip": "127.0.0.1",
  "probe_network_name": "NSA INC",
  "report_id": "",
  "resolver_asn": "AS99",
  "resolver_ip": "66.185.124.243",
  "resolver_network_name": "WoodyNet, Inc.",
  "software_name": "miniooni",
  "software_version": "3.22.0-alpha",
  "test_keys": {
    "success": true,
    "network_events": [
      {
        "operation": "state",
        "stage": "PRE_START",
        "t": 0.033876298,
        "tags": [],
        "packet": null,
        "transaction_id": 1
      },
      {
        "operation": "packet_out",
        "stage": "PRE_START",
        "t": 0.033878528,
        "tags": [],
        "packet": {
          "operation": "write",
          "opcode": "P_CONTROL_HARD_RESET_CLIENT_V2",
          "id": 0,
          "acks": null,
          "payload_size": 0,
          "send_attempts": 1
        },
        "transaction_id": 1
      },
      {
        "operation": "state",
        "stage": "START",
        "t": 0.072259548,
        "tags": [],
        "packet": null,
        "transaction_id": 1
      },
      {
        "operation": "packet_in",
        "stage": "START",
        "t": 0.072276358,
        "tags": [],
        "packet": {
          "operation": "read",
          "opcode": "P_CONTROL_HARD_RESET_SERVER_V2",
          "id": 0,
          "acks": [
            0
          ],
          "payload_size": 0,
          "send_attempts": null
        },
        "transaction_id": 1
      },
      {
        "operation": "packet_out",
        "stage": "START",
        "t": 0.072799518,
        "tags": [
          "client_hello"
        ],
        "packet": {
          "operation": "write",
          "opcode": "P_CONTROL_V1",
          "id": 1,
          "acks": [
            0
          ],
          "payload_size": 281,
          "send_attempts": 1
        },
        "transaction_id": 1
      },
      {
        "operation": "packet_in",
        "stage": "START",
        "t": 0.108788928,
        "tags": [],
        "packet": {
          "operation": "read",
          "opcode": "P_ACK_V1",
          "id": 0,
          "acks": [
            1
          ],
          "payload_size": 0,
          "send_attempts": null
        },
        "transaction_id": 1
      },
      {
        "operation": "packet_in",
        "stage": "START",
        "t": 0.108967768,
        "tags": [
          "server_hello"
        ],
        "packet": {
          "operation": "read",
          "opcode": "P_CONTROL_V1",
          "id": 1,
          "acks": null,
          "payload_size": 1170,
          "send_attempts": null
        },
        "transaction_id": 1
      },
      {
        "operation": "packet_in",
        "stage": "START",
        "t": 0.108974368,
        "tags": [],
        "packet": {
          "operation": "read",
          "opcode": "P_CONTROL_V1",
          "id": 2,
          "acks": null,
          "payload_size": 291,
          "send_attempts": null
        },
        "transaction_id": 1
      },
      {
        "operation": "state",
        "stage": "SENT_KEY",
        "t": 0.11104146,
        "tags": [],
        "packet": null,
        "transaction_id": 1
      },
      {
        "operation": "packet_out",
        "stage": "SENT_KEY",
        "t": 0.11106886,
        "tags": [],
        "packet": {
          "operation": "write",
          "opcode": "P_CONTROL_V1",
          "id": 2,
          "acks": null,
          "payload_size": 1036,
          "send_attempts": 1
        },
        "transaction_id": 1
      },
      {
        "operation": "packet_out",
        "stage": "SENT_KEY",
        "t": 0.11107201,
        "tags": [],
        "packet": {
          "operation": "write",
          "opcode": "P_CONTROL_V1",
          "id": 3,
          "acks": null,
          "payload_size": 296,
          "send_attempts": 1
        },
        "transaction_id": 1
      },
      {
        "operation": "packet_in",
        "stage": "SENT_KEY",
        "t": 0.149513181,
        "tags": [],
        "packet": {
          "operation": "read",
          "opcode": "P_CONTROL_V1",
          "id": 3,
          "acks": [
            2
          ],
          "payload_size": 158,
          "send_attempts": null
        },
        "transaction_id": 1
      },
      {
        "operation": "packet_in",
        "stage": "SENT_KEY",
        "t": 0.154226516,
        "tags": [],
        "packet": {
          "operation": "read",
          "opcode": "P_CONTROL_V1",
          "id": 4,
          "acks": [
            3
          ],
          "payload_size": 207,
          "send_attempts": null
        },
        "transaction_id": 1
      },
      {
        "operation": "state",
        "stage": "GOT_KEY",
        "t": 0.154282176,
        "tags": [],
        "packet": null,
        "transaction_id": 1
      },
      {
        "operation": "packet_out",
        "stage": "GOT_KEY",
        "t": 0.154323886,
        "tags": [],
        "packet": {
          "operation": "write",
          "opcode": "P_CONTROL_V1",
          "id": 4,
          "acks": null,
          "payload_size": 35,
          "send_attempts": 1
        },
        "transaction_id": 1
      },
      {
        "operation": "packet_in",
        "stage": "GOT_KEY",
        "t": 0.21135702,
        "tags": [],
        "packet": {
          "operation": "read",
          "opcode": "P_ACK_V1",
          "id": 0,
          "acks": [
            4
          ],
          "payload_size": 0,
          "send_attempts": null
        },
        "transaction_id": 1
      },
      {
        "operation": "packet_in",
        "stage": "GOT_KEY",
        "t": 0.21142598,
        "tags": [],
        "packet": {
          "operation": "read",
          "opcode": "P_CONTROL_V1",
          "id": 5,
          "acks": null,
          "payload_size": 290,
          "send_attempts": null
        },
        "transaction_id": 1
      },
      {
        "operation": "state",
        "stage": "ACTIVE",
        "t": 0.21150542,
        "tags": [],
        "packet": null,
        "transaction_id": 1
      },
      {
        "operation": "state",
        "stage": "GENERATED_KEYS",
        "t": 0.21159593,
        "tags": [],
        "packet": null,
        "transaction_id": 1
      }
    ],
    "tcp_connect": [
      {
        "ip": "51.15.187.53",
        "port": 1194,
        "status": {
          "failure": null,
          "success": true
        },
        "t0": 0.00003125,
        "t": 0.033783028,
        "tags": [],
        "transaction_id": 1
      }
    ],
    "openvpn_handshake": [
      {
        "bootstrap_time": 0.177719632,
        "endpoint": "openvpn://51.15.187.53:1194/tcp",
        "failure": null,
        "ip": "51.15.187.53",
        "port": 1194,
        "transport": "tcp",
        "provider": "riseup",
        "openvpn_options": {
          "auth": "SHA512",
          "cipher": "AES-256-GCM"
        },
        "t0": 0.033876298,
        "t": 0.21159593,
        "tags": [],
        "transaction_id": 1
      }
    ]
  },
  "test_name": "openvpn",
  "test_runtime": 0.21167471,
  "test_start_time": "2024-04-03 10:56:39",
  "test_version": "0.1.1"
}

```

# Privacy considerations

OpenVPN does not seek to provide anonymity. An adversary can observe that a
user is connecting to OpenVPN servers. OpenVPN servers can also determine the
users location.

Besides this, the [https://github.com/ooni/minivpn](openvpn implementation used in this experiment)
is known to have several minor distinguisher features in
comparison to the reference OpenVPN implementation. While work is being done to
close the gap between the two implementations, a motivated adversary can in
theory infer the usage of probing activity by means of implementation quirks.
However, probing activity is already evident because of the traffic patterns
and timing, so this should not be a high-impact concern in practice.

# Packet capture considerations

This test does not capture packets by default.

A lightweight serialization of exchanged packets is stored under `network_events`. This contains some of the packet metadata at the protocol layer that you would see in, e.g., wireshark's protocol dissector.

# Status and future directions

This test is in experimental state.

Some functionality has been removed compared to previous proposed iterations of
this spec (ICMP ping, urlgrabber), and it's in the roadmap to include them in
future versions of the experiment.

One possible outcome, to be discussed, is the relationship of this experiment
with experiments that measure the behavior for concrete services (i.e.,
experiments adapted to the particularities of concrete VPN service providers).

To this end, it might be beneficial to turn the `openvpn` spec into a library
for implementing concrete openvpn probes.

Also, we might want to abstract the openvpn and wireguard experiments as
different flavors of a single `vpn` experiment (possibly mapping some of the
possible errors at different stages of the connection).

Another potential for improvement includes adding richer bridge information to this
openvpn experiment (the only bridge we are aware of right now is obfs4). The
obfuscated vpn tunnel could be a different experiment, but it would make sense
to simply treat it as a different input variable so to be able to easily perform
comparisons.


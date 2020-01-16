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
  "measurement_start_time": "2020-01-16 14:41:31",
  "test_runtime": 0.72184469,
  "probe_asn": "AS30722",
  "probe_cc": "IT",
  "probe_ip": "127.0.0.1",
  "report_id": "20200116T144131Z_AS30722_VCY4K6dIcplLIGEQo4NnDCPyrVBMDjG99fIaNWJMuyz5gEihD5",
  "resolver_asn": "AS15169",
  "resolver_ip": "172.217.34.4",
  "resolver_network_name": "Google LLC",
  "software_name": "miniooni",
  "software_version": "0.1.0-dev",
  "test_keys": {
    "targets": {
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
            "t": 0.413078
          },
          {
            "conn_id": 3,
            "failure": null,
            "num_bytes": 6247,
            "operation": "write",
            "proto": "tcp",
            "t": 0.415011
          },
          {
            "conn_id": 3,
            "failure": null,
            "num_bytes": 2608,
            "operation": "read",
            "proto": "tcp",
            "t": 0.721159
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
            "t": 0.413078
          }
        ],
        "tls_handshakes": null
      }
    }
  },
  "test_name": "tor",
  "test_start_time": "2020-01-16 14:41:31",
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

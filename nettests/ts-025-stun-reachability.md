# Specification version number

2020-06-01-000

* _status_: experimental

# Specification name

STUN reachability (`stun_reachability`)

# Test preconditions

None

# Expected impact

Detect whether [STUN](https://en.wikipedia.org/wiki/STUN) is working in a specific network.

# Expected inputs

This nettest will test all the stun server endpoints (i.e. `"<domain>:<port>"`) passed
as input. If no input is provided, `"stun.l.google.com:19302"` is tested.

# Test description

For each STUN input endpoint, this nettest sends a binding request to the specified
endpoint and receives the corresponding response. If a valid response is received, then
the nettest is successful, otherwise it failed.

# Expected output

## Parent data format

- `df-002-dnst`
- `df-007-errors`
- `df-008-netevents`

## Required output data

```JSON
{
  "endpoint": "",
  "failure": null,
  "network_events": [],
  "queries": []
}
```

- `endpoint` (`string`): STUN endpoint that we are using;

- `failure` (`string|null`): string indicating the error that occurred
or `null` if no error occurred (see `df-007-errors`);

- `network_events` (`[]NetworkEvent`): see `df-008-netevents`;

-  `queries` (`[]Query`): see `df-002-dnst`.

## Example output sample

```JSON
{
  "annotations": {
    "assets_version": "20200529153246",
    "engine_name": "miniooni",
    "engine_version": "0.12.0",
    "platform": "macos"
  },
  "data_format_version": "0.2.0",
  "extensions": {
    "dnst": 0,
    "netevents": 0
  },
  "input": null,
  "measurement_start_time": "2020-06-01 16:51:44",
  "probe_asn": "AS30722",
  "probe_cc": "IT",
  "probe_ip": "127.0.0.1",
  "probe_network_name": "VODAFONE-IT-ASN Vodafone Italia S.p.A.",
  "report_id": "20200601T165144Z_AS30722_qwaNcWHznyBuj2Unhq3YpL1fJ1pV1WCs98xZHDjcUL8U6WP3Ot",
  "resolver_asn": "AS30722",
  "resolver_ip": "91.80.36.85",
  "resolver_network_name": "VODAFONE-IT-ASN Vodafone Italia S.p.A.",
  "software_name": "miniooni",
  "software_version": "0.12.0",
  "test_keys": {
    "endpoint": "stun.l.google.com:19302",
    "failure": null,
    "network_events": [
      {
        "failure": null,
        "operation": "resolve_start",
        "t": 2.336e-05
      },
      {
        "failure": null,
        "operation": "resolve_done",
        "t": 0.04526879
      },
      {
        "address": "108.177.15.127:19302",
        "failure": null,
        "operation": "connect",
        "proto": "udp",
        "t": 0.045541248
      },
      {
        "failure": null,
        "num_bytes": 20,
        "operation": "write",
        "t": 0.04578789
      },
      {
        "failure": null,
        "num_bytes": 32,
        "operation": "read",
        "t": 0.084153449
      }
    ],
    "queries": [
      {
        "answers": [
          {
            "asn": 15169,
            "as_org_name": "GOOGLE",
            "answer_type": "A",
            "ipv4": "108.177.15.127",
            "ttl": null
          }
        ],
        "engine": "system",
        "failure": null,
        "hostname": "stun.l.google.com",
        "query_type": "A",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "",
        "t": 0.04526879
      },
      {
        "answers": [
          {
            "asn": 15169,
            "as_org_name": "GOOGLE",
            "answer_type": "AAAA",
            "ipv6": "2a00:1450:400c:c07::7f",
            "ttl": null
          }
        ],
        "engine": "system",
        "failure": null,
        "hostname": "stun.l.google.com",
        "query_type": "AAAA",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "",
        "t": 0.04526879
      }
    ]
  },
  "test_name": "stun_reachability",
  "test_runtime": 0.085115757,
  "test_start_time": "2020-06-01 16:51:44",
  "test_version": "0.0.1"
}
```

# Privacy considerations

The STUN server response will contain the user's IP address. For this reason we
should not save the STUN server response into `network_events`.

# Packet capture considerations

This test does not capture packets by default.

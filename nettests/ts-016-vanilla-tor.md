# Specification version number

2022-05-10

This version of the specification documents the Go implementation of
`vanilla_tor`, written on 2022-05-10. The
[previous](https://github.com/ooni/spec/blob/fc05b9a12f4202d824f2bcdb52b4eacfbb914a4e/nettests/ts-016-vanilla-tor.md)
(and slightly incompatible!) version of this specification documents the original and
obsolete Python implementation inside `ooni/probe-legacy`.

* _status_: experimental

# Specification name

`vanilla_tor` (Vanilla Tor)

# Test preconditions

* An internet connection

* The `tor` binary installed on the system

# Expected impact

Ability to determine if Tor in it's default configuration is able to bootstrap
or at what point in bootstrapping it fails.

# Expected inputs

None

# Test description

The test will run the tor executable and collect logs. The bootstrap
will either succeed or eventually time out.

# Expected output

## Parent data format

* none

However, this test tries to produce a data structure as
similar as possible to `ts-030-torsf.md`.

## Semantics

```JSON
{
    "bootstrap_time": 1.1,
    "error": null,
    "failure": null,
    "success": false,
    "timeout": 600,
    "tor_logs": [],
    "tor_progress": 0,
    "tor_progress_tag": "",
    "tor_progress_summary": "",
    "tor_version": "",
    "transport_name": "vanilla"
}
```

where:

- `bootstrap_time` (`float`) is zero if the bootstrap times out and otherwise is
the number of seconds it required to bootstrap;

- `error` (`null | string`) is `null` on success, `timeout-reached` in case of
timeout, and `unknown-error` otherwise (this field only exists for backwards
compatibility with the previous version of the `vanilla_tor` spec);

- `failure` conforms to `df-007-errors`;

- `success` (`bool`) is set to `true` if we bootstrap, to `false` otherwise (this
field only exists for backwards compatibility);

- `timeout` (`float`) is the default timeout for the experiment (in seconds);

- `tor_logs` (`[]string`) is a list of bootstrap-related logs emitted by
the tor daemon during the bootstrap;

- `tor_progress` (`int`) is the progress in the last bootstrap line;

- `tor_progress_tag` (`string`) is the machine readable tag of the last bootstrap line;

- `tor_progress_summary` (`string`) is the human readable description of
the last bootstrap line;

- `tor_version` (`string`) is the version of `tor` we're using;

- `transport_name` (`string`) is always set to `"vanilla"`.

## Incompatibility with ooni/probe-legacy

The `ooni/probe-legacy` implementation used different field names and/or data types as
documented [by the previous version of this spec](
https://github.com/ooni/spec/blob/fc05b9a12f4202d824f2bcdb52b4eacfbb914a4e/nettests/ts-016-vanilla-tor.md).
The following table shows which fields changed since the previous implementation:

| legacy name            | legacy type     | new name      | new type        |
| ---------------------- | --------------- | ------------- | --------------- |
| `tor_log`              | `string`        | `tor_logs`    | `[]string`      |
| `timeout`              | `integer`       | `timeout`     | `float`         |

The _main_ difference between the new and the old implementation is that the new
implementation collects the logs as an array of lines while the old implementation
collects the logs as a single string.

The `timeout` field changed only in its type and it should be possible to parse it
using a language such as Python or JavaScript without major issues, since it's still
a numeric value. Also, the timeout we set is always an integral number of seconds,
which means that most JSON emitters (including
Golang's JSON emitter) will emit an integer (i.e., without a serialized
number without trailing `.0`).

## Possible conclusions

If Tor with the default configuration can successfully bootstrap.

## Example output sample

```JSON
{
  "annotations": {
    "architecture": "arm64",
    "engine_name": "ooniprobe-engine",
    "engine_version": "3.15.0-alpha",
    "platform": "macos"
  },
  "data_format_version": "0.2.0",
  "input": null,
  "measurement_start_time": "2022-05-10 11:31:29",
  "probe_asn": "AS30722",
  "probe_cc": "IT",
  "probe_ip": "127.0.0.1",
  "probe_network_name": "Vodafone Italia S.p.A.",
  "report_id": "",
  "resolver_asn": "AS30722",
  "resolver_ip": "91.80.36.88",
  "resolver_network_name": "Vodafone Italia S.p.A.",
  "software_name": "miniooni",
  "software_version": "3.15.0-alpha",
  "test_keys": {
    "bootstrap_time": 3.620014542,
    "error": null,
    "failure": null,
    "success": true,
    "timeout": 200,
    "tor_logs": [
      "May 10 13:31:26.000 [notice] Bootstrapped 0% (starting): Starting",
      "May 10 13:31:26.000 [notice] Bootstrapped 5% (conn): Connecting to a relay",
      "May 10 13:31:26.000 [notice] Bootstrapped 10% (conn_done): Connected to a relay",
      "May 10 13:31:26.000 [notice] Bootstrapped 14% (handshake): Handshaking with a relay",
      "May 10 13:31:26.000 [notice] Bootstrapped 15% (handshake_done): Handshake with a relay done",
      "May 10 13:31:26.000 [notice] Bootstrapped 20% (onehop_create): Establishing an encrypted directory connection",
      "May 10 13:31:26.000 [notice] Bootstrapped 25% (requesting_status): Asking for networkstatus consensus",
      "May 10 13:31:26.000 [notice] Bootstrapped 30% (loading_status): Loading networkstatus consensus",
      "May 10 13:31:27.000 [notice] Bootstrapped 40% (loading_keys): Loading authority key certs",
      "May 10 13:31:27.000 [notice] Bootstrapped 45% (requesting_descriptors): Asking for relay descriptors",
      "May 10 13:31:28.000 [notice] Bootstrapped 50% (loading_descriptors): Loading relay descriptors",
      "May 10 13:31:29.000 [notice] Bootstrapped 55% (loading_descriptors): Loading relay descriptors",
      "May 10 13:31:29.000 [notice] Bootstrapped 61% (loading_descriptors): Loading relay descriptors",
      "May 10 13:31:29.000 [notice] Bootstrapped 70% (loading_descriptors): Loading relay descriptors",
      "May 10 13:31:29.000 [notice] Bootstrapped 75% (enough_dirinfo): Loaded enough directory info to build circuits",
      "May 10 13:31:29.000 [notice] Bootstrapped 80% (ap_conn): Connecting to a relay to build circuits",
      "May 10 13:31:29.000 [notice] Bootstrapped 85% (ap_conn_done): Connected to a relay to build circuits",
      "May 10 13:31:29.000 [notice] Bootstrapped 89% (ap_handshake): Finishing handshake with a relay to build circuits",
      "May 10 13:31:29.000 [notice] Bootstrapped 90% (ap_handshake_done): Handshake finished with a relay to build circuits",
      "May 10 13:31:29.000 [notice] Bootstrapped 95% (circuit_create): Establishing a Tor circuit",
      "May 10 13:31:29.000 [notice] Bootstrapped 100% (done): Done"
    ],
    "tor_progress": 100,
    "tor_progress_tag": "done",
    "tor_progress_summary": "Done",
    "tor_version": "0.4.7.7",
    "transport_name": "vanilla"
  },
  "test_name": "vanilla_tor",
  "test_runtime": 3.8545842500000003,
  "test_start_time": "2022-05-10 11:31:26",
  "test_version": "0.2.0"
}
```

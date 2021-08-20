# Specification version number

2021-06-18-001

* _status_: experimental

# Specification name

`torsf` (Tor using snowflake)

# Test preconditions

* An internet connection
* The `tor` binary installed on the system

# Expected impact

Ability to detect if `tor` would bootstrap using the Snowflake
pluggable transport (PT) within a reasonable timeout.

# Expected inputs

None

# Test description

This test starts `tor` using the following command line arguments:

- `UseBridges` `1`
- `ClientTransportPlugin` `'snowflake socks5 127.0.0.1:PORT'`
- `Bridge` `'snowflake ADDR_PORT FINGERPRINT'`

where `PORT` is a port on the local host managed by OONI that speaks
the SOCKS5 protocol, and `ADDR_PORT` and `FINGERPRINT` describe a
Snowflake bridge.

The listening port will accept connections from the `tor` daemon and
forward bytes back and forth over a Snowflake connection created using
Snowflake's PTv2.1 capabilities.

The result of this test can be one of the following:

1. we cannot create a listening port on the local host, which is
considered as a failure to start the test up;

2. the `tor` daemon times out when performing the bootstrap;

3. we successfully complete the bootstrap.

# Expected output

## Parent data format

* none

## Semantics

```JSON
{
    "bootstrap_time": 1.1,
    "failure": null
}
```

where:

- `bootstrap_time` (`float`) is zero if the bootstrap times out and otherwise is
the number of seconds it required to bootstrap;

- `failure` conforms to `df-007-errors`.

## Possible conclusions

Whether we can successfully bootstrap `tor` using the Snowflake PT.

## Example output sample

```json
{
  "annotations": {
    "engine_name": "ooniprobe-engine",
    "engine_version": "3.11.0-alpha",
    "platform": "macos"
  },
  "data_format_version": "0.2.0",
  "input": null,
  "measurement_start_time": "2021-06-18 10:34:27",
  "probe_asn": "AS30722",
  "probe_cc": "IT",
  "probe_ip": "127.0.0.1",
  "probe_network_name": "Vodafone Italia S.p.A.",
  "report_id": "",
  "resolver_asn": "AS30722",
  "resolver_ip": "91.80.36.92",
  "resolver_network_name": "Vodafone Italia S.p.A.",
  "software_name": "miniooni",
  "software_version": "3.11.0-alpha",
  "test_keys": {
    "bootstrap_time": 41.677585167,
    "failure": null
  },
  "test_name": "torsf",
  "test_runtime": 41.890146875,
  "test_start_time": "2021-06-18 10:34:27",
  "test_version": "0.1.0"
}
```

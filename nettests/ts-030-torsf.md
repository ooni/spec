# Specification version number

2022-05-10

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

This test does not take any input. Yet, it accepts options when using
`miniooni` via the `-O` command line flag.

These options are available:

- `DisablePersistentDatadir` (type: `bool`, default value: `false)`: this
option allows to disable using a persistent `tor` datadir for the `torsf`
experiment. The default is to use a persistent datadir.

- `DisableProgress` (type: `bool`, default value: `false`): this option
allows you to disable printing progress.

- `RendezvousMethod` (type: `str`, default value: `""`): this option
chooses between the `"amp"` and `"domain_fronting"` Snowflake rendezvous
methods. A `""` value for this option indicates we should be using
the default rendezvous method (`"domain_fronting"` as of 2022-02-07).

These options and their default values may change at a later time, once we have
improved our understanding of the `torsf` experiment. See
[probe#2004](https://github.com/ooni/probe/issues/2004) for more context
on what led us to add these options.

# Test description

This test starts `tor` using the following command line arguments:

- `UseBridges` `1`
- `ClientTransportPlugin` `'snowflake socks5 127.0.0.1:PORT'`
- `Bridge` `'snowflake ADDR_PORT FINGERPRINT'`

where `PORT` is a port on the local host managed by OONI that speaks
the SOCKS5 protocol, and `ADDR_PORT` and `FINGERPRINT` describe a
Snowflake bridge.

If `DisablePersistentDatadir` is `false`, `torsf` will use a persistent
datadir at `$OONI_HOME/tunnel/torsf/tor` otherwise the datadir will
be inside a temporary directory. Using a persistent datadir means that
`tor` will already have some cached information to make the bootstrap
faster when using Snowflake (more on this later).

The listening port will accept connections from the `tor` daemon and
forward bytes back and forth over a Snowflake connection created using
Snowflake's PTv2.1 capabilities. Depending on the `RendezvousMethod`
config value, Snowflake will use `"amp"` or `"domain_fronting"` as the
rendezvous method.

The result of this test can be one of the following:

1. we cannot create a listening port on the local host, which is
considered as a failure to start the test up;

2. the `tor` daemon times out when performing the bootstrap;

3. we successfully complete the bootstrap.

# Expected output

## Parent data format

* none

However, this test tries to produce a data structure as
similar as possible to `ts-016-vanilla-tor.md`.

## Semantics

```JSON
{
    "bootstrap_time": 1.1,
    "error": null,
    "failure": null,
    "success": false,
    "timeout": 600,
    "persistent_datadir": true,
    "rendezvous_method": "domain_fronting",
    "tor_logs": [],
    "tor_progress": 0,
    "tor_progress_tag": "",
    "tor_progress_summary": "",
    "tor_version": "",
    "transport_name": "snowflake"
}
```

where:

- `bootstrap_time` (`float`) is zero if the bootstrap times out and otherwise is
the number of seconds it required to bootstrap;

- `error` (`null | string`) is `null` on success, `timeout-reached` in case of
timeout, and `unknown-error` otherwise (this field only exists for backwards
compatibility with the previous version of the `vanilla_tor` spec);

- `failure` conforms to `df-007-errors`;

- `persistent_datadir` (`bool`) is the value of the `PersistentDatadir` option;

- `rendezvous_method` (`string`) is the value of the `RendezvousMethod` option;

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

*Note*: unreleased versions of ooniprobe used `default_timeout` instead of
`timeout` between 2022-04-12 and 2022-05-10.

## Possible conclusions

Whether we can successfully bootstrap `tor` using the Snowflake PT. See also
the [data analysis considerations](#data-analysis-considerations) section below.

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
  "measurement_start_time": "2022-05-10 12:39:51",
  "probe_asn": "AS30722",
  "probe_cc": "IT",
  "probe_ip": "127.0.0.1",
  "probe_network_name": "Vodafone Italia S.p.A.",
  "report_id": "",
  "resolver_asn": "AS30722",
  "resolver_ip": "91.80.36.92",
  "resolver_network_name": "Vodafone Italia S.p.A.",
  "software_name": "miniooni",
  "software_version": "3.15.0-alpha",
  "test_keys": {
    "bootstrap_time": 18.437362125,
    "error": null,
    "failure": null,
    "success": true,
    "persistent_datadir": true,
    "rendezvous_method": "domain_fronting",
    "timeout": 600,
    "tor_logs": [
      "May 10 14:39:32.000 [notice] Bootstrapped 0% (starting): Starting",
      "May 10 14:39:33.000 [notice] Bootstrapped 1% (conn_pt): Connecting to pluggable transport",
      "May 10 14:39:33.000 [notice] Bootstrapped 2% (conn_done_pt): Connected to pluggable transport",
      "May 10 14:39:33.000 [notice] Bootstrapped 10% (conn_done): Connected to a relay",
      "May 10 14:39:46.000 [notice] Bootstrapped 14% (handshake): Handshaking with a relay",
      "May 10 14:39:46.000 [notice] Bootstrapped 15% (handshake_done): Handshake with a relay done",
      "May 10 14:39:46.000 [notice] Bootstrapped 45% (requesting_descriptors): Asking for relay descriptors",
      "May 10 14:39:46.000 [notice] Bootstrapped 50% (loading_descriptors): Loading relay descriptors",
      "May 10 14:39:49.000 [notice] Bootstrapped 57% (loading_descriptors): Loading relay descriptors",
      "May 10 14:39:50.000 [notice] Bootstrapped 62% (loading_descriptors): Loading relay descriptors",
      "May 10 14:39:51.000 [notice] Bootstrapped 70% (loading_descriptors): Loading relay descriptors",
      "May 10 14:39:51.000 [notice] Bootstrapped 75% (enough_dirinfo): Loaded enough directory info to build circuits",
      "May 10 14:39:51.000 [notice] Bootstrapped 90% (ap_handshake_done): Handshake finished with a relay to build circuits",
      "May 10 14:39:51.000 [notice] Bootstrapped 95% (circuit_create): Establishing a Tor circuit",
      "May 10 14:39:51.000 [notice] Bootstrapped 100% (done): Done"
    ],
    "tor_progress": 100,
    "tor_progress_tag": "done",
    "tor_progress_summary": "Done",
    "tor_version": "0.4.7.7",
    "transport_name": "snowflake"
  },
  "test_name": "torsf",
  "test_runtime": 18.948177959,
  "test_start_time": "2022-05-10 12:39:32",
  "test_version": "0.3.0"
}
```

## Data analysis considerations

From [probe#2004](https://github.com/ooni/probe/issues/2004), we know that
_generally_ using a persistent data dir improves the bootstrap time. We have
seen this strategy to be particularly successful on mobile devices.

That said, we have empirically also seen cases of long bootstraps when
using a persistent data dir. So, we cannot conclude _a priori_ that using
a persistent data dir necessarily leads to faster bootstrap times _in
all cases_.

To figure out whether `tor` had enough cached information to perform an
in-theory-faster bootstrap, you should look into the sequence of bootstrap
events. The following bootstrap (which, by the way, too 316 seconds to
complete) did not require `tor` to fetch _additional_ information because
its datadir already contained a fresh cache:

```json
{
    "tor_logs": [
      "Feb 07 12:42:20.000 [notice] Bootstrapped 0% (starting): Starting",
      "Feb 07 12:42:20.000 [notice] Bootstrapped 1% (conn_pt): Connecting to pluggable transport",
      "Feb 07 12:42:20.000 [notice] Bootstrapped 2% (conn_done_pt): Connected to pluggable transport",
      "Feb 07 12:42:20.000 [notice] Bootstrapped 10% (conn_done): Connected to a relay",
      "Feb 07 12:47:32.000 [notice] Bootstrapped 14% (handshake): Handshaking with a relay",
      "Feb 07 12:47:33.000 [notice] Bootstrapped 15% (handshake_done): Handshake with a relay done",
      "Feb 07 12:47:33.000 [notice] Bootstrapped 75% (enough_dirinfo): Loaded enough directory info to build circuits",
      "Feb 07 12:47:34.000 [notice] Bootstrapped 90% (ap_handshake_done): Handshake finished with a relay to build circuits",
      "Feb 07 12:47:34.000 [notice] Bootstrapped 95% (circuit_create): Establishing a Tor circuit",
      "Feb 07 12:47:37.000 [notice] Bootstrapped 100% (done): Done"
    ],
 }
```

Conversely, this bootstrap required `tor` to fetch additional information (and, again,
anecdotally, it took 67 seconds to complete):

```json
{
    "tor_logs": [
      "Feb 07 12:38:29.000 [notice] Bootstrapped 0% (starting): Starting",
      "Feb 07 12:38:29.000 [notice] Bootstrapped 1% (conn_pt): Connecting to pluggable transport",
      "Feb 07 12:38:29.000 [notice] Bootstrapped 2% (conn_done_pt): Connected to pluggable transport",
      "Feb 07 12:38:29.000 [notice] Bootstrapped 10% (conn_done): Connected to a relay",
      "Feb 07 12:38:43.000 [notice] Bootstrapped 14% (handshake): Handshaking with a relay",
      "Feb 07 12:38:45.000 [notice] Bootstrapped 15% (handshake_done): Handshake with a relay done",
      "Feb 07 12:38:45.000 [notice] Bootstrapped 20% (onehop_create): Establishing an encrypted directory connection",
      "Feb 07 12:38:46.000 [notice] Bootstrapped 25% (requesting_status): Asking for networkstatus consensus",
      "Feb 07 12:38:49.000 [notice] Bootstrapped 30% (loading_status): Loading networkstatus consensus",
      "Feb 07 12:38:52.000 [notice] Bootstrapped 45% (requesting_descriptors): Asking for relay descriptors",
      "Feb 07 12:38:52.000 [notice] Bootstrapped 58% (loading_descriptors): Loading relay descriptors",
      "Feb 07 12:38:58.000 [notice] Bootstrapped 65% (loading_descriptors): Loading relay descriptors",
      "Feb 07 12:39:04.000 [notice] Bootstrapped 73% (loading_descriptors): Loading relay descriptors",
      "Feb 07 12:39:04.000 [notice] Bootstrapped 75% (enough_dirinfo): Loaded enough directory info to build circuits",
      "Feb 07 12:39:05.000 [notice] Bootstrapped 76% (ap_conn_pt): Connecting to pluggable transport to build circuits",
      "Feb 07 12:39:05.000 [notice] Bootstrapped 77% (ap_conn_done_pt): Connected to pluggable transport to build circuits",
      "Feb 07 12:39:05.000 [notice] Bootstrapped 85% (ap_conn_done): Connected to a relay to build circuits",
      "Feb 07 12:39:13.000 [notice] Bootstrapped 89% (ap_handshake): Finishing handshake with a relay to build circuits",
      "Feb 07 12:39:15.000 [notice] Bootstrapped 90% (ap_handshake_done): Handshake finished with a relay to build circuits",
      "Feb 07 12:39:15.000 [notice] Bootstrapped 95% (circuit_create): Establishing a Tor circuit",
      "Feb 07 12:39:36.000 [notice] Bootstrapped 100% (done): Done"
    ],
}
```

Thus, we can say that there is enough cached information if the bootstrap jumps from
`handshake_done` to `enough_dirinfo` without emitting the `onehop_create`, `requesting_status`
and `requesting_descriptors` bootstrap events.

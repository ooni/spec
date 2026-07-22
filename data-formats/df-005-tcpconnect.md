# TCPConnect Data Format

This document describes the keys with `test_keys` that all experiments
performing TCP connects SHOULD populate, possibly using directly the
specific template code. See this directory's [README](README.md) for the
basic concepts.

| Name       | `tcpconnect` |
|------------|--------------|
| Version    | 0            |

## Specification

```JSON
{
  "tcp_connect": [],
}
```

- `tcp_connect` (`[]TCPConnect`): list of TCPConnect objects. See below.

## TCPConnect

```JavaScript
{
    // fields currently used as of 2022-09-08
    "ip": "149.154.171.5",
    "port": 80,
    "status": {},
    "t0": 1.011,
    "t": 1.114,
    "tags": [],
    "transaction_id": 1,

    // deprecated or unused fields
    "conn_id": 141,
    "dial_id": 177171,
}
```

- `conn_id` (`int`; optional; since 2020-01-11; deprecated): identifier of the connection. See
the discussion in `df-008-netevents.md`.

- `dial_id` (`int`; optional; since 2020-01-11; deprecated): identifier of a dialing
operation (i.e. name resolution followed by connect). See the
discussion in `df-002-dnst.md`.

- `ip` (`string`): IP address we're connecting to.

- `port` (`int`): port we're connecting to.

- `status` (`Status`): object describing the results.

- `t0` (`float`): number of seconds elapsed since `measurement_start_time`
measured in the moment in which we started the operation (`t - t0` gives you
the amount of time spent performing the operation);

- `t` (`float`): number of seconds elapsed since `measurement_start_time`
measured in the moment in which `failure` is determined (`t - t0` gives you
the amount of time spent performing the operation);

- `tags` (`[]string`; optional): list of tags for this event. This is useful to
understand what part of a complex measurement generated an event.

- `transaction_id` (`int`; optional; since 2020-01-11): the set of operations
to which this event belongs to (typically an HTTP transaction or a DNS
round trip). A zero or missing value means we don't know the transaction
to which this code belongs to.

## Status

```JavaScript
{
    "blocked": null, // only WebConnectivity, new nettests SHOULD NOT include it
    "failure": null,
    "success": true
}
```

- `blocked` (`string`; nullable; deprecated; optional): field used only by Web
Connectivity to indicate whether this endpoint is blocked. New experiments
SHOULD NOT use this field and SHOULD instead use distinct keys to represent
network observations and the probe's analysis.

- `failure` (`string`; nullable): if there was an error, this field is
a string indicating the error, otherwise it MUST be `null`. Some older versions of OONI Probe
set this to `false` instead of `null`.

- `success` (`bool`): true if failure is `null`, false otherwise.

## Example

In the following example we've omitted all the keys that are
not relevant to the HTTP data format:

```JSON
{
  "ip": "93.184.216.34",
  "port": 443,
  "status": {
    "blocked": false,
    "failure": null,
    "success": true
  },
  "t0": 0.450831,
  "t": 0.595157,
  "transaction_id": 4
}
```

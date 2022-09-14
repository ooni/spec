# NetEvents Data Format

This document describes the keys with `test_keys` that experiments
MAY use to include network-level events. See this directory's
[README](README.md) for the basic concepts.

| Name       | `netevents` |
|------------|-------------|
| Version    | 0           |

## Specification

```JSON
{
    "network_events": []
}
```

- `network_events` (`[]Event`): list of events.

## Event

```JavaScript
{
    // fields currently used as of 2022-09-08
    "address": "1.1.1.1:443",
    "failure": "connection_reset",
    "num_bytes": 4114,
    "operation": "read",
    "proto": "tcp",
    "t0": 1.001,
    "t": 1.174,
    "tags": [],
    "transaction_id": 1,

    // deprecated or unused fields
    "conn_id": 11,
    "dial_id": 4,
}
```

- `address` (`string`; optional): address for `connect`.

- `conn_id` (`int`; optional; deprecated): identifier of this connection (see below). When
zero, it means we don't know the conn ID. SHOULD be omitted when zero.

- `dial_id` (`int`; optional; since 2020-01-11; deprecated): identifier of a dialing
operation (i.e. name resolution followed by connect). See the
discussion in `df-002-dnst.md`.

- `failure` (`string`; nullable): if there was an error, this field is
a string indicating the error, otherwise it MUST be `null`.

- `num_bytes` (`int`; optional): number of bytes transferred by
`read` or `write`.

- `operation` (`string`): one of `connect`, `read`, and `write`.

- `proto` (`string`; optional): protocol for `connect` (`tcp` or `udp`).

- `t0` (`float`): number of seconds elapsed since `measurement_start_time`
measured in the moment in which we started the operation (`t - t0` gives you
the amount of time spent performing the operation);

- `t` (`float`): number of seconds elapsed since `measurement_start_time`
measured in the moment in which `failure` is determined (`t - t0` gives you
the amount of time spent performing the operation);

- `tags` (`[]string`): list of tags for this event. This is useful to
understand what part of a complex measurement generated an event.

- `transaction_id` (`int`; optional; since 2020-01-11): the set of operations
to which this event belongs to (typically an HTTP transaction or a DNS
round trip). A zero or missing value means we don't know the transaction
to which this code belongs to.

## Connection ID and Life Cycle (deprecated)

When a connection is created you see a `connect` event with a
specific `conn_id` and no failure. Subsequently you should see
one or more `read` or `write` with the same `conn_id`.

If you see another `connect` with the same `conn_id`, this means
that the implementation is reusing connection IDs, and you should
henceforth consider such ID as a new connection.

Note that this is perfectly normal. A probe implementation
MAY reuse the `conn_id` in the same measurement session.

## Example

In the following example we've omitted all the keys that are
not relevant to the netevents data format:

```JSON
{
  "address": "93.184.216.34:443",
  "failure": null,
  "num_bytes": 99,
  "operation": "read",
  "proto": "tcp",
  "t0": 0.602109,
  "t": 0.746866,
  "transaction_id": 4
}
```

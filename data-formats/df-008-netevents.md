# NetEvents Data Format

This document describes the keys with `test_keys` that experiments
MAY use to include network-level events. See this directory's
[README](README.md) for the basic concepts.

## Specification

```JSON
{
    "network_events": []
}
```

- `network_events` (`[]Event`): list of events.

## Event

```JSON
{
    "address": "1.1.1.1:443",
    "conn_id": 11,
    "failure": "connection_reset",
    "num_bytes": 4114,
    "operation": "read",
    "proto": "tcp",
    "t": 1.174
}
```

- `address` (`string`; optional): address for `connect`.

- `conn_id` (`int`): identifier of this connection (see below).

- `failure` (`string`; nullable): if there was an error, this field is
a string indicating the error, otherwise it MUST be `null`.

- `num_bytes` (`int`; optional): number of bytes transferred by
`read` or `write`.

- `operation` (`string`): one of `connect`, `read`, and `write`.

- `proto` (`string`; optional): protocol for `connect` (`tcp` or `udp`).

- `t` (`float`): number of seconds elapsed since `measurement_start_time`.

## Connection ID and Life Cycle

When a connection is created you see a `connect` event with a
specific `conn_id` and no failure. Subsequently you should see
one or more `read` or `write` with the same `conn_id`.

If you see another `connect` with the same `conn_id`, this means
that the implementation is reusing connection IDs, and you should
henceforth consider such ID as a new connection.

## Example

In the following example we've omitted all the keys that are
not relevant to the TCP data format:

```JSON
{
    "test_keys": {
        "network_events": [{
            "address": "1.1.1.1:444",
            "conn_id": 11,
            "failure": "connection_refused",
            "operation": "connect",
            "proto": "tcp",
            "t": 0.11
        }, {
            "address": "1.1.1.1:443",
            "conn_id": 12,
            "failure": null,
            "operation": "connect",
            "proto": "tcp",
            "t": 0.16
        }, {
            "conn_id": 12,
            "failure": null,
            "num_bytes": 1024,
            "operation": "write",
            "t": 0.17
        }, {
            "conn_id": 12,
            "failure": null,
            "num_bytes": 5110,
            "operation": "read",
            "t": 0.44
        }]
    }
}
```

# TCPConnect Data Format

This document describes the keys with `test_keys` that all experiments
performing TCP connects SHOULD populate, possibly using directly the
specific template code. See this directory's [README](README.md) for the
basic concepts.

|------------|--------------|
| Name       | `tcpconnect` |
| Version    | 0            |

## Specification

```JSON
{
  "tcp_connect": [],
}
```

- `tcp_connect` (`[]TCPConnect`): list of TCPConnect objects. See below.

## TCPConnect

```JSON
{
    "conn_id": 141,
    "dial_id": 177171,
    "ip": "149.154.171.5",
    "port": 80,
    "status": {},
    "t": 1.114,
    "transaction_id": 1
}
```

- `conn_id` (`int`; optional; since v0.3.3): identifier of the connection. See
the discussion in `df-008-netevents.md`.

- `dial_id` (`int`; optional; since v0.3.3): identifier of a dialing
operation (i.e. name resolution followed by connect). See the
discussion in `df-002-dnst.md`.

- `ip` (`string`): IP address we're connecting to.

- `port` (`int`): port we're connecting to.

- `status` (`Status`): object describing the results.

- `t` (`float`): number of seconds elapsed since `measurement_start_time`
measured when `connect` is complete.

- `transaction_id` (`int`; optional; since v0.3.4): if present, this is the
ID of the HTTP transaction that caused this TCP connect.

## Status

```JSON
{
    "failure": null,
    "success": true
}
```

- `failure` (`string`; nullable): if there was an error, this field is
a string indicating the error, otherwise it MUST be `null`.

- `success` (`bool`): true if failure is `null`, false otherwise.

## Example

In the following example we've omitted all the keys that are
not relevant to the HTTP data format:

```JSON
{
  "test_keys": {
    "tcp_connect": [
      {
        "conn_id": 5,
        "dial_id": 555,
        "ip": "149.154.171.5",
        "port": 80,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 1.114,
        "transaction_id": 1
      }
    ]
  }
}
```

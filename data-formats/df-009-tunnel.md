# Tunnel Data Format

This document describes the keys with `test_keys` that experiments
MAY use when they're using a tunnel, e.g., psiphon. See this directory's
[README](README.md) for the basic concepts.

| Name       | `tunnel` |
|------------|----------|
| Version    | 0        |

When an implementation includes `tunnel` in the `extensions` it merely
means that the experiment COULD be using a `tunnel`. To detect whether a
tunnel was used, you need to check the `test_keys.tunnel` field.

## Specification

```JSON
{
    "bootstrap_time": 6.1,
    "failure": null,
    "socksproxy": "127.0.0.1:9050",
    "tunnel": "psiphon"
}
```

- `bootstrap_time` (`float`; optional): number of seconds it took to bootstrap
the tunnel. This field is omitted if there is no tunnel. (See also the
description of `failure` below).

- `failure` (`string`; nullable): if there was an error, this field is
a string indicating the error, otherwise it MUST be `null`. Note that this
field is also defined by other specifications. When there is an error in
bootstrapping the tunnel, `bootstrap_time` is present and set to zero, the
`tunnel` field is present, and this value is not `null`. If an error instead
happens after the tunnel bootstrap, the `bootstrap_time` is nonzero.

- `socksproxy` (`string`; optional): address of the SOCKS proxy being
used. Omit or set to `null` if no SOCKS proxy is being used. The format
to be used is `1.2.3.4:54321` for IPv4 and `[::1234]:54321` for IPv6.

- `tunnel` (`string`; optional): not provided if there is no tunnel, otherwise
one of `"psiphon"` or `"tor"` when there is a tunnel.

## Example

In the following example we've omitted all the keys that are
not relevant to the tunnel data format:

```JSON
{
    "test_keys": {
        "bootstrap_time": 6.1,
        "failure": null,
        "socksproxy": "127.0.0.1:9050",
        "tunnel": "psiphon"
    }
}
```

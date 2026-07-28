# ICMP Data Format

This document describes the keys with `test_keys` that all experiments
using ICMP SHOULD populate, possibly using directly the specific template
code. See this directory's [README](README.md) for the basic concepts.

| Name       | `icmp` |
|------------|--------|
| Version    | 0      |

## Specification

```JSON
{
    "messages": []
}
```

- `messages` (`[] Message`): list of message objects. See below.

## Message

```Javascript
{
    "timeout": "no",
    "connected": "no",
    "error": "no",
    "source_ip": "1.2.3.4",
    "type": 0,
    "code": 0,
    "quote": {},
    "t0": 1785153856079
    "t": 1785153856080
}
```

- `timeout` (`string`): string describing whether the TTL-limited probe timed out without receiving an ICMP message in response

- `connected` (`string`): string describing whether the TTL-limited probe successfully connected to the destination IP address of the probe

- `error` (`string`): string describing any errors that occur on the socket

- `source_ip` (`string`): the source IP address of the ICMP message

- `type` (`int`): the type of the ICMP message

- `code` (`int`): the code of the ICMP message

- `quote` (`Quote`): object describing the IP header and subsequent 8 bytes of the original packet

- `t0` (`float64`): the time when the TTL-limited probe is sent, represented in terms of the UNIX epoch

- `t` (`float64`): the time when the ICMP message triggered via the TTL-limited probe is received, represented in terms of the UNIX epoch

## Quote

```Javascript
{
    "source_ip": "1.2.3.4",
    "destination_ip": "5.6.7.8",
    "protocol": "tcp",
    "source_port": 7342,
    "destination_port": 80,
    "tcp_sequence_number": 123456789,
    "udp_length": null,
    "udp_checksum": null
}
```

- `source_ip` (`string`): the source IP address of the original quoted packet

- `destination_ip` (`string`): the destination IP address of the original quoted packet

- `protocol` (`string`): the protocol of the original quoted packet

- `source_port` (`int`): the source port of the original quoted packet

- `destination_port` (`int`): the destination port of the original quoted packet

- `tcp_sequence_number` (`int`): the TCP sequence number of the original quoted packet, if the protocol is tcp

- `udp_length` (`int`): the length of the original quoted packet, if the protocol is udp

- `udp_checksum` (`int`): the checksum of the original quoted packet, if the protocol is udp

## Example

In the following example we've omitted all the keys that are not relevant to the ICMP data format:

```JSON
{
    "timeout": "no",
    "connected": "",
    "error": "",
    "source_ip": "148.113.176.252",
    "type": 11,
    "code": 0,
    "quote": {
        "protocol": 6,
        "source_port": 46828,
        "destination_port": 443,
        "tcp_sequence_number": 2972880068,
        "udp_length": 0,
        "udp_checksum": 0
    },
    "t0": 1785236311439,
    "t": 1785236311439
}
```
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
    "source_ip": "1.2.3.4",
    "destination_ip": "5.6.7.8",
    "type": 0,
    "code": 0,
    "quote": {}
}
```

- `source_ip` (`string`): the source IP address of the ICMP message

- `destination_ip` (`string`): the destination IP address of the ICMP message

- `type` (`int`): the type of the ICMP message

- `code` (`int`): the code of the ICMP message

- `quote` (`Quote`): object describing the IP header and subsequent 8 bytes of the original packet

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

- `source_ip` (`string`): the source IP address of the original packet

- `destination_ip` (`string`): the destination IP address of the original packet

## Example

In the following example we've omitted all the keys that are not relevant to the ICMP data format:

```Javascript
{
    "messages": [{
        
    }
    ]
}
```
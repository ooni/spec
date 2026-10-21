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

```JSON
{
    "timeout": false,
    "connected": false,
    "error": "",
    "source_ip_prefix": "148.113.176.252",
    "source_ip_country_code": "CA",
    "source_ip_asn": 16276,
    "source_ip_asn_org": "OVH SAS",
    "type": 11,
    "code": 0,
    "quote": {},
    "t0": 0.054354953,
    "t": 0.054706712
}
```

- `timeout` (`bool`): string describing whether the TTL-limited probe timed out without receiving an ICMP message in response

- `connected` (`bool`): string describing whether the TTL-limited probe successfully connected to the destination IP address of the probe

- `error` (`string`): string describing any errors that occur on the socket

- `source_ip` (`string`): the source IP address of the ICMP message (will not be populated if PrivacyMode is `advanced`)

- `source_ip_country_code` (`string`): the geolocated country of the source IP address

- `source_ip_asn` (`int`): the AS of the source IP address

- `source_ip_asn_org` (`string`): the AS organization of the source IP address

- `type` (`int`): the type of the ICMP message

- `code` (`int`): the code of the ICMP message

- `quote` (`Quote`): object describing the IP header and subsequent 8 bytes of the original packet (will not be populated if PrivacyMode is `advanced`)

- `t0` (`float64`): number of seconds elapsed since `measurement_start_time` measured in the moment in which we started the operation (`t - t0` gives you the amount of time spent performing the operation)
 
- `t` (`float64`): number of seconds elapsed since `measurement_start_time` measured in the moment in which `failure` is determined (`t - t0` gives you the amount of time spent performing the operation) (will not be populated if PrivacyMode is `advanced`)

## Quote

```JSON
{
    "protocol": "tcp",
    "source_port": 7342,
    "destination_port": 80,
    "tcp_sequence_number": 123456789,
    "udp_length": null,
    "udp_checksum": null
    "remaining_payload": null,
}
```

- `protocol` (`string`): the protocol of the original quoted packet

- `source_port` (`int`): the source port of the original quoted packet

- `destination_port` (`int`): the destination port of the original quoted packet

- `tcp_sequence_number` (`int`): the TCP sequence number of the original quoted packet, if the protocol is tcp

- `udp_length` (`int`): the length of the original quoted packet, if the protocol is udp

- `udp_checksum` (`int`): the checksum of the original quoted packet, if the protocol is udp

- `remaining_payload` (`string`): the bytes of the remaining payload encoded as a Base64 string

## Example

In the following example we've omitted all the keys that are not relevant to the ICMP data format:

```JSON
{
    "timeout": false,
    "connected": false,
    "error": "",
    "source_ip_prefix": "198.27.73.205",
    "source_ip_country_code": "CA",
    "source_ip_asn": 16276,
    "source_ip_asn_org": "OVH SAS",
    "type": 11,
    "code": 0,
    "quote": {
        "protocol": 6,
        "source_port": 53722,
        "destination_port": 443,
        "tcp_sequence_number": 1077918402,
        "udp_length": 0,
        "udp_checksum": 0,
        "remaining_payload": "AAAAAKAC+vCJLAAAAgQFtAQCCAqgxRMSAAAAAAEDAwcAAAAAAAAAAA=="
    },
    "t0": 0.555171312,
    "t": 0.564973274
}
```
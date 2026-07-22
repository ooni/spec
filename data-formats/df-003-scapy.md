# Scapy Data Format

This document describes the keys with `test_keys` that all experiments
sending and receiving data using Scapy template SHOULD populate, possibly
using directly the specific template code. See this directory's
[README](README.md) for the basic concepts.

## Specification

```JSON
{
    "answer_flags": [],
    "answered_packets": [],
    "sent_packets": []
}
```

- `answer_flags` (`[]string`): List of options that are set for determining
how to understand if a received packet is answer to a sent packet (these
only apply to ICMP messages). Zero or more of the following:

    - `ipsrc` means that we check to see if the src and destination ports
    in the ICMP IP citation match.

    - `ipid` means that we look at the IPID in the response to match it up
    to sent packets.

    - `seqack` means that we check if TCP sequence number and ACK match in
    the ICMP citation when processing TCP inside of ICMP.

- `answered_packets` (`[]Packet`): are the packets that match up as
answers according to the rules defined in the `answers_flags` options.

- `sent_packets` is like `answered_packets` except that of course it
contains the packets that have been sent.

## Packet

```JavaScript
{
    "raw_packet": BinaryData(),
    "summary": "string"
}
```

- `raw_packet` (`BinaryData`): encoding of the packet inclusive of IP header
using the `BinaryData` object defined in `df-001-httpt.md`.

- `summary` (`string`): human readable representation of the packet.

## Example

In the following example we've omitted all the keys that are
not relevant to the Scapy data format:

```JSON
{
    "test_keys": {
        "answer_flags": [
            "ipsrc"
        ],
        "answered_packets": [
            {
                "raw_packet": {
                    "data": "RcAAOFqPAAAwAeD/1Ypt6AoAAQQDA6VKAAAAAEUAABxEnwAAAREmvAoAAQTVim3oXIYAFgAI+w0=",
                    "format": "base64"
                },
                "summary": "[<IP  version=4L ihl=5L tos=0xc0 len=56 id=23183 flags= frag=0L ttl=48 proto=icmp chksum=0xe0ff src=213.138.109.232 dst=10.0.1.4 options=[] |<ICMP  type=dest-unreach code=port-unreachable chksum=0xa54a unused=0 |<IPerror  version=4L ihl=5L tos=0x0 len=28 id=17567 flags= frag=0L ttl=1 proto=udp chksum=0x26bc src=10.0.1.4 dst=213.138.109.232 options=[] |<UDPerror  sport=23686 dport=ssh len=8 chksum=0xfb0d |>>>>]"
            },
            {
                "raw_packet": {
                    "data": "RQAAOBGSAAD/AZQuCgABAQoAAQQLAEOQAAAAAEUAABzCWAAAARGpAgoAAQTVim3ocGMAFwAIQO0=",
                    "format": "base64"
                },
                "summary": "[<IP  version=4L ihl=5L tos=0x0 len=56 id=4498 flags= frag=0L ttl=255 proto=icmp chksum=0x942e src=10.0.1.1 dst=10.0.1.4 options=[] |<ICMP  type=time-exceeded code=ttl-zero-during-transit chksum=0x4390 unused=0 |<IPerror  version=4L ihl=5L tos=0x0 len=28 id=49752 flags= frag=0L ttl=1 proto=udp chksum=0xa902 src=10.0.1.4 dst=213.138.109.232 options=[] |<UDPerror  sport=28771 dport=telnet len=8 chksum=0x40ed |>>>>]"
            },
            {
                "raw_packet": {
                    "data": "RcAAOD57AADvAetXW986TwoAAQQLAJ1NAAAAAEUAABwySQAAARE5EgoAAQTVim3ogEgANQAI1yw=",
                    "format": "base64"
                },
                "summary": "[<IP  version=4L ihl=5L tos=0xc0 len=56 id=15995 flags= frag=0L ttl=239 proto=icmp chksum=0xeb57 src=91.223.58.79 dst=10.0.1.4 options=[] |<ICMP  type=time-exceeded code=ttl-zero-during-transit chksum=0x9d4d unused=0 |<IPerror  version=4L ihl=5L tos=0x0 len=28 id=12873 flags= frag=0L ttl=1 proto=udp chksum=0x3912 src=10.0.1.4 dst=213.138.109.232 options=[] |<UDPerror  sport=32840 dport=domain len=8 chksum=0xd72c |>>>>]"
            },
            {
                "raw_packet": {
                    "data": "RcAAOCLEAAAwARjL1Ypt6AoAAQQDA6VKAAAAAEUAABwa6wAACxFGcAoAAQTVim3oZO4AFgAI8qU=",
                    "format": "base64"
                },
                "summary": "[<IP  version=4L ihl=5L tos=0xc0 len=56 id=8900 flags= frag=0L ttl=48 proto=icmp chksum=0x18cb src=213.138.109.232 dst=10.0.1.4 options=[] |<ICMP  type=dest-unreach code=port-unreachable chksum=0xa54a unused=0 |<IPerror  version=4L ihl=5L tos=0x0 len=28 id=6891 flags= frag=0L ttl=11 proto=udp chksum=0x4670 src=10.0.1.4 dst=213.138.109.232 options=[] |<UDPerror  sport=25838 dport=ssh len=8 chksum=0xf2a5 |>>>>]"
            },
            {
                "raw_packet": {
                    "data": "RQAAOBGYAAD/AZQoCgABAQoAAQQLAEOQAAAAAEUAABxnSAAAAREEEwoAAQTVim3oU6f//wAIXcA=",
                    "format": "base64"
                },
                "summary": "[<IP  version=4L ihl=5L tos=0x0 len=56 id=4504 flags= frag=0L ttl=255 proto=icmp chksum=0x9428 src=10.0.1.1 dst=10.0.1.4 options=[] |<ICMP  type=time-exceeded code=ttl-zero-during-transit chksum=0x4390 unused=0 |<IPerror  version=4L ihl=5L tos=0x0 len=28 id=26440 flags= frag=0L ttl=1 proto=udp chksum=0x413 src=10.0.1.4 dst=213.138.109.232 options=[] |<UDPerror  sport=21415 dport=65535 len=8 chksum=0x5dc0 |>>>>]"
            },
            {
                "raw_packet": {
                    "data": "RcAAOEz9AADvAdzVW986TwoAAQQLAJ1NAAAAAEUAABxiIAAAAREJOwoAAQTVim3o9N4fkAAIQzs=",
                    "format": "base64"
                },
                "summary": "[<IP  version=4L ihl=5L tos=0xc0 len=56 id=19709 flags= frag=0L ttl=239 proto=icmp chksum=0xdcd5 src=91.223.58.79 dst=10.0.1.4 options=[] |<ICMP  type=time-exceeded code=ttl-zero-during-transit chksum=0x9d4d unused=0 |<IPerror  version=4L ihl=5L tos=0x0 len=28 id=25120 flags= frag=0L ttl=1 proto=udp chksum=0x93b src=10.0.1.4 dst=213.138.109.232 options=[] |<UDPerror  sport=62686 dport=http_alt len=8 chksum=0x433b |>>>>]"
            },
            {
                "raw_packet": {
                    "data": "RcAAOHZYAADvAbN6W986TwoAAQQLAJ1NAAAAAEUAABwZDgAAARFSTQoAAQTVim3ou3kAUAAIm+A=",
                    "format": "base64"
                },
                "summary": "[<IP  version=4L ihl=5L tos=0xc0 len=56 id=30296 flags= frag=0L ttl=239 proto=icmp chksum=0xb37a src=91.223.58.79 dst=10.0.1.4 options=[] |<ICMP  type=time-exceeded code=ttl-zero-during-transit chksum=0x9d4d unused=0 |<IPerror  version=4L ihl=5L tos=0x0 len=28 id=6414 flags= frag=0L ttl=1 proto=udp chksum=0x524d src=10.0.1.4 dst=213.138.109.232 options=[] |<UDPerror  sport=47993 dport=http len=8 chksum=0x9be0 |>>>>]"
            },
            {
                "raw_packet": {
                    "data": "RQAAqAJHAAD5AalDCpYAMQoAAQQLAH/9AAAABEUAABxL8AAAAhEeawoAAQTVim3oxtsAFgAIkLiqqgAWAAjHuqqqABYACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAD5AwAIAQED8+H/",
                    "format": "base64"
                },
                "summary": "[<IP  version=4L ihl=5L tos=0x0 len=168 id=583 flags= frag=0L ttl=249 proto=icmp chksum=0xa943 src=10.150.0.49 dst=10.0.1.4 options=[] |<ICMP  type=time-exceeded code=ttl-zero-during-transit chksum=0x7ffd unused=4 |<IPerror  version=4L ihl=5L tos=0x0 len=28 id=19440 flags= frag=0L ttl=2 proto=udp chksum=0x1e6b src=10.0.1.4 dst=213.138.109.232 options=[] |<UDPerror  sport=50907 dport=ssh len=8 chksum=0x90b8 |<Padding  load='\\xaa\\xaa\\x00\\x16\\x00\\x08\\xc7\\xba\\xaa\\xaa\\x00\\x16\\x00\\x08\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00 \\x00\\xf9\\x03\\x00\\x08\\x01\\x01\\x03\\xf3\\xe1\\xff' |>>>>>]"
            },
            {
                "raw_packet": {
                    "data": "RQAAOFaJAAD4AVoOx6g/gQoAAQQLAJ1NAAAAAEUAABw/wAAAARErmwoAAQTVim3o3yEAFgAIeHI=",
                    "format": "base64"
                },
                "summary": "[<IP  version=4L ihl=5L tos=0x0 len=56 id=22153 flags= frag=0L ttl=248 proto=icmp chksum=0x5a0e src=199.168.63.129 dst=10.0.1.4 options=[] |<ICMP  type=time-exceeded code=ttl-zero-during-transit chksum=0x9d4d unused=0 |<IPerror  version=4L ihl=5L tos=0x0 len=28 id=16320 flags= frag=0L ttl=1 proto=udp chksum=0x2b9b src=10.0.1.4 dst=213.138.109.232 options=[] |<UDPerror  sport=57121 dport=ssh len=8 chksum=0x7872 |>>>>]"
            }
        ],
        "sent_packets": [
            {
                "raw_packet": {
                    "data": "RQAAKIc9AAABBuQcCgABBNWKbeiRQgAAAACVawAAAABQAiAAGr4AAA==",
                    "format": "base64"
                },
                "summary": "[<IP  id=34621 frag=0 ttl=1 proto=tcp dst=213.138.109.232 |<TCP  sport=37186 dport=0 seq=38251 flags=S |>>]"
            },
            {
                "raw_packet": {
                    "data": "RQAAKADhAAABBmp5CgABBNWKbehsSAAWAACbxwAAAABQAiAAOUYAAA==",
                    "format": "base64"
                },
                "summary": "[<IP  id=225 frag=0 ttl=1 proto=tcp dst=213.138.109.232 |<TCP  sport=27720 dport=ssh seq=39879 flags=S |>>]"
            },
            {
                "raw_packet": {
                    "data": "RQAAKO9JAAABBnwQCgABBNWKbeg1bwAXAAApTwAAAABQAiAA4pYAAA==",
                    "format": "base64"
                },
                "summary": "[<IP  id=61257 frag=0 ttl=1 proto=tcp dst=213.138.109.232 |<TCP  sport=13679 dport=telnet seq=10575 flags=S |>>]"
            },
            {
                "raw_packet": {
                    "data": "RQAAKNKoAAABBpixCgABBNWKbeixRwA1AABobwAAAABQAiAAJ4AAAA==",
                    "format": "base64"
                },
                "summary": "[<IP  id=53928 frag=0 ttl=1 proto=tcp dst=213.138.109.232 |<TCP  sport=45383 dport=domain seq=26735 flags=S |>>]"
            },
            {
                "raw_packet": {
                    "data": "RQAAKPzTAAABBm6GCgABBNWKbejCJwBQAACA3wAAAABQAiAA/hQAAA==",
                    "format": "base64"
                },
                "summary": "[<IP  id=64723 frag=0 ttl=1 proto=tcp dst=213.138.109.232 |<TCP  sport=49703 dport=http seq=32991 flags=S |>>]"
            },
            {
                "raw_packet": {
                    "data": "RQAAKNzQAAABBo6JCgABBNWKbejZyAB7AAD+NQAAAABQAiAAaPIAAA==",
                    "format": "base64"
                },
                "summary": "[<IP  id=56528 frag=0 ttl=1 proto=tcp dst=213.138.109.232 |<TCP  sport=55752 dport=ntp seq=65077 flags=S |>>]"
            }
        ]
    }
}
```

## Privacy considerations

When the user has configured to not include their IP Address in the reports we
will replace the src IP address of the IP Header with "127.0.0.1" of sent
packets and the dst field of the IP header of received packets with
"127.0.0.1".

Note though that such strategy will not fully prevent the leaking of the users
IP address via the IP packet payload (for example ICMP error messages will cite
the packet they are referring to and it will contain the non anonymized user IP
address).

On this specific issue there is an open ticket here:
https://trac.torproject.org/projects/tor/ticket/7933.

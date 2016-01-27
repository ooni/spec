# ScapyTest data format

Data Format Version: 0.2.0

This specifies the data format for tests that are based on
ooni.templates.scapyt.ScapyTest.

## Specification

**sent_packets** are the packets that have been generated and sent over the
network by the probe.

**answered_packets** are the packets that match up as answers according to the
rules defined in the **answers_flags** options.

```
{
    "answer_flags": [
          "List of options that are set for determining how to understand if a"
          "received packet is answer to a sent packet (these only apply to ICMP"
          "messages)"

          "'ipsrc' means that we check to see if the src and destination ports in"
          "the ICMP IP citation match."

          "'ipid' means that we look at the IPID in the response to match it up"
          "to sent packets."

          "'seqack' means that we check if TCP sequence number and ACK match in"
          "the ICMP citation when processing TCP inside of ICMP."

    ],
    "answered_packets": [
        {
            "raw_packet": {
                "data": "Encoding of packet the packet inclusive of IP header. "
                    "The type of encoding is specified in the format field."
                "format": "The encoding of the data field. Currently only supports base64."
            },
            "summary":
                "A human readable representation of the packet as is the output "
                "of repr on the scapy.packet object."
        },
    ],
    "sent_packets": [
        {
            "raw_packet": {
                "data": "Encoding of packet the packet inclusive of IP header. "
                    "The type of encoding is specified in the format field."
                "format": "The encoding of the data field. Currently only supports base64."
            },
            "summary":
                "A human readable representation of the packet as is the output "
                "of repr on the scapy.packet object."
        },
    ],
}
```

## Example output

```
{
    "bucket_date": "2015-11-13",
    "data_format_version": "0.2.0",
    "id": "ea9f588b-49ca-4261-babf-0111307877c4",
    "input": null,
    "options": [],
    "probe_asn": "AS8048",
    "probe_cc": "VE",
    "probe_ip": "127.0.0.1",
    "report_filename": "2015-11-13/20151113T104654Z-VE-AS8048-multi_protocol_traceroute-iq0hFnbx4ex7bAvysJBenb9uJAuh7LT02BhDrvIhK6Lpwe7PdCvJ7BHFzm4voYe7-0.1.0-probe.json",
    "report_id": "iq0hFnbx4ex7bAvysJBenb9uJAuh7LT02BhDrvIhK6Lpwe7PdCvJ7BHFzm4voYe7",
    "software_name": "ooniprobe",
    "software_version": "1.3.1",
    "test_helpers": {
        "backend": "213.138.109.232"
    },
    "backend_version": "1.1.4",
    "input_hashes": [],
    "probe_city": null,
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
        ],
        "test_icmp_traceroute": {
            "hops": [
                {
                    "address": "141.136.98.238",
                    "rtt": 2.039386034,
                    "ttl": 10
                },
                {
                    "address": "91.223.58.79",
                    "rtt": 2.2439029217,
                    "ttl": 11
                },
                {
                    "address": "213.138.109.232",
                    "rtt": 2.4453678131,
                    "ttl": 12
                }
            ]
        },
        "test_tcp_traceroute": {
            "hops_0": [
                {
                    "address": "141.136.98.238",
                    "rtt": 2.0464248657,
                    "sport": 34854,
                    "ttl": 10
                },
                {
                    "address": "91.223.58.79",
                    "rtt": 2.2470018864,
                    "sport": 10415,
                    "ttl": 11
                },
                {
                    "address": "213.138.109.232",
                    "rtt": 2.4521570206,
                    "sport": 0,
                    "ttl": 12
                }
            ],
            "hops_123": [
                {
                    "address": "141.136.98.238",
                    "rtt": 2.0381779671,
                    "sport": 50988,
                    "ttl": 10
                },
                {
                    "address": "91.223.58.79",
                    "rtt": 2.240860939,
                    "sport": 7867,
                    "ttl": 11
                },
                {
                    "address": "213.138.109.232",
                    "rtt": 2.4443869591,
                    "sport": 123,
                    "ttl": 12
                }
            ],
            "hops_22": [
                {
                    "address": "141.136.98.238",
                    "rtt": 2.0354959965,
                    "sport": 36980,
                    "ttl": 10
                },
                {
                    "address": "91.223.58.79",
                    "rtt": 2.2357189655,
                    "sport": 26447,
                    "ttl": 11
                },
                {
                    "address": "213.138.109.232",
                    "rtt": 2.4381670952,
                    "sport": 22,
                    "ttl": 12
                }
            ],
            "hops_23": [
                {
                    "address": "141.136.98.238",
                    "rtt": 2.0388379097,
                    "sport": 4690,
                    "ttl": 10
                },
                {
                    "address": "91.223.58.79",
                    "rtt": 2.2384901047,
                    "sport": 51177,
                    "ttl": 11
                },
                {
                    "address": "213.138.109.232",
                    "rtt": 2.4421479702,
                    "sport": 23,
                    "ttl": 12
                }
            ],
            "hops_443": [
                {
                    "address": "141.136.98.238",
                    "rtt": 2.0386300087,
                    "sport": 11218,
                    "ttl": 10
                },
                {
                    "address": "91.223.58.79",
                    "rtt": 2.240696907,
                    "sport": 26319,
                    "ttl": 11
                },
                {
                    "address": "213.138.109.232",
                    "rtt": 2.4430809021,
                    "sport": 443,
                    "ttl": 12
                }
            ],
            "hops_53": [
                {
                    "address": "141.136.98.238",
                    "rtt": 2.0381169319,
                    "sport": 36901,
                    "ttl": 10
                },
                {
                    "address": "91.223.58.79",
                    "rtt": 2.2402248383,
                    "sport": 60900,
                    "ttl": 11
                },
                {
                    "address": "213.138.109.232",
                    "rtt": 2.4425189495,
                    "sport": 53,
                    "ttl": 12
                }
            ],
            "hops_65535": [
                {
                    "address": "141.136.98.238",
                    "rtt": 2.0387971401,
                    "sport": 57248,
                    "ttl": 10
                },
                {
                    "address": "91.223.58.79",
                    "rtt": 2.2455801964,
                    "sport": 52285,
                    "ttl": 11
                },
                {
                    "address": "213.138.109.232",
                    "rtt": 2.4457411766,
                    "sport": 65535,
                    "ttl": 12
                }
            ],
            "hops_80": [
                {
                    "address": "141.136.108.130",
                    "rtt": 1.8421959877,
                    "sport": 23745,
                    "ttl": 9
                },
                {
                    "address": "141.136.98.238",
                    "rtt": 2.0382699966,
                    "sport": 22618,
                    "ttl": 10
                },
                {
                    "address": "91.223.58.79",
                    "rtt": 2.2403969765,
                    "sport": 45566,
                    "ttl": 11
                },
                {
                    "address": "213.138.109.232",
                    "rtt": 2.4452321529,
                    "sport": 80,
                    "ttl": 12
                }
            ],
            "hops_8080": [
                {
                    "address": "141.136.98.238",
                    "rtt": 2.0389461517,
                    "sport": 57892,
                    "ttl": 10
                },
                {
                    "address": "91.223.58.79",
                    "rtt": 2.2410969734,
                    "sport": 51593,
                    "ttl": 11
                },
                {
                    "address": "213.138.109.232",
                    "rtt": 2.4440560341,
                    "sport": 8080,
                    "ttl": 12
                }
            ]
        },
        "test_udp_traceroute": {
            "hops_0": [],
            "hops_123": [
                {
                    "address": "141.136.108.130",
                    "rtt": 1.920017004,
                    "sport": 57583,
                    "ttl": 9
                },
                {
                    "address": "91.223.58.79",
                    "rtt": 2.24168396,
                    "sport": 18721,
                    "ttl": 11
                },
                {
                    "address": "213.138.109.232",
                    "rtt": 2.4463579655,
                    "sport": 25517,
                    "ttl": 12
                }
            ],
            "hops_22": [
                {
                    "address": "141.136.108.130",
                    "rtt": 1.9136769772,
                    "sport": 45625,
                    "ttl": 9
                },
                {
                    "address": "141.136.98.238",
                    "rtt": 2.0372998714,
                    "sport": 50609,
                    "ttl": 10
                },
                {
                    "address": "91.223.58.79",
                    "rtt": 2.2419588566,
                    "sport": 14160,
                    "ttl": 11
                },
                {
                    "address": "213.138.109.232",
                    "rtt": 2.4428777695,
                    "sport": 23686,
                    "ttl": 12
                }
            ],
            "hops_23": [
                {
                    "address": "141.136.108.130",
                    "rtt": 1.9202280045,
                    "sport": 58718,
                    "ttl": 9
                },
                {
                    "address": "141.136.98.238",
                    "rtt": 2.0369830132,
                    "sport": 39310,
                    "ttl": 10
                },
                {
                    "address": "91.223.58.79",
                    "rtt": 2.2406070232,
                    "sport": 9348,
                    "ttl": 11
                },
                {
                    "address": "213.138.109.232",
                    "rtt": 2.4436769485,
                    "sport": 56507,
                    "ttl": 12
                }
            ],
            "hops_443": [
                {
                    "address": "141.136.108.130",
                    "rtt": 1.9194400311,
                    "sport": 61062,
                    "ttl": 9
                },
                {
                    "address": "141.136.98.238",
                    "rtt": 2.0356152058,
                    "sport": 57814,
                    "ttl": 10
                },
                {
                    "address": "91.223.58.79",
                    "rtt": 2.2425971031,
                    "sport": 36493,
                    "ttl": 11
                },
                {
                    "address": "213.138.109.232",
                    "rtt": 2.4469130039,
                    "sport": 20708,
                    "ttl": 12
                }
            ],
            "hops_53": [
                {
                    "address": "141.136.108.130",
                    "rtt": 1.9192700386,
                    "sport": 63309,
                    "ttl": 9
                },
                {
                    "address": "141.136.98.238",
                    "rtt": 2.0371799469,
                    "sport": 44259,
                    "ttl": 10
                },
                {
                    "address": "91.223.58.79",
                    "rtt": 2.2417399883,
                    "sport": 32840,
                    "ttl": 11
                },
                {
                    "address": "213.138.109.232",
                    "rtt": 2.4441540241,
                    "sport": 6946,
                    "ttl": 12
                }
            ],
            "hops_65535": [
                {
                    "address": "141.136.108.130",
                    "rtt": 1.9188029766,
                    "sport": 16637,
                    "ttl": 9
                },
                {
                    "address": "91.223.58.79",
                    "rtt": 2.2441849709,
                    "sport": 56282,
                    "ttl": 11
                }
            ],
            "hops_80": [
                {
                    "address": "141.136.108.130",
                    "rtt": 1.9194018841,
                    "sport": 26666,
                    "ttl": 9
                },
                {
                    "address": "91.223.58.79",
                    "rtt": 2.2409110069,
                    "sport": 47993,
                    "ttl": 11
                },
                {
                    "address": "213.138.109.232",
                    "rtt": 2.4452769756,
                    "sport": 43930,
                    "ttl": 12
                }
            ],
            "hops_8080": [
                {
                    "address": "141.136.108.130",
                    "rtt": 1.9188380241,
                    "sport": 53083,
                    "ttl": 9
                },
                {
                    "address": "91.223.58.79",
                    "rtt": 2.2436709404,
                    "sport": 62686,
                    "ttl": 11
                }
            ]
        }
    },
    "test_name": "multi_protocol_traceroute",
    "test_runtime": 57.7884280682,
    "test_start_time": "2015-11-13 10:46:54",
    "test_version": "0.3"
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

# Specification version number

2014-12-08-000

# Specification name

Raw UDP Echo Test Helper

# Helper description

The Raw UDP Echo Test Helper listens on a UDP port for incoming packets. When a
packet is recieved, it sends a UDP packet in reply with the original packet's
header as its payload.

# Helper preconditions

 * An Internet connection
 * An Internet-Reachable UDP Port
 * No known middleboxes rewriting UDP headers in unexpected ways between
   the helper and the transit ISP

# Expected impact

Ability to help an ooni-probe client determine if the UDP header is being
rewritten and if packets are being truncated when UDP-lite is used with a
shorter checksum coverage than the full length of the packet using the UDP
protocol number in the IP header.

# Expected inputs

 * A UDP packet addressed to the helper
 * The destination port should not be one that might attract special treatment
 * The payload should not contain keywords that might attract special treatment

# Expected output

 * A UDP packet with the original incoming packet as its payload addressed to
   return to the ooniprobe client

# Possible conclusions

Possible conclusions that could be drawn from tests using this helper are:

 * Middleboxes are truncating UDP-lite packets when the UDP protocol number is
   used
 * Middleboxes are discarding UDP-lite packets with the checksum does not match
   for the full length of the packet
 * Source and destination ports are being rewritten

# Notes

An implementation of this test helper is currently being worked on by Iain R.
Learmonth <<irl@fsfe.org>> using Scapy.


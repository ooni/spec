# Specification version number

2014-12-15-000

* status: _obsolete_

# Specification name

Raw UDP Echo Test Helper

# Helper description

The Raw UDP Echo Test Helper listens on a UDP port for incoming packets. When a
packet is recieved, it sends a UDP packet in reply with the original packet's
IP and UDP header and payload as the reply's payload.

# Helper preconditions

 * An Internet connection
 * An Internet-Reachable UDP Port
 * No known middleboxes rewriting UDP headers in unexpected ways between
   the helper and the transit ISP

# Expected impact

Ability to help an ooni-probe client determine if the UDP header is being
rewritten and if packets are being truncated when UDP-lite [[RFC3828][]] is
used with a shorter checksum coverage than the full length of the packet using
the UDP protocol number in the IP header.

# Expected inputs

 * A UDP packet addressed to the helper
 * The destination port should not be one that might attract special treatment
 * The payload should not contain keywords that might attract special treatment

# Expected output

 * A UDP packet with the original incoming packet as its payload addressed to
   return to the ooni-probe meter

# Possible conclusions

Possible conclusions that could be drawn from tests using this helper are:

 * Middleboxes are truncating UDP-lite packets when the UDP protocol number is
   used
 * Middleboxes are discarding UDP-lite packets with the checksum does not match
   for the full length of the packet
 * Source and destination ports are being rewritten

# Security considerations

In order to prevent the possibility of this helper being used to set up a
"loop" where a forged source address causes packets to be sent to another
service that replies to arbitrary UDP packets, such as UDP echo, the first byte
of the payload in the request must have a zero value. Replies will never have a
zero value as this first byte contains the IP protocol version number from the
IP header.

The possibility of this helper being used for an amplification attack was
considered, but as the amplification factor is limited to the size of an IP and
UDP header, it was not deemed that mitigation for this was necessary.

# Notes

An implementation of this test helper is currently being worked on by Iain R.
Learmonth <<irl@fsfe.org>> using Scapy.

[RFC3828]: http://tools.ietf.org/html/rfc3828

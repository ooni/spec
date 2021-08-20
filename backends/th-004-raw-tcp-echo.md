# Specification version number

2014-12-15-000

* status: _obsolete_

# Specification name

Raw TCP Echo Test Helper

# Helper description

The Raw TCPEcho Test Helper listens on a TCP port for incoming connections.
When a connection is initiated, it accepts the connection, reads a dummy HTTP
request and sends an HTTP reply containing an encoding of the IP packets that
made up the TCP 3 way handshake [[Wikipedia-3WHS][]] which can be compared
against the packets sent by an ooni-probe meter.

# Helper preconditions

* An Internet connection
* An Internet-Reachable TCP Port (preferably port 80)
* No known middleboxes rewriting IP or TCP headers in unexpected ways between
  the helper and the transit ISP

# Expected impact

Ability to help an ooni-probe client determine if the IP or TCP headers have
been modified in transit, possibly indicating that the connection is being
transparently proxied.

# Expected inputs

 * An HTTP 1.1 [[RFC2616][]] request that should not include any "dubious" Host:
   header or keywords that might attract special treatment

By emulating an HTTP session, a protocol known to censorship systems and
protocol-enhancing proxies, it will increase the chances to see intereference
occuring over using another protocol that may simply be passed through.

# Expected output

 * An HTTP 1.1 [[RFC2616][]] reply that includes as its body an encoding of the
   packets that made up the TCP 3 way handshake [[Wikipedia-3WHS][]] from the
   vantage point of the helper

The encoding chosen could be simply a binary PCAP trace, a base64 encoded PCAP
trace or even a JSON encoding of a dissector output as long as the dissector is
sufficiently verbose to maximise the usefulness of the helper.

MIME types like text/html should be avoided as these have a stronger potential
for being rewritten on the wire.

# Possible conclusions

Possible conclusions that could be drawn from tests using this helper are:

 * The presence of a transparent proxy
 * The presence of network address translation
 * The bleaching of bits in the IP and TCP header by badly implemented middleboxes

# Notes

An implementation of this test helper is currently being worked on by Iain R.
Learmonth <<irl@fsfe.org>> using Scapy.

[RFC2616]: http://tools.ietf.org/html/rfc2616
[Wikipedia-3WHS]: http://en.wikipedia.org/wiki/Transmission_Control_Protocol#Connection_establishment

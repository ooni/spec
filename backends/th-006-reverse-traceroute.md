# Specification version number

2014-12-15-000

* status: _obsolete_

# Specification name

Reverse Traceroute Test Helper

# Helper description

The reverse traceroute test helper listens for incoming connections either on
a TCP socket or via a web server. When a connection is initiated, it performs
a reverse traceroute to the connection's source IP address and returns the
results of the traceroute via the same connection.

# Helper preconditions

 * An Internet connection
 * An Internet-Reachable TCP Port
 * No known middleboxes rewriting packet payloads in unexpected ways between
   the helper and the transit ISP

# Expected impact

Through cross-referencing results, the ability to determine where on the
network path network interference exists which could indicate whether or not
the interference is localised to an access ISP or being conducted on a national
level.

# Expected inputs

 * The initiation of a connection.

# Expected output

 * The results of a traceroute giving the IP address of each hop and, if
   available, the ping times to each hop.

The encoding chosen could be JSON, CSV, or another format. It should be
possible to convert between this format and the format used by tests that
perform a forward traceroute in ooni-probe.

# Possible conclusions

Through cross-referencing of results, it should be possible to determine in
which AS the network interference is occuring.

# Notes

An implementation of this test helper is currently being worked on by Iain R.
Learmonth <<irl@fsfe.org>> using Scapy.


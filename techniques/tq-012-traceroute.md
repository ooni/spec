# tq-012 traceroute

When the IP or IP:Port tuple is suspected to be blocked it is interesting to collect traceroutes to the following endpoints:
- vary the host within the same /24 subnet keeping port and protocol the same
- vary the host within a different /24 of the same AS keeping port and protocol the same
- vary the port amongst the set of well-known<sup>[1](#fn1)</sup> ports keeping the protocol and IP the same
- vary the port amongst the set of possibly-blacklisted ports (25, 135-139, 445, etc.) keeping the protocol and IP the same
- vary the protocol comparing TCP to UDP and ICMP
- vary the network path for UDP<sup>[2](#fn2)</sup> to account for possible ECMP routes
- test a control vantage point<sup>[3](#fn3)</sup> to ensure that the network does not block all the traceroutes
- test a non-routable vantage point to find closest router without default route (likely, having a full view)

Traceroutes should capture PTR records for routers generating ICMP errors as
some routers may have RFC1918 IP addresses (so, global PTR record does not make
sense for them and can’t be resolved on ingestion or later).

## (TBD) Privacy considerations

- likely we don’t want to store PTR record for the very first hop if it’s RFC1918 address, some OpenWRT routers set it to their hostname and it may have user-supplied PII
- maybe we don’t want to store exact IP address for the very first hop as well
- maybe we don’t want to scrub anything if the user has set their privacy settings to share their IP address
- we likely want to store the IP addresses and PTR record for all the path, that’s valuable information: see APN-Proxy-after-DPI in Uganda, see Tor blocking in Venezuela, see PTRs like “filter-gw.transtelecom...” and “censor-02.obit...” in Russia
- we may want to ask the user to share their IP address if we detect that some case can't properly be bisected on the probe without that information
- we probably don't want to round IPs of whole path down to AS numbers as it kills all PTRs

<a name="fn1">1</a>: it may be the set of 80, 443, 22, 110, 143 or other `Safe_ports` from squid, BUT comparing 80 to 443 is not enough. Also, `mtr` uses port 80 by default for TCP.

<a name="fn2">2</a>: it’s impossible to do that for TCP without root; there is no ECMP for ICMP

<a name="fn3">3</a>: it’s TBD if it should be RIPE Atlas Anchor with well-known network location or some anycasted service like DNS Root

## Examples
- AS8997, Russia blocks www.imperialviolet.org having address 159.203.111.115 due to partial Amazon ban. ICMP traceroute reaches destination, UDP traceroute reaches destination and shows ECMP in action, TCP traceroutes to ports 80 or 443 stop at AS1299 (≈same teleco, different AS), TCP traceroutes to random port and port 22 (ssh) both reach destination
- see proxy notes in report on [Uganda Social Media Tax](https://ooni.torproject.org/post/uganda-social-media-tax/), see also how 443/https and 25/smtp traceroutes differ
- [AS8048, CANTV, Venezuela blocked tor](https://ooni.torproject.org/post/venezuela-internet-censorship/#testing) by IP:Port of ORs on reverse path, “forward” traceroute from the client could not capture that
- see [Leonid’s talk at Chaos Constructions 2017](http://darkk.net.ru/garbage/RIPE-Atlas-OONI-and-CC2017.pdf) for PTR record samples

# tq-017 Request to discard test helper

If a TCP or UDP request triggers an unexpected response it is interesting to send that request to a test helper acting as a discard or dummy server. An unexpected reply highlights possible internet-wide protocol interception. The test helper can do following tricks:

- capture TCP/IP metadata<sup>[1](#fn1)</sup> of injected RST or ICMP Unreachable
- request capture to check for the mere presence of the request<sup>[2](#fn2)</sup> with out of band channel<sup>[3](#fn3)</sup>
- observe RST injection to distinguish “two-sided” injector from “one-sided”
- block RST injection together with the client to distinguish “on-path” filter from “in-path”
- reverse traceroute to the client
- parasitic reverse traceroute with SYN-ACK in case of TCP
- parasitic reverse traceroute with the reply payload

<a name="fn1">1</a>: TTL may be the same as the client's or a different one, IP ID, bad Seq/Ack numbers, TCP Window value and so on

<a name="fn2">2</a>: the request may be dropped by in-path filter, but on-path filter can't do it

<a name="fn3">3</a>: speaking directly to the test-helper may be bad idea when IP is blacklisted for a while after "triggering" the filter

## Example

- [Iran blocked www.instagram.com](http://www.instagram.com), parasitic reverse traceroute to the client was different from parasitic reverse traceroute with CommonName=instagram.com ServerCertificate payload
- [AS8048, CANTV, Venezuela blocked tor](https://ooni.torproject.org/post/venezuela-internet-censorship/#testing) by IP:Port of ORs on reverse path, reverse traceroute clearly indicated that
- Rostelecom was banning IP:Port for ~two hours after [MTProto-like handshake](https://github.com/darkk/poormansmtproto/)
- Yota was shaping some connections to ~32 kbit/s with "stateful" shaper that has kept policy for a while even when different service was brought up on that IP:Port (TBD: href to the blog post when published)

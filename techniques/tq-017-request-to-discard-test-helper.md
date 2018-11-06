# tq-017 Request to discard test helper

If a TCP or UDP request triggers an unexpected response it is interesting to send that request to a test helper acting as a discard or dummy server. An unexpected reply highlights possible internet-wide protocol interception. The test helper can do following tricks:

- full packet capture seeking for TCP/IP headers metadata
- request capture to confirm or refute the mere presence of the request with out of band channel
- observe RST injection to distinguish “two-sided” injector from “one-sided”
- block RST injection together with the client to distinguish “on-path” filter from “in-path”
- reverse traceroute to the client
- parasitic reverse traceroute with SYN-ACK in case of TCP
- parasitic reverse traceroute with the reply payload

## Example

- [Iran blocked www.instagram.com](http://www.instagram.com), parasitic reverse traceroute to the client was different from parasitic reverse traceroute with CommonName=instagram.com ServerCertificate payload
- [AS8048, CANTV, Venezuela blocked tor](https://ooni.torproject.org/post/venezuela-internet-censorship/#testing) by IP:Port of ORs on reverse path, reverse traceroute clearly indicated that

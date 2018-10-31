# tq-004 DNS/TCP, DoT, DoH against same resolver

When Probe assumes MITM between the client and the recursive DNS resolver, it
is interesting to compare responses got via DNS/UDP and responses got via
DNS/TCP, DoT ([DNS over TLS](https://tools.ietf.org/html/rfc7858)) and DoH (DNS
over HTTPS) as those requests are likely to go through same network path. Extra
IPs got that way may be added to set of “Origin IPs” for further tests (TCP,
HTTP, TLS).

It makes sense both for [public DNS resolvers](https://en.wikipedia.org/wiki/Public_recursive_name_server),
and ISP’s DNS resolvers.

## Examples
- [AS41843, ER-Telecom, Omsk](https://github.com/ooni/probe/issues/647#issuecomment-275999682): DNS/TCP does not provoke “censored” reply for rutracker.org neither from Google’s 8.8.8.8, nor from ISP’s 5.3.3.3, but DNS/TCP gives “censored” reply from another ISP’s resolver 109.194.112.1
- AS61173, Green Web Samaneh Novin Co Ltd, Iran — “uncensored” reply from 8.8.8.8 for bridges.torproject.org via TCP

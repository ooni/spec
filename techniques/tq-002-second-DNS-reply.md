# tq-002 Second DNS reply

The client issuing a DNS/UDP query may receive two<sup>[1](#fn1)</sup> DNS responses, one coming
from the legitimate DNS resolver and one coming from the censor. In order to capture both the first reply, but also, possibily, a second one, it's suggested to wait 5 seconds for the first response<sup>[2](#fn2)</sup> and an additional 5 seconds<sup>[3](#fn3)</sup> on the same UDP socket after receving the first reply.

These two responses should have [TTL](./tq-015-packet-headers-exfiltration-with-BPF.md) and
[latency](./tq-000-timing-information-collection.md) recorded (if platform
permits). All the captured IPs from several responses should be passed to
further tests.

<a name="fn1">1</a>: There may be more than one extra response, but that has never been observed so far.

<a name="fn2">2</a>: 5 second timeout is default `RES_TIMEOUT` in GNU C library
2.23. It’s possible to estimate platform `getaddrinfo()` timeout with an
attempt to resolve a domain from non-responding server, but it’ll make code
more complex.

<a name="fn3">3</a>: Two separate 5 second windows come from the hypothesis
that the query may be sitting in the TX queue for several seconds, so it would
be silly to get first response in 4.9s and stop waiting just in 0.1s. It is
also reasonable to wait for 10 seconds since query if that makes implementation
easier, but it makes the test a bit more “sleepy” and makes treatment of these
two responses a bit less “fair”.

If a network operator also firewalls the DNS packets from leaving or entering
their network, there would not be a second response even though in reality there
is injection happening as opposed to hijacking. This is a technical detail and
does not change the fact that there is DNS interception happening.

## Examples
- [AS41843, CJSC "ER-Telecom Holding" Omsk branch](https://github.com/ooni/probe/issues/647#issuecomment-275999682)

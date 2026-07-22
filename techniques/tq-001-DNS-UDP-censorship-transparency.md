# tq-001 DNS/UDP Censorship Transparency

DNS testing is fundamental to network measurement to detect censorship as it’s
a commonly used technique to implement censorship.

When reasoning about DNS interference, we shall consider the following possibilities:
- [_DNS hijacking_](https://en.wikipedia.org/wiki/DNS_hijacking#Manipulation_by_ISPs) (or _Policy Based DNS interference_), whereby a DNS resolver run by the ISP, parental control DNS service or government is configured to return specifically altered responses to specific queries. This is usually trivial to circumvent by changing resolver.
- [_DNS Spoofing_](https://en.wikipedia.org/wiki/DNS_spoofing), whereby there is equipment in the network that listens for DNS queries and sends replies back to the user faster than the legitimate DNS server. This tends to be tricker to circumvent.
- _DNS Transparent Proxy_, whereby all DNS requests sent by a user are routed through a DNS proxy box regardless of the destination DNS server, and the reply is served by the proxy box. This also tends to be trickier to circumvent.

The difference between _DNS Spoofing_ and _DNS Transparent Proxy_ is that in one case the
origin server gets the client query and in the other it doesn't, in other words &mdash; if the
[end-to-end principle](https://en.wikipedia.org/wiki/End-to-end_principle) is
preserved or 100%-violated.  If the origin server gets the query from the
client and the response from origin server is blocked so the client only gets a
single injected response, then it's still spoofing. The following metadata bits are
useful to classify the case as _spoofing_ or _proxy_:

- [presence of second DNS reply to single query](./tq-002-second-DNS-reply.md)
- [IP TTL values of the replies](./tq-007-UDP-information-collection.md) got from _different_ resolvers
- difference between probe IP addresses collected over HTTPS, DNS/TCP, DNS/UDP and STUN/UDP
- different handling of hop-by-hop [EDNS(0)](https://tools.ietf.org/html/rfc6891) options

E.g. lack of the second DNS reply combined with the injected DNS response
suggests<sup>[1](#fn1)</sup> that censorship equipment is doing an
[_in-path_ attack (aka _man-in-the-middle_)](https://en.wikipedia.org/wiki/Man-in-the-middle_attack),
while the presence of a second DNS reply suggests<sup>[2](#fn2)</sup> that an
[_on-path_ attack (aka _man-on-the-side_)](https://en.wikipedia.org/wiki/Man-on-the-side_attack)
is happening.

<a name="fn1">1</a>: _"suggets in-path"_ (not _"proves"_) as the second DNS reply can also _disappear_ due to natural packet loss

<a name="fn2">2</a>: _"suggets on-path"_ (not _"proves"_) as in-path equipment may do *all* on-path attacks as well

The following techniques may help to distinguish DNS-based censorship from a
malfunctioning network or DNS service:

- [more than one reply](./tq-002-second-DNS-reply.md) is received for a single DNS query
- the same resolver gives the same answer with [DNS/TCP, DoT and DoH](./tq-004-DNS-TCP-DoT-DoH-against-same-resolver.md)
- [DNS Resource Record TTL “ticks”](./tq-005-DNS-Resource-Record-TTL-ticks-in-cache.md) on caching Recursive Resolver
- [another “non-existent” domain in same zone gives same error](./tq-006-another-NXDOMAIN-domain-in-same-zone.md)
- timeout can be explained by [5-tuple load balancing going bad](./tq-007-UDP-information-collection.md)
- delegation [chain works from root](./tq-008-DNS-delegation-chain-from-root.md) (dig +trace, drill)
- domain and parent domains have [SOAs and NSes matching with control](./tq-010-SOAs-and-NSes-for-possibly-censored-domain.md) measurement
- TBD :-)

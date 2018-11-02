# tq-001 DNS/UDP Censorship Transparency

DNS testing is fundamental to network measurement to detect censorship as it’s
a very commonly used technique to implement censorship.

When reasoning about DNS interference, we shall consider the following possibility:
- _Policy Based DNS interference_ (aka [_DNS hijacking_](https://en.wikipedia.org/wiki/DNS_hijacking#Manipulation_by_ISPs)), whereby a DNS resolver run by the ISP, Family-DNS service or government is configured to return specifically altered responses to specific queries. This is usually trivial to circumvent by changing resolver.
- _DNS Spoofing_, whereby there is equipment in the network that listens for DNS queries and sends replies back to the user faster than the legitimate DNS server. This tends to be tricker to circumvent.
- _DNS Transparent Proxy_, whereby all DNS requests sent by a user are routed through a DNS proxy box regardless of the destination DNS server, and the reply is served by the proxy box. This also tends to be trickier to circumvent.

Especially when DNS Spoofing is present, it’s interesting to gain a deeper
understanding of when the spoofing is happening.

Traditionally most DNS queries are performed using the UDP protocol, meaning
that censorship equipment does not need to do DNS Spoofing in-path, but they
can do it “[on the side](https://en.wikipedia.org/wiki/Man-on-the-side_attack)”.

The following techniques may help to distinguish DNS-based censorship from a
malfunctioning network or DNS service:

- more than one reply is received for a single DNS query
- the same resolver gives the same answer with DNS/TCP, DoT and DoH
- DNS Resource Record TTL “ticks” on caching Recursive Resolver
- another “non-existent” domain in same zone gives same error
- timeout can be explained by 5-tuple load balancing going bad
- delegation chain works from root (dig +trace, drill)
- domain and parent domains have SOAs and NSes matching with control measurement
- TBD :-)

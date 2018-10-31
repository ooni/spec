# tq-001 DNS/UDP Censorship Transparency

DNS testing is fundamental to network measurement to detect censorship as it’s
a very commonly used technique to implement censorship.

When implementing blocking on a DNS level, censorship equipment will typically
implement one of two techniques:

- _DNS Hijacking_, whereby a DNS resolver run by the ISP or government will deliver false responses to queries for the users domain. This is usually trivial to circumvent by changing resolver.
- _DNS Spoofing_, whereby the DNS queries of the user are intercepted and the false response is sent to the user faster than the legitimate response. This tends to be trickier to circumvent.

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

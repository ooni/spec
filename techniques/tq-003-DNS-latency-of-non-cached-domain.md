# tq-003 DNS latency of non-cached domain

To understand if the filtering equipment has a rule for `*.censored.net` or not it 
can be interesting to measure the lantency of looking up `random-subdomain.censored.net` 
as this would cause recursive resolution when no such rule exists. Conversely if the 
policy is to block anything containing `censored.net` the response may arrive earlier, 
because there is no extra latency caused by the recursive resolution.

There are however some caveats in this approach. Indeed, if the recursor hosts a zone for
`censored.net` it does not have to query the `censored.net` `NS` for the domain. But
it’s not a 100% clear signal as some [DNSSEC versions may leak cacheable ranges](https://blog.cloudflare.com/dnssec-complexities-and-considerations/)
of non-existent domains. Also, NSes responsible for the `censored.net` zone may be
unreachable<sup>[1](#fn1)</sup> and that information may be cached as well, that will also affect
resolution latency.

<a name="fn1">1</a>: e.g. some israeli authoritative DNS servers were dropping requests from Egypt

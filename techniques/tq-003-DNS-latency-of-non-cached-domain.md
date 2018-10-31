# tq-003 DNS latency of non-cached domain

It may be tempting to use the latency to resolve
`random-subdomain.censored.net` as a signal of possible network interference
touching `censored.net` domain. Indeed, if the recursor hosts a zone for
`censored.net` it does not have to query `censored.net` NS for the domain. But
it’s not 100% clear signal as some [DNSSEC versions may leak cacheable ranges](https://blog.cloudflare.com/dnssec-complexities-and-considerations/)
of non-existent domains. Also, NSes responsible for `censored.net` zone may be
unreachable<sup>[1](#fn1)</sup> and that information may be cached as well, that will also affect
resolution latency.

<a name="fn1">1</a>: e.g. some israeli authoritative DNS servers were dropping requests from Egypt

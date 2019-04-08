# tq-009 Subdomains of possibly-censored domains

When a domain is suspected to be censored by a resolver (returns unexpected error
or unexpected RR for a query) it is interesting to check well-known and random
subdomains of this domain and compare those measurements to control. They may
present same values / errors as a parent domain due to the following reasons:

- NSes for the domain may be unreachable from the recursive resolver, so `SERVFAIL`
- domain may have a delegation or DNSSEC misconfiguration, so `SERVFAIL`
- whole domain may be censored via DNS
- domain may have an actual “star” record (or have dynamically generated records)

## Examples
- some israeli authoritative DNS servers were dropping requests from Egypt
- [delegation misconfiguration for pernambuco.com](https://ooni.torproject.org/post/not-quite-network-censorship/) (NS pointing to CNAME)
- AS61173, Iran — woohoo.torproject.org points to 10.10.34.36
- AS41843, Russia — woo.hoo.rutracker.org points to 5.3.3.17
- *.*.*.*.livejournal.com and *.*.*.*.blogspot.com are CNAMEs to same load balancer

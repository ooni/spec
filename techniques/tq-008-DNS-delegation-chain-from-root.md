# tq-008 DNS delegation chain from root

When domain is suspected to be censored by resolver it is interesting to check
if delegation chain for the domain works if the client starts from the DNS
root. It also allows verification that NS record do not point to CNAME Resource
Records that breaks bind software.

TBD: it’s unclear if the client should try both doing [QNAME minimisation (RFC7816)](https://tools.ietf.org/html/rfc7816)
and avoiding it. Different results may also highlight presence of network
anomaly. But [doing it according to the letter of RFC may be problematic](https://ripe72.ripe.net/presentations/120-unbound_qnamemin_ripe72.pdf),
so data format should be verbose enough to capture what was actually done.

TBD: it’s unclear if every A/AAAA for NS records should be resolved from root as well. Probably, they should be.

TBD: it’s unclear if DNSSEC should be validated. Probably, it should be, but in non-fatal mode following NS-points-to-CNAME logic.

## Examples

- some israeli authoritative DNS servers were dropping requests from Egypt, so domains look like censored by resolver while not being actually censored by egyptian networks
- [delegation misconfiguration for pernambuco.com](https://ooni.torproject.org/post/not-quite-network-censorship/) (NS pointing to CNAME) was not a censorship incident
- AS41843, Russia: sending a query for `rutracker.org` without QNAME minification triggers injected response when the query is sent to root servers

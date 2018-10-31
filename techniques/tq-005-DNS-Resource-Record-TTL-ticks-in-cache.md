# tq-005 DNS Resource Record TTL “ticks” in cache

When probe assumes that specific domain name is censored it’s interesting to
query the same nameserver for the same name in two seconds and check if TTL
field changes. If the TTL field does not change, it’s clear indicator that at
least one of following is likely true:

- the domain name is served by the caching recursive DNS resolver
- the domain name has very low TTL so it expires and is re-fetched while Probe sleeps
- the load balancer in front of the DNS servers cluster is not aware of DNS names, so requests to the cache are not “sticky”
- the response is injected with static TTL by an entity that is able to observe the traffic

If TTL changes for an “unexpected” value (e.g. diff is not within 1..3 range
after 2 seconds delay) it may be also a side-effect of qname-unaware load
balancing or some other logic. That was observed at least with 8.8.8.8.

## Examples

- [AS41843, ER-Telecom, Omsk](https://github.com/ooni/probe/issues/647#issuecomment-275999682): static TTL=600 for “censored” DNS/UDP reply for `rutracker.org` for any resolver
- [AS41843](https://github.com/ooni/probe/issues/647#issuecomment-275999682): ticking(!) TTL for “censored” DNS/TCP reply for `rutracker.org` from ISP’s resolver 109.194.112.1
- AS61173, Green Web Samaneh Novin Co Ltd, Iran — static TTL=418 from 8.8.8.8 for bridges.torproject.org

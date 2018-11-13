# tq-011 Both A and AAAA DNS queries

It is important to do both A and AAAA DNS queries for all the domains 
Probes resolve during testing, as sometimes a “censor” will add the second stack (ex. IPv6) for a
single-stack network endpoint to serve a blockpage.

## Examples

- [AS41843, ER-Telecom, Omsk, Russia](https://github.com/ooni/probe/issues/647#issuecomment-275999682) makes “grani.ru” dual-stack with “5.3.3.17” and “2a02:2698:a002:1::3:17” while it’s “normally” single-stacked with 95.211.178.194

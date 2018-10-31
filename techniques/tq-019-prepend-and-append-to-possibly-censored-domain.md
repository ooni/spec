# tq-019 Prepend and append to possibly-censored domain

When we suspect a domain name to be censored in some protocol request (DNS,
HTTP, TLS), it is interesting to see if same protocol request to same endpoint
returns different error when we prepend possibly-censored domain to some
nonexistent domain name. It is also interesting to check well-known and random
subdomains of the possibly-censored domain.

The logic is to check if block of evil.co(sic!) observes same pattern as
**www.**evil.co, **we**evil.co, evil.co**m**, evil.co**.tls-chan.net** and even
**garbag**evil.co**.tls-chan.net**.

DNS subdomains (like www.evil.org) are better described in
[tq-009 subdomains of possibly censored domains](./tq-009-subdomains-of-possibly-censored-domains.md).

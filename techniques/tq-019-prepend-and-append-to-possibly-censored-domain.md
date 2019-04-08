# tq-019 Prepend and append to possibly-censored domain

When we suspect a domain name to be censored in some protocol request (DNS,
HTTP, TLS), it is interesting to see if the same protocol request to the same endpoint
returns a different error when we prepend a possibly-censored domain to some
nonexistent domain name. It is also interesting to check well-known and random
subdomains of the possibly-censored domain.

The logic is to check if the block of evil.co(sic!) observes the same pattern as
**www.**evil.co, **we**evil.co, evil.co**m**, evil.co**.tls-chan.net** and even
**garbag**evil.co**.tls-chan.net**.

DNS subdomains (like www.evil.org) are better described in
[tq-009 subdomains of possibly censored domains](./tq-009-subdomains-of-possibly-censored-domains.md).

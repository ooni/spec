# tq-020 0x20-hack for possibly-censored domain

When we suspect a domain name to be censored in some protocol request (DNS,
HTTP, TLS), it is interesting to see if same protocol request to same endpoint
returns different error when we apply 0x20-hack to the domain.

TBD: verify that 0x20-hack is not rejected by HTTP and TLS servers.

## Examples
- [AS41843, ER-Telecom, Omsk, Russia](https://github.com/ooni/probe/issues/647#issuecomment-275999682) 0x20-hack works for TLS

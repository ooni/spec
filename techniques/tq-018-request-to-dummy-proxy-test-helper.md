# tq-018 Request to dummy proxy test helper

When we suspect an IP address or domain name to be censored, we can do a
request to proxy-like test-helper and see if request is blocked. See “request
to discard test helper” for possible test-helper capabilities. At least
following protocols are interesting to test:

- HTTP proxy call with domain name in `Host` header
- CONNECT to domain name
- Socks5 connection to domain name
- CONNECT to IP address 
- Socks5 connection to IP address

A TCP request triggering a suspected-to-be-injected response should follow if
the client gets a reply from test-helper. The test helper always gives positive
reply, but never actually relay any traffic. Test helper should pass “proof of
genuine reply” in headers so client can distinguish transparent proxy
intercepting requests to proxies from genuine dummy proxy.

That is slightly different from “request to discard test helper” technique as
proxy protocol may be different from “triggering request”, e.g. it’s possible
to do OpenVPN/TCP hello over CONNECT.

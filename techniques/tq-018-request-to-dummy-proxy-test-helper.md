# tq-018 Request to dummy proxy test helper

When we suspect an IP address or domain name to be censored, we can do a
request to a proxy-like test-helper and see if the request is being blocked. See “request
to discard test helper” for possible test-helper capabilities. At least the
following protocols are interesting to test:

- HTTP proxy call with domain name in `Host` header
- CONNECT to domain name
- Socks5 connection to domain name
- CONNECT to IP address 
- Socks5 connection to IP address

A TCP request triggering a suspected-to-be-injected response should follow if
the client gets a reply from the test-helper. The test helper always gives positive
reply, but never actually relays any traffic. Test helpers should pass “proof of
genuine reply” in headers so a client can distinguish a transparent proxy
intercepting requests to proxies from a genuine dummy proxy.

That is slightly different from the “request to discard test helper” technique as
the proxy protocol may be different from a “triggering request”, e.g. it’s possible
to do OpenVPN/TCP hello over CONNECT.

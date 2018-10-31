# tq-026 SNI-free and fake-SNI TLS ClientHello

If a TLS request triggers an unexpected response it is interesting to check the
role of [SNI field](https://tools.ietf.org/html/rfc3546#section-3.1) in
triggering the behavior. SNI may be both “expectedly” absent (e.g.
https://1.1.1.1) and “expectedly” present (TLS1.2, TLS1.3 without
[ESNI](https://blog.cloudflare.com/encrypted-sni/)). Outcome of following
tricks may be inspected:

- absent SNI may be filled with related<sup>[1](#fn1)</sup> domain (e.g. “one.one.one.one” for “1.1.1.1”)
- absent SNI may be filled with unrelated domain (e.g. “example.org”)
- present SNI may be dropped
- present SNI may be replaced with related<sup>[1](#fn1)</sup> domain that also has risk to be censored
- present SNI may be replaced with unrelated domain, but control measurement should check for “expected” server reply in this case

<a name="fn1">1</a>: domain “related” to the IP address may be extracted from dataset like [Rapid7 Forward DNS](https://opendata.rapid7.com/sonar.fdns_v2/), some data may be also extracted from TLS certificate presented from SNI-free query

## Examples
- AS8997, Russia blocks requests to https://1.1.1.1 without SNI field, but requests with SNI=one.one.one.one pass
- AS8997, Russia blocks requests to https://rutracker.org when SNI field exists, but requests to same endpoint without SNI field pass
- [Iran blocked www.instagram.com](https://ooni.torproject.org/post/2018-iran-protests-pt2/) using information both from SNI and unencrypted Server Certificate, these two cases had different timing pattern

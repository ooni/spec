# tq-026 SNI-free and fake-SNI TLS ClientHello

If a TLS request triggers an unexpected response it is interesting to check the
role of the [SNI field](https://tools.ietf.org/html/rfc3546#section-3.1) in
triggering the behavior. SNI may be both “expectedly” absent (e.g.
https://1.1.1.1) and “expectedly” present (TLS1.2, TLS1.3 without
[ESNI](https://blog.cloudflare.com/encrypted-sni/)). The outcome of the following
tricks may be inspected:

- absent SNI may be filled with a related<sup>[1](#fn1)</sup> domain (e.g. “one.one.one.one” for “1.1.1.1”)
- absent SNI may be filled with an unrelated domain (e.g. “example.org”)
- present SNI may be dropped
- present SNI may be replaced with a related<sup>[1](#fn1)</sup> domain that also has a risk to be censored
- present SNI may be replaced with an unrelated domain, but control measurement should check for “expected” server reply in this case

<a name="fn1">1</a>: a domain “related” to the IP address may be extracted from a dataset like the [Rapid7 Forward DNS](https://opendata.rapid7.com/sonar.fdns_v2/), some data may also be extracted from the TLS certificate presented via a SNI-free query

## Examples
- AS8997, Russia blocks requests to https://1.1.1.1 without SNI field, but requests with SNI=one.one.one.one pass
- AS8997, Russia blocks requests to https://rutracker.org when SNI field exists, but requests to the same endpoint without an SNI field pass
- [Iran blocked www.instagram.com](https://ooni.torproject.org/post/2018-iran-protests-pt2/) using information both from SNI and unencrypted Server Certificate, these two cases have different timing patterns

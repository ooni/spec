# tq-021 TLS cert recording

Every TLS connection observing certificate validation anomalies should record
full certificate as injection of self-signed certificate is another method for
transparency of TLS-based protocols censorship. Failure to validate certificate
should be recorded, but should not block the connection as some ISPs serve
blockpages for https URLs that way.

OONI Probe may prefer to ship it’s own CA bundle to avoid trusting “enterprise”
CAs in “enterprise” networks on BYOD devices running OONI Probe.

OONI should not submit to [CertificateTransparency](https://www.certificate-transparency.org/how-ct-works)
logs without understanding if the issuing CA is
[Locally-trusted “enterprise” CA](https://chromium.googlesource.com/chromium/src/+/master/net/docs/certificate-transparency.md#Certificate-Transparency-for-Enterprises)
or not. It may be not trivial to implement while shipping own CA bundle.

TLS1.3 will require certificate being exported from TLS library as TLS1.3 encrypts it on the wire.

TBD: it’s unclear if TLS certificates recording should be always-on feature.

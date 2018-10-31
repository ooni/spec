# tq-999 Backlog

Following techniques are out of scope of currently described techniques as they’re hard to ship to our current userbase.

These tricks require non-trivial network setup or elevated privileges on users’ system:

- IP fragmentation (both for UDP and TCP). It needs root, but it is fun for sure: http://www.dtic.mil/dtic/tr/fulltext/u2/a391565.pdf, https://monkey.org/~dugsong/fragroute/
- TCP reordering
- overlapping TCP segments
- exfiltration of protocol metadata from packet capture

These tricks are considered too labor-intensive for us to properly implement currently:

- Good ESNI support. ESNI is just rolled out, censors’ move is unclear
- Ancient SSL test to see if a middlebox “allows” a handshake with pre-historical version of TLS protocol unlike the “expected” server behind same IP address
- TLS1.3 / TLS1.2 contrast to check if ServerCertificate triggers “censors” (TLS1.3 encrypts ServerCertificate on the wire)
- [SNI Proxy test helper](https://github.com/dlundquist/sniproxy). While it's useful to have a test-helper on an "unrelated" IP address returning valid (proxied) or self-signed certificate for any domain we want, the usefulness of this data will be declining quite rapidly during TLS1.3 rollout in Browsers and Webservers as TLS1.3 encrypts ServerCertificate on the wire and needs no additional configuration unlike ESNI. Also, we’ve not seen (yet) a DPI doing both ServerCertificate-based filtering and Certificate chain validation, so that’s not a useful bit of data (yet).
- Throttling detection for HTTP and HTTPS: one way to measure it is to find some web asset that has a reasonable size and measure the bandwidth with precise timing information while downloading that web asset, the baseline for bandwidth may be NDT
- Analysis of collected TCP_INFO samples
- Analysis of collected NDT and DASH samples
- Detection of protocol-based blocking and throttling of UDP- and TCP-based VPNs
- Handling “stateful” filter that “learns” network endpoints (like one of ISPs in China blocking access to all websites after visiting “bad” URL, like one of Russian ISPs banning IP:Port temporary after MTProto-like handshake, like one of ISPs in Turkmenistan blocking residential connection for a while after an attempt to use VPN)

- EICAR request & [`Server: EICAR`](https://twitter.com/__phw/status/1039596771993776128) HTTP header are fun and may trigger antivirus middleboxes, but it’s unclear if those are middleboxes OONI is looking for
- [ReQrypt](https://reqrypt.org/reqrypt.html)-like tricks passing requests out-of-band to see if reply is censored
- all the stuff that [Netalyzr](https://trac.torproject.org/projects/tor/wiki/doc/OONI/CensorshipDetectionTools/Netalyzr) does

These tricks have unclear value, their value should be confirmed by examples (experiments):
- DNS “whoami” test-helper responding with requester’s IP address to every A / AAAA / TXT(?) query. It may help to capture transparent DNS proxies. It’s unclear if it is **significantly** better than publicly available “o-o.myaddr.l.google.com”, “whoami.akamai.net” and “myip.opendns.com” available via resolver{1,2}.opendns.com.

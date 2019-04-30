# tq-035 Blocking QUIC

[QUIC](https://quicwg.org/) is a new transport protocol built on UDP. QUIC is
a stream based protocol that provides congestion control, connection
multiplexing, IP migration, data encryption, etc. In addition, it is expected
to improve human rights on the Internet<sup>[1](#fn1)</sup>.
HTTP is the fundamental Web protocol and QUIC is going to be used for the next
version of HTTP - [HTTP/3](https://en.wikipedia.org/wiki/HTTP/3).
To prepare for the future of the Web it is useful to understand
how accessible QUIC is today. Unfortunately, there already exists discussions
on blocking it among system administrators and ISPs <sup>[2](#fn2)</sup>
<sup>[3](#fn3)</sup> <sup>[4](#fn4)</sup>.

## Methodology

1. Run a QUIC server listening on 443 and some random port(s).
2. Send some random data over QUIC to all ports.
3. Make the server simply echo the data.
4. Wait for the data from the server and check if it matches the originally
   sent one.

## References

1. <a name="fn1">https://tools.ietf.org/html/draft-martini-hrpc-quichr-00</a>
2. <a name="fn2">https://www.reddit.com/r/paloaltonetworks/comments/6yqpjf/anyone_blocking_quic</a>
3. <a name="fn3">https://www.reddit.com/r/networking/comments/9wriid/http3quic_and_the_yawning_abysmal_division</a>
4. <a name="fn4">https://www.reddit.com/r/k12sysadmin/comments/9w9jdr/quic_protocol_to_block_or_not_to_block</a>

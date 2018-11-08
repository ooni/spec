# tq-024 TCP segmentation

If a TCP request triggers an unexpected response it is interesting to see if the unexpected response persists if the request is segmented into several distinct packets. There are several segmentation strategies:

- Split the request in the middle of the “badword” (domain, URL, binary fingerprint)
- Split the request in the beginning of the request to confuse the DPI protocol detection and prevent a reassembly attempt
- Send the request byte-by-byte with some [packet pacing](https://en.wikipedia.org/wiki/TCP_pacing), maybe considering [LSO/TSO/GSO](https://en.wikipedia.org/wiki/Large_send_offload) 
- Send the request byte-by-byte waiting for bytes to be ACKed
- HTTP-specific: some DPI boxes are erratically triggered as soon as they see “Host: censored.org” without seeing “\r\n” (so the request can become “Host: censored.org.ru”)

Nagle should be disabled to prevent the kernel from gluing packets together (see TCP_NODELAY).

TBD: conduct a series of experiments and collect examples to define reasonable segmentation rules (all of them?)

TBD: is `TCP_MAXSEG` useful for this purpose? It may affect segment sizes in both directions as it may be used to announce small MSS to peer.

## Example
- [GoodbyeDPI](https://github.com/ValdikSS/goodbyedpi) and [brdgrd](https://github.com/NullHypothesis/brdgrd) work at different edges of the network with some non-zero success rate for HTTP, HTTPS, Tor/TLS, OpenVPN/TCP
- TBD: Philipp Winter has paper on the bisection search method for discovering the exact fingerprint the censor is using.

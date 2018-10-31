# tq-030 Fingerprinting requests for transparent proxies

If we suspect a transparent proxy handling a DNS or HTTP request on behalf of the origin server, then we can send several fingerprinting requests to get more knowledge about the specific proxy implementation:

- HTTP Squid has “[GET cache_object://localhost/info HTTP/1.1\r\n](https://github.com/ooni/probe-legacy/blob/master/ooni/nettests/experimental/http_trix.py)” request (single “\r\n”!)
- DNS servers may answer `CHAOS` `TXT` queries for “version.bind”, “hostname.bind”, “id.server” and “version.server”, [RIPE Atlas mass-collects that info](https://atlas.ripe.net/docs/built-in/)

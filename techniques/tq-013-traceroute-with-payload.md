# tq-013 traceroute with payload

If a TCP<sup>[1](#fn1)</sup> or UDP<sup>[2](#fn2)</sup> request triggers an
unexpected response it is interesting to do a traceroute with that payload to
understand if we can point to a network location possibly responsible for the
unexpected response. It is also interesting to compare the result of the
experiment to an ordinary traceroute without payload. A UDP experiment should
account for multi-path and perform several experiments following the logic of
paris-traceroute<sup>[3](#fn3)</sup>. A TCP experiment can’t do that
without root as it’s impossible to stick to the path (reuse 5-tuple) within
reasonable timeframe as it requires to wait for `TIME_WAIT` timeout (order of
minutes) before performing the next experiment.

<a name="fn1">1</a>: DNS/TCP, TLS Client Hello, Tor/TLS, HTTP GET, OpenVPN/TCP and so on

<a name="fn2">2</a>: DNS/UDP, OpenVPN/UDP

<a name="fn3">3</a>: TBD: does dublin-traceroute provide any useful extension above paris-traceroute?

TBD: does `IP_RECVERR` + `IP_TTL` provide enough information for TCP sockets

# tq-014 TCP injection blocking with BPF

If a TCP request triggers a "suspected-to-be-injected response" (RST packet, TLS
Error, HTTP redirect not matching a control) it is interesting to repeat the same
measurement by blocking the "supected-to-be-injected response" with a BPF filter<sup>[1](#fn1)</sup> and
observing if the latency of an error or response changes. The filter can be made to
match packet data, TCP and IP headers.

The test may uncover “single-sided on-path injector” if injection blocking
leads to “normal” communication.

That is specific to TCP as UDP can wait for another reply to come and both
replies will be delivered to the same socket, UDP does not need special
machinery as it has no L4 state (no connection, no “stream” of bytes to
overwrite). Although, UDP has L3 state (like PMTU), but we haven't 
observed PMTU being used for filtering purposes (yet).

It is also possible to attach and detach a drop-all BPF filter using a timer and
try to win the race (drop the injected packets within time window) without
generating BPF code to match content dynamically. It MAY be beneficial to
follow the “race” method when an injected response tries to circumvent the filter
splitting redirect into different TCP segments or IP fragments. We
hope that filters are not going to play _that_ sort of cat-and-mouse game
against an attempt to increase transparency of network filters.

See the PoC implementation at [github.com/darkk/rstlss](https://github.com/darkk/rstlss).

<a name="fn1">1</a>: `SO_ATTACH_BPF` is available to non-privileged users at least on Linux and Android

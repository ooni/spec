# tq-014 TCP injection blocking with BPF

If a TCP request triggers a suspected-to-be-injected response (RST packet, TLS
Error, HTTP redirect not matching a control) it is interesting repeating a
measurement blocking that response with BPF filter<sup>[1](#fn1)</sup> and
observing if latency of error or response changes. The filter can match packet
data, TCP and IP headers.

The test may uncover “single-sided on-path injector” if injection blocking
leads to “normal” communication.

That is specific to TCP as UDP can wait for another reply to come and both
replies will be delivered to the same socket, UDP does not need special
machinery as it has no L4 state (no connection, no “stream” of bytes to
overwrite). Although, UDP has L3 state (like PMTU), but the author has not
observed PMTU being used for filtering purposes (yet).

It is also possible to attach and detach drop-all BPF filter using timer and
try to win the race (drop the injected packets within time window) without
generating BPF code to match content dynamically. It MAY be beneficial to
follow “race” method when injected response tries to circumvent the filter
splitting redirect into different TCP segments or IP fragments. The author
hopes that filters are not going to play _that_ sort of cat-and-mouse game
against an attempt to increase transparency of network filters.

<a name="fn1">1</a>: `SO_ATTACH_BPF` is available to non-privileged users at least on Linux and Android

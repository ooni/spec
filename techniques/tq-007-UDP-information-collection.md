# tq-007 UDP information collection

UDP client should `bind()` to random port for every query sent to the same
server<sup>[1](#fn1)</sup> and should not reuse same 5-tuple for retries.
It should enable `IP_RECVERR` and `IP_RECVTTL` to collect more metadata.

Random UDP source port ...
- alows to distinguish ICMP errors delivered via `IP_RECVERR` to `MSG_ERRQUEUE` across queries
- accounts for ECMP-like<sup>[2](#fn2)</sup> broken paths
- is BCP to prevent blind DNS/UDP spoofing

<a name="fn1">1</a>: unless doing traceroutes or other alike measurements that
SHOULD preserve path like paris-traceroute does

<a name="fn2">2</a>: that accounts for unlikely but possible sources of DNS
timeouts: when the route to resolver is load-balanced using 5-tuple at any
stage of the network path: ECMP routes, different queues of NIC, etc.

# tq-007 Handle ECMP while doing DNS

DNS client should `bind()` to random port for every DNS query sent to the same
server (unless doing traceroutes or other alike measurements) and should not
reuse same 5-tuple for retries.

Adding entropy to source port is also one of best current practices to prevent
blind DNS spoofing.

That also accounts for possible sources of DNS timeouts: when the route to
resolver is load-balanced using 5-tuple at any stage of the network path: ECMP
routes, different queues of NIC, etc.

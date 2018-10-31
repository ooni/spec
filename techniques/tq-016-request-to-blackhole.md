# tq-016 Request to blackhole

If a TCP or UDP request triggers an unexpected response it is interesting to
send that request to endpoint that is not expected to reply that request and/or
protocol. It may be interesting to preserve destination port.

E.g. sending TLS ClientHello to 8.8.8.8:53 TCP and see if it gets “censored” reply.

E.g. sending OpenVPN/UDP hello to the IP address that is routable but acts as blackhole.

E.g. sending DNS/UDP request to the IP address that is not routed in global BGP table.

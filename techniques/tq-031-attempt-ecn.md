# tq-031 Attempt use of Explicit Congestion Notification

When a transparent HTTP or TLS proxy is in the path between the probe and the
target server, an attempt to use explicit congestion notification (ECN) may
reveal its presence in following ways:

1. The connection fails due to unknown TCP flags being set
2. The connection fails due to unknown IP flags being set
3. ECN is not negotiated where expected, or is negotiated where it is not
   expected

## Methodology

1. Fetch a webpage from a target server using either HTTP or HTTPS, negotiating
   ECN.
3. If the first connection failed, retry the request without attempting to
   negotiate ECN to confirm that this was responsible for the connectivity
   failure, and not just that the host was down

## Implementation issues

- To use ECN on Linux, it is necessary to enable a sysctl switch in the kernel
  which would typically require root access. This also affects *all* new
  connections and so this test should not be scheduled to run in parallel with
  other tests. A userland TCP stack would be able to implement per-connection
  ECN logic, but would require raw sockets.
- To confirm that ECN usage was successful it is necessary to perform a packet
  capture, while connectivity failures can be confirmed from the application
  layer feedback alone
- Analysis of raw packets, and also setting the flags for TCP negotiation,
  could be performed using an eBPF program which could be attached from
  userspace. Some information on this can be found in [an LWN
  article](https://lwn.net/Articles/740157/).
- It would be possible to attempt the use of multiple protocol features on the
  first connection, falling back to trying each individually only if the first
  connection fails. In some rare cases the use of a protocol feature can brick
  the CPE or upstream middleboxes but this should either happen immediately or
  never happen.

## Examples

- Censorship infrastructure was discovered using this technique in the EE
  mobile operator network in the United Kingdom. See: I. R. Learmonth, A. Lutu,
  G. Fairhurst, D. Ros and Ö. Alay, "[Path transparency measurements from the
  mobile edge with
  PATHspider](https://iain.learmonth.me/stuff/pubs/PATHspiderMobile2017.pdf),"
  *2017 Network Traffic Measurement and Analysis Conference (TMA)*, Dublin, 2017,
  pp. 1-6. doi:10.23919/TMA.2017.8002922

## References

- [RFC3168: The Addition of Explicit Congestion Notification (ECN) to IP](https://tools.ietf.org/html/rfc3168)

## Implementations

- An independent implementation exists for this technique in PATHspider's [ECN
  plugin](https://pathspider.readthedocs.io/en/latest/plugins/ecn.html)

# tq-033 Attempt use of TCP Fast Open

When a transparent HTTP or TLS proxy is in the path between the probe and the
target server, an attempt to use TCP fast open may reveal its presence in
following ways:

1. The connection fails due to an unknown TCP option being present
2. The second connection fails due to data being present on the TCP SYN packet
3. TCP fast open is not negotiated where expected, or is negotiated where it is
   not expected

## Methodology

1. Fetch a webpage from a target server using either HTTP or HTTPS, using TCP
   fast open to establish a TFO cookie
2. If successful, fetch a webpage from the same server, again using TCP fast
   open (this time will have data on the SYN)
3. If the first connection failed, retry the request without the use of the TCP
   fast open to confirm that this was responsible for the connectivity failure,
   and not just that the host was down

## Implementation issues

- To confirm that TCP fast open usage was successful (negotiation and use of
  TFO cookie) it is necessary to perform a packet capture, while failures
  can be confirmed from the application layer feedback alone
- Analysis of raw packets could be performed using an eBPF program which could
  be attached from userspace. Some information on this can be found in [an LWN
  article](https://lwn.net/Articles/740157/).
- It would be possible to attempt the use of multiple protocol features on the
  first connection, falling back to trying each individually only if the first
  connection fails. In some rare cases the use of a protocol feature can brick
  the CPE or upstream middleboxes but this should either happen immediately or
  never happen.

## Examples

- None yet for TCP fast open, although this technique uses similar principles
  to discover middleboxes as presented in: I. R. Learmonth, A. Lutu, G.
  Fairhurst, D. Ros and Ö. Alay, "[Path transparency measurements from the mobile
  edge with
  PATHspider](https://iain.learmonth.me/stuff/pubs/PATHspiderMobile2017.pdf),"
  *2017 Network Traffic Measurement and Analysis Conference (TMA)*, Dublin, 2017,
  pp. 1-6. doi:10.23919/TMA.2017.8002922

## References

- [RFC7413: TCP Fast Open](https://tools.ietf.org/html/rfc7413)

## Implementations

- An independent implementation exists for this technique in PATHspider's [TFO
  plugin](https://pathspider.readthedocs.io/en/latest/plugins/tfo.html)

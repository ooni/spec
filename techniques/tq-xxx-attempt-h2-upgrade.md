# tq-xxx Attempt upgrade to H2

When a transparent HTTP proxy is in the path between the probe and the target
server, an attempt to upgrade to H2 may reveal its presence in one of the
following ways:

1. The connection fails due to an unknown header being present
2. The header is passed successfully to the server but the connection fails
   because the reply using h2c was not understood by the proxy
3. A server that is expected to negotiate h2 or h2c does not, or a server that
   is not expected to negotiate h2 or h2c does

When a transparent TLS proxy is in the path, it may reveal its presence in
one of the following ways:

1. Stripping the ALPN option which would cause h2 to not be negotiated where
   expected
2. The connection fails because the ALPN option is unknown

## Methodology

1. Fetch a webpage from a target server using either HTTP or HTTPS, with an H2
   upgrade mechanism
2. If the connection fails, retry the request without the use of the upgrade
   mechanism to confirm that this was responsible for the connectivity failure,
   and not just that the host was down

## Implementation issues

- It would be possible to attempt the use of multiple protocol features on the
  first connection, falling back to trying each individually only if the first
  connection fails. In some rare cases the use of a protocol feature can brick
  the CPE or upstream middleboxes but this should either happen immediately or
  never happen.

## Examples

- None yet

## References

- [Protocol upgrade mechanism](https://developer.mozilla.org/en-US/docs/Web/HTTP/Protocol_upgrade_mechanism) at MDN web docs
- [RFC7540: Hypertext Transfer Protocol Version 2 (HTTP/2)](https://tools.ietf.org/html/rfc7540)

## Implementations

- An independent implementation exists for this technique in PATHspider's [H2
  plugin](https://pathspider.readthedocs.io/en/latest/plugins/h2.html)

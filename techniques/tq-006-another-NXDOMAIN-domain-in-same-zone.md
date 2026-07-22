# tq-006 Check another “NXDOMAIN” domain in same zone

When the suspected-to-be-censored domain returns the `NXDOMAIN` error from the resolver
it is interesting to attempt a resolution of another domain that we know for sure to not exist. These two
queries may result in different outcomes that may be a sign of network
interference.

## Examples
- AS22047, VTR, Chile — “SOA? riseup.net.” sent to ISP’s resolver resulted in an `NXDOMAIN` reply with 0 answers and 0 authority records, while “SOA? riseup-5223-547-27075.net.” also was an `NXDOMAIN` with 0 answers, but had 1 authority records “a.gtld-servers.net. Nstld.verisign-grs.com ...” with valid `Serial` and other fields clearly distinguishing it as non-existent domain.

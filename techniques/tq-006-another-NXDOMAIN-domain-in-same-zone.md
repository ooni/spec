# tq-006 Check another “NXDOMAIN” domain in same zone

When suspected-to-be-censored domain returns `NXDOMAIN` error from the resolver
it is interesting to check for another for sure non-existent domain. These two
queries may result in different outcomes that may be sign of network
interference.

## Examples
- AS22047, VTR, Chile — “SOA? riseup.net.” sent to ISP’s resolver resulted in an NXDOMAIN reply with 0 answers and 0 authority records, while “SOA? riseup-5223-547-27075.net.” also was an NXDOMAIN with 0 answers, but had 1 authority records “a.gtld-servers.net. Nstld.verisign-grs.com ...” with valid Serial and other fields clearly distinguishing it as non-existent domain.

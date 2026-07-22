tq-034 Request DNSSEC-related records from resolver
===================================================

When a network operator provides a DNS resolver for clients either explicitly
or through the use of injection or hijacking, it may also prevent the request
of DNSSEC-related records. These include DS, DNSKEY, NSEC, and RRSIG. This
would prevent the client's ability to verify records served by the operator's
resolver and leave the client vulnerable to spoofed records.

A resolver may support DNSSEC while a middlebox that alters responses does not
which would result in the signature not being valid.

Methodology
-----------

1. Attempt to validate the full chain of DNSSEC signatures back to the root
   zone for a hostname that is known to have valid DNSSEC signatures set up
2. If it was possible to retrieve the full chain of signatures, validate them

Implementation issues
---------------------

This test would require performing a "stub" resolution, where the requests
that would have been made to the authoritative servers would instead be
made to the resolver.

Examples
--------

- None as seen in the wild for deliberate censorship reasons
- Older resolvers, especially appliances that may now be end-of-life, may not
  have support for these records

References
----------

[RFC4034: Resource Records for the DNS Security Extensions](https://www.ietf.org/rfc/rfc4034.txt)

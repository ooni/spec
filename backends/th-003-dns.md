# Specification version number

2013-09-26-000

# Specification name

  DNS Test Helper

# Helper preconditions

 * An Internet connection.
 * An Internet-Reachable UDP Port. (Typically 53)

# Expected impact

  Provides a public recursive DNS resolver with all of the known drawbacks to
  doing so.

# Expected inputs

  Any valid DNS Queries

## Required input data

  A valid DNS Query

## Semantics

  The implementation depends on twisted.names.server.DNSFactory and forwards
  all requests to an upstream resolver. The default resolver is Google public
  DNS (8.8.8.8).

# Helper description

  An Open Recursive DNS Resolver.

# Expected output

  A Response to a DNS Query.

## Required output data

  A Response to a DNS Query.

## Possible conclusions

  An ooni-probe client can use the DNS Test Helper as a control resolver in
  tests that to determine if an experiment resolver is tampering with DNS
  responses.

## Known Limitations

  Running an open public recursive resolver is not recommended. Miscreants
  scan the Internet looking for recursive resolvers and use them in traffic
  reflection attacks to DoS victims.

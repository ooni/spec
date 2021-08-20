# Specification version number 

2013-09-26-000

* status: _obsolete_

# Specification name

TCP Echo Test Helper

# Helper preconditions

* An Internet connection
* An Internet-Reachable TCP Port.

# Expected impact

Ability to help an ooni-probe client determine if TCP payload has been
modified in transit.

# Expected inputs

Bytes received over TCP.

## Semantics

TCP Echo helper listens on a TCP port and writes any bytes received back to
the connected client. The implementation depends on
twisted.internet.TCPServer and the TCP and lower protocols are therefore
transparent to the helper.

# Helper description

A TCP Echo service.

# Expected output

Bytes received over TCP.

## Required output data
  
All unmodified received bytes.

## Possible conclusions

The TCP Echo test helper can be used by ooni-probe tests to determine if
the TCP payload has been modified in transit.

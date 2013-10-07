# Specification version number

2013-10-07-000

# Specification name

Multi Port Traceroute test

# Test preconditions

  * An internet connection.
  * Ability to run ooni-probe as root or with raw sockets capabilities

For reporting to the backend to work that it is possible for the probe to
establish a connection to the Tor network.

# Expected impact

  * Ability to determine differences in network paths of
    different protocols and ports


# Expected inputs

  * No additional inputs are required as the destination host
    (backend) defaults to 8.8.8.8. The backend can optionally
    be specified with argument -b.

  * Additional parameters such as source port, maximum TTL,
    and timeout values can also be set


## Semantics

  * The backend host is specified as a dotted-quad IPv4
    address.

  * Maximum TTL defaults to 30.

# Test description

A series of packets are constructed and sent to the backend
host with incrementing TTL values (traceroute).

See also: https://tools.ietf.org/rfc/rfc792.txt

For protocols UDP and TCP, a traceroute is performed for each
of the following ports: 0, 22, 23, 53, 80, 123, 443, 8080,
65535.

For protocol ICMP, there is only a single series of packets
as there is no concept of ports.

The time-exceeded ICMP responses are added to the report. 

# Expected output

The collected ICMP time-exceeded responses from IP routers
that properly implement RFC792 in the forward path towards
the backend host. 

## Parent data format

df-003-scapyt

## Semantics

The report object will contain keys of the format "hops_" +
port, e.g. report['hops_22']. The corresponding value is an
ordered list of the parsed responses, encoded like so:

{'ttl': The TTL of the packet sent,
 'address', The address of the remote host at which the TTL expired,
 'rtt', the round-trip-time, measured as the difference between the received response and sent packet time.
 'sport', the source port of the sent packet
}

## Possible conclusions

By examining the differences in the responses between protocols and destination ports, it is possible to ascertain that routing decisions are made on a protocol layer above IP, and determine what path was taken for different protocols.

## Example output sample

XXX: currently bugged by https://github.com/TheTorProject/ooni-probe/issues/214

# Privacy considerations

The scapyt report format includes the binary packets as sent or received. In the ICMP response payload a portion (64 bits) or all of the original packet is returned. The client source address will be contained in the report.

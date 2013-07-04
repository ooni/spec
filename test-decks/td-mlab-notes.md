This is the list of tests that shall be included inside of the MLAB test deck:


## HTTP Invalid Request Line

This tests does some basic fuzzing on the HTTP request line, generating a
series of invalid HTTP requests between the OONI test client and the M-Lab
server. The M-Lab server runs a TCP echo test helper, and if the response from
the server doesn’t match with what was sent, the conclusion is that tampering
is occurring. The assumption driving this methodology is that certain
transparent HTTP proxies may not properly parse the HTTP request line.

## DNS Spoof

This test detects DNS spoofing by performing a query to a test resolver and to
a validated control resolver. The query is considered tampered with if the two
responses do not match.

## Header Field Manipulation 

This test client sends HTTP requests request headers that vary capitalization
toward an HTTPReturnJSONHeaders test helper backend running on an M-Lab server.
If the headers received by the M-Lab server don’t match those sent, tampering
is inferred.

## Multi-port Traceroute

This test performs a multi port, multi-protocol traceroute from an OONI client
toward an M-Lab server. The goal of such is to determine biases in the paths
based on destination port. Destination ports are 22, 23, 80, 123, 443. Note
that if the user has opted not to include source IP in the report then source
and destination IP will be eliminated from the collected data. Note that while
a user may be able to opt not to eliminate IP address, we will need to
provision an option for those who wish IP not to be collected.

## HTTP Host

This test detects the presence of a transparent HTTP proxy and enumerates the
sites it is configured to censor. To do this the test places the hostname of a
probable censored site inside of the Host header field, and communicates this
stream of data between an OONI client and an M-Lab server. If the response from
the server doesn’t match the data sent, the test determines the presence of a
transparent HTTP proxy.

## DNS Tamper

This test performs A queries to a set of test resolvers and a validated control
resolver. If the two results do not match it performs a reverse DNS lookup on
the first A record address of both sets of queries, checking that they both
resolve to the same name. NOTE: This test frequently results in false positives
due to GeoIP-based load balancing on major global sites such as Google,
Facebook, and Youtube, etc. This will need to be noted and accounted for.


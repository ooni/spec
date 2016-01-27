# Specification version number

2013-01-30-000

# Specification name

DNS Consistency Test

# Test preconditions

  * An internet connection
  * A unfiltered connection to a DNS resolver that is not performing censorship

For reporting to the backend to work that it is possible for the probe to
establish a connection to the Tor network.

# Expected impact

Ability to detect if A DNS queries for a certain hostname are being tampered with.

# Expected inputs

  * A list of hostnames to be tested for censorship
  * A list of DNS resolvers to be tested for censorship
  * A DNS resolver that is not being tampered with (control_resolver)

The list of hostnames should be in a text file and separated by newline.

Example:

    one.example.com
    two.example.com
    three.example.com

The list of DNS resolvers to test for tampering shold be in a text file as
dotted quads separated by a newline:

Example:

    1.1.1.1
    2.2.2.2
    3.3.3.3

# Test Description

For each hostname to be tested we do the following:

We perform an A DNS query (via UDP) to the control resolver. The answer to such
query is called the control answer.

For each DNS resolver to be tested we perform an A DNS query for the domain in
question. We then compare this answer (experiment answer) with the control
answer.

If the two have a common IPV4 address then the hostname is not considered to be
tampered with the resolver in question (tampering: False)

If they do not have commonalities we take the first IPV4 address in the control
answer and the first IPV4 address in the experiment answer and do a reverse
lookup. If the two reverse lookups match (the PTR record points to the same
hostname), we take note of this (tampering: "reverse_match").

In any other case we mark the result as: tampering: True.

# Expected output

## Data format

df-002-dnst

## Semantics

Two extra dicts will be present inside of every report entry:

tampering:
  **dict** containing as keys the IPv4 addresses of the test resolvers
  and as values True|False|'reverse_match'

test_resolvers:
  **list** of IPv4 addresses of the test resolvers

## Possible conclusions

That the DNS resolver in question has provided a false response to a DNS Query.

## Expected post-processing efforts

## Example output sample

    input: example.com
    control_resolver: &id001 [203.0.113.1, 53]
    queries:
    - addrs: [203.0.113.2]
      answers:
      - [<RR name=example.com type=A class=IN ttl=2562s auth=False>, <A address=203.0.113.2
          ttl=2562>]
      query: '[Query(''example.com'', 1, 1)]'
      query_type: A
      resolver: *id001
    - addrs: [203.0.113.2]
      answers:
      - [<RR name=example.com type=A class=IN ttl=7200s auth=False>, <A address=203.0.113.2
          ttl=7200>]
      query: '[Query(''example.com'', 1, 1)]'
      query_type: A
      resolver: [203.0.113.3, 53]
    - addrs: [203.0.113.2]
      answers:
      - [<RR name=example.com type=A class=IN ttl=4007s auth=False>, <A address=203.0.113.2
          ttl=4007>]
      query: '[Query(''example.com'', 1, 1)]'
      query_type: A
      resolver: [203.0.113.4, 53]
    - addrs: [203.0.113.2]
      answers:
      - [<RR name=example.com type=A class=IN ttl=7200s auth=False>, <A address=203.0.113.2
          ttl=7200>]
      query: '[Query(''example.com'', 1, 1)]'
      query_type: A
      resolver: [203.0.113.5, 53]
    - addrs: [203.0.113.2]
      answers:
      - [<RR name=example.com type=A class=IN ttl=7200s auth=False>, <A address=203.0.113.2
          ttl=7200>]
      query: '[Query(''example.com'', 1, 1)]'
      query_type: A
      resolver: [203.0.113.6, 53]
    - addrs: [203.0.113.2]
      answers:
      - [<RR name=example.com type=A class=IN ttl=7200s auth=False>, <A address=203.0.113.2
          ttl=7200>]
      query: '[Query(''example.com'', 1, 1)]'
      query_type: A
      resolver: [203.0.113.7, 53]
    - addrs: [203.0.113.2]
      answers:
      - [<RR name=example.com type=A class=IN ttl=7200s auth=False>, <A address=203.0.113.2
          ttl=7200>]
      query: '[Query(''example.com'', 1, 1)]'
      query_type: A
      resolver: [203.0.113.8, 53]
    - query: '[Query(''example.com'', 1, 1)]'
      query_type: A
      resolver: [203.0.113.9, 53]
    - query: '[Query(''example.com'', 1, 1)]'
      query_type: A
      resolver: [203.0.113.1, 53]
    - failure: deferred_timeout_error
      query: '[Query(''example.com'', 1, 1)]'
      query_type: A
      resolver: [203.0.113.10, 53]
    tampering: {203.0.113.11: no_answer, 203.0.113.6: false, 203.0.113.4: false, 203.0.113.5: false,
      203.0.113.7: false, 203.0.113.3: false, 203.0.113.9: no_answer, 203.0.113.8: false}
    test_resolvers: [203.0.113.3, 203.0.113.4, 203.0.113.5, 203.0.113.6, 203.0.113.7,
      203.0.113.8, 203.0.113.9, 203.0.113.11, 203.0.113.10]
    test_name: test_a_lookup
    test_runtime: 2.6424369812011719
    test_started: 1357167921.0688701
    ...

# Privacy considerations

This test does not inherently risk leaking user information.

# Packet capture considerations

We do not do any packet capturing, this test only requires to be able to create
UDP sockets.

# Notes

Sites that do geolocation based load balancing via DNS will report a different
set of IPv4 addresses depending on the source of the DNS request. For this
reason we also do a reverse lookup to check to see if the domain pointers of
the IP addresses match.
This means of seeding out false positive, though, is also not that effective
since in some circumstances also the PTR record will point to a different
domain name.

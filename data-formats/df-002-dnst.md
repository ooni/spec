# DNSTest template data format

Data Format Version: df-001-dnst-000

This is the specification of the data format that every test that is
based on ooni.templates.dnst.DNSTest shall be using.

Third party tests that run DNS related measurements SHOULD also be using such
data format.

## Specification

    queries:
      `list` of DNS query and answers for this testing session

Every DNS query is formatted as follows:

    addrs:
      `list` present if the DNS query is question is of A type and will include
      the IPv4 addresses of the answer.

    answers:
    - [`string` representation of the Resource Record of the answer (repr),
       `string` representation of the answer payload (python repr)]
    - [etc. etc.]

    query:
      `string` that is the representation (python repr) of the DNS querie(s)
      that where performed.
      This string can be passed to an instance of `twisted.names.client.Resolver`
      and it will reproduce the DNS query of this report.
      The Query object is described in `twisted.names.dns.Query`.

    query_type:
      `string` the name of the DNS query that is being performed.

    resolver: [`string` resolver IP address, `int` resolver port number]

## Example output

    input: example.com
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
    test_name: test_a_lookup
    test_runtime: 2.6424369812011719
    test_started: 1357167921.0688701
    ...


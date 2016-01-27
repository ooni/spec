# Specification version number

0.2.0

# Specification name

DNS Injection test

# Test preconditions

* An internet connection

* An IP address that will traverse a box doing DNS injection triggering an
  injected DNS response.

# Expected impact

Ability to detect the presence of DNS Injection and list of domains that are
being blocked via DNS injection.

# Expected inputs

* List of domains to test for injection.

* IP address to send DNS queries to. This IP should not have a DNS resolver
  listening on port 53 UDP or TCP.

## Semantics

one domain name per line

# Test description

For every domain in the input list we perform a A query towards the target IP
address using UDP on port 53.

We wait for a DNS response until the timeout (by default 3 seconds) is reached.

If we have received an answer by that time we say that that hostname is being
injected (since the endpoint is not a DNS resolver the answer we got must have
been injected by the censorship middle boxes).

If we don't receive an answer that means everything is as usual and we mark
that hostname as not being injected.

# Expected output

## Parent data format

df-002-dnst

## Required output data

* If the domain as input is being injected or not

## Semantics

injected: true|false
Indicates if we got an injected response for the domain in question.

## Possible conclusions

If DNS injection is being done and on which domains.

## Example output sample

```
###########################################
# OONI Probe Report for dns_injection (0.1)
# Wed Sep 10 09:34:51 2014
###########################################
---
input_hashes: [d87e90ead07a7d8ec8f8ca4724807e3fb6c7f1b9471979c934d0dc01b0bd6551]
options: [-r, 123.58.180.7, -f, domains.txt]
probe_asn: AS7922
probe_cc: US
probe_city: null
probe_ip: 127.0.0.1
software_name: ooniprobe
software_version: 1.1.1
start_time: 1410356091.339939
test_name: dns_injection
test_version: '0.1'
...
---
injected: true
input: facebook.com
queries:
- addrs: [173.252.110.27]
  answers:
  - [<RR name=facebook.com type=A class=IN ttl=121s auth=False>, <A address=173.252.110.27
      ttl=121>]
  query: '[Query(''facebook.com'', 1, 1)]'
  query_type: A
  resolver: [123.58.180.7, 53]
...
---
injected: true
input: www.twitter.com
queries:
- addrs: [199.16.156.198, 199.16.156.230, 199.16.156.6, 199.16.156.102]
  answers:
  - [<RR name=www.twitter.com type=CNAME class=IN ttl=548s auth=False>, <CNAME name=twitter.com
      ttl=548>]
  - [<RR name=twitter.com type=A class=IN ttl=16s auth=False>, <A address=199.16.156.198
      ttl=16>]
  - [<RR name=twitter.com type=A class=IN ttl=16s auth=False>, <A address=199.16.156.230
      ttl=16>]
  - [<RR name=twitter.com type=A class=IN ttl=16s auth=False>, <A address=199.16.156.6
      ttl=16>]
  - [<RR name=twitter.com type=A class=IN ttl=16s auth=False>, <A address=199.16.156.102
      ttl=16>]
  query: '[Query(''www.twitter.com'', 1, 1)]'
  query_type: A
  resolver: [123.58.180.7, 53]
...
---
injected: true
input: youtube.com
queries:
- addrs: [173.194.43.35, 173.194.43.36, 173.194.43.37, 173.194.43.38, 173.194.43.39,
    173.194.43.40, 173.194.43.41, 173.194.43.46, 173.194.43.32, 173.194.43.33, 173.194.43.34]
  answers:
  - [<RR name=youtube.com type=A class=IN ttl=300s auth=False>, <A address=173.194.43.35
      ttl=300>]
  - [<RR name=youtube.com type=A class=IN ttl=300s auth=False>, <A address=173.194.43.36
      ttl=300>]
  - [<RR name=youtube.com type=A class=IN ttl=300s auth=False>, <A address=173.194.43.37
      ttl=300>]
  - [<RR name=youtube.com type=A class=IN ttl=300s auth=False>, <A address=173.194.43.38
      ttl=300>]
  - [<RR name=youtube.com type=A class=IN ttl=300s auth=False>, <A address=173.194.43.39
      ttl=300>]
  - [<RR name=youtube.com type=A class=IN ttl=300s auth=False>, <A address=173.194.43.40
      ttl=300>]
  - [<RR name=youtube.com type=A class=IN ttl=300s auth=False>, <A address=173.194.43.41
      ttl=300>]
  - [<RR name=youtube.com type=A class=IN ttl=300s auth=False>, <A address=173.194.43.46
      ttl=300>]
  - [<RR name=youtube.com type=A class=IN ttl=300s auth=False>, <A address=173.194.43.32
      ttl=300>]
  - [<RR name=youtube.com type=A class=IN ttl=300s auth=False>, <A address=173.194.43.33
      ttl=300>]
  - [<RR name=youtube.com type=A class=IN ttl=300s auth=False>, <A address=173.194.43.34
      ttl=300>]
  query: '[Query(''youtube.com'', 1, 1)]'
  query_type: A
  resolver: [123.58.180.7, 53]
...
```

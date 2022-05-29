# DNS Data Format

This document describes the keys with `test_keys` that all experiments
using DNS SHOULD populate, possibly using directly the specific template
code. See this directory's [README](README.md) for the basic concepts.

| Name       | `dnst` |
|------------|--------|
| Version    | 0      |

## Specification

```JSON
{
    "queries": []
}
```

- `queries` (`[]Query`): list of query objects. See below.

## Query

```JSON
{
    "answers": [],
    "dial_id": 177171,
    "engine": "udp",
    "failure": "dns_nxdomain_error",
    "hostname": "dns.googlex",
    "query_type": "A",
    "resolver_address": "8.8.8.8:53",
    "resolver_hostname": "8.8.8.8",
    "resolve_port": "53",
    "t": 1.114,
    "transaction_id": 1
}
```

- `answers` (`[]Answer`): list of answer objects. See below.

- `dial_id` (`int`; optional; since 2020-01-11): identifier of a dialing
operation (i.e. name resolution followed by connect). The zero dial_id
means that we don't know the real dial ID. Applications SHOULD NOT
emit the dial_id when it is zero. Rest assured that the dial_id will
be unique during a measurement session.

- `engine` (`string`; optional): the specific engine used to perform
the DNS query. If omitted implies `"system"`, which means that we are
using in a way or another `getaddrinfo`. See also below for a list
of available resolver engines.

- `failure` (`string`; nullable): if there was an error, this field is
a string indicating the error, otherwise it MUST be `null`.

- `hostname`: (`string`): the hostname used in the DNS query, which MUST
be reversed for PTR lookups like `1.0.0.127.in-addr.arpa`.

- `query_type`: (`string`): a valid DNS query type (e.g. `MX`).

- `resolver_address`: (`string`; since 2019-12-29): more flexible way of
specifying the resolver address that also allows for DoH, because it does
not assume that the resolver is identified by an address, port tuple.

- `resolver_hostname`: (`string`; optional; deprecated): legacy way to
specify the resolver hostname when using a custom resolver. This is not
used by ooni/probe-engine, which sets it to `null`.

- `resolver_port`: (`string`; optional; deprecated): legacy way to
specify the resolver hostname when using a custom resolver. This is not
used by ooni/probe-engine, which sets it to `null`.

- `t` (`float`): number of seconds elapsed since `measurement_start_time`
measured in the moment in which `failure` is determined.

- `transaction_id` (`int`; optional; since 2020-01-11): if present, this is the
ID of the HTTP transaction that caused this query.

### DNS resolver engines

The following table documents the available DNS resolver engines.

| Engine name | Description |
| :---------- | ----------- |
| system      | We are using getaddrinfo |
| netgo       | We are using Golang's "netgo" DNS resolver |
| udp         | Custom DNS-over-UDP resolver |
| tcp         | Custom DNS-over-TCP resolver |
| dot         | Custom DNS-over-TLS resolver |
| doh         | Custom DNS-over-HTTPS resolver |

Before 2022-05-29 (i.e., for `ooniprobe<3.16.0`), we did not distinguish
between cases where we were using getaddrinfo and cases where we were
using the netgo resolver (see [ooni/probe-cli#765](
https://github.com/ooni/probe-cli/pull/765)).

## Answer

```JSON
{
    "answer_type": "AAAA",
    "expiration_limit": "",
    "hostname": "",
    "ipv4": "1.1.1.1",
    "ipv6": "",
    "minimum_ttl": "",
    "refresh_interval": "",
    "responsible_name": "",
    "retry_interval": "",
    "serial_number": 0,
    "ttl": null,
}
```

- `answer_type`: like `Query.query_type`.

- `expiration_limit` (`string`; only for SOA answers): the time
after which this zone should no longer be authoritative.

- `hostname` (`string`; optional): for PTR lookups it is the hostname
that points back to the queried IP. For CNAME lookups it is the hostname
of the alias for the IP. For SOA answers it is the hostname of the
nameserver responsible for the data of this zone.

- `ipv4` (`string`; optional): the dotted quad IPv4 (only for A answers).

- `ipv6`: like `ipv4` but for AAAA answers.

- `minimum_ttl` (`string`; only for SOA answers): the minimum ttl to
be exported with any record from this zone.

- `refresh_interval` (`string`; only for SOA answers): the time interval before
which this zone should be refreshed.

- `responsible_name` (`string`; only for SOA answers): the
mailbox of the person responsible for this zone.

- `retry_interval` (`string`; only for SOA answers): the time interval
that should be elapsed before the zone should be retried in case of failure.

- `serial_number` (`int`; only for SOA answers): version number
of the original copy of the zone.

- `ttl` (`int`; nullable): the TTL if known, otherwise `null`.

## Example

In the following example we've omitted all the keys that are
not relevant to the DNS data format:

```JSON
{
  "test_keys": {
    "agent": "redirect",
    "queries": [
      {
        "answers": [
          {
            "answer_type": "A",
            "ipv4": "149.154.167.99",
            "ttl": null
          }
        ],
        "dial_id": 177171,
        "engine": "system",
        "failure": null,
        "hostname": "web.telegram.org",
        "query_type": "A",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "",
        "t": 1.114,
        "transaction_id": 1
      }
    ]
  }
}
```

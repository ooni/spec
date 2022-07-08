# Specification version number

2022-07-08

* _status_: experimental

# Specification name

`dnsping` (DNS ping)

# Test preconditions

* An internet connection

# Expected impact

The possibility of pinging a DNS server using UDP.

# Expected inputs

* A URL like `udp://<host>:<port>`.

* An optional list of domains to use (`-O Domains="value ..."` with `miniooni`).

# Test description

The experiment will send A/AAAA queries for the given domains to the given
list of servers. Requests will be emitted every second for ten seconds.

# Expected output

## Parent data format

* `df-002-dnst`

## Semantics

```JSON
{
    "pings": []
}

```

where:

- `pings` contains a list of `SinglePing` instances which look like:

```JSON
{
  "query": {}
}
```

where:

- `query` follows the `df-002-dnst` data format

Before 2022-07-08, `query` pointed to a *list* of `df-002-dnst`
data. We changed this because the nettest is still experimental and we want to
clearly indicate that a single DNS Lookup per `SinglePing` is possible.
## Possible conclusions

This experiment is an exploratory tool. There is no immediate conclusion
from its results but it is useful to perform censorship research.

## Example output sample

```JSON
{
  "annotations": {
    "architecture": "amd64",
    "engine_name": "ooniprobe-engine",
    "engine_version": "3.16.0-alpha",
    "platform": "linux"
  },
  "data_format_version": "0.2.0",
  "input": "udp://8.8.8.8:53",
  "measurement_start_time": "2022-07-08 16:12:11",
  "options": [
    "Domains=example.com"
  ],
  "probe_asn": "AS24560",
  "probe_cc": "IN",
  "probe_ip": "127.0.0.1",
  "probe_network_name": "Bharti Airtel Limited",
  "report_id": "",
  "resolver_asn": "AS13335",
  "resolver_ip": "162.158.45.17",
  "resolver_network_name": "Cloudflare, Inc.",
  "software_name": "miniooni",
  "software_version": "3.16.0-alpha",
  "test_keys": {
    "pings": [
      {
        "query": {
          "answers": [
            {
              "asn": 15133,
              "as_org_name": "Edgecast Inc.",
              "answer_type": "A",
              "ipv4": "93.184.216.34",
              "ttl": null
            }
          ],
          "engine": "udp",
          "failure": null,
          "hostname": "example.com",
          "query_type": "A",
          "resolver_hostname": null,
          "resolver_port": null,
          "resolver_address": "8.8.8.8:53",
          "t": 0.012180722
        }
      },
      {
        "query": {
          "answers": [
            {
              "asn": 15133,
              "as_org_name": "Edgecast Inc.",
              "answer_type": "AAAA",
              "ipv6": "2606:2800:220:1:248:1893:25c8:1946",
              "ttl": null
            }
          ],
          "engine": "udp",
          "failure": null,
          "hostname": "example.com",
          "query_type": "AAAA",
          "resolver_hostname": null,
          "resolver_port": null,
          "resolver_address": "8.8.8.8:53",
          "t": 0.00633031
        }
      },
      {
        "query": {
          "answers": [
            {
              "asn": 15133,
              "as_org_name": "Edgecast Inc.",
              "answer_type": "A",
              "ipv4": "93.184.216.34",
              "ttl": null
            }
          ],
          "engine": "udp",
          "failure": null,
          "hostname": "example.com",
          "query_type": "A",
          "resolver_hostname": null,
          "resolver_port": null,
          "resolver_address": "8.8.8.8:53",
          "t": 1.010636651
        }
      },
      {
        "query": {
          "answers": [
            {
              "asn": 15133,
              "as_org_name": "Edgecast Inc.",
              "answer_type": "AAAA",
              "ipv6": "2606:2800:220:1:248:1893:25c8:1946",
              "ttl": null
            }
          ],
          "engine": "udp",
          "failure": null,
          "hostname": "example.com",
          "query_type": "AAAA",
          "resolver_hostname": null,
          "resolver_port": null,
          "resolver_address": "8.8.8.8:53",
          "t": 1.010546639
        }
      },
      {
        "query": {
          "answers": [
            {
              "asn": 15133,
              "as_org_name": "Edgecast Inc.",
              "answer_type": "A",
              "ipv4": "93.184.216.34",
              "ttl": null
            }
          ],
          "engine": "udp",
          "failure": null,
          "hostname": "example.com",
          "query_type": "A",
          "resolver_hostname": null,
          "resolver_port": null,
          "resolver_address": "8.8.8.8:53",
          "t": 2.014877748
        }
      },
      {
        "query": {
          "answers": [
            {
              "asn": 15133,
              "as_org_name": "Edgecast Inc.",
              "answer_type": "AAAA",
              "ipv6": "2606:2800:220:1:248:1893:25c8:1946",
              "ttl": null
            }
          ],
          "engine": "udp",
          "failure": null,
          "hostname": "example.com",
          "query_type": "AAAA",
          "resolver_hostname": null,
          "resolver_port": null,
          "resolver_address": "8.8.8.8:53",
          "t": 2.015116933
        }
      },
      {
        "query": {
          "answers": [
            {
              "asn": 15133,
              "as_org_name": "Edgecast Inc.",
              "answer_type": "A",
              "ipv4": "93.184.216.34",
              "ttl": null
            }
          ],
          "engine": "udp",
          "failure": null,
          "hostname": "example.com",
          "query_type": "A",
          "resolver_hostname": null,
          "resolver_port": null,
          "resolver_address": "8.8.8.8:53",
          "t": 3.007311328
        }
      },
      {
        "query": {
          "answers": [
            {
              "asn": 15133,
              "as_org_name": "Edgecast Inc.",
              "answer_type": "AAAA",
              "ipv6": "2606:2800:220:1:248:1893:25c8:1946",
              "ttl": null
            }
          ],
          "engine": "udp",
          "failure": null,
          "hostname": "example.com",
          "query_type": "AAAA",
          "resolver_hostname": null,
          "resolver_port": null,
          "resolver_address": "8.8.8.8:53",
          "t": 3.009005329
        }
      },
      {
        "query": {
          "answers": [
            {
              "asn": 15133,
              "as_org_name": "Edgecast Inc.",
              "answer_type": "A",
              "ipv4": "93.184.216.34",
              "ttl": null
            }
          ],
          "engine": "udp",
          "failure": null,
          "hostname": "example.com",
          "query_type": "A",
          "resolver_hostname": null,
          "resolver_port": null,
          "resolver_address": "8.8.8.8:53",
          "t": 4.009202965
        }
      },
      {
        "query": {
          "answers": [
            {
              "asn": 15133,
              "as_org_name": "Edgecast Inc.",
              "answer_type": "AAAA",
              "ipv6": "2606:2800:220:1:248:1893:25c8:1946",
              "ttl": null
            }
          ],
          "engine": "udp",
          "failure": null,
          "hostname": "example.com",
          "query_type": "AAAA",
          "resolver_hostname": null,
          "resolver_port": null,
          "resolver_address": "8.8.8.8:53",
          "t": 4.008773356
        }
      },
      {
        "query": {
          "answers": [
            {
              "asn": 15133,
              "as_org_name": "Edgecast Inc.",
              "answer_type": "A",
              "ipv4": "93.184.216.34",
              "ttl": null
            }
          ],
          "engine": "udp",
          "failure": null,
          "hostname": "example.com",
          "query_type": "A",
          "resolver_hostname": null,
          "resolver_port": null,
          "resolver_address": "8.8.8.8:53",
          "t": 5.013456252
        }
      },
      {
        "query": {
          "answers": [
            {
              "asn": 15133,
              "as_org_name": "Edgecast Inc.",
              "answer_type": "AAAA",
              "ipv6": "2606:2800:220:1:248:1893:25c8:1946",
              "ttl": null
            }
          ],
          "engine": "udp",
          "failure": null,
          "hostname": "example.com",
          "query_type": "AAAA",
          "resolver_hostname": null,
          "resolver_port": null,
          "resolver_address": "8.8.8.8:53",
          "t": 5.013968032
        }
      },
      {
        "query": {
          "answers": [
            {
              "asn": 15133,
              "as_org_name": "Edgecast Inc.",
              "answer_type": "A",
              "ipv4": "93.184.216.34",
              "ttl": null
            }
          ],
          "engine": "udp",
          "failure": null,
          "hostname": "example.com",
          "query_type": "A",
          "resolver_hostname": null,
          "resolver_port": null,
          "resolver_address": "8.8.8.8:53",
          "t": 6.012388294
        }
      },
      {
        "query": {
          "answers": [
            {
              "asn": 15133,
              "as_org_name": "Edgecast Inc.",
              "answer_type": "AAAA",
              "ipv6": "2606:2800:220:1:248:1893:25c8:1946",
              "ttl": null
            }
          ],
          "engine": "udp",
          "failure": null,
          "hostname": "example.com",
          "query_type": "AAAA",
          "resolver_hostname": null,
          "resolver_port": null,
          "resolver_address": "8.8.8.8:53",
          "t": 6.012190274
        }
      },
      {
        "query": {
          "answers": [
            {
              "asn": 15133,
              "as_org_name": "Edgecast Inc.",
              "answer_type": "A",
              "ipv4": "93.184.216.34",
              "ttl": null
            }
          ],
          "engine": "udp",
          "failure": null,
          "hostname": "example.com",
          "query_type": "A",
          "resolver_hostname": null,
          "resolver_port": null,
          "resolver_address": "8.8.8.8:53",
          "t": 7.011494316
        }
      },
      {
        "query": {
          "answers": [
            {
              "asn": 15133,
              "as_org_name": "Edgecast Inc.",
              "answer_type": "AAAA",
              "ipv6": "2606:2800:220:1:248:1893:25c8:1946",
              "ttl": null
            }
          ],
          "engine": "udp",
          "failure": null,
          "hostname": "example.com",
          "query_type": "AAAA",
          "resolver_hostname": null,
          "resolver_port": null,
          "resolver_address": "8.8.8.8:53",
          "t": 7.012493186
        }
      },
      {
        "query": {
          "answers": [
            {
              "asn": 15133,
              "as_org_name": "Edgecast Inc.",
              "answer_type": "A",
              "ipv4": "93.184.216.34",
              "ttl": null
            }
          ],
          "engine": "udp",
          "failure": null,
          "hostname": "example.com",
          "query_type": "A",
          "resolver_hostname": null,
          "resolver_port": null,
          "resolver_address": "8.8.8.8:53",
          "t": 8.017688232
        }
      },
      {
        "query": {
          "answers": [
            {
              "asn": 15133,
              "as_org_name": "Edgecast Inc.",
              "answer_type": "AAAA",
              "ipv6": "2606:2800:220:1:248:1893:25c8:1946",
              "ttl": null
            }
          ],
          "engine": "udp",
          "failure": null,
          "hostname": "example.com",
          "query_type": "AAAA",
          "resolver_hostname": null,
          "resolver_port": null,
          "resolver_address": "8.8.8.8:53",
          "t": 8.018410881
        }
      },
      {
        "query": {
          "answers": [
            {
              "asn": 15133,
              "as_org_name": "Edgecast Inc.",
              "answer_type": "A",
              "ipv4": "93.184.216.34",
              "ttl": null
            }
          ],
          "engine": "udp",
          "failure": null,
          "hostname": "example.com",
          "query_type": "A",
          "resolver_hostname": null,
          "resolver_port": null,
          "resolver_address": "8.8.8.8:53",
          "t": 9.014945119
        }
      },
      {
        "query": {
          "answers": [
            {
              "asn": 15133,
              "as_org_name": "Edgecast Inc.",
              "answer_type": "AAAA",
              "ipv6": "2606:2800:220:1:248:1893:25c8:1946",
              "ttl": null
            }
          ],
          "engine": "udp",
          "failure": null,
          "hostname": "example.com",
          "query_type": "AAAA",
          "resolver_hostname": null,
          "resolver_port": null,
          "resolver_address": "8.8.8.8:53",
          "t": 9.01539972
        }
      }
    ]
  },
  "test_name": "dnsping",
  "test_runtime": 10.00088401,
  "test_start_time": "2022-07-08 16:12:01",
  "test_version": "0.1.0"
}

```

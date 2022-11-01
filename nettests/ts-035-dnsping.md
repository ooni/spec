# Specification version number

2022-08-25

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
  "query": {},
  "delayed_responses": []
}
```

where:

- `query` follows the `df-002-dnst` data format

- `delayed_responses` contains one or more delayed DNS responses of `df-002-dnst` data format

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
  "measurement_start_time": "2022-08-25 06:10:04",
  "options": [
    "Domains=example.com"
  ],
  "probe_asn": "AS45609",
  "probe_cc": "IN",
  "probe_ip": "127.0.0.1",
  "probe_network_name": "Bharti Airtel Limited",
  "report_id": "",
  "resolver_asn": "AS9498",
  "resolver_ip": "182.78.212.206",
  "resolver_network_name": "Bharti Airtel Limited",
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
          "raw_response": "u9qBgAABAAEAAAAAB2V4YW1wbGUDY29tAAABAAHADAABAAEAAFBmAARduNgi",
          "resolver_hostname": null,
          "resolver_port": null,
          "resolver_address": "8.8.8.8:53",
          "t0": 0.000359366,
          "t": 0.073830927
        },
        "delayed_response": []
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
          "raw_response": "mbKBgAABAAEAAAAAB2V4YW1wbGUDY29tAAAcAAHADAAcAAEAAFMUABAmBigAAiAAAQJIGJMlyBlG",
          "resolver_hostname": null,
          "resolver_port": null,
          "resolver_address": "8.8.8.8:53",
          "t0": 0.000308478,
          "t": 0.073982625
        },
        "delayed_response": []
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
          "raw_response": "XIiBgAABAAEAAAAAB2V4YW1wbGUDY29tAAABAAHADAABAAEAAE1zAARduNgi",
          "resolver_hostname": null,
          "resolver_port": null,
          "resolver_address": "8.8.8.8:53",
          "t0": 1.000989621,
          "t": 1.254724705
        },
        "delayed_response": []
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
          "raw_response": "pZ6BgAABAAEAAAAAB2V4YW1wbGUDY29tAAAcAAHADAAcAAEAAFFOABAmBigAAiAAAQJIGJMlyBlG",
          "resolver_hostname": null,
          "resolver_port": null,
          "resolver_address": "8.8.8.8:53",
          "t0": 1.000915811,
          "t": 1.255178063
        },
        "delayed_response": []
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
          "raw_response": "m+KBgAABAAEAAAAAB2V4YW1wbGUDY29tAAAcAAHADAAcAAEAAFOEABAmBigAAiAAAQJIGJMlyBlG",
          "resolver_hostname": null,
          "resolver_port": null,
          "resolver_address": "8.8.8.8:53",
          "t0": 2.00049805,
          "t": 2.040689907
        },
        "delayed_response": []
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
          "raw_response": "YDqBgAABAAEAAAAAB2V4YW1wbGUDY29tAAABAAHADAABAAEAAE1yAARduNgi",
          "resolver_hostname": null,
          "resolver_port": null,
          "resolver_address": "8.8.8.8:53",
          "t0": 2.000556926,
          "t": 2.04973474
        },
        "delayed_response": []
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
          "raw_response": "/12BgAABAAEAAAAAB2V4YW1wbGUDY29tAAABAAHADAABAAEAAFBEAARduNgi",
          "resolver_hostname": null,
          "resolver_port": null,
          "resolver_address": "8.8.8.8:53",
          "t0": 3.000751795,
          "t": 3.052840121
        },
        "delayed_response": []
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
          "raw_response": "P3aBgAABAAEAAAAAB2V4YW1wbGUDY29tAAAcAAHADAAcAAEAAFK/ABAmBigAAiAAAQJIGJMlyBlG",
          "resolver_hostname": null,
          "resolver_port": null,
          "resolver_address": "8.8.8.8:53",
          "t0": 3.000673174,
          "t": 3.06180341
        },
        "delayed_response": []
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
          "raw_response": "xxWBgAABAAEAAAAAB2V4YW1wbGUDY29tAAABAAHADAABAAEAAEoRAARduNgi",
          "resolver_hostname": null,
          "resolver_port": null,
          "resolver_address": "8.8.8.8:53",
          "t0": 4.001226811,
          "t": 4.211905927
        },
        "delayed_response": []
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
          "raw_response": "Eo+BgAABAAEAAAAAB2V4YW1wbGUDY29tAAAcAAHADAAcAAEAAFOCABAmBigAAiAAAQJIGJMlyBlG",
          "resolver_hostname": null,
          "resolver_port": null,
          "resolver_address": "8.8.8.8:53",
          "t0": 4.001151084,
          "t": 4.21213355
        },
        "delayed_response": []
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
          "raw_response": "xMuBgAABAAEAAAAAB2V4YW1wbGUDY29tAAAcAAHADAAcAAEAAFK6ABAmBigAAiAAAQJIGJMlyBlG",
          "resolver_hostname": null,
          "resolver_port": null,
          "resolver_address": "8.8.8.8:53",
          "t0": 8.000424039,
          "t": 8.038948747
        },
        "delayed_response": []
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
          "raw_response": "hQaBgAABAAEAAAAAB2V4YW1wbGUDY29tAAABAAHADAABAAEAAFBeAARduNgi",
          "resolver_hostname": null,
          "resolver_port": null,
          "resolver_address": "8.8.8.8:53",
          "t0": 8.000453325,
          "t": 8.052861375
        },
        "delayed_response": []
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
          "raw_response": "JcGBgAABAAEAAAAAB2V4YW1wbGUDY29tAAAcAAHADAAcAAEAAFKFABAmBigAAiAAAQJIGJMlyBlG",
          "resolver_hostname": null,
          "resolver_port": null,
          "resolver_address": "8.8.8.8:53",
          "t0": 9.0005869,
          "t": 9.039456662
        },
        "delayed_response": []
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
          "raw_response": "zuGBgAABAAEAAAAAB2V4YW1wbGUDY29tAAABAAHADAABAAEAAE+VAARduNgi",
          "resolver_hostname": null,
          "resolver_port": null,
          "resolver_address": "8.8.8.8:53",
          "t0": 9.000657823,
          "t": 9.053067344
        },
        "delayed_response": []
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
          "raw_response": "f2qBgAABAAEAAAAAB2V4YW1wbGUDY29tAAAcAAHADAAcAAEAAFOBABAmBigAAiAAAQJIGJMlyBlG",
          "resolver_hostname": null,
          "resolver_port": null,
          "resolver_address": "8.8.8.8:53",
          "t0": 5.001284311,
          "t": 5.85040832
        },
        "delayed_response": []
      },
      {
        "query": {
          "answers": null,
          "engine": "udp",
          "failure": "generic_timeout_error",
          "hostname": "example.com",
          "query_type": "A",
          "resolver_hostname": null,
          "resolver_port": null,
          "resolver_address": "8.8.8.8:53",
          "t0": 5.001301915,
          "t": 10.001762849
        },
        "delayed_response": []
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
          "raw_response": "u86BgAABAAEAAAAAB2V4YW1wbGUDY29tAAAcAAHADAAcAAEAAE26ABAmBigAAiAAAQJIGJMlyBlG",
          "resolver_hostname": null,
          "resolver_port": null,
          "resolver_address": "8.8.8.8:53",
          "t0": 6.001054485,
          "t": 6.772006242
        },
        "delayed_response": []
      },
      {
        "query": {
          "answers": null,
          "engine": "udp",
          "failure": "generic_timeout_error",
          "hostname": "example.com",
          "query_type": "A",
          "resolver_hostname": null,
          "resolver_port": null,
          "resolver_address": "8.8.8.8:53",
          "t0": 6.001172389,
          "t": 11.002013029
        },
        "delayed_response": []
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
          "raw_response": "CUyBgAABAAEAAAAAB2V4YW1wbGUDY29tAAAcAAHADAAcAAEAAFK6ABAmBigAAiAAAQJIGJMlyBlG",
          "resolver_hostname": null,
          "resolver_port": null,
          "resolver_address": "8.8.8.8:53",
          "t0": 7.000592866,
          "t": 7.897996214
        },
        "delayed_response": []
      },
      {
        "query": {
          "answers": null,
          "engine": "udp",
          "failure": "generic_timeout_error",
          "hostname": "example.com",
          "query_type": "A",
          "resolver_hostname": null,
          "resolver_port": null,
          "resolver_address": "8.8.8.8:53",
          "t0": 7.000671678,
          "t": 12.0014597
        },
        "delayed_response": []
      }
    ]
  },
  "test_name": "dnsping",
  "test_runtime": 12.00158091,
  "test_start_time": "2022-08-25 06:09:52",
  "test_version": "0.3.0"
}
```

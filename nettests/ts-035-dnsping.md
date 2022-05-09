# Specification version number

2022-05-09

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

- `pings` contains a list of `df-002-dnst` results.

## Possible conclusions

This experiment is an exploratory tool. There is no immediate conclusion
from its results but it is useful to perform censorship research.

## Example output sample

```JSON
{
  "annotations": {
    "architecture": "arm64",
    "engine_name": "ooniprobe-engine",
    "engine_version": "3.15.0-alpha",
    "platform": "macos"
  },
  "data_format_version": "0.2.0",
  "input": "udp://8.8.8.8:53",
  "measurement_start_time": "2022-05-09 12:50:45",
  "options": [
    "Domains=example.com"
  ],
  "probe_asn": "AS30722",
  "probe_cc": "IT",
  "probe_ip": "127.0.0.1",
  "probe_network_name": "Vodafone Italia S.p.A.",
  "report_id": "",
  "resolver_asn": "AS30722",
  "resolver_ip": "91.80.36.92",
  "resolver_network_name": "Vodafone Italia S.p.A.",
  "software_name": "miniooni",
  "software_version": "3.15.0-alpha",
  "test_keys": {
    "pings": [
      {
        "queries": [
          {
            "answers": [
              {
                "answer_type": "A",
                "ipv4": "93.184.216.34"
              }
            ],
            "engine": "udp",
            "failure": null,
            "hostname": "example.com",
            "query_type": "A",
            "resolver_address": "8.8.8.8:53",
            "t": 0.034158834,
            "started": 0.000227792
          }
        ]
      },
      {
        "queries": [
          {
            "answers": [
              {
                "answer_type": "AAAA",
                "ivp6": "2606:2800:220:1:248:1893:25c8:1946"
              }
            ],
            "engine": "udp",
            "failure": null,
            "hostname": "example.com",
            "query_type": "AAAA",
            "resolver_address": "8.8.8.8:53",
            "t": 0.034158834,
            "started": 0.000227792
          }
        ]
      },
      {
        "queries": [
          {
            "answers": [
              {
                "answer_type": "A",
                "ipv4": "93.184.216.34"
              }
            ],
            "engine": "udp",
            "failure": null,
            "hostname": "example.com",
            "query_type": "A",
            "resolver_address": "8.8.8.8:53",
            "t": 1.010683667,
            "started": 1.001460167
          }
        ]
      },
      {
        "queries": [
          {
            "answers": [
              {
                "answer_type": "AAAA",
                "ivp6": "2606:2800:220:1:248:1893:25c8:1946"
              }
            ],
            "engine": "udp",
            "failure": null,
            "hostname": "example.com",
            "query_type": "AAAA",
            "resolver_address": "8.8.8.8:53",
            "t": 1.010683667,
            "started": 1.001460167
          }
        ]
      },
      {
        "queries": [
          {
            "answers": [
              {
                "answer_type": "A",
                "ipv4": "93.184.216.34"
              }
            ],
            "engine": "udp",
            "failure": null,
            "hostname": "example.com",
            "query_type": "A",
            "resolver_address": "8.8.8.8:53",
            "t": 2.01174975,
            "started": 2.001313
          }
        ]
      },
      {
        "queries": [
          {
            "answers": [
              {
                "answer_type": "AAAA",
                "ivp6": "2606:2800:220:1:248:1893:25c8:1946"
              }
            ],
            "engine": "udp",
            "failure": null,
            "hostname": "example.com",
            "query_type": "AAAA",
            "resolver_address": "8.8.8.8:53",
            "t": 2.01174975,
            "started": 2.001313
          }
        ]
      },
      {
        "queries": [
          {
            "answers": [
              {
                "answer_type": "A",
                "ipv4": "93.184.216.34"
              }
            ],
            "engine": "udp",
            "failure": null,
            "hostname": "example.com",
            "query_type": "A",
            "resolver_address": "8.8.8.8:53",
            "t": 3.010953625,
            "started": 3.001348417
          }
        ]
      },
      {
        "queries": [
          {
            "answers": [
              {
                "answer_type": "AAAA",
                "ivp6": "2606:2800:220:1:248:1893:25c8:1946"
              }
            ],
            "engine": "udp",
            "failure": null,
            "hostname": "example.com",
            "query_type": "AAAA",
            "resolver_address": "8.8.8.8:53",
            "t": 3.010953625,
            "started": 3.001348417
          }
        ]
      },
      {
        "queries": [
          {
            "answers": [
              {
                "answer_type": "A",
                "ipv4": "93.184.216.34"
              }
            ],
            "engine": "udp",
            "failure": null,
            "hostname": "example.com",
            "query_type": "A",
            "resolver_address": "8.8.8.8:53",
            "t": 4.010690875,
            "started": 4.001394959
          }
        ]
      },
      {
        "queries": [
          {
            "answers": [
              {
                "answer_type": "AAAA",
                "ivp6": "2606:2800:220:1:248:1893:25c8:1946"
              }
            ],
            "engine": "udp",
            "failure": null,
            "hostname": "example.com",
            "query_type": "AAAA",
            "resolver_address": "8.8.8.8:53",
            "t": 4.010690875,
            "started": 4.001394959
          }
        ]
      },
      {
        "queries": [
          {
            "answers": [
              {
                "answer_type": "A",
                "ipv4": "93.184.216.34"
              }
            ],
            "engine": "udp",
            "failure": null,
            "hostname": "example.com",
            "query_type": "A",
            "resolver_address": "8.8.8.8:53",
            "t": 5.017204209,
            "started": 5.001349625
          }
        ]
      },
      {
        "queries": [
          {
            "answers": [
              {
                "answer_type": "AAAA",
                "ivp6": "2606:2800:220:1:248:1893:25c8:1946"
              }
            ],
            "engine": "udp",
            "failure": null,
            "hostname": "example.com",
            "query_type": "AAAA",
            "resolver_address": "8.8.8.8:53",
            "t": 5.017204209,
            "started": 5.001349625
          }
        ]
      },
      {
        "queries": [
          {
            "answers": [
              {
                "answer_type": "A",
                "ipv4": "93.184.216.34"
              }
            ],
            "engine": "udp",
            "failure": null,
            "hostname": "example.com",
            "query_type": "A",
            "resolver_address": "8.8.8.8:53",
            "t": 6.019601584,
            "started": 6.00146175
          }
        ]
      },
      {
        "queries": [
          {
            "answers": [
              {
                "answer_type": "AAAA",
                "ivp6": "2606:2800:220:1:248:1893:25c8:1946"
              }
            ],
            "engine": "udp",
            "failure": null,
            "hostname": "example.com",
            "query_type": "AAAA",
            "resolver_address": "8.8.8.8:53",
            "t": 6.019601584,
            "started": 6.00146175
          }
        ]
      },
      {
        "queries": [
          {
            "answers": [
              {
                "answer_type": "A",
                "ipv4": "93.184.216.34"
              }
            ],
            "engine": "udp",
            "failure": null,
            "hostname": "example.com",
            "query_type": "A",
            "resolver_address": "8.8.8.8:53",
            "t": 7.010071125,
            "started": 7.000904667
          }
        ]
      },
      {
        "queries": [
          {
            "answers": [
              {
                "answer_type": "AAAA",
                "ivp6": "2606:2800:220:1:248:1893:25c8:1946"
              }
            ],
            "engine": "udp",
            "failure": null,
            "hostname": "example.com",
            "query_type": "AAAA",
            "resolver_address": "8.8.8.8:53",
            "t": 7.010071125,
            "started": 7.000904667
          }
        ]
      },
      {
        "queries": [
          {
            "answers": [
              {
                "answer_type": "A",
                "ipv4": "93.184.216.34"
              }
            ],
            "engine": "udp",
            "failure": null,
            "hostname": "example.com",
            "query_type": "A",
            "resolver_address": "8.8.8.8:53",
            "t": 8.019252959,
            "started": 8.001470709
          }
        ]
      },
      {
        "queries": [
          {
            "answers": [
              {
                "answer_type": "AAAA",
                "ivp6": "2606:2800:220:1:248:1893:25c8:1946"
              }
            ],
            "engine": "udp",
            "failure": null,
            "hostname": "example.com",
            "query_type": "AAAA",
            "resolver_address": "8.8.8.8:53",
            "t": 8.019252959,
            "started": 8.001470709
          }
        ]
      },
      {
        "queries": [
          {
            "answers": [
              {
                "answer_type": "A",
                "ipv4": "93.184.216.34"
              }
            ],
            "engine": "udp",
            "failure": null,
            "hostname": "example.com",
            "query_type": "A",
            "resolver_address": "8.8.8.8:53",
            "t": 9.011677334,
            "started": 9.001221084
          }
        ]
      },
      {
        "queries": [
          {
            "answers": [
              {
                "answer_type": "AAAA",
                "ivp6": "2606:2800:220:1:248:1893:25c8:1946"
              }
            ],
            "engine": "udp",
            "failure": null,
            "hostname": "example.com",
            "query_type": "AAAA",
            "resolver_address": "8.8.8.8:53",
            "t": 9.011677334,
            "started": 9.001221084
          }
        ]
      }
    ]
  },
  "test_name": "dnsping",
  "test_runtime": 9.011842209,
  "test_start_time": "2022-05-09 12:50:36",
  "test_version": "0.1.0"
}
```

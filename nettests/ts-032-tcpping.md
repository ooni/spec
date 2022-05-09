# Specification version number

2022-05-09

* _status_: experimental

# Specification name

`tcpping` (TCP ping)

# Test preconditions

* An internet connection

# Expected impact

The possibility of pinging a TCP endpoint.

# Expected inputs

A URL like `tcpconnect://<host>:<port>`.

# Test description

The experiment will attempt to connect to the given TCP endpoint
every second for ten times and return the results.

# Expected output

## Parent data format

* `df-005-tcpconnect`

## Semantics

```JSON
{
    "pings": []
}
```

where:

- `pings` contains a list of `df-005-tcpconnect` results.

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
  "input": "tcpconnect://8.8.8.8:443",
  "measurement_start_time": "2022-05-09 07:00:09",
  "probe_asn": "AS30722",
  "probe_cc": "IT",
  "probe_ip": "127.0.0.1",
  "probe_network_name": "Vodafone Italia S.p.A.",
  "report_id": "",
  "resolver_asn": "AS30722",
  "resolver_ip": "91.80.36.88",
  "resolver_network_name": "Vodafone Italia S.p.A.",
  "software_name": "miniooni",
  "software_version": "3.15.0-alpha",
  "test_keys": {
    "pings": [
      {
        "tcp_connect": [
          {
            "ip": "8.8.8.8",
            "port": 443,
            "t": 0.0157685,
            "status": {
              "blocked": false,
              "failure": null,
              "success": true
            },
            "started": 0.00027075
          }
        ]
      },
      {
        "tcp_connect": [
          {
            "ip": "8.8.8.8",
            "port": 443,
            "t": 1.016991917,
            "status": {
              "blocked": false,
              "failure": null,
              "success": true
            },
            "started": 1.001177334
          }
        ]
      },
      {
        "tcp_connect": [
          {
            "ip": "8.8.8.8",
            "port": 443,
            "t": 2.026658709,
            "status": {
              "blocked": false,
              "failure": null,
              "success": true
            },
            "started": 2.001280459
          }
        ]
      },
      {
        "tcp_connect": [
          {
            "ip": "8.8.8.8",
            "port": 443,
            "t": 3.025365,
            "status": {
              "blocked": false,
              "failure": null,
              "success": true
            },
            "started": 3.001233959
          }
        ]
      },
      {
        "tcp_connect": [
          {
            "ip": "8.8.8.8",
            "port": 443,
            "t": 4.019205709,
            "status": {
              "blocked": false,
              "failure": null,
              "success": true
            },
            "started": 4.001288084
          }
        ]
      },
      {
        "tcp_connect": [
          {
            "ip": "8.8.8.8",
            "port": 443,
            "t": 5.027602292,
            "status": {
              "blocked": false,
              "failure": null,
              "success": true
            },
            "started": 5.000583125
          }
        ]
      },
      {
        "tcp_connect": [
          {
            "ip": "8.8.8.8",
            "port": 443,
            "t": 6.082865667,
            "status": {
              "blocked": false,
              "failure": null,
              "success": true
            },
            "started": 6.001351792
          }
        ]
      },
      {
        "tcp_connect": [
          {
            "ip": "8.8.8.8",
            "port": 443,
            "t": 7.255470792,
            "status": {
              "blocked": false,
              "failure": null,
              "success": true
            },
            "started": 7.001372834
          }
        ]
      },
      {
        "tcp_connect": [
          {
            "ip": "8.8.8.8",
            "port": 443,
            "t": 8.13132125,
            "status": {
              "blocked": false,
              "failure": null,
              "success": true
            },
            "started": 8.001229584
          }
        ]
      },
      {
        "tcp_connect": [
          {
            "ip": "8.8.8.8",
            "port": 443,
            "t": 9.021270834,
            "status": {
              "blocked": false,
              "failure": null,
              "success": true
            },
            "started": 9.001323625
          }
        ]
      }
    ]
  },
  "test_name": "tcpping",
  "test_runtime": 9.021483791,
  "test_start_time": "2022-05-09 07:00:00",
  "test_version": "0.1.0"
}
```

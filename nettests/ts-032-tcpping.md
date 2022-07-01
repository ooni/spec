# Specification version number

2022-06-22

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

- `pings` is a `SinglePing` instance, which looks like:

```JSON
{
	"tcp_connect": {}
}
```

where:

- `tcp_connect` follows the `df-005-tcpconnect` data format.

Before 2022-06-22, `tcp_connect` pointed to a *list* of `df-005-tcpconnect`
data. We changed this because the nettest is still experimental and we want to
clearly indicate that a single TCP connect per `SinglePing` is possible.

## Possible conclusions

This experiment is an exploratory tool. There is no immediate conclusion
from its results but it is useful to perform censorship research.

## Example output sample

```JSON
{
  "annotations": {
    "architecture": "arm64",
    "engine_name": "ooniprobe-engine",
    "engine_version": "3.16.0-alpha",
    "platform": "macos"
  },
  "data_format_version": "0.2.0",
  "input": "tcpconnect://8.8.8.8:443",
  "measurement_start_time": "2022-06-22 13:32:07",
  "probe_asn": "AS30722",
  "probe_cc": "IT",
  "probe_ip": "127.0.0.1",
  "probe_network_name": "Vodafone Italia S.p.A.",
  "report_id": "20220622T133208Z_tcpping_IT_30722_n1_tWfDobdbZfWsdwHG",
  "resolver_asn": "AS30722",
  "resolver_ip": "91.80.36.88",
  "resolver_network_name": "Vodafone Italia S.p.A.",
  "software_name": "miniooni",
  "software_version": "3.16.0-alpha",
  "test_keys": {
    "pings": [
      {
        "tcp_connect": {
          "ip": "8.8.8.8",
          "port": 443,
          "status": {
            "failure": null,
            "success": true
          },
          "t": 0.020375
        }
      },
      {
        "tcp_connect": {
          "ip": "8.8.8.8",
          "port": 443,
          "status": {
            "failure": null,
            "success": true
          },
          "t": 1.028173
        }
      },
      {
        "tcp_connect": {
          "ip": "8.8.8.8",
          "port": 443,
          "status": {
            "failure": null,
            "success": true
          },
          "t": 2.02758
        }
      },
      {
        "tcp_connect": {
          "ip": "8.8.8.8",
          "port": 443,
          "status": {
            "failure": null,
            "success": true
          },
          "t": 3.026412
        }
      },
      {
        "tcp_connect": {
          "ip": "8.8.8.8",
          "port": 443,
          "status": {
            "failure": null,
            "success": true
          },
          "t": 4.028897
        }
      },
      {
        "tcp_connect": {
          "ip": "8.8.8.8",
          "port": 443,
          "status": {
            "failure": null,
            "success": true
          },
          "t": 5.026734
        }
      },
      {
        "tcp_connect": {
          "ip": "8.8.8.8",
          "port": 443,
          "status": {
            "failure": null,
            "success": true
          },
          "t": 6.020745
        }
      },
      {
        "tcp_connect": {
          "ip": "8.8.8.8",
          "port": 443,
          "status": {
            "failure": null,
            "success": true
          },
          "t": 7.019039
        }
      },
      {
        "tcp_connect": {
          "ip": "8.8.8.8",
          "port": 443,
          "status": {
            "failure": null,
            "success": true
          },
          "t": 8.027933
        }
      },
      {
        "tcp_connect": {
          "ip": "8.8.8.8",
          "port": 443,
          "status": {
            "failure": null,
            "success": true
          },
          "t": 9.025553
        }
      }
    ]
  },
  "test_name": "tcpping",
  "test_runtime": 9.025986292,
  "test_start_time": "2022-06-22 13:31:58",
  "test_version": "0.2.0"
}
```

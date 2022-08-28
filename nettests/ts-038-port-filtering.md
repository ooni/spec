# Specification version number

2022-08-28

*_status_: current

# Specification name

Port filtering

# Test preconditions

* An internet connection

# Expected impact

Ability to detect port-based filtering if present

# Expected inputs


# Test description

This test uses a predefined list of TCP ports and attempts to establish a connection to each 
port listening on a test-helper. 

The main task involved in the experiment is:

**TCP Connect**
    Attempt to establish a TCP session on the given ports in a pseudo-random order. The results 
    of the connecting end up in the "tcp_connect" key. (see df-005-tcpconnect.md).

# Expected output

## Parent data format

We will include data following these data formats:

* `df-005-tcpconnect`

## Semantics

```JSON
{
   "tcp_connect": [],
}
```

where:

- `tcp_connect` contains a list of `df-005-tcpconnect` instances

## Possible conclusions

* If a blocking mechanism censors a particular port.

## Example output sample

Response:

```JSON
{
  "annotations": {
    "architecture": "amd64",
    "engine_name": "ooniprobe-engine",
    "engine_version": "3.16.0-alpha",
    "platform": "linux"
  },
  "data_format_version": "0.2.0",
  "input": null,
  "measurement_start_time": "2022-08-28 16:50:42",
  "probe_asn": "AS24560",
  "probe_cc": "IN",
  "probe_ip": "127.0.0.1",
  "probe_network_name": "Bharti Airtel Limited",
  "report_id": "20220828T165042Z_portfiltering_IN_24560_n1_ovdo0VNE17ydZ2w7",
  "resolver_asn": "AS13335",
  "resolver_ip": "162.158.45.17",
  "resolver_network_name": "Cloudflare, Inc.",
  "software_name": "miniooni",
  "software_version": "3.16.0-alpha",
  "test_keys": {
    "tcp_connect": [
      {
        "ip": "127.0.0.1",
        "port": 23,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.000635687
      },
      {
        "ip": "127.0.0.1",
        "port": 587,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.101378718
      },
      {
        "ip": "127.0.0.1",
        "port": 443,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.20102326
      },
      {
        "ip": "127.0.0.1",
        "port": 445,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.300638003
      },
      {
        "ip": "127.0.0.1",
        "port": 80,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.401474309
      },
      {
        "ip": "127.0.0.1",
        "port": 993,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.501179546
      },
      {
        "ip": "127.0.0.1",
        "port": 22,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.600831884
      },
      {
        "ip": "127.0.0.1",
        "port": 143,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.701751593
      },
      {
        "ip": "127.0.0.1",
        "port": 25,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.801554046
      }
    ]
  },
  "test_name": "portfiltering",
  "test_runtime": 0.801730751,
  "test_start_time": "2022-08-28 16:50:41",
  "test_version": "0.1.0"
}
```
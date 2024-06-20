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

- `port` (`string`; optional): a target port to scan

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
   "tcp_connect": {},
}
```

where:

- `tcp_connect` contains a `df-005-tcpconnect` instance

## Possible conclusions

* If a blocking mechanism censors a particular port.

## Example output sample

Response:

```JSON
{
  "annotations": {
    "architecture": "amd64",
    "engine_name": "ooniprobe-engine",
    "engine_version": "3.17.0-alpha",
    "platform": "linux"
  },
  "data_format_version": "0.2.0",
  "input": "5000",
  "measurement_start_time": "2022-10-03 17:25:02",
  "probe_asn": "AS24560",
  "probe_cc": "IN",
  "probe_ip": "127.0.0.1",
  "probe_network_name": "Bharti Airtel Limited",
  "report_id": "",
  "resolver_asn": "AS13335",
  "resolver_ip": "162.158.45.57",
  "resolver_network_name": "Cloudflare, Inc.",
  "software_name": "miniooni",
  "software_version": "3.17.0-alpha",
  "test_keys": {
    "tcp_connect": {
      "ip": "127.0.0.1",
      "port": 5000,
      "status": {
        "failure": "connection_refused",
        "success": false
      },
      "t0": 0.000090346,
      "t": 0.000512644
    }
  },
  "test_name": "portfiltering",
  "test_runtime": 0.000567197,
  "test_start_time": "2022-10-03 17:25:02",
  "test_version": "0.1.0"
}
```
# Specification version number

0.2.0

# Specification name

TCP Connect Test

# Test preconditions

  * An internet connection

For reporting to the backend to work that it is possible for
the probe to establish a connection to the Tor network.

# Expected impact

Ability to determine if a TCP connection can be successfully established.

# Expected inputs

## Import document or import data format

A list of URLs to be tested for censorship.

## Data specification version number

## Semantics

The input document may contain an http or https URL, an IP:PORT, or a FQDN:PORT per line. e.g.

```
http://www.google.com
google.com:80
8.8.8.8:53
```

are all valid entries

# Test description

For every item given as input we perform a TCP connect. If
the connection is succesful, we record 'success' for the
test. If the connection fails, we record the reason for the
failure.

# Expected output

The key 'connection' is added to the report. One report entry is written per line in the input document.

## Required output data

The result of the connection attempt, 'success' or failure type.

## Semantics

'success' or a string indicating the reason for the failure.

## Possible conclusions

Ability to determine that a specific host:port is blocked.

## Example output sample

```
{
    "bucket_date": "2015-12-29",
    "data_format_version": "0.2.0",
    "id": "6305de45-ce5d-43b5-ba11-fd9019e5e90c",
    "input": "github.com:443\n",
    "input_hashes": [
        "586ded3d64bcb8672fedb475c8ea799331779b446e529b204a2088bedc91e3f0"
    ],
    "options": [
        "-f",
        "hosts.txt"
    ],
    "probe_asn": "AS13703",
    "probe_cc": "US",
    "probe_ip": "127.0.0.1",
    "report_filename": "2015-12-29/20151225T201931Z-US-AS13703-tcp_connect-IHsje0cnGs2uOpRgEmfnkpuZAa8ysrZgdf8YyImTUhtBTSZSoTeXle79RuchYuzi-0.1.0-probe.json",
    "report_id": "IHsje0cnGs2uOpRgEmfnkpuZAa8ysrZgdf8YyImTUhtBTSZSoTeXle79RuchYuzi",
    "software_name": "ooniprobe",
    "software_version": "1.3.1",
    "backend_version": "1.1.4",
    "probe_city": null,
    "test_helpers": {},
    "test_keys": {
        "connection": "success",
    },
    "test_name": "tcp_connect",
    "test_runtime": 0.0218939781,
    "test_start_time": "2015-12-25 20:19:31",
    "test_version": "0.1"
}
```

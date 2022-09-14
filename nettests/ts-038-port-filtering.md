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
    "engine_version": "3.17.0-alpha",
    "platform": "linux"
  },
  "data_format_version": "0.2.0",
  "input": null,
  "measurement_start_time": "2022-09-14 14:50:09",
  "probe_asn": "AS24560",
  "probe_cc": "IN",
  "probe_ip": "127.0.0.1",
  "probe_network_name": "Bharti Airtel Limited",
  "report_id": "20220914T145011Z_portfiltering_IN_24560_n1_3QtlUHDn3bpAX0TY",
  "resolver_asn": "AS13335",
  "resolver_ip": "162.158.45.57",
  "resolver_network_name": "Cloudflare, Inc.",
  "software_name": "miniooni",
  "software_version": "3.17.0-alpha",
  "test_keys": {
    "tcp_connect": [
      {
        "ip": "127.0.0.1",
        "port": 139,
        "status": {
          "failure": "connection_refused",
          "success": false
        },
        "t0": 0.000179591,
        "t": 0.000670947
      },
      {
        "ip": "127.0.0.1",
        "port": 68,
        "status": {
          "failure": "connection_refused",
          "success": false
        },
        "t0": 0.100981248,
        "t": 0.101230465,
        "transaction_id": 1
      },
      {
        "ip": "127.0.0.1",
        "port": 111,
        "status": {
          "failure": "connection_refused",
          "success": false
        },
        "t0": 0.200674328,
        "t": 0.20117694,
        "transaction_id": 2
      },
      {
        "ip": "127.0.0.1",
        "port": 1026,
        "status": {
          "failure": "connection_refused",
          "success": false
        },
        "t0": 0.300501712,
        "t": 0.300935915,
        "transaction_id": 3
      },
      {
        "ip": "127.0.0.1",
        "port": 2049,
        "status": {
          "failure": "connection_refused",
          "success": false
        },
        "t0": 0.40024919,
        "t": 0.400547578,
        "transaction_id": 4
      },
      {
        "ip": "127.0.0.1",
        "port": 445,
        "status": {
          "failure": "connection_refused",
          "success": false
        },
        "t0": 0.500851731,
        "t": 0.50125194,
        "transaction_id": 5
      },
      {
        "ip": "127.0.0.1",
        "port": 5060,
        "status": {
          "failure": "connection_refused",
          "success": false
        },
        "t0": 0.600513797,
        "t": 0.600929497,
        "transaction_id": 6
      },
      {
        "ip": "127.0.0.1",
        "port": 49152,
        "status": {
          "failure": "connection_refused",
          "success": false
        },
        "t0": 0.700130769,
        "t": 0.700407135,
        "transaction_id": 7
      },
      {
        "ip": "127.0.0.1",
        "port": 20031,
        "status": {
          "failure": "connection_refused",
          "success": false
        },
        "t0": 0.80060226,
        "t": 0.801000992,
        "transaction_id": 8
      },
      {
        "ip": "127.0.0.1",
        "port": 518,
        "status": {
          "failure": "connection_refused",
          "success": false
        },
        "t0": 0.900341038,
        "t": 0.900793321,
        "transaction_id": 9
      },
      {
        "ip": "127.0.0.1",
        "port": 49154,
        "status": {
          "failure": "connection_refused",
          "success": false
        },
        "t0": 1.001186803,
        "t": 1.001578026,
        "transaction_id": 10
      },
      {
        "ip": "127.0.0.1",
        "port": 1723,
        "status": {
          "failure": "connection_refused",
          "success": false
        },
        "t0": 1.10099987,
        "t": 1.101475905,
        "transaction_id": 11
      },
      {
        "ip": "127.0.0.1",
        "port": 21,
        "status": {
          "failure": "connection_refused",
          "success": false
        },
        "t0": 1.200737876,
        "t": 1.201247116,
        "transaction_id": 12
      },
      {
        "ip": "127.0.0.1",
        "port": 626,
        "status": {
          "failure": "connection_refused",
          "success": false
        },
        "t0": 1.30050252,
        "t": 1.300832021,
        "transaction_id": 13
      },
      {
        "ip": "127.0.0.1",
        "port": 69,
        "status": {
          "failure": "connection_refused",
          "success": false
        },
        "t0": 1.401201546,
        "t": 1.401707361,
        "transaction_id": 14
      },
      {
        "ip": "127.0.0.1",
        "port": 2222,
        "status": {
          "failure": "connection_refused",
          "success": false
        },
        "t0": 1.501118445,
        "t": 1.50155889,
        "transaction_id": 15
      },
      {
        "ip": "127.0.0.1",
        "port": 5353,
        "status": {
          "failure": "connection_refused",
          "success": false
        },
        "t0": 1.600904393,
        "t": 1.601344638,
        "transaction_id": 16
      },
      {
        "ip": "127.0.0.1",
        "port": 49153,
        "status": {
          "failure": "connection_refused",
          "success": false
        },
        "t0": 1.700609564,
        "t": 1.7010262,
        "transaction_id": 17
      },
      {
        "ip": "127.0.0.1",
        "port": 1646,
        "status": {
          "failure": "connection_refused",
          "success": false
        },
        "t0": 1.800215881,
        "t": 1.800690403,
        "transaction_id": 18
      },
      {
        "ip": "127.0.0.1",
        "port": 143,
        "status": {
          "failure": "connection_refused",
          "success": false
        },
        "t0": 1.901068795,
        "t": 1.901367617,
        "transaction_id": 19
      },
      {
        "ip": "127.0.0.1",
        "port": 3456,
        "status": {
          "failure": "connection_refused",
          "success": false
        },
        "t0": 2.00055435,
        "t": 2.000958965,
        "transaction_id": 20
      },
      {
        "ip": "127.0.0.1",
        "port": 500,
        "status": {
          "failure": "connection_refused",
          "success": false
        },
        "t0": 2.100177319,
        "t": 2.100435743,
        "transaction_id": 21
      },
      {
        "ip": "127.0.0.1",
        "port": 520,
        "status": {
          "failure": "connection_refused",
          "success": false
        },
        "t0": 2.200744032,
        "t": 2.201237384,
        "transaction_id": 22
      },
      {
        "ip": "127.0.0.1",
        "port": 137,
        "status": {
          "failure": "connection_refused",
          "success": false
        },
        "t0": 2.300498304,
        "t": 2.300784217,
        "transaction_id": 23
      },
      {
        "ip": "127.0.0.1",
        "port": 3283,
        "status": {
          "failure": "connection_refused",
          "success": false
        },
        "t0": 2.401154222,
        "t": 2.401481891,
        "transaction_id": 24
      },
      {
        "ip": "127.0.0.1",
        "port": 161,
        "status": {
          "failure": "connection_refused",
          "success": false
        },
        "t0": 2.500843759,
        "t": 2.501154345,
        "transaction_id": 25
      },
      {
        "ip": "127.0.0.1",
        "port": 1812,
        "status": {
          "failure": "connection_refused",
          "success": false
        },
        "t0": 2.60049185,
        "t": 2.60104354,
        "transaction_id": 26
      },
      {
        "ip": "127.0.0.1",
        "port": 3389,
        "status": {
          "failure": "connection_refused",
          "success": false
        },
        "t0": 2.700258731,
        "t": 2.7006857159999997,
        "transaction_id": 27
      },
      {
        "ip": "127.0.0.1",
        "port": 4500,
        "status": {
          "failure": "connection_refused",
          "success": false
        },
        "t0": 2.801019244,
        "t": 2.801508934,
        "transaction_id": 28
      },
      {
        "ip": "127.0.0.1",
        "port": 32768,
        "status": {
          "failure": "connection_refused",
          "success": false
        },
        "t0": 2.900845622,
        "t": 2.901327979,
        "transaction_id": 29
      },
      {
        "ip": "127.0.0.1",
        "port": 7,
        "status": {
          "failure": "connection_refused",
          "success": false
        },
        "t0": 3.000709124,
        "t": 3.001185051,
        "transaction_id": 30
      },
      {
        "ip": "127.0.0.1",
        "port": 5900,
        "status": {
          "failure": "connection_refused",
          "success": false
        },
        "t0": 3.100408941,
        "t": 3.100789423,
        "transaction_id": 31
      },
      {
        "ip": "127.0.0.1",
        "port": 8080,
        "status": {
          "failure": "connection_refused",
          "success": false
        },
        "t0": 3.201142274,
        "t": 3.201633742,
        "transaction_id": 32
      },
      {
        "ip": "127.0.0.1",
        "port": 135,
        "status": {
          "failure": "connection_refused",
          "success": false
        },
        "t0": 3.30093205,
        "t": 3.301318119,
        "transaction_id": 33
      },
      {
        "ip": "127.0.0.1",
        "port": 1645,
        "status": {
          "failure": "connection_refused",
          "success": false
        },
        "t0": 3.400493726,
        "t": 3.400810037,
        "transaction_id": 34
      },
      {
        "ip": "127.0.0.1",
        "port": 631,
        "status": {
          "failure": "connection_refused",
          "success": false
        },
        "t0": 3.501169955,
        "t": 3.501547801,
        "transaction_id": 35
      },
      {
        "ip": "127.0.0.1",
        "port": 995,
        "status": {
          "failure": "connection_refused",
          "success": false
        },
        "t0": 3.600856212,
        "t": 3.601256349,
        "transaction_id": 36
      },
      {
        "ip": "127.0.0.1",
        "port": 996,
        "status": {
          "failure": "connection_refused",
          "success": false
        },
        "t0": 3.7005328669999997,
        "t": 3.700882687,
        "transaction_id": 37
      },
      {
        "ip": "127.0.0.1",
        "port": 136,
        "status": {
          "failure": "connection_refused",
          "success": false
        },
        "t0": 3.800175706,
        "t": 3.800592848,
        "transaction_id": 38
      },
      {
        "ip": "127.0.0.1",
        "port": 123,
        "status": {
          "failure": "connection_refused",
          "success": false
        },
        "t0": 3.900913656,
        "t": 3.9013363549999998,
        "transaction_id": 39
      },
      {
        "ip": "127.0.0.1",
        "port": 80,
        "status": {
          "failure": "connection_refused",
          "success": false
        },
        "t0": 4.000762357,
        "t": 4.001119084,
        "transaction_id": 40
      },
      {
        "ip": "127.0.0.1",
        "port": 2048,
        "status": {
          "failure": "connection_refused",
          "success": false
        },
        "t0": 4.100470741,
        "t": 4.100813383,
        "transaction_id": 41
      },
      {
        "ip": "127.0.0.1",
        "port": 67,
        "status": {
          "failure": "connection_refused",
          "success": false
        },
        "t0": 4.201213439,
        "t": 4.201635579,
        "transaction_id": 42
      },
      {
        "ip": "127.0.0.1",
        "port": 1701,
        "status": {
          "failure": "connection_refused",
          "success": false
        },
        "t0": 4.301008599,
        "t": 4.301490217,
        "transaction_id": 43
      },
      {
        "ip": "127.0.0.1",
        "port": 998,
        "status": {
          "failure": "connection_refused",
          "success": false
        },
        "t0": 4.400725224,
        "t": 4.401137612,
        "transaction_id": 44
      },
      {
        "ip": "127.0.0.1",
        "port": 1900,
        "status": {
          "failure": "connection_refused",
          "success": false
        },
        "t0": 4.500478782,
        "t": 4.500931387,
        "transaction_id": 45
      },
      {
        "ip": "127.0.0.1",
        "port": 138,
        "status": {
          "failure": "connection_refused",
          "success": false
        },
        "t0": 4.600143458,
        "t": 4.600563589,
        "transaction_id": 46
      },
      {
        "ip": "127.0.0.1",
        "port": 999,
        "status": {
          "failure": "connection_refused",
          "success": false
        },
        "t0": 4.700869071,
        "t": 4.701286398,
        "transaction_id": 47
      },
      {
        "ip": "127.0.0.1",
        "port": 997,
        "status": {
          "failure": "connection_refused",
          "success": false
        },
        "t0": 4.800649524,
        "t": 4.80098966,
        "transaction_id": 48
      },
      {
        "ip": "127.0.0.1",
        "port": 25,
        "status": {
          "failure": "connection_refused",
          "success": false
        },
        "t0": 4.900198631,
        "t": 4.900555127,
        "transaction_id": 49
      },
      {
        "ip": "127.0.0.1",
        "port": 443,
        "status": {
          "failure": "connection_refused",
          "success": false
        },
        "t0": 5.000848381,
        "t": 5.001232948,
        "transaction_id": 50
      },
      {
        "ip": "127.0.0.1",
        "port": 1434,
        "status": {
          "failure": "connection_refused",
          "success": false
        },
        "t0": 5.100533463,
        "t": 5.10097256,
        "transaction_id": 51
      },
      {
        "ip": "127.0.0.1",
        "port": 1433,
        "status": {
          "failure": "connection_refused",
          "success": false
        },
        "t0": 5.200130508,
        "t": 5.200365997,
        "transaction_id": 52
      },
      {
        "ip": "127.0.0.1",
        "port": 993,
        "status": {
          "failure": "connection_refused",
          "success": false
        },
        "t0": 5.300709893,
        "t": 5.301125032,
        "transaction_id": 53
      },
      {
        "ip": "127.0.0.1",
        "port": 53,
        "status": {
          "failure": "connection_refused",
          "success": false
        },
        "t0": 5.400516553,
        "t": 5.40094399,
        "transaction_id": 54
      },
      {
        "ip": "127.0.0.1",
        "port": 514,
        "status": {
          "failure": "connection_refused",
          "success": false
        },
        "t0": 5.500190932,
        "t": 5.50063521,
        "transaction_id": 55
      },
      {
        "ip": "127.0.0.1",
        "port": 22,
        "status": {
          "failure": "connection_refused",
          "success": false
        },
        "t0": 5.600971269,
        "t": 5.601481948,
        "transaction_id": 56
      },
      {
        "ip": "127.0.0.1",
        "port": 3306,
        "status": {
          "failure": "connection_refused",
          "success": false
        },
        "t0": 5.700835243,
        "t": 5.701328909,
        "transaction_id": 57
      },
      {
        "ip": "127.0.0.1",
        "port": 593,
        "status": {
          "failure": "connection_refused",
          "success": false
        },
        "t0": 5.800593429,
        "t": 5.8010164589999995,
        "transaction_id": 58
      },
      {
        "ip": "127.0.0.1",
        "port": 162,
        "status": {
          "failure": "connection_refused",
          "success": false
        },
        "t0": 5.900248092,
        "t": 5.900488986,
        "transaction_id": 59
      },
      {
        "ip": "127.0.0.1",
        "port": 1025,
        "status": {
          "failure": "connection_refused",
          "success": false
        },
        "t0": 6.000825294,
        "t": 6.001217606,
        "transaction_id": 60
      },
      {
        "ip": "127.0.0.1",
        "port": 110,
        "status": {
          "failure": "connection_refused",
          "success": false
        },
        "t0": 6.100499873,
        "t": 6.100844805,
        "transaction_id": 61
      },
      {
        "ip": "127.0.0.1",
        "port": 23,
        "status": {
          "failure": "connection_refused",
          "success": false
        },
        "t0": 6.201233567,
        "t": 6.201747388,
        "transaction_id": 62
      }
    ]
  },
  "test_name": "portfiltering",
  "test_runtime": 6.201797635,
  "test_start_time": "2022-09-14 14:50:03",
  "test_version": "0.1.0"
}
```
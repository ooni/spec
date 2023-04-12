# Specification version number

2023-01-13-000

# Specification name

Random Traffic

# Test preconditions

An internet connection

# Expected impact

Ability to detect the censorship of fully-encrypted protocols which encrypt every
byte of traffic in an attempt to appear completely random.

```
Note: This does not include TLS as TLS has a standard handshake to begin with.
```

# Expected inputs

None

# Test description

The main goal of the test is to inform the user whether or not they are experiencing
censorship on connections that send fully encrypted packets that appear random, as
well as to record information about censored packets in order to better understand
the censorship algorithm. The test seeks to accomplish these goals by doing the
following:

1. If no IP address is given by the user, select an IP address from the list of IP 
   addresses in the affected range.
2. Complete a TCP handshake with the IP address and send a stream of null bytes as
   a control test. If this control test succeeds then proceed with the experiment, 
   otherwise attempt the control test with a new IP address two more times or until
   the control test is successful. If no control test succeeds end the test and
   return the error.
3. Repeat 20 times
    1. Complete a TCP handshake with the IP address and send a stream of random bytes.
       If this connection times out, we attempt to connect once more to check for residual
       censorship. 
    2. If the residual censorship test results in a timeout, we end the test,
       record information about the blocked packet, and inform the user they are experiencing
       censorship. Otherwise we continue with the test. If any error other than a timeout 
       occor the test terminates.
5. If no errors occurred and the test was completed, all connections are then closed
   and the test informs the user they are not experiencing censorship.

# Expected output

## Required output data

* The result of the test, 'success' or failure type
* Whether or not the censorship was detected

## Semantics

This experiment generates a "test keys" result object containing the following keys:

* success: True if no errors occurred
* connection_count: Number of successful connections
* final_popcount: The popcount of the triggering packet
* first_six: True if first six bytes of the final payload are printable
* twenty_contig: True if there exist twenty contiguous bytes of printable ASCII in
                the final payload
* half_printable: True if at least half of the final payload is made up of printable ASCII
* popcount_range: True if final popcount is less than 3.4 or greater than 4.6
* matches_http: True if fingerprinted as HTTP
* matches_tls: True if fingerprinted as TLS
* payload: Payload of final packet
* censorship: False if all 20 connections succeeded
* error: String of error

## Possible conclusions

Ability to determine if the user is experiencing censorship on fully-encrypted
traffic and what packet triggered the censorship.

## Example output sample

```JSON
{
    "annotations":{
        "architecture":"amd64",
        "engine_name":"ooniprobe-engine",
        "engine_version":"3.16.0-alpha",
        "platform":"macos"
    },
    "data_format_version":"0.2.0",
    "input":null,
    "measurement_start_time":"2023-01-03 06:53:40",
    "probe_asn":"AS6128",
    "probe_cc":"US",
    "probe_ip":"127.0.0.1",
    "probe_network_name":"Cablevision Systems Corp.",
    "report_id":"",
    "resolver_asn":"AS6128",
    "resolver_ip":"167.206.251.142",
    "resolver_network_name":"Cablevision Systems Corp.",
    "software_name":"miniooni",
    "software_version":"3.16.0-alpha",
    "test_keys":{
        "success":true,
        "connection_count":19,
        "final_popcount":4.074525745257453,
        "first_six":false,
        "twenty_contig":false,
        "half_printable":false,
        "popcount_range":false,
        "matches_http":false,
        "matches_tls":false,
        "payload":"KLpodhNrDfHPs6cEYBe096yVZdxqZ3udlhcs/ziiC11KHXcs2LUfa/CpiiLyo2NfguJ99k+k23XWE59+lw723HpsGJUKJnHop2BLXUCVUJDektT6Hm9rYTeBtAvqPZP+LVQ+WmqpoU7OFpeM3m7mVTut2AfSaH8TPhaDG377uYXz2tvZy+Oa7d/AsLzl4DKc707x+tITtFj4V/Gg2RfaHZe4C9tH9Wujw/62PiM6IgT3IK9fXT2QB0O9ZinY9+KxwVs7AYbXhoYdMoF9+s1wIL1f1NNx/Khgx6eYovROsj4768niLIPy6ketR0jZAA1CLidDAaWOvEDc/Tgv5vHcenUR0VawQFhGTfu+J6z4GEoQoi6e+N1HqvRoLXCd/OWdgybHVBlpPc8Wr7K8xrvdMwGIGKN+rpClGiFwxLJQkptr5kr9oZmM3T9cBy2ViZjdRM7HW3c8YmrGmw0jyVDszHcl4kBHeANgOEGtAudqvoxKPbLZYxvke64wu5RGr3CUEpwAnJW4GgPvl1KSWt9n5HSC0+Lhtbrcd7iUtlufoRjHrw3IGDt+n+S4F1tvV+4cslBRcv+wlJx4zFL+We+gJSg2CUFVLqOdRgpB73lBTe1Sb2vBB1RSZ3Cn0WTwhpbFVASpDS8nnJsD+CSVmXVpOy0PxvrYLA/UY6mE0kFBfqH9oVC8A+TN0IA3/vkzwZ/P9Xs8HRP5xm6shPvpy19MD9YWSK0Co3EXUpQrt4TW4kPeMbt/Dgpxe72zcuh6N9pjp3oR1fz1ioMOIp+1yalhB3XqgYAALUzpYI1Ya2A4if9qQq9nvVdLqDKFTehxKW1+mgJ+3/I7EG+6yprd7UGuQSpc49Yg/LhBchiXhIqTcgpNNNNClnjh31UTQwYT2NjYWuWK0ijGQfDjwP9bgYOPGaUOyzjkZTnWL1ejAaa5saA3q9TzKdZoY5Pw3BbO0WXP6SH2H1hhS/dB8XQPPLnq9jHj",
        "censorship":false,
        "error":null
    },
    "test_name":"shadowsocks",
    "test_runtime":6.178643611,
    "test_start_time":"2023-01-03 06:53:34",
    "test_version":"0.1.0"
}

```

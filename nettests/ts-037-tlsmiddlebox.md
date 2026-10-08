# Specification version number

2026-07-28

*_status_: current

# Specification name

TLS middlebox

# Test preconditions

* An internet connection

# Expected impact

Ability to detect the presence of TLS middleboxes censoring requests based on the servername.

# Expected inputs

- `control_sni` (`string`): a SNI to use as control (e.g. `example.org`)

- `testhelper` (`endpoint`): a URL like `tlshandshake://<host>:<port>` or 
`https://<host>:<port>`

- `sni` (`string`; optional): a potentially blocked SNI to measure (e.g. `1337x.be`)

The default implementation will use a domain such as `example.org` as
the `control_sni` and the testhelper's hostname as the target.  

# Test description

This test is divided into multiple steps that will each ensure that we can successfully 
perform iterative tracing on the `target` and return early in case of failure.

This test consists of two privacy modes: `default` and `'advanced`. These privacy modes only
pertain to the **TCP Traceroute** step of the test. The default privacy mode for all tests
is `default`.

The main steps of the experiment are:

1. **DNS lookup**
    Perform a A/AAAA query to the configured DoH resolver for the testhelper's hostname. Fall 
    back to the system resolver in case DoH fails and record the lst of DNS responses/records 
    under the "queried" key (see df-002-dnst.md).

2. **TCP Connect**
    Attempt to establish a TCP session on port 443 (default, overriden by the port in the 
    testhelper) for the list of IPs identified at step 1. The results of the connecting end up
    in the "tcp_connect" key. (see df-005-tcpconnect.md).

3. **TCP Traceroute**
    Attempt to conduct a TCP traceroute towards the list of filtered IPs. The results of the 
    traceroute end ip in `tcp_traceroute` within the `trace` key. The traceroute is run until
    the maximum TTL is reached. The outcome of each TTL-limited probe can either be a timeout,
    a successful connection, an error, or an ICMP message with the initial quoted packet.

    When the privacy mode is set to `default`, only country and AS information of routers on the
    forward network path between the client and server will be collected. When the privacy mode
    is set to `advanced`, additional IP address and RTT information of routers on the forward 
    network path between the client and server will be collected

4. **TLS Handshake**
    Attempt to perform a tls handshake for the list of filtered IPs (for which the TCP session 
    can successfully established) obtained at step 2. The handshake is performed iteratively 
    for each IP with an increment in the TTL for each successive iteration. 

    The entire tracing is done twice: using the `control_sni` and the `target`. Each iteration
    records the handshake results along with the corresponding TTL. The results of the trace end
    up in the `trace` key which is divided into: `control_trace` (the trace for the `control_sni`)
    and `target_trace` (the trace for the `target_sni`). Each `trace` field records the iterations
    for a single servername till we receive a `null` failure (a successful handshake) or a 
    `connection_reset`. The handshake results are recorded in the `handshake` field. (see 
    df-006-tlshandshake.md)

# Expected output

## Parent data format

We will include data following these data formats:

* `df-002-dnst`
* `df-005-tcpconnect`
* `df-010-icmp`
* `df-006-tlshandshake`

## Semantics

```JSON
{
   "queries": [],
   "tcp_connect": [],
   "iterative_trace": {
      "address": "",
      "tcp_traceroute": {},
      "control_trace": {},
      "target_trace": {}
   }
}
```

where:

- `queries` contains a list of `df-002-dnst` instances

- `tcp_connect` contains a list of `df-005-tcpconnect` instances

- `tcp_traceroute` contains the TCP traceroute of the form:

```JSON
{
  "ttl": ,
  "icmp_error": {}
}
```

where:

- `ttl` is a positive integer

- `icmp_error` follows the `df-010-icmp` data format

- `iterative_trace` contains the SNI-based iterative trace of the form:

```JSON
{
   "ttl": ,
   "handshake": {}
}
```

where:

- `ttl` is a positive integer

- `handshake` follows the `df-006-tlshandshake` data format

## Possible conclusions

* If there is a middlebox attempting to censor content in the network route 

* If the blocking of a particular servername is due to the presence of a middlebox
in the network route and where the middlebox is located with respect to
the forward network path


## Example output sample for `default` privacy mode

Response:

```JSON
{
  "annotations": {
    "architecture": "amd64",
    "engine_name": "ooniprobe-engine",
    "engine_version": "3.31.0-alpha",
    "go_version": "go1.26.8",
    "platform": "linux",
    "vcs_modified": "false",
    "vcs_revision": "6eaad0ed0048d3ed19980655f4a3ab743a951218",
    "vcs_time": "2026-10-05T10:34:23Z",
    "vcs_tool": "git"
  },
  "data_format_version": "0.2.0",
  "input": "tlstrace://github.com",
  "measurement_start_time": "2026-10-05 12:45:57",
  "options": [
    "MaxTTL=12"
  ],
  "probe_asn": "AS16276",
  "probe_cc": "CA",
  "probe_ip": "127.0.0.1",
  "probe_network_name": "OVH SAS",
  "resolver_asn": "AS16276",
  "resolver_ip": "158.69.169.9",
  "resolver_network_name": "OVH SAS",
  "software_name": "miniooni",
  "software_version": "3.31.0-alpha",
  "test_keys": {
    "queries": [
      {
        "answers": [
          {
            "asn": 13335,
            "as_org_name": "Cloudflare Inc",
            "answer_type": "AAAA",
            "ipv6": "2a06:98c1:52::4",
            "ttl": null
          },
          {
            "asn": 13335,
            "as_org_name": "Cloudflare Inc",
            "answer_type": "AAAA",
            "ipv6": "2803:f800:53::4",
            "ttl": null
          },
          {
            "asn": 13335,
            "as_org_name": "Cloudflare Inc",
            "answer_type": "A",
            "ipv4": "162.159.61.4",
            "ttl": null
          },
          {
            "asn": 13335,
            "as_org_name": "Cloudflare Inc",
            "answer_type": "A",
            "ipv4": "172.64.41.4",
            "ttl": null
          },
          {
            "answer_type": "CNAME",
            "hostname": "mozilla.cloudflare-dns.com.",
            "ttl": null
          }
        ],
        "engine": "getaddrinfo",
        "failure": null,
        "hostname": "mozilla.cloudflare-dns.com",
        "query_type": "ANY",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "",
        "t0": 0.000347891,
        "t": 0.001174443,
        "tags": []
      },
      {
        "answers": [
          {
            "asn": 36459,
            "as_org_name": "GitHub, Inc.",
            "answer_type": "A",
            "ipv4": "140.82.112.3",
            "ttl": null
          }
        ],
        "engine": "doh",
        "failure": null,
        "hostname": "github.com",
        "query_type": "A",
        "raw_response": "vymBgAABAAEAAAABBmdpdGh1YgNjb20AAAEAAcAMAAEAAQAAADEABIxScAMAACkE0AAAgAABnQAMAZkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "https://mozilla.cloudflare-dns.com/dns-query",
        "t0": 0.000211828,
        "t": 0.036852686,
        "tags": []
      },
      {
        "answers": null,
        "engine": "doh",
        "failure": "dns_no_answer",
        "hostname": "github.com",
        "query_type": "AAAA",
        "raw_response": "zZiBgAABAAAAAQABBmdpdGh1YgNjb20AABwAAcAMAAYAAQAAA3IASAducy0xNzA3CWF3c2Rucy0yMQJjbwJ1awARYXdzZG5zLWhvc3RtYXN0ZXIGYW1hem9uwBMAAAABAAAcIAAAA4QAEnUAAAFRgAAAKQTQAACAAAFZAAwBVQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "https://mozilla.cloudflare-dns.com/dns-query",
        "t0": 0.000142517,
        "t": 0.037201114,
        "tags": []
      }
    ],
    "tcp_connect": [
      {
        "ip": "140.82.112.3",
        "port": 443,
        "status": {
          "failure": null,
          "success": true
        },
        "t0": 0.037391663,
        "t": 0.051356225,
        "tags": []
      }
    ],
    "iterative_trace": [
      {
        "address": "140.82.112.3:443",
        "tcp_traceroute": {
          "server_name": "github.com",
          "iterations": [
            {
              "ttl": 1,
              "icmp_error": {
                "timeout": false,
                "connected": false,
                "error": "",
                "source_ip_prefix": "",
                "source_ip_country_code": "CA",
                "source_ip_asn": 16276,
                "source_ip_asn_org": "OVH SAS",
                "type": 11,
                "code": 0,
                "quote": {
                  "protocol": 0,
                  "source_port": 0,
                  "destination_port": 0,
                  "tcp_sequence_number": 0,
                  "udp_length": 0,
                  "udp_checksum": 0,
                  "remaining_payload": null
                },
                "t0": 0.051487013,
                "t": 0
              }
            },
            {
              "ttl": 2,
              "icmp_error": {
                "timeout": false,
                "connected": false,
                "error": "",
                "source_ip_prefix": "",
                "source_ip_country_code": "ZZ",
                "source_ip_asn": 0,
                "source_ip_asn_org": "",
                "type": 11,
                "code": 0,
                "quote": {
                  "protocol": 0,
                  "source_port": 0,
                  "destination_port": 0,
                  "tcp_sequence_number": 0,
                  "udp_length": 0,
                  "udp_checksum": 0,
                  "remaining_payload": null
                },
                "t0": 0.152389069,
                "t": 0
              }
            },
            {
              "ttl": 3,
              "icmp_error": {
                "timeout": false,
                "connected": false,
                "error": "",
                "source_ip_prefix": "",
                "source_ip_country_code": "ZZ",
                "source_ip_asn": 0,
                "source_ip_asn_org": "",
                "type": 11,
                "code": 0,
                "quote": {
                  "protocol": 0,
                  "source_port": 0,
                  "destination_port": 0,
                  "tcp_sequence_number": 0,
                  "udp_length": 0,
                  "udp_checksum": 0,
                  "remaining_payload": null
                },
                "t0": 0.251540123,
                "t": 0
              }
            },
            {
              "ttl": 4,
              "icmp_error": {
                "timeout": false,
                "connected": false,
                "error": "",
                "source_ip_prefix": "",
                "source_ip_country_code": "ZZ",
                "source_ip_asn": 0,
                "source_ip_asn_org": "",
                "type": 11,
                "code": 0,
                "quote": {
                  "protocol": 0,
                  "source_port": 0,
                  "destination_port": 0,
                  "tcp_sequence_number": 0,
                  "udp_length": 0,
                  "udp_checksum": 0,
                  "remaining_payload": null
                },
                "t0": 0.351764356,
                "t": 0
              }
            },
            {
              "ttl": 5,
              "icmp_error": {
                "timeout": false,
                "connected": false,
                "error": "",
                "source_ip_prefix": "",
                "source_ip_country_code": "ZZ",
                "source_ip_asn": 0,
                "source_ip_asn_org": "",
                "type": 11,
                "code": 0,
                "quote": {
                  "protocol": 0,
                  "source_port": 0,
                  "destination_port": 0,
                  "tcp_sequence_number": 0,
                  "udp_length": 0,
                  "udp_checksum": 0,
                  "remaining_payload": null
                },
                "t0": 0.451993338,
                "t": 0
              }
            },
            {
              "ttl": 6,
              "icmp_error": {
                "timeout": false,
                "connected": false,
                "error": "",
                "source_ip_prefix": "",
                "source_ip_country_code": "CA",
                "source_ip_asn": 16276,
                "source_ip_asn_org": "OVH SAS",
                "type": 11,
                "code": 0,
                "quote": {
                  "protocol": 0,
                  "source_port": 0,
                  "destination_port": 0,
                  "tcp_sequence_number": 0,
                  "udp_length": 0,
                  "udp_checksum": 0,
                  "remaining_payload": null
                },
                "t0": 0.552303441,
                "t": 0
              }
            },
            {
              "ttl": 7,
              "icmp_error": {
                "timeout": false,
                "connected": false,
                "error": "",
                "source_ip_prefix": "",
                "source_ip_country_code": "ZZ",
                "source_ip_asn": 0,
                "source_ip_asn_org": "",
                "type": 11,
                "code": 0,
                "quote": {
                  "protocol": 0,
                  "source_port": 0,
                  "destination_port": 0,
                  "tcp_sequence_number": 0,
                  "udp_length": 0,
                  "udp_checksum": 0,
                  "remaining_payload": null
                },
                "t0": 0.652567929,
                "t": 0
              }
            },
            {
              "ttl": 8,
              "icmp_error": {
                "timeout": false,
                "connected": false,
                "error": "",
                "source_ip_prefix": "",
                "source_ip_country_code": "CA",
                "source_ip_asn": 16276,
                "source_ip_asn_org": "OVH SAS",
                "type": 11,
                "code": 0,
                "quote": {
                  "protocol": 0,
                  "source_port": 0,
                  "destination_port": 0,
                  "tcp_sequence_number": 0,
                  "udp_length": 0,
                  "udp_checksum": 0,
                  "remaining_payload": null
                },
                "t0": 0.751759974,
                "t": 0
              }
            },
            {
              "ttl": 9,
              "icmp_error": {
                "timeout": false,
                "connected": false,
                "error": "",
                "source_ip_prefix": "",
                "source_ip_country_code": "ZZ",
                "source_ip_asn": 0,
                "source_ip_asn_org": "",
                "type": 11,
                "code": 0,
                "quote": {
                  "protocol": 0,
                  "source_port": 0,
                  "destination_port": 0,
                  "tcp_sequence_number": 0,
                  "udp_length": 0,
                  "udp_checksum": 0,
                  "remaining_payload": null
                },
                "t0": 0.851983748,
                "t": 0
              }
            },
            {
              "ttl": 10,
              "icmp_error": {
                "timeout": false,
                "connected": false,
                "error": "",
                "source_ip_prefix": "",
                "source_ip_country_code": "CA",
                "source_ip_asn": 0,
                "source_ip_asn_org": "",
                "type": 11,
                "code": 0,
                "quote": {
                  "protocol": 0,
                  "source_port": 0,
                  "destination_port": 0,
                  "tcp_sequence_number": 0,
                  "udp_length": 0,
                  "udp_checksum": 0,
                  "remaining_payload": null
                },
                "t0": 0.952198982,
                "t": 0
              }
            },
            {
              "ttl": 11,
              "icmp_error": {
                "timeout": true,
                "connected": false,
                "error": "",
                "source_ip_prefix": "",
                "source_ip_country_code": "",
                "source_ip_asn": 0,
                "source_ip_asn_org": "",
                "type": 0,
                "code": 0,
                "quote": {
                  "protocol": 0,
                  "source_port": 0,
                  "destination_port": 0,
                  "tcp_sequence_number": 0,
                  "udp_length": 0,
                  "udp_checksum": 0,
                  "remaining_payload": null
                },
                "t0": 1.052467762,
                "t": 4.05558034
              }
            },
            {
              "ttl": 12,
              "icmp_error": {
                "timeout": true,
                "connected": false,
                "error": "",
                "source_ip_prefix": "",
                "source_ip_country_code": "",
                "source_ip_asn": 0,
                "source_ip_asn_org": "",
                "type": 0,
                "code": 0,
                "quote": {
                  "protocol": 0,
                  "source_port": 0,
                  "destination_port": 0,
                  "tcp_sequence_number": 0,
                  "udp_length": 0,
                  "udp_checksum": 0,
                  "remaining_payload": null
                },
                "t0": 4.055771778,
                "t": 7.058863605
              }
            }
          ]
        },
        "control_trace": {
          "server_name": "example.com",
          "iterations": [
            {
              "ttl": 1,
              "handshake": {
                "network": "",
                "address": "",
                "cipher_suite": "",
                "failure": "host_unreachable",
                "failure_chain": [
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*net.OpError",
                    "error": "read tcp [scrubbed]:39868->140.82.112.3:443: read: no route to host"
                  },
                  {
                    "type": "*os.SyscallError",
                    "error": "read: no route to host"
                  },
                  {
                    "type": "syscall.Errno",
                    "error": "no route to host"
                  }
                ],
                "negotiated_protocol": "",
                "no_tls_verify": false,
                "peer_certificates": null,
                "server_name": "example.com",
                "t": 0,
                "tags": null,
                "tls_version": ""
              }
            },
            {
              "ttl": 2,
              "handshake": {
                "network": "",
                "address": "",
                "cipher_suite": "",
                "failure": "host_unreachable",
                "failure_chain": [
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*net.OpError",
                    "error": "read tcp [scrubbed]:39874->140.82.112.3:443: read: no route to host"
                  },
                  {
                    "type": "*os.SyscallError",
                    "error": "read: no route to host"
                  },
                  {
                    "type": "syscall.Errno",
                    "error": "no route to host"
                  }
                ],
                "negotiated_protocol": "",
                "no_tls_verify": false,
                "peer_certificates": null,
                "server_name": "example.com",
                "t": 0,
                "tags": null,
                "tls_version": ""
              }
            },
            {
              "ttl": 3,
              "handshake": {
                "network": "",
                "address": "",
                "cipher_suite": "",
                "failure": "host_unreachable",
                "failure_chain": [
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*net.OpError",
                    "error": "read tcp [scrubbed]:39890->140.82.112.3:443: read: no route to host"
                  },
                  {
                    "type": "*os.SyscallError",
                    "error": "read: no route to host"
                  },
                  {
                    "type": "syscall.Errno",
                    "error": "no route to host"
                  }
                ],
                "negotiated_protocol": "",
                "no_tls_verify": false,
                "peer_certificates": null,
                "server_name": "example.com",
                "t": 0,
                "tags": null,
                "tls_version": ""
              }
            },
            {
              "ttl": 4,
              "handshake": {
                "network": "",
                "address": "",
                "cipher_suite": "",
                "failure": "host_unreachable",
                "failure_chain": [
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*net.OpError",
                    "error": "read tcp [scrubbed]:39896->140.82.112.3:443: read: no route to host"
                  },
                  {
                    "type": "*os.SyscallError",
                    "error": "read: no route to host"
                  },
                  {
                    "type": "syscall.Errno",
                    "error": "no route to host"
                  }
                ],
                "negotiated_protocol": "",
                "no_tls_verify": false,
                "peer_certificates": null,
                "server_name": "example.com",
                "t": 0,
                "tags": null,
                "tls_version": ""
              }
            },
            {
              "ttl": 5,
              "handshake": {
                "network": "",
                "address": "",
                "cipher_suite": "",
                "failure": "host_unreachable",
                "failure_chain": [
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*net.OpError",
                    "error": "read tcp [scrubbed]:39908->140.82.112.3:443: read: no route to host"
                  },
                  {
                    "type": "*os.SyscallError",
                    "error": "read: no route to host"
                  },
                  {
                    "type": "syscall.Errno",
                    "error": "no route to host"
                  }
                ],
                "negotiated_protocol": "",
                "no_tls_verify": false,
                "peer_certificates": null,
                "server_name": "example.com",
                "t": 0,
                "tags": null,
                "tls_version": ""
              }
            },
            {
              "ttl": 6,
              "handshake": {
                "network": "",
                "address": "",
                "cipher_suite": "",
                "failure": "host_unreachable",
                "failure_chain": [
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*net.OpError",
                    "error": "read tcp [scrubbed]:39918->140.82.112.3:443: read: no route to host"
                  },
                  {
                    "type": "*os.SyscallError",
                    "error": "read: no route to host"
                  },
                  {
                    "type": "syscall.Errno",
                    "error": "no route to host"
                  }
                ],
                "negotiated_protocol": "",
                "no_tls_verify": false,
                "peer_certificates": null,
                "server_name": "example.com",
                "t": 0,
                "tags": null,
                "tls_version": ""
              }
            },
            {
              "ttl": 7,
              "handshake": {
                "network": "",
                "address": "",
                "cipher_suite": "",
                "failure": "host_unreachable",
                "failure_chain": [
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*net.OpError",
                    "error": "read tcp [scrubbed]:39926->140.82.112.3:443: read: no route to host"
                  },
                  {
                    "type": "*os.SyscallError",
                    "error": "read: no route to host"
                  },
                  {
                    "type": "syscall.Errno",
                    "error": "no route to host"
                  }
                ],
                "negotiated_protocol": "",
                "no_tls_verify": false,
                "peer_certificates": null,
                "server_name": "example.com",
                "t": 0,
                "tags": null,
                "tls_version": ""
              }
            },
            {
              "ttl": 8,
              "handshake": {
                "network": "",
                "address": "",
                "cipher_suite": "",
                "failure": "host_unreachable",
                "failure_chain": [
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*net.OpError",
                    "error": "read tcp [scrubbed]:39942->140.82.112.3:443: read: no route to host"
                  },
                  {
                    "type": "*os.SyscallError",
                    "error": "read: no route to host"
                  },
                  {
                    "type": "syscall.Errno",
                    "error": "no route to host"
                  }
                ],
                "negotiated_protocol": "",
                "no_tls_verify": false,
                "peer_certificates": null,
                "server_name": "example.com",
                "t": 0,
                "tags": null,
                "tls_version": ""
              }
            },
            {
              "ttl": 9,
              "handshake": {
                "network": "",
                "address": "",
                "cipher_suite": "",
                "failure": "host_unreachable",
                "failure_chain": [
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*net.OpError",
                    "error": "read tcp [scrubbed]:39944->140.82.112.3:443: read: no route to host"
                  },
                  {
                    "type": "*os.SyscallError",
                    "error": "read: no route to host"
                  },
                  {
                    "type": "syscall.Errno",
                    "error": "no route to host"
                  }
                ],
                "negotiated_protocol": "",
                "no_tls_verify": false,
                "peer_certificates": null,
                "server_name": "example.com",
                "t": 0,
                "tags": null,
                "tls_version": ""
              }
            },
            {
              "ttl": 10,
              "handshake": {
                "network": "",
                "address": "",
                "cipher_suite": "",
                "failure": "host_unreachable",
                "failure_chain": [
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*net.OpError",
                    "error": "read tcp [scrubbed]:39946->140.82.112.3:443: read: no route to host"
                  },
                  {
                    "type": "*os.SyscallError",
                    "error": "read: no route to host"
                  },
                  {
                    "type": "syscall.Errno",
                    "error": "no route to host"
                  }
                ],
                "negotiated_protocol": "",
                "no_tls_verify": false,
                "peer_certificates": null,
                "server_name": "example.com",
                "t": 0,
                "tags": null,
                "tls_version": ""
              }
            },
            {
              "ttl": 11,
              "handshake": {
                "network": "",
                "address": "",
                "cipher_suite": "",
                "failure": "generic_timeout_error",
                "failure_chain": [
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "generic_timeout_error"
                  },
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "generic_timeout_error"
                  },
                  {
                    "type": "*net.OpError",
                    "error": "read tcp [scrubbed]:39958->140.82.112.3:443: i/o timeout"
                  },
                  {
                    "type": "*poll.DeadlineExceededError",
                    "error": "i/o timeout"
                  }
                ],
                "negotiated_protocol": "",
                "no_tls_verify": false,
                "peer_certificates": null,
                "server_name": "example.com",
                "t": 0,
                "tags": null,
                "tls_version": ""
              }
            },
            {
              "ttl": 12,
              "handshake": {
                "network": "",
                "address": "",
                "cipher_suite": "",
                "failure": "generic_timeout_error",
                "failure_chain": [
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "generic_timeout_error"
                  },
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "generic_timeout_error"
                  },
                  {
                    "type": "*net.OpError",
                    "error": "read tcp [scrubbed]:39960->140.82.112.3:443: i/o timeout"
                  },
                  {
                    "type": "*poll.DeadlineExceededError",
                    "error": "i/o timeout"
                  }
                ],
                "negotiated_protocol": "",
                "no_tls_verify": false,
                "peer_certificates": null,
                "server_name": "example.com",
                "t": 0,
                "tags": null,
                "tls_version": ""
              }
            }
          ]
        },
        "target_trace": {
          "server_name": "github.com",
          "iterations": [
            {
              "ttl": 1,
              "handshake": {
                "network": "",
                "address": "",
                "cipher_suite": "",
                "failure": "host_unreachable",
                "failure_chain": [
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*net.OpError",
                    "error": "read tcp [scrubbed]:45926->140.82.112.3:443: read: no route to host"
                  },
                  {
                    "type": "*os.SyscallError",
                    "error": "read: no route to host"
                  },
                  {
                    "type": "syscall.Errno",
                    "error": "no route to host"
                  }
                ],
                "negotiated_protocol": "",
                "no_tls_verify": false,
                "peer_certificates": null,
                "server_name": "github.com",
                "t": 0,
                "tags": null,
                "tls_version": ""
              }
            },
            {
              "ttl": 2,
              "handshake": {
                "network": "",
                "address": "",
                "cipher_suite": "",
                "failure": "host_unreachable",
                "failure_chain": [
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*net.OpError",
                    "error": "read tcp [scrubbed]:45928->140.82.112.3:443: read: no route to host"
                  },
                  {
                    "type": "*os.SyscallError",
                    "error": "read: no route to host"
                  },
                  {
                    "type": "syscall.Errno",
                    "error": "no route to host"
                  }
                ],
                "negotiated_protocol": "",
                "no_tls_verify": false,
                "peer_certificates": null,
                "server_name": "github.com",
                "t": 0,
                "tags": null,
                "tls_version": ""
              }
            },
            {
              "ttl": 3,
              "handshake": {
                "network": "",
                "address": "",
                "cipher_suite": "",
                "failure": "host_unreachable",
                "failure_chain": [
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*net.OpError",
                    "error": "read tcp [scrubbed]:45938->140.82.112.3:443: read: no route to host"
                  },
                  {
                    "type": "*os.SyscallError",
                    "error": "read: no route to host"
                  },
                  {
                    "type": "syscall.Errno",
                    "error": "no route to host"
                  }
                ],
                "negotiated_protocol": "",
                "no_tls_verify": false,
                "peer_certificates": null,
                "server_name": "github.com",
                "t": 0,
                "tags": null,
                "tls_version": ""
              }
            },
            {
              "ttl": 4,
              "handshake": {
                "network": "",
                "address": "",
                "cipher_suite": "",
                "failure": "host_unreachable",
                "failure_chain": [
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*net.OpError",
                    "error": "read tcp [scrubbed]:45944->140.82.112.3:443: read: no route to host"
                  },
                  {
                    "type": "*os.SyscallError",
                    "error": "read: no route to host"
                  },
                  {
                    "type": "syscall.Errno",
                    "error": "no route to host"
                  }
                ],
                "negotiated_protocol": "",
                "no_tls_verify": false,
                "peer_certificates": null,
                "server_name": "github.com",
                "t": 0,
                "tags": null,
                "tls_version": ""
              }
            },
            {
              "ttl": 5,
              "handshake": {
                "network": "",
                "address": "",
                "cipher_suite": "",
                "failure": "host_unreachable",
                "failure_chain": [
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*net.OpError",
                    "error": "read tcp [scrubbed]:45948->140.82.112.3:443: read: no route to host"
                  },
                  {
                    "type": "*os.SyscallError",
                    "error": "read: no route to host"
                  },
                  {
                    "type": "syscall.Errno",
                    "error": "no route to host"
                  }
                ],
                "negotiated_protocol": "",
                "no_tls_verify": false,
                "peer_certificates": null,
                "server_name": "github.com",
                "t": 0,
                "tags": null,
                "tls_version": ""
              }
            },
            {
              "ttl": 6,
              "handshake": {
                "network": "",
                "address": "",
                "cipher_suite": "",
                "failure": "host_unreachable",
                "failure_chain": [
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*net.OpError",
                    "error": "read tcp [scrubbed]:45954->140.82.112.3:443: read: no route to host"
                  },
                  {
                    "type": "*os.SyscallError",
                    "error": "read: no route to host"
                  },
                  {
                    "type": "syscall.Errno",
                    "error": "no route to host"
                  }
                ],
                "negotiated_protocol": "",
                "no_tls_verify": false,
                "peer_certificates": null,
                "server_name": "github.com",
                "t": 0,
                "tags": null,
                "tls_version": ""
              }
            },
            {
              "ttl": 7,
              "handshake": {
                "network": "",
                "address": "",
                "cipher_suite": "",
                "failure": "host_unreachable",
                "failure_chain": [
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*net.OpError",
                    "error": "read tcp [scrubbed]:45956->140.82.112.3:443: read: no route to host"
                  },
                  {
                    "type": "*os.SyscallError",
                    "error": "read: no route to host"
                  },
                  {
                    "type": "syscall.Errno",
                    "error": "no route to host"
                  }
                ],
                "negotiated_protocol": "",
                "no_tls_verify": false,
                "peer_certificates": null,
                "server_name": "github.com",
                "t": 0,
                "tags": null,
                "tls_version": ""
              }
            },
            {
              "ttl": 8,
              "handshake": {
                "network": "",
                "address": "",
                "cipher_suite": "",
                "failure": "host_unreachable",
                "failure_chain": [
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*net.OpError",
                    "error": "read tcp [scrubbed]:45972->140.82.112.3:443: read: no route to host"
                  },
                  {
                    "type": "*os.SyscallError",
                    "error": "read: no route to host"
                  },
                  {
                    "type": "syscall.Errno",
                    "error": "no route to host"
                  }
                ],
                "negotiated_protocol": "",
                "no_tls_verify": false,
                "peer_certificates": null,
                "server_name": "github.com",
                "t": 0,
                "tags": null,
                "tls_version": ""
              }
            },
            {
              "ttl": 9,
              "handshake": {
                "network": "",
                "address": "",
                "cipher_suite": "",
                "failure": "host_unreachable",
                "failure_chain": [
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*net.OpError",
                    "error": "read tcp [scrubbed]:45984->140.82.112.3:443: read: no route to host"
                  },
                  {
                    "type": "*os.SyscallError",
                    "error": "read: no route to host"
                  },
                  {
                    "type": "syscall.Errno",
                    "error": "no route to host"
                  }
                ],
                "negotiated_protocol": "",
                "no_tls_verify": false,
                "peer_certificates": null,
                "server_name": "github.com",
                "t": 0,
                "tags": null,
                "tls_version": ""
              }
            },
            {
              "ttl": 10,
              "handshake": {
                "network": "",
                "address": "",
                "cipher_suite": "",
                "failure": "host_unreachable",
                "failure_chain": [
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*net.OpError",
                    "error": "read tcp [scrubbed]:45990->140.82.112.3:443: read: no route to host"
                  },
                  {
                    "type": "*os.SyscallError",
                    "error": "read: no route to host"
                  },
                  {
                    "type": "syscall.Errno",
                    "error": "no route to host"
                  }
                ],
                "negotiated_protocol": "",
                "no_tls_verify": false,
                "peer_certificates": null,
                "server_name": "github.com",
                "t": 0,
                "tags": null,
                "tls_version": ""
              }
            },
            {
              "ttl": 11,
              "handshake": {
                "network": "",
                "address": "",
                "cipher_suite": "",
                "failure": "generic_timeout_error",
                "failure_chain": [
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "generic_timeout_error"
                  },
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "generic_timeout_error"
                  },
                  {
                    "type": "*net.OpError",
                    "error": "read tcp [scrubbed]:46000->140.82.112.3:443: i/o timeout"
                  },
                  {
                    "type": "*poll.DeadlineExceededError",
                    "error": "i/o timeout"
                  }
                ],
                "negotiated_protocol": "",
                "no_tls_verify": false,
                "peer_certificates": null,
                "server_name": "github.com",
                "t": 0,
                "tags": null,
                "tls_version": ""
              }
            },
            {
              "ttl": 12,
              "handshake": {
                "network": "",
                "address": "",
                "cipher_suite": "",
                "failure": "generic_timeout_error",
                "failure_chain": [
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "generic_timeout_error"
                  },
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "generic_timeout_error"
                  },
                  {
                    "type": "*net.OpError",
                    "error": "read tcp [scrubbed]:46006->140.82.112.3:443: i/o timeout"
                  },
                  {
                    "type": "*poll.DeadlineExceededError",
                    "error": "i/o timeout"
                  }
                ],
                "negotiated_protocol": "",
                "no_tls_verify": false,
                "peer_certificates": null,
                "server_name": "github.com",
                "t": 0,
                "tags": null,
                "tls_version": ""
              }
            }
          ]
        }
      }
    ]
  },
  "test_name": "tlsmiddlebox",
  "test_runtime": 29.289105532,
  "test_start_time": "2026-10-05 12:45:57",
  "test_version": "0.1.3"
}
```

## Example output sample for `advanced` privacy mode

```JSON
{
  "annotations": {
    "architecture": "amd64",
    "engine_name": "ooniprobe-engine",
    "engine_version": "3.31.0-alpha",
    "go_version": "go1.26.8",
    "platform": "linux",
    "vcs_modified": "false",
    "vcs_revision": "6eaad0ed0048d3ed19980655f4a3ab743a951218",
    "vcs_time": "2026-10-05T10:34:23Z",
    "vcs_tool": "git"
  },
  "data_format_version": "0.2.0",
  "input": "tlstrace://github.com",
  "measurement_start_time": "2026-10-05 12:50:12",
  "options": [
    "MaxTTL=12",
    "PrivacyMode=advanced"
  ],
  "probe_asn": "AS16276",
  "probe_cc": "CA",
  "probe_ip": "127.0.0.1",
  "probe_network_name": "OVH SAS",
  "resolver_asn": "AS16276",
  "resolver_ip": "158.69.169.16",
  "resolver_network_name": "OVH SAS",
  "software_name": "miniooni",
  "software_version": "3.31.0-alpha",
  "test_keys": {
    "queries": [
      {
        "answers": [
          {
            "asn": 13335,
            "as_org_name": "Cloudflare Inc",
            "answer_type": "AAAA",
            "ipv6": "2a06:98c1:52::4",
            "ttl": null
          },
          {
            "asn": 13335,
            "as_org_name": "Cloudflare Inc",
            "answer_type": "AAAA",
            "ipv6": "2803:f800:53::4",
            "ttl": null
          },
          {
            "asn": 13335,
            "as_org_name": "Cloudflare Inc",
            "answer_type": "A",
            "ipv4": "172.64.41.4",
            "ttl": null
          },
          {
            "asn": 13335,
            "as_org_name": "Cloudflare Inc",
            "answer_type": "A",
            "ipv4": "162.159.61.4",
            "ttl": null
          },
          {
            "answer_type": "CNAME",
            "hostname": "mozilla.cloudflare-dns.com.",
            "ttl": null
          }
        ],
        "engine": "getaddrinfo",
        "failure": null,
        "hostname": "mozilla.cloudflare-dns.com",
        "query_type": "ANY",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "",
        "t0": 0.000517956,
        "t": 0.001430246,
        "tags": []
      },
      {
        "answers": [
          {
            "asn": 36459,
            "as_org_name": "GitHub, Inc.",
            "answer_type": "A",
            "ipv4": "140.82.112.3",
            "ttl": null
          }
        ],
        "engine": "doh",
        "failure": null,
        "hostname": "github.com",
        "query_type": "A",
        "raw_response": "TiOBgAABAAEAAAABBmdpdGh1YgNjb20AAAEAAcAMAAEAAQAAABgABIxScAMAACkE0AAAgAABnQAMAZkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "https://mozilla.cloudflare-dns.com/dns-query",
        "t0": 0.000259497,
        "t": 0.03943692,
        "tags": []
      },
      {
        "answers": null,
        "engine": "doh",
        "failure": "dns_no_answer",
        "hostname": "github.com",
        "query_type": "AAAA",
        "raw_response": "bUOBgAABAAAAAQABBmdpdGh1YgNjb20AABwAAcAMAAYAAQAADgsANQRkbnMxA3AwOAVuc29uZQNuZXQACmhvc3RtYXN0ZXLAMWK7sjcAAKjAAAAcIAASdQAAAA4QAAApBNAAAIAAAWwADAFoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "https://mozilla.cloudflare-dns.com/dns-query",
        "t0": 0.000231906,
        "t": 0.039740939,
        "tags": []
      }
    ],
    "tcp_connect": [
      {
        "ip": "140.82.112.3",
        "port": 443,
        "status": {
          "failure": null,
          "success": true
        },
        "t0": 0.039926601,
        "t": 0.054221657,
        "tags": []
      }
    ],
    "iterative_trace": [
      {
        "address": "140.82.112.3:443",
        "tcp_traceroute": {
          "server_name": "github.com",
          "iterations": [
            {
              "ttl": 1,
              "icmp_error": {
                "timeout": false,
                "connected": false,
                "error": "",
                "source_ip_prefix": "148.113.176.252",
                "source_ip_country_code": "CA",
                "source_ip_asn": 16276,
                "source_ip_asn_org": "OVH SAS",
                "type": 11,
                "code": 0,
                "quote": {
                  "protocol": 6,
                  "source_port": 53676,
                  "destination_port": 443,
                  "tcp_sequence_number": 4095625418,
                  "udp_length": 0,
                  "udp_checksum": 0,
                  "remaining_payload": null
                },
                "t0": 0.054354953,
                "t": 0.054706712
              }
            },
            {
              "ttl": 2,
              "icmp_error": {
                "timeout": false,
                "connected": false,
                "error": "",
                "source_ip_prefix": "10.165.11.60",
                "source_ip_country_code": "ZZ",
                "source_ip_asn": 0,
                "source_ip_asn_org": "",
                "type": 11,
                "code": 0,
                "quote": {
                  "protocol": 6,
                  "source_port": 53684,
                  "destination_port": 443,
                  "tcp_sequence_number": 2501184286,
                  "udp_length": 0,
                  "udp_checksum": 0,
                  "remaining_payload": "AAAAAKAC+vDlsAAAAgQFtAQCCAqgxRGCAAAAAAEDAwc="
                },
                "t0": 0.155239289,
                "t": 0.155439834
              }
            },
            {
              "ttl": 3,
              "icmp_error": {
                "timeout": false,
                "connected": false,
                "error": "",
                "source_ip_prefix": "10.34.116.74",
                "source_ip_country_code": "ZZ",
                "source_ip_asn": 0,
                "source_ip_asn_org": "",
                "type": 11,
                "code": 0,
                "quote": {
                  "protocol": 6,
                  "source_port": 53688,
                  "destination_port": 443,
                  "tcp_sequence_number": 797244013,
                  "udp_length": 0,
                  "udp_checksum": 0,
                  "remaining_payload": null
                },
                "t0": 0.255410296,
                "t": 0.255971642
              }
            },
            {
              "ttl": 4,
              "icmp_error": {
                "timeout": false,
                "connected": false,
                "error": "",
                "source_ip_prefix": "10.74.10.6",
                "source_ip_country_code": "ZZ",
                "source_ip_asn": 0,
                "source_ip_asn_org": "",
                "type": 11,
                "code": 0,
                "quote": {
                  "protocol": 6,
                  "source_port": 53704,
                  "destination_port": 443,
                  "tcp_sequence_number": 3544527072,
                  "udp_length": 0,
                  "udp_checksum": 0,
                  "remaining_payload": "AAAAAKAC+vCA4wAAAgQFtAQCCAqgxRJJAAAAAAEDAwc="
                },
                "t0": 0.354637846,
                "t": 0.35478255
              }
            },
            {
              "ttl": 5,
              "icmp_error": {
                "timeout": false,
                "connected": false,
                "error": "",
                "source_ip_prefix": "10.95.81.8",
                "source_ip_country_code": "ZZ",
                "source_ip_asn": 0,
                "source_ip_asn_org": "",
                "type": 11,
                "code": 0,
                "quote": {
                  "protocol": 6,
                  "source_port": 53720,
                  "destination_port": 443,
                  "tcp_sequence_number": 291007086,
                  "udp_length": 0,
                  "udp_checksum": 0,
                  "remaining_payload": "AAAAAKAC+vAIzwAAAgQFtAQCCAqgxRKtAAAAAAEDAwcAAAAAAAAAAA=="
                },
                "t0": 0.454862312,
                "t": 0.481119917
              }
            },
            {
              "ttl": 6,
              "icmp_error": {
                "timeout": false,
                "connected": false,
                "error": "",
                "source_ip_prefix": "198.27.73.205",
                "source_ip_country_code": "CA",
                "source_ip_asn": 16276,
                "source_ip_asn_org": "OVH SAS",
                "type": 11,
                "code": 0,
                "quote": {
                  "protocol": 6,
                  "source_port": 53722,
                  "destination_port": 443,
                  "tcp_sequence_number": 1077918402,
                  "udp_length": 0,
                  "udp_checksum": 0,
                  "remaining_payload": "AAAAAKAC+vCJLAAAAgQFtAQCCAqgxRMSAAAAAAEDAwcAAAAAAAAAAA=="
                },
                "t0": 0.555171312,
                "t": 0.564973274
              }
            },
            {
              "ttl": 7,
              "icmp_error": {
                "timeout": false,
                "connected": false,
                "error": "",
                "source_ip_prefix": "192.99.146.219",
                "source_ip_country_code": "CA",
                "source_ip_asn": 16276,
                "source_ip_asn_org": "OVH SAS",
                "type": 11,
                "code": 0,
                "quote": {
                  "protocol": 6,
                  "source_port": 53732,
                  "destination_port": 443,
                  "tcp_sequence_number": 2339561224,
                  "udp_length": 0,
                  "udp_checksum": 0,
                  "remaining_payload": "AAAAAKAC+vAZRQAAAgQFtAQCCAqgxRN2AAAAAAEDAwcAAAAAAAAAAA=="
                },
                "t0": 0.655350959,
                "t": 0.665820959
              }
            },
            {
              "ttl": 8,
              "icmp_error": {
                "timeout": false,
                "connected": false,
                "error": "",
                "source_ip_prefix": "198.27.73.203",
                "source_ip_country_code": "CA",
                "source_ip_asn": 16276,
                "source_ip_asn_org": "OVH SAS",
                "type": 11,
                "code": 0,
                "quote": {
                  "protocol": 6,
                  "source_port": 53746,
                  "destination_port": 443,
                  "tcp_sequence_number": 2605417823,
                  "udp_length": 0,
                  "udp_checksum": 0,
                  "remaining_payload": "AAAAAKAC+vBipAAAAgQFtAQCCAqgxRPZAAAAAAEDAwcAAAAAAAAAAA=="
                },
                "t0": 0.754610642,
                "t": 0.768000691
              }
            },
            {
              "ttl": 9,
              "icmp_error": {
                "timeout": false,
                "connected": false,
                "error": "",
                "source_ip_prefix": "10.200.2.209",
                "source_ip_country_code": "ZZ",
                "source_ip_asn": 0,
                "source_ip_asn_org": "",
                "type": 11,
                "code": 0,
                "quote": {
                  "protocol": 6,
                  "source_port": 53748,
                  "destination_port": 443,
                  "tcp_sequence_number": 4177358491,
                  "udp_length": 0,
                  "udp_checksum": 0,
                  "remaining_payload": "AAAAAKAC+vAbUAAAAgQFtAQCCAqgxRQ9AAAAAAEDAwcAAAAAAAAAAA=="
                },
                "t0": 0.854787644,
                "t": 0.869618758
              }
            },
            {
              "ttl": 10,
              "icmp_error": {
                "timeout": false,
                "connected": false,
                "error": "",
                "source_ip_prefix": "206.126.237.205",
                "source_ip_country_code": "CA",
                "source_ip_asn": 0,
                "source_ip_asn_org": "",
                "type": 11,
                "code": 0,
                "quote": {
                  "protocol": 6,
                  "source_port": 53760,
                  "destination_port": 443,
                  "tcp_sequence_number": 3060716111,
                  "udp_length": 0,
                  "udp_checksum": 0,
                  "remaining_payload": null
                },
                "t0": 0.955035432,
                "t": 0.968472598
              }
            },
            {
              "ttl": 11,
              "icmp_error": {
                "timeout": true,
                "connected": false,
                "error": "",
                "source_ip_prefix": "",
                "source_ip_country_code": "",
                "source_ip_asn": 0,
                "source_ip_asn_org": "",
                "type": 0,
                "code": 0,
                "quote": {
                  "protocol": 0,
                  "source_port": 0,
                  "destination_port": 0,
                  "tcp_sequence_number": 0,
                  "udp_length": 0,
                  "udp_checksum": 0,
                  "remaining_payload": null
                },
                "t0": 1.055312263,
                "t": 4.058201113
              }
            },
            {
              "ttl": 12,
              "icmp_error": {
                "timeout": true,
                "connected": false,
                "error": "",
                "source_ip_prefix": "",
                "source_ip_country_code": "",
                "source_ip_asn": 0,
                "source_ip_asn_org": "",
                "type": 0,
                "code": 0,
                "quote": {
                  "protocol": 0,
                  "source_port": 0,
                  "destination_port": 0,
                  "tcp_sequence_number": 0,
                  "udp_length": 0,
                  "udp_checksum": 0,
                  "remaining_payload": null
                },
                "t0": 4.058380348,
                "t": 7.061466554
              }
            }
          ]
        },
        "control_trace": {
          "server_name": "example.com",
          "iterations": [
            {
              "ttl": 1,
              "handshake": {
                "network": "",
                "address": "",
                "cipher_suite": "",
                "failure": "host_unreachable",
                "failure_chain": [
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*net.OpError",
                    "error": "read tcp [scrubbed]:45996->140.82.112.3:443: read: no route to host"
                  },
                  {
                    "type": "*os.SyscallError",
                    "error": "read: no route to host"
                  },
                  {
                    "type": "syscall.Errno",
                    "error": "no route to host"
                  }
                ],
                "negotiated_protocol": "",
                "no_tls_verify": false,
                "peer_certificates": null,
                "server_name": "example.com",
                "t": 0,
                "tags": null,
                "tls_version": ""
              }
            },
            {
              "ttl": 2,
              "handshake": {
                "network": "",
                "address": "",
                "cipher_suite": "",
                "failure": "host_unreachable",
                "failure_chain": [
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*net.OpError",
                    "error": "read tcp [scrubbed]:46000->140.82.112.3:443: read: no route to host"
                  },
                  {
                    "type": "*os.SyscallError",
                    "error": "read: no route to host"
                  },
                  {
                    "type": "syscall.Errno",
                    "error": "no route to host"
                  }
                ],
                "negotiated_protocol": "",
                "no_tls_verify": false,
                "peer_certificates": null,
                "server_name": "example.com",
                "t": 0,
                "tags": null,
                "tls_version": ""
              }
            },
            {
              "ttl": 3,
              "handshake": {
                "network": "",
                "address": "",
                "cipher_suite": "",
                "failure": "host_unreachable",
                "failure_chain": [
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*net.OpError",
                    "error": "read tcp [scrubbed]:46002->140.82.112.3:443: read: no route to host"
                  },
                  {
                    "type": "*os.SyscallError",
                    "error": "read: no route to host"
                  },
                  {
                    "type": "syscall.Errno",
                    "error": "no route to host"
                  }
                ],
                "negotiated_protocol": "",
                "no_tls_verify": false,
                "peer_certificates": null,
                "server_name": "example.com",
                "t": 0,
                "tags": null,
                "tls_version": ""
              }
            },
            {
              "ttl": 4,
              "handshake": {
                "network": "",
                "address": "",
                "cipher_suite": "",
                "failure": "host_unreachable",
                "failure_chain": [
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*net.OpError",
                    "error": "read tcp [scrubbed]:46008->140.82.112.3:443: read: no route to host"
                  },
                  {
                    "type": "*os.SyscallError",
                    "error": "read: no route to host"
                  },
                  {
                    "type": "syscall.Errno",
                    "error": "no route to host"
                  }
                ],
                "negotiated_protocol": "",
                "no_tls_verify": false,
                "peer_certificates": null,
                "server_name": "example.com",
                "t": 0,
                "tags": null,
                "tls_version": ""
              }
            },
            {
              "ttl": 5,
              "handshake": {
                "network": "",
                "address": "",
                "cipher_suite": "",
                "failure": "host_unreachable",
                "failure_chain": [
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*net.OpError",
                    "error": "read tcp [scrubbed]:46022->140.82.112.3:443: read: no route to host"
                  },
                  {
                    "type": "*os.SyscallError",
                    "error": "read: no route to host"
                  },
                  {
                    "type": "syscall.Errno",
                    "error": "no route to host"
                  }
                ],
                "negotiated_protocol": "",
                "no_tls_verify": false,
                "peer_certificates": null,
                "server_name": "example.com",
                "t": 0,
                "tags": null,
                "tls_version": ""
              }
            },
            {
              "ttl": 6,
              "handshake": {
                "network": "",
                "address": "",
                "cipher_suite": "",
                "failure": "host_unreachable",
                "failure_chain": [
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*net.OpError",
                    "error": "read tcp [scrubbed]:46032->140.82.112.3:443: read: no route to host"
                  },
                  {
                    "type": "*os.SyscallError",
                    "error": "read: no route to host"
                  },
                  {
                    "type": "syscall.Errno",
                    "error": "no route to host"
                  }
                ],
                "negotiated_protocol": "",
                "no_tls_verify": false,
                "peer_certificates": null,
                "server_name": "example.com",
                "t": 0,
                "tags": null,
                "tls_version": ""
              }
            },
            {
              "ttl": 7,
              "handshake": {
                "network": "",
                "address": "",
                "cipher_suite": "",
                "failure": "host_unreachable",
                "failure_chain": [
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*net.OpError",
                    "error": "read tcp [scrubbed]:46040->140.82.112.3:443: read: no route to host"
                  },
                  {
                    "type": "*os.SyscallError",
                    "error": "read: no route to host"
                  },
                  {
                    "type": "syscall.Errno",
                    "error": "no route to host"
                  }
                ],
                "negotiated_protocol": "",
                "no_tls_verify": false,
                "peer_certificates": null,
                "server_name": "example.com",
                "t": 0,
                "tags": null,
                "tls_version": ""
              }
            },
            {
              "ttl": 8,
              "handshake": {
                "network": "",
                "address": "",
                "cipher_suite": "",
                "failure": "host_unreachable",
                "failure_chain": [
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*net.OpError",
                    "error": "read tcp [scrubbed]:46044->140.82.112.3:443: read: no route to host"
                  },
                  {
                    "type": "*os.SyscallError",
                    "error": "read: no route to host"
                  },
                  {
                    "type": "syscall.Errno",
                    "error": "no route to host"
                  }
                ],
                "negotiated_protocol": "",
                "no_tls_verify": false,
                "peer_certificates": null,
                "server_name": "example.com",
                "t": 0,
                "tags": null,
                "tls_version": ""
              }
            },
            {
              "ttl": 9,
              "handshake": {
                "network": "",
                "address": "",
                "cipher_suite": "",
                "failure": "host_unreachable",
                "failure_chain": [
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*net.OpError",
                    "error": "read tcp [scrubbed]:46050->140.82.112.3:443: read: no route to host"
                  },
                  {
                    "type": "*os.SyscallError",
                    "error": "read: no route to host"
                  },
                  {
                    "type": "syscall.Errno",
                    "error": "no route to host"
                  }
                ],
                "negotiated_protocol": "",
                "no_tls_verify": false,
                "peer_certificates": null,
                "server_name": "example.com",
                "t": 0,
                "tags": null,
                "tls_version": ""
              }
            },
            {
              "ttl": 10,
              "handshake": {
                "network": "",
                "address": "",
                "cipher_suite": "",
                "failure": "host_unreachable",
                "failure_chain": [
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*net.OpError",
                    "error": "read tcp [scrubbed]:46062->140.82.112.3:443: read: no route to host"
                  },
                  {
                    "type": "*os.SyscallError",
                    "error": "read: no route to host"
                  },
                  {
                    "type": "syscall.Errno",
                    "error": "no route to host"
                  }
                ],
                "negotiated_protocol": "",
                "no_tls_verify": false,
                "peer_certificates": null,
                "server_name": "example.com",
                "t": 0,
                "tags": null,
                "tls_version": ""
              }
            },
            {
              "ttl": 11,
              "handshake": {
                "network": "",
                "address": "",
                "cipher_suite": "",
                "failure": "generic_timeout_error",
                "failure_chain": [
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "generic_timeout_error"
                  },
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "generic_timeout_error"
                  },
                  {
                    "type": "*net.OpError",
                    "error": "read tcp [scrubbed]:46066->140.82.112.3:443: i/o timeout"
                  },
                  {
                    "type": "*poll.DeadlineExceededError",
                    "error": "i/o timeout"
                  }
                ],
                "negotiated_protocol": "",
                "no_tls_verify": false,
                "peer_certificates": null,
                "server_name": "example.com",
                "t": 0,
                "tags": null,
                "tls_version": ""
              }
            },
            {
              "ttl": 12,
              "handshake": {
                "network": "",
                "address": "",
                "cipher_suite": "",
                "failure": "generic_timeout_error",
                "failure_chain": [
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "generic_timeout_error"
                  },
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "generic_timeout_error"
                  },
                  {
                    "type": "*net.OpError",
                    "error": "read tcp [scrubbed]:46072->140.82.112.3:443: i/o timeout"
                  },
                  {
                    "type": "*poll.DeadlineExceededError",
                    "error": "i/o timeout"
                  }
                ],
                "negotiated_protocol": "",
                "no_tls_verify": false,
                "peer_certificates": null,
                "server_name": "example.com",
                "t": 0,
                "tags": null,
                "tls_version": ""
              }
            }
          ]
        },
        "target_trace": {
          "server_name": "github.com",
          "iterations": [
            {
              "ttl": 1,
              "handshake": {
                "network": "",
                "address": "",
                "cipher_suite": "",
                "failure": "host_unreachable",
                "failure_chain": [
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*net.OpError",
                    "error": "read tcp [scrubbed]:48178->140.82.112.3:443: read: no route to host"
                  },
                  {
                    "type": "*os.SyscallError",
                    "error": "read: no route to host"
                  },
                  {
                    "type": "syscall.Errno",
                    "error": "no route to host"
                  }
                ],
                "negotiated_protocol": "",
                "no_tls_verify": false,
                "peer_certificates": null,
                "server_name": "github.com",
                "t": 0,
                "tags": null,
                "tls_version": ""
              }
            },
            {
              "ttl": 2,
              "handshake": {
                "network": "",
                "address": "",
                "cipher_suite": "",
                "failure": "host_unreachable",
                "failure_chain": [
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*net.OpError",
                    "error": "read tcp [scrubbed]:48192->140.82.112.3:443: read: no route to host"
                  },
                  {
                    "type": "*os.SyscallError",
                    "error": "read: no route to host"
                  },
                  {
                    "type": "syscall.Errno",
                    "error": "no route to host"
                  }
                ],
                "negotiated_protocol": "",
                "no_tls_verify": false,
                "peer_certificates": null,
                "server_name": "github.com",
                "t": 0,
                "tags": null,
                "tls_version": ""
              }
            },
            {
              "ttl": 3,
              "handshake": {
                "network": "",
                "address": "",
                "cipher_suite": "",
                "failure": "host_unreachable",
                "failure_chain": [
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*net.OpError",
                    "error": "read tcp [scrubbed]:48206->140.82.112.3:443: read: no route to host"
                  },
                  {
                    "type": "*os.SyscallError",
                    "error": "read: no route to host"
                  },
                  {
                    "type": "syscall.Errno",
                    "error": "no route to host"
                  }
                ],
                "negotiated_protocol": "",
                "no_tls_verify": false,
                "peer_certificates": null,
                "server_name": "github.com",
                "t": 0,
                "tags": null,
                "tls_version": ""
              }
            },
            {
              "ttl": 4,
              "handshake": {
                "network": "",
                "address": "",
                "cipher_suite": "",
                "failure": "host_unreachable",
                "failure_chain": [
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*net.OpError",
                    "error": "read tcp [scrubbed]:48212->140.82.112.3:443: read: no route to host"
                  },
                  {
                    "type": "*os.SyscallError",
                    "error": "read: no route to host"
                  },
                  {
                    "type": "syscall.Errno",
                    "error": "no route to host"
                  }
                ],
                "negotiated_protocol": "",
                "no_tls_verify": false,
                "peer_certificates": null,
                "server_name": "github.com",
                "t": 0,
                "tags": null,
                "tls_version": ""
              }
            },
            {
              "ttl": 5,
              "handshake": {
                "network": "",
                "address": "",
                "cipher_suite": "",
                "failure": "host_unreachable",
                "failure_chain": [
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*net.OpError",
                    "error": "read tcp [scrubbed]:48228->140.82.112.3:443: read: no route to host"
                  },
                  {
                    "type": "*os.SyscallError",
                    "error": "read: no route to host"
                  },
                  {
                    "type": "syscall.Errno",
                    "error": "no route to host"
                  }
                ],
                "negotiated_protocol": "",
                "no_tls_verify": false,
                "peer_certificates": null,
                "server_name": "github.com",
                "t": 0,
                "tags": null,
                "tls_version": ""
              }
            },
            {
              "ttl": 6,
              "handshake": {
                "network": "",
                "address": "",
                "cipher_suite": "",
                "failure": "host_unreachable",
                "failure_chain": [
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*net.OpError",
                    "error": "read tcp [scrubbed]:48244->140.82.112.3:443: read: no route to host"
                  },
                  {
                    "type": "*os.SyscallError",
                    "error": "read: no route to host"
                  },
                  {
                    "type": "syscall.Errno",
                    "error": "no route to host"
                  }
                ],
                "negotiated_protocol": "",
                "no_tls_verify": false,
                "peer_certificates": null,
                "server_name": "github.com",
                "t": 0,
                "tags": null,
                "tls_version": ""
              }
            },
            {
              "ttl": 7,
              "handshake": {
                "network": "",
                "address": "",
                "cipher_suite": "",
                "failure": "host_unreachable",
                "failure_chain": [
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*net.OpError",
                    "error": "read tcp [scrubbed]:48252->140.82.112.3:443: read: no route to host"
                  },
                  {
                    "type": "*os.SyscallError",
                    "error": "read: no route to host"
                  },
                  {
                    "type": "syscall.Errno",
                    "error": "no route to host"
                  }
                ],
                "negotiated_protocol": "",
                "no_tls_verify": false,
                "peer_certificates": null,
                "server_name": "github.com",
                "t": 0,
                "tags": null,
                "tls_version": ""
              }
            },
            {
              "ttl": 8,
              "handshake": {
                "network": "",
                "address": "",
                "cipher_suite": "",
                "failure": "host_unreachable",
                "failure_chain": [
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*net.OpError",
                    "error": "read tcp [scrubbed]:48260->140.82.112.3:443: read: no route to host"
                  },
                  {
                    "type": "*os.SyscallError",
                    "error": "read: no route to host"
                  },
                  {
                    "type": "syscall.Errno",
                    "error": "no route to host"
                  }
                ],
                "negotiated_protocol": "",
                "no_tls_verify": false,
                "peer_certificates": null,
                "server_name": "github.com",
                "t": 0,
                "tags": null,
                "tls_version": ""
              }
            },
            {
              "ttl": 9,
              "handshake": {
                "network": "",
                "address": "",
                "cipher_suite": "",
                "failure": "host_unreachable",
                "failure_chain": [
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*net.OpError",
                    "error": "read tcp [scrubbed]:48264->140.82.112.3:443: read: no route to host"
                  },
                  {
                    "type": "*os.SyscallError",
                    "error": "read: no route to host"
                  },
                  {
                    "type": "syscall.Errno",
                    "error": "no route to host"
                  }
                ],
                "negotiated_protocol": "",
                "no_tls_verify": false,
                "peer_certificates": null,
                "server_name": "github.com",
                "t": 0,
                "tags": null,
                "tls_version": ""
              }
            },
            {
              "ttl": 10,
              "handshake": {
                "network": "",
                "address": "",
                "cipher_suite": "",
                "failure": "host_unreachable",
                "failure_chain": [
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "host_unreachable"
                  },
                  {
                    "type": "*net.OpError",
                    "error": "read tcp [scrubbed]:48280->140.82.112.3:443: read: no route to host"
                  },
                  {
                    "type": "*os.SyscallError",
                    "error": "read: no route to host"
                  },
                  {
                    "type": "syscall.Errno",
                    "error": "no route to host"
                  }
                ],
                "negotiated_protocol": "",
                "no_tls_verify": false,
                "peer_certificates": null,
                "server_name": "github.com",
                "t": 0,
                "tags": null,
                "tls_version": ""
              }
            },
            {
              "ttl": 11,
              "handshake": {
                "network": "",
                "address": "",
                "cipher_suite": "",
                "failure": "generic_timeout_error",
                "failure_chain": [
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "generic_timeout_error"
                  },
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "generic_timeout_error"
                  },
                  {
                    "type": "*net.OpError",
                    "error": "read tcp [scrubbed]:48286->140.82.112.3:443: i/o timeout"
                  },
                  {
                    "type": "*poll.DeadlineExceededError",
                    "error": "i/o timeout"
                  }
                ],
                "negotiated_protocol": "",
                "no_tls_verify": false,
                "peer_certificates": null,
                "server_name": "github.com",
                "t": 0,
                "tags": null,
                "tls_version": ""
              }
            },
            {
              "ttl": 12,
              "handshake": {
                "network": "",
                "address": "",
                "cipher_suite": "",
                "failure": "generic_timeout_error",
                "failure_chain": [
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "generic_timeout_error"
                  },
                  {
                    "type": "*netxlite.ErrWrapper",
                    "error": "generic_timeout_error"
                  },
                  {
                    "type": "*net.OpError",
                    "error": "read tcp [scrubbed]:48290->140.82.112.3:443: i/o timeout"
                  },
                  {
                    "type": "*poll.DeadlineExceededError",
                    "error": "i/o timeout"
                  }
                ],
                "negotiated_protocol": "",
                "no_tls_verify": false,
                "peer_certificates": null,
                "server_name": "github.com",
                "t": 0,
                "tags": null,
                "tls_version": ""
              }
            }
          ]
        }
      }
    ]
  },
  "test_name": "tlsmiddlebox",
  "test_runtime": 29.293524585,
  "test_start_time": "2026-10-05 12:50:12",
  "test_version": "0.1.3"
}

```
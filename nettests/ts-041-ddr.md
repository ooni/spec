# Specification version number

2025-01-21-000

* _status_: experimental

# Specification name

ddr

# Test preconditions

* An internet connection

# Expected impact

Query the DDR protocol at the local recursive resolver, thus gathering information about DoE services in designated resolvers available and suggested to the user.

# Expected inputs

This experiment does not require inputs. It will by default query the system-configured recursive resolver. On Linux systems, this is the recursive resolver that is configured in the `/etc/resolve.conf` file.

This experiment can be configured to use a custom resolver. In this case, this resolver will be used. In this case the CustomResolver configuration property must be set to a domain or and IP-address, optionally providing a port. When no port is supplied, the default DNS port of 53 is used.

# Test description

The DDR (Discovery of Designated Resolvers) protocol is used for client to establish the connection to a encrypted DNS resolver. In most cases, DNS queries from the client are not configured with encryption by default, such as when only an IP is supplied by DHCP. With DDR a client can query a DNS recursive resolver for designated resolvers (encrypted resolvers). The recursive resolver will respond with a list of designated resolvers with their supported protocols.

This experiment issues such a DDR query and reports the result. 

# Expected output

## Semantics

The `test_keys` key of the measurement has such a structure:

```JSON
{
	"queries": [],
  "supports_ddr": false,
  "failure": null
}
```

The `supports_ddr` key is set to `true` only when the resolver returned a valid DDR response. It does not provide information about wether the designated resolver are valid.

The key `queries` follows the df-002-dnst format, with `svcb` key filled with the ddr responses.

A svcb record in an answer of the queries object looks like this:

```JSON
{
    "priority": 1,
    "target_name": "one.one.one.one.",
    "params":{
        "alpn":"h2,h3",
        "dohpath":"/dns-query{?dns}",
        "ipv4hint":"1.1.1.1,1.0.0.1",
        "ipv6hint":"2606:4700:4700::1111,2606:4700:4700::1001",
        "port":"443"
    }
}
```

The priority and target_name keys are directly from the SVCB record, where priority specifies the priority among the records at which use this record and target specifies the designated resolver. The key `params` is a map from string to string, that includes the keys that were specified for the SVCB record.
In the case of this example, the `params` map includes this information:

- `alpn`: The protocol this designated resolver uses, so in this case HTTP2 or HTTP3 for DNS over HTTPS
- `dohpath`: How the URL needs to be constructed to send a DoH query to the designated resolver.
- `ipv4hint`: How to reach the resolver via IPv4
- `ipv6hint`: How to reach the resolver via IPv6
- `port`: The port at which to reach the resolver

## Example output sample

```JSON

{
  "annotations": {
    "architecture": "amd64",
    "engine_name": "ooniprobe-engine",
    "engine_version": "3.25.0-alpha",
    "go_version": "go1.22.2",
    "platform": "linux",
    "vcs_modified": "true",
    "vcs_revision": "8ddec182caff7c1f9d49aa76a69d2fd10733e613",
    "vcs_time": "2024-12-19T14:59:47Z",
    "vcs_tool": "git"
  },
  "data_format_version": "0.2.0",
  "input": null,
  "measurement_start_time": "2025-01-31 09:58:28",
  "probe_asn": "AS3320",
  "probe_cc": "DE",
  "probe_ip": "127.0.0.1",
  "probe_network_name": "Deutsche Telekom AG",
  "report_id": "20250131T095828Z_ddr_DE_3320_n1_tNwEDtCeE2KK3ZGS",
  "resolver_asn": "AS42",
  "resolver_ip": "74.63.24.222",
  "resolver_network_name": "WoodyNet, Inc.",
  "software_name": "miniooni",
  "software_version": "3.25.0-alpha",
  "test_keys": {
    "queries": {
      "answers": [
        {
          "answer_type": "SVCB",
          "ttl": null,
          "svcb": {
            "priority": 2,
            "target_name": "dns.quad9.net.",
            "params": {
              "alpn": "h2",
              "dohpath": "/dns-query{?dns}",
              "ipv4hint": "9.9.9.9,149.112.112.112",
              "ipv6hint": "2620:fe::fe",
              "port": "443"
            }
          }
        },
        {
          "answer_type": "SVCB",
          "ttl": null,
          "svcb": {
            "priority": 2,
            "target_name": "dns.quad9.net.",
            "params": {
              "alpn": "h2",
              "dohpath": "/dns-query{?dns}",
              "ipv4hint": "9.9.9.9,149.112.112.112",
              "ipv6hint": "2620:fe::fe",
              "port": "443"
            }
          }
        }
      ],
      "engine": "udp",
      "failure": null,
      "hostname": "_dns.resolver.arpa.",
      "query_type": "SVCB",
      "raw_response": "xnuBAAABAAIAAAAEBF9kbnMIcmVzb2x2ZXIEYXJwYQAAQAABwAwAQAABAAAAPAA/AAEDZG5zBXF1YWQ5A25ldAAAAQAEA2RvdAADAAIDVQAEAAgJCQkJlXBwcAAGABAmIAD+AAAAAAAAAAAAAAD+wAwAQAABAAAAPABSAAIDZG5zBXF1YWQ5A25ldAAAAQADAmgyAAMAAgG7AAQACAkJCQmVcHBwAAYAECYgAP4AAAAAAAAAAAAAAP4ABwAQL2Rucy1xdWVyeXs/ZG5zfQNkbnMFcXVhZDkDbmV0AAABAAEAAAA8AAQJCQkJwM0AAQABAAAAPAAElXBwcMDNABwAAQAAADwAECYgAP4AAAAAAAAAAAAAAP4AACkE0AAAgAAAAA==",
      "resolver_hostname": null,
      "resolver_port": null,
      "resolver_address": "192.168.10.1:53",
      "t0": 0.000070584,
      "t": 0.013585498,
      "tags": null
    },
    "supports_ddr": true,
    "failure": null
  },
  "test_name": "ddr",
  "test_runtime": 0.013683332,
  "test_start_time": "2025-01-31 09:58:28",
  "test_version": "0.1.0"
}

```
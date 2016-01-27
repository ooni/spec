# DNSTest template data format

Data Format Version: 0.2.0

This is the specification of the data format that every test that is
based on ooni.templates.dnst.DNSTest shall be using.

Third party tests that run DNS related measurements SHOULD also be using such
data format.

## Specification

```
"queries": [
    {
        "failure": "null or a string representing the failure",

        "hostname":
            "The hostname used in the DNS query. For PTR lookups this will be the reversed "
            "ipv4 address in the form: xxx.xxx.xxx.xxx.in-addr.arpa.",

        "query_type": "A | MX | PTR | SOA",

        "resolver_hostname":
            "The hostname of the DNS resolver being used",

        "resolver_port":
            "The port of the DNS resolver being used"

        "answers": [
            {
                "answer_type": "A | MX | PTR | SOA | CNAME",

                "ipv4":
                    "(only for A answers) The dotted quad of the IPV4 address",

                "ttl": "The ttl of the Returned resource record",

                "hostname":
                    "(only for PTR, SOA and CNAME answers)"
                    "For PTR lookups it is the hostname that points back to the queried IP."
                    "For CNAME lookups it is the hostname of the alias for the IP."
                    "For SOA answers it is the hostname of the nameserver "
                    "responsible for the data of this zone."

                "responsible_name":
                    "(only for SOA answers) The mailbox of the person responsible "
                    "for this zone."

                "serial_number":
                    "(only for SOA answers) Version number of the original copy of "
                    "the zone."

                "refresh_interval":
                    "(only for SOA answers) The time interval before which this "
                    "zone should be refreshed."

                "retry_interval":
                    "(only for SOA answers) The time interval that should be "
                    "elapsed before the zone should be retried in case of failure."

                "minimum_ttl":
                    "(only for SOA answers) The minimum ttl to be exported with "
                    "any record from this zone."

                "expiration_limit":
                    "(only for SOA answers) The time after which this zone should "
                    "no longer be authoritative."
            }
        ],


    }
]
```

## Example output

```
{
    "bucket_date": "2015-11-23",
    "data_format_version": "0.2.0",
    "id": "e6f6257f-e7c2-48fa-8345-b7ed055ab1d2",
    "input": "198.175.124.185",
    "options": [
        "-f",
        "citizenlab-urls-global.txt",
        "-T",
        "dns-server-jo.txt"
    ],
    "probe_asn": "AS8376",
    "probe_cc": "JO",
    "probe_ip": "127.0.0.1",
    "report_filename": "2015-11-23/20151123T161428Z-JO-AS8376-dns_consistency-F1KI1WusW4c1T6OGyQDgHJjaSQ1bfpqV2G39bpmuHiLAJnse8R1F44vdRuTz6nO4-0.1.0-probe.json",
    "report_id": "F1KI1WusW4c1T6OGyQDgHJjaSQ1bfpqV2G39bpmuHiLAJnse8R1F44vdRuTz6nO4",
    "software_name": "ooniprobe",
    "software_version": "1.3.1",
    "test_helpers": {
        "backend": "8.8.8.8:53"
    },
    "input_hashes": [
        "0055f0881fba857d8b48123017d7aec83014e89f057e44b66107f657ec5e2eab"
    ],
    "probe_city": null,
    "backend_version": "1.1.4",
    "test_keys": {
        "control_resolver": "8.8.8.8:53",
        "errors": {
            "212.118.0.1": "no_answer",
            "212.118.0.2": "no_answer",
            "212.38.128.3": "dns_lookup_error",
            "217.144.6.6": "no_answer",
            "8.8.8.8:53": "no_answer",
            "80.90.160.135": "dns_lookup_error",
            "80.90.160.172": "dns_lookup_error",
            "81.28.112.2": "dns_lookup_error"
        },
        "failed": [
            "80.90.160.172",
            "8.8.8.8:53",
            "212.118.0.2",
            "80.90.160.135",
            "212.38.128.3",
            "212.118.0.1",
            "217.144.6.6",
            "81.28.112.2"
        ],
        "inconsistent": [
        ],
        "queries": [
            {
                "answers": [],
                "failure": "no_answer",
                "hostname": "198.175.124.185",
                "query_type": "A",
                "resolver_hostname": "8.8.8.8",
                "resolver_port": 53
            },
            {
                "answers": [],
                "failure": "deferred_timeout_error",
                "hostname": "198.175.124.185",
                "query_type": "A",
                "resolver_hostname": "212.38.128.3",
                "resolver_port": 53
            },
            {
                "answers": [],
                "failure": "no_answer",
                "hostname": "198.175.124.185",
                "query_type": "A",
                "resolver_hostname": "217.144.6.6",
                "resolver_port": 53
            },
            {
                "answers": [],
                "failure": "deferred_timeout_error",
                "hostname": "198.175.124.185",
                "query_type": "A",
                "resolver_hostname": "81.28.112.2",
                "resolver_port": 53
            },
            {
                "answers": [],
                "failure": "deferred_timeout_error",
                "hostname": "198.175.124.185",
                "query_type": "A",
                "resolver_hostname": "80.90.160.135",
                "resolver_port": 53
            },
            {
                "answers": [],
                "failure": "deferred_timeout_error",
                "hostname": "198.175.124.185",
                "query_type": "A",
                "resolver_hostname": "80.90.160.172",
                "resolver_port": 53
            },
            {
                "answers": [],
                "failure": "no_answer",
                "hostname": "198.175.124.185",
                "query_type": "A",
                "resolver_hostname": "212.118.0.1",
                "resolver_port": 53
            },
            {
                "answers": [],
                "failure": "no_answer",
                "hostname": "198.175.124.185",
                "query_type": "A",
                "resolver_hostname": "212.118.0.2",
                "resolver_port": 53
            }
        ],
        "start_time": 1448291668.0,
        "successful": []
    },
    "test_name": "dns_consistency",
    "test_runtime": 0.0837070942,
    "test_start_time": "2015-11-23 16:14:28",
    "test_version": "0.6"
}
```

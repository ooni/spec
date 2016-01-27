# Specification version number

0.2.0

# Specification name

DNS Consistency

# Test preconditions

  * An internet connection
  * A unfiltered connection to a DNS resolver that is not performing censorship

For reporting to the backend to work that it is possible for the probe to
establish a connection to the Tor network.

# Expected impact

Ability to detect if A DNS queries for a certain hostname are being tampered with.

# Expected inputs

  * A list of hostnames to be tested for censorship
  * A list of DNS resolvers to be tested for censorship
  * A DNS resolver that is not being tampered with (control_resolver)

The list of hostnames should be in a text file and separated by newline.

Example:

    one.example.com
    two.example.com
    three.example.com

The list of DNS resolvers to test for tampering shold be in a text file as
dotted quads separated by a newline:

Example:

    1.1.1.1
    2.2.2.2
    3.3.3.3

# Test Description

For each hostname to be tested we do the following:

We perform an A DNS query (via UDP) to the control resolver. The answer to such
query is called the control answer.

For each DNS resolver to be tested we perform an A DNS query for the domain in
question. We then compare this answer (experiment answer) with the control
answer.

If the two have a common IPV4 address then the hostname is not considered to be
tampered with the resolver in question (tampering: False)

If they do not have commonalities we take the first IPV4 address in the control
answer and the first IPV4 address in the experiment answer and do a reverse
lookup. If the two reverse lookups match (the PTR record points to the same
hostname), we take note of this (tampering: "reverse_match").

In any other case we mark the result as: tampering: True.

# Expected output

## Parent Data format

df-002-dnst

## Semantics

The following extra fields will be present in every measurement entry.

```
{
    "successful": [
        "The list of addresses of the resolvers that provided a consistent"
        "answer to our query."
    ],
    "failures": [
        "The list of addresses that failed to resolve the query."
        "Note: in the case of NXDOMAIN these will turn up as failures."
    ],
    "inconsistent": [
        "The list of addresses that returned an inconsistent result"
    ],
    "errors": {
        "RESOLVER_IP": "error string of the failure"
    }

}
```

## Possible conclusions

That the DNS resolver in question has provided a false response to a DNS Query.

## Expected post-processing efforts

## Example output sample

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

# Privacy considerations

This test does not inherently risk leaking user information.

# Packet capture considerations

We do not do any packet capturing, this test only requires to be able to create
UDP sockets.

# Notes

Sites that do geolocation based load balancing via DNS will report a different
set of IPv4 addresses depending on the source of the DNS request. For this
reason we also do a reverse lookup to check to see if the domain pointers of
the IP addresses match.
This means of seeding out false positive, though, is also not that effective
since in some circumstances also the PTR record will point to a different
domain name.

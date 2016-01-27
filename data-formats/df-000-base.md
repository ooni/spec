# OONI Data formats

The output of test is the composition of:

    +---------------------------+
    |   Base data format        |
    +---------------------------+
    | Test template data format |
    +---------------------------+
    | Test specific data format |
    +---------------------------+

In this directory shall go only the data format specifications of Test
templates. The Test specific data formats should go in the specification of the
test.

Data produced by the ooniprobe client can be either in YAML or JSON format.

YAML is used when writing reports to the users filesystem, while JSON is used
as a format for the published processed reports.

# Base test data format

This specification is of the basic data format common to all ooniprobe test
outputs.

Every entry contains the following common fields. The `test_keys` key will
contain instead all the keys that are specific to the test in question.

The JSON data format is made up of a series of JSON documents separated by
newline characters.

Data Format Version: 0.2.0

## Specification

```
{
    "input": "If the test takes an input this will contain the value of it"
        " these can be for example URLs, hostnames, IPs, etc.",

    "input_hashes": "A list of the SHA256 hash of encoded "
        "as hex of the inputs to this test.",

    "id": "This is an identifier of this particular measurement",

    "bucket_date": "A date in the format of %Y-%m-%d that indicates "
        "when the report was processed by the data pipeline"

    "data_format_version": "0.1.0|0.2.0",

    "report_filename": "{bucket_date}/{timestamp as '%Y%m%dT%h%M%sZ'}-{probe_cc}-{probe_asn}-{test_name}-{report_id}-{data_format_version}-{probe|backend}.json",

    "options": ["A list of options passed to the test as command line arguments"],

    "probe_asn": "The AS Number of the probe (prefixed by AS, ex. AS1234) "
        "or AS0 if includeasn is set to false.",

    "probe_cc": "The two letter country code of the probe or ZZ if "
        "inlcudecountry is set to false.",

    "probe_ip": "The IPv4 address of the probe or 127.0.0.1 if "
        "includeip is set to false.",

    "probe_ip": "The name of the city of the probe or null if "
        "includecity is set to false.",

    "report_id": "20140130T111423Z_ELNkuajQzUWfktBupbfZUxseQDczEvEaIhtciykhoLSuiNiCCV",

    "software_name": "The name of the software that has generated "
        "such report (ex. ooniprobe)",

    "software_version": "The version of the software used to generate this report",

    "backend_version": "The version of the backend that collected this measurement",

    "test_helpers": null,

    "test_name": "The name of the test that generated "
        "this measurement (ex. http_requests)",

    "test_version": "",

    "test_runtime": null,

    "test_start_time": "Timestamp of when the measurement was performed in "
        "UTC time coordinates (ex. 2015-08-24 12:02:23)",

    "test_keys": {
        "The keys that are specific to the test"
    }
}
```

# Example output

```
{
    "bucket_date": "2015-11-22",
    "data_format_version": "0.2.0",
    "id": "07873c37-9441-47e3-93b8-94db10444c64",
    "input": "http://example.com/",
    "options": [
        "-f",
        "37e60e13536f6afe47a830bfb6b371b5cf65da66d7ad65137344679b24fdccd1"
    ],
    "probe_asn": "AS0",
    "probe_cc": "CH",
    "probe_ip": "127.0.0.1",
    "report_filename": "2015-11-22/20151122T103202Z-CH-AS0-http_requests-XsQk40qrhgvJEdbXAUFzYjbbGCBuEsc1UV5RAAFXo4hysiUo3qyTfo4NTr7MjiwN-0.1.0-probe.json",
    "report_id": "XsQk40qrhgvJEdbXAUFzYjbbGCBuEsc1UV5RAAFXo4hysiUo3qyTfo4NTr7MjiwN",
    "software_name": "ooniprobe",
    "software_version": "1.3.1",
    "backend_version": "1.1.4",
    "test_helpers": {},
    "input_hashes": [
        "37e60e13536f6afe47a830bfb6b371b5cf65da66d7ad65137344679b24fdccd1"
    ],
    "test_name": "http_requests",
    "test_runtime": 0.1842639446,
    "test_start_time": "2015-11-22 10:32:02",
    "test_version": "0.2.4"
    "test_keys": {
    },
}
```

# Error strings

Here are the mappings between twisted errors and the corresponding ooniprobe
error_string:

* twisted.internet.error.ConnectionRefusedError: `connection_refused_error`

* socket.gaierror: `address_family_not_supported_error`

* twisted.internet.error.DNSLookupError: `dns_lookup_error`

* twisted.internet.error.TCPTimedOutError: `tcp_timed_out_error`

* twisted.internet.error.ConnectionDone: `connection_done`

* twisted.web._newclient.ResponseNeverReceived: `response_never_received`

* twisted.internet.error.TimeoutError: `generic_timeout_error`

* twisted.internet.defer.TimeoutError: `deferred_timeout_error`

* txsocksx.errors.ServerFailure: `socks_server_failure`

* txsocksx.errors.ConnectionNotAllowed: `socks_connection_not_allowed`

* txsocksx.errors.NetworkUnreachable: `socks_network_unreachable`

* txsocksx.errors.HostUnreachable: `socks_host_unreachable`

* txsocksx.errors.ConnectionRefused: `socks_connection_refused`

* txsocksx.errors.TTLExpired: `socks_ttl_expired`

* txsocksx.errors.CommandNotSupported: `socks_command_not_supported`

* txsocksx.errors.AddressNotSupported: `socks_address_not_supported`

* txsocksx.errors.SOCKSError: `socks_error`

* This will be the error message if the task has timed out: `task_timed_out`

* Every other failure: 'unknown_failure %s' % str(failure.value)

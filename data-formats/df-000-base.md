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

    "annotations": "Optional map of key-value annotations to the report that"
            "provide metadata to this measurement. Apps SHOULD always add to the map of"
            "annotations the platform, which could be one of: macos, linux, windows, ios, android, lepidopter. "
            "Users may want to add more annotations",

    "report_filename": "{bucket_date}/{timestamp as '%Y%m%dT%h%M%sZ'}-{probe_cc}-{probe_asn}-{test_name}-{report_id}-{data_format_version}-{probe|backend}.json",

    "options": ["A list of options passed to the test as command line arguments"],

    "probe_asn": "The AS Number of the probe (prefixed by AS, ex. AS1234) "
        "or AS0 if includeasn is set to false.",

    "probe_cc": "The two letter country code of the probe or ZZ if "
        "inlcudecountry is set to false.",

    "probe_ip": "The IPv4 address of the probe or 127.0.0.1 if "
        "includeip is set to false.",

    "probe_city": "The name of the city of the probe or null if "
        "includecity is set to false.",

    "report_id": "20140130T111423Z_ELNkuajQzUWfktBupbfZUxseQDczEvEaIhtciykhoLSuiNiCCV",

    "software_name": "The name of the software that has generated "
        "such report (ex. ooniprobe)",

    "software_version": "The version of the software used to generate this report",

    "backend_version": "The version of the backend that collected this measurement",

    "test_helpers": {"test_specific_test_helper_name": "The address of the test helper used. (Note that the name used for the helper is not necessarily the helper name according to the bouncer, and is typically test specific; e.g. WebConnectivity currently uses 'backend' to refer to the 'web-connectivity' helper."},

    "test_name": "The name of the test that generated "
        "this measurement (ex. http_requests)",

    "test_version": "",

    "test_runtime": null,

    "measurement_start_time": "Timestamp of when the measurement was performed in "
        "UTC time coordinates (ex. 2015-08-24 12:02:23) (Note: ooniprobe <= 1.4.0 generates skewed timing information)",

    "test_start_time": "Timestamp of when the test was started in "
        "UTC time coordinates (ex. 2015-08-24 12:02:23) (Note: ooniprobe <= 1.4.0 generates skewed timing information)",


    "test_keys": {
        "The keys that are specific to the test"
    },

    "signature": "The signature of the data object, defined below.",
}
```

# Example output

```JSON
{
    "annotations": {"platform": "macos"},
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
    "test_version": "0.2.4",
    "test_keys": {
    },
    "signature": "XXXTODO",
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

* twisted.internet.error.ConnectError: `connect_error`

* twisted.internet.error.ConnectionLost: `connection_lost_error`

* twisted.internet.defer.TimeoutError: `deferred_timeout_error`

* twisted.names.error.DNSNameError: `dns_name_error`

* twisted.names.error.DNSServerError: `dns_name_failure`

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


# Signatures

Test data objects are signed by a probe-specific key, so that OONI users setting
up trustworthy probes (for which they might know additional metadata) can access
the measurements those specific probes generated, in such a way that the origin
of the measurement cannot be forged.

The signatures should provide the following properties:
- measurements produced by the same probe should not be linkable without
  knowledge of the probe's public key;
- the signatures should be verifiable independently of content-preserving
  transformations applied to the object's representation (e.g. reindenting the
  JSON, converting it to YAML or to a binary format, ...);
- it should be possible to selectively redact fields from the data object
  without breaking the signature, so as to be able to redact privacy-critical
  information *a posteriori* if it ever is necessary.


Given those design goals, the signatures are specified as
`ECVRF(objecthash(data))`; [objecthash] is an encoding-agnostic hash
construction for JSON-like objects -- which is applicable to JSON, YAML,
ProtoBuf, ... -- and [ECVRF] is a Verifiable Random Function constructed over
elliptic curves; ECVRF is instanciated as XXXTODO.

[ECVRF]: https://tools.ietf.org/html/draft-goldbe-vrf-01#section-5
[objecthash]: https://github.com/benlaurie/objecthash


## Privacy considerations

### “Always-on” signatures

To avoid drastically reducing the anonymity set of probes which belong to an
organisation using the signature feature, all probes should be signing their
measurement data.  As an extreme example, if only a single probe was signing its
measurements, they could be trivially linked together.

There are two possible designs here:
- either all probes generate a persistent probe key if it is absent, and use it
  to sign measurements,
- or probes that do not have a persistent probe key generate an ephemeral key
  each time they sign a measurement.

Systematically generating a persistent key means that it is possible to set up a
probe (without doing anything special) and later obtain its public key to be
able to access its measurements; on the other hand, a break in ECVRF (including
the potential future where the adversary has sufficiently-large quantum
computers) could result in measurements being linkable for all probes (if they
all use persistent keys).

XXXTODO: Is there a construction for signatures that is unconditionally hiding?
         That would let us have our cake and eat it too  :)


### Fields redaction

If we ever define fields which we expect to redact at some point, we should
decorate them with a random string (256b of entropy) to guarantee that the
redacted data cannot be deduced from its hash.

This is a [known issue](https://github.com/benlaurie/objecthash#redactability),
and decorating with random strings guarantees that the hash cannot be reverted.


XXXTODO: Could we use an ObjectHash variant that uses the VRF in such a way
         that only the probe can compute the hash of the object (and inner
         values), preventing redacted fields from being reverted?

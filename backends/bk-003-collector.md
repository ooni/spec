# OONI collector specification

* version: 2.0.0
* date: 2019-03-13
* author: Arturo Filastò, Aaron Gibson, Simone Basso

This document aims at providing a functional specification of the OONI collector. It
has been forked from version 1.4.0 of [bk-001-ooni-backend.md](bk-001-ooni-backend.md)
and, as of version 2.0.0, is such that an implementation of this specification that
implements all the deprecated behavior will be compatible with version 1.4.0.

# 1.0 System overview

The collector exposes an HTTP API allowing OONI probes to submit the results
of their measurements. Measurement submitted to a OONI collector will be
archived, processed, and published by OONI. Modern OONI probes represent a
set of logically-related measurements (a *report*) as a set of separate
JSON documents. Legacy OONI probes represent a single report consisting of
several measurements as a single YAML document. Users still using the old
YAML based format are encouraged to upgrade to JSON ASAP. A server side
implementation of the collector MUST support the JSON format.

It is outside of the scope of this section to define:

1. the way in which a OONI probe discovers the collector API endpoint

2. whether the collector should push measurements to some other component for
archival, processing, and publishing, or whether a scraper component would
be responsible for gathering measurements from OONI collectors.

The collector MUST be exposed as an HTTPS service. It MAY also be exposed as
a Tor onion service. A [legacy document](
https://ooni.torproject.org/docs/architecture.html#why-tor-hidden-services)
explains why the OONI project originally chose to allow for both HTTPS
and Tor onion service services.

# 2.0 Threat model

The collector MUST provide end-to-end encryption and authentication between
the OONI probe and itself. Therefore, a malicious actor won't be able to update
test results that they have not created.

It is outside of the scope of the collector to provide blocking resistance or
to conceal to a passive network observer the fact that they are communicating to
a collector. Such properties are to be provided by other software, e.g. Tor.

# 3.0 API

Unless otherwise stated all of the network operations below MAY be performed
either via HTTPS or via a Tor onion service.

In the most general case, you create a report (see 3.1), update it by adding
measurements (see 3.2), then close it (see 3.3).

When the report consists of a single measurement entry, however, you can use
a simplified flow to perform all these operations together in a single
API call (see 3.4).

A report that has successfully be open is in the OPEN state. A OONI collector
should record the last time a report has been updated, and close a report
that has been inactive for too much time. An implementation is free to choose
any threshold for closing stale, OPEN reports; however, this threshold
SHOULD NOT be smaller than two hours for compatibility with existing
implementations of the OONI collector.

## 3.1 Create a new report

When a probe starts a test it will *create* a new report by sending a `POST`
request conforming to the following specification:

    POST /report

    {
     'content':
        (optional, deprecated) `string` it is optionally possible to create a report with
        already some data inside of it. MUST be a serialized JSON or YAML depending
        on the value of the 'format' key.

     'data_format_version':
        `string` describing the version of the data format. The current value
        of the data format version is "0.2.0".

     'format':
        `string` that must be either "json" or "yaml" and is used to identify the
        format of the report content.

     'input_hashes':
        (optional, deprecated) `list` of hex encoded sha256sum of the contents
        of the inputs we are using for this test. This field is required if the
        collector only accepts certain inputs.

     'probe_asn':
        `string` the Autonomous System Number of the network the test is
        related to prefixed by "AS" (ex. "AS1234"). This field MUST
        match this regex: `^AS[0-9]{1,10}$`.

     'probe_cc':
        `string` the two-letter country code of the probe as defined in
        ISO3166-1 alpha-2, or ZZ when undefined (ex. "IT"). This field MUST
        match this regexp: `^[A-Z]{2}$`.

     'probe_ip':
        (optional, deprecated) `string` the IP address of the OONI probe client.

     'software_name':
        `string` the name of the software that is creating a report (ex. "ooni-probe")
        that MUST match this regexp: `^[0-9A-Za-z_.+-]+$`.

     'software_version':
        `string` the version of the software creating the report (ex. "0.0.10-beta")
        that MUST match this regexp: `^[0-9A-Za-z_.+-]+$`.

     'test_name':
        `string` the name of the test performing the network measurement that
        MUST match this regexp: `^[a-zA-Z0-9_\\- ]+$`.

     'test_helper':
        (optional, deprecated) `string` the name of the required test_helper for this test.

     'test_start_time':
        (optional) `string` timestamp in UTC of when the test was started using
        the format "%Y-%m-%d %H:%M:%S"

     'test_version':
        `string` the version of the test performing the network measurement that
        MUST match the same regexp of 'software_version'.
    }

Where the above is intended as a specification for generating a compliant
serialized JSON object.

The `Content-Type` header is not required, but SHOULD be properly set for
additional clarity. In such case, we recommend setting the `Content-Type` to
`application/json` or `application/json; charset=utf-8`.

Upon receiving a request to create a report, the collector:

1. MUST fail with `4xx` if the JSON does not parse, it is not an object,
   any required field is missing and/or if any present field has an invalid value.

2. MUST fail with `4xx` if the request is not compliant with its policies.

3. SHOULD fail with `5xx` if the `content` field is present, or if the
   `test_helper` field is present, or if the `format` is "yaml", unless the
   implementor really wants to support now-historical OONI probe implementations.

4. MUST fail with `5xx` if it cannot generate the report ID (see below) or
   in case of other failures.

5. SHOULD exercise care to avoid logging the `probe_ip` field, if set.

6. if everything is okay, MUST return a `200` response with the body
   described below.

In case of error, the collector MAY return a JSON body. In case of
success, it MUST return a JSON body generated in compliance with
the following specification:

    {
      'backend_version':
        `string` containing the version of the backend. This version MUST
        match the regex provided above for 'software_version'.

      'report_id':
        `string` report identifier. The format of this field is not
        specified, except that is MUST be a valid UTF-8 string, of
        course. The client MUST NOT make any assumption with respect
        to the structure of this field. It MUST treat this field as
        an opaque identifier. The only requirement is that it SHOULD
        be at least 256 bits and MUST be generated with a CSPRNG.

      'test_helper_address':
        (conditional, deprecated) `string` the address of a test helper that
        the client requested using the `test_helper_name` field.

      'supported_formats':
        `list` of strings detailing what are the supported formats for
        submitted reports. Allowed values are "json" and "yaml".
    }

New collector implementations MUST&mdash;and existing ones
SHOULD&mdash;set `Content-Type` using a content type value
indicating JSON (as mentioned above when discussing what
`Content-Type` value the client should use).

Upon receiving a response, the client:

1. MUST verify that the status is `200` before continuing

2. SHOULD check whether the `Content-Type` indicates that
   the server returned a JSON document.

3. if it is a `yaml` client, it MUST make sure that the backend is
   supporting such format

4. MUST save the report ID for using it later

The following example shows how opening a report looks like from
the point of view of a modern collector client (where the JSON
messages have been edited for readability):

```
> POST /report HTTP/1.1
> Host: collector-sandbox.ooni.io
> Accept: */*
> Content-Type: application/json
> Content-Length: 243
> 
>{
>  "data_format_version":"0.2.0",
>  "format":"json",
>  "input_hashes":[],
>  "probe_asn":"AS30722",
>  "probe_cc":"IT",
>  "software_name":"mkcollector",
>  "software_version":"0.0.1",
>  "test_name":"dummy",
>  "test_version":"0.0.1"
>}
< HTTP/1.1 200 OK
< Server: nginx
< Date: Wed, 13 Mar 2019 13:19:42 GMT
< Content-Type: application/json; charset=utf-8
< Content-Length: 152
< Connection: keep-alive
< 
<{
<  "backend_version":"2.0.0-alpha",
<  "report_id":"20190313T131942Z_AS30722_dU70oZPs80d5E21z8Ef6GXel6CwsdLoXvDk44Fsajv1LDLOIeI",
<  "supported_formats":["json"]
<}
```

## 3.2 Update a report

Updating a report means appending a measurement to the report. A probe SHOULD do
that within a reasonable time frame after the measurement has terminated. Also,
as stated above, a collector SHOULD NOT close an open, stale report before two
hours of inactivity. Also, the probe implementation SHOULD record the
elapsed time between when it opened a report and when it is updating it, and
open a new report if the update operation fails and the elapsed time is greater
than one hour.

To update a report, the probe issues a request compliant with the following:

    POST /report/${report_id}

    {
     content:
       When the report is in YAML, this is a string. Otherwise, this is
       a JSON object. In both cases, the content of this field MUST
       follow the df-000-base.md specification (see below).

     'format':
        `string` either "json" or "yaml".
    }

Upon receiving this request, the collector:

1. MUST check whether `${report_id}` is a valid report ID and reject
   the request with a `4xx` status otherwise.

2. MUST reject the request with a `4xx` status if the `format`
   is "yaml" and it is not handling YAML.

3. MUST reject the request with a `4xx` if the JSON/YAML does not
   parse or the JSON is not an object.

4. MUST parse `content` into a JSON/YAML to verify that the top-level
   fields are compliant with [df-000-base.md](
   ../data-formats/df-000-base.md) and otherwise return a `4xx`
   status to the client.

5. MAY parse `test_keys` fields and return a `4xx` status if
   such it finds some field with an invalid value.

6. SHOULD write the measurement to persistent storage or to some
   database before returning `200` to the client, and SHOULD
   make sure that it successfully saved the measurement (e.g. by
   checking the return value of `fclose`). In writing the
   measurement, the collector SHOULD NOT transform it to the
   maximum possible extent, unless such transformation is
   known to be harmless. Saving the original bytes sent by
   the client SHOULD be preferred to reserializing the
   parsed measurement and saving that.

7. MUST reset the report-specific timer used for automatically
   closed OPEN reports that have become stale.

8. MAY submit the measurement to some pipeline speed processing
   layer, but this operation MUST NOT have an impact onto the
   HTTP status returned to the client, and SHOULD be performed
   asynchronously such that the response is returned to the
   client as quickly as possible.

9. if everything is okay, returns `200` to the client (see below).

For backwards compatibility with the existing implementation, the
`200` status SHOULD include this body along with a compliant
`Content-Type` header value indicating JSON (see above):

```JSON
{"status": "success"}
```

## 3.3 Closing a report

This request is done by a probe to tell the backend that they have finished
running the test and the report can be considered done:

`POST /report/$report_id/close`

## 3.4 Submitting single measurements using a single API call

When you have single-entry reports, you can submit them by `POST`ing onto
the `/measurement` endpoint:

`POST /measurement`

This API only works for reports expressed in JSON format. The request body
should be the measurement entry. The following
JSON document is an example body sent to the `/measurement` API generated by
measurement-kit where the `test-keys` key has been omitted for brevity:

```JSON
{
    "data_format_version": "0.2.0",
    "input": "",
    "measurement_start_time": "2016-10-12 10:10:16",
    "probe_asn": "AS0",
    "probe_cc": "ZZ",
    "probe_ip": "127.0.0.1",
    "software_name": "measurement_kit",
    "software_version": "0.3.2",
    "test_keys": {
    },
    "test_name": "http_invalid_request_line",
    "test_runtime": 5.06855893135071,
    "test_start_time": "2016-10-12 10:10:16",
    "test_version": "0.0.1"
}
```

When the request is successful the backend shall return:

`Status code: 200 (OK)`

Message:

```JSON
{
"report_id": "XXXX",
"measurement_id": "YYYY"
}
```

Otherwise, it shall return:

`Status code: 500 (Internal Server Error)`

Message:

```JSON
{"error": "error string"}
```

## 4.0 Report life-cycle

When a report is created (section 3.1) it should be marked as NEW and a
timestamp should be recorded. If a report was rejected, it is discarded.

Once it is updated (section 3.2) it should be marked as ACTIVE. An ACTIVE
report can be updated with new data. The collector must keep track of the last
time a certain report is updated with new and valid data.

A report is considered CLOSED when either the probe instructs the collector to
close the report (section 3.3) or when a report is in ACTIVE state and has
not been updated with valid data for more than 2 hours.

## 2.5 Report publishing and cleaning

Once a report is closed it should be made available to the public for download
and analysis. This shall happen as soon as a report reaches the CLOSED state
(either because the user closed it or because it entered a stale state).

Reports should be published to:

`https://ooni.torproject.org/reports/` **reportFormatVersion** `/` **CC** `/`

Requesting such URL may also result in a 302 to the location of reports for
that specific country.

Where CC is the two letter country code as specified by ISO 31666-2.

For example the reports for Italy (CC is it) of the reportVersion 0.1 may be
found in:

https://ooni.torproject.org/reports/0.1/IT/

This directory shall contain the various reports for the test using the
following convention:

test name - timestamp in ISO8601 format - probe AS number - probe|backend.yamloo

The timestamp is expressed using ISO 8601 including seconds and with no : to
delimit hours, minutes, days.

Such date is the time in which the report was created and must be set by the
backend.

Like so:

YEAR - MONTH - DAY T HOURS MINUTES SECONDS Z

The time is always expressed in UTC.

If a collision is detected then an int (starting with 1) will get appended to
the test.

For example if two report that are created on the first of January 2012 at Noon
(UTC time) sharp from MIT (AS3) will be stored here:

https://ooni.torproject.org/reports/0.1/US/http_test-2012-01-01T120000Z-AS3-probe.yamloo
https://ooni.torproject.org/reports/0.1/US/http_test-2012-01-01T120000Z-AS3-probe.1.yamloo

Implementation notes:
The task of publishing a report should be made modular so that we can replace
the publishing mechanism if we discover the limitations of this system (not
infinite disk space).

The basic implementation shall just scp the files to a machine that is
configurable by config file.

?? Question:
How does this integrate into the m-lab infrastructure?

How will this work when some reports results are stored on m-lab and some are
not?

# OONI collector specification

* version: 2.0.0
* date: 2019-03-13
* author: Simone Basso (v2.0.0); Arturo Filastò, Aaron Gibson (v1.4.0)

This document aims at providing a functional specification of the OONI collector. It
has been forked from version 1.4.0 of [bk-001-ooni-backend.md](bk-001-ooni-backend.md)
and, as of version 2.0.0, is such that an implementation of this specification that
implements all the deprecated behavior will still be compatible with version 1.4.0 of
[bk-001-ooni-backend.md](bk-001-ooni-backend.md).

# 1.0 System overview

The collector exposes an HTTP API allowing OONI probes to submit the results
of their measurements. The client and the server MUST NOT assume a keep
alive semantics for the HTTP connections.

New server implementations MUST support `Content-Encoding: gzip` to
compress request bodies. OONI production clients MUST NOT use this
feature until all OONI's production servers server are known to have
implemented it. Third party clients should either coordinate with
us or be prepared to retry without compression.

New implementations MUST properly set `Content-Type`. Server side
implementatons MUST be able to deal with legacy clients that possibly
do not correctly set the `Content-Type`.

Measurement submitted to a OONI collector will be archived, processed, and
published by OONI. How that will happen is out of the scope of this document
and is part of the design of the OONI pipeline. You may also want to read
[about our data policy](https://ooni.io/about/data-policy/).

Modern OONI probes represent a set of logically-related measurements
(a *report*) as a set of separate JSON documents each containing a
JSON object. Legacy OONI probes represent a report as a single YAML
document containing a header and several YAML objects. Users still using
the old YAML based format are encouraged to upgrade to JSON ASAP. A
server side implementation of the collector MUST support the JSON format.

The collector MUST be exposed as an HTTPS service. It MUST also be exposed as
a Tor onion service as long as legacy OONI probe clients use it. The need
to expose an onion service will be rediscussed when legacy OONI probe
clients will no longer be relevant. A [legacy document](
https://ooni.torproject.org/docs/architecture.html)
explains why the OONI project originally chose to allow for both HTTPS
and Tor onion service services (henceforth, Onion).

It is also outside of the scope of this section to define the way in which
a OONI probe discovers the collector API endpoint, as well as how, given
several endpoints and/or endpoint types (HTTPS, Onion), it chooses a specific
endpoint.

# 2.0 Threat model

The collector transport MUST guarantee some reasonable level of encryption
and authentication between the OONI probe and itself. Therefore, a malicious
lazy actor won't be able to easily modify test results that they have not
created while they are being submitted to the collector. Also, they will not
be able to easily log the messages exchanged with the collector.

It is outside of the scope of the collector to provide blocking resistance or
to conceal to a passive network observer the fact that they are communicating to
a collector. Such properties are to be provided by other software, e.g. Tor.

Therefore a client implementation of the collector protocol SHOULD allow one
to specify a [SOCKS5](https://tools.ietf.org/html/rfc1928) proxy where the
name resolution is performed by the circumvention tool (`socks5h`).

# 3.0 API

The same API is available via HTTP and Onion.

The standard flow for submitting measurements is the following:

- you create a report (see 3.1);

- you update it by adding measurements (see 3.2);

- then, you close it (see 3.3).

There is also a flow for submitting a report consisting of a single
measurement (see 3.4).

A report that has successfully be created is in the OPEN state. A OONI collector
MUST start a timer when a report is created or updated and MUST automatically
close reports that have been inactive for too much time. For backwards
compatibility a report MUST NOT be considered stale if it had been updated
within the previous two hours. The implementation of this timer MUST use
a monotonic clock to prevent clock jumps from miscalculating the elapsed time.

## 3.1 Create a new report

When a probe starts a test it will *create* a new report by sending a `POST`
request conforming to the following, informal specification:

    POST /report

    {
     "content":
        (optional, deprecated) `string` it is optionally possible to create a report with
        already some data inside of it. MUST be a serialized JSON or YAML depending
        on the value of the 'format' key.

     "data_format_version":
        `string` describing the version of the data format. The current value
        of the data format version is "0.2.0".

     "format":
        `string` that MUST be either "json" or "yaml" and is used to identify the
        format of the `content` field.

     "input_hashes":
        (optional, deprecated) `list` of hex encoded sha256sum of the contents
        of the inputs we are using for this test. This field is required if the
        collector only accepts certain inputs.

     "probe_asn":
        `string` the Autonomous System Number of the network the test is
        related to prefixed by "AS" (ex. "AS1234"). This field MUST
        match this regex: `^AS[0-9]{1,10}$`.

     "probe_cc":
        `string` the two-letter country code of the probe as defined in
        ISO3166-1 alpha-2, or ZZ when undefined (ex. "IT"). This field MUST
        match this regexp: `^[A-Z]{2}$`.

     "probe_ip":
        (optional, deprecated) `string` the IP address of the OONI probe client.

     "software_name":
        `string` the name of the software that is creating a report (ex. "ooni-probe")
        that MUST match this regexp: `^[0-9A-Za-z_.+-]+$`.

     "software_version":
        `string` the version of the software creating the report (ex. "0.0.10-beta")
        that MUST match this regexp: `^[0-9A-Za-z_.+-]+$`.

     "test_name":
        `string` the name of the test performing the network measurement that
        MUST match this regexp: `^[a-zA-Z0-9_\\- ]+$`.

     "test_helper":
        (optional, deprecated) `string` the name of the required test_helper for this test.

     "test_start_time":
        (optional, deprecated) `string` timestamp *in UTC* of when the test was started
        using the format "%Y-%m-%d %H:%M:%S".

     "test_version":
        `string` the version of the test performing the network measurement that
        MUST match the same regexp of 'software_version'.
    }

Where the above is intended as an informal specification for generating a
compliant, serialized JSON object.

Upon receiving a request to create a report, the collector:

1. MUST fail with `4xx` if the request body does not parse, it is not a JSON object,
   any required field is missing and/or if any present field has an invalid value.

2. MUST fail with `4xx` if the request is not compliant with its policies.

3. the collector MAY fail with `5xx` in the following cases:
   
   - the `content` field is present
   
   - the `format` is "yaml"
   
   - the `test_helper` field is present

   This allows a new implementation to drop support for legacy clients.

4. MUST fail with `5xx` if it cannot generate the report ID (see below) or
   in case of other failures opening the report.

5. SHOULD exercise care to avoid logging the `probe_ip` field, if set (e.g.
   by setting it immediately to `null` if such field is not used).

6. if everything is okay, MUST return a `200` response with the body
   described below.

In case of success, the collector MUST return a JSON body generated in
compliance with the following, informal specification:

    {
      "backend_version":
        `string` containing the version of the backend. This version MUST
        match the regex provided above for 'software_version'.

      "report_id":
        `string` report identifier. The format of this field is not
        specified, except that is MUST be a valid UTF-8 string, of
        course. The client MUST NOT make any assumption with respect
        to the structure of this field. It MUST treat this field as
        an opaque identifier. The only requirement is that it MUST
        be at least 256 bits and MUST be generated with a CSPRNG.

      "test_helper_address":
        (conditional, deprecated) `string` the address of a test helper that
        the client requested using the `test_helper_name` field.

      "supported_formats":
        `list` of strings detailing what are the supported formats for
        submitted reports. Allowed values are "json" and "yaml".
    }

Upon receiving a response, new written clients MUST check that the
status is `200` before continuing, MUST ensure that the server suports
its preferred data submission format, and MUST save the report ID.

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
> {
>  "data_format_version":"0.2.0",
>  "format":"json",
>  "probe_asn":"AS30722",
>  "probe_cc":"IT",
>  "software_name":"mkcollector",
>  "software_version":"0.0.1",
>  "test_name":"dummy",
>  "test_version":"0.0.1"
> }
< HTTP/1.1 200 OK
< Server: nginx
< Date: Wed, 13 Mar 2019 13:19:42 GMT
< Content-Type: application/json; charset=utf-8
< Content-Length: 152
< Connection: keep-alive
< 
< {
<  "backend_version":"2.0.0-alpha",
<  "report_id":"20190313T131942Z_AS30722_dU70oZPs80d5E21z8Ef6GXel6CwsdLoXvDk44Fsajv1LDLOIeI",
<  "supported_formats":["json"]
< }
```

## 3.2 Update a report

Updating a report means appending a measurement to the report. A probe MUST do
its best to submit measurements as soon as possible, compatibly with its
configuration and other constraints (e.g. it may be configured to defer submitting
reports until it is connected to a Wi-Fi network).

A collector MUST NOT close an open, stale report before two hours of inactivity.

A probe MUST cache measurements that it could not submit because of network
errors and MUST retry at a later time.

In general, but especially when retrying to submit measurements, a probe MUST record
the elapsed time between when it opened a report and when it is updating it. If a
submission attempt fails with `4xx` _and_ the elapsed time is greater than one hour,
the probe MUST open a new report and submit the measurement as part of this new
report. In doing that, the probe MUST edit the saved measurement to replace
the previous report ID with the newly obtained report ID.

To update a report, the probe issues a request compliant with:

    POST /report/${report_id}

    {
     "content":
       When the report is in YAML, this is a string. Otherwise, this is
       a JSON object. In both cases, this MUST be an object whose top
       level keys MUST follow the df-000-base.md specification (see below).

     "format":
        `string` either "json" or "yaml".
    }

Upon receiving this request, the collector:

1. MUST check whether `${report_id}` is a valid, OPEN report ID and reject
   the request with a `4xx` status otherwise.

2. MUST reject the request with a `4xx` status if the `format`
   is "yaml" _and_ it is not handling YAML.

3. MUST reject the request with a `4xx` if the JSON/YAML does not
   parse or the parsed value is not a JSON/YAML object.

4. MUST verify that the top-level keys are compliant with [df-000-base.md](
   ../data-formats/df-000-base.md) and otherwise return a `4xx`
   status to the client. Additionally:

   - if the `report_id` inside `content` does not match the
     `${report_id}` in the request URL, the collector software
     MUST reject the request with `4xx`.

   - a future version of this specification will explain what
     to do for measurements coming from the future.

5. MAY also parse the `test_keys` fields and, for tests for which the
   schema is known, return a `4xx` status if finds invalid values. We do
   leave this as an option for the future, where probably we will do
   some experiments in this direction.

6. MUST "commit" the measurement to persistent storage or to some
   database before returning `200` to the client making
   sure that it successfully saved the measurement (e.g. by
   checking the return value of `fclose`). There SHOULD be
   integration tests to check whether the JSON serialized by
   a specific implementation is compliant with the format
   expected by the pipeline (e.g. in `go` with `omitempty`
   `null` values are removed by a marshal-serialize cycle
   while the Python parser preserves them).

7. MUST reset the report-specific timer used for automatically
   closing OPEN reports that have become stale.

8. is allowed to perform additional quick operations that may have
   an impact on the status code, and MUST defer other operations
   that do not have an impact on the status code to after the status
   code has been sent to the client (the goal being to keep the
   connection open for as little as possible to avoid the risk that
   a middlebox in a constrained network flags the connection as
   stale and closse it, thus preventing the server from telling the client
   that the measurement has been successfully submitted).

9. if everything is okay, returns `200` to the client (see below).

In case of `200` responses, new collector implementations MUST
at least include a unique identifier for the measurement that the
client may later use to reference said measurement. For example:


```JSON
{"measurement_id":"e00c584e6e9e5326"}
```

As far as the client is concerned, this `measurement_id` is an
opaque UTF-8 string that has some meaning to the server.

The following example shows how updating a report looks like from
the point of view of a modern collector client (where the JSON
messages have been edited for readability):

```
> POST /report/20190313T131942Z_AS30722_dU70oZPs80d5E21z8Ef6GXel6CwsdLoXvDk44Fsajv1LDLOIeI HTTP/1.1
> Host: collector-sandbox.ooni.io
> Accept: */*
> Content-Type: application/json
> Content-Length: 612
> 
> {
>  "content": {
>   "annotations":{},
>   "data_format_version":"0.2.0",
>   "id":"bdd20d7a-bba5-40dd-a111-9863d7908572",
>   "input":null,
>   "input_hashes":[],
>   "measurement_start_time":"2018-11-01 15:33:20",
>   "options":[],
>   "probe_asn":"AS0",
>   "probe_cc":"ZZ",
>   "probe_city":null,
>   "probe_ip":"127.0.0.1",
>   "report_id":"20190313T131942Z_AS30722_dU70oZPs80d5E21z8Ef6GXel6CwsdLoXvDk44Fsajv1LDLOIeI",
>   "software_name":"mkcollector",
>   "software_version":"0.0.1",
>   "test_helpers":[],
>   "test_keys":{"client_resolver":"91.80.37.104"},
>   "test_name":"dummy",
>   "test_runtime":5.0565230846405,
>   "test_start_time":"2018-11-01 15:33:17",
>   "test_version":"0.0.1"
>  },
>  "format":"json"
> }
< HTTP/1.1 200 OK
< Server: nginx
< Date: Wed, 13 Mar 2019 13:19:43 GMT
< Content-Type: application/json; charset=utf-8
< Content-Length: 60
< Connection: keep-alive
< 
< {"measurement_id":"e00c584e6e9e5326"}
```

## 3.3 Closing a report

To close a report, a probe should submit a request like:

    POST /report/${report_id}/close

Upon receiving this request, a collector MUST mark a report
as closed and MUST NOT accept further measurements for
this report. If the report is not existing, a `4xx` error
is returned to the client. Otherwise, `200` is returned
and the response MUST include this body for backwards
compatibility with existing implementations:

```JSON
{"status": "success"}
```

The following example shows how closing a report looks like from
the point of view of a modern collector client (where the JSON
messages have been edited for readability):

```
> POST /report/20190313T131942Z_AS30722_dU70oZPs80d5E21z8Ef6GXel6CwsdLoXvDk44Fsajv1LDLOIeI/close HTTP/1.1
> Host: collector-sandbox.ooni.io
> Accept: */*
> Content-Length: 0
> 
< HTTP/1.1 200 OK
< Server: nginx
< Date: Wed, 13 Mar 2019 13:19:43 GMT
< Content-Type: application/json; charset=utf-8
< Content-Length: 20
< Connection: keep-alive
< 
< {"status":"success"}
```

## 3.4 Submitting single measurements using a single API call

When you have single-entry reports, you can submit them by `POST`ing onto
the `/measurement` endpoint:

    POST /measurement

The request body MUST be a JSON-format OONI measurement.

Upon receiving this request, the collector MUST behave like the client
performed the following operations:

1. opened a report

2. submitted the measurement as part of the report with the correct
   report ID returned in the previous step

3. closed the report

Of course, when processing the measurement submitted using this API, the
collector will ignore any `report_id` field and overwrite it using the
`report_id` it generated for the measurement.

In case of success, the collector MUST return to the client a JSON body
containing _at least_ the following fields:

```JSON
{
 "measurement_id":"e00c584e6e9e5326",
 "report_id":"20190313T131942Z_AS30722_dU70oZPs80d5E21z8Ef6GXel6CwsdLoXvDk44Fsajv1LDLOIeI"
}
```

The following example shows how submitting a single measurement looks
like from the point of view of a modern collector client (where the JSON
messages have been edited for readability):

```
> POST /measurement HTTP/1.1
> Host: collector-sandbox.ooni.io
> Accept: */*
> Content-Type: application/json
> Content-Length: 612
> 
> {
>  "content": {
>   "annotations":{},
>   "data_format_version":"0.2.0",
>   "id":"bdd20d7a-bba5-40dd-a111-9863d7908572",
>   "input":null,
>   "input_hashes":[],
>   "measurement_start_time":"2018-11-01 15:33:20",
>   "options":[],
>   "probe_asn":"AS0",
>   "probe_cc":"ZZ",
>   "probe_city":null,
>   "probe_ip":"127.0.0.1",
>   "software_name":"mkcollector",
>   "software_version":"0.0.1",
>   "test_helpers":[],
>   "test_keys":{"client_resolver":"91.80.37.104"},
>   "test_name":"dummy",
>   "test_runtime":5.0565230846405,
>   "test_start_time":"2018-11-01 15:33:17",
>   "test_version":"0.0.1"
>  },
>  "format":"json"
> }
< HTTP/1.1 200 OK
< Server: nginx
< Date: Wed, 13 Mar 2019 13:19:43 GMT
< Content-Type: application/json; charset=utf-8
< Content-Length: 60
< Connection: keep-alive
< 
< {
<  "measurement_id":"362X4YzBos8=",
<  "report_id":"20190313T131942Z_AS30722_dU70oZPs80d5E21z8Ef6GXel6CwsdLoXvDk44Fsajv1LDLOIeI"
< }
```

# 4.0 Implementation considerations

A client side implementation of the collector protocol MUST make sure
that it is emitting timestamps using UTC rather than local time.

# oonib specification

* version: 1.3.0
* date: 2016-02-05
* author: Arturo Filastò, Aaron Gibson

This document aims at providing a functional specification of oonib. At the
time of writing this document not all parts are fully implemented, though the
application interface to oonib is.


# 0.0 Notes

When we use the term **Network measurement** we are usually referring to a **NetTest**,
that is a test to be run on the network written using the ooniprobe API.

# 1.0 System overview

oonib is the backend component of ooni. It is responsible for:

  * Collecting the results of tests from ooni-probes (Collector).

  * Exposing a set of services that are needed for allowing ooni-probes to
    perform their tests (Test Helpers).

  * Exposing a set of inputs that the collector provides for ooni-probes to
    use with their tests (Collector Inputs)

  * Exposing a policy that describes which tests and inputs the collector
    is willing to accept.

# 2.0 Collector

## 2.1 System overview

The oonib collector exposes a JSON RPC like HTTP interface and allows probes to
submit the results of their measurements. Once probe measurement is complete
the test result is published as an ooni test report in the YAML format.

The oonib collector shall be exposed as a Tor Hidden Service and as a HTTPS
service. The reason for supporting both Tor HS and HTTPS is [better explained in this document](https://ooni.torproject.org/docs/architecture.html#why-tor-hidden-services)

## 2.2 Theat model

The collector shall provide end-to-end encryption and authentication between the probe and the oonib
collector.

A malicious actor should not be able to update test results that they have not
created.

It is outside of the scope of the oonib collector to provide blocking
resistance or to conceal to a passive network observer the fact that they are
communicating to a collector.
Such properties are to be provided by other software components, for example
using Tor or obfsproxy.

## 2.3 Collector API

## 2.3.1 Test result submission interface

Unless otherwise stated all of the network operations below can be performed
either via HTTPS or HTTPO (HTTP over Tor Hidden Service).

Note: we will eventually want to migrate over to using YAML instead of JSON as
a data exchange format. Not doing so adds unnecessary overhead in including
YAML data inside of JSON data.

### 2.3.1.1 Create a new report

When a probe starts a test they will *create* a new report with the oonib
collector backend.
The HTTP request it performs is:

`POST /report`

    {

     'software_name':
        `string` the name of the software that is creating a report (ex. "ooni-probe")

     'software_version':
        `string` the version of the software creating the report (ex. "0.0.10-beta")

     'probe_asn':
        `string` the Authonomous System Number of the network the test is
          related to prefixed by "AS" (ex. "AS1234")

     'probe_cc':
        NEW since oonibackend 1.3
        `string` the two-letter country code of the probe as defined in
        ISO3166-1 alpha-2 or ZZ when undefined (ex. "IT")

     'test_name':
        `string` the name of the test performing the network measurement. In
          the case of ooni-probe this is the test filename without the ".py"
          extension.

     'test_version':
        `string` the version of the test peforming the network measurement.

     'data_format_version':
        NEW since oonibackend 1.3
        `string` that must be either "json" or "yaml" to identify the format
        of the content.

     'start_time':
        NEW since oonibackend 1.3
        `float` seconds since epoch in UTC of when the measurement was started.

     'input_hashes':
        (optional) `list` of hex encoded sha256sum of the contents
          of the inputs we are using for this test. This field is required if the collector backend only
          accepts certain inputs (that is it has a collector policy).
          For more information on policies see section 2.3.

     'test_helper':
        (optional) `string` the name of the required test_helper for this test.

     'content':
        DEPRECATED since oonibackend 1.3
        (optional) `string` it is optionally possible to create a report with
          already some data inside of it.

     'probe_ip':
        (optional) `string` the IP Address of the ooniprobe client. When the
          test requires a test_helper the probe should inform oonib of it's IP
          address. We need to know this since we are not sure if the probe is
          accessing the report collector via Tor or not.

     'format':
        `string` that must be either "json" or "yaml" to identify the format
        of the content.
        New since version 0.2.0 of the data format or 1.2 of the backend.

     }

When a report is created the backend will respond with a report identifier
that will then allow the probe to update the report and the version of the
backend software like follows:

`Status Code: 201 (Created)`

{

      'backend_version':
        `string` containing the version of the backend

      'report_id':
        `string` report identifier of the format detailed below.

      'test_helper_address':
        (conditional) `string` the address of a test helper that the client requested.

      'supported_formats':
        NEW since oonibackend 1.3
        `list` of strings detailing what are the supported formats for
        submitted reports. Can either be "json" or "yaml".

}

The report identifier allows the probe to update the report and it will be
contructed as follows:

  ISO 8601 timestamp + '_' + probe ASN + '_' + 50 mixed lowercase uppercase characters

A report identifier can be for example:

  19120623T101234Z_AS1234_ihvhaeZDcBpDwYTbmdyqZSLCDNuJSQuoOdJMciiQWwAWUKJwmR

If the report does not match the collector policy it will not create a report 
or return a valid report_id.

The collector will instead respond like follows:

`Status Code: 406 (Not Acceptable)`

    {
      'error': 'invalid-input-hash'
    }

Note:
The report identifier should be at least 256 bits and generated by means of a
CSPRNG. It is a token that is used to provide read and update authority.

Client implementation notes:
Probes should not expect the report identifier to be in a particular format as
the report id may be changed in the future.

Probes should parse the report_status before proceeding with a report.

### 2.3.1.2 Update a report

Once the probe has a report ID they will be able to add test related content to
the report by referencing it by id:

`PUT /report`

```
{

    'report_id':
      `string` the report identifier

    'content':
      `string` content to be added to the report. This can be one or more
        report entries in the format specified in df-000-base.md

     'format':
        `string` that must be either "json" or "yaml" to identify the format
        of the content.
        New since version 0.3 of the data format or 1.2 of the backend.

}
```

This method is deprecated, because it is not proper usage of HTTP request methods.
PUT should only be used for operations that are idempotent.

The backend should validate the request to make sure it is a valid YAML Stream.

New collectors should use the following format for updating reports:

`POST /report/$report_id`

```
{

    content:
      `string` content to be added to the report. This can be one or more
        report entries in the format specified in df-000-base.md

     'format':
        `string` that must be either "json" or "yaml" to identify the format
        of the content.
        New since version 0.3 of the data format or 1.2 of the backend.

}
```

### 2.3.1.3 Closing a report

This request is done by a probe to tell the backend that they have finished
running the test and the report can be considered done:

`POST /report/$report_id/close`

## 2.3.2 Descriptors

### 2.3.2.1 Decks (or Experiments)

These are what a user will end up running. A deck is basically a set of nettests and one input (or none) per nettest.

#### GET /deck

This will list all the available decks.


```
[

  {
    'id': "The deck ID that is the hash of the YAML ooni deck",
    'name': "The name of the deck",
    'description': "The description of the deck",
  },

  ...
]
```

#### GET /deck/$deck_id

This will return the descriptor for the specified deck

```
{
    'name': "the name of the deck",
    'description': "a description of the deck",
    'version': "the deck version number",
    'author': "the author name and email address in the format John Doe <john@example.com>",
    'date': "the deck creation time in ISO 8601",
}
```

#### GET /deck/$deck_id/yaml

This will return the deck content in YAML format

### 2.3.2.2 Inputs

These are the inputs supported by the collector in question. Such inputs will then be given to a nettests or referenced by a deck.

#### GET /input

This will list all the available inputs:


```
{
  'id': "The deck ID that is the hash of the input file",
  'name': "The name of the input",
  'description': "The description of the input",
}
```

#### GET /input/$input_id

This will return the descriptor for the specified input

```
{
 'name': "the name of the input",
 'description': "a description of the input",
 'version': "the input version number",
 'author': "the author name and email address in the format John Doe <john@example.com>",
 'date': "the input creation time in ISO 8601",
}
```

#### GET /input/$input_id/file

This will return the file content

### 2.3.2.3 NetTest

This is the code that gets run by ooniprobe to perform network measurements.

#### GET /nettest

This will list all the available nettests.


```
{
  'id': "The nettest ID that is the hash of the nettest",
  'name': "The name of the nettest",
  'description': "The description of the nettest",
}
```

#### GET /nettest/$nettest_id

This will return the descriptor for the specified nettest

```
{ 
 'name': "the name of the deck",
 'description': "a description of the deck",
 'version': "the deck version number",
 'author': "the author name and email address in the format John Doe <john@example.com>",
 'date': "the deck creation time in ISO 8601",
}

```

#### GET /nettest/$nettest_id/py

This will return the nettest python file content.

## 2.3.3 Policies

This allows a collector administrator to specify which nettests and inputs it is willing to accept reports on.

### 2.3.3.1 Input Policy

This specifies which inputs are allowed.

#### GET /policy/input

```
[
  {'id': 'the ID of the input we accept reports for'},
  ...
  {'id': ''}
]
```

### 2.3.3.2 Nettest Policy

#### GET /policy/nettest

```
[
  {'name': 'the name nettest we accept reports for',
   'version': 'version number we accept reports for'},
  ...
]
```

## 2.4 Report lifecycle

When a report is created (section 2.3.1) it should be marked as NEW and a
timestamp should be recorded. If a report was rejected, it is discarded.

Once it is updated (section 2.3.2) it should be marked as ACTIVE. An ACTIVE
report can be updated with new data. The collector must keep track of the last
time a certain report is updated with new and valid data.

A report is considered CLOSED when either the probe instructs the collector to
close the report (section 2.3.3) or when a report is in ACTIVE state and has
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

## 2.6 Test helper collector relationship

Some tests involve adding to the report also data that is collected by means of
a test helper. This is the case in the two way traceroute test, where the
report should include a traceroute also from the vantage point of the ooni
backend.

In these circumstances the report from the vantange point of the backend should
be inside of a separate file that has the same name of the probe report but
"-probe" should be replaced with "-backend".

For example the backend part of the report for a traceroute test called
`two_way_traceroute-2012-01-01T120000Z-AS3-probe.yamloo`, shall be called

`two_way_traceroute-2012-01-01T120000Z-AS3-backend.yamloo`


# 3.0 Test Helpers

These are services exposed to ooniprobe clients that are of assistance to
performing network measurements.

# 3.1 System overview

Probes will always receive as address of a test helper that of the one running
on the same machine as the collector.

They will only point to a test helper on a different machine if the test helper
for the test the user is interested in running is not available on the desired
machine.

This can happen, for example, if the machine does not have two network
interfaces with two differnet IP addresses. In this case the HTTP Return JSON
Headers test helper cannot run at the same time as the TCP echo test helper
(both bind to port 80).

Some communication with the collector is required. This is the case of the two
way traceroute test, where a multiport multiprotocol traceroute must also be
performed from the backend to the probe.

Test helpers are two kinds:

  * Reply: are test helpers that reply to requests from probes. For example
    HTTP test helpers are of this kind.

  * Active: are test helpers that actively perform requests towards the probe
    idepedently from probe requests.

Implementation notes:
Although I am talking about the collector as two differnet software components
they both run inside of the same process and are part of the same piece of
software.

## 3.1.1 Test Helper collector mapping

When a report that requires a test helper is created with the collector
component of oonib the test helper should be notified of the probes IP
address (the probe_ip).

This will allow the test helper to know from which IP address it should either
expect the probe to come from or towards what IP address it should perform an
active measurement.

## 3.2 Threat model (or non-goals)

Because of the nature of the services that they are exposing it is not possible
to guarantee end to end confidentiality and authentication of the data
transmitted to and from test helpers.

Moreover we are currently not making any particular effort to make test helpers
look like something that they are not (i.e. make test helper traffic not look
like test helper traffic).

## 3.3 Test helper listing API

### GET /test-helper

This lists all the test helpers running on this machine:

```
{
  'id': 'the name of the test helper',
  'description': 'description of the test helper',
  'address': 'the full address of the test helper (this should include at least IP and port)'
}
```

## 3.4 Reply Test Helpers

### 3.4.1 HTTP Return JSON Headers

This test helper will bind on port 80 and expect HTTP requests from a probe. It
shall respond to every HTTP request with the HTTP Headers and HTTP request line
as seen from the backend point of view.

The response is structured in JSON as follows:

    {

        'request_headers':
            [[HTTP header1 name, HTTP header1 value], [HTTP header2 name, HTTP header2 value]]
            the list is ordered based on how the headers were received.

        'request_line':
            the value of the HTTP request line.

        'headers_dict':
            `dict` containing as keys the HTTP header name (normalized) and as
            value a list containing the values of such header

    }

For example:

    {

        'request_headers':
            [['User-Agent', 'IE6'], ['Content-Length', 200]]
        'request_line':
            'GET / HTTP/1.1'

        'headers_dict':
            {'User-Agent': ['IE6'], 'Content-Length': [200]}
    }

### 3.4.2 DNS Test Helper

Shall provide a DNS resolver over UDP and TCP exposed on port 53. Such DNS
resolver shall not filter any DNS query.

### 3.4.3 TCP Echo Helper

This shall expose a TCP echo service that is bound to port 80.

## 3.5 Active Test Helpers

### 3.5.1 Two way traceroute

This shall perform the ooniprobe traceroute test and attach the result to the
final report as described in section 2.5.

# 4.0 Bouncer

This is the service that will allow the ooni-probe to discover collectors that run test helpers that the probe needs.

## 4.1 API

### POST /bouncer

This will return a list of required collectors.

Currently a client has two ways to request the required collectors.

#### POST /bouncer/test-helpers

The first and old way is to provide a bunch of test-helpers, oonib then will return the identity of 
the collectors and the addresses of machines that can run the requested test helpers.

This way, the client sends:
```
{
  'test-helpers': [
     'id of first test helper I need',
     'id of second test helper I need']
}
```

And the bouncer replies:

```
{
   'id-of-test-helper': {
       'address': '127.0.0.1',
       'collector': 'httpo://thirteenchars1.onion'
   },
   'id-of-test-helper2': {
       'address': '127.0.0.1:8081',
       'collector': 'httpo://thirteenchars1.onion'
   },
   'id-of-test-helper3': {
       'address': 'http://127.0.0.1',
       'collector': 'httpo://thirteenchars2.onion'
   },
   'default': {
       'collector': 'httpo://thirteenchars1.onion'
   }
}
```

If it is not possible to find a test helper for one of the required test
helpers an error message is returned:
```
{'error': 'test-helper-not-found'}
```

#### POST /bouncer/net-tests

The second and policy respectful way is to provide a bunch of nettests, then the bouncer
will return the identity of the machines that:
 1. Can run the required test-helpers
 2. Can send back to the client a set of required inputs
 3. Can collect the report of the nettest
 
If a known collector to the bouncer cannot provide any of the three previous requirements,
the collector won't be sent back to the client in the bouncer request.

If no policy respectful collector can be returned to the client, a default one will be sent
when the bouncer knows the identity of a collector that accepts any request, which is 
expressed as a lack of any policy for that collector in the oonib.conf file.

Both the test-helpers and the input-hashed attributes are optional for the client's request,
but the nettest's name is mandatory.

This way the client sends:
```
{
    'net-tests': [
        {
            'test-helpers': ['required test helper', ...],
            'input-hashes': ['required input id', ...],
            'name': 'name of nettest',
            'version': 'version of nettest'
        },
        ....
    ]
}
```

And the bouncer replies:
```
{
    'net-tests': [
        {
            'test-helpers': [
                {'requested test helper': 'address'},
                ...
            ],
            'input-hashed': ['requested input id', ...],
            'name': 'name of nettest',
            'version': 'version of nettest',
            'collector': 'address'
        },
        ....
    ]
}
```

If it's not possible to find a collector for the request, oonib will respond with:
```
{'error': 'collector-not-found'}
```

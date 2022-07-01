# OONI Run specification

* author: Norbel Ambanumben
* version: 0.0.1
* date: 2022-06-15
* status: _draft_

This document provides a functional specification for OONI Run.

# 1.0 System overview

The ooni/api exposes an HTTP API allowing OONI Run web app to submit links to the
backend and also allow the OONI Probe to query OONI Run link data.
The client and the server MUST NOT assume a keep
alive semantics for the HTTP connections.

New server implementations MUST support `Content-Encoding: gzip` to
compress request bodies. OONI production clients MUST NOT use this
feature until all OONI's production servers server are known to have
implemented it. Third party clients should either coordinate with
us or be prepared to retry without compression.

New implementations MUST properly set `Content-Type`. Server side
implementatons MUST be able to deal with legacy clients that possibly
do not correctly set the `Content-Type`.

Tests submitted to the OONI Run API will be stored and processed by OONI backend
and OONI Probes the URL is shared with.
How that will happen is out of the scope of this document. You may also want to read
[about our data policy](https://ooni.io/about/data-policy/).

The OONI Run MUST be exposed as an HTTPS service. It MUST also be exposed as
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

The OONI RUN Service transport MUST guarantee some reasonable level of encryption
and authentication between the OONI probe and itself. Therefore, a malicious
lazy actor won't be able to easily modify test results that they have not
created while they are being submitted to the OONI Run Service. Also, they will not
be able to easily log the messages exchanged with the OONI Run Service.

It is outside of the scope of the OONI Run Service to provide blocking resistance or
to conceal to a passive network observer the fact that they are communicating to
a OONI Run Service. Such properties are to be provided by other software, e.g. Tor.

Therefore a client implementation of the OONI Run Service protocol SHOULD allow one
to specify a [SOCKS5](https://tools.ietf.org/html/rfc1928) proxy where the
name resolution is performed by the circumvention tool (`socks5h`).

# 3.0 API

The same API is available via HTTP and Onion.

The standard flow for OONI RUN Link is the following:

- you create an OONI RUN Link (see 3.1);

- you update it by adding more tests or metadata (see 3.2);

- you access it from probes or frontend service (see 3.3);

- then, you can disable/delete it (see 3.4).

## 3.1 Create a new OONI Run link

### Request

When you *create* a new OONI RUN link, the frontend sends a `POST`
request conforming to the following, informal specification:

    POST /api/v2/oonirun/link

    {
     "name":
        (required) `string` it is required property used in identifying the link in the OONI probe and other parts of the system.

     "description":
        (optional) `string` describing the tests included as part of the OONI Run link.
      
      "tests": `array` provides a JSON array of tests to be run.
         [
            {
                  "ta": {
                     "inputs": []
                  },
                  "tn": "web_connectivity"
            },
            {
                  "tn": "telegram"
            },
            {
                  "tn": "signal"
            }
         ]
    }

Where the above is intended as an informal specification for generating a
compliant, serialized JSON object.

### Response status code

Upon receiving a request to create a report, the OONI Run Service:

1. SHOULD fail with `4xx` if the request body does not parse, it is not a JSON object,
   any required field is missing and/or if any present field has an invalid value.

2. MUST fail with `4xx` if the request is not compliant with its policies.

3. MUST fail with `5xx` if it cannot generate the OONI Run ID (see below) or
   in case of other failures opening the OONI Run.

4. if everything is okay, MUST return a `200` response.

### Response body

In case of failure, the OONI Run Service MUST return a JSON object, whose content
is implementation dependent and MAY be empty. Some existing implementations
return a `{"error": "string"}` object to make debugging easier.

In case of success (i.e. `200` response), the OONI Run Service MUST return a JSON body
generated in compliance with the following, informal specification:

    {
      "backend_version":
        `string` containing the version of the backend. This version MUST
        match the regex provided above for 'software_version'.

      "ooni_run_id":
        `string` OONI Run identifier. The format of this field is not
        specified, except that is MUST be a valid UTF-8 string, of
        course. The client MUST NOT make any assumption with respect
        to the structure of this field.
    }

### Response processing requirements

Upon receiving a response, new written clients MUST check that the
status is `200` before continuing, MUST ensure that the server supports
their preferred data submission format, and MUST save the OONI Run ID.

## 3.2 Update an OONI Run Link

Updating an OONI Run Link means appending a test to the OONI Run Link.

### Request

To update an OONI Run Link, the client issues a request compliant with:

    POST /api/v2/oonirun/link/${ooni_run_id}

    {
     "name":
        (required) `string` it is required property used in identifying the link in the OONI probe and other parts of the system.

     "description":
        (optional) `string` describing the tests included as part of the OONI Run link.
      
      "tests": `array` provides a JSON array of tests to be run.
         [
            {
                  "ta": {
                     "urls": []
                  },
                  "tn": "web_connectivity"
            },
            {
                  "tn": "telegram"
            },
            {
                  "tn": "signal"
            }
         ]
    }

### Response status code

Upon receiving this request, the OONI Run backend:

1. SHOULD check whether `${ooni_run_id}` is a valid, OONI Run ID and reject
   the request with a `4xx` status otherwise.

2. SHOULD reject the request with a `4xx` if the JSON does not
   parse or the parsed value is not a JSON object.

3. MUST "commit" the OONI Run data to persistent storage or to some
   database before returning `200` to the client making
   sure that it successfully saved the OONI Run Data (e.g. by
   checking the return value of `fclose`). There SHOULD be
   integration tests to check whether the JSON serialized by
   a specific implementation is compliant with the format
   expected by the pipeline (e.g. in `go` with `omitempty`
   `null` values are removed by a marshal-serialize cycle
   while the Python parser preserves them).

4. is allowed to perform additional quick operations that may have
   an impact on the status code, and SHOULD defer other operations
   that do not have an impact on the status code to after the status
   code has been sent to the client (the goal being to keep the
   connection open for as little as possible to avoid the risk that
   a middlebox in a constrained network flags the connection as
   stale and closse it, thus preventing the server from telling the client
   that the measurement has been successfully submitted).

5. if everything is okay, returns `200` to the client (see below).

### Response body

In case of failure, the OONI Run Service MUST return a JSON object, whose content
is implementation dependent and MAY be empty. Some existing implementations
return a `{"error": "string"}` object to make debugging easier.

In case of `200` responses, new OONI Run Service implementations MAY
include a unique identifier for the OONI Run Link that the
client may later use to reference said OONI Run Link. For example:


```JSON
{"ooni_run_id":"e00c584e6e9e5326"}
```

As far as the client is concerned, this `ooni_run_id` is an
opaque UTF-8 string that has some meaning to the server.

## 3.3 Deleting an OONI Run Link

To delete a report, a client should submit a request like:

    DELETE /api/v2/oonirun/link/${ooni_run_id}

If the report exists, `200` is returned
and the response MUST include this body for backwards
compatibility with existing implementations:

```JSON
{"status": "success"}
```

Otherwise, in case of failure, the OONI Run Service MUST return a JSON object, whose
content is implementation dependent and MAY be empty. Some existing implementations
return a `{"error": "string"}` object to make debugging easier.

# 4.0 Implementation considerations

A client side implementation of the OONI Run Service MUST make sure
that it is emitting timestamps using UTC rather than local time.

A client side implementation MAY retry any failing OONI Run Service operation
immediately for three times in case there is a DNS or TCP error. This
is to ensure that transient errors do not prevent us from submitting the
data immediately. If all these immediate retries fail, then the client
SHOULD arrange for resubmitting the OONI Run Link at a later time, either
requiring user input or automatically. In the latter case, the delay
after which the client will attempt to resubmit SHOULD be exponentially
distributed and SHOULD NOT be smaller than 15 minutes.

A server implementation MAY publish metrics allowing OONI to gradually
enforce more JSON schema correctness in the OONI Run Service, both for the
open-report request and for submitted data. A possible strategy to make
this happen consists of parsing without rejecting, counting the number
of failures, and then iterating until the number of failures starts
converging to zero. At that point, it is possible to make the checks
mandatory and reject invalid input.

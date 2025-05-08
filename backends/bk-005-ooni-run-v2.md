# OONI Run v2 specification

-   author: Norbel Ambanumben, Arturo Filastò
-   version: 2024.02.23
-   status: release-candidate

This document provides a functional specification for OONI Run.

# 1.0 System overview

OONI Run links allow users to coordinate measurement campaigns with
volunteers by sharing a mobile deep link that will instrument the OONI Probe
application to run a set of nettests (or experiments) configured in a certain
way.

Below are definitions for important components of the system:

* **OONI Run link** is a mobile deep link that when clicked or tapped on a system
  with the OONI Probe app installed allows the user to instrument their probe to
  run the nettests configured by the link creator. If the OONI Probe app is not
  installed, it will display a web page asking them to download the app.

* **OONI Run descriptor** contains the metadata for a specific OONI Run link and
  the nettest definitions: what nettests should be run and how they should be
  configured (ex. what URLs should be tested)

* **OONI Run descriptor URL** is the web resource from which the descriptor is
  retrieved.

The high level workflow looks like the following:

```mermaid
sequenceDiagram
    actor CampaignOrganizer as Campaign Organizer
    participant OONIAPI
    actor Volunteer

    CampaignOrganizer->>OONIAPI: Create OONI Run link to run web_connectivity with http://example.com
    OONIAPI->>CampaignOrganizer: OONI Run link: https://run.ooni.io/v2/deadbeef
    CampaignOrganizer-->>Volunteer: Hey, can you open the link https://run.ooni.io/v2/deadbeef with OONI Probe?
    Volunteer-)OONIAPI: What is the descriptor for OONI Run link with ID "deadbeef"
    OONIAPI->>Volunteer: Here is the descriptor for "deadbeef"
```

It's important to notice how, in the event that the user has the OONI Probe app
installed, a web request to `https://run.ooni.org/io/v2/deadbeef` will never be
issued on the network, but rather the metadata encoded in the URL itself is used
to retrieve the OONI Run descriptor from a different OONI API endpoint.

When a Volunteer taps on an OONI Run link (in the above example
`https://run.ooni.io/v2/deadbeef`) the OONI Probe app is opened and a they are
presented with the metadata of the OONI Run link as well as the nettests it is
configured with.
At this point, assuming they feel confortable with running the nettests they see
on their screen, they can "install" the OONI Run link inside their app making it
available as new card on the dashboard page allowing them to manually or
automatically run it as part of regular OONI Probe testing.

In a way, an OONI Run link generated card, is very similar to the existing OONI
Probe test groups, except these can be community contributed.

# 2.0 Threat model

The OONI Run service MUST ensure that only the creator of a link is able to
perform UPDATE operations through some form of authentication. It is outside
of the scope of this document to specify the exact details of how authentication
should work, but traditional techniques for implementing authentication should be
used (ex. JWT token sent using appropriate HTTP headers).

Communication with the OONI API MUST be done over a communication channel that
ensures confidentiality, integrity and authenticity of the transmitted content,
such as TLS or onion services.

Whenever a change is made to an OONI Run link, it's important that the end user
is informed about them and the OONI Run link is disabled until they agree with
them.

It is outside of the current scope of this document to prescribe if and how some
level of blocking resistance should be implemented or provided by the system.
That said it's worth noting that since the content of a OONI Run descriptor is
static, it should be possible server it from a mirror that provides higher
levels of blocking resistance (and potentially some higher level of stealth),
such as s3 or github.

# 3.0 OONI Run descriptor

OONI Run descriptors define a set of experiments and configuration vectors used.
It also includes additional metadata used to display a particular OONI Run object
to the end user.

Our goal is to use OONI Run descriptors to implement all the cards currently
present inside of the OONI Probe app. As such we will be having a set of default
OONI Run links that apps will ship with.

An OONI Run link descriptor is a JSON file with the following semantics:

```JavaScript
{
  "name": "(required) `string` is the display name for the OONI Run link",

  // (optional) `map` of translations to language codes for the name
  "name_intl": {
    "it": "Il nome dello OONI Run link in italiano",
  },

  // TODO: recommend a maximum length for this field
  "short_description": "(optional) `string` short_description for the OONI Run link.",

  // (optional) `map` of translations to language codes for the short_description
  "short_description_intl": {},

  "description": "(optional) `string` full description for this OONI Run link. This goes into the details of the card. Markdown is supported.",

  // (optional) `map` of translations to language codes for the description
  "description_intl": {
    "it": "La descrizione del test in italiano"
  },

  "icon": "(optional) `string` the ID of any icon part of the OONI icon set",

  "author": "(optional) `string` name of the creator of this OONI Run link",

  "is_expired": "(optional) `bool` a boolean flag used to indicate if this OONI Run link is expired. When an OONI Run link is archived, it does not run",

  // `array` provides a JSON array of tests to be run.
  "nettests":[{

    // (optional) `array` provides a JSON array of inputs for the specified test.
    "inputs": [
      "https://example.com/",
      "https://ooni.org/"
    ],

    // (optional) `array` provides a richer JSON array containing targets for the specified experiment.
    // One of either `inputs` or `targets` can be specified, but not both.
    "targets": [{
        "input": "https://example.com/",
        "extra": {
           "category_code": "HUMR",
        }
      }
    ],

   // (optional) string used to specify during creation what is the label for targets to use.
   "targets_name": "websites_list_prioritized",

    // (optional) `map` options arguments provided to the specified test_name
    //
    // Note: this field is currently experimental. A future version of the specification
    // may modify the field name or its semantics if we discover it needs changes.
    "options": {
      "HTTP3Enabled": true
    },

    // (optional) `bool` indicates if this test should be run as part of autoruns. Defaults to true.
    //
    // Note: this field is currently experimental. A future version of the specification
    // may modify the field name or its semantics if we discover it needs changes.
    "is_background_run_enabled": true,

    // (optional) `bool` indicates if this test should be run as part of manual runs. Defaults to true.
    //
    // Note: this field is currently experimental. A future version of the specification
    // may modify the field name or its semantics if we discover it needs changes.
    "is_manual_run_enabled": true,

    "test_name": "web_connectivity"
  }, {
    "test_name": "openvpn",
    "targets": [{
      "input": "https://foo.com/",
      "extra": {
         "provider": "riseupvpn",
      }
    }],
  }]
}
```

In reality there are two different views onto an OONI Run link descriptor. One
is the view from the perspective of the creator and owner of the link, the
second is from the perspective of measurement applications that need to consume
these links.

The reason for this is that certain target lists need to be generated
dynamically and at runtime, while the parameters for generating these dynamic
links are specified by the creator of the link.

A prime example of this would be the OONI Run link for the stock OONI Websites
card. The OONI Run descriptor, as specified from the link creator, is saying
"run the test-lists with weights applied based on coverage", while the mobile
application will then receive a prioritized and sorted list which will change
every time a new run is performed.

To achieve this we need 2 different views on the link, one for the creation
phase (`target_name`) and another for the retrieval phase (`targets`).

Based on the above specification it would be possible to re-implement the cards for the OONI Probe
dashboard as follows.

### Websites

```json
{
"name": "Websites",
"short_description": "Test the blocking of websites",
"description": "Check whether websites are blocked using OONI's [Web Connectivity test](https://ooni.org/nettest/web-connectivity/)...",
"icon": "OONINettestGroupWebsites",
"author": "contact@ooni.org",
"nettests":
   [
      {
         "targets": [{
            "input": "https://example.com/",
            "extra": {
               "category_code": "HUMR",
            }
         }],
         "is_manual_run_enabled": true,
         "is_background_run_enabled": false,
         "test_name": "web_connectivity"
      },
      {
         "is_manual_run_enabled": false,
         "is_background_run_enabled": true,
         "test_name": "web_connectivity"
      },
   ]
}
```

### Instant Messaging

```json
{
"name": "Instant Messaging",
"short_description": "Test the blocking of instant messaging apps",
"description": "Check whether [WhatsApp](https://ooni.org/nettest/whatsapp/), ...",
"icon": "OONINettestGroupInstantMessaging",
"author": "contact@ooni.org",
"nettests":
   [
      {
         "test_name": "whatsapp"
      },
      {
         "test_name": "telegram"
      },
      {
         "test_name": "facebook_messenger"
      },
      {
         "test_name": "signal"
      },
   ]
}
```

### Circumvention

```json
{
"name": "Circumvention",
"short_description": "Test the blocking of censorship circumvention tools",
"description": "Check whether [Psiphon](https://ooni.org/nettest/psiphon/), ...",
"icon": "OONINettestGroupCircumvention",
"author": "contact@ooni.org",
"nettests":
   [
      {
         "test_name": "psiphon"
      },
      {
         "test_name": "tor"
      },
      {
         "test_name": "riseupvpn"
      }
   ]
}
```

### Performance

```json
{
"name": "Performance",
"short_description": "Test your network speed and performance",
"description": "Measure the speed and performance of your network using the [NDT](https://ooni.org/nettest/ndt/) test. ...",
"icon": "OONINettestGroupPerformance",
"author": "contact@ooni.org",
"nettests":
   [
      {
         "test_name": "http_invalid_request_line"
      },
      {
         "test_name": "http_header_field_manipulation"
      },
      {
         "test_name": "ndt"
      },
      {
         "test_name": "dash"
      },
   ]
}
```

### Experimental

```json
{
"name": "Experimental",
"short_description": "Run new experimental tests",
"icon": "OONINettestGroupExperimental",
"author": "contact@ooni.org",
"nettests":
   [
      {
         "test_name": "stun_reachability"
      },
      {
         "test_name": "dnscheck"
      },
      {
         "is_manual_run_enabled": false,
         "test_name": "tor_snowflake"
      },
      {
         "is_manual_run_enabled": false,
         "test_name": "vanilla_tor"
      },
   ]
}
```

# 4.0 API

In order to support the above workflow the OONI API needs to support the following operations:

* CREATE a new OONI Run link, returning the OONI Run link ID (see 4.1)

* UPDATE an existing OONI Run link (see 4.2)

* GET the OONI Run descriptor, provided an ID (4.3)

In the following sections we will specify how these operations should be done.

By design, we don't specify a delete operation. This is because we want to
ensure there is a permanent record of all OONI Run links that ever existed.

A certain OONI Run link can rendered ineffective by setting the
`expiration_date` to a past date.
In this case the OONI Run link still remains available, but it will not lead to
tests being initiated.

## 4.1 CREATE a new OONI Run link

This operation will be performed by a logged in user that is interested in
performing an OONI Run link based measurement campaign.

It is outside of the scope of this document to specify how registration and
authentication should be handled.

### Request

When you `CREATE` a new OONI RUN link, the client sends a HTTP `POST`
request conforming to the following:

`POST /api/v2/oonirun/links`

```JavaScript
{
"name": "", // (required) `string` is the display name for the OONI Run link

"description": "", // (required) `string` describing the scope of this OONI Run link system

"short_description": "(optional) `string` short_description for the OONI Run link.",

"author": "", // `string` email address of the creator of this OONI Run link

"name_intl": {"it": ""}, // (optional) `string` is the display name for the OONI Run link

"short_description_intl": {}, // (optional) `map` of translations to language codes for the short_description

"description_intl": {"it": ""}, // (optional) `string` describing the scope of this OONI Run link system

"icon": "", // (optional) `string` the ID of any icon part of the OONI icon set

"color": "", // (optional) `string` hex encoding of the 6 hex digit color used for the card prefixed by # (eg. #000000)

"expiration_date": "", // `string` timestamp indiciating at what time the link will expire

"nettests": // `array` provides a JSON array of tests to be run.
   [
      {
         "inputs": [
            "https://example.com/",
            "https://ooni.org/"
         ],
         "options": {
            "HTTP3Enabled": true,
         },
         "test_name": "web_connectivity"
      },
      {
         "test_name": "dnscheck"
      }
   ]
}
```

Moreover it's possible to specify `targets` as rich JSON structure or
`target_name` indicating the name of the target list which will result in the
target list being generated dynamically.

`target`, `target_name` and `inputs` are mutually exclusive.

### Response status code

Upon receiving a request to create a link, the API will respond:

1. SHOULD fail with `4xx` if the request body does not parse, it is not a JSON object,
   any required field is missing and/or if any present field has an invalid value.

2. if everything is okay, MUST return a `200` response.

### Response body

In case of failure, the OONI Run Service MUST return a JSON object formatted as
`{"error": "string"}` containing details about the encountered error.

In case of success (i.e. `200` response), the OONI Run Service MUST return the
following JSON body:

```JavaScript
{

"title": "",

"description": "",

"author": "",

// [... rest of the OONI Run link payload]

// Additional fields that are added by the backend are:

"oonirun_link_id": "", // `string` OONI Run link identifier.
"is_expired": false, // `string` indicates if the OONI run link has expired
"date_created": "",
"date_updated": "",
"expiration_date": "", // `string` timestamp indiciating at what time the link will expire
"revision": 1, // `int` incremental number indication what revision of the link this is. Whenever changes to the nettests occur a new revision will be generated.
"is_mine": false, // `bool` flag indiciating if the link is owned by the requester
}
```

## 4.2 UPDATE an existing OONI Run link

This operation will be performed by a logged in user that is interested in
performing an OONI Run link based measurement campaign.

It is outside of the scope of this document to specify how registration and
authentication should be handled.

Updating an OONI Run Link means editing any of the fields of an OONI Run link
descriptor. This may involve adding or removing tests, editing targets of
existing ones or making changes to the OONI Run link metadata.

The web UI should discourage users from making changes to the title, icon and
descriptions of OONI Run links as to not confused volunteers that have installed
a link.

### Request

To update an OONI Run Link, the client issues a request compliant the same as the create request.

Below we list the extra fields that are settable from the edit request that are
not settable during CREATE.

`PUT /api/v2/oonirun/links/{ooni_run_link_id}`

```JavaScript
{
   // See create for full semantics
}
```

### Response status code

Upon receiving this request, the OONI Run backend:

1. SHOULD check whether the `${oonirun_link_id}` exists and they have permission to
   edit it and reject the request with a `4xx` status otherwise.

2. SHOULD reject the request with a `4xx` if the JSON does not
   parse or the parsed value is not a JSON object.

3. if everything is okay, returns `200` to the client (see below).

### Response body

In case of failure, the OONI Run Service MUST return a JSON object formatted as
`{"error": "string"}` containing details about the encountered error.

In case of success (i.e. `200` response), the OONI Run Service MUST return the
following JSON body:

```JavaScript
{
"oonirun_link_id": "", // `string` OONI Run link identifier.

"title": "",

"description": "",

"author": "",

// [... rest of the OONI Run link payload]

}
```

## 4.3 GET the OONI Run descriptor

This operation is performed by OONI Probe clients to retrieve the latest
revision for a descriptor of a certain OONI Run link given the ID.

As such, this request does not require any authentication.

### Request

To retrieve an OONI Run link descriptor, the client issues a request compliant with:

`GET /api/v2/oonirun/links/{oonirun_link_id}`

### Response status code

Upon receiving this request, the OONI Run backend:

1. SHOULD check whether the `${oonirun_link_id}` exists and return 404 if it does
   not.

2. if everything is okay, returns `200` to the client (see below).

### Response body

In case of success (i.e. `200` response), the OONI Run Service MUST return the
following JSON body:

```JavaScript
{
   // See CREATE response format for full format.
}
```

Note: for dynamically generated run links, this view will only return the
`target_name` and not the `targets` list.

## 4.4 GET the OONI Run full descriptor by revision

This operation is performed by OONI Probe clients to retrieve the descriptor of
a certain OONI Run link given the ID and revision

As such, this request does not require any authentication.

### Request

To retrieve an OONI Run link descriptor, the client issues a request compliant with:

`GET /api/v2/oonirun/links/{oonirun_link_id}/full-descriptor/{revision}`

### Response status code

Same as 4.3 GET the OONI Run descriptor

### Response body

Same as 4.3 GET the OONI Run descriptor

Note: for dynamically generated run links, this view will only return the
`target_name` and not the `targets` list.

## 4.4 GET the OONI Run engine descriptor revision

This operation is performed by OONI Probe clients to retrieve the engine descriptor of
a certain OONI Run link given the ID and revision

As such, this request does not require any authentication.

This method is used to return just the nettests, revision and date_created
sections of a descriptor to be used by the measurement engine.

When the specified OONI Run link contains dynamic targets, it will return the
generated `targets` list and hence every request might return a different target
list.

### Request

To retrieve an OONI Run link descriptor, the client issues a request compliant with:

`GET /api/v2/oonirun/links/{oonirun_link_id}/engine-descriptor/{revision}?run_type={timed|manual}&is_charging={true|false}`

Upon receiving this request, the OONI Run backend:

1. SHOULD check whether the `${oonirun_link_id}` exists and return 404 if it does
   not.

2. if everything is okay, returns `200` to the client (see below).

A client should also include the following headers to allow the server to
properly generate dynamic target lists:
* `X-OONI-NetworkInfo`: `<probe_asn>,<probe_cc> (<network_type>)`, eg `AS1234,IT (wifi)`
* `X-OONI-WebsiteCategoryCodes`: comma separated list of category codes that user has chosen to test (eg. NEWS,HUMR)
* `X-OONI-Credentials`: base64 encoded OONI anonymous credentials

The the `platform`, `software_name`, `software_name`, `engine_name` and
`engine_version` are encoded inside of the `User-Agent` string using the following
format:
```
<software_name>/<software_version> (<platform>) <engine_name>/<engine_version> (<engine_version_full>)
```

### Response body

In case of success (i.e. `200` response), the OONI Run Service MUST return the
following JSON body:

```JavaScript
{
   "revision": "1",
   "date_created": ""
   "nettests": [
      {
         // See CREATE response format for other fields
         "targets": [{
            "input": "https://example.com/",
            "extra": {
               "category_code": "HUMR",
            }
         }],
         "test_name": "web_connectivity"
      }
   ]
}
```

Additionally, the `Vary` header should specify the list of headers that affect
the response body caching, which are all headers starting with the `X-OONI-`
prefix.

The server might also return an updated version of the submitted anonymous
credentials using the `X-OONI-Credentials` header.

## 4.7 LIST the OONI Run descriptors

This operation is performed by users of the OONI Run platform to list all the existing OONI Run links.

Authentication for this endpoint is optional.

### Request

To retrieve an OONI Run link descriptor, the client issues a request compliant with:

`GET /api/v2/oonirun/links?only_latest=true&only_mine=true&include_archived=true`

-   `only_latest`, boolean flag to filter only by the latest revision of an OONI
    Run link. If unset or set to false, it will instead include all revisions as
    separate entries.
-   `only_mine` , boolean flag to filter only the links of the logged in user. Will only work when the Authentication header is used.
-   `include_archived` , boolean flag used to indicate if the listing should include archived links as well.

### Response status code

Upon receiving this request, the OONI Run backend:

1. SHOULD check whether the `${oonirun_link_id}` exists and return 404 if it does
   not.

2. if everything is okay, returns `200` to the client (see below).

### Response body

In case of success (i.e. `200` response), the OONI Run Service MUST return the
following JSON body:

```JavaScript
{
   "links": [

      // List of OONI Run links, see CREATE response format for full format.
   ]
}
```

# 5.0 Implementation considerations

Special attention should be placed in ensuring the OONI Run links (which are
mobile deep links) are sharable though various apps.
In particular the format of the OONI Run link should be such that if the URL is
being truncated, it should be visible to the end, as such it's recommend that we
restrict the character set of the `ooni_run_link_id` to just numbers. Since we
might not end up having that many OONI Run link, this also lends itself well to
allowing users to manually type OONI Run links directly into the app. When manually
typing OONI Run links, the OONI Run link might be displayed broken up into
numbers + spaces or dashes to make it easier to type.

Mobile deep links can be registered using two different methods, one is a custom
prefix (ex. `ooni://`), the other is a custom URL prefix (ex.
`https://run.ooni.io/1234`). In our testing we have seen that the custom prefix
is more reliable, yet it has the tradeoff of not allowing us to display a web
page when the user does not have the app installed. As such the recommended
strategy is to encourage users to share the custom URL prefix OONI Run link, but
on the web page itself, in the event that the app did not handle the deep link,
have a link to the custom prefix approach to "force" the opening of the app
(similar to how OONI Run works now).

As such we recommend using the following addresses for OONI Run link and OONI Run descriptor URLs:

* `https://run.ooni.io/{ooni_run_link_id}`, where `{ooni_run_link_id}` is a number

* `ooni://runv2/{ooni_run_link_id}`

* `https://api.ooni.io/api/v1/ooni_run/{ooni_run_link_id}`

# 6.0 Future work

We could at some point host these links on s3 or github and have them
be accessible via URLs in the form:

* `https://raw.githubusercontent.com/ooni/run-links/master/data/{ooni_run_link_id}.json`

* `https://s3.amazonaws.com/ooni-data/ooni-run-links/{ooni_run_link_id}.json`

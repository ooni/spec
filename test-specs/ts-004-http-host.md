# Specification version number

0.2.0

# Specification name

HTTP Host test

# Test preconditions

  * An internet connection.
  * That no special treatment is given to the supplied oonib test helper.

For reporting to the backend to work that it is possible for the probe to
establish a connection to the Tor network.

# Expected impact

  * Ability to determine that the transparent HTTP proxy is doing censorship
    based on the HTTP Host header field.

  * Ability to detect the presence of a Transparent HTTP Proxy

  * Ability to detect which logic is being used by the Transparent proxy to
    censor the target sites and if some circumvention strategies are effective.

  * (optional) if the blockpage is specified if the hostname under analysis is
    being blocked.

# Expected inputs

  * A list of hostnames to be tested

  * The IP address (or hostname) of an oonib HTTPReturnJSONHeadersHelper test
    helper running on port 80.

  * (optional) the content of the blockpage to compare against when processing
    the response.

## Semantics

One per line a list of hostnames, for example:

    torproject.org
    ooni.nu

# Test description

For every given hostname we perform the following series of tests. Once every
test is completed we always perform a fixed set of operations to infer the
presence of a transparent HTTP proxy and/or censorship.

We take the response from our request and check to see if it starts with the
character '{', if it does not we consider that a transparent HTTP proxy is
present.

If not we attempt to parse the response as a JSON string, if it does not parse
we consider a that a transparent HTTP proxy is present.

If the JSON string does parse we look for the following dict keys:

  * 'request_headers'

  * 'request_line'

  * 'headers_dict'

If all of them are present we consider that no transparent HTTP proxy is
present.

If a transparent HTTP proxy is present and the user has specified the content
of the censorship blockpage we compare the response with the known blockpage
and check if they match. If they do match then the hostname is maked as
censored.

These operations are done once for every one of the following tests:

## test_send_host_header

We connect to the backend test helper on port 80 and perform a HTTP GET request
with the Host header field set to the target hostname.

## test_filtering_via_fuzzy_matching

The Host header field contains the hostname prefixed by 10 random characters
and postfixed by 10 random characters.

The purpose of this is to determine if censorship is being triggerred by fuzzy
matching.

## test_filtering_of_subdomain

The Host header field contains a random 10 character subdomain of the target
hostname (`ninechars1.example.com`).

The purpose of this is to determine if also subdomains are being censored.


## test_filtering_add_tab_to_host

The Host header field contains the subdomain postfixed by the tab character
`\t`.

The purpose of this is to determine if by appending a tab character the filter
is being bypassed.

## test_filtering_prepend_newline_to_method

The HTTP Request Line is prefixed with a newline character `\n`.

The purpose of this is to determine if this is a valid filter bypassing
strategy.

XXX move this to a separate test as it does not have much to do with the HTTP
Host field.

# Expected output

## Parent data format

df-001-httpt

## Semantics

'filtering_via_fuzzy_matching': true|false|null
'filtering_prepend_newline_to_method': true|false|null
'filtering_add_tab_to_host': true|false|null
'filtering_of_subdomain': true|false|null

  If the site supplied as input can be reached by using the evasion technique
  this is set to false.

  If the content of the blockpage is specified we make an evaluation of
  censorship or not based on the response matching it or not.

  If the response contains the expect JSON dict returned from the oonib test
  helper then we consider censorship to not be happening ('censorship': False).

  In all other cases 'censorship' is set to null.

'transparent_http_proxy': true|false

  if we have detected the presence of a transparent HTTP proxy or not.

## Possible conclusions

We can say that a certain site is blocked or not and looking at the result we
can understand which censorship bypassing strategies have worked and therefore
understand which censorship device the one being analyzed may be.
## Example output sample

```
{
    "bucket_date": "2015-11-25",
    "data_format_version": "0.2.0",
    "id": "a59899ab-cd33-49db-8ca4-7bf5dd2d317d",
    "input": null,
    "options": [],
    "probe_asn": "AS3269",
    "probe_cc": "IT",
    "probe_ip": "127.0.0.1",
    "report_filename": "2015-11-25/20151125T214003Z-IT-AS3269-http_host-FKByhJTXzseUDZOSvQkPiZur0ji6csV5UCiyarEoCCUCiKicGTgXq06fcJVA6XfA-0.1.0-probe.json",
    "report_id": "FKByhJTXzseUDZOSvQkPiZur0ji6csV5UCiyarEoCCUCiKicGTgXq06fcJVA6XfA",
    "software_name": "ooniprobe",
    "software_version": "1.3.2",
    "test_helpers": {
        "backend": "http://216.156.197.144:80"
    },
    "input_hashes": [],
    "probe_city": null,
    "backend_version": "1.1.4",
    "test_keys": {
        "agent": "agent",
        "filtering_prepend_newline_to_method": false,
        "requests": [
            {
                "request": {
                    "body": null,
                    "headers": {
                        "Host": null
                    },
                    "method": "GET",
                    "tor": {
                        "exit_ip": false,
                        "exit_name": false,
                        "is_tor": false
                    },
                    "url": "http://216.156.197.144:80"
                },
                "response": {
                    "body": "{\"headers_dict\": {\"Connection\": [\"close\"], \"Host\": [\"None\"]}, \"request_line\": \"GET / HTTP/1.1\", \"request_headers\": [[\"Connection\", \"close\"], [\"Host\", \"None\"]]}",
                    "code": 200,
                    "headers": {}
                },
                "response_length": null
            },
            {
                "request": {
                    "body": null,
                    "headers": {
                        "Host": null
                    },
                    "method": "\nGET",
                    "tor": {
                        "exit_ip": false,
                        "exit_name": false,
                        "is_tor": false
                    },
                    "url": "http://216.156.197.144:80"
                },
                "response": {
                    "body": "{\"headers_dict\": {\"Connection\": [\"close\"], \"Host\": [\"None\"]}, \"request_line\": \"\\nGET / HTTP/1.1\", \"request_headers\": [[\"Connection\", \"close\"], [\"Host\", \"None\"]]}",
                    "code": 200,
                    "headers": {}
                },
                "response_length": null
            }
        ],
        "send_host_header": false,
        "socksproxy": null,
        "start_time": 1448484003.0,
        "transparent_http_proxy": false
    },
    "test_name": "http_host",
    "test_runtime": 0.3475949764,
    "test_start_time": "2015-11-25 21:40:03",
    "test_version": "0.2.4"
}
```

# Privacy considerations

If the user is behind a transparent HTTP proxy that sets the X-Forwarded-For
header their IP address will end up being part of the final report.

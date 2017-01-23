# Specification version number

0.2.0

# Specification name

HTTP Requests Test

# Test preconditions

  * An internet connection
  * Ability to reach the Tor network (either Tor is not censored or the user has a Tor bridge)

# Expected impact

The ability to detect which websites are being blocked.

# Expected inputs

## Import document or import data format

A list of URLs to be tested for censorship.

## Semantics

A http URL one per line as per RFC2616 section 3.2.

# Test description

For every URL given as input we perform a HTTP GET request over the probes
network and one over the Tor network.

By default the HTTP User Agent is chosen at random and is different between the
control request and the experiment request.

Since version 0.2.3 the User Agent is chosen at random, but is the same between
the control request and the experiment request.

The user agent is chosen amongst this set of possible user agents:

```
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7",
"Mozilla/5.0 (iPhone; U; CPU iPhone OS 3 1 2 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Mobile/7D11",
"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2) Gecko/20100115 Firefox/3.6",
"Mozilla/5.0 (Windows; U; Windows NT 6.1; de; rv:1.9.2) Gecko/20100115 Firefox/3.6",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2) Gecko/20100115 Firefox/3.6",
"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7 (.NET CLR 3.5.30729)"
```

These user agents are taken from the "How Unique Is Your Web Browser?"
(https://panopticlick.eff.org/browser-uniqueness.pdf) paper as the browser user
agents with largest anonymity set.

We compare the HTTP response body and HTTP response headers to of the request
made over Tor and that made over the probes network for consistency.

The response body is considered to match if the proportion between the body of
the response over Tor and the response over the probes network is greater than
a certain factor (by default 0.8).

# Expected output

## Parent data format

df-001-httpt

## Required output data

* The requests that have been made.

* The received responses.

* If factor between the two response bodies

* If the response bodies appear to match

Present only in test version >= 0.2:

* The difference between the two response headers

* If the two response headers match

Present only in test version >= 0.2.2:

* If the control responses or experiment requests have failed their error
  message.

## Semantics

```
{
    "body_length_match":
        "true|false|null depending on whether or not the body lengths "
        "of the experiment match the control. It is null when no control "
        "or experiment response was retreived."

    "body_proportion":
        "float the proportion between the two response bodies"

    "factor":
        "float the body proportion factor used to assert length equality"
}
```

Only in test version >= 0.2:

```
{
    "headers_diff": [
        "List of the keys of the headers that are different between "
        "the two responses"
    ]

    "headers_match":
      "true|false|null depending on whether or not the headers of the control "
      "and experiment are consistent."
}
```

Only in test version >= 0.2.2:

```
{
    "control_failure":
        "null or string containing the HTTP request error string (for a list of"
        "possible error string see df-000-base section 'Error strings')"

    "experiment_failure":
        "null or string containing the HTTP request error string (for a list of
        "possible error string see df-000-base section 'Error strings')"

}
```

## Possible conclusions

If the website in question is reachable from the probes network.

## Example output sample

```
{
    "bucket_date": "2015-11-22",
    "data_format_version": "0.2.0",
    "id": "07873c37-9441-47e3-93b8-94db10444c64",
    "input": "http://googleusercontent.com/",
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
    "test_helpers": {},
    "backend_version": "1.1.4",
    "input_hashes": [
        "37e60e13536f6afe47a830bfb6b371b5cf65da66d7ad65137344679b24fdccd1"
    ],
    "probe_city": null,
    "test_name": "http_requests",
    "test_runtime": 0.1842639446,
    "test_start_time": "2015-11-22 10:32:02",
    "test_version": "0.2.4"
    "test_keys": {
        "agent": "agent",
        "body_length_match": null,
        "body_proportion": null,
        "control_failure": "socks_host_unreachable",
        "experiment_failure": "dns_lookup_error",
        "factor": 0.8,
        "headers_diff": null,
        "headers_match": null,
        "requests": [
            {
                "failure": "dns_lookup_error",
                "request": {
                    "body": null,
                    "headers": {
                        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; de; rv:1.9.2) Gecko/20100115 Firefox/3.6"
                    },
                    "method": "GET",
                    "tor": {
                        "exit_ip": false,
                        "exit_name": false,
                        "is_tor": false
                    },
                    "url": "http://googleusercontent.com/"
                },
                "response": {
                    "body": null,
                    "headers": {}
                },
                "response_length": null
            },
            {
                "failure": "socks_host_unreachable",
                "request": {
                    "body": null,
                    "headers": {
                        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7"
                    },
                    "method": "GET",
                    "tor": {
                        "exit_ip": null,
                        "exit_name": null,
                        "is_tor": true
                    },
                    "url": "http://googleusercontent.com/"
                },
                "response": {
                    "body": null,
                    "headers": {}
                },
                "response_length": null
            },
            {
                "failure": "dns_lookup_error",
                "request": {
                    "body": null,
                    "headers": {
                        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; de; rv:1.9.2) Gecko/20100115 Firefox/3.6"
                    },
                    "method": "GET",
                    "tor": {
                        "exit_ip": null,
                        "exit_name": null,
                        "is_tor": false
                    },
                    "url": "http://googleusercontent.com/"
                },
                "response": {
                    "body": null,
                    "headers": {}
                },
                "response_length": null
            },
            {
                "failure": "dns_lookup_error",
                "request": {
                    "body": null,
                    "headers": {
                        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; de; rv:1.9.2) Gecko/20100115 Firefox/3.6"
                    },
                    "method": "GET",
                    "tor": {
                        "exit_ip": null,
                        "exit_name": null,
                        "is_tor": false
                    },
                    "url": "http://googleusercontent.com/"
                },
                "response": {
                    "body": null,
                    "headers": {}
                },
                "response_length": null
            },
            {
                "failure": "socks_host_unreachable",
                "request": {
                    "body": null,
                    "headers": {
                        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; de; rv:1.9.2) Gecko/20100115 Firefox/3.6"
                    },
                    "method": "GET",
                    "tor": {
                        "exit_ip": null,
                        "exit_name": null,
                        "is_tor": true
                    },
                    "url": "http://googleusercontent.com/"
                },
                "response": {
                    "body": null,
                    "headers": {}
                },
                "response_length": null
            },
            {
                "failure": "socks_host_unreachable",
                "request": {
                    "body": null,
                    "headers": {
                        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; de; rv:1.9.2) Gecko/20100115 Firefox/3.6"
                    },
                    "method": "GET",
                    "tor": {
                        "exit_ip": null,
                        "exit_name": null,
                        "is_tor": true
                    },
                    "url": "http://googleusercontent.com/"
                },
                "response": {
                    "body": null,
                    "headers": {}
                },
                "response_length": null
            }
        ],
        "socksproxy": null,
        "start_time": 1448184722.0
    }
}
```

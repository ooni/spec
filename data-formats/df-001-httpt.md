# HTTPTest template data format

Data Format Version: 0.2.0

This is the specification of the data format that every test that is
based on ooni.templates.httpt.HTTPTest shall be using.

Third party tests that run HTTP related measurements SHOULD also be using such
data format.

## Specification

```
"agent": "agent|redirect depending on weither the client "
    "will ignore 30X redirects or follow them.",

"socksproxy": "null | IP:PORT of the socksproxy to be used to "
    "perform the experiment requests on",

"requests": [
    {
        "failure": "This will contain an error string for why the "
            "request failed or null if no failure occurred",

        "request": {
            "body": "If the request of the client contains some payload it "
                "will be in here, otherwise it is set to null",

            "headers": {
                "Header-Name": "Header-Value"
            },

            "method": "GET|POST|PUT",
            "tor": {
                "exit_ip": "The address of the Tor exit used for the request or "
                    "null if Tor was not used or the test was run with an older version of ooniprobe.",

                "exit_name": "The name of the Tor exit used for the request or "
                    "null if Tor was not used or the test was run with an older version of ooniprobe.",

                "is_tor": "true|false depending on wether or not "
                    "this request was done over Tor or not."
            },
            "url": "The URL of the request that has been performed."
        },
        "response": {
            "body": "The body of the response or null if not response was found. If the response is binary "
                "then this will be a dictionary containing the format in which the binary data is encoded and "
                "the encoded data (ex. {"format": "base64", "data": "AQI="}). "
                "Currently the only type of format supported is base64.",

            "headers": {
                "Header-Name": "Header-Value"
            }
        },
        "response_length": null
    }
]
```

## Example output

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

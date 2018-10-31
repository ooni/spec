# Specification version number

0.2.0

# Specification name

Header Field Manipulation Test

# Test preconditions

  * An internet connection
  * An ooni-backend providing the http-return-json-headers test helper

For reporting to the backend to work that it is possible for
the probe to establish a connection to the Tor network.

# Expected impact

The ability to determine if HTTP request headers are being manipulated,
inferring the existence of HTTP aware middleboxes.

# Expected inputs

The address of the http-return-json-headers test helper.

## Semantics

A backend must be passed with option -b, e.g.

  ooniprobe manipulation/http_header_field_manipulation -b http://12.34.56.78

Optionally, a yaml file containing request headers may be supplied with option
-h.

# Test description

It performs HTTP requests with request headers that vary capitalization towards
a backend. If the headers reported by the server differ from the ones we sent,
then we have detected tampering.

If the optional headers yaml file is not supplied, the
headers will be constructed as so:

```
{
  "User-Agent": [random.choice(net.userAgents)],
  "Accept":["text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"],
  "Accept-Encoding": ["gzip,deflate,sdch"],
  "Accept-Language": ["en-US,en;q=0.8"],
  "Accept-Charset": ["ISO-8859-1,utf-8;q=0.7,*;q=0.3"],
  "Host": [randomStr(15)+'.com']
}
```

The Host header is a random string of 15 characters + .com
The User-Agent header is randomly selected from one of the following:

```
Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7
Mozilla/5.0 (iPhone; U; CPU iPhone OS 3 1 2 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Mobile/7D11
Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6
Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6
Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6
Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2) Gecko/20100115 Firefox/3.6
Mozilla/5.0 (Windows; U; Windows NT 6.1; de; rv:1.9.2) Gecko/20100115 Firefox/3.6
Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2) Gecko/20100115 Firefox/3.6
Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7
Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7 (.NET CLR 3.5.30729))
```

A request is then made towards the backend.

We have 5 categories of tampering:

## total

The response is not a json object and therefore we were not
able to reach the ooniprobe test backend

## request_line_capitalization

HTTP Request line (e.x. GET / HTTP/1.1) does not match the capitalization we set.

## header_field_number

The number of headers we sent does not match those the backend received.

## header_name_capitalization

The header field names do not match those that we sent.

## header_field_value

The header field value does not match with the one we transmitted.

# Expected output

## Parent data format

df-001-httpt

## Required output data

In addition to the details provided in the parent data format we add to the
report the key 'tampering', which is a dictionary containing the following keys
that correspond to the categories of tampering we detect as well as the
difference between the sent and received headers represented as a list of the
headers not present in both the sent and received headers.

## Semantics

```
{
  "total":
        "true|false if an invalid response was received from the "
        "backend control server.",

  "request_line_capitalization":
        "true|false if the capitalisation of the request method was normalised.",

  "header_name_capitalization":
        "true|false if the header name capitalisation was normalised.",

  "header_field_value":
        "true|false if the value of the headers received by the backend "
        "does not match the value of the headers sent by the probe.",

  "header_field_number":
        "true|false if the number of headers received different than the "
        "number of headers sent."

  "header_name_diff": [
        "The keys of the headers that differ in the request and the response."
   ]
}
```

## Example output sample


```
{
    "bucket_date": "2015-11-29",
    "data_format_version": "0.2.0",
    "id": "3cd95f57-9930-48b9-90b0-67ed20f3adfe",
    "input": null,
    "options": [],
    "probe_asn": "AS12876",
    "probe_cc": "FR",
    "probe_ip": "127.0.0.1",
    "report_filename": "2015-11-29/20151129T230014Z-FR-AS12876-http_header_field_manipulation-no_report_id-0.1.0-probe.json",
    "report_id": null,
    "software_name": "ooniprobe",
    "software_version": "1.3.1",
    "backend_version": "1.1.4",
    "input_hashes": [],
    "probe_city": null,
    "test_helpers": {
        "backend": "http://173.205.4.16:80"
    },
    "test_keys": {
        "agent": "agent",
        "requests": [
            {
                "request": {
                    "body": null,
                    "headers": {
                        "ACCEpT-cHarSET": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
                        "AccEPT-LAngUAge": "en-US,en;q=0.8",
                        "HOSt": "kFR3mwImawc0ivv.com",
                        "aCCePT": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                        "acCEpt-encOdING": "gzip,deflate,sdch",
                        "useR-agEnT": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6"
                    },
                    "method": "get",
                    "tor": {
                        "exit_ip": false,
                        "exit_name": false,
                        "is_tor": false
                    },
                    "url": "http://173.205.4.16:80"
                },
                "response": {
                    "body": "{\"headers_dict\": {\"AccEPT-LAngUAge\": [\"en-US,en;q=0.8\"], \"acCEpt-encOdING\": [\"gzip,deflate,sdch\"], \"HOSt\": [\"kFR3mwImawc0ivv.com\"], \"aCCePT\": [\"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\"], \"useR-agEnT\": [\"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6\"], \"ACCEpT-cHarSET\": [\"ISO-8859-1,utf-8;q=0.7,*;q=0.3\"], \"Connection\": [\"close\"]}, \"request_line\": \"get / HTTP/1.1\", \"request_headers\": [[\"Connection\", \"close\"], [\"AccEPT-LAngUAge\", \"en-US,en;q=0.8\"], [\"acCEpt-encOdING\", \"gzip,deflate,sdch\"], [\"aCCePT\", \"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\"], [\"useR-agEnT\", \"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6\"], [\"ACCEpT-cHarSET\", \"ISO-8859-1,utf-8;q=0.7,*;q=0.3\"], [\"HOSt\", \"kFR3mwImawc0ivv.com\"]]}",
                    "code": 200,
                    "headers": {}
                },
                "response_length": null
            }
        ],
        "socksproxy": null,
        "start_time": 1448834414.0,
        "tampering": {
            "header_field_name": false,
            "header_field_number": false,
            "header_field_value": false,
            "header_name_capitalization": false,
            "header_name_diff": [],
            "request_line_capitalization": false,
            "total": false
        }
    },
    "test_name": "http_header_field_manipulation",
    "test_runtime": 0.4789488316,
    "test_start_time": "2015-11-29 23:00:14",
    "test_version": "0.1.5"
}
```

# Privacy considerations

If the user is behind a transparent HTTP proxy that sets the X-Forwarded-For
header their IP address will end up being part of the final report.

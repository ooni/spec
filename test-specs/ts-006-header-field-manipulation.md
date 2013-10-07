# Specification version number

2013-10-07-000

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

{
  "User-Agent": [random.choice(net.userAgents)],
  "Accept":["text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"],
  "Accept-Encoding": ["gzip,deflate,sdch"],
  "Accept-Language": ["en-US,en;q=0.8"],
  "Accept-Charset": ["ISO-8859-1,utf-8;q=0.7,*;q=0.3"],
  "Host": [randomStr(15)+'.com']
}

The Host header is a random string of 15 characters + .com
The User-Agent header is randomly selected from one of the following:

[
  "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7",
  "Mozilla/5.0 (iPhone; U; CPU iPhone OS 3 1 2 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Mobile/7D11",
  "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6",
  "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6",
  "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6",
  "Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2) Gecko/20100115 Firefox/3.6",
  "Mozilla/5.0 (Windows; U; Windows NT 6.1; de; rv:1.9.2) Gecko/20100115 Firefox/3.6",
  "Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2) Gecko/20100115 Firefox/3.6",
  "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7",
  "Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7 (.NET CLR 3.5.30729)")
]

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

df-001-httpt-000

## Required output data

In addition to the details provided in the parent data format we add to the
report the key 'tampering', which is a dictionary containing the following keys
that correspond to the categories of tampering we detect as well as the
difference between the sent and received headers represented as a list of the
headers not present in both the sent and received headers.

## Semantics

{
  'total': True|False,
  'request_line_capitalization': True|False,
  'header_name_capitalization': True|False,
  'header_field_value': True|False,
  'header_field_number': True|False
  'header_name_diff': []
}

## Example output sample

  ###########################################
  # OONI Probe Report for http_header_field_manipulation (0.1.3)
  # Wed Oct  9 10:57:42 2013
  ###########################################
  ---
  input_hashes: []
  options: [-b, 'http://12.34.56.78']
  probe_asn: AS1234
  probe_cc: US
  probe_ip: 127.0.0.1
  software_name: ooniprobe
  software_version: 1.0.0-rc3
  start_time: 1381316262.744312
  test_name: http_header_field_manipulation
  test_version: 0.1.3
  ...
  ---
  agent: agent
  input: null
  requests:
  - request:
      body: null
      headers:
      - - ACCePT-LAnGuagE
        - ['en-US,en;q=0.8']
      - - aCCEPT-ENcODInG
        - ['gzip,deflate,sdch']
      - - aCcEPT
        - ['text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8']
      - - User-AGeNt
        - ['Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.7) Gecko/20091221
            Firefox/3.5.7']
      - - aCCEpt-cHArSEt
        - ['ISO-8859-1,utf-8;q=0.7,*;q=0.3']
      - - HOsT
        - [KIXnnZDJfGKRNab.com]
      method: GET
      url: http://12.34.56.78
    response:
      body: '{"headers_dict": {"ACCePT-LAnGuagE": ["en-US,en;q=0.8"], "aCCEPT-ENcODInG":
        ["gzip,deflate,sdch"], "HOsT": ["KIXnnZDJfGKRNab.com"], "aCcEPT": ["text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"],
        "User-AGeNt": ["Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.7)
        Gecko/20091221 Firefox/3.5.7"], "aCCEpt-cHArSEt": ["ISO-8859-1,utf-8;q=0.7,*;q=0.3"],
        "Connection": ["close"]}, "request_line": "GET / HTTP/1.1", "request_headers":
        [["Connection", "close"], ["ACCePT-LAnGuagE", "en-US,en;q=0.8"], ["aCCEPT-ENcODInG",
        "gzip,deflate,sdch"], ["aCcEPT", "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"],
        ["User-AGeNt", "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.7)
        Gecko/20091221 Firefox/3.5.7"], ["aCCEpt-cHArSEt", "ISO-8859-1,utf-8;q=0.7,*;q=0.3"],
        ["HOsT", "KIXnnZDJfGKRNab.com"]]}'
      code: 200
      headers: []
  socksproxy: null
  tampering:
    header_field_name: false
    header_field_number: false
    header_field_value: false
    header_name_capitalization: false
    header_name_diff: []
    request_line_capitalization: false
    total: false
  ...
  ---
  agent: agent
  input: null
  requests:
  - request:
      body: null
      headers:
      - - accePt-LAnguAGE
        - ['en-US,en;q=0.8']
      - - AcCEpT-eNCOdinG
        - ['gzip,deflate,sdch']
      - - accept
        - ['text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8']
      - - UseR-aGENt
        - ['Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2) Gecko/20100115 Firefox/3.6']
      - - aCcEPT-cHARSeT
        - ['ISO-8859-1,utf-8;q=0.7,*;q=0.3']
      - - HoSt
        - [AjzqKfZkMpoRf8r.com]
      method: POst
      url: http://12.34.56.78
    response:
      body: '{"headers_dict": {"accePt-LAnguAGE": ["en-US,en;q=0.8"], "AcCEpT-eNCOdinG":
        ["gzip,deflate,sdch"], "HoSt": ["AjzqKfZkMpoRf8r.com"], "accept": ["text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"],
        "UseR-aGENt": ["Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2) Gecko/20100115
        Firefox/3.6"], "aCcEPT-cHARSeT": ["ISO-8859-1,utf-8;q=0.7,*;q=0.3"], "Connection":
        ["close"]}, "request_line": "POst / HTTP/1.1", "request_headers": [["Connection",
        "close"], ["accePt-LAnguAGE", "en-US,en;q=0.8"], ["AcCEpT-eNCOdinG", "gzip,deflate,sdch"],
        ["accept", "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"],
        ["UseR-aGENt", "Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2) Gecko/20100115
        Firefox/3.6"], ["aCcEPT-cHARSeT", "ISO-8859-1,utf-8;q=0.7,*;q=0.3"], ["HoSt",
        "AjzqKfZkMpoRf8r.com"]]}'
      code: 200
      headers: []
  socksproxy: null
  tampering:
    header_field_name: false
    header_field_number: false
    header_field_value: false
    header_name_capitalization: false
    header_name_diff: []
    request_line_capitalization: false
    total: false
  ...
  ---
  agent: agent
  input: null
  requests:
  - request:
      body: null
      headers:
      - - Accept-Language
        - ['en-US,en;q=0.8']
      - - Accept-Encoding
        - ['gzip,deflate,sdch']
      - - Accept
        - ['text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8']
      - - User-Agent
        - ['Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2) Gecko/20100115
            Firefox/3.6']
      - - Accept-Charset
        - ['ISO-8859-1,utf-8;q=0.7,*;q=0.3']
      - - Host
        - [NViZZh58LWHFnyp.com]
      method: PUT
      url: http://12.34.56.78
    response:
      body: '{"headers_dict": {"Accept-Language": ["en-US,en;q=0.8"], "Accept-Encoding":
        ["gzip,deflate,sdch"], "Host": ["NViZZh58LWHFnyp.com"], "Accept": ["text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"],
        "User-Agent": ["Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2) Gecko/20100115
        Firefox/3.6"], "Accept-Charset": ["ISO-8859-1,utf-8;q=0.7,*;q=0.3"], "Connection":
        ["close"]}, "request_line": "PUT / HTTP/1.1", "request_headers": [["Connection",
        "close"], ["Accept-Language", "en-US,en;q=0.8"], ["Accept-Encoding", "gzip,deflate,sdch"],
        ["Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"],
        ["User-Agent", "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2) Gecko/20100115
        Firefox/3.6"], ["Accept-Charset", "ISO-8859-1,utf-8;q=0.7,*;q=0.3"], ["Host",
        "NViZZh58LWHFnyp.com"]]}'
      code: 200
      headers: []
  socksproxy: null
  tampering:
    header_field_name: false
    header_field_number: false
    header_field_value: false
    header_name_capitalization: false
    header_name_diff: []
    request_line_capitalization: false
    total: false
  ...
  ---
  agent: agent
  input: null
  requests:
  - request:
      body: null
      headers:
      - - AccepT-langUaGe
        - ['en-US,en;q=0.8']
      - - aCcePT-ENcoDing
        - ['gzip,deflate,sdch']
      - - ACCEpT
        - ['text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8']
      - - uSER-agent
        - ['Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.7) Gecko/20091221
            Firefox/3.5.7 (.NET CLR 3.5.30729)']
      - - aCCept-CHaRSEt
        - ['ISO-8859-1,utf-8;q=0.7,*;q=0.3']
      - - HoSt
        - [48wD518oXAV1pzv.com]
      method: pUT
      url: http://12.34.56.78
    response:
      body: '{"headers_dict": {"AccepT-langUaGe": ["en-US,en;q=0.8"], "aCcePT-ENcoDing":
        ["gzip,deflate,sdch"], "HoSt": ["48wD518oXAV1pzv.com"], "ACCEpT": ["text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"],
        "uSER-agent": ["Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.7) Gecko/20091221
        Firefox/3.5.7 (.NET CLR 3.5.30729)"], "aCCept-CHaRSEt": ["ISO-8859-1,utf-8;q=0.7,*;q=0.3"],
        "Connection": ["close"]}, "request_line": "pUT / HTTP/1.1", "request_headers":
        [["Connection", "close"], ["AccepT-langUaGe", "en-US,en;q=0.8"], ["aCcePT-ENcoDing",
        "gzip,deflate,sdch"], ["ACCEpT", "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"],
        ["uSER-agent", "Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.7) Gecko/20091221
        Firefox/3.5.7 (.NET CLR 3.5.30729)"], ["aCCept-CHaRSEt", "ISO-8859-1,utf-8;q=0.7,*;q=0.3"],
        ["HoSt", "48wD518oXAV1pzv.com"]]}'
      code: 200
      headers: []
  socksproxy: null
  tampering:
    header_field_name: false
    header_field_number: false
    header_field_value: false
    header_name_capitalization: false
    header_name_diff: []
    request_line_capitalization: false
    total: false
  ...
  ---
  agent: agent
  input: null
  requests:
  - request:
      body: null
      headers:
      - - accEpt-LANGuAGE
        - ['en-US,en;q=0.8']
      - - aCcepT-ENCoDIng
        - ['gzip,deflate,sdch']
      - - AccEpT
        - ['text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8']
      - - uSEr-AGenT
        - ['Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2) Gecko/20100115
            Firefox/3.6']
      - - aCCEPT-cHarseT
        - ['ISO-8859-1,utf-8;q=0.7,*;q=0.3']
      - - hoSt
        - [XJs7REREvvxO3wL.com]
      method: geT
      url: http://12.34.56.78
    response:
      body: '{"headers_dict": {"accEpt-LANGuAGE": ["en-US,en;q=0.8"], "aCcepT-ENCoDIng":
        ["gzip,deflate,sdch"], "hoSt": ["XJs7REREvvxO3wL.com"], "AccEpT": ["text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"],
        "uSEr-AGenT": ["Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2) Gecko/20100115
        Firefox/3.6"], "aCCEPT-cHarseT": ["ISO-8859-1,utf-8;q=0.7,*;q=0.3"], "Connection":
        ["close"]}, "request_line": "geT / HTTP/1.1", "request_headers": [["Connection",
        "close"], ["accEpt-LANGuAGE", "en-US,en;q=0.8"], ["aCcepT-ENCoDIng", "gzip,deflate,sdch"],
        ["AccEpT", "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"],
        ["uSEr-AGenT", "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2) Gecko/20100115
        Firefox/3.6"], ["aCCEPT-cHarseT", "ISO-8859-1,utf-8;q=0.7,*;q=0.3"], ["hoSt",
        "XJs7REREvvxO3wL.com"]]}'
      code: 200
      headers: []
  socksproxy: null
  tampering:
    header_field_name: false
    header_field_number: false
    header_field_value: false
    header_name_capitalization: false
    header_name_diff: []
    request_line_capitalization: false
    total: false
  ...
  ---
  agent: agent
  input: null
  requests:
  - request:
      body: null
      headers:
      - - Accept-Language
        - ['en-US,en;q=0.8']
      - - Accept-Encoding
        - ['gzip,deflate,sdch']
      - - Accept
        - ['text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8']
      - - User-Agent
        - ['Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2) Gecko/20100115 Firefox/3.6']
      - - Accept-Charset
        - ['ISO-8859-1,utf-8;q=0.7,*;q=0.3']
      - - Host
        - [iIjXcFcLGv8WHMk.com]
      method: POST
      url: http://12.34.56.78
    response:
      body: '{"headers_dict": {"Accept-Language": ["en-US,en;q=0.8"], "Accept-Encoding":
        ["gzip,deflate,sdch"], "Host": ["iIjXcFcLGv8WHMk.com"], "Accept": ["text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"],
        "User-Agent": ["Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2) Gecko/20100115
        Firefox/3.6"], "Accept-Charset": ["ISO-8859-1,utf-8;q=0.7,*;q=0.3"], "Connection":
        ["close"]}, "request_line": "POST / HTTP/1.1", "request_headers": [["Connection",
        "close"], ["Accept-Language", "en-US,en;q=0.8"], ["Accept-Encoding", "gzip,deflate,sdch"],
        ["Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"],
        ["User-Agent", "Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2) Gecko/20100115
        Firefox/3.6"], ["Accept-Charset", "ISO-8859-1,utf-8;q=0.7,*;q=0.3"], ["Host",
        "iIjXcFcLGv8WHMk.com"]]}'
      code: 200
      headers: []
  socksproxy: null
  tampering:
    header_field_name: false
    header_field_number: false
    header_field_value: false
    header_name_capitalization: false
    header_name_diff: []
    request_line_capitalization: false
    total: false
  ...

# Privacy considerations

If the user is behind a transparent HTTP proxy that sets the X-Forwarded-For
header their IP address will end up being part of the final report.

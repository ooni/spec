# Specification version number

2015-10-11-000

# Specification name

Psiphon Test

# Test preconditions

Have psiphon-circumvention-system (including psiphon-circumvention-system/pyclient/psi_client.py) cloned in the home of the user that runs ooni or somewhere else accessible to the user that runs ooni.

# Expected impact

Ability to measure whether Psiphon is working from the given network vantage point.

# Expected inputs

Optionally:
A single URL to fetch, supplied by command line argument "--url (-u)".
Psiphon path, specified by the command line argument "--psiphonpath (-p)"
The ip:port that Psiphon will use for the SOCKS proxy, with the command line argument "--socksproxy (-s)"

# Test description

This test first check that the Psiphon path exists, then launches Psiphon and parses output to determine if it has bootstrapped. After bootstrap, it fetches google.com (or other URL specified by the --url argument) using Psiphons SOCKS proxy listening on 127.0.0.1:1080 (or otherwise specified by the --socksproxy argument).

The specific string used to determine bootstrap from Psiphon output in version
"0.0.1" is "Press Ctrl-C to terminate." from standard output.

# Expected output

## Parent data format

The following keys from df-001-httpt.md are used when Psiphon bootstraps: requests, socksproxy, agent.
When Psiphon is not installed or does not bootstrap, only agent and socksproxy are used.

## Required output data

psiphon_installed:
**boolean** Whether Psiphon client is found or not (success or failure).

success:
**boolean** The bootstrap status of Psiphon (success or failure).

/tmp/<temporary file>:
**dictionary** the parent key of Psiphon's output that contains the keys stdout and stderr and exit_reason

stdout:
**string** Output produced by Psiphon's standard output.

stderr:
**string** Error produced by Psiphon's standard error.

## Data specification version number

## Semantics

    'psiphon_installed' - True or False - whether Psiphon is found.
    'success' - True or False - whether Psiphon has bootstrapped.
    'body' - http page body if successfully requested.
    '/tmp/<temporary file>': 
      'stdout' - Contents of standard output produced by Psiphon.
      'stderr' - Contents of standard error produced by Psiphon.


## Possible conclusions

We can determine whether or not Psiphon is found.
We can determine whether or not Psiphon is able to bootstrap, according to its output.
We can determine whether or not a given URL is reachable via Psiphon.

## Example output sample
```
---
input_hashes: []
options: [-u, google.com]
probe_asn: AS0
probe_cc: ZZ
probe_city: null
probe_ip: 127.0.0.1
report_id: 4dAHr0ceNDBmw5lUQ7pBoxqgyUSfP873Qj1zv5VyElnSSTXwcsLYeCv69DsUjb94
software_name: ooniprobe
software_version: 1.3.1
start_time: 1444686051.0
test_helpers: {}
test_name: psiphon_test
test_version: 0.0.1
...
---
/tmp/tmplKg8K3: {exit_reason: process_done, stderr: '', stdout: "./ssh is not a valid\
    \ executable. Using standard ssh.\r\n\r\nYour SOCKS proxy is now running at 127.0.0.1:1080\r\
    \n\r\nPress Ctrl-C to terminate.\r\nTerminating...\r\nConnection closed\r\n"}
agent: agent
input: null
psiphon_installed: true
requests:
- request:
    body: null
    headers: []
    method: GET
    tor: {is_tor: false}
    url: http://google.com
  response:
    body: "<HTML><HEAD><meta http-equiv=\"content-type\" content=\"text/html;charset=utf-8\"\
      >\n<TITLE>301 Moved</TITLE></HEAD><BODY>\n<H1>301 Moved</H1>\nThe document has\
      \ moved\n<A HREF=\"http://www.google.com/\">here</A>.\r\n</BODY></HTML>\r\n"
    code: 301
    headers:
    - - Content-Length
      - ['219']
    - - X-XSS-Protection
      - [1; mode=block]
    - - Expires
      - ['Wed, 11 Nov 2015 21:40:58 UTC']
    - - Server
      - [gws]
    - - Connection
      - [close]
    - - Location
      - ['http://www.google.com/']
    - - Cache-Control
      - ['public, max-age=2592000']
    - - Date
      - ['Mon, 12 Oct 2015 21:40:58 UTC']
    - - X-Frame-Options
      - [SAMEORIGIN]
    - - Content-Type
      - [text/html; charset=UTF-8]
socksproxy: 127.0.0.1:1080
test_runtime: 7.373162031173706
test_start_time: 1444686052.0
...
```

## Expected Post-processing efforts

# Privacy considerations

Psiphon does not seek to provide anonymity. 
An adversary can observe that a user is connecting to Psiphon servers.
Psiphon servers can also determine the users location.

# Packet capture considerations

This test does not capture packets by default.

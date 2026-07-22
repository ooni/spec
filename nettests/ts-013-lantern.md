# Specification version number

0.1.0

* _status_: obsolete

# Specification name

Lantern Test

# Test preconditions

Downloaded or compiled the "lantern" binary and made executable and in
the users PATH environment variable.

# Expected impact

Ability to measure whether Lantern is working from the given network vantage point.

# Expected inputs

None

# Test description

This test launches Lantern in --headless mode, and parses output to determine
if it has bootstrapped.  After bootstrap, it fetches a URL using Lanterns HTTP
proxy interface listening on 127.0.0.1.8787 and checks to see if the response
body matches the expected result.
As a URL for testing we use http://www.google.com/humans.txt and look for the
string "Google is built by a large" in the response body.

The specific string used to determine bootstrap from Lantern output in version
"2.0.10" is "Successfully dialed via" from standard output.

# Expected output

## Parent data format

None.

## Required output data

success:
**boolean** The bootstrap status of Lantern (success or failure).

lantern --headless:
**dictionary** the parent key of Lanterns output that contains the keys stdout and stderr

stdout:
**string** Output produced by Lanterns standard output.

stderr:
**string** Error produced by Lanterns standard error.

body:
**string** The page body of a successful HTTP request.

failure:
**string** If failure, then the corresponding failure message.


## Data specification version number

## Semantics

'success' - True or False - whether Lantern has bootstrapped.
'body' - http page body if successfully requested.
'failure' - optional, present if there is a failure.
'lantern --headless':
  'stdout' - Contents of standard output produced by Lantern.
  'stderr' - Contents of standard error produced by Lantern.
'default_configuration' - True or False - whether it is using the default, sane, configuration or not

## Possible conclusions

We can determine whether or not Lantern is able to bootstrap, according to its output.
We can determine whether or not a URL is reachable via Lantern.

## Example output sample
```
---
input_hashes: []
options: []
probe_asn: AS1234
probe_cc: US
probe_city: null
probe_ip: 127.0.0.1
software_name: ooniprobe
software_version: 1.2.3-rc1
start_time: 1428344311.0
test_name: lantern_circumvention_tool_test
test_version: 0.1.0
...
---
body: "Google is built by a large team of engineers, designers, researchers, robots, and others in many different sites across the globe. It is updated continuously, and built with more tools and technologies than we can shake a stick at. If you'd like to help us out, see google.com/careers."
bootstrapped: true
default_configuration: true
input: null
lantern --headless: {exit_reason: process_done, stderr: '', stdout: ''}
```

## Expected Post-processing efforts

You should be aware of the `default_confguration` parameter as the user may
have misconfigured the test leading to inconsistent results.

# Privacy considerations

Lantern does not seek to provide anonymity. Lantern contains tracking analytics
software and may connect directly to Lantern-provided proxy endpoints, or use
fronted domains via Content Delivery Networks (CDNs) as a data channel.

# Packet capture considerations

This test does not capture packets by default.

# Specification version number

0.1.0

* _status_: obsolete

# Specification name

Vanilla Tor Test

# Test preconditions

* An internet connection

* Tor is installed

# Expected impact

Ability to determine if Tor in it's default configuration is able to bootstrap
or at what point in bootstrapping it fails.

# Expected inputs

None

# Test description

The test will run the tor executable and monitor the standard
output looking for a line in it's output indicating it has
bootstrapped to 100%.

# Expected output

## Parent data format

None

## Required output data

A flag to indicate if we were able to establish a Tor connection.

## Semantics

error:
    **string** indicating that an error occurred

    timeout-reached: to indicate tor was unable to bootstrap in the allocated time.

    null: no error was detected.

success:
    **boolean** indiciating if whether or not we were able to connect to the
    Tor network.

    True: indicates that we reached 100% bootstrap

    False: indicates that we were unable to reach 100% bootstrap before the
    timeout was reached.

    null: indicates that tor exited before we were able to complete the test,
    this can be due to some unhandled error.


timeout:
    **integer** indicating the timeout, in seconds, after which we should
    consider Tor as not working. The default it is set to 200 seconds.

transport_name:
    **string** always set to vanilla

tor_version:
    **string** indicating the version string of the tor client being used.

tor_progress:
    **integer** indicating the percentage of tor bootstrapping at which we
    stopped.

tor_progress_tag:
    **string** a string giving a textual description of what the progress
    percentage means.

tor_progress_summary:
    **string** a more verbose string giving a textual description of what the
    progress percentage state is.

tor_log:
    **string** notice level log output of tor.

## Possible conclusions

If Tor with the default configuration can successfully bootstrap.

## Example output sample

```
###########################################
# OONI Probe Report for vanilla_tor (0.1.0)
# Tue Mar 15 15:09:33 2016
###########################################
---
annotations: null
input_hashes: []
options: []
probe_asn: AS0
probe_cc: ZZ
probe_city: null
probe_ip: 127.0.0.1
report_id: wvKi9dtBJXFub4lBSwgcA0DZDiCJ38DRjhh3rYeBOwpwfJ0bfUznBLva5djRFOHR
software_name: ooniprobe
software_version: 1.3.2
start_time: 1458047373.0
test_helpers: {}
test_name: vanilla_tor
test_version: 0.1.0
...
---
{error: null, input: null, success: true, test_runtime: 7.101379871368408, test_start_time: 1458047374.0,
  timeout: 200, tor_log: 'Mar 15 15:09:34.000 [notice] Tor 0.2.6.10 (git-58c51dc6087b0936)
    opening new log file.

    Mar 15 15:09:34.063 [warn] OpenSSL version from headers does not match the version
    we''re running with. If you get weird crashes, that might be why. (Compiled with
    1000204f: OpenSSL 1.0.2d 9 Jul 2015; running with 1000206f: OpenSSL 1.0.2f  28
    Jan 2016).

    Mar 15 15:09:34.064 [notice] Tor v0.2.6.10 (git-58c51dc6087b0936) running on Darwin
    with Libevent 2.0.22-stable, OpenSSL 1.0.2f and Zlib 1.2.5.

    Mar 15 15:09:34.082 [notice] Tor can''t help you if you use it wrong! Learn how
    to be safe at https://www.torproject.org/download/download#warning

    Mar 15 15:09:34.121 [notice] Configuration file "/non-existant" not present, using
    reasonable defaults.

    Mar 15 15:09:34.172 [notice] Opening Socks listener on 127.0.0.1:1886

    Mar 15 15:09:34.173 [notice] Opening Control listener on 127.0.0.1:27345

    Mar 15 15:09:34.000 [notice] Parsing GEOIP IPv4 file /usr/local/Cellar/tor/0.2.6.10/share/tor/geoip.

    Mar 15 15:09:34.000 [notice] Parsing GEOIP IPv6 file /usr/local/Cellar/tor/0.2.6.10/share/tor/geoip6.

    Mar 15 15:09:34.000 [notice] Bootstrapped 0%: Starting

    Mar 15 15:09:34.000 [notice] New control connection opened from 127.0.0.1.

    Mar 15 15:09:34.000 [notice] Tor 0.2.6.10 (git-58c51dc6087b0936) opening log file.

    Mar 15 15:09:35.000 [notice] Bootstrapped 5%: Connecting to directory server

    Mar 15 15:09:35.000 [notice] Bootstrapped 10%: Finishing handshake with directory
    server

    Mar 15 15:09:35.000 [notice] Bootstrapped 15%: Establishing an encrypted directory
    connection

    Mar 15 15:09:35.000 [notice] Bootstrapped 20%: Asking for networkstatus consensus

    Mar 15 15:09:35.000 [notice] Bootstrapped 25%: Loading networkstatus consensus

    Mar 15 15:09:36.000 [notice] I learned some more directory information, but not
    enough to build a circuit: We have no usable consensus.

    Mar 15 15:09:36.000 [notice] Bootstrapped 40%: Loading authority key certs

    Mar 15 15:09:36.000 [notice] Bootstrapped 45%: Asking for relay descriptors

    Mar 15 15:09:36.000 [notice] I learned some more directory information, but not
    enough to build a circuit: We need more microdescriptors: we have 0/7138, and
    can only build 0% of likely paths. (We have 0% of guards bw, 0% of midpoint bw,
    and 0% of exit bw = 0% of path bw.)

    Mar 15 15:09:37.000 [notice] Bootstrapped 50%: Loading relay descriptors

    Mar 15 15:09:38.000 [notice] Bootstrapped 57%: Loading relay descriptors

    Mar 15 15:09:38.000 [notice] Bootstrapped 66%: Loading relay descriptors

    Mar 15 15:09:39.000 [notice] Bootstrapped 72%: Loading relay descriptors

    Mar 15 15:09:39.000 [notice] Bootstrapped 78%: Loading relay descriptors

    Mar 15 15:09:39.000 [notice] Bootstrapped 80%: Connecting to the Tor network

    Mar 15 15:09:39.000 [notice] Bootstrapped 90%: Establishing a Tor circuit

    Mar 15 15:09:41.000 [notice] Tor has successfully opened a circuit. Looks like
    client functionality is working.

    Mar 15 15:09:41.000 [notice] Bootstrapped 100%: Done

    Mar 15 15:09:41.000 [notice] Catching signal TERM, exiting cleanly.

    ', tor_progress: 100, tor_progress_summary: Done, tor_progress_tag: done, tor_version: 0.2.6.10,
  transport_name: vanilla}
...                                                                                                                                                                                     ''}
```

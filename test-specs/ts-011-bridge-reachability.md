# Specification version number

2014-08-06-001

# Specification name

Bridge Reachability Test

# Test preconditions

* An internet connection

# Expected impact

Ability to detect which bridges are working from the given network vantage
point.

# Expected inputs

A list of bridge IP addressed, port numbers and pluggable transport type (when
applicable).

## Semantics

They should be in a flat text file one per line in the format:

    IP:ORPort

Example:

    203.0.113.27:1828
    198.51.100.45:9045

For normal Tor bridges.

For pluggable transport bridges the format is:

    TransportType IP:ORPort

Example:
  
    obfs2 203.0.113.27:1828
    obfs3 198.51.100.45:9045


# Test description

For every bridge specified as input a new tor instance is started and it is
instructed to connect to Tor using that bridge. It will try to bootstrap to
100% and either succeed or timeout after a default time of 120 seconds.

# Expected output

## Parent data format

None.

## Required output data

* The bridge address used in the measurement (bridge_address).

* Whether or not it succeeded in connecting to the Tor networking using the
  specified bridge (success).

* The bootstrap percentage at which the test timed out (tor_progress).

* The name of the transport used (transport_name).

## Semantics

error:
    **string** indicating that an error occurred when running the test on the
    given input.

    unsupported-tor-version: to indicate that the version of tor is too old to
    connect to the specified bridge.

    missing-pyobfsproxy: to indicate that obfsproxy is not installed.

    missing-fteproxy: to indicate that fteproxy is not installed.

    null: no error was detected.

success:
    **boolean** indiciating if whether or not we were able to establish a
    connection to the Tor network with the supplied bridge.

    True: indicates that we reached 100% bootstrap

    False: indicates that we were unable to reach 100% bootstrap before the
    timeout was reached.

    null: indicates that tor exited before we were able to complete the test,
    this can be due to some unhandled error.


timeout:
    **integer** indicating the timeout, in seconds, after which we should
    consider the bridge non-functioning. By default it is set to 120 seconds.

transport_name:
    **string** indicating the name of transport name used by the bridge.
    
    vanilla: a regular, non pluggable transport, bridge.

    obfs2: for [obfs2 obfsproxy](https://gitweb.torproject.org/pluggable-transports/obfsproxy.git/blob/HEAD:/obfsproxy/transports/obfs2.py).

    obfs3: for [obfs3 obfsproxy](https://gitweb.torproject.org/pluggable-transports/obfsproxy.git/blob/HEAD:/obfsproxy/transports/obfs3.py).

    obfs4: for [obfs4 obfsproxy](https://gitweb.torproject.org/pluggable-transports/obfs4.git/tree/obfs4proxy/obfs4proxy.go).

    fte: for [fte-proxy](https://fteproxy.org/)

    scramblesuit: for [ScrambleSuit](http://www.cs.kau.se/philwint/scramblesuit/)

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

bridge_address:
    **string** the address of the bridge being used.

obfsproxy_version (since 0.1.1):
    **string** indicating the version string of the obfsproxy client being used.

obfsproxy_log (since 0.1.2):
    **string** info level log output of obfsproxy

## Possible conclusions

Which bridges are functioning from the given network vantage point and which
ones are not.

## Example output sample

```
###########################################
# OONI Probe Report for bridge_reachability (0.1)
# Thu Aug  7 16:10:50 2014
###########################################
---
input_hashes: [595c8ad9b63ff9f142eca6296021990df6367ab03b3c4eb1c69a8747f0cd41a1]
options: [-f, bridges.txt]
probe_asn: AS3269
probe_cc: IT
probe_city: null
probe_ip: 127.0.0.1
software_name: ooniprobe
software_version: 1.0.2
start_time: 1407420650.560137
test_name: bridge_reachability
test_version: '0.1'
...
---
{bridge_address: '169.229.59.74:31493', error: null, input: 'obfs3 169.229.59.74:31493
    AF9F66B7B04F8FF6F32D455F05135250A16543C9', success: true, timeout: 120, tor_log: null,
  tor_progress: 100, tor_progress_summary: Done, tor_progress_tag: done, tor_version: 0.2.4.20,
  transport_name: obfs3}
...
---
{bridge_address: '169.229.59.75:46328', error: null, input: 'obfs3 169.229.59.75:46328
    AF9F66B7B04F8FF6F32D455F05135250A16543C9', success: true, timeout: 120, tor_log: null,
  tor_progress: 100, tor_progress_summary: Done, tor_progress_tag: done, tor_version: 0.2.4.20,
  transport_name: obfs3}
...
---
{bridge_address: '208.79.90.242:35658', error: null, input: 'obfs3 208.79.90.242:35658
    BA61757846841D64A83EA2514C766CB92F1FB41F', success: true, timeout: 120, tor_log: null,
  tor_progress: 100, tor_progress_summary: Done, tor_progress_tag: done, tor_version: 0.2.4.20,
  transport_name: obfs3}
...
---
{bridge_address: '83.212.100.216:47870', error: null, input: 'obfs2 83.212.100.216:47870
    1F01A7BB60F49FC96E0850A6BAD6D076DFEFAF80', success: false, timeout: 120, tor_log: '',
  tor_progress: 0, tor_progress_summary: null, tor_progress_tag: null, tor_version: 0.2.4.20,
  transport_name: obfs2}
...
---
{bridge_address: '83.212.96.182:46602', error: null, input: 'obfs2 83.212.96.182:46602
    6F058CBEF888EB20D1DEB9886909F1E812245D41', success: false, timeout: 120, tor_log: '',
  tor_progress: 0, tor_progress_summary: null, tor_progress_tag: null, tor_version: 0.2.4.20,
  transport_name: obfs2}
...
---
{bridge_address: '70.182.182.109:54542', error: null, input: 'obfs2 70.182.182.109:54542
    94C9E691688FAFDEC701A0788BD15BE8AD34ED35', success: false, timeout: 120, tor_log: '',
  tor_progress: 0, tor_progress_summary: null, tor_progress_tag: null, tor_version: 0.2.4.20,
  transport_name: obfs2}
...
---
{bridge_address: '128.31.0.34:1051', error: null, input: 'obfs2 128.31.0.34:1051 CA7434F14A898C7D3427B8295A7F83446BC7F496',
  success: false, timeout: 120, tor_log: '', tor_progress: 0, tor_progress_summary: null,
  tor_progress_tag: null, tor_version: 0.2.4.20, transport_name: obfs2}
...
---
{bridge_address: '83.212.101.2:45235', error: null, input: 'obfs2 83.212.101.2:45235
    2ADFE7AA8D272C520D1FBFBF4E413F3A1B26313D', success: false, timeout: 120, tor_log: '',
  tor_progress: 0, tor_progress_summary: null, tor_progress_tag: null, tor_version: 0.2.4.20,
  transport_name: obfs2}
...
---
{bridge_address: '83.212.101.2:42782', error: null, input: 'obfs3 83.212.101.2:42782
    2ADFE7AA8D272C520D1FBFBF4E413F3A1B26313D', success: false, timeout: 120, tor_log: '',
  tor_progress: 0, tor_progress_summary: null, tor_progress_tag: null, tor_version: 0.2.4.20,
  transport_name: obfs3}
...
---
{bridge_address: '83.212.101.2:443', error: null, input: 'obfs3 83.212.101.2:443 2ADFE7AA8D272C520D1FBFBF4E413F3A1B26313D',
  success: false, timeout: 120, tor_log: '', tor_progress: 0, tor_progress_summary: null,
  tor_progress_tag: null, tor_version: 0.2.4.20, transport_name: obfs3}
...
---
{bridge_address: '209.141.36.236:45496', error: null, input: 'obfs3 209.141.36.236:45496
    58D91C3A631F910F32E18A55441D5A0463BA66E2', success: false, timeout: 120, tor_log: '',
  tor_progress: 0, tor_progress_summary: null, tor_progress_tag: null, tor_version: 0.2.4.20,
  transport_name: obfs3}
...
```

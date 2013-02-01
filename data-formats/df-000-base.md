# OONI Data formats

The output of test is the composition of:

+---------------------------+
|   Base data format        |
+---------------------------+
| Test template data format |
+---------------------------+
| Test specific data format |
+---------------------------+

In this directory shall go only the data format specifications of Test
templates. The Test specific data formats should go in the specification of the
test.

All data produced from ooniprobe tests is in YAML formatted.

Every test that is interested in reporting with ooniprobe MUST use such data
format.

# Base test data format

This specification is of the basic data format common to all ooniprobe test
outputs.

Data Format Version: df-000-base-000

## Specification

    ###########################################
    # OONI Probe Report for HTTP Requests test
    # Wed Jan 30 21:03:56 2013
    ###########################################
    ---
    options:
      A dict containing the keys and values of options passed to the test.

    probe_asn:
      The AS Number of the probe (prefixed by AS, ex. AS1234) or null if includeasn is set to false.

    probe_cc:
      The two letter country code of the probe or null if inlcudecc is set to false.

    probe_ip:
      The IPv4 address of the probe or null if includeip is set to false.

    software_name:
      The name of the software that has generated such report (ex. ooniprobe).

    software_version:
      The version of the software that has generated such report (ex. 0.0.10).

    start_time:
      The time at which the test was started in seconds since epoch.

    test_name:
      The name of the test that such report is for (ex. HTTP Requests).

    test_version:
      The version of the test that such report is for (ex. 0.0.10).

    data_format_version:
      The version string of the data format being used by the test (ex. httpt-000)
    ...

# Example output

    ###########################################
    # OONI Probe Report for HTTP Invalid Request Line test
    # Mon Jan 28 21:33:59 2013
    ###########################################
    ---
    options:
      collector: null
      help: 0
      logfile: null
      parallelism: '10'
      pcapfile: null
      reportfile: null
      resume: 0
      subargs: [-b, 'http://93.95.227.200']
      test: nettests/manipulation/http_invalid_request_line.py
    probe_asn: null
    probe_cc: null
    probe_ip: null
    software_name: ooniprobe
    software_version: 0.0.10
    start_time: 1359401639.0
    test_name: HTTP Invalid Request Line
    test_version: 0.1.3
    ...


# Report Entry data format

Every iteration over an input given to a test will produce a Report Entry.

A Report Entry is a YAML Stream as specified here:
http://www.yaml.org/spec/1.2/spec.html#id2801681

Here are specified the keys that will always be present inside of every report
entry.

## Specification

input:
  The item we this specific test instance is referring to. null in case no
  input is being iterated over.

test_name:
  `string` the name of the test method this test is referring to (that is the
  class method of a NetTestCase)

test_runtime:
  `float` the runtime of the test

test_started:
  `float` seconds since epoch from the starting of the test.


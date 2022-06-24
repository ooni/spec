# Specification version number

2022-06-01-000

* _status_: experimental

# Specification name

browser_web

# Test preconditions

* An internet connection

# Expected impact

Determine if a web browser is able to access a particular web resource.

# Expected inputs

This experiment takes in input a list of URLs.

There are some limitations in what kinds of URLs can be measured due to specific
server-side CORS configuration.

In particular, if the URL we are trying to measure is setting [CORP headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cross-Origin_Resource_Policy_(CORP)),
it will always show up as a failure, making the measurement unreliable.

# Test description

Browser web is a test designed to run inside of a users web browser. To initiate
the test a web page is visited and after an informed consent procedure, it is
possible to run the experiment.

The test uses the [fetch
API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API) in an attempt
to measure if certain target URLs are being blocked.

This test will produce as a final result the time it took to load the resource
(using the [performance
API](https://developer.mozilla.org/en-US/docs/Web/API/Performance)) and whether the
result was successful.

## Caveats

Because the information collected by this test is not very detailed some extra
precautions need to be taken when interpreting the results.

If the server hosting the site we intend to measure is setting the
`Cross-Origin-Resource-Policy` header, since our request will be issued from a
different `Origin`, it will always result in a failure. For this reason, it's
advisable to pre-screen the targets for testing, to exclude sites that have this
header set.

Another issue, is that if the measurement tool is deployed on HTTPS any request
to HTTP sites will fail due to it being a [mixed content request](https://developer.mozilla.org/en-US/docs/Web/Security/Mixed_content).
Even if we were to be able to bypass this limitation, since aren't able to read
the payload of the response, we are not able to determine if the retrieve
content is consistent with what we would expect to see. It's therefore advisable
to only use as testing targets HTTPS websites as an inconsistent DNS response or
a TLS MITM would be visible as a failure.

Moreover, if the user has enabled [strict enhanced tracking
protection](https://support.mozilla.org/en-US/kb/enhanced-tracking-protection-firefox-desktop#w_strict-enhanced-tracking-protection)
on Firefox, requests to certain sites (ex. twitter.com or facebook.com) will
fail and appear to be a result of blocking.
The workaround is to detect if the user has enabled this setting and if so
request that they add a whitelist of the site hosting the `browser_web`
experiment.

# Expected output

## Parent data format

## Semantics

The contents of the `test_keys` field is as follows:

```JSON
{
  "result": "ok",
  "load_time_ms": 404.40000000596046
}
```

where:

* `result` (`string`) will be `ok` in the case of a successful measurement,
  while it will be `error` in the case of a failure;
* `load_time_ms` (`float`) indicates the number of milliseconds it took to load
  the requested resource.

## Possible conclusions

If a certain web resource is accessible or not from the vantage point of the
user.

## Example output sample

```JSON
{
  "software_name": "ooniprobe-web",
  "software_version": "0.0.1",
  "test_start_time": "2022-06-02 13:08:21",
  "test_name": "browser_web",
  "test_version": "0.1.0",
  "data_format_version": "0.2.0",
  "report_id": "20220602T130821Z_browserweb_IT_30722_n1_MJoDg0lHFMo9QncM",
  "measurement_start_time": "2022-06-02 13:10:01",
  "probe_asn": "AS30722",
  "probe_cc": "IT",
  "probe_network_name": "Vodafone Italia S.p.A.",
  "input": "https://go-text.me/",
  "test_runtime": 0.4044000000059605,
  "test_keys": {
      "result": "ok",
      "load_time_ms": 404.40000000596046
  }
}
```

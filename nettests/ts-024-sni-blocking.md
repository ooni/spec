# Specification version number

0.1.0

# Specification name

SNI blocking (`sni_blocking`)

# Test preconditions

  * An internet connection

# Expected impact

Understanding whether there is SNI based blocking. This experiment is useful
when you know a website that may be blocked with this blocking technique, and
you would like to verify this hypothesis.

# Expected inputs

## Import document or import data format

A list of domain, port endpoints to which to connect.

## Data specification version number

## Semantics

The input document will contain a list of zero or more endpoints to
which to connect using TLS. The following

```
www.google.com:443
www.facebook.com:443
```

are all valid entries.

# Test description

For every input endpoint we:

1. connect and perform a TLS handshake

2. repeat forcing a random SNI

# Expected output

The key `test_keys` key object will be added to the report.

The `test_keys.failure_with_proper_sni` contains the error of connecting and
performing a TLS handshake to the input endpoint using proper SNI. This key
will be null in case there is no error.

The `test_keys.failure_with_random_sni` contains the error of connecting and
performing a TLS handshake to the input endpoint using a random SNI. This
key will be null in case there is no error.

## Understanding the results

Under normal conditions, we expect the attempt with the proper SNI to succeed
and the attempt with the random SNI to fail with an error indicating that
the provided certificate does not cover the configured SNI.

When there is SNI based blocking, we instead expect the attempt with the proper
SNI to fail with a connection reset, and we expect to see in the second
attempt the same failure we see under normal conditions.

## Example output sample

```
{
  "data_format_version": "0.2.1",
  "input": "www.kernel.org:443",
  "measurement_start_time": "2019-10-08 16:54:38",
  "test_runtime": 0,
  "probe_asn": "AS30722",
  "probe_cc": "IT",
  "probe_ip": "127.0.0.1",
  "report_id": "20191008T165438Z_AS30722_MeeceRVVuRnOxy9DOGxJZd9gyuQsmCrqJowvESbuTNOn24YPJT",
  "resolver_ip": "172.253.197.4",
  "software_name": "miniooni",
  "software_version": "0.1.0-dev",
  "test_keys": {
    "failure_with_proper_sni": null,
    "failure_with_random_sni": "x509: certificate is valid for kernel.org, archive.kernel.org, git.kernel.org, mirrors.kernel.org, www.kernel.org, not spyvkhuzbl.bel"
  },
  "test_name": "sni_blocking",
  "test_start_time": "2019-10-08 16:54:37",
  "test_version": "0.1.0"
}
{
  "data_format_version": "0.2.1",
  "input": "expired.badssl.com:443",
  "measurement_start_time": "2019-10-08 16:54:38",
  "test_runtime": 0,
  "probe_asn": "AS30722",
  "probe_cc": "IT",
  "probe_ip": "127.0.0.1",
  "report_id": "20191008T165438Z_AS30722_MeeceRVVuRnOxy9DOGxJZd9gyuQsmCrqJowvESbuTNOn24YPJT",
  "resolver_ip": "172.253.197.4",
  "software_name": "miniooni",
  "software_version": "0.1.0-dev",
  "test_keys": {
    "failure_with_proper_sni": "x509: certificate has expired or is not yet valid",
    "failure_with_random_sni": "x509: certificate has expired or is not yet valid"
  },
  "test_name": "sni_blocking",
  "test_start_time": "2019-10-08 16:54:37",
  "test_version": "0.1.0"
}
```

## Limitations

This first iteration of the experiment [does not allow to repeat the
experiment with variations of the random SNI, to understand how blocking
is happening](https://github.com/ooni/spec/pull/159#discussion_r332989964).
A future version of this specification will address these limitations.

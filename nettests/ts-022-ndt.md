# Specification version number

2020-04-08-001

* _status_: current

# Specification name

NDT (Network Diagnostic Tool)

# Test preconditions

* An internet connection

# Expected impact

Measurement of performance parameters of the end-to-end path between the
user's device and a Measurement Lab server.

# Expected inputs

None

# Test description

This is an external experiment. Not only OONI users but many users
worldwide are using NDT every day to measure network performance. We
wrote our own, spec compliant implementation of NDT, but we are using
third party server infrastructure and implementation provided by the
[Measurement Lab](https://www.measurementlab.net/) consortium. As such,
the [privacy policy](https://www.measurementlab.net/privacy/) of
Measurement Lab applies in additon to [OONI's privacy policy](
https://ooni.org/about/data-policy/).

There are two flavours of the NDT protocol: ndt5 and ndt7. The ndt5
version of the protocol is now obsolete. This documentation describes
OONI's usage of ndt7. The specification of the ndt7 protocol is
[available at github.com/m-lab/ndt-server](
https://github.com/m-lab/ndt-server/blob/master/spec/ndt7-protocol.md).

Data consumers could differentiate ndt7 and ndt5 tests by looking at
the following features. Ndt5 tests have a `"test_s2c"` key that is not
present inside of ndt7 tests. Ndt7 clients also include a key that is
called `"protocol"` and is set to `7`.

# Expected output

## Parent data format

* df-000-base

* df-009-tunnel

## Semantics

The ndt7 toplevel keys are the following:

```JSON
{
  "download": [],
  "failure": null,
  "protocol": 7,
  "server": {},
  "summary": {},
  "upload": [],
}
```

where:

- `"download"` (`[]Measurement`): contains measurements collected
during the download phase of the experiment;

- `"failure"` (`string`; nullable): `null` on success, `string` on
error as documented in `df-007-errors.md`;

- `"protocol"` (`int`): is the protocol being used, `7` for ndt7;

- `"server"` (`Server`): contains info on the server you're using;

- `"summary"` (`Summary`): contains the experiment summary;

- `"upload"` (`[]Measurement`): contains measurements collected
during the upload phase of the experiment.

The `Measurement` object is a "Measurement message" described by the
aformentioned ndt7 specification. Its `"Origin"` field allows to take
apart measurements from the client and measurements from the server. As
of v0.9.0 of such spec, a `Measurement` is like:

```JSON
{
  "AppInfo": {
    "ElapsedTime": 1234,
    "NumBytes": 1234,
  },
  "Origin": "server",
  "Test": "download",
  "TCPInfo": {
    "BusyTime": 1234,
    "BytesAcked": 1234,
    "BytesReceived": 1234,
    "BytesSent": 1234,
    "BytesRetrans": 1234,
    "ElapsedTime": 1234,
    "MinRTT": 1234,
    "RTT": 1234,
    "RTTVar": 1234,
    "RWndLimited": 1234,
    "SndBufLimited": 1234
  }
}
```

where:

- `AppInfo` is an _optional_ `object` only included in the measurement
  when an application-level measurement is available:

    - `ElapsedTime` (a `int64`) is the time elapsed since the beginning of
      this test, measured in microseconds.

    - `NumBytes` (a `int64`) is the number of bytes sent (or received) since
      the beginning of the specific test. Note that this counter tracks the
      amount of data sent at application level. It does not account for the
      overheaded of the WebSockets, TLS, TCP/IP, and link layers.

- `Origin` is an _optional_ `string` that indicates whether the measurement
  has been performed by the client or by the server. This field SHOULD
  only be used when the entity that performed the measurement would otherwise
  be ambiguous.

- `Test` is an _optional_ `string` that indicates the name of the
  current test. This field SHOULD only be used when the current test
  should otherwise not be obvious.

- `TCPInfo` is an _optional_ `object` only included in the measurement
  when it is possible to access `TCP_INFO` stats. It contains:

    - `BusyTime` aka `tcpi_busy_time` (an _optional_ `int64`), i.e. the number of
       microseconds spent actively sending data because the write queue
       of the TCP socket is non-empty.

    - `BytesAcked` aka `tcpi_bytes_acked` (an _optional_ `int64`), i.e. the number
      of bytes for which we received acknowledgment. Note that this field,
      and all other `TCPInfo` fields, contain the number of bytes measured
      at TCP/IP level (i.e. including the WebSocket and TLS overhead).

    - `BytesReceived` aka `tcpi_bytes_received` (an _optional_ `int64`), i.e. the number
      of bytes for which we sent acknowledgment.

    - `BytesSent` aka `tcpi_bytes_sent` (an _optional_ `int64`), i.e. the number of bytes
      which have been transmitted _or_ retransmitted.

    - `BytesRetrans` aka `tcpi_bytes_retrans` (an _optional_ `int64`), i.e. the number
      of bytes which have been retransmitted.

    - `ElapsedTime` (an _optional_ `int64`), i.e. the time elapsed since the beginning of
      this test, measured in microseconds.

    - `MinRTT` aka `tcpi_min_rtt` (an _optional_ `int64`), i.e. the minimum RTT seen
       by the kernel, measured in microseconds.

    - `RTT` aka `tcpi_rtt` (an _optional_ `int64`), i.e. the current smoothed RTT
      value, measured in microseconds.

    - `RTTVar` aka `tcpi_rtt_var` (an _optional_ `int64`), i.e. the variance or `RTT`.

    - `RWndLimited` aka `tcpi_rwnd_limited` (an _optional_ `int64`), i.e. the amount
      of microseconds spent stalled because there is not enough
      buffer at the receiver.

    - `SndBufLimited` aka `tcpi_sndbuf_limited` (an _optional_ `int64`), i.e. the amount
      of microseconds spent stalled because there is not enough buffer at
      the sender.

The real measurement MAY include more TCPInfo fields, but the ones mentioned above
are the ones that are guaranteed to be there.

The `Server` object is like:

```JSON
{
  "hostname": ""
}
```

where `"hostname"` maps to the server hostname.

The `Summary` object is like:

```JSON
{
  "avg_rtt": 44.207,
  "download": 86462.99292978938,
  "mss": 1460,
  "max_rtt": 72.787,
  "min_rtt": 20.764,
  "ping": 20.764,
  "retransmit_rate": 0,
  "upload": 19788.673292743886
}
```

where:

- `"avg_rtt"` (`float`): average RTT computed from server
provided data during the download phase, in millisecond;

- `"download"` (`float`): average download speed computed from
client side data during the download phase, in kbit/s;

- `"mss"` (`int`): maximum segment size computed from server
provided data during the download phase, in bytes;

- `"max_rtt"` (`float`): maximum observed value of the RTT
computed from server data during the download phase, in millisecond (keep
in mind that we may be missing samples, so the real maximum RTT may be
larger than that, but we may fail to observe it);

- `"min_rtt"` (`float`): minimum RTT computed from server
provided data during the download phase, in millisecond;

- `"ping"` is currently the same as `"min_rtt"`;

- `"retransmit_rate"` (`float`): number between `0` and `1` computed
by dividing the bytes retransmitted over the bytes sent, using
server provided data during the download phase;

- `"upload"` (`float`): average upload speed computed from
client side data during the upload phase, in kbit/s.

Data computed from server side data assumes that the server is sending
us TCPInfo snapshots, which Measurement Lab servers do. In specific
conditions (e.g. when there is no end to end connectivity due to application
level proxing by a mobile provider) TCPInfo data is very inaccurate. We are
researching how to detect this specific case. A common symptom appears to
be unreasonably low RTTs and unreasonably low download speeds.

## Possible conclusions

This experiment is a "here and now" snapshot of the performance between
the user and a well provisioned reasonably-nearby server. This experiment
does not provide information regarding the throttling of specific sites
and/or network paths (e.g. Netflix). It may be useful, instead, to understand
congestion.

This experiment attempts to use the full available bandwidth. If the
server is a Measurement Lab server (as it should be), it is using TCP
BBR, which generates an accurate model of the channel and should not
create excessive queue at the bottleneck. Therefore, the min RTT and the
average bandwidth included in the summary provide a good indication of
what the end to end channel can deliver.

It is important to understand that this experiment does not run for a long
time, compared to long lived flows such as streaming and video calls. So,
it likely won't detect throttling experienced by long lived flows. Nonetheless
analysing the performance over the lifetime of the experiment, as opposed to
just looking into the summary, provide insights into the performance dynamics.

This experiment does not use multiple flows. As such it provides an indication
of what a single flow can achieve on the given end to end path. This means
that it will perform less than other speed tests, e.g. speedtest.net, in cases
in which the connectivity is less than ideal. This is most likely what you
want from a diagnostic test, i.e. information rather than confirmation.

The selected server may vary across multiple runs of this experiment. Pay
attention to the server that you are using. It may be that you have good
connectivity with some servers and bad connectivity with others. NDT has been
indeed used in the past precisely to diagnose this kind of problems.

## Privacy considerations

Notwithstanding your privacy settings, this experiment will collect your
public IP address. It will not be included in OONI data but it will be
collected and saved by the Measurement Lab server you are using, and it
will be subsequently published by Measurement Lab. We are
working with Measurement Lab to understand whether it will be possible
to avoid collecting the IP address in a future version of NDT.

The two main reasons why removing IP addresses from NDT server data is
complex are managing abuses and beacons detection. With respect to managing
abuses, the Measurement Lab platform would need an alternative way to
protect itself from high-speed clients hammering it continuously. From
the research standpoint, instead, there is lots of value in keeping track
of how the performance of long-lived hosts (aka "beacons") across time. Until
we solve these two problems in a privacy preserving way, NDT will continue
to collect the full user IP address.

In addition, there is the additional, mainly technical obstacle that traceroute
data collected by services ancillary to the NDT server needs to be made
anonymous as well. If we don't make traceroute anonymous, then one can
join the NDT result with the traceroute result, thus obtaining the user's IP
address. This is possible because both the NDT server measurement and the
traceroute measurement include a UUID that uniquely identifies the
measurements session. Because a reverse traceroute is very valuable to
understand performance, we are facing another tradeoff here,
and removing the reverse traceroute for all NDT users does not seem to
be the right balance between measurements quality and privacy.

See [github.com/ooni/probe-engine#535](https://github.com/ooni/probe-engine/issues/535)
for progress updates on this effort.

## Example output sample

The following output sample has been trimmed for readability, by
removing multiple instances of `Measurement`.

```JSON
{
  "annotations": {
    "engine_name": "miniooni",
    "engine_version": "0.9.0",
    "platform": "linux"
  },
  "data_format_version": "0.2.0",
  "input": null,
  "measurement_start_time": "2020-04-08 10:18:00",
  "probe_asn": "AS30722",
  "probe_cc": "IT",
  "probe_ip": "127.0.0.1",
  "report_id": "20200408T101800Z_AS30722_Q2HYsPMDdmmdT6ZppPNkF8PNyHxe91HwFGtIJwWIlopRFJr358",
  "resolver_asn": "AS30722",
  "resolver_ip": "91.80.36.88",
  "resolver_network_name": "Vodafone Italia S.p.A.",
  "software_name": "miniooni",
  "software_version": "0.1.0-dev",
  "test_keys": {
    "download": [
      {
        "AppInfo": {
          "NumBytes": 1703936,
          "ElapsedTime": 250466
        },
        "Origin": "client",
        "Test": "download"
      },
      {
        "AppInfo": {
          "NumBytes": 4456448,
          "ElapsedTime": 500177
        },
        "Origin": "client",
        "Test": "download"
      },
      {
        "Origin": "server",
        "Test": "download",
        "TCPInfo": {
          "BusyTime": 230000,
          "BytesAcked": 876930,
          "BytesReceived": 661,
          "BytesRetrans": 0,
          "BytesSent": 1726350,
          "MinRTT": 23172,
          "RTT": 37812,
          "RTTVar": 2044,
          "RWndLimited": 38000,
          "RcvMSS": 536,
          "SndBufLimited": 0,
          "ElapsedTime": 202574
        }
      }
    ],
    "failure": null,
    "protocol": 7,
    "server": {
      "hostname": "ndt-iupui-mlab1-mil02.measurement-lab.org"
    },
    "summary": {
      "avg_rtt": 44.282,
      "download": 86735.17865757788,
      "mss": 1460,
      "max_rtt": 80.154,
      "min_rtt": 23.172,
      "ping": 23.172,
      "retransmit_rate": 0.0002913916808191168,
      "upload": 19788.436651446274
    },
    "upload": [
      {
        "AppInfo": {
          "NumBytes": 656384,
          "ElapsedTime": 250563
        },
        "Origin": "client",
        "Test": "upload"
      }
    ]
  },
  "test_name": "ndt",
  "test_runtime": 21.3737419,
  "test_start_time": "2020-04-08 10:18:00",
  "test_version": "0.4.0"
}
```

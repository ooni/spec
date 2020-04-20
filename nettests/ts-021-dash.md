# Specification version number

2020-04-19-001

# Specification name

DASH

# Test preconditions

* An internet connection

# Expected impact

Measurement of the quality at which it would be possible to stream
from the current vantage point using the DASH ([Dynamic Adaptive Streaming
over HTTP](https://en.wikipedia.org/wiki/Dynamic_Adaptive_Streaming_over_HTTP
)) streaming technique, a very simple player, and a reasonable well
provisioned nearby streaming server.

# Expected inputs

None

# Test description

This is an external experiment originally implemented for [Neubot](
https://github.com/neubot/neubot). This document describes the
implementation of such test used by OONI Probe.

We are using third party server infrastructure provided by the [Measurement Lab](
https://www.measurementlab.net/) consortium (M-Lab). We are also using the
server implementation provided by the Neubot project. As such,
[the privacy policy of M-Lab](https://www.measurementlab.net/privacy/)
and [the privacy policy of the DASH server](
https://github.com/neubot/dash/blob/master/PRIVACY.md) apply in
addition to [OONI's privacy policy](https://ooni.org/about/data-policy/).

## Test rationale

In DASH a video is divided into fixed time segments. Each segment is
encoded at different bitrates. The client downloads the segments,
may buffer some of them, and plays them. The client can increase or reduce the
bitrate of the video stream from the server, when the network is
respectively more or less performant.

This test emulates a very simple player. It basically starts
downloading a given segment after the previous segment has been
downloaded. It uses the speed at which the segment was downloaded
to select the quality (i.e. the bitrate) of the next segment
to be downloaded. No previous video segment will be buffered to ensure
the streaming does not stall in the event of changing network
conditions. As such, if this player was real, a user using it would see:

- video quality changing for every video segment (higher quality when the
  network is working better and lower quality when it slows down);

- occasional stalls when the next video segment is received after the
  current video segment has finished playing (because the network speed
  estimate from the previous segment was not accurate enough and/or
  the network conditions changed).

Real-world video players (e.g. YouTube and Netflix) do no behave
like this, of course. Rather, they seek to maintain quality steady
and to keep enough segments in the buffer so that streaming continues
even if there is a transient network issue.

However, precisely because of its simplicity, this test provides
more hints about the network quality. It basically shows at which video
bitrate you can typically stream from your vantage point, relying
only on the quality of the network to ensure smooth streaming.

## End-to-end performance remarks

Note that the quality that you see is of course correlated to the one
of your ISP, but it is also correlated to:

1. whether your computer or device is overloaded;

2. whether your connection with the first router is good (is the cable
   good? Is the Wi-Fi signal good? Are you close enough to the mobile cell?);

3. whether the server is close enough;

4. whether the server is overloaded;

5. whether the network hosting the server is overloaded;

6. whether the interconnection points are overloaded;

7. if there are other ISPs in the middle, whether their internal
   networks and interconnection points are overloaded.

In many cases, the [M-Lab](https://www.measurementlab.net/
) servers used by default by this test should be
close enough to the users. The minimum RTT can, in any case, be a useful
metric to confirm that this is actually the case.
Also, the server and the network where it is hosted should not be
overloaded without M-Lab noticing and reporting this incident.

## Comparability with other clients

As explained in the previous section, the client emulated by this
test is much simpler than real world clients (e.g. YouTube
or Netflix). As such, it may be
the case that a real world client could stream videos at a higher
quality than the one reported by this test, and without stalls.

## Network neutrality considerations

We have seen in the past [cases where the quality of video providers
was significantly reduced because of congestion at interconnection
points between video providers and ISPs](
https://arstechnica.com/tech-policy/2010/12/comcastlevel3/
). This may, in principle, be
detected by this test by comparison with historical data. Yet, in
practice, this cannot be detected because, in general, the path from
the client to the selected M-Lab server is different from the path
from the client to a specific video provider's servers. Thus, packets
may pass through different interconnection points missing the
congested ones.

## Algorithm

In its most general implementation, this test will:

1. discover the closest M-Lab server using [mlab-ns](
      https://github.com/m-lab/mlab-ns
   ), unless a server name has been explicitly specified by the user;

2. establish a persistent HTTP connection with said server;

3. set the initial estimated rate at which to attempt streaming;

4. for each segment in the emulated video, then, it will:

    2.1. request to the remote server the next segment encoded at the
         previously estimated rate;

    2.2. measure the speed at which the segment was downloaded;

    2.3. possibly scale down the speed significantly when the download
         took more than the duration of a video segment;

    2.4. update the rate estimate using some configurable mechanism
         to obtain a new estimate of the bitrate from the measured
         speed (see below).

The following defaults apply to the version of the test implemented by
used by OONI Probe:

- the initial rate estimate is 3,000 kbit/s;

- the duration of a video segment is two seconds;

- the video consists of 15 segments;

- the speed is not scaled down when the download takes more
  than the duration of a video segment;

- the rate estimate is set equal to the measured speed (this cannot happen
  in reality because a server cannot encode a video into all the possible
  bitrates, but is useful to measure network performance, as explained below).

## Rationale of selected parameters

The initial bitrate estimate is set to 3,000 kbit/s because that
is [the minimum download speed that Netflix reccommends for
SD quality](https://help.netflix.com/en/node/306). The Neubot implementation used
instead 100 kbit/s.

Segments contain two seconds of video.
[Two seconds is the value used by Microsoft's streaming solution and
is the lower end value recommended by Bitmovin](
https://bitmovin.com/mpeg-dash-hls-segment-length/). We chose two seconds
because that allows us to adapt more quickly to the fluctuating
network conditions.

We use fifteen segments so that the overall test duration is around
thirty seconds in the common case (fifteen segments each containing two
seconds of video).

The Neubot implementation scales down the speed after the download
of a segment takes more than the duration of a segment. This was
done because Neubot was a background tool and we did not want to
overload the network. We decided to disable this behavior by default
in OONI Probe, so to better measure the network quality.

The Neubot implementation used a fixed vectors of available bitrates,
selecting the highest available bitrate that was lower than the
speed with which the last segment was downloaded. In OONI Probe,
we decided to disable this behavior by default, so to better measure
the network quality.

# Expected output

## Parent data format

* none

## Semantics

```JSON
{
    "failure": null,
    "receiver_data": [],
    "sender_data": [],
    "simple": {}
}
```

Where `simple` contains the summary, `failure` is a nullable string containing
the error as defined in `df-007-errors.md`, `receiver_data` contains the client
side measurements, and `sender_data` contains the server measurements.

The `sender_data` array is optional. All the other fields MUST be present. More in
detail, the `receiver_data` array is like:

```JSON
[{
    "connect_time": 0.019882652,
    "elapsed": 0.17025906,
    "elapsed_target": 2,
    "iteration": 0,
    "platform": "darwin",
    "rate": 3000,
    "received": 750000,
    "request_ticks": 2.6875e-05,
    "server_url": "https://neubot-mlab-mlab3-mil02.measurement-lab.org/dash/download/750000",
    "timestamp": 1587376362,
    "version": "0.008000000"
}]
```

where:

- `connect_time`: time required by `connect()` to complete, which can be
an approximation of the minimum RTT, measured in seconds.

- `elapsed`: time elapsed since before sending the HTTP request for the
segment until the HTTP response body is fully received, measured
in seconds.

- `elapsed_target`: target for elapsed, measured in seconds. The objective
of this experiment is to select the maximum rate such that the `elapsed`
time is not greater than `elapsed_target`.

- `iteration`: number of the segment (should be an integer between
one and the maximum number of segments).

- `platform`: platform where we're running.

- `rate`: bitrate of the segment (in kbit/s), i.e. video quality.

- `received`: number of bytes received.

- `request_ticks`: moment when the request was issued, relative to some
base time, and suitable only for computing time differences.

- `timestamp`: number of seconds elapsed since the EPOCH.

- `version`: fixed at "0.008000000" to indicate OONI Probe's Go engine
and "0.007000000" to indicate Measurement Kit. Lower values indicate
a specific version of Neubot.

Note that real clients possibly include more fields. We are increasingly
deprecating legacy fields that do not matter to OONI Probe. As such,
this version of this specification is only listing fields that matter
with modern implementations of DASH.

The optional `sender_data` array is like:

```JSON
[{
    "iteration": 1,
    "ticks": 1245.3,
    "timestamp": 12345678,
    "web100_snap": {}
}]
```

where:

- `iteration` is like `iteration` in the `receiver_data`.

- `ticks` is like `request_ticks` in the `receiver_data`.

- `timestamp` is like `timestamp` in the `receiver_data`.

- `web100_snap` contains Web100 variables (which, as of this writing
are not collected anymore because M-Lab upgraded its platform and
is now using TCPInfo for the same purpose).

The `simple` object is like:


```JSON
{
    "connect_latency": 0.019882652,
    "median_bitrate": 83985,
    "min_playout_delay": 0
}
```

Where:

- `connect_latency`: same as `connect_time` in `receiver_data`;

- `median_bitrate`: median of the `rate`s in `receiver_data`;

- `min_playout_delay`: minimum amount of delay after which the player
should have started playing the first segment to ensure smooth
streaming. Computed as the sum of the differences between the moment
where a segment was received and the moment where it should have
been played. If negative, it means it would have been possible
to perform smooth streaming without adding further delay.

## Possible conclusions

- When running in the default configuration, median bitrate at which streaming
  would have been possible, coupled with the required playout delay.
  The default test implementation seeks to maximize the bitrate and keep the
  required playout delay to zero. When the playout delay is significantly larger
  than zero, the network quality changed during the test.

- Video quality (e.g. `420p`, `720p`) roughly corresponding to the median
  bitrate downloaded during the test. This can be inferred from information
  published by popular video streaming sites, e.g. [YouTube](
  https://support.google.com/youtube/answer/1722171?hl=en-GB).

## Privacy considerations

Notwithstanding your privacy settings, this experiment will collect your
public IP address. It will not be included in OONI data but it will be
collected and saved by the Measurement Lab server you are using, and it
will be subsequently published by Measurement Lab. We are
working with Measurement Lab to understand whether it will be possible
to avoid collecting the IP address in a future version of DASH. The
tracking issue for this effort is [github.com/ooni/probe-engine#502](
https://github.com/ooni/probe-engine/issues/502).

## Example output sample

The following example has been trimmed for readability:

```json
{
  "annotations": {
    "_probe_engine_sanitize_test_keys": "true",
    "engine_name": "miniooni",
    "engine_version": "0.9.0",
    "platform": "macos"
  },
  "data_format_version": "0.2.0",
  "input": null,
  "measurement_start_time": "2020-04-20 09:52:40",
  "probe_asn": "AS30722",
  "probe_cc": "IT",
  "probe_ip": "127.0.0.1",
  "report_id": "20200420T095240Z_AS30722_spiLF4fBpbo36q1FFGwaSIyLguwxpbQN5pSI1ZiC8ZJ9KeeNW9",
  "resolver_asn": "AS30722",
  "resolver_ip": "91.80.36.88",
  "resolver_network_name": "Vodafone Italia S.p.A.",
  "software_name": "miniooni",
  "software_version": "0.1.0-dev",
  "test_keys": {
    "simple": {
      "connect_latency": 0.019882652,
      "median_bitrate": 83985,
      "min_playout_delay": 0
    },
    "failure": null,
    "receiver_data": [
      {
        "connect_time": 0.019882652,
        "elapsed": 0.17025906,
        "elapsed_target": 2,
        "iteration": 0,
        "platform": "darwin",
        "rate": 3000,
        "received": 750000,
        "request_ticks": 2.6875e-05,
        "server_url": "https://neubot-mlab-mlab3-mil02.measurement-lab.org/dash/download/750000",
        "timestamp": 1587376362,
        "version": "0.008000000"
      }
    ]
  },
  "test_name": "dash",
  "test_runtime": 11.817663836,
  "test_start_time": "2020-04-20 09:52:39",
  "test_version": "0.10.0"
}
```

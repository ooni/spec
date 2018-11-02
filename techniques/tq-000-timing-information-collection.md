# tq-000 Timing information collection

All the experiments should collect all possible timing information, every sent
and incoming byte, every network error of every exchange should be time-stamped
with monotonic timer started at the measurement_start_time<sup>[1](#fn1)</sup>. Incoming TCP ACKs
may be time-stamped with some precision polling TCP_INFO. L5 and L7 events like
“ServerCertificate arrived over TLS1.3” and “HTTP header arrived” should also
be time-stamped when possible.

Bytes come in packets, so packet may be time-stamped for UDP and byte range may
be time-stamped for TCP.

TBD: It’s unclear if SO_TIMESTAMP and other alike options are useful.

TBD: is `connect()` time the best estimate for SYN-ACK? Is RTT estimate from
`TCP_INFO` after `connect()` also good or, maybe, better? Maybe `BBR_INFO` and
`TCP_CC_INFO`?

Having all monotonic timestamps within the measurement rooted at single wall
clock sample is needed as intra-measurement ordering may be important: imagine
“stateful” DPI that can “learn” a protocol of service at IP:Port and two
traceroute tests to the endpoint done before and after “teaching” DPI the
protocol.

<a name="fn1">1</a>: there is no need to _explicitly_ keep singleton object of
reference clock if all participating libraries use same monotonic clock time
source. Platforms may have several monotonic timescales!

## Examples
- when RST or TLS Alert packet arrives way faster than SYN-ACK it is likely injected
- when DNS reply for non-cached “censored” hostname arrives as fast as reply to “a.root-servers.net.” or “.” served from root hints it is likely injected
- Mozilla has [tips on cross-platform monotonic clock](https://firefox-source-docs.mozilla.org/toolkit/components/telemetry/telemetry/data/main-ping.html#sessionlength), Go/1.9+ and C++11 also have monotonic clock support

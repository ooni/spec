# tq-025 Saving bandwidth in repeated HTTP requests

HTTP tests have a very high-volume response compared to the request size. For example
response bodies for censored webpages may weight up to 4MB. If the request is repeated hundreds of times
due to traceroutes, TCP Segmentation, various HTTP camouflage and other tricks
it can significantantly increase the bill for traffic without a good reason. OONI Probe
should terminate the connection as soon as it is reasonably sure that the HTTP
body is not going to differ from the one that it has already recorded.

A limited TCP initcwnd (initial congestion window) at servers ensures that OONI
Probe has one RTT to decide if it wants to continue fetching the data.

OONI Probe may also set low `SO_RCVBUF` or `TCP_WINDOW_CLAMP` to do TCP backpressure.

TBD: is it possible to drain the kernel buffer without sending an ACK with some
non-zero window? The data that is already in the buffer should probably make its
way into the measurement data.

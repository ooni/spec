# tq-025 Saving bandwidth in repeated HTTP requests

HTTP tests have very high-volume response compared to request size, request to
censored webpage may have 4 MiB body. If the request is repeated hundred times
due to traceroutes, TCP Segmentation, various HTTP camouflage and other tricks
it can bring significant bill for traffic without good reason. OONI Probe
should terminate the connection as soon as it is reasonably sure that the HTTP
body is not going to differ from one that is already recorded.

Limited TCP initcwnd (initial congestion window) at servers ensures that OONI
Probe has one RTT to decide if it wants to continue fetching the data.

OONI Probe may also set low `SO_RCVBUF` or `TCP_WINDOW_CLAMP` to do TCP backpressure.

TBD: is it possible to drain the kernel buffer without sending ACK with some
non-zero window? The data that is already in the buffer should probably do its
way to the measurement data.

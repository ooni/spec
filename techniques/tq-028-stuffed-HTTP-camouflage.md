# tq-028 Stuffed HTTP camouflage

If a HTTP request triggers an unexpected response it is interesting to try
several “camouflage stuffing” tricks to check if they trigger different
behavior:

- append TAB (“\t”) character to Host header before “\r\n”
- prepend LF (“\n”) to GET
- append DOT (“.”) to domain in Host header
- extra SP (“ “) after GET
- newline-space (“\r\n ”) before domain in Host header
- “host” or “hoSt” header instead of “Host” header
- dropping usual space after colon in “Host:example.com”
- adding long “X-Stuff: AAA...AAA” header to push “Host” header to another packet
- “\n” instead of “\r\n”
- …

These tricks may reveal existence of several different DPI boxes inspecting the
traffic one after another having different HTTP parser flaws.

The list of tricks is incomplete and, moreover, may break some HTTP servers.
E.g. “Host:\r\n<SP><SP>example.com\r\n” is valid, but lighttpd-1.4 fails to
parse it and throws “400 Bad Request” while Django built-in HTTP server just
crashes.

## Examples
- [Turkmenistan](https://ooni.torproject.org/post/tab-tab-come-in/) did not handle appended \t and prepended \n properly
- Is there some interesting data from [http_filtering_bypassing.py](https://github.com/ooni/probe-legacy/blob/master/ooni/nettests/experimental/http_filtering_bypassing.py) ?
- Some of these tricks are claimed to be successful by [GoodbyeDPI](https://github.com/ValdikSS/GoodbyeDPI)

# HTTP Header Field Manipulation

This test tries to detect the presence of network components (“middle box”)
which could be responsible for censorship and/or traffic manipulation.

HTTP is a protocol which transfers or exchanges data across the internet. It
does so by handling a client's request to connect to a server, and a server's
response to a client's request. Every time you connect to a server, you (the
client) send a request through the HTTP protocol to that server. Such requests
include “HTTP headers”, which transmit various types of information, including
your device's operating system and the type of browser that it's using. If you
are using Firefox on Windows, for example, the “user agent header” in your HTTP
request will tell the server that you're trying to connect to that you're using
a Firefox browser on a Windows operating system.

This test emulates what would have been a valid HTTP request towards a server,
but instead sends HTTP headers that have variations in capitalization. In other
words, this test sends HTTP requests which include valid, but non-standard HTTP
headers. Such requests are sent to a backend control server which sends back any
data it receives. If we receive the HTTP headers exactly as we sent them, then
we assume that there is no “middle box” in the network which could be
responsible for censorship, surveillance and/or traffic manipulation. If,
however, such software is present in the network that we are testing, it will
likely normalize the invalid headers that we are sending or add extra headers.

Depending on whether the HTTP headers that we send and receive from a backend
control server are the same or not, we are able to evaluate whether software –
which could be responsible for traffic manipulation – is present in the network
that we are testing.

**Note:** A false negative could potentially occur in the hypothetical instance
that ISPs are using highly sophisticated software that is specifically designed
to not interfere with invalid HTTP headers when it receives them. Furthermore,
the presence of a middle box is not necessarily indicative of traffic
manipulation, as they are often used in networks for caching purposes.

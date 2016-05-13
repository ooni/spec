# HTTP Requests

This test tries to detect online censorship based on a comparison of HTTP
requests over Tor and over the network of the user.

HTTP is a protocol which allows communication between a client and a server. It
does so by handling a client's request to connect to a server, and a server's
response to a client's request. Every time you connect to a website, your
browser (the client) sends a request through the HTTP protocol to the server
which is hosting that website. A server normally responds with the content of
the website it is hosting. In some cases though, Internet Service Providers
(ISP) prevent users from accessing certain websites by blocking or interfering
with the connection between them and the server.

To detect such cases of censorship, we have developed a test which performs HTTP
requests to given websites over the network of its user, and then over the Tor
network. As Tor software is designed to circumvent censorship by making its
user's traffic appear to come from a different part of the world, we have chosen
to use the Tor network as a baseline for comparing HTTP requests to websites. If
the two results match, then there is no clear sign of network interference; but
if the results are different, then the website that the user is testing is
likely censored.

If one of the following is present in the results, then there is a sign of
network interference:

* The length of the body of the two websites (over Tor and over the user's
  network) differs by some percentage

* The HTTP request over the user's network fails

* The HTTP headers do not match

**Note:** False positives might occur when the Tor control connection is being
discriminated by the server. This happens, for example, when a CloudFlare
CAPTCHA page appears.


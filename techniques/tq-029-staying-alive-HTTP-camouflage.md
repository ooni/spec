# tq-029 Staying-alive HTTP camouflage

If a HTTP request triggers an unexpected response it is interesting to see if
it’ll trigger a response if it follows “good” request in the same Keep-Alive
connection. It’s non-trivial to define a “good” request:
http://censored.org/robots.txt may be still filtered because of domain and
webserver MAY drop connection after /robots.txt request to the domain that is
not served, but [Apache and Chrome are okay](https://stackoverflow.com/questions/42717719/http-keep-alive-to-a-different-host) with the trick.

That also reminds of [tq-018 Request to dummy proxy](./tq-018-request-to-dummy-proxy-test-helper.md).

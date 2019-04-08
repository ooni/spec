# tq-029 Staying-alive HTTP camouflage

If a HTTP request triggers an unexpected response it is interesting to see if
it’ll trigger a response if it follows a “good” request in the same Keep-Alive
connection. It’s non-trivial to define a “good” request:
http://censored.org/robots.txt may still be filtered because of the domain and
webserver MAY drop connection after the /robots.txt request to the domain that is
not served, but [Apache and Chrome are okay](https://stackoverflow.com/questions/42717719/http-keep-alive-to-a-different-host) with the trick.

This is related to [tq-018 Request to dummy proxy](./tq-018-request-to-dummy-proxy-test-helper.md).

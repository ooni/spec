# tq-022 Test-helper L7 checks for possibly-censored IPs

If probe gets a set of IPs for the origin servers that it can’t connect to, the
test-helper should do a L5/L7-check for these IPs if they serve content for the
domain. The HTTP protocol can do a GET request and fetch the page title / hashsum /
simhash, TLS can issue a ClientHello, fetch the Server Certificate and validate it.

# tq-022 Test-helper L7 checks for possibly-censored IPs

If probe gets set of IPs for the origin servers that it can’t connect to the
test-helper should do L5/L7-check for these IPs if they serve content for the
domain. HTTP protocol can do GET query and fetch page title / hashsum /
simhash, TLS can do ClientHello, fetch Server Certificate and validate it.

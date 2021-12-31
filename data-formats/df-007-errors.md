# Errors

This document describes the possible values of the `failure` key that
occurs in several data formats to indicate a failure. The type of
this key is `string; nullable`. See also this directory's
[README](README.md) for the basic concepts.

To indicate that an error is emitted by ooni/probe-legacy we will flag
the error using `(PL)`. To indicate that an error is emitted by Measurement
Kit, we will flag it using `(MK)`. To indicate that an error is emitted by
ooni/probe-engine, we will flag it using `(PE)`. When an error is emitted
by more than one product we will write `(product, product)`. When an error
is not flagged, it means that it's used by all the three products.

For clarity, we would look at the errors currently faced, separately
from the legacy errors. Following are the errors emitted by
ooni/probe-engine and/or Mesurement Kit.

|            Error               |Flag(s)|Details|
|:------------------------------:|:-----:|:-----:|
|`null`                          |   -   |no error has occurred|
|`"connection_refused"`          |MK, PE |ECONNREFUSED|
|`"connection_reset"`            |MK, PE |ECONNRESET|
|`"dns_bogon_error"`             |  PE   |detected bogon in DNS reply|
|`"dns_nxdomain_error"`          |  PE   |NXDOMAIN in DNS reply|
|`"eof_error"`                   |MK, PE |unexpected EOF on connection|
|`"http_request_failed"`         |MK, PE |HTTP request did not return a successful response code|
|`"generic_timeout_error"`       |   -   |some timer has expired|
|`"http_unexpected_redirect_url"`|  PE   |we expected a specific redirect URL and instead we saw either no redirect URL or a different redirect URL|
|`"http_unexpected_status_code"` |  PE   |we did not expected to see this status code (e.g. we expected a redirection and saw something else)|
|`"interrupted"`                 |  PE   |the user interrupted us by cancelling the context|
|`"json_parse_error"`            |MK, PE |parsing of a JSON failed|
|`"ssl_invalid_hostname"`        |MK, PE |certificate not valid for SNI|
|`"ssl_unknown_autority"`        |  PE   |cannot find CA validating certificate|
|`"ssl_invalid_certificate"`     |MK, PE |e.g. certificate expired|
|`"unknown_failure ..."`         |   -   |any other error|



The ooni/probe-legacy contains mostly the legacy errors, listed below.


|              Error                   |Details|
|:------------------------------------:|:-----:|
|`"socks_error"`                       |Generic error in SOCKS code. <mark>Also an (MK) error</mark>|
|`"address_family_not_supported_error"`|[socket.gaierror](https://docs.python.org/3.8/library/socket.html#socket.gaierror)|
|`"connect_error"`                     |[t.i.e.ConnectError](https://twistedmatrix.com/documents/15.4.0/api/twisted.internet.error.ConnectError.html)||
|`"connection_done"`                   |[t.i.e.ConnectionDone](https://twistedmatrix.com/documents/15.4.0/api/twisted.internet.error.ConnectionDone.html)|
|`"connection_lost_error"`             |[t.i.e.ConnectionLost](https://twistedmatrix.com/documents/15.4.0/api/twisted.internet.error.ConnectionLost.html)|
|`"connection_refused_error"`          |[t.i.e.ConnectionRefusedError](https://twistedmatrix.com/documents/15.4.0/api/twisted.internet.error.ConnectionRefusedError.html)|
|`"deferred_timeout_error"`            |[t.i.d.TimeoutError](https://twistedmatrix.com/documents/15.4.0/api/twisted.internet.defer.TimeoutError.html)|
|`"dns_lookup_error"`                  |[t.i.e.DNSLookupError](https://twistedmatrix.com/documents/15.4.0/api/twisted.internet.error.DNSLookupError.html)|
|`"dns_name_error"`                    |[t.n.e.DNSNameError](https://twistedmatrix.com/documents/15.4.0/api/twisted.names.error.DNSNameError.html)|
|`"dns_name_failure"`                  |[t.n.e.DNSServerError](https://twistedmatrix.com/documents/15.4.0/api/twisted.names.error.DNSServerError.html)|
|`"response_never_received"`           |[t.w._newclient.ResponseNeverReceived](https://twistedmatrix.com/documents/15.4.0/api/twisted.web._newclient.ResponseNeverReceived.html)|
|`"socks_address_not_supported"`       |[txsocksx.errors.AddressNotSupported](https://github.com/habnabit/txsocksx/blob/59ac4e088ea064ae9ee44ac371df3ed46ca3b92f/txsocksx/errors.py)|
|`"socks_command_not_supported"`       |[txsocksx.errors.CommandNotSupported](https://github.com/habnabit/txsocksx/blob/59ac4e088ea064ae9ee44ac371df3ed46ca3b92f/txsocksx/errors.py)|
|`"socks_connection_not_allowed"`      |[txsocksx.errors.ConnectionNotAllowed](https://github.com/habnabit/txsocksx/blob/59ac4e088ea064ae9ee44ac371df3ed46ca3b92f/txsocksx/errors.py)|
|`"socks_connection_refused"`          |[txsocksx.errors.ConnectionRefused](https://github.com/habnabit/txsocksx/blob/59ac4e088ea064ae9ee44ac371df3ed46ca3b92f/txsocksx/errors.py)|
|`"socks_host_unreachable"`            |[txsocksx.errors.HostUnreachable](https://github.com/habnabit/txsocksx/blob/59ac4e088ea064ae9ee44ac371df3ed46ca3b92f/txsocksx/errors.py)|
|`"socks_network_unreachable"`         |[txsocksx.errors.NetworkUnreachable](https://github.com/habnabit/txsocksx/blob/59ac4e088ea064ae9ee44ac371df3ed46ca3b92f/txsocksx/errors.py)
|`"socks_server_failure"`              |[txsocksx.errors.ServerFailure](https://github.com/habnabit/txsocksx/blob/59ac4e088ea064ae9ee44ac371df3ed46ca3b92f/txsocksx/errors.py)|
|`"socks_ttl_expired"`                 |[txsocksx.errors.TTLExpired](https://github.com/habnabit/txsocksx/blob/59ac4e088ea064ae9ee44ac371df3ed46ca3b92f/txsocksx/errors.py)|
|`"task_timed_out"`                    |a task has timed out|
|`"tcp_timed_out_error"`               |[t.i.e.TCPTimedOutError](https://twistedmatrix.com/documents/15.4.0/api/twisted.internet.error.TCPTimedOutError.html)|
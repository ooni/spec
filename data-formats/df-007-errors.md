# Errors

This document describes the possible values of the `failure` key that
occurs in several data formats to indicate a failure. See this directory's
[README](README.md) for the basic concepts.

To indicate that an error is emitted by ooni/probe-legacy we will flag
the error using `(PL)`. To indicate that an error is emitted by Measurement
Kit, we will flag it using `(MK)`. To indicate that an error is emitted by
ooni/probe-engine, we will flag it using `(PE)`. When an error is emitted
by more than one product we will write `(product, product)`. When an error
is not flagged, it means that it's used by all the three products.

- `null`: no error has occurred

- `"address_family_not_supported_error"` (PL): [socket.gaierror](https://docs.python.org/3.8/library/socket.html#socket.gaierror)

- `"connect_error"` (PL): [t.i.e.ConnectError](https://twistedmatrix.com/documents/15.4.0/api/twisted.internet.error.ConnectError.html)

- `"connection_done"` (PL): [t.i.e.ConnectionDone](https://twistedmatrix.com/documents/15.4.0/api/twisted.internet.error.ConnectionDone.html)

- `"connection_lost_error"` (PL): [t.i.e.ConnectionLost](https://twistedmatrix.com/documents/15.4.0/api/twisted.internet.error.ConnectionLost.html)

- `"connection_refused_error"` (PL): [t.i.e.ConnectionRefusedError](https://twistedmatrix.com/documents/15.4.0/api/twisted.internet.error.ConnectionRefusedError.html)

- `"connection_refused"` (MK, PE): ECONNREFUSED

- `"connection_reset"` (MK, PE): ECONNRESET

- `"deferred_timeout_error"` (PL): [t.i.d.TimeoutError](https://twistedmatrix.com/documents/15.4.0/api/twisted.internet.defer.TimeoutError.html)

- `"dns_bogon_error"` (PE): detected bogon in DNS reply

- `"dns_lookup_error"` (PL): [t.i.e.DNSLookupError](https://twistedmatrix.com/documents/15.4.0/api/twisted.internet.error.DNSLookupError.html)

- `"dns_name_error"` (PL): [t.n.e.DNSNameError](https://twistedmatrix.com/documents/15.4.0/api/twisted.names.error.DNSNameError.html)

- `"dns_name_failure"` (PL): [t.n.e.DNSServerError](https://twistedmatrix.com/documents/15.4.0/api/twisted.names.error.DNSServerError.html)

- `"dns_nxdomain_error"` (PE): NXDOMAIN in DNS reply

- `"eof_error"` (MK, PE): unexpected EOF on connection

- `"generic_timeout_error"`: some timer has expired

- `"response_never_received"` (PL): [t.w._newclient.ResponseNeverReceived](https://twistedmatrix.com/documents/15.4.0/api/twisted.web._newclient.ResponseNeverReceived.html)

- `"socks_address_not_supported"` (PL): [txsocksx.errors.AddressNotSupported](https://github.com/habnabit/txsocksx/blob/59ac4e088ea064ae9ee44ac371df3ed46ca3b92f/txsocksx/errors.py)

- `"socks_command_not_supported"` (PL): [txsocksx.errors.CommandNotSupported](https://github.com/habnabit/txsocksx/blob/59ac4e088ea064ae9ee44ac371df3ed46ca3b92f/txsocksx/errors.py)

- `"socks_connection_not_allowed"` (PL): [txsocksx.errors.ConnectionNotAllowed](https://github.com/habnabit/txsocksx/blob/59ac4e088ea064ae9ee44ac371df3ed46ca3b92f/txsocksx/errors.py)

- `"socks_connection_refused"` (PL): [txsocksx.errors.ConnectionRefused](https://github.com/habnabit/txsocksx/blob/59ac4e088ea064ae9ee44ac371df3ed46ca3b92f/txsocksx/errors.py)

- `"socks_error"` (PL, MK): Generic error in SOCKS code

- `"socks_host_unreachable"` (PL): [txsocksx.errors.HostUnreachable](https://github.com/habnabit/txsocksx/blob/59ac4e088ea064ae9ee44ac371df3ed46ca3b92f/txsocksx/errors.py)

- `"socks_network_unreachable"` (PL): [txsocksx.errors.NetworkUnreachable](https://github.com/habnabit/txsocksx/blob/59ac4e088ea064ae9ee44ac371df3ed46ca3b92f/txsocksx/errors.py)

- `"socks_server_failure"` (PL): [txsocksx.errors.ServerFailure](https://github.com/habnabit/txsocksx/blob/59ac4e088ea064ae9ee44ac371df3ed46ca3b92f/txsocksx/errors.py)

- `"socks_ttl_expired"` (PL): [txsocksx.errors.TTLExpired](https://github.com/habnabit/txsocksx/blob/59ac4e088ea064ae9ee44ac371df3ed46ca3b92f/txsocksx/errors.py)

- `"ssl_invalid_hostname"` (MK, PE): certificate not valid for SNI

- `"ssl_unknown_autority"` (PE): cannot find CA validating certificate

- `"ssl_invalid_certificate"` (MK, PE): e.g. certificate expired

- `"task_timed_out"` (PL): a task has timed out

- `"tcp_timed_out_error"` (PL): [t.i.e.TCPTimedOutError](https://twistedmatrix.com/documents/15.4.0/api/twisted.internet.error.TCPTimedOutError.html)

- `"unknown_failure ..."`: any other error

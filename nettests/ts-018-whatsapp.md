# Specification version number

2022-12-07-001

* _status_: current

# Specification name

WhatsApp

# Test preconditions

* An internet connection

# Expected impact

Ability to detect whether specific services used by WhatsApp are
accessible and working as intended. Even if this test does not detect
any issue, WhatsApp may still be blocked in more complex ways.

# Expected inputs

None

# Test description

This test will check if 3 services are working as they should:

1. The whatsapp endpoints used by the WhatsApp mobile app;

2. The registration service, i.e. the service used to register a new account;

3. The WhatsApp web interface.

## WhatsApp endpoints check

The WhatsApp endpoints are those used by the WhatsApp app to send and receive
messages. These endpoints have the following hostnames:

* e1.whatsapp.net
* e2.whatsapp.net
* e3.whatsapp.net
* e4.whatsapp.net
* e5.whatsapp.net
* e6.whatsapp.net
* e7.whatsapp.net
* e8.whatsapp.net
* e9.whatsapp.net
* e10.whatsapp.net
* e11.whatsapp.net
* e12.whatsapp.net
* e13.whatsapp.net
* e14.whatsapp.net
* e15.whatsapp.net
* e16.whatsapp.net

The behaviour of the WhatsApp app is to attempt to connect to each of the
following hostnames on ports 443 and 5222 until one succeeds. A previous
version of this specification checked only just one of the above endpoints,
but since 2020-07-09 we check all the endpoints on ports 443 and 5222.

We lookup every domain name and record the ASN of each returned IP, deferring to
OONI data processing pipeline to determine whether the IP is legitimate.

If we can connect to at least one endpoint, we set:

```JSON
{
    "whatsapp_endpoints_status": "ok",
}
```

If all endpoints fail, we set:

```JSON
{
    "whatsapp_endpoints_status": "blocked",
}
```

Therefore, this specific key tells us whether the WhatsApp would work by
attempting with each of the hardcoded endpoints on ports 443 and 5222.

As of 2020-07-09, all endpoints work with ports 443 and 5222 from an
unfiltered network connection. If an endpoint fails for both ports, then
we consider it blocked and we add it to the list of blocked endpoints
as follows:

```JSON
{
    "whatsapp_endpoints_blocked": [
        "e1.whatsapp.net"
    ]
}
```

If only a single port of an endpoint fails, we do not include the
endpoint in the list of blocked endpoints. (This specific choice
retains backwards compatibility with previous versions of this spec.)

If all endpoints work for at least one port, we simply do not
insert any endpoint inside the list, as follows:

```JSON
{
    "whatsapp_endpoints_blocked": []
}
```

We always additionally write into the report:

```JSON
{
    "whatsapp_endpoints_dns_inconsistent": []
}
```

The `whatsapp_endpoints_dns_inconsistent` key is a legacy key that we
used to compute whether an endpoint was part of the WhatsApp address
space, but this check has been broken since at least 2020-02-17, so we
first disabled the check and then updated the spec to sync up with
the actual implementation of the experiment.

## Registration service check

The registration service is used by WhatsApp to register a number to a
whatsapp account. As such blocking the registration service inhibits new
account creations.

The registration service is a `https` service at the following URL:
https://v.whatsapp.net/v2/register.

To check if it is working properly we do a HTTP GET request to
`https://v.whatsapp.net/v2/register`. We conside this request to
be successful if we don't see any DNS, TCP connect, TLS, or I/O
error. We don't rely on the HTTP status code to determine whether
this request succeeded, because we assume it is enough to determine
whether we could have an HTTPS conversation with this service.

If there is no failure, we write in the report:

```json
{
    "registration_server_status": "ok",
    "registration_server_failure": null
}
```

When it fails we write:

```json
{
    "registration_server_status": "blocked",
    "registration_server_failure": "FAILURE STRING"
}
```

## WhatApp web check

WhatsApp web is the service by which users are able to use WhatsApp from a
web browser on their computer. When using WhatsApp web users scan a QR code
displayed in the browser from their phone to authenticate the web app.

For the service to work a user needs to have whatsapp be working properly
from their phone (it needs to be unblocked there) and if the "Keep me signed
in" option is unticked their phone needs to be connected to the internet and
be able to reach the whatsapp endpoints for the duration of the session.

We check to see if WhatsApp web is working properly by doing a HTTPS GET request
to the following URLs:

* https://web.whatsapp.com/

We consider the GET for the HTTPS URL successful if we do not see any
DNS, TCP connect, TLS, or I/O errors when fetching the URL. WhatsApp may
return an 400 Bad Request response if the User-Agent header we use does
not seem to be consistent with our ClientHello.

Until 2022-12-07, we also checked for http://web.whatsapp.com. Afterwards,
we dropped this check with [ooni/probe-cli#998](https://github.com/ooni/probe-cli/pull/998)
to address [ooni/ooni.org#1317](https://github.com/ooni/ooni.org/issues/1317).

If the HTTPS endpoints is blocked then we write
in the report:

```json
{
    "whatsapp_web_status": "blocked",
    "whatsapp_web_failure": "FAILURE STRING"
}
```

If it is not blocked then we write:

```json
{
    "whatsapp_web_status": "ok",
    "whatsapp_web_failure": null
}
```

# Expected output

## Parent data format

* df-001-httpt

* df-002-dnst

* df-005-tcpconnect

* df-006-tlshandshake

* df-008-netevents

## Semantics

The `test_keys` emitted by this nettest include the following keys:

```JSON
{
    "network_events": [],
    "queries": [],
    "requests": [],
    "tcp_connect": [],
    "tls_handshakes": [],

    "registration_server_failure": null,
    "registration_server_status": "ok",
    "whatsapp_endpoints_blocked": [],
    "whatsapp_endpoints_dns_inconsistent": [],
    "whatsapp_endpoints_status": "ok",
    "whatsapp_web_failure": null,
    "whatsapp_web_status": "ok"
}
```

where:

- `network_events` (`[]NetworkEvent`; nullable): see `df-008-netevents`;

- `queries` (`[]Query`; nullable): see `df-002-dnst`;

- `requests` (`[]Transaction`; nullable): see `df-001-httpt`;

- `tcp_connect` (`[]TCPConnect`; nullable): see `df-005-tcpconnect`;

- `tls_handshakes` (`[]Handshake`; nullable): see `df-006-tlshandshake`;

- `registration_server_failure` (`string`; nullable): the failure when
accessing the registration server (see `df-007-errors.md`);

- `registration_server_status` (`string`): one of `"ok"` and `"blocked"`;

- `whatsapp_endpoints_blocked` (`[]string`): list of blocked endpoints;

- `whatsapp_endpoints_dns_inconsistent` (`[]string`): legacy key
that is always empty;

- `whatsapp_endpoints_status` (`string`): one of `"ok"` and `"blocked"`;

- `whatsapp_web_failure` (`string`; nullable): the failure when
accessing the WhatsApp web interface (see `df-007-errors.md`);

- `whatsapp_web_status` (`string`): one of `"ok"` and `"blocked"`.

## Possible conclusions

* If it is possible for users to create new accounts via WhatsApp

* If it is possible for users to use WhatsApp Web

* If it is possible for users to use the WhatsApp software

## Example output sample

```JSON
{
  "annotations": {
    "architecture": "arm64",
    "engine_name": "ooniprobe-engine",
    "engine_version": "3.17.0-alpha",
    "platform": "macos"
  },
  "data_format_version": "0.2.0",
  "extensions": {
    "dnst": 0,
    "httpt": 0,
    "netevents": 0,
    "tcpconnect": 0,
    "tlshandshake": 0,
    "tunnel": 0
  },
  "input": null,
  "measurement_start_time": "2022-12-07 09:52:48",
  "probe_asn": "AS30722",
  "probe_cc": "IT",
  "probe_ip": "127.0.0.1",
  "probe_network_name": "Vodafone Italia S.p.A.",
  "report_id": "20221207T095248Z_whatsapp_IT_30722_n1_jwFo3mIUDj120GFH",
  "resolver_asn": "AS30722",
  "resolver_ip": "91.80.36.88",
  "resolver_network_name": "Vodafone Italia S.p.A.",
  "software_name": "miniooni",
  "software_version": "3.17.0-alpha",
  "test_keys": {
    "agent": "redirect",
    "failed_operation": null,
    "failure": null,
    "network_events": [
      {
        "failure": null,
        "operation": "resolve_start",
        "t": 0.000478042
      },
      {
        "failure": null,
        "operation": "resolve_done",
        "t": 0.021444625
      },
      {
        "address": "3.33.252.61:443",
        "failure": null,
        "operation": "connect",
        "proto": "tcp",
        "t": 0.038953792
      },
      {
        "failure": null,
        "operation": "resolve_start",
        "t": 0.000449417
      },
      {
        "failure": null,
        "operation": "resolve_done",
        "t": 0.022710292
      },
      {
        "address": "3.33.252.61:443",
        "failure": null,
        "operation": "connect",
        "proto": "tcp",
        "t": 0.039018709
      },
      {
        "failure": null,
        "operation": "resolve_start",
        "t": 0.000431709
      },
      {
        "failure": null,
        "operation": "resolve_done",
        "t": 0.022696625
      },
      {
        "address": "3.33.221.48:5222",
        "failure": null,
        "operation": "connect",
        "proto": "tcp",
        "t": 0.03902025
      },
      {
        "failure": null,
        "operation": "resolve_start",
        "t": 0.03934675
      },
      {
        "failure": null,
        "operation": "resolve_done",
        "t": 0.05877325
      },
      {
        "address": "3.33.252.61:443",
        "failure": null,
        "operation": "connect",
        "proto": "tcp",
        "t": 0.073610834
      },
      {
        "failure": null,
        "operation": "resolve_start",
        "t": 0.039493834
      },
      {
        "failure": null,
        "operation": "resolve_done",
        "t": 0.061327167
      },
      {
        "address": "15.197.210.208:443",
        "failure": null,
        "operation": "connect",
        "proto": "tcp",
        "t": 0.075890875
      },
      {
        "failure": null,
        "operation": "resolve_start",
        "t": 0.0396
      },
      {
        "failure": null,
        "operation": "resolve_done",
        "t": 0.064785709
      },
      {
        "address": "15.197.206.217:443",
        "failure": null,
        "operation": "connect",
        "proto": "tcp",
        "t": 0.082615
      },
      {
        "failure": null,
        "operation": "resolve_start",
        "t": 0.073848042
      },
      {
        "failure": null,
        "operation": "resolve_done",
        "t": 0.093433667
      },
      {
        "address": "3.33.221.48:443",
        "failure": null,
        "operation": "connect",
        "proto": "tcp",
        "t": 0.109965334
      },
      {
        "failure": null,
        "operation": "resolve_start",
        "t": 0.076044167
      },
      {
        "failure": null,
        "operation": "resolve_done",
        "t": 0.094401917
      },
      {
        "address": "15.197.210.208:5222",
        "failure": null,
        "operation": "connect",
        "proto": "tcp",
        "t": 0.111479792
      },
      {
        "failure": null,
        "operation": "resolve_start",
        "t": 0.111564
      },
      {
        "failure": null,
        "operation": "resolve_done",
        "t": 0.12930825
      },
      {
        "address": "15.197.210.208:443",
        "failure": null,
        "operation": "connect",
        "proto": "tcp",
        "t": 0.144534042
      },
      {
        "failure": null,
        "operation": "resolve_start",
        "t": 0.110089542
      },
      {
        "failure": null,
        "operation": "resolve_done",
        "t": 0.128412625
      },
      {
        "address": "3.33.221.48:443",
        "failure": null,
        "operation": "connect",
        "proto": "tcp",
        "t": 0.144595959
      },
      {
        "failure": null,
        "operation": "resolve_start",
        "t": 0.144663417
      },
      {
        "failure": null,
        "operation": "resolve_done",
        "t": 0.146710875
      },
      {
        "address": "15.197.206.217:5222",
        "failure": null,
        "operation": "connect",
        "proto": "tcp",
        "t": 0.163556292
      },
      {
        "failure": null,
        "operation": "resolve_start",
        "t": 0.163757792
      },
      {
        "failure": null,
        "operation": "resolve_done",
        "t": 0.164956042
      },
      {
        "address": "15.197.210.208:443",
        "failure": null,
        "operation": "connect",
        "proto": "tcp",
        "t": 0.1809045
      },
      {
        "failure": null,
        "operation": "resolve_start",
        "t": 0.144713167
      },
      {
        "failure": null,
        "operation": "resolve_done",
        "t": 0.164855417
      },
      {
        "address": "3.33.252.61:5222",
        "failure": null,
        "operation": "connect",
        "proto": "tcp",
        "t": 0.182005834
      },
      {
        "failure": null,
        "operation": "http_transaction_start",
        "t": 0.082829125
      },
      {
        "failure": null,
        "operation": "resolve_start",
        "t": 0.082947
      },
      {
        "failure": null,
        "operation": "resolve_done",
        "t": 0.103592209
      },
      {
        "address": "31.13.86.51:443",
        "failure": null,
        "operation": "connect",
        "proto": "tcp",
        "t": 0.117675834
      },
      {
        "failure": null,
        "operation": "tls_handshake_start",
        "t": 0.117684875
      },
      {
        "failure": null,
        "num_bytes": 282,
        "operation": "write",
        "t": 0.118151209
      },
      {
        "failure": null,
        "num_bytes": 517,
        "operation": "read",
        "t": 0.133623625
      },
      {
        "failure": null,
        "num_bytes": 863,
        "operation": "read",
        "t": 0.13415775
      },
      {
        "failure": null,
        "num_bytes": 1788,
        "operation": "read",
        "t": 0.134639542
      },
      {
        "failure": null,
        "num_bytes": 64,
        "operation": "write",
        "t": 0.135941125
      },
      {
        "failure": null,
        "operation": "tls_handshake_done",
        "t": 0.13597625
      },
      {
        "failure": null,
        "num_bytes": 86,
        "operation": "write",
        "t": 0.13605525
      },
      {
        "failure": null,
        "num_bytes": 198,
        "operation": "write",
        "t": 0.136145459
      },
      {
        "failure": null,
        "num_bytes": 140,
        "operation": "read",
        "t": 0.151334959
      },
      {
        "failure": null,
        "num_bytes": 31,
        "operation": "write",
        "t": 0.151386042
      },
      {
        "failure": null,
        "num_bytes": 1897,
        "operation": "read",
        "t": 0.189129209
      },
      {
        "failure": null,
        "operation": "http_transaction_done",
        "t": 0.189301417
      },
      {
        "failure": null,
        "num_bytes": 24,
        "operation": "write",
        "t": 0.1894065
      },
      {
        "failure": "connection_already_closed",
        "operation": "read",
        "t": 0.189455125
      },
      {
        "failure": null,
        "operation": "resolve_start",
        "t": 0.182216959
      },
      {
        "failure": null,
        "operation": "resolve_done",
        "t": 0.184475959
      },
      {
        "address": "3.33.252.61:5222",
        "failure": null,
        "operation": "connect",
        "proto": "tcp",
        "t": 0.200444875
      },
      {
        "failure": null,
        "operation": "resolve_start",
        "t": 0.18116825
      },
      {
        "failure": null,
        "operation": "resolve_done",
        "t": 0.198820584
      },
      {
        "address": "15.197.206.217:5222",
        "failure": null,
        "operation": "connect",
        "proto": "tcp",
        "t": 0.215879542
      },
      {
        "failure": null,
        "operation": "resolve_start",
        "t": 0.200522917
      },
      {
        "failure": null,
        "operation": "resolve_done",
        "t": 0.209702125
      },
      {
        "address": "3.33.221.48:443",
        "failure": null,
        "operation": "connect",
        "proto": "tcp",
        "t": 0.227087375
      },
      {
        "failure": null,
        "operation": "resolve_start",
        "t": 0.189874834
      },
      {
        "failure": null,
        "operation": "resolve_done",
        "t": 0.209710709
      },
      {
        "address": "3.33.221.48:5222",
        "failure": null,
        "operation": "connect",
        "proto": "tcp",
        "t": 0.227118875
      },
      {
        "failure": null,
        "operation": "resolve_start",
        "t": 0.227215875
      },
      {
        "failure": null,
        "operation": "resolve_done",
        "t": 0.228273459
      },
      {
        "address": "3.33.221.48:5222",
        "failure": null,
        "operation": "connect",
        "proto": "tcp",
        "t": 0.247043084
      },
      {
        "failure": null,
        "operation": "resolve_start",
        "t": 0.216049417
      },
      {
        "failure": null,
        "operation": "resolve_done",
        "t": 0.236456625
      },
      {
        "address": "15.197.210.208:443",
        "failure": null,
        "operation": "connect",
        "proto": "tcp",
        "t": 0.250968459
      },
      {
        "failure": null,
        "operation": "resolve_start",
        "t": 0.22725675
      },
      {
        "failure": null,
        "operation": "resolve_done",
        "t": 0.248662917
      },
      {
        "address": "15.197.210.208:5222",
        "failure": null,
        "operation": "connect",
        "proto": "tcp",
        "t": 0.266117875
      },
      {
        "failure": null,
        "operation": "resolve_start",
        "t": 0.247174459
      },
      {
        "failure": null,
        "operation": "resolve_done",
        "t": 0.248173292
      },
      {
        "address": "3.33.252.61:5222",
        "failure": null,
        "operation": "connect",
        "proto": "tcp",
        "t": 0.266169084
      },
      {
        "failure": null,
        "operation": "resolve_start",
        "t": 0.266215709
      },
      {
        "failure": null,
        "operation": "resolve_done",
        "t": 0.267222834
      },
      {
        "address": "15.197.206.217:443",
        "failure": null,
        "operation": "connect",
        "proto": "tcp",
        "t": 0.283247042
      },
      {
        "failure": null,
        "operation": "resolve_start",
        "t": 0.266291542
      },
      {
        "failure": null,
        "operation": "resolve_done",
        "t": 0.267509625
      },
      {
        "address": "3.33.221.48:443",
        "failure": null,
        "operation": "connect",
        "proto": "tcp",
        "t": 0.284150625
      },
      {
        "failure": null,
        "operation": "resolve_start",
        "t": 0.251029042
      },
      {
        "failure": null,
        "operation": "resolve_done",
        "t": 0.271013417
      },
      {
        "address": "3.33.221.48:5222",
        "failure": null,
        "operation": "connect",
        "proto": "tcp",
        "t": 0.289730209
      },
      {
        "failure": null,
        "operation": "resolve_start",
        "t": 0.283427334
      },
      {
        "failure": null,
        "operation": "resolve_done",
        "t": 0.284613084
      },
      {
        "address": "3.33.221.48:443",
        "failure": null,
        "operation": "connect",
        "proto": "tcp",
        "t": 0.29997075
      },
      {
        "failure": null,
        "operation": "resolve_start",
        "t": 0.28425975
      },
      {
        "failure": null,
        "operation": "resolve_done",
        "t": 0.285060167
      },
      {
        "address": "3.33.221.48:5222",
        "failure": null,
        "operation": "connect",
        "proto": "tcp",
        "t": 0.300009084
      },
      {
        "failure": null,
        "operation": "resolve_start",
        "t": 0.289827875
      },
      {
        "failure": null,
        "operation": "resolve_done",
        "t": 0.290794917
      },
      {
        "address": "15.197.210.208:5222",
        "failure": null,
        "operation": "connect",
        "proto": "tcp",
        "t": 0.30852475
      },
      {
        "failure": null,
        "operation": "resolve_start",
        "t": 0.300104709
      },
      {
        "failure": null,
        "operation": "resolve_done",
        "t": 0.301412167
      },
      {
        "address": "15.197.210.208:5222",
        "failure": null,
        "operation": "connect",
        "proto": "tcp",
        "t": 0.318773292
      },
      {
        "failure": null,
        "operation": "resolve_start",
        "t": 0.308634875
      },
      {
        "failure": null,
        "operation": "resolve_done",
        "t": 0.309714084
      },
      {
        "address": "15.197.210.208:443",
        "failure": null,
        "operation": "connect",
        "proto": "tcp",
        "t": 0.326225
      },
      {
        "failure": null,
        "operation": "resolve_start",
        "t": 0.318950917
      },
      {
        "failure": null,
        "operation": "resolve_done",
        "t": 0.321179042
      },
      {
        "address": "3.33.252.61:443",
        "failure": null,
        "operation": "connect",
        "proto": "tcp",
        "t": 0.336746667
      },
      {
        "failure": null,
        "operation": "resolve_start",
        "t": 0.326380375
      },
      {
        "failure": null,
        "operation": "resolve_done",
        "t": 0.327117875
      },
      {
        "address": "3.33.252.61:5222",
        "failure": null,
        "operation": "connect",
        "proto": "tcp",
        "t": 0.342397167
      },
      {
        "failure": null,
        "operation": "resolve_start",
        "t": 0.336840584
      },
      {
        "failure": null,
        "operation": "resolve_done",
        "t": 0.337729667
      },
      {
        "address": "15.197.210.208:5222",
        "failure": null,
        "operation": "connect",
        "proto": "tcp",
        "t": 0.352054625
      },
      {
        "failure": null,
        "operation": "http_transaction_start",
        "t": 0.300085459
      },
      {
        "failure": null,
        "operation": "resolve_start",
        "t": 0.3001635
      },
      {
        "failure": null,
        "operation": "resolve_done",
        "t": 0.321002042
      },
      {
        "address": "31.13.86.51:443",
        "failure": null,
        "operation": "connect",
        "proto": "tcp",
        "t": 0.335926709
      },
      {
        "failure": null,
        "operation": "tls_handshake_start",
        "t": 0.335937584
      },
      {
        "failure": null,
        "num_bytes": 280,
        "operation": "write",
        "t": 0.336195042
      },
      {
        "failure": null,
        "num_bytes": 517,
        "operation": "read",
        "t": 0.353721334
      },
      {
        "failure": null,
        "num_bytes": 1800,
        "operation": "read",
        "t": 0.353978417
      },
      {
        "failure": null,
        "num_bytes": 850,
        "operation": "read",
        "t": 0.354016084
      },
      {
        "failure": null,
        "num_bytes": 64,
        "operation": "write",
        "t": 0.354682584
      },
      {
        "failure": null,
        "operation": "tls_handshake_done",
        "t": 0.354731125
      },
      {
        "failure": null,
        "num_bytes": 86,
        "operation": "write",
        "t": 0.354832417
      },
      {
        "failure": null,
        "num_bytes": 206,
        "operation": "write",
        "t": 0.354974334
      },
      {
        "failure": null,
        "num_bytes": 118,
        "operation": "read",
        "t": 0.369096292
      },
      {
        "failure": null,
        "num_bytes": 31,
        "operation": "write",
        "t": 0.36922525
      },
      {
        "failure": null,
        "num_bytes": 181,
        "operation": "read",
        "t": 0.477104959
      },
      {
        "failure": null,
        "operation": "http_transaction_done",
        "t": 0.477391917
      },
      {
        "failure": null,
        "num_bytes": 24,
        "operation": "write",
        "t": 0.477605667
      },
      {
        "failure": "connection_already_closed",
        "operation": "read",
        "t": 0.477723875
      }
    ],
    "queries": [
      {
        "answers": [
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "3.33.252.61",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "15.197.210.208",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "3.33.221.48",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "15.197.206.217",
            "ttl": null
          }
        ],
        "engine": "system",
        "failure": null,
        "hostname": "e5.whatsapp.net",
        "query_type": "A",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "",
        "t": 0.021444625
      },
      {
        "answers": [
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "3.33.252.61",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "15.197.210.208",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "3.33.221.48",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "15.197.206.217",
            "ttl": null
          }
        ],
        "engine": "system",
        "failure": null,
        "hostname": "e1.whatsapp.net",
        "query_type": "A",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "",
        "t": 0.022710292
      },
      {
        "answers": [
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "3.33.221.48",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "15.197.206.217",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "15.197.210.208",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "3.33.252.61",
            "ttl": null
          }
        ],
        "engine": "system",
        "failure": null,
        "hostname": "e10.whatsapp.net",
        "query_type": "A",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "",
        "t": 0.022696625
      },
      {
        "answers": [
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "3.33.252.61",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "15.197.206.217",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "3.33.221.48",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "15.197.210.208",
            "ttl": null
          }
        ],
        "engine": "system",
        "failure": null,
        "hostname": "e11.whatsapp.net",
        "query_type": "A",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "",
        "t": 0.05877325
      },
      {
        "answers": [
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "15.197.210.208",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "3.33.221.48",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "3.33.252.61",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "15.197.206.217",
            "ttl": null
          }
        ],
        "engine": "system",
        "failure": null,
        "hostname": "e8.whatsapp.net",
        "query_type": "A",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "",
        "t": 0.061327167
      },
      {
        "answers": [
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "15.197.206.217",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "15.197.210.208",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "3.33.252.61",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "3.33.221.48",
            "ttl": null
          }
        ],
        "engine": "system",
        "failure": null,
        "hostname": "e6.whatsapp.net",
        "query_type": "A",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "",
        "t": 0.064785709
      },
      {
        "answers": [
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "3.33.221.48",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "15.197.210.208",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "3.33.252.61",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "15.197.206.217",
            "ttl": null
          }
        ],
        "engine": "system",
        "failure": null,
        "hostname": "e2.whatsapp.net",
        "query_type": "A",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "",
        "t": 0.093433667
      },
      {
        "answers": [
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "15.197.210.208",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "3.33.252.61",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "15.197.206.217",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "3.33.221.48",
            "ttl": null
          }
        ],
        "engine": "system",
        "failure": null,
        "hostname": "e12.whatsapp.net",
        "query_type": "A",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "",
        "t": 0.094401917
      },
      {
        "answers": [
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "15.197.210.208",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "15.197.206.217",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "3.33.221.48",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "3.33.252.61",
            "ttl": null
          }
        ],
        "engine": "system",
        "failure": null,
        "hostname": "e4.whatsapp.net",
        "query_type": "A",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "",
        "t": 0.12930825
      },
      {
        "answers": [
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "3.33.221.48",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "3.33.252.61",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "15.197.206.217",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "15.197.210.208",
            "ttl": null
          }
        ],
        "engine": "system",
        "failure": null,
        "hostname": "e14.whatsapp.net",
        "query_type": "A",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "",
        "t": 0.128412625
      },
      {
        "answers": [
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "15.197.206.217",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "15.197.210.208",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "3.33.252.61",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "3.33.221.48",
            "ttl": null
          }
        ],
        "engine": "system",
        "failure": null,
        "hostname": "e6.whatsapp.net",
        "query_type": "A",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "",
        "t": 0.146710875
      },
      {
        "answers": [
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "15.197.210.208",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "3.33.252.61",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "15.197.206.217",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "3.33.221.48",
            "ttl": null
          }
        ],
        "engine": "system",
        "failure": null,
        "hostname": "e12.whatsapp.net",
        "query_type": "A",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "",
        "t": 0.164956042
      },
      {
        "answers": [
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "3.33.252.61",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "15.197.210.208",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "3.33.221.48",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "15.197.206.217",
            "ttl": null
          }
        ],
        "engine": "system",
        "failure": null,
        "hostname": "e16.whatsapp.net",
        "query_type": "A",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "",
        "t": 0.164855417
      },
      {
        "answers": [
          {
            "asn": 32934,
            "as_org_name": "Facebook, Inc.",
            "answer_type": "A",
            "ipv4": "31.13.86.51",
            "ttl": null
          }
        ],
        "engine": "system",
        "failure": null,
        "hostname": "web.whatsapp.com",
        "query_type": "A",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "",
        "t": 0.103592209
      },
      {
        "answers": [
          {
            "asn": 32934,
            "as_org_name": "Facebook, Inc.",
            "answer_type": "AAAA",
            "ipv6": "2a03:2880:f208:c5:face:b00c:0:167",
            "ttl": null
          }
        ],
        "engine": "system",
        "failure": null,
        "hostname": "web.whatsapp.com",
        "query_type": "AAAA",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "",
        "t": 0.103592209
      },
      {
        "answers": [
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "3.33.252.61",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "15.197.210.208",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "3.33.221.48",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "15.197.206.217",
            "ttl": null
          }
        ],
        "engine": "system",
        "failure": null,
        "hostname": "e5.whatsapp.net",
        "query_type": "A",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "",
        "t": 0.184475959
      },
      {
        "answers": [
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "15.197.206.217",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "3.33.221.48",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "3.33.252.61",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "15.197.210.208",
            "ttl": null
          }
        ],
        "engine": "system",
        "failure": null,
        "hostname": "e7.whatsapp.net",
        "query_type": "A",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "",
        "t": 0.198820584
      },
      {
        "answers": [
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "3.33.221.48",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "15.197.210.208",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "15.197.206.217",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "3.33.252.61",
            "ttl": null
          }
        ],
        "engine": "system",
        "failure": null,
        "hostname": "e3.whatsapp.net",
        "query_type": "A",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "",
        "t": 0.209702125
      },
      {
        "answers": [
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "3.33.221.48",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "15.197.210.208",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "15.197.206.217",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "3.33.252.61",
            "ttl": null
          }
        ],
        "engine": "system",
        "failure": null,
        "hostname": "e3.whatsapp.net",
        "query_type": "A",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "",
        "t": 0.209710709
      },
      {
        "answers": [
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "3.33.221.48",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "15.197.210.208",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "3.33.252.61",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "15.197.206.217",
            "ttl": null
          }
        ],
        "engine": "system",
        "failure": null,
        "hostname": "e2.whatsapp.net",
        "query_type": "A",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "",
        "t": 0.228273459
      },
      {
        "answers": [
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "15.197.210.208",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "3.33.252.61",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "15.197.206.217",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "3.33.221.48",
            "ttl": null
          }
        ],
        "engine": "system",
        "failure": null,
        "hostname": "e15.whatsapp.net",
        "query_type": "A",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "",
        "t": 0.236456625
      },
      {
        "answers": [
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "15.197.210.208",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "3.33.221.48",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "3.33.252.61",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "15.197.206.217",
            "ttl": null
          }
        ],
        "engine": "system",
        "failure": null,
        "hostname": "e13.whatsapp.net",
        "query_type": "A",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "",
        "t": 0.248662917
      },
      {
        "answers": [
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "3.33.252.61",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "15.197.210.208",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "3.33.221.48",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "15.197.206.217",
            "ttl": null
          }
        ],
        "engine": "system",
        "failure": null,
        "hostname": "e1.whatsapp.net",
        "query_type": "A",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "",
        "t": 0.248173292
      },
      {
        "answers": [
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "15.197.206.217",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "3.33.221.48",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "3.33.252.61",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "15.197.210.208",
            "ttl": null
          }
        ],
        "engine": "system",
        "failure": null,
        "hostname": "e7.whatsapp.net",
        "query_type": "A",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "",
        "t": 0.267222834
      },
      {
        "answers": [
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "3.33.221.48",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "15.197.206.217",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "15.197.210.208",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "3.33.252.61",
            "ttl": null
          }
        ],
        "engine": "system",
        "failure": null,
        "hostname": "e10.whatsapp.net",
        "query_type": "A",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "",
        "t": 0.267509625
      },
      {
        "answers": [
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "3.33.221.48",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "15.197.210.208",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "15.197.206.217",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "3.33.252.61",
            "ttl": null
          }
        ],
        "engine": "system",
        "failure": null,
        "hostname": "e9.whatsapp.net",
        "query_type": "A",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "",
        "t": 0.271013417
      },
      {
        "answers": [
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "3.33.221.48",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "15.197.210.208",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "15.197.206.217",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "3.33.252.61",
            "ttl": null
          }
        ],
        "engine": "system",
        "failure": null,
        "hostname": "e9.whatsapp.net",
        "query_type": "A",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "",
        "t": 0.284613084
      },
      {
        "answers": [
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "3.33.221.48",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "3.33.252.61",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "15.197.206.217",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "15.197.210.208",
            "ttl": null
          }
        ],
        "engine": "system",
        "failure": null,
        "hostname": "e14.whatsapp.net",
        "query_type": "A",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "",
        "t": 0.285060167
      },
      {
        "answers": [
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "15.197.210.208",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "15.197.206.217",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "3.33.221.48",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "3.33.252.61",
            "ttl": null
          }
        ],
        "engine": "system",
        "failure": null,
        "hostname": "e4.whatsapp.net",
        "query_type": "A",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "",
        "t": 0.290794917
      },
      {
        "answers": [
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "15.197.210.208",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "3.33.221.48",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "3.33.252.61",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "15.197.206.217",
            "ttl": null
          }
        ],
        "engine": "system",
        "failure": null,
        "hostname": "e8.whatsapp.net",
        "query_type": "A",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "",
        "t": 0.301412167
      },
      {
        "answers": [
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "15.197.210.208",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "3.33.221.48",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "3.33.252.61",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "15.197.206.217",
            "ttl": null
          }
        ],
        "engine": "system",
        "failure": null,
        "hostname": "e13.whatsapp.net",
        "query_type": "A",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "",
        "t": 0.309714084
      },
      {
        "answers": [
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "3.33.252.61",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "15.197.210.208",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "3.33.221.48",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "15.197.206.217",
            "ttl": null
          }
        ],
        "engine": "system",
        "failure": null,
        "hostname": "e16.whatsapp.net",
        "query_type": "A",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "",
        "t": 0.321179042
      },
      {
        "answers": [
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "3.33.252.61",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "15.197.206.217",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "3.33.221.48",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "15.197.210.208",
            "ttl": null
          }
        ],
        "engine": "system",
        "failure": null,
        "hostname": "e11.whatsapp.net",
        "query_type": "A",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "",
        "t": 0.327117875
      },
      {
        "answers": [
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "15.197.210.208",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "3.33.252.61",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "15.197.206.217",
            "ttl": null
          },
          {
            "asn": 16509,
            "as_org_name": "Amazon.com, Inc.",
            "answer_type": "A",
            "ipv4": "3.33.221.48",
            "ttl": null
          }
        ],
        "engine": "system",
        "failure": null,
        "hostname": "e15.whatsapp.net",
        "query_type": "A",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "",
        "t": 0.337729667
      },
      {
        "answers": [
          {
            "asn": 32934,
            "as_org_name": "Facebook, Inc.",
            "answer_type": "A",
            "ipv4": "31.13.86.51",
            "ttl": null
          }
        ],
        "engine": "system",
        "failure": null,
        "hostname": "v.whatsapp.net",
        "query_type": "A",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "",
        "t": 0.321002042
      },
      {
        "answers": [
          {
            "asn": 32934,
            "as_org_name": "Facebook, Inc.",
            "answer_type": "AAAA",
            "ipv6": "2a03:2880:f208:c5:face:b00c:0:167",
            "ttl": null
          }
        ],
        "engine": "system",
        "failure": null,
        "hostname": "v.whatsapp.net",
        "query_type": "AAAA",
        "resolver_hostname": null,
        "resolver_port": null,
        "resolver_address": "",
        "t": 0.321002042
      }
    ],
    "requests": [
      {
        "failure": null,
        "request": {
          "body": "",
          "body_is_truncated": false,
          "headers_list": [
            [
              "Accept",
              "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
            ],
            [
              "Accept-Language",
              "en-US,en;q=0.9"
            ],
            [
              "Host",
              "web.whatsapp.com"
            ],
            [
              "User-Agent",
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
            ]
          ],
          "headers": {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
            "Host": "web.whatsapp.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
          },
          "method": "GET",
          "tor": {
            "exit_ip": null,
            "exit_name": null,
            "is_tor": false
          },
          "x_transport": "tcp",
          "url": "https://web.whatsapp.com/"
        },
        "response": {
          "body": "<!DOCTYPE html><html lang=\"en\" id=\"facebook\"><head><title>Error</title><meta charset=\"utf-8\" /><meta http-equiv=\"Cache-Control\" content=\"no-cache\" /><meta name=\"robots\" content=\"noindex,nofollow\" /><style nonce=\"wfWasHre\">html, body { color: #333; font-family: 'Lucida Grande', 'Tahoma', 'Verdana', 'Arial', sans-serif; margin: 0; padding: 0; text-align: center;}\n#header { height: 30px; padding-bottom: 10px; padding-top: 10px; text-align: center;}\n#icon { width: 30px;}\n.core { margin: auto; padding: 1em 0; text-align: left; width: 904px;}\nh1 { font-size: 18px;}\np { font-size: 13px;}\n.footer { border-top: 1px solid #ddd; color: #777; float: left; font-size: 11px; padding: 5px 8px 6px 0; width: 904px;}</style></head><body><div id=\"header\"><a href=\"//www.facebook.com/\"><img id=\"icon\" src=\"//static.facebook.com/images/logos/facebook_2x.png\" /></a></div><div class=\"core\"><h1>Sorry, something went wrong.</h1><p>We&#039;re working on getting this fixed as soon as we can.</p><p><a id=\"back\" href=\"//www.facebook.com/\">Go Back</a></p><div class=\"footer\"> Meta &#169; 2022 &#183; <a href=\"//www.facebook.com/help/?ref=href052\">Help</a></div></div><script nonce=\"wfWasHre\">\n              document.getElementById(\"back\").onclick = function() {\n                if (history.length > 1) {\n                  history.back();\n                  return false;\n                }\n              };\n            </script></body></html><!-- @codegen-command : phps GenerateErrorPages --><!-- @generated SignedSource<<aa30090ace0190809cb1ff902c2ba23b>> -->",
          "body_is_truncated": false,
          "code": 400,
          "headers_list": [
            [
              "Alt-Svc",
              "h3=\":443\"; ma=86400"
            ],
            [
              "Content-Length",
              "1542"
            ],
            [
              "Content-Type",
              "text/html; charset=\"utf-8\""
            ],
            [
              "Cross-Origin-Opener-Policy",
              "unsafe-none"
            ],
            [
              "Date",
              "Wed, 07 Dec 2022 09:52:48 GMT"
            ],
            [
              "Priority",
              "u=3,i"
            ],
            [
              "Strict-Transport-Security",
              "max-age=31536000; preload; includeSubDomains"
            ],
            [
              "Vary",
              "Sec-Fetch-Site, Sec-Fetch-Mode"
            ],
            [
              "Vary",
              "Accept-Encoding"
            ],
            [
              "X-Fb-Debug",
              "S/9ZQqkYmYlncywQTI+5YcnE9XKvk/jd9mllbVKqFePTAlfEotY2wXnj9LTLTElZU5aoXtmYLk6FhcHpsGyn1Q=="
            ],
            [
              "X-Fb-Trip-Id",
              "1679558926"
            ]
          ],
          "headers": {
            "Alt-Svc": "h3=\":443\"; ma=86400",
            "Content-Length": "1542",
            "Content-Type": "text/html; charset=\"utf-8\"",
            "Cross-Origin-Opener-Policy": "unsafe-none",
            "Date": "Wed, 07 Dec 2022 09:52:48 GMT",
            "Priority": "u=3,i",
            "Strict-Transport-Security": "max-age=31536000; preload; includeSubDomains",
            "Vary": "Sec-Fetch-Site, Sec-Fetch-Mode",
            "X-Fb-Debug": "S/9ZQqkYmYlncywQTI+5YcnE9XKvk/jd9mllbVKqFePTAlfEotY2wXnj9LTLTElZU5aoXtmYLk6FhcHpsGyn1Q==",
            "X-Fb-Trip-Id": "1679558926"
          }
        },
        "t": 0.189301417
      },
      {
        "failure": null,
        "request": {
          "body": "",
          "body_is_truncated": false,
          "headers_list": [
            [
              "Accept",
              "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
            ],
            [
              "Accept-Language",
              "en-US,en;q=0.9"
            ],
            [
              "Host",
              "v.whatsapp.net"
            ],
            [
              "User-Agent",
              "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
            ]
          ],
          "headers": {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
            "Host": "v.whatsapp.net",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
          },
          "method": "GET",
          "tor": {
            "exit_ip": null,
            "exit_name": null,
            "is_tor": false
          },
          "x_transport": "tcp",
          "url": "https://v.whatsapp.net/v2/register"
        },
        "response": {
          "body": "{\"param\":\"authkey\",\"reason\":\"missing_param\",\"status\":\"fail\"}\n",
          "body_is_truncated": false,
          "code": 200,
          "headers_list": [
            [
              "Content-Length",
              "61"
            ],
            [
              "Content-Type",
              "text/json ; charset=utf-8"
            ],
            [
              "Date",
              "Wed, 07 Dec 2022 09:52:48 GMT"
            ],
            [
              "Server",
              "Yaws 2.0.9"
            ],
            [
              "X-Fb-Trip-Id",
              "1679558926"
            ]
          ],
          "headers": {
            "Content-Length": "61",
            "Content-Type": "text/json ; charset=utf-8",
            "Date": "Wed, 07 Dec 2022 09:52:48 GMT",
            "Server": "Yaws 2.0.9",
            "X-Fb-Trip-Id": "1679558926"
          }
        },
        "t": 0.477391917
      }
    ],
    "tcp_connect": [
      {
        "ip": "3.33.252.61",
        "port": 443,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.038953792
      },
      {
        "ip": "3.33.252.61",
        "port": 443,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.039018709
      },
      {
        "ip": "3.33.221.48",
        "port": 5222,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.03902025
      },
      {
        "ip": "3.33.252.61",
        "port": 443,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.073610834
      },
      {
        "ip": "15.197.210.208",
        "port": 443,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.075890875
      },
      {
        "ip": "15.197.206.217",
        "port": 443,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.082615
      },
      {
        "ip": "3.33.221.48",
        "port": 443,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.109965334
      },
      {
        "ip": "15.197.210.208",
        "port": 5222,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.111479792
      },
      {
        "ip": "15.197.210.208",
        "port": 443,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.144534042
      },
      {
        "ip": "3.33.221.48",
        "port": 443,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.144595959
      },
      {
        "ip": "15.197.206.217",
        "port": 5222,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.163556292
      },
      {
        "ip": "15.197.210.208",
        "port": 443,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.1809045
      },
      {
        "ip": "3.33.252.61",
        "port": 5222,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.182005834
      },
      {
        "ip": "31.13.86.51",
        "port": 443,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.117675834
      },
      {
        "ip": "3.33.252.61",
        "port": 5222,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.200444875
      },
      {
        "ip": "15.197.206.217",
        "port": 5222,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.215879542
      },
      {
        "ip": "3.33.221.48",
        "port": 443,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.227087375
      },
      {
        "ip": "3.33.221.48",
        "port": 5222,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.227118875
      },
      {
        "ip": "3.33.221.48",
        "port": 5222,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.247043084
      },
      {
        "ip": "15.197.210.208",
        "port": 443,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.250968459
      },
      {
        "ip": "15.197.210.208",
        "port": 5222,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.266117875
      },
      {
        "ip": "3.33.252.61",
        "port": 5222,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.266169084
      },
      {
        "ip": "15.197.206.217",
        "port": 443,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.283247042
      },
      {
        "ip": "3.33.221.48",
        "port": 443,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.284150625
      },
      {
        "ip": "3.33.221.48",
        "port": 5222,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.289730209
      },
      {
        "ip": "3.33.221.48",
        "port": 443,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.29997075
      },
      {
        "ip": "3.33.221.48",
        "port": 5222,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.300009084
      },
      {
        "ip": "15.197.210.208",
        "port": 5222,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.30852475
      },
      {
        "ip": "15.197.210.208",
        "port": 5222,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.318773292
      },
      {
        "ip": "15.197.210.208",
        "port": 443,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.326225
      },
      {
        "ip": "3.33.252.61",
        "port": 443,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.336746667
      },
      {
        "ip": "3.33.252.61",
        "port": 5222,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.342397167
      },
      {
        "ip": "15.197.210.208",
        "port": 5222,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.352054625
      },
      {
        "ip": "31.13.86.51",
        "port": 443,
        "status": {
          "failure": null,
          "success": true
        },
        "t": 0.335926709
      }
    ],
    "tls_handshakes": [
      {
        "network": "",
        "address": "31.13.86.51:443",
        "cipher_suite": "TLS_AES_128_GCM_SHA256",
        "failure": null,
        "negotiated_protocol": "h2",
        "no_tls_verify": false,
        "peer_certificates": [
          {
            "data": "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",
            "format": "base64"
          },
          {
            "data": "MIIEsTCCA5mgAwIBAgIQBOHnpNxc8vNtwCtCuF0VnzANBgkqhkiG9w0BAQsFADBsMQswCQYDVQQGEwJVUzEVMBMGA1UEChMMRGlnaUNlcnQgSW5jMRkwFwYDVQQLExB3d3cuZGlnaWNlcnQuY29tMSswKQYDVQQDEyJEaWdpQ2VydCBIaWdoIEFzc3VyYW5jZSBFViBSb290IENBMB4XDTEzMTAyMjEyMDAwMFoXDTI4MTAyMjEyMDAwMFowcDELMAkGA1UEBhMCVVMxFTATBgNVBAoTDERpZ2lDZXJ0IEluYzEZMBcGA1UECxMQd3d3LmRpZ2ljZXJ0LmNvbTEvMC0GA1UEAxMmRGlnaUNlcnQgU0hBMiBIaWdoIEFzc3VyYW5jZSBTZXJ2ZXIgQ0EwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQC24C/CJAbIbQRf1+8KZAayfSImZRauQkCbztyfn3YHPsMwVYcZuU+UDlqUH1VWtMICKq/QmO4LQNfE0DtyyBSe75CxEamu0si4QzrZCwvV1ZX1QK/IHe1NnF9Xt4ZQaJn1itrSxwUfqJfJ3KSxgoQtxq2lnMcZgqaFD15EWCo3j/018QsIJzJa9buLnqS9UdAn4t07QjOjBSjEuyjMmqwrIw14xnvmXnG3Sj4I+4G3FhahnSMSTeXXkgisdaScus0Xsh5ENWV/UyU50RwKmmMbGZJ0aAo3wsJSSMs5WqK24V3B3aAguCGikyZvFEohQcftbZvySC/zA/WiaJJTL17jAgMBAAGjggFJMIIBRTASBgNVHRMBAf8ECDAGAQH/AgEAMA4GA1UdDwEB/wQEAwIBhjAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwNAYIKwYBBQUHAQEEKDAmMCQGCCsGAQUFBzABhhhodHRwOi8vb2NzcC5kaWdpY2VydC5jb20wSwYDVR0fBEQwQjBAoD6gPIY6aHR0cDovL2NybDQuZGlnaWNlcnQuY29tL0RpZ2lDZXJ0SGlnaEFzc3VyYW5jZUVWUm9vdENBLmNybDA9BgNVHSAENjA0MDIGBFUdIAAwKjAoBggrBgEFBQcCARYcaHR0cHM6Ly93d3cuZGlnaWNlcnQuY29tL0NQUzAdBgNVHQ4EFgQUUWj/kK8CB3U8zNllZGKiErhZcjswHwYDVR0jBBgwFoAUsT7DaQP4v0cB1JgmGggC72NkK8MwDQYJKoZIhvcNAQELBQADggEBABiKlYkD5m3fXPwdaOpKj4PWUS+Na0QWnqxj9dJubISZi6qBcYRb7TROsLd5kinMLYBq8I4g4Xmk/gNHE+r1hspZcX30BJZr01lYPf7TMSVcGDiEo+afgv2MW5gxTs14nhr9hctJqvIni5ly/D6q1UEL2tU2ob8cbkdJf17ZSHwD2f2LSaCYJkJA69aSEaRkCldUxPUd1gJea6zuxICaEnL6VpPX/78whQYwvwt/Tv9XBZ0k7YXDK/umdaisLRbvfXknsuvCnQsH6qqF0wGjIChBWUMo0oHjqvbsezt3tkBigAVBRQHvFwY+3sAzm2fTYS5yh+Rp/BIAV0AecPUeybQ=",
            "format": "base64"
          }
        ],
        "server_name": "web.whatsapp.com",
        "t": 0.13597625,
        "tags": null,
        "tls_version": "TLSv1.3"
      },
      {
        "network": "",
        "address": "31.13.86.51:443",
        "cipher_suite": "TLS_AES_128_GCM_SHA256",
        "failure": null,
        "negotiated_protocol": "h2",
        "no_tls_verify": false,
        "peer_certificates": [
          {
            "data": "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",
            "format": "base64"
          },
          {
            "data": "MIIEsTCCA5mgAwIBAgIQBOHnpNxc8vNtwCtCuF0VnzANBgkqhkiG9w0BAQsFADBsMQswCQYDVQQGEwJVUzEVMBMGA1UEChMMRGlnaUNlcnQgSW5jMRkwFwYDVQQLExB3d3cuZGlnaWNlcnQuY29tMSswKQYDVQQDEyJEaWdpQ2VydCBIaWdoIEFzc3VyYW5jZSBFViBSb290IENBMB4XDTEzMTAyMjEyMDAwMFoXDTI4MTAyMjEyMDAwMFowcDELMAkGA1UEBhMCVVMxFTATBgNVBAoTDERpZ2lDZXJ0IEluYzEZMBcGA1UECxMQd3d3LmRpZ2ljZXJ0LmNvbTEvMC0GA1UEAxMmRGlnaUNlcnQgU0hBMiBIaWdoIEFzc3VyYW5jZSBTZXJ2ZXIgQ0EwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQC24C/CJAbIbQRf1+8KZAayfSImZRauQkCbztyfn3YHPsMwVYcZuU+UDlqUH1VWtMICKq/QmO4LQNfE0DtyyBSe75CxEamu0si4QzrZCwvV1ZX1QK/IHe1NnF9Xt4ZQaJn1itrSxwUfqJfJ3KSxgoQtxq2lnMcZgqaFD15EWCo3j/018QsIJzJa9buLnqS9UdAn4t07QjOjBSjEuyjMmqwrIw14xnvmXnG3Sj4I+4G3FhahnSMSTeXXkgisdaScus0Xsh5ENWV/UyU50RwKmmMbGZJ0aAo3wsJSSMs5WqK24V3B3aAguCGikyZvFEohQcftbZvySC/zA/WiaJJTL17jAgMBAAGjggFJMIIBRTASBgNVHRMBAf8ECDAGAQH/AgEAMA4GA1UdDwEB/wQEAwIBhjAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwNAYIKwYBBQUHAQEEKDAmMCQGCCsGAQUFBzABhhhodHRwOi8vb2NzcC5kaWdpY2VydC5jb20wSwYDVR0fBEQwQjBAoD6gPIY6aHR0cDovL2NybDQuZGlnaWNlcnQuY29tL0RpZ2lDZXJ0SGlnaEFzc3VyYW5jZUVWUm9vdENBLmNybDA9BgNVHSAENjA0MDIGBFUdIAAwKjAoBggrBgEFBQcCARYcaHR0cHM6Ly93d3cuZGlnaWNlcnQuY29tL0NQUzAdBgNVHQ4EFgQUUWj/kK8CB3U8zNllZGKiErhZcjswHwYDVR0jBBgwFoAUsT7DaQP4v0cB1JgmGggC72NkK8MwDQYJKoZIhvcNAQELBQADggEBABiKlYkD5m3fXPwdaOpKj4PWUS+Na0QWnqxj9dJubISZi6qBcYRb7TROsLd5kinMLYBq8I4g4Xmk/gNHE+r1hspZcX30BJZr01lYPf7TMSVcGDiEo+afgv2MW5gxTs14nhr9hctJqvIni5ly/D6q1UEL2tU2ob8cbkdJf17ZSHwD2f2LSaCYJkJA69aSEaRkCldUxPUd1gJea6zuxICaEnL6VpPX/78whQYwvwt/Tv9XBZ0k7YXDK/umdaisLRbvfXknsuvCnQsH6qqF0wGjIChBWUMo0oHjqvbsezt3tkBigAVBRQHvFwY+3sAzm2fTYS5yh+Rp/BIAV0AecPUeybQ=",
            "format": "base64"
          }
        ],
        "server_name": "v.whatsapp.net",
        "t": 0.354731125,
        "tags": null,
        "tls_version": "TLSv1.3"
      }
    ],
    "registration_server_failure": null,
    "registration_server_status": "ok",
    "whatsapp_endpoints_blocked": [],
    "whatsapp_endpoints_dns_inconsistent": [],
    "whatsapp_endpoints_status": "ok",
    "whatsapp_web_failure": null,
    "whatsapp_web_status": "ok"
  },
  "test_name": "whatsapp",
  "test_runtime": 0.478158125,
  "test_start_time": "2022-12-07 09:52:47",
  "test_version": "0.10.0"
}
```

## History

Since 2020-02-17, the heristics for checking whether a netblock belongs to
WhatsApp as described in version 2016-10-25-001 of this specification is
fundamentally broken (see [ooni/probe-engine#341](
https://github.com/ooni/probe-engine/issues/341)). This issue affected
ooni/probe-legacy <= 2.3.0, ooni/probe-ios <= 2.2.0, ooni/probe-android
<= 2.2.0. The `test_version` was 0.6.0 for ooni/probe-legacy and 0.6.1
for the mobile apps. Since Measurement Kit 0.10.10 (`test_version`
0.7.0) we will completely disable such check. Since 2020-07-09 the spec
does not mention anymore the CIDR check.

Since 2022-12-07, we don't check `http://web.whatsapp.com`, for
reasons explained more in detail above.

# Specification version number

2023-10-17-000

* _status_: current

# Specification name

RiseupVPN

# Test preconditions

* An internet connection with functional DNS

# Expected impact

The ability to detect both if the RiseupVPN API and its gateways can be reached and connected to.

# Expected inputs

## Import document or import data format

None. We aim to allow the user to specify a provider in a future version, the default is riseup.net.

# Test description

This test will check if a LEAP-platform-based VPN service like RiseupVPN is working as exepected. The experiment consists of two parts.

1. The RiseupVPN API service

2. The advertised gateways (the VPN servers used by RiseupVPN clients)

## RiseupVPN API check

A HTTP GET request to an API endpoint will hand out the self-signed certificate needed to access most other API endpoints. While RiseupVPN clients will perform a fingerprint verification, this test skips that step in order to reduce the complexity.

The RiseupVPN provider serves a JSON describing which endpoints a client could use (https://example.org/provider.json) for bootstrapping. However, for the sake of simplicity we hardcoded all endpoints that will be tested.

Using the self signed certificate, we perform a HTTP GET requests to test the reachability of the provider API endpoints. The API check implies a working DNS.

The locations of RiseupVPNs endpoints are:

* `https://black.riseup.net/ca.crt` fetched with a GET request, contains the self-signed X.509 certificate used in all subsequent requests.

* `https://riseup.net/provider.json` fetched with a GET request.

* `https://api.black.riseup.net:443/3/config/eip-service.json` fetched with GET request, contains gateway addresses, available transports, location, ports, etc. We use version 3 here.

* `https://api.black.riseup.net:9001/json` (hereafter referred to as geo service) contains the the client's IP address, geolocation and gives a list of gateways that's the closest and/or under less stress (from other users). This can be different and change.

Since ooniprobe 3.19.0 and version 0.3.0 of the riseupvpn experiment, any failure in accessing any of the above services as well as any failure in using the self-signed X.509 certificate causes the experiment to stop early, without measuring gateways.

Before ooniprobe 3.19.0, the data format was different as documented by [a previous version of this document](https://github.com/ooni/spec/blob/f9bbaa83541484e3e509ffa56dd87b0c5ce8c31a/nettests/ts-026-riseupvpn.md).

Since ooniprobe 3.19.0, if all parts of the API are functional and reachable then we write:

```JSON
{
    "api_failures": null,
    "ca_cert_status": true,
}
```

In case any API fails, we include its error into the `api_failures` string list, as follows:

```JSON
{
    "api_failures": ["failure1", "failure2"],
    "ca_cert_status": true,
}
```

The `ca_cert_status` boolean flag is set to false if we cannot get the self-signed X.509 certificate or the returned bytes are not a valid PEM-encoded certificate.

## RiseupVPN gateways test

If the provider API is reachable, it provides a JSON-file which contains the IP addresses and capabilites of the VPN gateways.
The reachability of gateways will be tested depending on their capabilities as described by the provider (ports, OpenVPN, obfs4) by performing TCP handshakes. If a TCP handshake fails we assume the corresponding port and transport of that gateway to be blocked.

Before ooniprobe 3.19.0, the data format was different as documented by [a previous version of this document](https://github.com/ooni/spec/blob/f9bbaa83541484e3e509ffa56dd87b0c5ce8c31a/nettests/ts-026-riseupvpn.md).

Since ooniprobe 3.19.0, we do not write any toplevel key associated with riseupvpn gateways.

# Expected output

## Parent data format

* `df-001-httpt`
* `df-002-dnst`
* `df-005-tcpconnect`
* `df-006-tlshandshake`
* `df-009-tunnel`

## Required output data

JSON fields described above.

## Semantics

```
{
    "api_failures": ["FAILURE STRING"] | null,
    "ca_cert_status": true | false,
}
```

`api_failure` can be any error string flagged with `(PE)` defined in `df-007-errors` or:

* `invalid_ca` in case the fetched ca certificate is invalid
* `invalid_eipservice_response` in case the fetched eip-service.json is invalid
* `invalid_geoservice_response` in case the fetched geo service response is invalid

## Possible conclusions

* Users will be able to fetch client certificates and use the RiseupVPN services.

## Example output sample

## Expected Post-processing efforts

The providers will be able to learn if, where and which gateways are blocked. Depending on that, they might move or open up new VPN gateways in other locations.

# Privacy considerations

A network observer will learn that these servers exist and see that you are connecting to some IP addresses.

# Status and future directions

This test is currently experimental and will be used to further understand the design space. The idea is to broaden this test, besides Riseup, there is for example the Calyx Institute which offers a service based on the same software.

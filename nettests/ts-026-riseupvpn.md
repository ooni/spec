# Specification version number

2020-10-13-000

# Specification name

RiseupVPN

# Test preconditions

* An internet connection with functional DNS

# Expected impact

The ability to detect both if the RiseupVPN API and its gateways can be reached and connected to.

# Expected inputs

## Import document or import data format

None. In the next iteration we will allow the user to specify a provider, the default is riseup.net.

# Test description

This test will check if a LEAP platform based VPN service like RiseupVPN is working as exepected. The experiment consists of two parts.

1. The RiseupVPN API service

2. The advertised gateways (the VPN servers used by RiseupVPN clients)

## RiseupVPN API check

A HTTP GET request to an API endpoint will hand out the self-signed certificate needed to access most other API endpoints. While RiseupVPN clients will perform a fingerprint verification, this test skips that step in order to reduce the complexity.

The RiseupVPN provider serves a JSON describing which endpoints a client could use (https://example.org/provider.json) for bootstrapping. However, for the sake of simplicity we hardcoded all endpoints that will be tested.

Using the self signed certificate, we perform a HTTP GET requests to test the reachability of the provider API endpoints. The API check implies a working DNS.

The locations of RiseupVPNs endpoints are:

* https://black.riseup.net/ca.crt fetched with a GET request, contains the self-signed x509 certificate used in all subsequent requests.

* https://riseup.net/provider.json fetched with a GET request.

* https://api.black.riseup.net:443/3/config/eip-service.json fetched with GET request, contains gateway addresses, available transports, location, ports, etc.). Versions is 3 here.

* https://api.black.riseup.net:9001/json contains the the client's IP address, geolocation and gives a list of gateways that's the closest and/or under less stress (from other users). This can be different and change.

We consider RiseupVPN API to be blocked when we can't fetch a valid self-signed x509 certificate or we don't get a valid HTTP response. If fetching a valid certificate failed, the experiment will skip all subsequent tests.

Example output if API endpoints couldn't be reached by HTTP GET requests

```json
{
    "api_failure": "FAILURE STRING",
    "api_status": "blocked",
    "ca_cert_status": true,
}
```

If all parts of the API are functional and reachable then we write:

```json
{
    "api_failure": null,
    "api_status": "ok",
    "ca_cert_status": true,
}
```

## RiseupVPN gateways test

If the provider API is reachable, it provides a JSON-file which contains the IP addresses and capabilites of the VPN gateways. The reachability of gateways will be tested depending on their capabilities as described by the provider (ports, OpenVPN, obfs4) by performing TCP handshakes. If a TCP handshake fails we can assume the corresponding port and transport of that gateway to be blocked.

Example output for reported blocked gateways:

```json
{
   "failing_gateways":[
         {
            "ip":"192.0.2.1",
            "port":443,
            "transport_type":"openvpn"
         },
         {
            "ip":"192.0.2.1",
            "port":23042,
            "transport_type":"obfs4"
         }
    ]
}
```

If none of the gateways are blocked then we write:

```json
{
    "failing_gateways": null
}
```

If for whatever reason 1 or more of their gatewayservers is overloaded, suffers a network outage or isn't reachable for other reasons, then the status will still say it's blocked.

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
    "api_failure": "FAILURE STRING" | null,
    "api_status": "blocked"| "ok",
    "ca_cert_status": true | false,
    "failing_gateways": [
         {
            "ip":"IP ADDRESS STRING",
            "port": 0-65535,
            "transport_type":"openvpn" | "obfs4"
         },
    ] | null
}
```

`api_failure` can be any error string flagged with `(PE)` defined in `df-007-errors` or `invalid_ca` in case fetching a valid ca certificate failed.

## Possible conclusions

* Users will be able to fetch client certificates and use the RiseupVPN services.

## Example output sample

## Expected Post-processing efforts

The providers will be able to learn if, where and which gateways are blocked. Depending on that, they might move or open up new VPN gateways in other locations.

# Privacy considerations

A network observer will learn that these servers exist and see that you try to use OpenVPN.

# Status and future directions

This test is currently experimental and will be used to further understand the design space. The idea is to broaden this test, besides Riseup, there is for example the Calyx Institute which offers a service based on the same software.

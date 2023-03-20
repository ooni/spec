# Specification version number

2023-03-20-000

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

* https://api.black.riseup.net:443/3/config/eip-service.json fetched with GET request, contains gateway addresses, available transports, location, ports, etc.. Versions is 3 here.

* https://api.black.riseup.net:9001/json (hereafter referred to as geo service) contains the the client's IP address, geolocation and gives a list of gateways that's the closest and/or under less stress (from other users). This can be different and change.

We consider RiseupVPN API to be blocked when we can't fetch the main configuration json eip-service.json.
The failure of other API endpoints will be reported in the tests, but might related to server sided misbehavior and therefore cannot be used as an indicator for a blocked API.
If fetching a valid certificate failed, the experiment continues without TLS verification. If the API was not reachable, a tunnel through Tor and Snowflake is attempted. That circumvention strategy simulates the actual behavior of RiseupVPNs clients. If the API is still unreachable via Tor and Snowflake, the subsequent gateway tests are skipped because the required configuration data to reach them is missing.

Example output if API endpoints couldn't be reached by HTTP GET requests

```json
{
    "api_failure": ["FAILURE STRING"],
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

If the provider API is reachable, it provides a JSON-file which contains the IP addresses and capabilites of the VPN gateways. A subset of max. three gateways will be tested: gateways that are not overloaded (deduced from the geo service) and which are part of the top two locations having most redundancy regarding obfs4 bridges.
The reachability of gateways will be tested depending on their capabilities as described by the provider (ports, OpenVPN, obfs4) by performing TCP handshakes. If a TCP handshake fails we assume the corresponding port and transport of that gateway to be blocked and add it to the list of failing gateways.
We consider a transport to be accessible if it was possible to connect at least to one gateway port providing that transport.

Example output for reported blocked gateways:

```json
{
    "transport_status":{
        "obfs4":"blocked",
        "openvpn":"ok"
    },
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
    "transport_status":{
        "obfs4": "ok",
        "openvpn":"ok"
    },
    "failing_gateways": null
}
```

If for whatever reason one or more gateway servers suffer a network outage or aren't reachable for other reasons, then the corresponding gateway statuses will be still shown as blocked. In order to avoid these false positives the **transport_status should be considered as the main indicator for successful censorship attempts of the VPN**.

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
    "api_failure": ["FAILURE STRING"] | null,
    "api_status": "blocked"| "ok",
    "ca_cert_status": true | false,
    "transport_status":{
        "obfs4": "ok" | "blocked",
        "openvpn":"ok" | "blocked"
    },
    "failing_gateways": [
         {
            "ip":"IP ADDRESS STRING",
            "port": 0-65535,
            "transport_type":"openvpn" | "obfs4"
         },
    ] | null
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

A network observer will learn that these servers exist and see that you try to use OpenVPN.

# Status and future directions

This test is currently experimental and will be used to further understand the design space. The idea is to broaden this test, besides Riseup, there is for example the Calyx Institute which offers a service based on the same software.

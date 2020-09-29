# Specification version number

2020-09-14-000

# Specification name

RiseupVPN

# Test preconditions

* An internet connection with functional DNS
* When testing the connection to a riseupvpn gateway, we assume that OpenVPN is already installed

# Expected impact

The ability to detect both if the (RiseupVPN) API of the provider and its gateways can be reached and connected to. TCP-connection and HTTP GET request provide a JSON-file which contains the IP addresses of the VPN gateways. A second request to the API will hand out the CA-material to verify the gateways. Different transports will be tested, depending on their capabilities as described by the provider (TCP, UDP, ports, OpenVPN, obfs4,...).

# Expected inputs

## Import document or import data format
None. In a next iteration you can specify a provider, the default is riseup.net

## Semantics

DO WE WANT THIS, DO WE WANT THIS NOW, LIKE THIS? FORMAT REQUIRES IMPROVEMENT
* A provider can be specified with their domain name: https://calyx.net
* A specific gateway and transport can be tested with a url: ovpn://192.168.1.1:1194

# Test description

This test will check if a VPN service like RiseupVPN is working as exepected. If the first fails, we can't execute the second. When the probe has OpenVPN installed, we can execute the second test, otherwise we only do the first.

1. The RiseupVPN API service
1. The advertised gateways (the VPN servers used by RiseupVPN clients)

## RiseupVPN API check

The RiseupVPN provider serves a JSON describing which servers a client could use (https://example.org/provider.json). When parsing, we learn where their CA-certificate is stored. The locations of the VPN gateway servers are also described. At last we will request a client certificate, enabling us to proceed to the next tests. This all implies a working DNS.

The locations are:

* https://riseup.net/provider.json fetched with a GET request
* https://api.black.riseup.net:443/3/config/eip-service.json fetched with GET request, contains gateway addresses, available transports, location, ports, etc.). Versions is 3 here.
* https://api.black.riseup.net:9001/json contains the the client's IP address, geolocation and gives a list of gateways that's the closest and/or under less stress (from other users). This can be different and change.
* https://api.black.riseup.net/3/cert for fetching an OpenVPN client certificate

We consider RiseupVPN API to be blocked when we can't make TCP connections. `RiseupVPNApiWebFailure` and `RiseupVPNApiWebStatus` are used in the reports. FIXME: WHAT ARE THEIR VALUES? CAN WE WRITE riseupvpn_api_status, leave out Web, let the CameLs free?

```json
{
    "riseupvpn_api_failure": "FAILURE STRING",
    "riseupvpn_api_status": "blocked"
}
```

If all parts of the API are functional and reachable then we write:

```json
{
    "riseupvpn_api_failure": null,
    "riseupvpn_api_status": "ok"
}
```

## RiseupVPN gateways test

When OpenVPN is installed, we can verify if a connection to these gateways is possible. If they can't be reached or we don't get the expected results we can presume them to be blocked. However, without OpenVPN installed, we don't run this test. We test by using the client certificate fetched in the API check.

If any one of the OpenVPN gateways are blocked then we presume them to blocked and write in the report: FIXME: DO WE WRITE WHICH GATEWAYS ARE BLOCKED? HOW?

```json
{
    "riseupvpn_gateway_failure": "FAILURE STRING",
    "riseupvpn_gateway_status": "blocked"
}
```

If none of the gateways are blocked then we write:

```json
{
    "riseupvpn_gateway_failure": null,
    "riseupvpn_gateway_status": "ok"
}
```

If for whatever reason 1 or more of their gatewayservers is overloaded, suffers a network outage or isn't reachable for other reasons, then the status will still say it's blocked.

# Expected output

## Parent data format
FIXME: I'M MISSING SOME STUFF :(

* `df-001-httpt`
* `df-002-dnst` (since 2020-01-09 in ooni/probe-engine)
* `df-005-tcpconnect`
* `df-006-tlshandshake` (since 2020-01-11 in ooni/probe-engine)

## Required output data

FIXME: sorry, don't know yet what to write here. 

## Semantics

```
{
    "riseupvpn_api_failure": "FAILURE STRING" | null,
    "riseupvpn_api_status": "blocked"| "ok",

    "riseupvpn_gateway_failure": "FAILURE STRING" | null,
    "riseupvpn_gateway_status": "blocked" | "ok" | null,
}
```

## Possible conclusions

* Users will be able to fetch client certificates and use the RiseupVPN services.

## Example output sample

## Expected Post-processing efforts

The providers will be able to learn if, where and which gateways are blocked. Depending on that, they might move or open up new VPN gateways in other locations.

# Privacy considerations

A network observer will learn that these sesrvers exist and see that you try to use OpenVPN.

# Other notes

The idea is to broaden this test, besides Riseup, there is for example the Calyx Institute which offers the same kind of service.




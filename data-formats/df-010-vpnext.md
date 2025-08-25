# External VPN Report Data Format

This document describes the `test_keys` that experiments
SHOULD use when they contain measurements reported by an external VPN application.

These are special measurements that are not obtained by OONI Probes; instead, they contain external information about network failures -or absence thereof- reported by heterogeneous sources.

The rationale is that VPN applications can opt-in to report failed connection
attempts to the OONI backend. VPN providers, alternatively, can also aggregate
failure rate data and submit aggregated reports to the OONI Collector.

| Name    | `vpnext` |
|---------|----------|
| Version | 0        |


## Specification

We try to keep the semantics for the keys in this specification compatible
with the ones defined within the [Network Error Logging (W3C Editor's
Draft)](https://w3c.github.io/network-error-logging/).

However, we adapt the specification for OONI's purposes.

Instead of a fixed `network-error` type, we expect the measurement to contain
one of the following types. They are obtained by prepending either `api` or
`vpn` to the basic report type.

- `api-ok`: Report for a successful connection while contacting the VPN Provider's API.

- `api-network-error`: Report for errors observed while contacting the provider's backend during a bootstrap phase (authentication, getting available gateways,
  fetching authentication tokens).

- `vpn-ok`: Report for a successful tunnel establishment.

- `vpn-network-error`: Report for errors registered while establishing the tunnel
  (handshake, failure to obtain a working tunnel usage). The semantics vary
  according to the VPN protocol in use.

### API Network Errors

The former follows more closely a subset of the NEL standard proposal, since
it's describing an HTTP request.

```JSON
{
  "type": "api-network-error",
  "url": "https://api.vpn-provider.org/v1/gateways",
  "provider": "unknown",
  "body": {
	"sampling_fraction": 1.0,
	"server_ip": "",
	"server_asn": "",
	"client_asn": "",
	"protocol": "h2",
	"method": "GET",
	"status_code": 0,
	"elapsed_time": 143,
	"phase": "dns",
	"type": "dns.name_not_resolved"
  }
}
```

- `type` (`string`): Type of error being reported. `api-network-error` in this case.

- `url` (`string`): The URL the client application was attempting to reach.

- `provider` (`string`): A normalized label for the VPN provider, according to a list known to OONI. If the provider cannot be identified, replace it by `unknown`.

- `body` (`object`): The body of the report. Contains the following fields:

	- `sampling_fraction` (`float`): The [sampling rate](https://w3c.github.io/network-error-logging/#dfn-sampling-rate) in use, as announced by the equivalent NEL policy that generated the report.

   - `server_ip` (`string`; optional, `nullable`): The IP address for the server client was trying to reach - if previously known, or if DNS resolution returned one.

   - `server_asn` (`string`; optional): The AS number for the server target of the request.

   - `client_asn` (`string`; optional): If known, AS number for the origin of the request.

   - `protocol` (`string`; optional): The [network protocol](https://www.w3.org/TR/resource-timing/#dom-performanceresourcetiming-nexthopprotocol) used to fetch the resource as identified by the ALPN Protocol ID, if available.

   - `method` (`string`): Request's [method](https://httpwg.org/specs/rfc7231.html#section-4).

   - `status_code` (`int`): The status code of the HTTP Response, if available. Otherwise, `0`.

   - `elapsed_time` (`int`; optional): The elapsed number of milliseconds between the start of the resource fetch and when it was completed or aborted by the user agent.

   - `phase`: (`string`): If request failed, the phase of its network error. If request succeeded, "application".
   - `type`: If request failed, the type of its network error. If request succeeded, "ok".


#### Example

In the following example we've omitted all the keys that are not relevant to the vpn report data format:

```JSON
{
  "type": "api-network-error",
  "url": "https://api.vpn-provider.org/v1/gateways",
  "provider": "unknown",
  "body": {
	"sampling_fraction": 1.0,
	"server_ip": "2.2.0.0",
	"server_asn": "9876",
	"client_asn": "1010",
	"protocol": "h2",
	"method": "GET",
	"status_code": 0,
	"elapsed_time": 143,
	"phase": "dns",
	"type": "dns.name_not_resolved"
  }
}
```

### VPN Network Errors

This category of errors departs from the NEL Draft, since reports refer to protocols other than HTTP.

```JSON
{
  "type": "vpn-network-error",
  "url": "vpn://unknown.openvpn/addr=1.2.1.2"
  "provider": "unknown",
  "body": {
	"sampling_fraction": 1.0,
	"server_ip": "1.2.1.2",
	"server_asn": "9876",
	"client_asn": "1010",
	"protocol": "openvpn",
	"obfuscation": "none",
	"elapsed_time": 143,
	"phase": "dns",
	"type": "dns.name_not_resolved"
  }
}
```

The keys that differ from the `API` report in the previous section are:

- `url` (`string`): Follows the specification in the `openvpn` and `wireguard`
  nettests --- TODO(ainghazal): add links to spec when merged.
- `protocol` (`string`): One of `openvpn`, `wireguard`, `outline`...
- `obfuscation` (`string`): Follows the `openvpn` and `wireguard` specs. Valid
  values are: `obfs4`, `ss`, `wg+tls`, ...
- `phase` (`string`): Depending on the tunnel protocol, it can be: `dns`,
  `handshake`, `tunnel check`.


### Aggregated reports

VPN Providers of all sizes are welcome to report known failure or success
rates. For that, providers MUST set their own infrastructure as the recipient
of the NEL reports, and periodically submit aggregated reports to the OONI
Collector.

Daily submission is preferred for standardization.

The server then submits an array with aggregation of individual `body` reports,
per target and source `ASN`, and divided by protocol and obfuscation type.

```JSON
{
  "type": "vpn-network-error",
  "url": "vpn://cool-provider.wireguard/addr=1.2.1.2"
  "provider": "cool-provider",
  "from": "2023-01-01 00:00:00",
  "to": "2023-01-01 23:59:59",
  "bodies": [
  {
	"failure_ratio": 0.90,
	"sampling_size": 1e6,
	"failure_sampling_fraction": 1.0,
	"success_sampling_fraction": 1.0,
	"server_asn": "9000",
	"client_asn": "1010",
	"protocol": "openvpn",
	"obfuscation": "none",
	"phase": "handshake",
  },
  {
	"failure_ratio": 0.50,
	"sampling_size": 1e4,
	"failure_sampling_fraction": 1.0,
	"succes_sampling_fraction": 0.1,
	"server_asn": "7000",
	"client_asn": "1010",
	"protocol": "openvpn",
	"obfuscation": "none",
	"phase": "handshake",
  }]
}
```

- `from` (`string`): The beginning timestamp of the aggregated sampling period.
- `to` (`string`): The end timestamp of the aggregated sampling period.
- `bodies`: An array of objects of the type `body` described above.
- `failure_ratio` (`float`): Aggregated failure ratio for all the clients from
  the same ASN, reaching the same target ASN via same protocol + obfuscation -
  broken out by tunnel stage, during the observation period.
- `sampling_size (`int`): An approximation (by the nearest power of 10,
  rounding up) of the sampling size used to compute the aggregation.
- `failure_sampling_fraction` (`float`): The sampling fraction for the failure
  rate set in the NEL policy during the sampling period.
- `success_sampling_fraction (`float`)`: The sampling fraction for the success
  rate set in the NEL policy during the sampling period.


## Privacy considerations

When error data is collected and OONI is the direct (via NEL policy) or
indirect (via server aggregation) recipient of these reports, user MUST be
asked for informed consent, and able to opt-out at any time.

At any time, efforts will be made to provide enough anonymization of the
reported data, taking into account the estimated anonymity set.

## Threat model

Setting OONI as the recipient of the NEL reports via the `report-to` header is feasible for HTTP-based requests. This, in principle, has the advantage that each provider has to maintain one less piece of infrastructure that can be blocked by the censor.

Care should be taken so that no direct connections are made to the collector in
highly sensitive contexts, to avoid traffic analysis via observation of
connection patterns to the collector. It is assumed that the reports are
delivered via the use of a successful tunnel strategy, or stored and sent from
a different network. Maximum retention period in the NEL policy should be
adjusted accordingly.

It should also be assumed that a censor can potentially use public aggregated data to try to enumerate endpoints in the provider system. While this can be done by other means, active measures should be employed to limit this possibility.

One trivial countermeasure is to drop the `server_ip` key, and use just the `server_asn` instead. `server_ip` can also zero the less significant octets.

If this is a stronger concern, providers are encouraged to apply some sort of filtering heuristic about the canonical subset of endpoints that are covered by the aggregated reports. Further additions to the specification should take this partial reporting into account. 

## Security considerations

In principle, none of the reports can be trusted in an absolute way. Reported
measurements, and any trend or event detection derived, should be compared
against other data sources.

When talking about aggregated measurements, and to defend against injection
of bogus measuremerents, we should consider a future extension to the data
format described here that allows to cryptographically sign the report contents.

## Implementation considerations

Implementors of NEL policies are encouraged to set a very low value for the
sampling rate of the success fraction for networks and/or countries where the
likelihood of censorship is low.

This specification only describes the format for the OONI measurement, which is
expected to be received at the standard OONI Collector. It should be
more or less straightforward to implement a NEL Collector that can receive NEL-compatible
reports and forward them to the OONI Collector.

## References

- [Sampling rates](https://w3c.github.io/network-error-logging/#sampling-rates)
- [Error types](https://w3c.github.io/network-error-logging/#predefined-network-error-types)
- [Example NEL Collector implementation](https://github.com/google/nel-collector) (archived since Dec 29, 2022).
- [User considerations for private measurement](https://gitlab.com/pitg/private-measurement-user-considerations/-/blob/main/private-measurement-user-considerations.md#trust-model)

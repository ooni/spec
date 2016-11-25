# Specification version number

2016-10-25-001

# Specification name

Facebook Messenger

# Test preconditions

* An internet connection

# Expected impact

Ability to detect if the Facebook Messenger instant messaging platform is
working, by checking if the DNS resolutions are consistent and if it's possible
to establish a TCP session with the IPs of the endpoints.

# Expected inputs

None

# Test description

This test verifies if the following Facebook Messenger endpoints resolve to
consistent IPs and if it's possible to establish TCP connection to them on port
443:

* stun.fbsbx.com (stun)

* b-api.facebook.com (b-api)

* b-graph.facebook.com (b-graph)

* edge-mqtt.facebook.com (edge)

* external.xx.fbcdn.net (external-cdn)

* scontent.xx.fbcdn.net (scontent-cdn)

* star.c10r.facebook.com (star)

In parens is the identifier used inside of the report file to identify that
particular endpoint.

For each endpoint we do an A lookup for the domain name in question and
consider it to be consistent if the IP is inside of a netblock linked to the
facebook Authonomous System Number (AS32934).

When we find a certain endpoint presents an inconsistent DNS we write the following in
the report file:

```json
{
    "facebook-$ENDPOINT_NAME-dns-consistent": false,
    "facebook-dns-blocking": true
}
```

Where `$ENDPOINT_NAME` is one of `stun`, `b-api`, `b-graph`, `edge`,
`external-cdn`, `scontent-cdn`, `star`.

If the endpoint is consistent then we write:

```json
{
    "facebook-$ENDPOINT_NAME-dns-consistent": true,
}
``` 

If all endpoints are consistent then we write:
```json
{
    "facebook-dns-blocking": false,
}
``` 

For each of the IPs we have found to be consistent we then do a TCP connect on
port 443 and check to see if it succeeds.
We ignore the IPs resolved to by the `stun` endpoint since that is UDP based
service.

If any of the TCP connections fail then we consider the endpoint to be blocked
and mark it as such in the report:

```json
{
    "facebook-$ENDPOINT_NAME-reachable": false,
    "facebook-tcp-blocking": true
}
```

If the endpoint is not blocked we write:

```json
{
    "facebook-$ENDPOINT_NAME-reachable": true,
    "facebook-tcp-blocking": true
}
```

If all the endpoints are not blocked then we write:

```json
{
    "facebook-tcp-blocking": false
}
```

# Expected output

## Parent data format

* df-001-httpt

* df-002-dnst

## Semantics

```json
{
	"facebook-b-api-dns-consistent": true | false | null,
	"facebook-b-api-reachable": true | false | null,

	"facebook-b-graph-dns-consistent": true | false | null,
	"facebook-b-graph-reachable": true | false | null,

	"facebook-edge-dns-consistent": true | false | null,
	"facebook-edge-reachable": true | false | null,

	"facebook-external-cdn-dns-consistent": true | false | null,
	"facebook-external-cdn-reachable": true | false | null,

	"facebook-scontent-cdn-dns-consistent": true | false | null,
	"facebook-scontent-cdn-reachable": true | false | null,

	"facebook-star-dns-consistent": true | false | null,
	"facebook-star-reachable": true | false | null,

	"facebook-stun-dns-consistent": true | false | null,
	"facebook-stun-reachable": null,

    "facebook-tcp-blocking": true | false | null,
    "facebook-dns-blocking": true | false | null,

    "tcp_connect": [
        {
            "ip": "xxx.xxx.xxx.xxx",
            "port": 5222 | 443,
            "status": {
                "success": true | false,
                "failure": "FAILURE STRING"
            }
        }
    ],
}
```

The meaning of the various keys is described in the above section.

## Possible conclusions


* If it is possible for users to use the Facebook Messenger app

* Which endpoints of Facebook Messenger appear to be blocked and how 


## Example output sample

```json
{
    "annotations": {
        "platform": "macos"
    },
    "data_format_version": "0.2.0",
    "id": "0651db48-f4fb-41fb-8e35-40869380fdd6",
    "input": null,
    "input_hashes": [],
    "measurement_start_time": "2016-11-25 12:52:05",
    "options": [],
    "probe_asn": "AS30722",
    "probe_cc": "IT",
    "probe_city": null,
    "probe_ip": "127.0.0.1",
    "report_id": "OOc2k6mbJ0a4w32uXfr02vdlR7292kpbnN1jTPcSWx4bcUo0N8kurasA4fsvrLbh",
    "software_name": "ooniprobe",
    "software_version": "2.0.3.dev0",
    "test_helpers": {},
    "test_keys": {
        "agent": "redirect",
        "facebook-b-api-dns-consistent": true,
        "facebook-b-api-reachable": true,
        "facebook-b-graph-dns-consistent": true,
        "facebook-b-graph-reachable": true,
        "facebook-dns-blocking": false,
        "facebook-edge-dns-consistent": true,
        "facebook-edge-reachable": true,
        "facebook-external-cdn-dns-consistent": true,
        "facebook-external-cdn-reachable": true,
        "facebook-scontent-cdn-dns-consistent": true,
        "facebook-scontent-cdn-reachable": true,
        "facebook-star-dns-consistent": true,
        "facebook-star-reachable": true,
        "facebook-stun-dns-consistent": true,
        "facebook-stun-reachable": null,
        "facebook-tcp-blocking": false,
        "queries": [
            {
                "answers": [
                    {
                        "answer_type": "A",
                        "ipv4": "31.13.86.8"
                    }
                ],
                "failure": null,
                "hostname": "star.c10r.facebook.com",
                "query_type": "A",
                "resolver_hostname": null,
                "resolver_port": null
            },
            {
                "answers": [
                    {
                        "answer_type": "A",
                        "ipv4": "69.171.239.36"
                    }
                ],
                "failure": null,
                "hostname": "stun.fbsbx.com",
                "query_type": "A",
                "resolver_hostname": null,
                "resolver_port": null
            },
            {
                "answers": [
                    {
                        "answer_type": "CNAME",
                        "hostname": "scontent.xx.fbcdn.net"
                    },
                    {
                        "answer_type": "A",
                        "ipv4": "31.13.86.4"
                    }
                ],
                "failure": null,
                "hostname": "external.xx.fbcdn.net",
                "query_type": "A",
                "resolver_hostname": null,
                "resolver_port": null
            },
            {
                "answers": [
                    {
                        "answer_type": "A",
                        "ipv4": "31.13.86.4"
                    }
                ],
                "failure": null,
                "hostname": "scontent.xx.fbcdn.net",
                "query_type": "A",
                "resolver_hostname": null,
                "resolver_port": null
            },
            {
                "answers": [
                    {
                        "answer_type": "CNAME",
                        "hostname": "mqtt.c10r.facebook.com"
                    },
                    {
                        "answer_type": "A",
                        "ipv4": "31.13.86.2"
                    }
                ],
                "failure": null,
                "hostname": "edge-mqtt.facebook.com",
                "query_type": "A",
                "resolver_hostname": null,
                "resolver_port": null
            },
            {
                "answers": [
                    {
                        "answer_type": "CNAME",
                        "hostname": "z-m.facebook.com"
                    },
                    {
                        "answer_type": "CNAME",
                        "hostname": "z-m.c10r.facebook.com"
                    },
                    {
                        "answer_type": "A",
                        "ipv4": "31.13.86.37"
                    }
                ],
                "failure": null,
                "hostname": "b-graph.facebook.com",
                "query_type": "A",
                "resolver_hostname": null,
                "resolver_port": null
            },
            {
                "answers": [
                    {
                        "answer_type": "CNAME",
                        "hostname": "z-m.facebook.com"
                    },
                    {
                        "answer_type": "CNAME",
                        "hostname": "z-m.c10r.facebook.com"
                    },
                    {
                        "answer_type": "A",
                        "ipv4": "31.13.86.37"
                    }
                ],
                "failure": null,
                "hostname": "b-api.facebook.com",
                "query_type": "A",
                "resolver_hostname": null,
                "resolver_port": null
            }
        ],
        "socksproxy": null,
        "tcp_connect": [
            {
                "ip": "31.13.86.8",
                "port": 443,
                "status": {
                    "failure": false,
                    "success": true
                }
            },
            {
                "ip": "31.13.86.37",
                "port": 443,
                "status": {
                    "failure": false,
                    "success": true
                }
            },
            {
                "ip": "31.13.86.4",
                "port": 443,
                "status": {
                    "failure": false,
                    "success": true
                }
            },
            {
                "ip": "31.13.86.4",
                "port": 443,
                "status": {
                    "failure": false,
                    "success": true
                }
            },
            {
                "ip": "31.13.86.2",
                "port": 443,
                "status": {
                    "failure": false,
                    "success": true
                }
            },
            {
                "ip": "31.13.86.37",
                "port": 443,
                "status": {
                    "failure": false,
                    "success": true
                }
            }
        ]
    },
    "test_name": "facebook_messenger",
    "test_runtime": 0.43950486183166504,
    "test_start_time": "2016-11-25 12:52:05",
    "test_version": "0.3.0"
}
```

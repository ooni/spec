# Specification version number

2022-02-03

* _status_: experimental

# Specification name

`quicping` (QUIC PING)

# Test preconditions

* An internet connection

# Expected impact

The ability to ping UDP hosts that support QUIC.

And with that:
1) The ability to test the availability of UDP endpoints that leverage QUIC.
Since UDP has no acknowledgement mechanism, UDP endpoints cannot be tested with raw UDP datagrams.

2) The ability to measure HTTP/3 / QUIC blocking in a more sophisticated way by distinguishing TLS censorship from UDP and QUIC blocking.


# Expected inputs

The experiment takes in as input a single domain name or IP address, or a list of domains/IP addresses.

The following options can be configured (for now by using the `miniooni` client):
- target port, option `Port` (`int64`, default: 443)
- number of ping repetitions, option `Repetitions` (`int64`, default: 10)
- number of milliseconds before read timeout, option `Timeout` (`int64`, default: 5000).



# Test description

A QUIC PING is a single QUIC Initial packet which elicits a single response from the target.

`quicping` ping request:
- QUIC Initial packet with a size of 1200 bytes (minimum datagram size defined in the RFC 9000)
- random payload (i.e. no TLS ClientHello)
- version string 0xbabababa which forces Version Negotiation at the server

`quicping` ping response:
- QUIC [Version Negotiation packet](https://www.rfc-editor.org/rfc/rfc9000.html#name-version-negotiation) from the server 

`quicping` behavior:
- create a QUIC Initial packet with random payload (i.e. no TLS handshake payload)
- set the QUIC version to a version that the target server will not accept
- create a UDP socket and sends the QUIC ping packet 
- *if the server receives the ping packet, it will respond with a Version Negotiation packet*
- wait for `x` milliseconds to receive the Version Negotiation response

# Expected output

## Parent data format

* none

## Semantics

```JSON
{
  "domain": "cloudflare.com",
  "pings": [
    {
      "conn_id_dst": "JhyTpyzq6v+A",
      "conn_id_src": "8PijH1B+sHGFXhVFWWVaMg==",
      "failure": null,
      "request": {},
      "response": {},
      "supported_versions": []
    },
    {
      "conn_id_dst": "3Skotq1GVpnTWWK6W68=",
      "conn_id_src": "1a1ZgG6lDELY8+HgpJUlrw==",
      "failure": null,
      "request": {},
      "response": {},
      "supported_versions": []
    }
    ],
  "repetitions": 2
}
```

where:

- `domain` (`string`) is the domain of the target host

- `pings` is the list of ping operations:
    - `conn_id_dst` (`[]byte`) is the used destination connection ID
    - `conn_id_src` (`[]byte`) is the used source connection ID
    - `failure` conforms to `df-007-errors`
    - `request` is the raw ping request, or `nil`
    - `response` is the raw ping response, or `nil`
    - `supported_versions` is the list of supported QUIC versions announced by the server

- `repetitions` (`int64`) is the number of subsequent pings.

## Possible conclusions

If we receive the ping response from the server we conclude that
<ol type="a">
<li> the UDP endpoint is available, </li>
<li> the QUIC connection itself is not targeted by censorship.
</ol>


## Example output sample

```json
{
    "annotations": {
        "architecture": "amd64",
        "engine_name": "ooniprobe-engine",
        "engine_version": "3.14.0-alpha.1",
        "platform": "linux"
    },
    "data_format_version": "0.2.0",
    "input": "cloudflare.com",
    "measurement_start_time": "2022-02-03 13:22:34",
    "options": [
        "Repetitions=2",
        "Timeout=10000",
        "Port=443"
    ],
    "probe_asn": "AS6805",
    "probe_cc": "DE",
    "probe_ip": "127.0.0.1",
    "probe_network_name": "Telefonica Germany GmbH \u0026 Co.OHG",
    "report_id": "",
    "resolver_asn": "AS6805",
    "resolver_ip": "62.109.121.39",
    "resolver_network_name": "Telefonica Germany GmbH \u0026 Co.OHG",
    "software_name": "miniooni",
    "software_version": "3.14.0-alpha.1",
    "test_keys": {
        "Domain": "cloudflare.com",
        "pings": [
            {
                "ConnIdDst": "JhyTpyzq6v+A",
                "ConnIdSrc": "8PijH1B+sHGFXhVFWWVaMg==",
                "Failure": null,
                "Ping": {
                    "data": "y7q6uroJJhyTpyzq6v+AEPD4ox9QfrBxhV4VRVllWjIARJ0vvhJWBHnAIq8NZTurHAZQw3taaMqcJAlOJa7TjVqnVwf8w2ToEuvxCmctB/NJZhQLiHlvoHoQOB0ZRQYmj7juJ49hCtZMvhQxsCHwfKA9OZrXUhfLfcfr+CUvYE2ZmaTfp/WQGD8lXfNokrTmLWBvRQ/i9OViEUyzEeg5capr3/3ncBxlJlcXZwTcWR6erNlGzaO69OlM5xrU0Ckk5YcuXIUrP+nEbTdzHJYN8T9cpC2KUFs5xZuPwJykYg7LOjkM9OngtAE/sy41gnYuvy/IxzpneMqZ62RaBzFLyvcl2/79wglrJkPAlMkWzVdtaGnreZ+1d8S3+w1A/hnE0F6OCdCzpEBZsga9dQZt+T4RkURqdpIsXuSYeR1SqIPFclzWRkRSal/euTH8FejPlkgFrEELOyOn3XPwAhHHz8aM3nrbyHFM5IgLmXiJO2ttucmXTjvgyPN3SfdktETi1XtNMr6xGDkHuKCcOmH1t2f3/rjJaFYAiFgH+vpPu2gPgJw7g3SkwcasAmP5PbnPvUJ2ldqREFTg62JFRmazeJiKNW0S94fiVWCgsejd/dfn6l7Bwm9Wu/H5WAmkh2Dkzjn+W032EjjUShapIqyJscIoQhkc9j3UgoUHd6Bd107l6G+kMCNWllZ8nG0FBVOn7yA6onVUz0fF3xUyVn+8ld6VLhuZXFEzC7Dqr0q2v5dfRK6LCEl1QglfO1+h+w3nZxvnFo6E1ei6ny9pPul/87KKpXow5tqEx05xGR4ft4mP8546U9pdNSdz7dmDoLUsOOBfHZJB5U41IQRvO0BEKEeC7plYTojiE5V16t24s5jcs8I1EecCal452A/8InDYk942aGHY+q4wAeir7/h8IkgXG1ioLA3hzdm0GpWCtogKaTE/LFjs6uBo0MFBh760NDflMEqSwc84AyCkrlkG+B7NSOYxcpbG5VJcHg1VjV/ROwAfzZ5FXJLKXAhR+qQN/ITk9BppoqM7/o/EJHzHITKi9XJ3my2c/gJfC0fAzKWLiodMyJhszKDdx2t7p+ahJREoIWoZZusg5RggispLR7BLaponere9TVRkFMf3lhmJ5pxGeO+OCMpXp1aaVzl1cYhihTkfUdqsVrf9JqSPyRedxINFBUbymTn0rcYVYf1RdY2RobgoTlaAo+dyGMR7uTPDlqWVMh9f5cF2KlJBe8HJJ4JobCHXyudHfZzIMcPbJI/h8uqRCUu6yy4OEEeSz2uSZqQDzoL4o4VquBIDd7i45+qXZB1/VoKM7re/pGQkQgjZEzZrZ6FlvkpIh6FRi8v/mtStUXlhq4nN6LJcR5zDb4TsXFdPUJFqvRMyUd4a2uepYdVaxNlN66yK1cfU/9nUSkFvZ+Z83+P+Gv3bwu887PwDaTDDr3ovR0ZkaCsER9mnapPnl5MqBtMaiAEbGaUYT3zGIvb0j2TZvJxlcjsw7hbW6Z+vAedXwe8hqVMi4kwBekrCBBr3e5b/bvQqcEIv0s+/JLR00FI1w+Rr9xj+92aGTdvQ3FsWWRS3fNA+xK76sn0ePb+14RBGnJPmdQa5V3oHE/PuMgcHBZfOVQ==",
                    "format": "base64"
                },
                "Response": {
                    "data": "hwAAAAAQ8PijH1B+sHGFXhVFWWVaMgkmHJOnLOrq/4AAAAAB/wAAHf8AABz/AAAb",
                    "format": "base64"
                },
                "SupportedVersions": [
                    1,
                    4278190109,
                    4278190108,
                    4278190107
                ]
            }
        ],
        "Repetitions": 2
    },
    "test_name": "quicping",
    "test_runtime": 1.080815938,
    "test_start_time": "2022-02-03 13:22:32",
    "test_version": "0.1.0"
}
```




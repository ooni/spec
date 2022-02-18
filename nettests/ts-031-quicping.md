# Specification version number

2022-02-14

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
Additionally, `quicping` allows URL input. Although the URL is not the semantically precise target of the experiment, this behavior makes `quicping` consistent with other experiments and enables us to reuse test lists.

The following options can be configured (for now by using the `miniooni` client):
- target port, option `Port` (`int64`, default: 443)
- number of ping requests that `quicping` will send, option `Repetitions` (`int64`, default: 10)
    - `quicping` does *not* stop when it successfully receives a response but always sends `Repetitions` times of ping requests



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
- repeat 10 times (or `Repetitions` times, if specified):
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
      "t": 1.001847542,
      "responses": [
          {
            "response_data": {},
            "failure": null,
            "t": 1.046892876,
            "supported_versions": [],
          }
      ],
    },
    {
      "conn_id_dst": "3Skotq1GVpnTWWK6W68=",
      "conn_id_src": "1a1ZgG6lDELY8+HgpJUlrw==",
      "failure": null,
      "request": {},
      "t": 2.002123995,
      "responses": [
          {
            "response_data": {},
            "failure": null,
            "t": 2.046783656,
            "supported_versions": [],
          }
      ],
    }
  ],
  "unexpected_responses": null,
  "repetitions": 2
}
```

where:

- `domain` (`string`) is the domain of the target host,

- `pings` is the list of ping operations:
    - `conn_id_dst` (`[]byte`) is the used destination connection ID, base64 encoded,
    - `conn_id_src` (`[]byte`) is the used source connection ID, base64 encoded,
    - `failure` conforms to `df-007-errors`,
    - `request` is the raw ping request, or `null`, base64 encoded,
    - `t` (`float64`) is the number of seconds elapsed since the measurement start,
    - `responses` is the list of received responses assigned to a single ping request (normally, we expect to receive exactly one),
        - `response_data` is the raw ping response, or `null`, base64 encoded,
        - `failure` conforms to `df-007-errors`,
        - `t` (`float64`) is the number of seconds elapsed since the measurement start,
        - `supported_versions` is the list of supported QUIC versions announced by the server,

- `unexpected_responses` is the list of unexpected response packets which could not be assigned to any ping request (e.g. injected by a censor), or `null`,
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
    "input": "google.com",
    "measurement_start_time": "2022-02-14 18:42:57",
    "options": [
        "Repetitions=2"
    ],
    "probe_asn": "AS9009",
    "probe_cc": "BE",
    "probe_ip": "127.0.0.1",
    "probe_network_name": "M247 Ltd",
    "report_id": "20220214T184258Z_quicping_BE_9009_n1_tRJVbl1gTjNzw2EU",
    "resolver_asn": "AS6805",
    "resolver_ip": "62.109.121.37",
    "resolver_network_name": "Telefonica Germany GmbH \u0026 Co.OHG",
    "software_name": "miniooni",
    "software_version": "3.14.0-alpha.1",
    "test_keys": {
        "domain": "google.com",
        "pings": [
            {
                "conn_id_dst": "7d6b8c357319510cabb63e7f1b44f27163",
                "conn_id_src": "79a49544574d4160794cdac9dbb7d288",
                "failure": null,
                "request": {
                    "data": "wbq6uroRfWuMNXMZUQyrtj5/G0TycWMQeaSVRFdNQWB5TNrJ27fSiABElYwqs+gDwZMTaR5UlX+phKY3gEAb7iP19kzJ9usE1w9gaG9maxtxvCV5gS3QhMTuF7FhbRcioIqsqL2FLhGY1yHHJMRn72ZpEk8amURCWk82pI4tO12G+VoVv1Z5GsZlmbYN3GSfXcUyPzW7U/75CoibjI10XKmeZWNkXC6Z1DTlKz15HqnHkyoReOW0m0zmlkwkJDbf1lzLS467rG7yJIWeb3c6Ji5xjswu9cczB4n1rvWTSOYFA2lKSH/Di7anlLpbCHdcE8fL3c/e8xMMNWX/NOxz0627K3PQTsPJcmf0Ky6IuyMstdz6Am2sjJWXTkdDj1Ehxlu6JetvKvWcmdqjdlJmJgPwfiFxh2gxHZkl4x0MFKc+yy+xMwT+qwAun67t54T3+ZeDyhcLMdxYr2TXzOjAl7kKLxb35dVmv9u8wHEz3c00Oih/7m/xWNsvSLokMuPNQNy2OsDbYPqHfdQAmJj4QEdJAYxkKXX2s1td7U3UEJNdtfWPTC43PdN6lal/T3UWwd/3gCpkqaRnuLiGVcEs/NBdRomkzt1aDYeN3CaB5uHpMys0Dv4CFpGPM+zbfTXy4f/ySU68avtxSK0MaKqyHQKuF6h3FGlHt1HDlGzOKPn1IwvkdTlvadUKb3qfYTB0i2nf7ToUH6kj0zOte+R3CnXdtr+7Bf1WOd8KJjx5y8aJfJRXVM7OH1F04jmahTOzb63MJTE1HuzfF9Al8kiBCRjkWolVNw62zoPbZyVNtSZmeQt+g2+BMnWbaQeNUX5RCocGC1HMrWj8XWBd6edFbk/VdyjBcWlaTfFtHbdjzmVZ2gQxEI3S1aeKnY1uzslMxu+N84E3vmW9ucgVu7JHHDKaWFYDq3oHIR+G7iewgaheewRVeQCZs4C45E0UCy1GyoNthCspFk5+00fCqBxPnk8s6932LabpAj66sD6E8STjKiyeHPiDV32YtTgoZCqefjOUfnfoxMAEi0nhIZhDFRhMk84+V3LRtQAnBRhcT6uYh7BZ40MUGzipGGbE0pFjDBiOG1VQqCsIrlXuYZTUUSFcx+TQPkyZD9nyAtvj7Vlj4g4Db2Czd9vwc8l1waXctHp4pFF2HqdqxbdP/R3b6Oq/qHFpcxr1nNixaKuhPLb6m3MrCuTW2MC4gs07kQyefTtkBzt9ItleQWbE+XxZTQQR1YEGQ6VcfJNEyoIwe5zX1ElDm0kboJ83lZu8Ibwep9fk/WRYyVyjzculzB92H6qWMyiY8JyMp9G5FCOQ5us4t81mNsambw8rH7JVZVRbulq2fCXQ9MvdWNhCo7d502S5jZDmzFpMCi7VJZ42xUMALKcurnAIFI/TjcXS1sWZmVnz9p6lXeQbryR9uSSlodtY/KV/Ze+68G7FsfjhVbB+i4FmzKHVcRthvRgKZkU+l0eBUWOW2MttMzyEQ7SBHX/T67+8FmvUJfuuaENRZ6MzM3V7lGIeVBUhEDSBxcT52E2uUjdEWI3q2zhtN3aMHIJP4db3pfgYkvwwuPVvA9I9PZyXFfjg6JL+21NwKeIqAy/UsdbVgv+9a+/2SMNXyg==",
                    "format": "base64"
                },
                "t": 1.034675298,
                "responses": [
                    {
                        "response_data": {
                            "data": "wAAAAAAQeaSVRFdNQWB5TNrJ27fSiBF9a4w1cxlRDKu2Pn8bRPJxY0paqioAAAAB/wAAHVEwNTBRMDQ2UTA0Mw==",
                            "format": "base64"
                        },
                        "failure": null,
                        "t": 1.096688808,
                        "supported_versions": [
                            1247455786,
                            1,
                            4278190109,
                            1362113840,
                            1362113590,
                            1362113587
                        ]
                    }
                ]
            },
            {
                "conn_id_dst": "a94117fb039250bf4914504fcb51e6",
                "conn_id_src": "b93fbe40ae40b5f380e39cc5f7563860",
                "failure": null,
                "request": {
                    "data": "xLq6uroPqUEX+wOSUL9JFFBPy1HmELk/vkCuQLXzgOOcxfdWOGAARJeBHCJmN9cgxizRXoqBTZUOed4d9LlH2LkRmDS+iOoEMzMewJlcQdlvh3h6XPoeE7dArVf1isgsjvuzpnrmLWFFLUuGXAFOqQEzPHNLqM1zXxGhArRBn81fE/dDRJtEJxIq9hdmDIKuH1zH4rSu/6Z8SQRs4SuQOekeiXpeqYtg0m5wskvRHB4kUk8YXUafh7DOOz0gbWq8fLrHzHaiPzgtYNl/Deqfu4M7hlPufJFSVgRz1H3d37CCvr+emM8Cd8nbSYW3szhb9NsUtPw4ukCxbLPbqBJ4Juc59yhMaTZWNrXVQawmF2t+ycWjij+eQn9s/9+Of4QdHQcIMjqYtyD7Jwxrn8wpkV4syVzPWDJfm64hAqaSFJ8/3jzdtY4d4VtDWzHiH5PUdr3lTJ7EuPkNjEI6IbwbciAnlQ8SxsqPtZp1ls06hqjeA1lJ3Nej3LwOWhzU4IHanDOA3BV39CgXbMToCzXDp7HxCMnnxUtoUuxH1JPueX231aTcGJAWL5TCExYDMxQUOBGeUFweZalHdjapXZRBjQCqCBsP/xgudenlBih+SQ9p5O2/GqxNMHCgb/He5Dgkkk/Y0GUTyvLGFW27ugvbqw8/+48L+pefHogIDC/iIZ9h0+g9tI7tRoWCSJwaiBYJT58UD+xrA71k/gj/GoJcqna7LNXVSHmhQtymVaoZr5gycPjBLcDlhie9BHEXUa4bIZJOaSnJXVmsulp1rZ8+Rk7jrndXGN8NoTs8iUOVG8WPF1DkDtk66cHwjY8iH35dtjNOhCvcyMzWH3PgSq/2ubYKjuvQx5+cvK8/39SZdgVaYK6U7O6XmPScLf2UGWht3QrUqnXy1/qgKtNpRwRVdX1pOaK2bXYzuIU0bMIfHLCPEYqCAH4BW/n/btklQXQrATR829xStbf2cmbM9oNQiccGtZIRRp92tvN1PAWnfpQ0+x0EpvYRwyw1Mihf7o6YDgU7HS1xR9b8pJ/0A7FvStOfnlWC8+XHdC4sjdl6dlzX6cZk3IZb4Y9ySBSHt+/jPVHOUUbnsZLz4nBpK+SQ1A3+R3u+HHgTVWNvontMURcaxNXyo5gLWAowDlbu46yfMbyShVURxLJ4LBUyHuYg7oHOWTnnhInvYq7/MRvPbicDFg2SelSDl66XNUSoP9Bn2J1/PF+c4seSwpNp0qiZc9m0UopnTV51UIhpD0UN1erhquc47aARrJHJZlqlJSv1xPYHUPtLFBwWx0rT3eFzw9qQ8EfkAvm7UHziHyki+LWfAbnIKzYLILKbQy1ePwVyR5WstPz50mOWwCnH+AuC/cDbO/6cjaEkCsr87PGrcy8gZY9Cc0a33RlU9P4MbI/I8caqTRvYY2Nq69YltOh38A+/Tl1WDFwnwrcgovq1XSWz+EdyypGZSUVdb52/aXO46W6WQ638zj2uSlNF2NbrJWa3k0jXDWoWpYngS1OKgW+9pJoVeSAjkiZO0mI84hBu0HOVHYXaJhk80IBzOyVDyamg2f4dCv2ef1wT7Hwz48j99Fnu6qzKAxHe1dNFxUTNKs4keXOFXmHha/dLMUirWg==",
                    "format": "base64"
                },
                "t": 2.034790841,
                "responses": [
                    {
                        "response_data": {
                            "data": "wAAAAAAQuT++QK5AtfOA45zF91Y4YA+pQRf7A5JQv0kUUE/LUeYAAAAB/wAAHboa+qpRMDUwUTA0NlEwNDM=",
                            "format": "base64"
                        },
                        "failure": null,
                        "t": 2.096128099,
                        "supported_versions": [
                            1,
                            4278190109,
                            3122330282,
                            1362113840,
                            1362113590,
                            1362113587
                        ]
                    }
                ]
            }
        ],
        "unexpected_responses": null,
        "repetitions": 2
    },
    "test_name": "quicping",
    "test_runtime": 4.033399142,
    "test_start_time": "2022-02-14 18:42:53",
    "test_version": "0.1.0"
}
```




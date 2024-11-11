# Specification version number

2024-11-11-002

* _status_: experimental

# Specification name

ECH Check (`echcheck`)

# Test preconditions

* An internet connection

# Expected impact

Understanding whether there is blocking triggered by the presence of the
Encrypted Client Hello (ECH) extension in the Client Hello during a TLS
handshake.

# Expected inputs

- `input` (`string`; optional): a target URL that is unlikely to be blocked
 to connect to (e.g. `google.com`)

The default implementation will use the domain `example.org` as
the `input`.

# Test description

Before performing the test, this experiment will resolve the given target URL
and establish a TCP connection. It will then attempt three TLS handshakes - one
with an ECH extension and the `public_name` (see: [ECH spec](https://datatracker.ietf.org/doc/html/draft-ietf-tls-esni-22#section-6.1-6)) of the `echconfig` for the domain
in the `ClientHelloOuter`, secondly ECH with a different `public_name` than that
advertised in the `public_name` field (`public_name_alt`), finally a control
handshake without an ECH extension present. The order of these operations is randomized to account for
residual censorship.

Currently the above values are hardcoded to the following:
* `URL`: https://cloudflare-ech.com/cdn-cgi/trace
* `ClientHelloOuter->public_name`: `cloudflare-ech.com`
* `ClientHelloOuter->public_name_alt`: `cloudflare.com`

If the input is overriden with a custom URL, we will still use as the
`public_name_alt` the fqdn `cloudflare.com`.

This behaviour may change in future versions of the test.

The SNI used inside of the `ClientHelloOuter` can be distinguished by looking at
the value of `outer_server_name`.

This experiment does not actually encrypt the Client Hello, but instead
attempts a GREASE (Generate Random Extensions And Sustain Extensibility) ECH
connection as per [draft-ietf-tls-esni-14](https://datatracker.ietf.org/doc/draft-ietf-tls-esni/).
This entails placing mocked ECH extension with random values in the
Client Hello. As passive network observers cannot tell a GREASE ECH connection
apart from a regular one, this test helps detect if there is any interference
to TLS handshakes that possess this field.

# Expected output

## Parent data format

We will include data following these data formats:

* `df-006-tlshandshake`

## Semantics

```JSON
{
    "test_keys": {
        "tls_handshakes": {},
    }
}
```

- `tls_handshakes` : (since 0.2.0) follows the `df-006-tlshandshake` data format

- `control` : (deprecated since: 0.2.0) follows the `df-006-tlshandshake` data format
- `target` : (deprecated since: 0.2.0) follows the `df-006-tlshandshake` data format

To distinguish between the tls handshake with ECH or without, you can look at
the `echconfig` field of the `tls_handshakes` list and check if it's empty or
not.

## Possible conclusions

* Failure of the target TLS handshake with the corresponding control handshake
succeeding will indicate interference to TLS handshakes with the ECH extension
present

## Example output sample

```JSON
{
  "annotations": {
    "architecture": "arm64",
    "engine_name": "ooniprobe-engine",
    "engine_version": "3.24.0-alpha",
    "go_version": "go1.21.11",
    "platform": "macos",
    "vcs_modified": "true",
    "vcs_revision": "186df09a8fdbb459d47d45d4630e3170247bb25b",
    "vcs_time": "2024-11-08T13:18:54Z",
    "vcs_tool": "git"
  },
  "data_format_version": "0.2.0",
  "input": "https://cloudflare-ech.com/cdn-cgi/trace",
  "measurement_start_time": "2024-11-11 10:28:04",
  "probe_asn": "AS30722",
  "probe_cc": "IT",
  "probe_ip": "127.0.0.1",
  "probe_network_name": "Vodafone Italia S.p.A.",
  "report_id": "",
  "resolver_asn": "AS30722",
  "resolver_ip": "91.80.37.88",
  "resolver_network_name": "Vodafone Italia S.p.A.",
  "software_name": "miniooni",
  "software_version": "3.24.0-alpha",
  "test_keys": {
    "tls_handshakes": [
      {
        "address": "104.18.10.118:443",
        "cipher_suite": "TLS_AES_128_GCM_SHA256",
        "failure": null,
        "negotiated_protocol": "h2",
        "network": "tcp",
        "no_tls_verify": true,
        "peer_certificates": [
          {
            "data": "MIIDujCCA2CgAwIBAgIRAPBDTLHoCzLmE2ouZzdmwOwwCgYIKoZIzj0EAwIwOzELMAkGA1UEBhMCVVMxHjAcBgNVBAoTFUdvb2dsZSBUcnVzdCBTZXJ2aWNlczEMMAoGA1UEAxMDV0UxMB4XDTI0MTAzMDIxMjEzMloXDTI1MDEyODIxMjEzMVowHTEbMBkGA1UEAxMSY2xvdWRmbGFyZS1lY2guY29tMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAECOArZgHHhZwFdngJKHh3PbDTKr2UbgEN407X9NgzHzSc+ffnJm0fASWgmwxfuLPXuaMHlpXcLb3tJm7ShveaRaOCAmEwggJdMA4GA1UdDwEB/wQEAwIHgDATBgNVHSUEDDAKBggrBgEFBQcDATAMBgNVHRMBAf8EAjAAMB0GA1UdDgQWBBRi02JIT/pmFp5aTCJGDebmX0LS1jAfBgNVHSMEGDAWgBSQd5I1Z8T/qMyp5nvZgHl7zJP5ODBeBggrBgEFBQcBAQRSMFAwJwYIKwYBBQUHMAGGG2h0dHA6Ly9vLnBraS5nb29nL3Mvd2UxLzhFTTAlBggrBgEFBQcwAoYZaHR0cDovL2kucGtpLmdvb2cvd2UxLmNydDAzBgNVHREELDAqghJjbG91ZGZsYXJlLWVjaC5jb22CFCouY2xvdWRmbGFyZS1lY2guY29tMBMGA1UdIAQMMAowCAYGZ4EMAQIBMDYGA1UdHwQvMC0wK6ApoCeGJWh0dHA6Ly9jLnBraS5nb29nL3dlMS9aa2p6VVhLQ1V3VS5jcmwwggEEBgorBgEEAdZ5AgQCBIH1BIHyAPAAdQDPEVbu1S58r/OHW9lpLpvpGnFnSrAX7KwB0lt3zsw7CAAAAZLfhRAzAAAEAwBGMEQCIC4T9fxUhEiWfJ5+ltmzbw0Qi9Dtyvq8jO2xWptlGod8AiA9hSlQodL8y7VuqMzgwmDHthXgt1nsm6vBwCaxVI9HhQB3AMz7D2qFcQll/pWbU87psnwi6YVcDZeNtql+VMD+TA2wAAABkt+FEEAAAAQDAEgwRgIhAPqj7desNvIBunxRqb+Etres3D7rlCGX7nwtQ8XQUAPuAiEAlPGz6wihPtu1dkEs1ImdrzktfrGza60fY96tbaq/9jcwCgYIKoZIzj0EAwIDSAAwRQIgaL43R1neNgT8Jz7/nwt7rLWGZIODr4Gk44E1zFVk4OsCIQDvXu068bjKopUlxv22WnwchsKG9fbVIZnJLLGAQ8VhMw==",
            "format": "base64"
          },
          {
            "data": "MIICnzCCAiWgAwIBAgIQf/MZd5csIkp2FV0TttaF4zAKBggqhkjOPQQDAzBHMQswCQYDVQQGEwJVUzEiMCAGA1UEChMZR29vZ2xlIFRydXN0IFNlcnZpY2VzIExMQzEUMBIGA1UEAxMLR1RTIFJvb3QgUjQwHhcNMjMxMjEzMDkwMDAwWhcNMjkwMjIwMTQwMDAwWjA7MQswCQYDVQQGEwJVUzEeMBwGA1UEChMVR29vZ2xlIFRydXN0IFNlcnZpY2VzMQwwCgYDVQQDEwNXRTEwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAARvzTr+Z1dHTCEDhUDCR127WEcPQMFcF4XGGTfn1XzthkubgdnXGhOlCgP4mMTG6J7/EFmPLCaY9eYmJbsPAvpWo4H+MIH7MA4GA1UdDwEB/wQEAwIBhjAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwEgYDVR0TAQH/BAgwBgEB/wIBADAdBgNVHQ4EFgQUkHeSNWfE/6jMqeZ72YB5e8yT+TgwHwYDVR0jBBgwFoAUgEzW63T/STaj1dj8tT7FavCUHYwwNAYIKwYBBQUHAQEEKDAmMCQGCCsGAQUFBzAChhhodHRwOi8vaS5wa2kuZ29vZy9yNC5jcnQwKwYDVR0fBCQwIjAgoB6gHIYaaHR0cDovL2MucGtpLmdvb2cvci9yNC5jcmwwEwYDVR0gBAwwCjAIBgZngQwBAgEwCgYIKoZIzj0EAwMDaAAwZQIxAOcCq1HW90OVznX+0RGU1cxAQXomvtgM8zItPZCuFQ8jSBJSjz5keROv9aYsAm5VsQIwJonMaAFi54mrfhfoFNZEfuNMSQ6/bIBiNLiyoX46FohQvKeIoJ99cx7sUkFN7uJW",
            "format": "base64"
          },
          {
            "data": "MIIDejCCAmKgAwIBAgIQf+UwvzMTQ77dghYQST2KGzANBgkqhkiG9w0BAQsFADBXMQswCQYDVQQGEwJCRTEZMBcGA1UEChMQR2xvYmFsU2lnbiBudi1zYTEQMA4GA1UECxMHUm9vdCBDQTEbMBkGA1UEAxMSR2xvYmFsU2lnbiBSb290IENBMB4XDTIzMTExNTAzNDMyMVoXDTI4MDEyODAwMDA0MlowRzELMAkGA1UEBhMCVVMxIjAgBgNVBAoTGUdvb2dsZSBUcnVzdCBTZXJ2aWNlcyBMTEMxFDASBgNVBAMTC0dUUyBSb290IFI0MHYwEAYHKoZIzj0CAQYFK4EEACIDYgAE83Rzp2iLYK5DuDXFgTB7S0md+8FhzubeRr1r1WEYNa5A3XP3iZEwWus87oV8okB2O6nGuEfYKueSkWpz6bFyOZ8pn6KY019eWIZlD6GEZQbR3IvJx3PIjGov5cSr0R2Ko4H/MIH8MA4GA1UdDwEB/wQEAwIBhjAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwDwYDVR0TAQH/BAUwAwEB/zAdBgNVHQ4EFgQUgEzW63T/STaj1dj8tT7FavCUHYwwHwYDVR0jBBgwFoAUYHtmGkUNl8qJUC99BM00qP/8/UswNgYIKwYBBQUHAQEEKjAoMCYGCCsGAQUFBzAChhpodHRwOi8vaS5wa2kuZ29vZy9nc3IxLmNydDAtBgNVHR8EJjAkMCKgIKAehhxodHRwOi8vYy5wa2kuZ29vZy9yL2dzcjEuY3JsMBMGA1UdIAQMMAowCAYGZ4EMAQIBMA0GCSqGSIb3DQEBCwUAA4IBAQAYQrsPBtYDh5bjP2OBDwmkoWhIDDkic574y04tfzHpn+cJodI2D4SseesQ6bDrarZ7C30ddLibZatoKiws3UL9xnELz4ct92vID24FfVbiI1hY+SW6FoVHkNeWIP0GCbaM4C6uVdF5dTUsMVs/ZbzNnIdCp5Gxmx5ejvEau8otR/CskGN+hr/W5GvT1tMBjgWKZ1i4//emhA1JG1BbPzoLJQvyEotc03lXjTaCzv8mEbep8RqZ7a2CPsgRbuvTPBwcOMBBmuFeU88+FSBX6+7iP0il8b4Z0QFqIwwMHfs/L6K1vepuoxtGzi4CZ68zJpiq1UvSqTbFJjtbD4seiMHl",
            "format": "base64"
          }
        ],
        "server_name": "cloudflare-ech.com",
        "t": 0.098567,
        "t0": 0.076615,
        "tags": [],
        "tls_version": "TLSv1.3"
      },
      {
        "address": "104.18.10.118:443",
        "cipher_suite": "TLS_AES_128_GCM_SHA256",
        "echconfig": "GREASE",
        "failure": null,
        "negotiated_protocol": "h2",
        "network": "tcp",
        "no_tls_verify": true,
        "outer_server_name": "cloudflare-ech.com",
        "peer_certificates": [
          {
            "data": "MIIDujCCA2CgAwIBAgIRAPBDTLHoCzLmE2ouZzdmwOwwCgYIKoZIzj0EAwIwOzELMAkGA1UEBhMCVVMxHjAcBgNVBAoTFUdvb2dsZSBUcnVzdCBTZXJ2aWNlczEMMAoGA1UEAxMDV0UxMB4XDTI0MTAzMDIxMjEzMloXDTI1MDEyODIxMjEzMVowHTEbMBkGA1UEAxMSY2xvdWRmbGFyZS1lY2guY29tMFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAECOArZgHHhZwFdngJKHh3PbDTKr2UbgEN407X9NgzHzSc+ffnJm0fASWgmwxfuLPXuaMHlpXcLb3tJm7ShveaRaOCAmEwggJdMA4GA1UdDwEB/wQEAwIHgDATBgNVHSUEDDAKBggrBgEFBQcDATAMBgNVHRMBAf8EAjAAMB0GA1UdDgQWBBRi02JIT/pmFp5aTCJGDebmX0LS1jAfBgNVHSMEGDAWgBSQd5I1Z8T/qMyp5nvZgHl7zJP5ODBeBggrBgEFBQcBAQRSMFAwJwYIKwYBBQUHMAGGG2h0dHA6Ly9vLnBraS5nb29nL3Mvd2UxLzhFTTAlBggrBgEFBQcwAoYZaHR0cDovL2kucGtpLmdvb2cvd2UxLmNydDAzBgNVHREELDAqghJjbG91ZGZsYXJlLWVjaC5jb22CFCouY2xvdWRmbGFyZS1lY2guY29tMBMGA1UdIAQMMAowCAYGZ4EMAQIBMDYGA1UdHwQvMC0wK6ApoCeGJWh0dHA6Ly9jLnBraS5nb29nL3dlMS9aa2p6VVhLQ1V3VS5jcmwwggEEBgorBgEEAdZ5AgQCBIH1BIHyAPAAdQDPEVbu1S58r/OHW9lpLpvpGnFnSrAX7KwB0lt3zsw7CAAAAZLfhRAzAAAEAwBGMEQCIC4T9fxUhEiWfJ5+ltmzbw0Qi9Dtyvq8jO2xWptlGod8AiA9hSlQodL8y7VuqMzgwmDHthXgt1nsm6vBwCaxVI9HhQB3AMz7D2qFcQll/pWbU87psnwi6YVcDZeNtql+VMD+TA2wAAABkt+FEEAAAAQDAEgwRgIhAPqj7desNvIBunxRqb+Etres3D7rlCGX7nwtQ8XQUAPuAiEAlPGz6wihPtu1dkEs1ImdrzktfrGza60fY96tbaq/9jcwCgYIKoZIzj0EAwIDSAAwRQIgaL43R1neNgT8Jz7/nwt7rLWGZIODr4Gk44E1zFVk4OsCIQDvXu068bjKopUlxv22WnwchsKG9fbVIZnJLLGAQ8VhMw==",
            "format": "base64"
          },
          {
            "data": "MIICnzCCAiWgAwIBAgIQf/MZd5csIkp2FV0TttaF4zAKBggqhkjOPQQDAzBHMQswCQYDVQQGEwJVUzEiMCAGA1UEChMZR29vZ2xlIFRydXN0IFNlcnZpY2VzIExMQzEUMBIGA1UEAxMLR1RTIFJvb3QgUjQwHhcNMjMxMjEzMDkwMDAwWhcNMjkwMjIwMTQwMDAwWjA7MQswCQYDVQQGEwJVUzEeMBwGA1UEChMVR29vZ2xlIFRydXN0IFNlcnZpY2VzMQwwCgYDVQQDEwNXRTEwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAARvzTr+Z1dHTCEDhUDCR127WEcPQMFcF4XGGTfn1XzthkubgdnXGhOlCgP4mMTG6J7/EFmPLCaY9eYmJbsPAvpWo4H+MIH7MA4GA1UdDwEB/wQEAwIBhjAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwEgYDVR0TAQH/BAgwBgEB/wIBADAdBgNVHQ4EFgQUkHeSNWfE/6jMqeZ72YB5e8yT+TgwHwYDVR0jBBgwFoAUgEzW63T/STaj1dj8tT7FavCUHYwwNAYIKwYBBQUHAQEEKDAmMCQGCCsGAQUFBzAChhhodHRwOi8vaS5wa2kuZ29vZy9yNC5jcnQwKwYDVR0fBCQwIjAgoB6gHIYaaHR0cDovL2MucGtpLmdvb2cvci9yNC5jcmwwEwYDVR0gBAwwCjAIBgZngQwBAgEwCgYIKoZIzj0EAwMDaAAwZQIxAOcCq1HW90OVznX+0RGU1cxAQXomvtgM8zItPZCuFQ8jSBJSjz5keROv9aYsAm5VsQIwJonMaAFi54mrfhfoFNZEfuNMSQ6/bIBiNLiyoX46FohQvKeIoJ99cx7sUkFN7uJW",
            "format": "base64"
          },
          {
            "data": "MIIDejCCAmKgAwIBAgIQf+UwvzMTQ77dghYQST2KGzANBgkqhkiG9w0BAQsFADBXMQswCQYDVQQGEwJCRTEZMBcGA1UEChMQR2xvYmFsU2lnbiBudi1zYTEQMA4GA1UECxMHUm9vdCBDQTEbMBkGA1UEAxMSR2xvYmFsU2lnbiBSb290IENBMB4XDTIzMTExNTAzNDMyMVoXDTI4MDEyODAwMDA0MlowRzELMAkGA1UEBhMCVVMxIjAgBgNVBAoTGUdvb2dsZSBUcnVzdCBTZXJ2aWNlcyBMTEMxFDASBgNVBAMTC0dUUyBSb290IFI0MHYwEAYHKoZIzj0CAQYFK4EEACIDYgAE83Rzp2iLYK5DuDXFgTB7S0md+8FhzubeRr1r1WEYNa5A3XP3iZEwWus87oV8okB2O6nGuEfYKueSkWpz6bFyOZ8pn6KY019eWIZlD6GEZQbR3IvJx3PIjGov5cSr0R2Ko4H/MIH8MA4GA1UdDwEB/wQEAwIBhjAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwDwYDVR0TAQH/BAUwAwEB/zAdBgNVHQ4EFgQUgEzW63T/STaj1dj8tT7FavCUHYwwHwYDVR0jBBgwFoAUYHtmGkUNl8qJUC99BM00qP/8/UswNgYIKwYBBQUHAQEEKjAoMCYGCCsGAQUFBzAChhpodHRwOi8vaS5wa2kuZ29vZy9nc3IxLmNydDAtBgNVHR8EJjAkMCKgIKAehhxodHRwOi8vYy5wa2kuZ29vZy9yL2dzcjEuY3JsMBMGA1UdIAQMMAowCAYGZ4EMAQIBMA0GCSqGSIb3DQEBCwUAA4IBAQAYQrsPBtYDh5bjP2OBDwmkoWhIDDkic574y04tfzHpn+cJodI2D4SseesQ6bDrarZ7C30ddLibZatoKiws3UL9xnELz4ct92vID24FfVbiI1hY+SW6FoVHkNeWIP0GCbaM4C6uVdF5dTUsMVs/ZbzNnIdCp5Gxmx5ejvEau8otR/CskGN+hr/W5GvT1tMBjgWKZ1i4//emhA1JG1BbPzoLJQvyEotc03lXjTaCzv8mEbep8RqZ7a2CPsgRbuvTPBwcOMBBmuFeU88+FSBX6+7iP0il8b4Z0QFqIwwMHfs/L6K1vepuoxtGzi4CZ68zJpiq1UvSqTbFJjtbD4seiMHl",
            "format": "base64"
          }
        ],
        "server_name": "cloudflare-ech.com",
        "t": 0.123876,
        "t0": 0.096614,
        "tags": [],
        "tls_version": "TLSv1.3"
      },
      {
        "address": "104.18.10.118:443",
        "cipher_suite": "TLS_AES_128_GCM_SHA256",
        "echconfig": "GREASE",
        "failure": null,
        "negotiated_protocol": "h2",
        "network": "tcp",
        "no_tls_verify": true,
        "outer_server_name": "cloudflare.com",
        "peer_certificates": [
          {
            "data": "MIID6TCCA5CgAwIBAgIQFtGszwHTzwQT+KtePBiG1jAKBggqhkjOPQQDAjA7MQswCQYDVQQGEwJVUzEeMBwGA1UEChMVR29vZ2xlIFRydXN0IFNlcnZpY2VzMQwwCgYDVQQDEwNXRTEwHhcNMjQxMDEwMjMxNjM0WhcNMjUwMTA5MDAxNjMxWjAZMRcwFQYDVQQDEw5jbG91ZGZsYXJlLmNvbTBZMBMGByqGSM49AgEGCCqGSM49AwEHA0IABKeNXimrMJ319no17HrtqFFttI39bXomgPdJUEW0DiWGmQ0Z6HsqlD36i+EpGG5CyCncxp24KGQrvYlHO6ozJMujggKWMIICkjAOBgNVHQ8BAf8EBAMCB4AwEwYDVR0lBAwwCgYIKwYBBQUHAwEwDAYDVR0TAQH/BAIwADAdBgNVHQ4EFgQU99As+ZH4M51+yV9dSLrY5kSZnOAwHwYDVR0jBBgwFoAUkHeSNWfE/6jMqeZ72YB5e8yT+TgwXgYIKwYBBQUHAQEEUjBQMCcGCCsGAQUFBzABhhtodHRwOi8vby5wa2kuZ29vZy9zL3dlMS9GdEUwJQYIKwYBBQUHMAKGGWh0dHA6Ly9pLnBraS5nb29nL3dlMS5jcnQwaQYDVR0RBGIwYIIOY2xvdWRmbGFyZS5jb22CEmNwMi5jbG91ZGZsYXJlLmNvbYISY3AzLmNsb3VkZmxhcmUuY29tghJjcDQuY2xvdWRmbGFyZS5jb22CEmNwNS5jbG91ZGZsYXJlLmNvbTATBgNVHSAEDDAKMAgGBmeBDAECATA2BgNVHR8ELzAtMCugKaAnhiVodHRwOi8vYy5wa2kuZ29vZy93ZTEvVFFSUml0TlFaYTguY3JsMIIBAwYKKwYBBAHWeQIEAgSB9ASB8QDvAHUAzxFW7tUufK/zh1vZaS6b6RpxZ0qwF+ysAdJbd87MOwgAAAGSeO8yzAAABAMARjBEAiBvfQJrts8okqXkL2+tyb+Yn3uFkPgwSDHy1AsgksXYRwIgMEhDZTb6y9awS0g/IZ644TE+RECM0JEFqgVgSAXvCJ8AdgCi4wrkRe+9rZt+OO1HZ3dT14JbhJTXK14bLMS5UKRH5wAAAZJ47zKoAAAEAwBHMEUCIQDlgD4pa8FhXSmp/nK+shcuF9BavcPv+SK8YU6ncLswKQIgOnKg/xKZk8IMFFZm2w4O1CIaKSyTUZCX8V/dJVZWITMwCgYIKoZIzj0EAwIDRwAwRAIgYjquzQb6fiu1KfnHgJd8hLmW65P8QYje4FXU91cT5/ACIA/0fG/gb//HRc8jE/jD2L0qe4F1JKAMjlg/Vf8NOCV8",
            "format": "base64"
          },
          {
            "data": "MIICnzCCAiWgAwIBAgIQf/MZd5csIkp2FV0TttaF4zAKBggqhkjOPQQDAzBHMQswCQYDVQQGEwJVUzEiMCAGA1UEChMZR29vZ2xlIFRydXN0IFNlcnZpY2VzIExMQzEUMBIGA1UEAxMLR1RTIFJvb3QgUjQwHhcNMjMxMjEzMDkwMDAwWhcNMjkwMjIwMTQwMDAwWjA7MQswCQYDVQQGEwJVUzEeMBwGA1UEChMVR29vZ2xlIFRydXN0IFNlcnZpY2VzMQwwCgYDVQQDEwNXRTEwWTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAARvzTr+Z1dHTCEDhUDCR127WEcPQMFcF4XGGTfn1XzthkubgdnXGhOlCgP4mMTG6J7/EFmPLCaY9eYmJbsPAvpWo4H+MIH7MA4GA1UdDwEB/wQEAwIBhjAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwEgYDVR0TAQH/BAgwBgEB/wIBADAdBgNVHQ4EFgQUkHeSNWfE/6jMqeZ72YB5e8yT+TgwHwYDVR0jBBgwFoAUgEzW63T/STaj1dj8tT7FavCUHYwwNAYIKwYBBQUHAQEEKDAmMCQGCCsGAQUFBzAChhhodHRwOi8vaS5wa2kuZ29vZy9yNC5jcnQwKwYDVR0fBCQwIjAgoB6gHIYaaHR0cDovL2MucGtpLmdvb2cvci9yNC5jcmwwEwYDVR0gBAwwCjAIBgZngQwBAgEwCgYIKoZIzj0EAwMDaAAwZQIxAOcCq1HW90OVznX+0RGU1cxAQXomvtgM8zItPZCuFQ8jSBJSjz5keROv9aYsAm5VsQIwJonMaAFi54mrfhfoFNZEfuNMSQ6/bIBiNLiyoX46FohQvKeIoJ99cx7sUkFN7uJW",
            "format": "base64"
          },
          {
            "data": "MIIDejCCAmKgAwIBAgIQf+UwvzMTQ77dghYQST2KGzANBgkqhkiG9w0BAQsFADBXMQswCQYDVQQGEwJCRTEZMBcGA1UEChMQR2xvYmFsU2lnbiBudi1zYTEQMA4GA1UECxMHUm9vdCBDQTEbMBkGA1UEAxMSR2xvYmFsU2lnbiBSb290IENBMB4XDTIzMTExNTAzNDMyMVoXDTI4MDEyODAwMDA0MlowRzELMAkGA1UEBhMCVVMxIjAgBgNVBAoTGUdvb2dsZSBUcnVzdCBTZXJ2aWNlcyBMTEMxFDASBgNVBAMTC0dUUyBSb290IFI0MHYwEAYHKoZIzj0CAQYFK4EEACIDYgAE83Rzp2iLYK5DuDXFgTB7S0md+8FhzubeRr1r1WEYNa5A3XP3iZEwWus87oV8okB2O6nGuEfYKueSkWpz6bFyOZ8pn6KY019eWIZlD6GEZQbR3IvJx3PIjGov5cSr0R2Ko4H/MIH8MA4GA1UdDwEB/wQEAwIBhjAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwDwYDVR0TAQH/BAUwAwEB/zAdBgNVHQ4EFgQUgEzW63T/STaj1dj8tT7FavCUHYwwHwYDVR0jBBgwFoAUYHtmGkUNl8qJUC99BM00qP/8/UswNgYIKwYBBQUHAQEEKjAoMCYGCCsGAQUFBzAChhpodHRwOi8vaS5wa2kuZ29vZy9nc3IxLmNydDAtBgNVHR8EJjAkMCKgIKAehhxodHRwOi8vYy5wa2kuZ29vZy9yL2dzcjEuY3JsMBMGA1UdIAQMMAowCAYGZ4EMAQIBMA0GCSqGSIb3DQEBCwUAA4IBAQAYQrsPBtYDh5bjP2OBDwmkoWhIDDkic574y04tfzHpn+cJodI2D4SseesQ6bDrarZ7C30ddLibZatoKiws3UL9xnELz4ct92vID24FfVbiI1hY+SW6FoVHkNeWIP0GCbaM4C6uVdF5dTUsMVs/ZbzNnIdCp5Gxmx5ejvEau8otR/CskGN+hr/W5GvT1tMBjgWKZ1i4//emhA1JG1BbPzoLJQvyEotc03lXjTaCzv8mEbep8RqZ7a2CPsgRbuvTPBwcOMBBmuFeU88+FSBX6+7iP0il8b4Z0QFqIwwMHfs/L6K1vepuoxtGzi4CZ68zJpiq1UvSqTbFJjtbD4seiMHl",
            "format": "base64"
          }
        ],
        "server_name": "cloudflare-ech.com",
        "t": 0.139085,
        "t0": 0.11582,
        "tags": [],
        "tls_version": "TLSv1.3"
      }
    ]
  },
  "test_name": "echcheck",
  "test_runtime": 0.139121083,
  "test_start_time": "2024-11-11 10:28:04",
  "test_version": "0.2.0"
}
```

# Privacy considerations

This nettest may be less intrusive than other nettests as it encourages
connections to URLs that are unlikely to be censored. We are not issuing DNS
queries for the sensitive domain and we are not connecting to the sensitive
IP address.

# Packet capture considerations

This test does not capture packets by default.

# Acknowledgments

Cloudflare's ECH [implementation](https://github.com/cloudflare/go) was used as
a reference for this experiment.

# Future work

This nettest is still experimental. It will establish a full ECH connection
once the protocol is stable and a Go implementation is available.

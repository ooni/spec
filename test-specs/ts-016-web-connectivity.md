# Specification version number

2016-01-22-001

# Specification name

Web connectivity

# Test preconditions

* An internet connection

* The ability to reach the web consistency test helper

# Expected impact

Ability to detect if the websites being tested are reachable and if not what is
the reason for them not being reachable.

# Expected inputs

A list of URLs to be tested.

## Semantics

One URL per line:

http://example-1.com/
http://example-2.com/path1/
http://example-3.com/path2/

# Test description

This test is divided into multiple steps that will each test a different aspect
related to connectivity of the website in question.

The first step is to inform the web_connectivity test helper of our intention
to run the measurement against the URL in question and hence have it perform a
control measurement from an un-censored vantage point.

The control measurement shall include in the response the following information:

* The list of A records for a DNS query related to the hostname in question

* Wether or not it is able to establish a TCP session to the first A record in
  the DNS response

* The body length of the result of a HTTP GET request for the path in question

The request for the control measurement and the experiment measurements can run
in parallel, that is it is not a requirement to running the experiments to
already have the result of the control measurement since the comparison of the
control and experiment is done at the end.

The experiment itself consists of the following steps:

1. **Resolver identification**
   Determine what is the default resolver being used by the probe by performing
   an A lookup for a special domain that will contain in the A lookup answer
   section the IP of the resolver of the requester.
   An example of this is the service whoami.akamai.com, but also a specialised
   test-helper may be used.
   The result of this will be stored inside of the "client_resolver" key of the
   report.

2. **DNS lookup**
   Perform an A query to the default resolver for the hostname of the URL to be
   tested.
   Record the list of A records in a list inside the report under the key "ips".

3. **TCP connect**
   Attempt to establish a TCP session on port 80 for the list of IPs identified
   at step 2. If the URL begins with HTTPS then also establish a TCP session
   towards port 443.

4. **HTTP GET request**
   Perform a HTTP GET request for the path specified in the URI and record the
   response.
   The headers sent in the request shall be:
    **User-Agent**: `Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36`
    Corresponding to the most popular version (47.0.2526.106) of the most
    popular browser (Chrome) on the most popular OS (Windows 7).

5. **Control comparison**
   We then begin to poll the test-helper to learn if the control measurement
   has been performed. Once we obtain a result from the test-helper we shall do
   the following comparisons:

   * Are the DNS responses from the control consistent with those from the
     probe?
     The value of the report key "dns_consistency" can be the one of the following:

        * 'consistent' if the IP addresses of the A lookup from the control
          match exactly those of the experiment.

        * 'reverse_match' if the reverse lookup for any of the IPs in the DNS
          answer match (a match is defined as having any the domain.tld section
          in common).

        * 'inconsistent' if none of the above conditions are met.

    * Did we succeed in establishing a TCP session to the IP:port combinations
      found by doing A lookups?
      The value of the report key "tcp_connect" will be a list with 1 item per
      IP:port combination with the following values in each entry:

        * 'ip' the IP address a connection was attempted to be established to.

        * 'port' the port number we connected to.

        * 'status': {
            'success': boolean flag indicating if the connection attempt was successful (true) or failed (false),
            'failure': an error string indicating the reason for the failure,
            'blocked': boolean flag to indicate if blocking is happening on a
            TCP basis, this is determined by comparing the tcp_connect result
            from the control to that of the experiment. For example if both the
            control and the experiment produce a failure that host is assumed
            to be offline and hence no blocking is occurring, while if the
            experiment demonstrates an offline status, while the control
            succeeds we assume blocking is occuring.
        }

    * Does the body length of the experiment match that of the control?
      The value of the report key "body_length_match" is set to true if
      body_length_control/body_length_experiment > 0.8, null if we failed to
      connect, false if body_length_control/body_length_experiment < 0.8.

# Expected output

## Semantics

{
    "client_resolver": "xxx.xxx.xxx.xxx",
    "dns_consistency": "consistent" | "reverse_match" | "inconsistent",
    "body_length_match": true | false | null,
    "tcp_connect": [
        {
            "ip": "xxx.xxx.xxx.xxx",
            "port": 80 | 443,
            "status": {
                "success": true | false,
                "failure": "FAILURE STRING",
                "blocked": true | false | null
            }
        }
    ],
    "accessible": true | false | null,
    "blocking": "tcp_ip" | "dns" | "http" | null
}

The meaning of the keys "dns_consistency", "body_length_match" and
"tcp_connect" is described above.

The flag "accessible" indicates if the site in question is overall considered to be 
accessible (DNS responses are consistent, at least one TCP connection succeeds
and the expected HTTP response is received).

The flag "blocking" is set to null if "accessible" is true, otherwise it
indicates the reason for blocking, if that is due to inconsistent DNS
responses (dns), TCP/IP based blocking (tcp_ip) or if the body lengths mismatch
(http).

## Possible conclusions

* If the URL in question is accessible from the network vantage point of the probe.

* If the blocking of the URL in question is being performed by means of DNS
  tampering, TCP connection RST/IP blocking or by having a transparent HTTP
  proxy.

## Example output sample

XXX

# Privacy considerations

If the client has opted out of providing the ASN of their probe the
client_resolver key may give away extra information pertaining to the network
they are on if they are using the resolver of their ISP.

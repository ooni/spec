# DNS consistency

This test compares the DNS query results from a DNS resolver which is considered
to be reliable with one that is tested for tampering.

The domain name system (DNS) is what is responsible for transforming a host name
(e.g. torproject.org) into an IP address (e.g. 38.229.72.16). ISPs, amongst
others, run DNS resolvers which map IP addresses to host names. In certain
circumstances though, ISPs map the wrong IP addresses to the wrong host names.
This is a form of tampering, which OONI can detect by running its DNS
consistency test.

This test compares the IP address of a given host name allocated by the Google
DNS resolver (which we assume to not be tampered with) with the IP address
mapped to that website by a provider. If the two IP addresses of the same
website are different, then there is a sign of network interference. When ISPs
tamper with DNS answers, users are redirected to other websites or fail to
connect to their intended websites.

**Note:** DNS resolvers, such as Google or your local ISP, often provide users
with IP addresses that are closest to them geographically. Often this is not
done with the intent of network tampering, but merely for the purpose of
providing users faster access to websites. As a result, some false positives
might arise in OONI measurements.

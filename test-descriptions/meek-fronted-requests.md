# Meek Fronted Requests

This test examines whether the domains used by Meek (a type of [Tor
bridge](https://bridges.torproject.org/)) work in tested networks.

Meek is a pluggable transport which uses non-blocked domains, such as
google.com, awsstatic.com (Amazon cloud infrastructure) and ajax.aspnetcdn.com
(Microsoft azure cloud infrastructure), to proxy its users over
[Tor](https://www.torproject.org/) to blocked websites, while hiding both the
fact that they are connecting to such websites and how they are connecting to
them. As such, Meek is useful for not only connecting to websites that are
blocked, but for also hiding which websites you are connecting to.

Below is a simplified explanation of how this works:

[user] → https://www.google.com] → Meek hosted on the cloud] → Tor] → blocked-
[website]

The user will receive a response (access to a blocked website, for example) from
cloud-fronted domains, such as google.com, through the following way:

[blocked-website] → Tor] → Meek hosted on the cloud] → https://www.google.com] →
[user]

In short, this test does an encrypted connection to cloud-fronted domains over
HTTPS and examines whether it can connect to them or not.

# Tor Bridge Reachability

This test examines whether **[Tor bridges](https://bridges.torproject.org/)** work in tested networks.

[Tor](https://www.torproject.org/) is free and open source software which enables online anonymity and censorship circumvention. It was designed to bounce communications around a distributed network of relays run by volunteers around the world, thus hiding users' IP address and circumventing online tracking and censorship. However, Internet Service Providers (ISPs) in various countries around the world are often ordered by their governments to block users' access to Tor. As a result, Tor bridges were developed to enable users to connect to the Tor network in countries where such access is blocked.

This test runs Tor with a list of bridges and if it's able to connect to them successfully, we consider that Tor bridges are not blocked in the tested network. If the test, however, is unable to bootstrap a connection, then the Tor bridges are either offline or blocked.
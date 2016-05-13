# Lantern

This test provides an automated way of examining whether Lantern works in a
tested network.

[Lantern](https://getlantern.org/) is a centralized and peer-to-peer proxy,
which is used as a circumvention tool. It detects whether websites are blocked
and, if so, it allows you to access them via Lantern servers or via the network
of Lantern users.

This test runs Lantern and checks to see if it is working. If it's able to
connect to a Lantern server and reach a control website over it, then we
consider that Lantern can be used for censorship circumvention within the tested
network. If however the test is unable to connect to Lantern servers, then it is
likely the case that they are blocked within the tested network.

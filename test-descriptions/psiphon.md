# Psiphon

This test provides an automated way of examining whether Psiphon works in a
tested network.

[Psiphon](https://psiphon.ca/) is a free and open source tool that utilises SSH,
VPN and HTTP proxy technology for censorship circumvention.

This test runs Psiphon and checks to see if it is working. If it's able to
connect to a Psiphon server and reach a website over it, then we consider that
Psiphon can be used for censorship circumvention within the tested network. If
however the test is unable to connect to Psiphon servers, then it is likely the
case that they are blocked within the tested network.

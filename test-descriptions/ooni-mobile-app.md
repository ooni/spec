# OONI mobile

The OONI mobile version for Android and iOS can be called **ooniprobe - Test
your network**.

## App description (for Android and iOS)

Interested in collecting evidence of Internet censorship? Curious about the
speed and performance of the network that you are using?

By running ooniprobe's tests, you will examine the following:

* Blocking of websites 

* Presence of systems that could be responsible for censorship and/or surveillance

* Speed and performance of your network

These tests have been developed by the **[Open Observatory of Network Interference (OONI)](https://ooni.torproject.org/)**, a free software project
(under [The Tor Project](https://www.torproject.org/)) that aims to uncover
**Internet censorship** around the world. Since 2012, OONI has
[collected](https://explorer.ooni.torproject.org/world/) millions of network
measurements across more than 90 countries, shedding light on multiple cases of
network interference. By running these tests, you will help increase
*transparency* around Internet censorship and network interference around the
world.

* **Collecting evidence of Internet censorship.** OONI's web connectivity test is
designed to examine whether websites are blocked and if so, how. This test, in
particular, attempts to determine whether access to sites is blocked through DNS
tampering, TCP connection RST/IP blocking, or by a transparent HTTP proxy. By
knowing how access to sites is interfered with, you can more easily evaluate how
to circumvent specific types of censorship.

* **Detecting systems responsible for censorship and surveillance.** Various types of
proxy technologies are used in networks for implementing censorship,
surveillance, and traffic manipulation. OONI's HTTP invalid request line test is
designed to uncover the presence of such systems within tested networks.
However, it's important to point out that not all the systems that you might
find are necessarily responsible for censorship and/or surveillance. Many proxy
technologies, for example, are used in networks for caching purposes.

* **Measuring the speed and performance of your network.** Sometimes the network that
we are using doesn't work as well as we'd like it to. OONI's implementation of
the Network Diagnostic Test (NDT) attempts to measure the speed of your network
by connecting to [M-Lab](https://www.measurementlab.net/) servers near you and by subsequently uploading and
downloading random data. In doing so, NDT collects low level TCP/IP information
that can help characterize the speed and performance of your network. Such
information can also be useful in examining cases of throttling.

* **Open data.** OONI publishes all network measurement data that it collects and
processes because open data allows third parties to conduct independent studies,
to verify OONI findings and/or to answer other research questions. Such data can
also help increase transparency around Internet censorship and various forms of
network interference. All data is published on **[OONI Explorer](https://explorer.ooni.torproject.org/world/)**.

* **Free software.** All OONI tests, as well as its NDT implementation, are based on
free and open source software. You can find the source code through the
following links:

    * https://github.com/measurement-kit/ooniprobe-ios

    * https://github.com/measurement-kit/ooniprobe-android

* **Disclaimer.** Running ooniprobe might be against the terms of service of your ISP
or legally questionable in your country. By running ooniprobe you will connect
to web services which may be banned, and use web censorship circumvention
methods such as Tor. The OONI project will publish data submitted by probes,
possibly including your IP address or other identifying information. In
addition, your use of ooniprobe will be clear to anyone who has access to your
computer, and to anyone who can monitor your Internet connection (such as your
employer, ISP or government).

## Short app description (for Android) 

Run this app to examine Internet censorship and your network's performance!

### Keywords = network performance, Internet censorship

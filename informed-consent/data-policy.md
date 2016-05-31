# OONI Data Policy

**Effective:** 2016-05-05

**Version:** 1.0.0

This Data Policy explains what data is collected, processed, stored and
published by the [Open Observatory of Network Interference
(OONI)](https://ooni.torproject.org/) project, as well as how users can opt-out
from sending OONI their network measurements.

The use of OONI's software and website constitutes an acceptance of the policies
outlined in this Data Policy.

## Website Visitors

OONI does *not* use tracking cookies, analytics or any other tracking
technologies through its [website](https://ooni.torproject.org/) and does *not*
collect any information about its website visitors.

Access logs, which only include the date of the requested page, can be stored
for up to 2 weeks and do *not* include the IP addresses of website visitors nor
the time of access.

If this changes in the future, users will be notified through this Data Policy.

## Software Users

OONI's software is *not* designed to protect user privacy, but is developed by
people who *care* about user privacy. While OONI developers take measures to
protect users' privacy by *not* deliberately collecting their IP addresses,
users might still potentially face risks as a result of OONI's data collection,
processing, storing and publishing methods, as explained below.

To mitigate such potential risks, users can choose to *opt-out* from certain or
all types of data collection by OONI, though this would limit OONI's research.

### Data OONI Collects

When a user runs [OONI software
tests](https://github.com/TheTorProject/ooni-spec), the OONI project can
collect the following types of data:

**Country code**

OONI *by default* collects the code which corresponds to the country from which
the user is running OONI tests from, by automatically searching for it based on
the user's IP address through the [MaxMind GeoIP
database](https://www.maxmind.com/en/home). The collection of country codes is
an important part of OONI's research, as it enables OONI to map out global
network measurements and to identify where network interferences take place.
This information could potentially be useful to local researchers, journalists
and advocates who aim to discover network interferences (such as censorship and
traffic manipulation) in a country.

OONI software users can choose to *opt-out* from the collection of country codes
by [editing the ooniprobe
 configuration](https://github.com/TheTorProject/ooni-probe#configuring-ooniprobe)
file inside of `~/.ooni/ooniprobe.conf`.

**Autonomous System Number (ASN)**

OONI *by default* collects the Autonomous System Number (ASN) which corresponds
to the network that a user is running OONI tests from. The collection of the ASN
is useful to OONI's research because it reveals the specific network provider
(such as Vodafone) of a user. Such information can increase transparency in
regards to which network providers are implementing censorship or other forms of
network interference.

OONI software users can choose to *opt-out* from the collection of their
network's ASN by [editing the ooniprobe
configuration](https://github.com/TheTorProject/ooni-probe#configuring-ooniprobe)
file inside of  `~/.ooni/ooniprobe.conf`.

**Date and time of measurements**

OONI *by default* collects the time and date of when tests were run. This
information helps OONI evaluate when network interferences occur and to compare
them across time. Users *cannot* opt-out from this type of data collection, as
it is a core component of OONI's research.

**IP addresses and other information**

OONI does *not* deliberately collect or store users' IP addresses. In fact, OONI
takes measures to remove users' IP addresses from the collected measurements, to
protect its users from potential risks.

However, OONI might *unintentionally* collect users' IP addresses and other
potentially personally-identifiable information, if such information is included
in the HTTP headers or other metadata of measurements. This, for example, can
occur if the tested websites include tracking technologies or custom content
based on a user's network location.

By default, OONI does *not* collect users' IP addresses, but they can choose to
*opt-in* (to provide more accurate information) by [editing the ooniprobe
 configuration](https://github.com/TheTorProject/ooni-probe#configuring-ooniprobe)
file inside of `~/.ooni/ooniprobe.conf`.

**Network measurements**

The types of network measurements that OONI collects depend on the types of
tests that are run. Specifications about each OONI test can be viewed
[here](https://github.com/TheTorProject/ooni-spec/tree/master/test-specs), and
details about what collected network measurements entail can be viewed through
[OONI Explorer](https://explorer.ooni.torproject.org/world/) or through OONI's
[public list of measurements](https://measurements.ooni.torproject.org/).

OONI software users can choose to *opt-out* from sending OONI their measurements
by running ooniprobe with the `-n` command line option.

### Data OONI Processes

Through its [data pipeline](https://github.com/TheTorProject/ooni-pipeline),
OONI processes all of the network measurements that it collects, which include
the aforementioned types of data. OONI processes data with the aim of deriving
meaning from the collected measurements and, specifically, in an attempt to
answer the following types of questions:

* Which types of OONI tests were run?

* In which countries were those tests run?

* In which networks were those tests run?

* When were tests run?

* What types of network interferences occurred?

* In which countries did network interferences occur?

* In which networks did network interferences occur?

* When did network interferences occur?

* How did network interferences occur?

To answer such questions, OONI's pipeline is designed to process data which is
automatically sent to OONI's measurement collector by default.

Users can choose to *opt-out* from sending OONI their measurements by running
ooniprobe with the `-n` command line option.

### Data OONI Stores

OONI stores all of the aforementioned data that it collects and processes,
including users' IP addresses and other potentially personally-identifiable
information which *might unintentionally* be collected and therefore stored,
despite OONI's efforts to prevent this from happening.

Users can *opt-out* from sending specific types of data to OONI's measurement
collector as described in previous sections of this Data Policy, or they can
*opt-out* from sending OONI any of their measurements by running ooniprobe with
the `-n` command line option.

### Data OONI Publishes

OONI publishes all of the network measurement data that it collects and
processes because open data allows third parties to conduct independent studies,
to verify OONI findings and/or to answer other research questions.

Currently, OONI publishes all collected measurements on its website
through:

* [OONI Explorer](https://explorer.ooni.torproject.org/world/)

* [OONI's list of measurements](https://measurements.ooni.torproject.org/)

Both resources include the same measurements; the only difference is that OONI
Explorer is an interactive visualization of the measurements.

If users' IP addresses and/or other potentially personally-identifiable
information are included in the HTTP headers or other metadata of collected
measurements, then such information *might* be publicly available through the
above resources.

It's important to note that the publication of network measurements might raise
various types of *risks* for OONI users. Information about such risks can be
found [here](INCLUDE LINK). Users can also consider opting-out from submitting
some or all of their measurements to OONI through the following opt-out section
of this Data Policy.

### Opt-out

OONI software users can *opt-out* from sending OONI's measurement collector
specific types of data by [editing the ooniprobe
 configuration](https://github.com/TheTorProject/ooni-probe#configuring-ooniprobe)
 file inside of `~/.ooni/ooniprobe.conf`. Through this file, users can opt-out 
from sending OONI the following types of information:

* Country code

* Autonomous System Number (ASN)

By default, OONI does *not* collect users' IP addresses, but users can choose to
*opt-in* (to provide more accurate information) through the above configuration
file.

Users can also choose to *opt-out* from sending OONI's measurement collector any
data at all, by running ooniprobe with the `-n` command line option. This option
is quite often chosen by users who prefer to *not* have their measurements
published, due to potential risks that could emerge as a result of such
publication.

## Data Policy Changes

Although most changes are likely to be minor, OONI may change its Data Policy
from time to time, and in OONI's sole discretion.

OONI encourages its website visitors and software users to frequently check this
page for any changes to its Data Policy. The continued use of OONI's website and
software after any change in this Data Policy will constitute acceptance of such
change.


Thoughts or questions about this Data Policy? Please send an email to
**contact@openobservatory.org**.

```
Key ID:
    0CB177B7
Fingerprint:
4C15 DDA9 96C6 C0CF 48BD 3309 6B29 43F0 0CB1 77B7
```

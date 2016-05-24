# OONI Partnership Program

**Uncovering Evidence of Online Censorship Around the World**


Hunderds of volunteers around the world have made the OONI project possible over
the last years by contributing to the collection of millions of network
measurements across more than 95 countries. These measurements have unveiled
numerous cases of online censorship and traffic manipulation around the world,
and they have even shed light on the covert presence of proxy technologies which
might have been used for the purposes of surveillance.

Now we aim to take OONI a step further by studying network anomalies more
systematically and within local context, through OONI's Partnership Program. 

## What is the OONI Partnership Program?

The OONI Partnership Program is a collaboration between the [Open Observatory of
Network Interference (OONI)](https://ooni.torproject.org/) and groups or
organizations around the world on the study of network interferences, such as
online censorship.

## What is the aim of the OONI Partnership Program?

Through the Partnership Program, we aim to:

* increase transparency and public awareness about online censorship and other
  network anomalies

* increase the stable collection of measurements across time

* improve the quality of collected measurements

* provide context to collected measurements

* directly support partner organizations in terms of using ooniprobe and
  reporting on the results

We aim to study network measurements with input from partners not only in terms
of *which URLs* would be interesting to test for censorship within their
country's context, but also in terms of *when* would be an interesting period
for such testing (for example, during demonstrations or leading up to the
inauguaration of their Prime Minister).

## What does the OONI Partnership Program entail?

The OONI Partnership Program was developed in an attempt to study online
censorship and other network interferences more strategically and within local
context through partnerships. To this end, depending on the role of each partner
organization, the partnerships can include (but not necessarily limited to) the
following:

* Lepidopter: Running ooniprobe from a Raspberry Pi 

* Creation/Review of lists of URLs to test for online censorship

* Story-telling: Reports, blogs and data visualizations

### Lepidopter: Running ooniprobe from a Raspberry Pi

Over the last years, the collection of measurements based on OONI's [free
software tests](https://github.com/TheTorProject/ooni-spec) was mostly dependent
on volunteers running ooniprobe (OONI's network measurement software) from their
terminal. This by default limited tests to those who were tech-savvy enough to
run them, and to those who didn't mind running tests directly from their
computer. The data collection was also limited by users' ability to keep their
devices on and continuously connected to the internet while running tests (some
of which might even last for hours at a time). As a result, systematically
collecting and comparing measurements across time, and consistently monitoring
networks during important local events (such as elections) has been quite a
challenge.

In an attempt to address such limitations, we have developed **Lepidopter**: a
distribution of ooniprobe for Raspberry Pi platforms. This enables users to
contribute to the collection of network measurements consistently across time,
without having to manually run ooniprobe from their computers and regardless of
their technical skills. This distribution is configured in such a way that, when
inserted into a Raspberry Pi and connected to a network, it will by default run
ooniprobe once a day and send collected measurements directly to OONI's
measurement collector. It is also designed to automatically get updated to the
newest version of ooniprobe. All measurements collected by Lepidopter are
published on [OONI Explorer](https://explorer.ooni.torproject.org/world/).

The main advantages of collecting measurements through Raspberry Pis include the
following:

**Stable and continuous daily measurements across extended periods of time**

Through the use of Lepidopter by partners, we aim to create stable vantage
points which will allow for the continuous collection of daily measurements.
This can enable us to compare results across time and to better detect and
evaluate network interferences. Lepidopter is also particularly useful because
it allows us to provision it with new URLs to be tested, since it is meant to
constantly be connected to a network.

**More types of data collection**

Partners can run *more* tests through the use of a Raspberry Pi (in comparison
to the desktop version of ooniprobe) and contribute to vaster types of data
collection. While ooniprobe could, in theory, run all tests on Linux, that would
not only be complicated to set up properly, but it would also require to grant
the running process capabilities that could expose users to security risks,
should the code be vulnerable. All tests, on the other hand, can be run through
Raspberry Pis, thus increasing the amount of types of data collection. Running
tests on separate hardware devices also has the advantage that they are not
directly connected to a user's computer.

**More accurate measurements**

The various security products, such as firewalls, that users might have
installed on their devices can impact the accuracy of measurements. As Raspberry
Pis running ooniprobe would be independent from such products, the accuracy of
such measurements would be greater.

Through the measurements we have collected over the last years (which can be
viewed on [OONI Explorer](https://explorer.ooni.torproject.org/world/)), we have
observed that censorship is not always carried out countrywide, nor always
implemented in the same way across networks. As such, hosting Lepidopter within
various *different* networks in each country is an important component of OONI's
study and a core objective of the Partnership Program.

### Creation/Review of lists of URLs to test for online censorship

The Citizen Lab has supported OONI over the last years through the creation of
lists of URLs to test for online censorship. These lists include the following:

* **Country-specific test lists:** https://github.com/citizenlab/test-
  lists/tree/master/lists 

* **Global test list:** https://github.com/citizenlab/test-
  lists/blob/master/lists/global.csv (including a list of globally accessed
  websites)

Through the OONI Partnership Program, we aim to collaborate with groups and
organizations that are interested in reviewing the test lists that are specific
to their country, or by creating new test lists for their countries if they
don't already exist. This collaborative process would help include more URLs
which are relevant to the country's local context and which are potentially
interesting to test for censorship. Furthermore, through partnerships we would
also work towards the risk assessment of tested URLs and their associated
categories.

### Story-telling: Reports, blogs and data visualizations

OONI is a free software project and as such, our role is primarily that of a
*technical* partner. That said, we are *also* willing to support our partners in
terms of data analysis and story-telling based on the collected measurements.

We aim to increase transparency and public awareness about online censorship and
other forms of network interference by communicating the main findings through
reports, blogs and data visualizations. In collaboration with partners, we would
like to provide local context to the findings. Through consultation with legal
partners, for example, we would like to shed light on how and whether cases of
online censorship are legally justified within their country. We would also like
to collaborate with partners in terms of understanding the socio-political
context of their country and reporting on internet controls within that context.

## Who can join the OONI Partnership Program?

Groups and organizations interested in increasing transparency about online
censorship and other forms of network interference are encouraged to join the
OONI Partnership Program. This can include (but not necessarily limited to):

* NGOs

* hackerspaces

* legal associations

* media organizations

* research groups

Ideally, we would like to foster collaboration between various different types
of groups/organizations, each of which could contribute to the study of network
interferences from a difference lens and which would also allow for the
distribution of efforts amongst different groups.

Various hackerspaces, for example, could contribute to the data collection by
running ooniprobe (through Raspberry Pis) within different networks. Legal
organizations could provide consultation in regards to (potential) local legal
risks of running ooniprobe and/or provide legal analysis of collected
measurements. Media organizations could report on the findings, NGOs could
provide further analysis within the context of digital rights and research
groups could use the collected data to explore questions of their own. Through
this collaborative approach between groups and organizations, we aim to improve
the study and reporting of network interferences.

If you're interested in joining the OONI Partnership Program, please drop us an
email at **contact@ooni.io**.

## How can OONI support its partners?

If you're interested in examining online censorship within your country, OONI
can support you in the following ways:

* **Technical support:** We can guide you through the entire process of using
  OONI's software, whether that involves running ooniprobe from your computer
  or setting up a Raspberry Pi to run ooniprobe. We can also supply some of
  our partners with Raspberry Pis and SD cards, which are already set-up with
  ooniprobe and ready to be used for testing. Throughout the duration of the
  partnership, you can rely on us for technical support in regards to the use
  of OONI's software.

* **Creating/Reviewing lists of URLs to test for online censorship:** We will
  support you in terms of creating and/or reviewing a list of URLs specific to
  your country for testing online censorship throughout the duration of the
  partnership.

* **Communicating main findings:** We will support you in terms of communicating
  the main findings from the collected measurements to the public. Such
  support can include the writing of reports and blogs and, in some cases, the
  creation of data visualizations.

We might also be able to support partners in other additional ways, though this
can be evaluated on a case by case basis.







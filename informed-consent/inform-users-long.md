# Goal

OONI is a project aimed at mapping network anomalies by performing measurements
from the vantage point of its users. You can find details on what exactly it is
that we measure by reading through our [test
specifications](https://github.com/TheTorProject/ooni-spec/tree/master/test-
specs). The data we collect is then made available to the public for further
analysis.

The goal of this study is to have a better understanding of how the internet
works around the world and of how and when network interferences (such as
censorship and traffic manipulation) occur.

Please take a minute to go through what can possibly be the implications of
running ooniprobe and make sure you understand them before proceeding.

# Legality

OONI tests are designed to test networks for symptoms of censorship,
surveillance and traffic manipulation and, in some countries around the world,
this could potentially have **legal** or **extra-legal implications**. We
therefore strongly urge you to consult with lawyers *prior* to downloading,
installing and running OONI, especially if you are uncertain of what the
potential risks are in the country where you plan to use OONI.

## Legal implications

The legal implications of downloading, installing and running OONI can vary from
country to country, which is why we advise you to consult with local lawyers.
Some questions worth asking related to the use of OONI can include the
following:

* Does country X have laws in force that restrict or criminalize the use of
  **network measurement software**?

* Does country X have laws in force that restrict or criminalize the use of
  **censorship detection software**?

* Does country X have laws in force that restrict or criminalize the use of
  **censorship circumvention software**?

* Does country X have laws in force that restrict or criminalize certain types
  of **internet access**? (for example, is it illegal to access certain
  websites?)

* Does country X have laws in force or ISP License Agreements that require
  Internet Service Providers (ISPs) to track users' online activities and to
  retain such records?

* Does country X have laws in force that could potentially be used to
  criminalize the use of software like OONI?

* Have laws or rules in country X ever been used to criminalize groups or
  individuals based on their internet activity? (this does not necessarily need
  to be specific to network measurements)
 
Prior to running OONI, we strongly recommend that you ask a local lawyer to
review (1) the legality of accessing the websites that are included in both your
country's test list and in the global test list, and (2) the legality of running
OONI tests.

### Legality of websites included in OONI test lists

When running either oonideckgen (OONI's software package) or OONI's HTTP-request
test, you will connect to and download data from various websites which are
included in the following two lists:

* **Country-specific test list:** https://github.com/citizenlab/test-
  lists/tree/master/lists (search for your country's test list based on its
  country code)

* **Global test list:** https://github.com/citizenlab/test-
  lists/blob/master/lists/global.csv (including a list of globally accessed
  websites)

Many websites included in the above lists will likely be controversial and can
include pornography or hate speech, which might be illegal to access in your
country. We therefore recommend that you examine carefully whether you are
willing to take the risk of accessing and downloading data from such websites
through OONI tests, especially if this could potentially lead to various forms
of retribution.

### Legality of OONI tests

While network measurements or the use of censorship detection software might not
be illegal per se, some network tests that OONI does might be against the *terms
of service of your Internet Service Provider (ISP)* or legally questionable in
your country. We therefore urge you to review the specifications for each OONI
test carefully, prior to running it.

In summary, OONI tests are designed to:

* Detect whether websites are blocked

* Detect the presence of systems which might be responsible for censorship,
  surveillance and traffic manipulation

* Examine whether censorship circumvention tools, such as Tor bridges, Psiphon,
  Lantern and OpenVPN, are blocked

You can view details about what each OONI test does here:
https://github.com/TheTorProject/ooni- spec/tree/master/test-specs

We encourage you to check whether bypassing censorship is illegal in your
country, especially if you plan on running OONI tests (such as the Psiphon,
Lantern and OpenVPN tests) which require the installation of circumvention
software.

While most countries don't have laws which explicitly criminalize the use of
censorship detection or circumvention software, it's important to note that the
use of OONI can *still* potentially be criminalized in certain countries under
other, broader laws. The use of OONI, for example, can potentially be
criminalized on the grounds of *national security* if the data obtained by
running OONI is viewed as "jeopardizing" the country's external or internal
security. In some countries, downloading or using OONI could be viewed as an
illegal anti-government activity, even when there are no laws specifically
prohibiting the use of such software. In more extreme cases, any form of active
network measurement could be illegal or banned, or even considered a form of
espionage.

Many countries employ sophisticated surveillance measures that allow governments
to track individuals' online activities – even if they are using a VPN or a
proxy server to protect their privacy. In such countries, governments might be
able to identify you as a OONI user regardless of what measures you take to
protect your online privacy. Many countries also have a lengthy history of
subjecting digital rights activists to various forms of abuse that could make it
dangerous for individuals in these countries to run OONI.

Using OONI may subject you to severe civil, criminal, or extra-judicial penalties,
and such sanctions can possibly include:

* Imprisonment

* Physical assaults

* Large fines

* Receiving threats

* Being placed on government watchlists

* Targeted for surveillance

In view of potential legal and extra-legal threats, we strongly recommend that
you consult with local lawyers and understand legal risks prior to running OONI.

You can also reach out to us with specific inquiries at **legal@ooni.nu**.
Please bare in mind though that we are *not* lawyers, but we might be able to
seek legal advice for you or to put you in touch with lawyers who could address
your questions and/or concerns.

Some relevant resources include:

* [Tor Legal FAQ](https://www.eff.org/torchallenge/faq.html)

* [EFF Know Your Rights](https://www.eff.org/issues/know-your-rights)

# Privacy

OONI IS NOT DESIGNED TO PROTECT YOUR PRIVACY. It will reveal information about
your internet connection to the whole world. Particular groups, such as your ISP
and web services used by the OONI tests, might be able to discover even more
detailed information about you.

The public will be able to see the information collected by ooniprobe. This will
definitely include your approximate location, the network (ASN) you are
connecting from, and when you ran ooniprobe. Other identifying information, such
as your IP address, is not deliberately collected, but might be included in HTTP
headers or other metadata. The full page content downloaded by OONI could
potentially include further information if, for example, a website includes
tracking codes or custom content based on your network location.

You can view the details of what information OONI releases to the public through
its list of [measurements](https://ooni.torproject.org/reports/) and/or through
[OONI Explorer](https://explorer.ooni.torproject.org/world/). You should expect
this information to remain online permanently.

The OONI project when running some tests against our backends will be able to
see your IP address.

Organizations monitoring your internet activity will be able to see all web
traffic generated by OONI, including your IP address, and will likely be able to
link it to you personally. These organizations might include your government,
your ISP, and/or your employer.

Anybody with access to your computer, now or in the future, may be able to
see that you have installed or run ooni.

Services connected to by OONI will be able to see your IP address, and may be
able to detect that you are using OONI.

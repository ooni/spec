# HTTP Host

This test attempts to:

* examine whether the domain names of websites are blocked

* detect the presence of “middle boxes” (software which could be used for
  censorship and/or traffic manipulation) in tested networks

* assess which censorship circumvention techniques are capable of bypassing the
  censorship implemented by the “middle box”

HTTP is a protocol which transfers or exchanges data across the internet. It
does so by handling a client's request to connect to a server, and a server's
response to a client's request. Every time you connect to a server, you (the
client) send a request through the HTTP protocol to that server. Such requests
include “HTTP headers”, some of which (the “Host header”) include information
about the specific domain that you want to connect to. When you connect to
torproject.org, for example, the host header of your HTTP request includes
information which communicates that you want to connect to that domain.

This test implements a series of techniques which help it evade getting detected
from censors and then uses a list of domain names (such as bbc.co.uk) to connect
to an OONI backend control server, which sends the host headers of those domain
names back to us. If a “middle box” is detected between the network path of the
probe and the OONI backend control server, its fingerprint might be included in
the JSON data that we receive from the backend control server. Such data also
informs us if the tested domain names are blocked or not, as well as how the
censor tried to fingerprint the censorship of those domains. This can sometimes
lead to the identification of the type of infrastructure being used to implement
censorship.

**Note:** The presence of a middle box is not necessarily indicative of
censorship and/or traffic manipulation, as they are often used in networks for
caching purposes.

# tq-010 SOAs and NSes for possibly-censored domain

When domain is suspected to be censored by resolver it is interesting to
capture resolver’s opinion on NSes and SOA records for the domain and every
parent domain up to TLD<sup>[1](#fn1)</sup>. E.g. login.vk.com needs SOA and NS requests for
login.vk.com and vk.com at least.

<a name="fn1">1</a>: It may be easier to query all the domains up to the root as TLD definition is not trivial. See [public suffix list](https://publicsuffix.org/) for inspiration.

TBD: it’s unclear if SOA and NS records for some well-known subdomain are of use or not.

## Examples
- Italy, one of ISPs was transparent about login.vk.com blocking announcing the ISP in SOA Resource Record for vk.com
- [Russia, Omsk](https://glam-evil.livejournal.com/565583.html), one if ISPs was blocking youtube.com with admin@ email in SOA record

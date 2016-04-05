# Specification version number

2015-10-11-000

# Specification name

OpenVPN Test

# Test preconditions

Have OpenVPN installed and configured to work with at least one server and privileges to run the test as root.

# Expected impact

Ability to measure whether OpenVPN is working from the given network vantage point.

# Expected inputs

A single URL to fetch, supplied by command line argument "--url (-u)".
OpenVPN configuration file, specified by the command line argument "--openvpn-config (-c)"

# Test description

This test first launches OpenVPN and parses output to determine if it has bootstrapped. After bootstrap, it fetches the  URL specified by the --url argument using OpenVPN.

The specific string used to determine bootstrap from OpenVPN output in version
"0.0.1" is "Initialization Sequence Completed" from standard output.

# Expected output

## Parent data format

None.

## Required output data

success:
**boolean** The bootstrap status of OpenVPN (success or failure).

OpenVPN_linux --headless:
**dictionary** the parent key of OpenVPNs output that contains the keys stdout and stderr

stdout:
**string** Output produced by OpenVPNs standard output.

stderr:
**string** Error produced by OpenVPNs standard error.

body:
**string** The page body of a successful HTTP request.

failure:
**string** If failure, then the corresponding failure message.

## Data specification version number

## Semantics

    'success' - True or False - whether OpenVPN has bootstrapped.
    'body' - http page body if successfully requested.
    'failure' - optional, present if there is a failure.
    'l/usr/sbin/openvpn --config configfile': 
      'stdout' - Contents of standard output produced by OpenVPN.
      'stderr' - Contents of standard error produced by OpenVPN.

## Possible conclusions

We can determine whether or not OpenVPN is able to bootstrap, according to its output.
We can determine whether or not a given URL is reachable via OpenVPN.

## Example output sample
```
---
input_hashes: []
options: [-c, openvpnconfigfile.ovpn, -u, '']
probe_asn: AS0
probe_cc: ZZ
probe_city: null
probe_ip: 127.0.0.1
report_id: nqvK7YrK6J5Di7BiWDwPUBfyKcbLoVWeU4DgnxTzzKWMQABvhC2l3q6aLUwF0CA9
software_name: ooniprobe
software_version: 1.3.1
start_time: 1444925440.0
test_helpers: {}
test_name: test_openvpn_circumvent
test_version: 0.0.1
...
---
/usr/sbin/openvpn --config /pathtoopenvpnconfigfile/openvpnconfigfile.ovpn: {
  exit_reason: process_done, stderr: '', stdout: 'Thu Oct 15 20:10:40 2015 OpenVPN
    2.3.2 x86_64-pc-linux-gnu [SSL (OpenSSL)] [LZO] [EPOLL] [PKCS11] [eurephia] [MH]
    [IPv6] built on Dec  1 2014

    Thu Oct 15 20:10:40 2015 WARNING: file ''/tmp/openvpn.txt'' is group or others
    accessible

    Thu Oct 15 20:10:40 2015 Control Channel Authentication: tls-auth using INLINE
    static key file

    Thu Oct 15 20:10:40 2015 Attempting to establish TCP connection with [AF_INET]10.0.0.10:993
    [nonblock]

    Thu Oct 15 20:10:41 2015 TCP connection established with [AF_INET]10.0.0.10:993

    Thu Oct 15 20:10:41 2015 TCPv4_CLIENT link local: [undef]

    Thu Oct 15 20:10:41 2015 TCPv4_CLIENT link remote: [AF_INET]10.0.0.10:993

    Thu Oct 15 20:10:41 2015 WARNING: this configuration may cache passwords in memory
    -- use the auth-nocache option to prevent this

    Thu Oct 15 20:10:46 2015 [server] Peer Connection Initiated with [AF_INET]10.0.0.10:993

    Thu Oct 15 20:10:48 2015 Options error: Unrecognized option or missing parameter(s)
    in [PUSH-OPTIONS]:3: dhcp (2.3.2)

    Thu Oct 15 20:10:48 2015 TUN/TAP device tun0 opened

    Thu Oct 15 20:10:48 2015 do_ifconfig, tt->ipv6=0, tt->did_ifconfig_ipv6_setup=0

    Thu Oct 15 20:10:48 2015 /sbin/ip link set dev tun0 up mtu 1500

    Thu Oct 15 20:10:48 2015 /sbin/ip addr add dev tun0 local 10.10.0.34 peer 10.10.0.33

    Thu Oct 15 20:10:48 2015 Initialization Sequence Completed

    '}
body: "<?xml version=\"1.0\"?>\n<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Strict//EN\"\
  \n    \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\">\n<html xmlns=\"http://www.w3.org/1999/xhtml\"\
  >\n<head>\n<meta http-equiv=\"Content-Type\" content=\"text/html;charset=utf-8\"\
  \ />\n<title>This is a Tor Exit Router</title>\n\n<!--\n\nThis notice is intended\
  \ to be placed on a virtual host for a domain that\nyour Tor exit node IP reverse\
  \ resolves to so that people who may be about\nto file an abuse complaint would\
  \ check it first before bothering you or\nyour ISP. Ex:\nhttp://tor-exit.yourdomain.org\
  \ or http://tor-readme.yourdomain.org.\n\nThis type of setup has proven very effective\
  \ at reducing abuse complaints\nfor exit node operators.\n\nThere are a few places\
  \ in this document that you may want to customize.\nThey are marked with FIXME.\n\
  \n-->\n\n</head>\n<body>\n\n<p style=\"text-align:center; font-size:xx-large; font-weight:bold\"\
  >This is a\nTor Exit Router</p>\n\n<p>\nMost likely you are accessing this website\
  \ because you had some issue with\nthe traffic coming from this IP. This router\
  \ is part of the <a\nhref=\"https://www.torproject.org/\">Tor Anonymity Network</a>,\
  \ which is\ndedicated to <a href=\"https://www.torproject.org/about/overview\">providing\n\
  privacy</a> to people who need it most: average computer users. This\nrouter IP\
  \ should be generating no other traffic, unless it has been\ncompromised.</p>\n\n\
  <p style=\"text-align:center\">\n<a href=\"https://www.torproject.org/about/overview\"\
  >\n<img src=\"how_tor_works_thumb.png\" alt=\"How Tor works\" style=\"border-style:none\"\
  />\n</a></p>\n\n<p>\nTor sees use by <a href=\"https://www.torproject.org/about/torusers\"\
  >many\nimportant segments of the population</a>, including whistle blowers,\njournalists,\
  \ Chinese dissidents skirting the Great Firewall and oppressive\ncensorship, abuse\
  \ victims, stalker targets, the US military, and law\nenforcement, just to name\
  \ a few.  While Tor is not designed for malicious\ncomputer users, it is true that\
  \ they can use the network for malicious ends.\nIn reality however, the actual amount\
  \ of <a\nhref=\"https://www.torproject.org/docs/faq-abuse\">abuse</a> is quite low.\
  \ This\nis largely because criminals and hackers have significantly better access\
  \ to\nprivacy and anonymity than do the regular users whom they prey upon. Criminals\n\
  can and do <a\nhref=\"http://voices.washingtonpost.com/securityfix/2008/08/web_fraud_20_tools.html\"\
  >build,\nsell, and trade</a> far larger and <a\nhref=\"http://voices.washingtonpost.com/securityfix/2008/08/web_fraud_20_distributing_your.html\"\
  >more\npowerful networks</a> than Tor on a daily basis. Thus, in the mind of this\n\
  operator, the social need for easily accessible censorship-resistant private,\n\
  anonymous communication trumps the risk of unskilled bad actors, who are\nalmost\
  \ always more easily uncovered by traditional police work than by\nextensive monitoring\
  \ and surveillance anyway.</p>\n\n<p>\nIn terms of applicable law, the best way\
  \ to understand Tor is to consider it a\nnetwork of routers operating as common\
  \ carriers, much like the Internet\nbackbone. However, unlike the Internet backbone\
  \ routers, Tor routers\nexplicitly do not contain identifiable routing information\
  \ about the source of\na packet, and no single Tor node can determine both the origin\
  \ and destination\nof a given transmission.</p>\n\n<p>\nAs such, there is little\
  \ the operator of this router can do to help you track\nthe connection further.\
  \ This router maintains no logs of any of the Tor\ntraffic, so there is little that\
  \ can be done to trace either legitimate or\nillegitimate traffic (or to filter\
  \ one from the other).  Attempts to\nseize this router will accomplish nothing.</p>\n\
  \n<!-- FIXME: May or may not be US-only. Some non-US tor nodes have in\n     fact\
  \ reported DMCA harassment... -->\n\n<p>\nIf you are a representative of a company\
  \ who feels that this router is being\nused to violate the DMCA, please be aware\
  \ that this machine does not host or\ncontain any illegal content. Also be aware\
  \ that network infrastructure\nmaintainers are not liable for the type of content\
  \ that passes over their\nequipment, in accordance with <a\nhref=\"http://www.law.cornell.edu/uscode/text/17/512\"\
  >DMCA\n\"safe harbor\" provisions</a>. In other words, you will have just as much\
  \ luck\nsending a takedown notice to the Internet backbone providers. Please consult\n\
  <a href=\"https://www.torproject.org/eff/tor-dmca-response\">EFF's prepared\nresponse</a>\
  \ for more information on this matter.</p>\n\n<p>For more information, please consult\
  \ the following documentation:</p>\n\n<ol>\n<li><a href=\"https://www.torproject.org/about/overview\"\
  >Tor Overview</a></li>\n<li><a href=\"https://www.torproject.org/docs/faq-abuse\"\
  >Tor Abuse FAQ</a></li>\n<li><a href=\"https://www.torproject.org/eff/tor-legal-faq\"\
  >Tor Legal FAQ</a></li>\n</ol>\n\n<p>\nThat being said, if you still have a complaint\
  \ about the router,  you may\nemail the <a href=\"mailto:tor@openvpnconfigfile.ie\">maintainer</a>.\
  \ If\ncomplaints are related to a particular service that is being abused, I will\n\
  consider removing that service from my exit policy, which would prevent my\nrouter\
  \ from allowing that traffic to exit through it. I can only do this on an\nIP+destination\
  \ port basis, however. Common P2P ports are\nalready blocked.</p>\n\n<p>\nYou also\
  \ have the option of blocking this IP address and others on\nthe Tor network if\
  \ you so desire. The Tor project provides a <a\nhref=\"https://check.torproject.org/cgi-bin/TorBulkExitList.py\"\
  >web service</a>\nto fetch a list of all IP addresses of Tor exit nodes that allow\
  \ exiting to a\nspecified IP:port combination, and an official <a\nhref=\"https://www.torproject.org/tordnsel/dist/\"\
  >DNSRBL</a> is also available to\ndetermine if a given IP address is actually a\
  \ Tor exit server. Please\nbe considerate\nwhen using these options. It would be\
  \ unfortunate to deny all Tor users access\nto your site indefinitely simply because\
  \ of a few bad apples.</p>\n\n<p style=\"text-align:center; margin-bottom: 0.5em\"\
  >Exit Node provided by:<p>\n<h2 style=\"text-align: center\"><a style=\"color: black\"\
  \ href=\"http://www.openvpnconfigfile.ie\">DU Pirate Party</a><h2>\n\n</body>\n</html>\n"
input: null
success: true
test_runtime: 8.374207019805908
test_start_time: 1444925440.0
...
```

## Expected Post-processing efforts

# Privacy considerations

OpenVPN does not seek to provide anonymity. 
An adversary can observe that a user is connecting to OpenVPN servers.
OpenVPN servers can also determine the users location.

# Packet capture considerations

This test does not capture packets by default.

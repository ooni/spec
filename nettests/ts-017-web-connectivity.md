# Specification version number

2019-08-14-001

# Specification name

Web connectivity

# Test preconditions

* An internet connection

* The ability to reach the web consistency test helper

# Expected impact

Ability to detect if the websites being tested are reachable and if not what is
the reason for them not being reachable.

# Expected inputs

A list of URLs to be tested.

## Semantics

One URL per line:

http://example-1.com/
http://example-2.com/path1/
http://example-3.com/path2/

# Test description

This test is divided into multiple steps that will each test a different aspect
related to connectivity of the website in question.

The first step is to inform the web_connectivity test helper of our intention
to run the measurement against the URL in question and hence have it perform a
control measurement from an un-censored vantage point.

The control measurement shall include in the response the following information:

* The list of A records for a DNS query related to the hostname in question

* Wether or not it is able to establish a TCP session to the first A record in
  the DNS response

* The body length of the result of a HTTP GET request for the path in question

The request for the control measurement and the experiment measurements can run
in parallel, that is it is not a requirement to running the experiments to
already have the result of the control measurement since the comparison of the
control and experiment is done at the end.

The experiment itself consists of the following steps:

1. **Resolver identification**
   Determine what is the default resolver being used by the probe by performing
   an A lookup for a special domain that will contain in the A lookup answer
   section the IP of the resolver of the requester.
   An example of this is the service whoami.akamai.com, but also a specialised
   test-helper may be used.
   The result of this will be stored inside of the "client_resolver" key of the
   report.

2. **DNS lookup**
   Perform an A query to the default resolver for the hostname of the URL to be
   tested.
   Record the list of A records in a list inside the report under the key "ips".

3. **TCP connect**
   Attempt to establish a TCP session on port 80 for the list of IPs identified
   at step 2. If the URL begins with HTTPS then also establish a TCP session
   towards port 443.

4. **HTTP GET request**
   Perform a HTTP GET request for the path specified in the URI and record the
   response.
   The headers sent in the request shall be:
    **User-Agent**: `Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36`
    Corresponding to the most popular version (47.0.2526.106) of the most
    popular browser (Chrome) on the most popular OS (Windows 7).

5. **Control comparison**
   We then begin to poll the test-helper to learn if the control measurement
   has been performed. Once we obtain a result from the test-helper we shall do
   the following comparisons:

   * Are the DNS responses from the control consistent with those from the
     probe?
     The value of the report key "dns_consistency" can be the one of the following:

        * 'consistent' if the IP addresses of the A lookup from the control
          match exactly those of the experiment.

        * 'reverse_match' if the reverse lookup for any of the IPs in the DNS
          answer match (a match is defined as having any the domain.tld section
          in common).

        * 'inconsistent' if none of the above conditions are met.

    * Did we succeed in establishing a TCP session to the IP:port combinations
      found by doing A lookups?
      The value of the report key "tcp_connect" will be a list with 1 item per
      IP:port combination with the following values in each entry:

        * 'ip' the IP address a connection was attempted to be established to.

        * 'port' the port number we connected to.

        * 'status': {
            'success': boolean flag indicating if the connection attempt was successful (true) or failed (false),
            'failure': an error string indicating the reason for the failure,
            'blocked': boolean flag to indicate if blocking is happening on a
            TCP basis, this is determined by comparing the tcp_connect result
            from the control to that of the experiment. For example if both the
            control and the experiment produce a failure that host is assumed
            to be offline and hence no blocking is occurring, while if the
            experiment demonstrates an offline status, while the control
            succeeds we assume blocking is occuring.
        }

    * Does the body length of the experiment match that of the control?
      The value of the report key "body_length_match" is set to true if
      body_length_control/body_length_experiment > 0.7, null if we failed to
      connect, false if body_length_control/body_length_experiment < 0.7.

    * Do the HTTP headers match for the control and the experiment?
      The value of the report key "headers_match" is set to false if the header
      names are not consistent with the control request.

    * Does the HTTP status code match between the control and the experiment?
      The report key "status_code_match" is set to false if the status code
      of the experiment is inconsistent with the control.

    * Does the HTML title tag match between the control and experiment?
      The report key "title_match" is set to false if the first word in the title
      is longer than 5 characters and matches the first word in the title tag of
      the experiment.

6. **Reason for blocking**

The report key **blocking** is used to identify the reason for blocking. This
can be one of "tcp_ip", "dns" or "http".

It will be set to "dns" if the DNS query answers are inconsistent and when
doing the HTTP request we don't get the expected page
`((headers_match == false and body_length_match == false) or status_code_match == false)`.

Moreover "dns" will be the reason for blocking when doing the HTTP request we
get a failure of type "dns_lookup_error".

It will be set to "tcp_ip" when the DNS query answers are consistent, but we
have failed to connect to the IP:PORT combinations that have been resolved in
the experiment, while the control has succeeded. Moreover the HTTP request must
have failed.

It will be set to "http" when DNS resolutions are consistent and we are able to
establish a TCP connection to the IP ports of the control, but the HTTP request
either fails or we get back a HTTP response that contains a page we don't expect.

# Expected output

## Semantics

```
{
    "client_resolver": "xxx.xxx.xxx.xxx",
    "dns_consistency": "consistent" | "reverse_match" | "inconsistent",
    "body_length_match": true | false | null,
    "headers_match": true | false | null,
    "status_code_match": true | false | null,
    "title_match": true | false | null,
    "tcp_connect": [
        {
            "ip": "xxx.xxx.xxx.xxx",
            "port": 80 | 443,
            "status": {
                "success": true | false,
                "failure": "FAILURE STRING",
                "blocked": true | false | null
            }
        }
    ],
    "accessible": true | false | null,
    "blocking": "tcp_ip" | "dns" | "http-diff" | "http-failure" | null
}
```

The meaning of the keys "dns_consistency", "body_length_match" and
"tcp_connect" is described above.

The flag "accessible" indicates if the site in question is overall considered to be 
accessible (DNS responses are consistent, at least one TCP connection succeeds
and the expected HTTP response is received).

The flag "blocking" is set to null if "accessible" is true, otherwise it
indicates the reason for blocking, if that is due to inconsistent DNS
responses (dns), TCP/IP based blocking (tcp_ip), if the HTTP page response
matches with the control (http-diff) or if the HTTP response failed
(http-failure).

## Possible conclusions

* If the URL in question is accessible from the network vantage point of the probe.

* If the blocking of the URL in question is being performed by means of DNS
  tampering, TCP connection RST/IP blocking or by having a transparent HTTP
  proxy.

## Example output sample

```
{
    "annotations": null,
    "data_format_version": "0.2.0",
    "id": "6fee0dc8-2667-4378-bf88-e16bd19076e2",
    "input": "http://torproject.org/",
    "input_hashes": [],
    "measurement_start_time": "2016-05-23 11:10:46",
    "options": [
        "--url",
        ""
    ],
    "probe_asn": "AS3320",
    "probe_cc": "DE",
    "probe_city": null,
    "probe_ip": "127.0.0.1",
    "report_id": "20160523T110452Z_AS3320_s5kaXylbGbGXUyTAE6WR93zqatpmZD1K8GIwlJvxiq6IygRrrK",
    "software_name": "ooniprobe",
    "software_version": "1.4.2",
    "test_helpers": {
        "backend": {
            "address": "httpo://ckjj3ra6456muu7o.onion",
            "type": "onion"
        }
    },
    "test_keys": {
        "accessible": true,
        "agent": "redirect",
        "blocking": false,
        "body_length_match": true,
        "body_proportion": 1.0,
        "client_resolver": "74.125.18.24",
        "control": {
            "dns": {
                "failure": null,
                "ips": [
                    "82.195.75.101",
                    "138.201.14.197",
                    "154.35.132.70",
                    "86.59.30.40",
                    "93.95.227.222"
                ]
            },
            "http_request": {
                "body_length": 14539,
                "failure": null,
                "headers": {
                    "Accept-Ranges": "bytes",
                    "Cache-Control": "max-age=43200",
                    "Content-Language": "en",
                    "Content-Location": "index.html.en",
                    "Content-Type": "text/html",
                    "Date": "Mon, 23 May 2016 11:10:49 GMT",
                    "ETag": "\"38cb-5336fc9591c00-gzip\"",
                    "Expires": "Mon, 23 May 2016 23:10:49 GMT",
                    "Last-Modified": "Sun, 22 May 2016 15:14:56 GMT",
                    "Server": "Apache",
                    "Strict-Transport-Security": "max-age=15768000",
                    "Tcn": "choice",
                    "Vary": "negotiate,Accept-Encoding",
                    "X-Content-Type-Options": "nosniff",
                    "X-Frame-Options": "sameorigin",
                    "X-XSS-Protection": "1"
                },
                "status_code": 200
            },
            "tcp_connect": {
                "138.201.14.197:80": {
                    "failure": null,
                    "status": true
                },
                "154.35.132.70:80": {
                    "failure": null,
                    "status": true
                },
                "82.195.75.101:80": {
                    "failure": null,
                    "status": true
                },
                "86.59.30.40:80": {
                    "failure": null,
                    "status": true
                },
                "93.95.227.222:80": {
                    "failure": null,
                    "status": true
                }
            }
        },
        "control_failure": null,
        "dns_consistency": "consistent",
        "dns_experiment_failure": null,
        "headers_match": true,
        "http_experiment_failure": null,
        "queries": [
            {
                "answers": [
                    {
                        "answer_type": "A",
                        "ipv4": "93.95.227.222"
                    },
                    {
                        "answer_type": "A",
                        "ipv4": "82.195.75.101"
                    },
                    {
                        "answer_type": "A",
                        "ipv4": "138.201.14.197"
                    },
                    {
                        "answer_type": "A",
                        "ipv4": "86.59.30.40"
                    },
                    {
                        "answer_type": "A",
                        "ipv4": "154.35.132.70"
                    }
                ],
                "failure": null,
                "hostname": "torproject.org",
                "query_type": "A",
                "resolver_hostname": null,
                "resolver_port": null
            }
        ],
        "requests": [
            {
                "failure": null,
                "request": {
                    "body": null,
                    "headers": {
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                        "Accept-Language": "en-US;q=0.8,en;q=0.5",
                        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"
                    },
                    "method": "GET",
                    "tor": {
                        "exit_ip": null,
                        "exit_name": null,
                        "is_tor": false
                    },
                    "url": "http://torproject.org/"
                },
                "response": {
                    "body": "<!DOCTYPE html>\n <html>\n <head>\n   <meta charset=\"utf-8\">\n   <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">\n   <meta name=\"viewport\" content=\"width=\"device-width,\" initial-scale=1\">\n   <meta name=\"author\" content=\"The Tor Project, Inc.\">\n   <meta name=\"keywords\" content=\"anonymity online, tor, tor project, censorship circumvention, traffic analysis, anonymous communications research\">\n   <meta property=\"og:image\" content=\"https://www.torproject.org/images/tor-logo.jpg\">\n   <title>Tor Project: Anonymity Online</title>\n   <link rel=\"icon\" href=\"./images/favicon.ico\">\n   <link href=\"./css/master.css\" rel=\"stylesheet\">\n   <!--[if lte IE 8]>\n   <link href=\"./css/ie8-and-down.css\" rel=\"stylesheet\">\n   <![endif]-->\n   <!--[if lte IE 7]>\n   <link href=\"./css/ie7-and-down.css\" rel=\"stylesheet\">\n   <![endif]-->\n   <!--[if IE 6]>\n   <link href=\"./css/ie6.css\" rel=\"stylesheet\">\n   <![endif]-->\n</head>\n<body>\n<div id=\"wrap\">\n  <div id=\"header\">\n    <h1 id=\"logo\"><a href=\"index.html.en\">Tor</a></h1>\n      <div id=\"nav\">\n        <ul>\n        <li><a class=\"active\" href=\"index.html.en\">Home</a></li>\n<li><a href=\"about/overview.html.en\">About Tor</a></li>\n<li><a href=\"docs/documentation.html.en\">Documentation</a></li>\n<li><a href=\"press/press.html.en\">Press</a></li>\n<li><a href=\"https://blog.torproject.org/blog/\">Blog</a></li>\n<li><a href=\"about/contact.html.en\">Contact</a></li>\n        </ul>\n      </div>\n      <!-- END NAV -->\n      <div id=\"calltoaction\">\n        <ul>\n          <li class=\"donate\"><a href=\"download/download-easy.html.en\">Download</a></li>\n<li class=\"donate\"><a href=\"getinvolved/volunteer.html.en\">Volunteer</a></li>\n<li class=\"donate\"><a href=\"donate/donate-button.html.en\">Donate</a></li>\n        </ul>\n      </div>\n      <!-- END CALLTOACTION -->\n  </div>\n  <!-- END HEADER -->\n<div id=\"home\">\n    <div id=\"content\" class=\"clearfix\">\n    \t<div id=\"maincol\">\n      \t<div id=\"banner\">\n        \t<ul>\n          \t<li>Tor prevents people from learning your location or browsing habits.</li>\n            <li>Tor is for web browsers, instant messaging clients, and more.</li>\n            <li>Tor is free and open source for Windows, Mac, Linux/Unix, and Android</li>\n          </ul>\n        \t<h1 class=\"headline\">Anonymity Online</h1>\n          <p class=\"desc\">Protect your privacy. Defend yourself against network surveillance and traffic analysis.</p>\n      <div id=\"download\">\n        <a href=\"download/download-easy.html.en\">\n          <span class=\"download-tor\">Download Tor</span></a>\n      </div>\n      </div>\n        <div class=\"subcol-container clearfix\">\n          <div class=\"subcol first\">\n            <h2>What is Tor?</h2> <p>Tor is free software and an open\n            network that helps you defend against traffic analysis,\n            a form of network surveillance that\n            threatens personal freedom and privacy, confidential business\n            activities and relationships, and state security.<br>\n            <span class=\"continue\"><a href=\"about/overview.html.en\">Learn\n            more about Tor &raquo;</a></span></p>\n          </div>\n          <!-- END SUBCOL -->\n          <div class=\"subcol\">\n          <h2>Why Anonymity Matters</h2>\n          <p>Tor protects you by bouncing your communications around a\n          distributed network of relays run by volunteers all around\n          the world: it prevents somebody watching your Internet\n          connection from learning what sites you visit, and it prevents\n          the sites you visit from learning your physical location.<br>\n          <span class=\"continue\"><a href=\"getinvolved/volunteer.html.en\">Get involved with Tor\n          &raquo;</a></span></p>\n          </div>\n        </div>\n        <!-- END SUBCOL -->\n        <div id=\"home-our-projects\" class=\"clearfix\">\n          <h2>Our Projects</h2>\n          <div class=\"fauxhead\"></div>\n          <table style=\"table-layout: fixed;\" summary=\"\">\n            <tr>\n              <!-- Icon from the Crystal set\n                author: Everaldo Coelho\n                source: http://www.everaldo.com/crystal/\n                license: LGPL v2\n              -->\n              <td>\n                <div class=\"project\">\n                <a href=\"projects/torbrowser.html.en\"><img\n                src=\"./images/icon-TorBrowser.jpg\" alt=\"TorBrowser Icon\" width=\"75\" height=\"75\"></a>\n                <h3><a href=\"projects/torbrowser.html.en\">Tor\n                Browser</a></h3>\n                <p>Tor Browser contains everything you need to safely\n                browse the Internet.</p>\n                </div>\n              </td>\n              <td>\n                <div class=\"project\">\n                <a href=\"https://guardianproject.info/apps/orbot/\"><img\n                src=\"./images/icon-Orbot.jpg\" alt=\"Orbot Icon\" width=\"75\" height=\"75\"></a>\n                <h3><a href=\"https://guardianproject.info/apps/orbot/\">Orbot</a></h3>\n                <p>Tor for Google Android devices.</p>\n                </div>\n              </td>\n            </tr>\n            <tr>\n              <td>\n                <div class=\"project\">\n                <a href=\"https://tails.boum.org/\"><img src=\"./images/tails_logo.png\" alt=\"Tails Logo\" width=\"75\" height=\"75\"></a>\n                <h3><a href=\"https://tails.boum.org/\">Tails</a></h3>\n                <p>Live CD/USB operating system preconfigured to use\n                Tor safely.</p>\n                </div>\n              </td>\n              <!-- Icon from the Crystal set\n              author: Everaldo Coelho\n              source: http://www.everaldo.com/crystal/\n              license: LGPL v2\n              -->\n              <td>\n                <div class=\"project\">\n                <a href=\"https://www.atagar.com/arm/\"><img\n                src=\"./images/icon-Arm.jpg\" alt=\"Arm Icon\" width=\"75\" height=\"75\"></a>\n                <h3><a href=\"https://www.atagar.com/arm/\">Arm</a></h3>\n                <p>Terminal (command line) application for monitoring\n                and configuring Tor.</p>\n                </div>\n              </td>\n            </tr>\n            <tr>\n                <!-- Icon from the NuoveXT 2 set\n                author: Alexandre Moore\n                source: http://nuovext.pwsp.net/\n                license: LGPL v3\n                -->\n\t      <td>\n              <div class=\"project\">\n                <a href=\"https://atlas.torproject.org/\"><img\n                src=\"./images/icon-TorStatus.jpg\" alt=\"Atlas Icon\" width=\"75\" height=\"75\"></a>\n                <h3><a href=\"https://atlas.torproject.org/\">Atlas</a></h3>\n                <p>Site providing an overview of the Tor network.</p>\n                </div>\n              </td>\n                <!-- Obfsproxy Icon\n                author: Constantinos Crystallidis\n                license: Creative Commons Attribution-ShareAlike 2.0 Generic (CC BY-SA 2.0)\n                -->\n              <td>\n                <div class=\"project\">\n                <a href=\"projects/obfsproxy.html.en\"><img\n                src=\"./images/icon-Obfsproxy.jpg\" alt=\"Pluggable Transports Icon\" width=\"75\" height=\"75\"></a>\n                <h3><a href=\"docs/pluggable-transports.html.en\">Pluggable Transports</a></h3>\n                <p>Pluggable transports help you circumvent censorship.</p>\n                </div>\n              </td>\n            </tr>\n            <tr>\n              <td>\n               <div class=\"project\">\n              <a href=\"https://stem.torproject.org/\"><img\n              src=\"./images/icon-stem.jpg\" alt=\"Stem Icon\" width=\"75\" height=\"75\"></a>\n              <h3><a href=\"https://stem.torproject.org/\">Stem</a></h3>\n              <p>Library for writing scripts and applications that interact\n              with Tor.</p>\n                </div>\n              </td>\n              <td>\n               <div class=\"project\">\n              <a href=\"https://ooni.torproject.org/\"><img\n              src=\"./images/icon-OONI.png\" alt=\"OONI\" width=\"75\" height=\"75\"></a>\n               <h3><a href=\"https://ooni.torproject.org/\">OONI</a></h3>\n               <p>Global observatory monitoring for network censorship.</p>\n               </div>\n               </td>\n            </tr>\n          </table>\n\t  <span class=\"continue\"><a href=\"projects/projects.html.en\">Learn more about our projects &raquo;</a></span>\n      \t</div>\n        <!-- END TABLE -->\n      </div>\n      <!-- END MAINCOL -->\n      <div id=\"sidecol\">\n      <!-- BLOG WIDGET -->\n<div class='blogFeed'>\n  <div class='blogFirstRow'>\n  <h2>Recent Blog Posts</h2>\n  </div><div class=\"fauxhead\"></div><a href='https://blog.torproject.org/blog/tor-project-hiring-developer-ooni' title='The Tor Project is Hiring a Developer for OONI! '><div class='blogRow blogRow0'><p class='blogTitle'>The Tor Project is Hiring a Deve...</p>\n      <p class='blogDate'>Tue, 17 May 2016</p>\n      <p class='blogAuthor'>Posted by: <em>art</em></p>\n      </div>\n      </a><a href='https://blog.torproject.org/blog/tracking-impact-whatsapp-blockage-tor' title='Tracking The Impact of the WhatsApp Blockage on Tor'><div class='blogRow blogRow1'><p class='blogTitle'>Tracking The Impact of the Whats...</p>\n      <p class='blogDate'>Mon, 16 May 2016</p>\n      <p class='blogAuthor'>Posted by: <em>isabela</em></p>\n      </div>\n      </a><a href='https://blog.torproject.org/blog/gsoc-2016-projects' title='GSoC 2016 Projects'><div class='blogRow blogRow0'><p class='blogTitle'>GSoC 2016 Projects</p>\n      <p class='blogDate'>Sat, 07 May 2016</p>\n      <p class='blogAuthor'>Posted by: <em>atagar</em></p>\n      </div>\n      </a><a href='https://blog.torproject.org/blog/tor-browser-60a5-hardened-released' title='Tor Browser 6.0a5-hardened is released'><div class='blogRow blogRow1'><p class='blogTitle'>Tor Browser 6.0a5-hardened is re...</p>\n      <p class='blogDate'>Thu, 28 Apr 2016</p>\n      <p class='blogAuthor'>Posted by: <em>boklm</em></p>\n      </div>\n      </a><a href='https://blog.torproject.org/blog/tor-browser-60a5-released' title='Tor Browser 6.0a5 is released'><div class='blogRow blogRow0'><p class='blogTitle'>Tor Browser 6.0a5 is released</p>\n      <p class='blogDate'>Thu, 28 Apr 2016</p>\n      <p class='blogAuthor'>Posted by: <em>boklm</em></p>\n      </div>\n      </a><a href='https://blog.torproject.org' title='Tor Blog Home'>\n<div class='blogRow blogLastRow'>\n<p>View all blog posts &raquo;</p>\n</div>\n</a>\n      <!-- END BLOG WIDGET -->\n      \t<div id=\"home-users\">\n          <h2>Who Uses Tor?</h2>\n\t  <div class=\"fauxhead\"></div>\n          <div class=\"user\">\n            <h3>\n              <a href=\"about/torusers.html.en#normalusers\"><img src=\"./images/family.jpg\" alt=\"Normal People\" width=\"75\" height=\"75\">Family &amp; Friends</a>\n            </h3>\n            <p>People like you and your family use Tor to protect themselves, their children, and their dignity while using the Internet.</p>\n          </div>\n          <div class=\"user\">\n            <h3>\n              <a href=\"about/torusers.html.en#executives\"><img src=\"./images/consumers.jpg\" alt=\"Businesses\" width=\"75\" height=\"75\">Businesses</a>\n            </h3>\n            <p>Businesses use Tor to research competition, keep business strategies confidential, and facilitate internal accountability.</p>\n          </div>\n          <div class=\"user\">\n            <h3>\n              <a href=\"about/torusers.html.en#activists\"><img src=\"./images/activists.jpg\" alt=\"Activists &amp; Whistleblowers\" width=\"75\" height=\"75\">Activists</a>\n            </h3>\n            <p>Activists use Tor to anonymously report abuses from danger zones. Whistleblowers use Tor to safely report on corruption.</p>\n          </div>\n          <div class=\"user\">\n            <h3>\n              <a href=\"about/torusers.html.en#journalist\"><img src=\"./images/media.jpg\" alt=\"Journalists and the Media\" width=\"75\" height=\"75\">Media</a>\n            </h3>\n            <p>Journalists and the media use Tor to protect their research and sources online.</p>\n          </div>\n          <div class=\"user\">\n            <h3>\n              <a href=\"about/torusers.html.en#military\"><img src=\"./images/military.jpg\" alt=\"Military and Law Enforcement\" width=\"75\" height=\"75\">Military &amp; Law Enforcement</a>\n            </h3>\n            <p>Militaries and law enforcement use Tor to protect their communications, investigations, and intelligence gathering online.</p>\n          </div>\n        </div>\n        <!-- END TABLE -->\n      </div>\n      <!-- END SIDECOL -->\n    </div>\n    <!-- END CONTENT -->\n  </div>\n  <!-- END HOME -->\n    <div id=\"footer\">\n    \t<div class=\"onion\"><img src=\"./images/onion.jpg\" alt=\"Tor\" width=\"78\" height=\"118\"></div>\n      <div class=\"about\">\n    <p>Trademark, copyright notices, and rules for use by third parties can be found\n    <a href=\"docs/trademark-faq.html.en\">in our FAQ</a>.</p>\n<!--\n        Last modified: Sat May 21 14:41:08 2016 -0400\n        Last compiled: Sun May 22 2016 15:14:55 +0000\n-->\n      </div>\n      <!-- END ABOUT -->\n      <div class=\"col first\">\n      \t<h4>About Tor</h4>\n        <ul>\n          <li><a href=\"about/overview.html.en\">What Tor Does</a></li>\n          <li><a href=\"about/torusers.html.en\">Users of Tor</a></li>\n          <li><a href=\"about/corepeople.html.en\">Core Tor People</a></li>\n          <li><a href=\"about/sponsors.html.en\">Sponsors</a></li>\n          <li><a href=\"about/contact.html.en\">Contact Us</a></li>\n        </ul>\n      </div>\n      <!-- END COL -->\n      <div class=\"col\">\n      \t<h4>Get Involved</h4>\n        <ul>\n          <li><a href=\"donate/donate.html.en\">Donate</a></li>\n          <li><a href=\"docs/documentation.html.en#MailingLists\">Mailing Lists</a></li>\n          <li><a href=\"docs/hidden-services.html.en\">Hidden Services</a></li>\n          <li><a href=\"getinvolved/translation.html.en\">Translations</a></li>\n        </ul>\n      </div>\n      <!-- END COL -->\n      <div class=\"col\">\n      \t<h4>Documentation</h4>\n        <ul>\n          <li><a href=\"docs/tor-manual.html.en\">Manuals</a></li>\n          <li><a href=\"docs/documentation.html.en\">Installation Guides</a></li>\n          <li><a href=\"https://trac.torproject.org/projects/tor/wiki/\">Tor Wiki</a></li>\n          <li><a href=\"docs/faq.html.en\">General Tor FAQ</a></li>\n        </ul>\n      </div>\n        <div class=\"col\">\n        <a href=\"https://internetdefenseleague.org/\"><img src=\"./images/InternetDefenseLeague-footer-badge.png\" alt=\"Internet Defense League\" width=\"125\" height=\"125\"></a>\n        </div>\n      <!-- END COL -->\n    </div>\n    <!-- END FOOTER -->\n  </div>\n  <!-- END WRAP -->\n</body>\n</html>\n",
                    "code": 200,
                    "headers": {
                        "Accept-Ranges": "bytes",
                        "Cache-Control": "max-age=43200",
                        "Content-Language": "en",
                        "Content-Location": "index.html.en",
                        "Content-Type": "text/html",
                        "Date": "Mon, 23 May 2016 11:10:47 GMT",
                        "ETag": "\"38cb-5336fc9591c00-gzip\"",
                        "Expires": "Mon, 23 May 2016 23:10:47 GMT",
                        "Last-Modified": "Sun, 22 May 2016 15:14:56 GMT",
                        "Server": "Apache",
                        "Strict-Transport-Security": "max-age=15768000",
                        "TCN": "choice",
                        "Vary": "negotiate,Accept-Encoding",
                        "X-Content-Type-Options": "nosniff",
                        "X-Frame-Options": "sameorigin",
                        "X-Xss-Protection": "1"
                    }
                }
            },
            {
                "failure": null,
                "request": {
                    "body": null,
                    "headers": {
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                        "Accept-Language": "en-US;q=0.8,en;q=0.5",
                        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"
                    },
                    "method": "GET",
                    "tor": {
                        "exit_ip": null,
                        "exit_name": null,
                        "is_tor": false
                    },
                    "url": "http://torproject.org/"
                },
                "response": {
                    "body": null,
                    "code": 302,
                    "headers": {
                        "Content-Type": "text/html; charset=iso-8859-1",
                        "Date": "Mon, 23 May 2016 11:10:47 GMT",
                        "Location": "https://www.torproject.org/",
                        "Server": "Apache",
                        "X-Content-Type-Options": "nosniff",
                        "X-Frame-Options": "sameorigin",
                        "X-Xss-Protection": "1"
                    }
                }
            }
        ],
        "socksproxy": null,
        "status_code_match": true,
        "tcp_connect": [
            {
                "ip": "82.195.75.101",
                "port": 80,
                "status": {
                    "blocked": false,
                    "failure": null,
                    "success": true
                }
            },
            {
                "ip": "138.201.14.197",
                "port": 80,
                "status": {
                    "blocked": false,
                    "failure": null,
                    "success": true
                }
            },
            {
                "ip": "86.59.30.40",
                "port": 80,
                "status": {
                    "blocked": false,
                    "failure": null,
                    "success": true
                }
            },
            {
                "ip": "93.95.227.222",
                "port": 80,
                "status": {
                    "blocked": false,
                    "failure": null,
                    "success": true
                }
            },
            {
                "ip": "154.35.132.70",
                "port": 80,
                "status": {
                    "blocked": false,
                    "failure": null,
                    "success": true
                }
            }
        ]
    },
    "test_name": "web_connectivity",
    "test_runtime": 20.532310009002686,
    "test_start_time": "2016-05-23 11:10:45",
    "test_version": "0.1.0"
}
```

# Privacy considerations

If the client has opted out of providing the ASN of their probe the
client_resolver key may give away extra information pertaining to the network
they are on if they are using the resolver of their ISP.

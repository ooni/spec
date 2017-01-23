# Specification version number

0.2.0

# Specification name

Captive portal test.

# Test preconditions

  * An association to a captive portal.

# Expected impact

The ability to detect a captive portal.

# Test description

The test is split in four smaller tests:

    1. Http test that compares a requested document against the control one (vendor_tests).
    2. DNS test that checks a NXDOMAIN response to random hostnames requests (part of the vendor_dns_tests).
    3. DNS test that compares an A request to a static domain against its IP (part of the vendor_dns_tests).
    4. DNS test that check for 0x20 encoding (check0x20 tests).

# Expected output

Relevant data to think about the existence of a captive portal grouped between the http and dns tests.

## Parent data format

df-001-httpt

df-002-dnst

## Required output data

  * The result of the http tests
  * The result of the dns tests
  * The result of the 0x20 encoding tests

## Semantics

In addition to the data specified in the parent data format, the following fields are added to the report.

Version 0.2:

```
{
   "vendor_dns_tests": {
      "google_dns_cp": [
            "IP address(es) of the random hostnames that don't resolve "
            "to NXDOMAIN"
       ],
      "ms_dns_cp": [
            "IP address of the requested domain name"
      ]
    },

    "vendor_tests": {
        "result": "true|false"
        "vt": [
            "URL",
            "http_status_summary",
            "http_status_number",
            "User_Agent",
            "name_test"
        ]
    },

    "check0x20": [
        ["name_match", "serial_match", "querynames", "answernames", "SOA_serials"]
    ]
}
```

Version 0.3:

```
{
    "vendor_dns_tests": {
        "google_dns_cp": {
            "result": "true|false"
            "addresses": [
                "IP address(es) of the random hostnames that don't resolve to NXDOMAIN"
            ]
        }
        "ms_dns_cp": {
            "result": "true|false"
            "address": "IP address of the requested domain name"
        }
    },

    "vendor_tests": {
        "MS HTTP Captive Portal": {
            "result": "true|false",
            "url": "string",
            "http_status_summary": "string",
            "http_status_number": "number",
            "User_Agent": "string"
        },
        "W3 Captive Portal": {
            "result": "true|false",
            "url": "string",
            "http_status_summary": "string",
            "http_status_number": "number",
            "User_Agent": "string"
        },
        "Apple HTTP Captive Portal": {
            "result": "true|false",
            "url": "string",
            "http_status_summary": "string",
            "http_status_number": "number",
            "User_Agent": "string"
        }
    },

    "check0x20": {
        "result": "true|false",
        "name_match": "true|false"
        "serial_match": "true|false"
        "querynames": ["domain names of requested hostnames"]
        "answernames": ["domain names of answered requests"]
        "SOA_serials": ["serials of the DNSs zones of the requested queries"]
    }

}
```

## Possible conclusions

  Whether or not the tester is under a captive portal.

## Example output sample

XXX update this

    ###########################################
    # OONI Probe Report for captiveportal (0.2)
    # Sun May 11 16:39:09 2014
    ###########################################
    ---
    input_hashes: []
    options: []
    probe_asn: AS0
    probe_cc: ES
    probe_city: null
    probe_ip: 127.0.0.1
    software_name: ooniprobe
    software_version: 1.0.2
    start_time: 1399826349.184915
    test_name: captiveportal
    test_version: '0.2'
    ...
    ---
    agent: agent
    check0x20:
    - true
    - true
    - [OoNI.Nu, OoNI.Nu, OoNI.Nu, OoNI.Nu, OoNI.Nu]
    - [OoNI.Nu, OoNI.Nu, OoNI.Nu, OoNI.Nu]
    - ['2014011200', '2014011200', '2014011200', '2014011200']
    input: null
    queries:
    - addrs: [131.107.255.255]
      answers:
      - [<RR name=dns.msftncsi.com type=A class=IN ttl=18s auth=False>, <A address=131.107.255.255
          ttl=18>]
      query: '[Query(''dns.msftncsi.com'', 1, 1)]'
      query_type: A
      resolver: null
    - addrs: [dns2.registrar-servers.com, dns4.registrar-servers.com, dns5.registrar-servers.com,
        dns3.registrar-servers.com, dns1.registrar-servers.com]
      answers:
      - [<RR name=ooni.nu type=NS class=IN ttl=1800s auth=False>, <NS name=dns2.registrar-servers.com
          ttl=1800>]
      - [<RR name=ooni.nu type=NS class=IN ttl=1800s auth=False>, <NS name=dns4.registrar-servers.com
          ttl=1800>]
      - [<RR name=ooni.nu type=NS class=IN ttl=1800s auth=False>, <NS name=dns5.registrar-servers.com
          ttl=1800>]
      - [<RR name=ooni.nu type=NS class=IN ttl=1800s auth=False>, <NS name=dns3.registrar-servers.com
          ttl=1800>]
      - [<RR name=ooni.nu type=NS class=IN ttl=1800s auth=False>, <NS name=dns1.registrar-servers.com
          ttl=1800>]
      query: '[Query(''ooni.nu'', 2, 1)]'
      query_type: NS
      resolver: null
    - addrs: [208.64.122.244, 208.64.122.242]
      answers:
      - [<RR name=dns2.registrar-servers.com type=A class=IN ttl=580s auth=False>, <A
          address=208.64.122.244 ttl=580>]
      - [<RR name=dns2.registrar-servers.com type=A class=IN ttl=580s auth=False>, <A
          address=208.64.122.242 ttl=580>]
      query: '[Query(''dns2.registrar-servers.com'', 1, 1)]'
      query_type: A
      resolver: null
    - addrs: [173.245.58.17, 173.245.59.40, 173.245.58.45, 173.245.59.16]
      answers:
      - [<RR name=dns4.registrar-servers.com type=A class=IN ttl=1445s auth=False>, <A
          address=173.245.58.17 ttl=1445>]
      - [<RR name=dns4.registrar-servers.com type=A class=IN ttl=1445s auth=False>, <A
          address=173.245.59.40 ttl=1445>]
      - [<RR name=dns4.registrar-servers.com type=A class=IN ttl=1445s auth=False>, <A
          address=173.245.58.45 ttl=1445>]
      - [<RR name=dns4.registrar-servers.com type=A class=IN ttl=1445s auth=False>, <A
          address=173.245.59.16 ttl=1445>]
      query: '[Query(''dns4.registrar-servers.com'', 1, 1)]'
      query_type: A
      resolver: null
    - addrs: [208.64.122.244, 208.64.122.242]
      answers:
      - [<RR name=dns5.registrar-servers.com type=A class=IN ttl=1609s auth=False>, <A
          address=208.64.122.244 ttl=1609>]
      - [<RR name=dns5.registrar-servers.com type=A class=IN ttl=1609s auth=False>, <A
          address=208.64.122.242 ttl=1609>]
      query: '[Query(''dns5.registrar-servers.com'', 1, 1)]'
      query_type: A
      resolver: null
    - addrs: [69.197.21.28, 69.197.21.29]
      answers:
      - [<RR name=dns3.registrar-servers.com type=A class=IN ttl=602s auth=False>, <A
          address=69.197.21.28 ttl=602>]
      - [<RR name=dns3.registrar-servers.com type=A class=IN ttl=602s auth=False>, <A
          address=69.197.21.29 ttl=602>]
      query: '[Query(''dns3.registrar-servers.com'', 1, 1)]'
      query_type: A
      resolver: null
    - addrs: [173.245.59.16, 173.245.58.17, 173.245.58.45, 173.245.59.40]
      answers:
      - [<RR name=dns1.registrar-servers.com type=A class=IN ttl=816s auth=False>, <A
          address=173.245.59.16 ttl=816>]
      - [<RR name=dns1.registrar-servers.com type=A class=IN ttl=816s auth=False>, <A
          address=173.245.58.17 ttl=816>]
      - [<RR name=dns1.registrar-servers.com type=A class=IN ttl=816s auth=False>, <A
          address=173.245.58.45 ttl=816>]
      - [<RR name=dns1.registrar-servers.com type=A class=IN ttl=816s auth=False>, <A
          address=173.245.59.40 ttl=816>]
      query: '[Query(''dns1.registrar-servers.com'', 1, 1)]'
      query_type: A
      resolver: null
    - addrs:
      - [OoNI.Nu, 2014011200]
      answers:
      - [<RR name=OoNI.Nu type=SOA class=IN ttl=3601s auth=True>, <SOA mname=dns1.registrar-servers.com
          rname=hostmaster.registrar-servers.com serial=2014011200 refresh=3600 retry=1801
          expire=604800 minimum=3601 ttl=3601>]
      query: '[Query(''OoNI.Nu'', 6, 1)]'
      query_type: SOA
      resolver: [208.64.122.244, 53]
    - addrs:
      - [OoNI.Nu, 2014011200]
      answers:
      - [<RR name=OoNI.Nu type=SOA class=IN ttl=3601s auth=True>, <SOA mname=dns1.registrar-servers.com
          rname=hostmaster.registrar-servers.com serial=2014011200 refresh=3600 retry=1801
          expire=604800 minimum=3601 ttl=3601>]
      query: '[Query(''OoNI.Nu'', 6, 1)]'
      query_type: SOA
      resolver: [173.245.58.45, 53]
    - query: '[Query(''OoNI.Nu'', 6, 1)]'
      query_type: SOA
      resolver: [69.197.21.28, 53]
    - addrs:
      - [OoNI.Nu, 2014011200]
      answers:
      - [<RR name=OoNI.Nu type=SOA class=IN ttl=3601s auth=True>, <SOA mname=dns1.registrar-servers.com
          rname=hostmaster.registrar-servers.com serial=2014011200 refresh=3600 retry=1801
          expire=604800 minimum=3601 ttl=3601>]
      query: '[Query(''OoNI.Nu'', 6, 1)]'
      query_type: SOA
      resolver: [173.245.58.17, 53]
    - addrs:
      - [OoNI.Nu, 2014011200]
      answers:
      - [<RR name=OoNI.Nu type=SOA class=IN ttl=3601s auth=True>, <SOA mname=dns1.registrar-servers.com
          rname=hostmaster.registrar-servers.com serial=2014011200 refresh=3600 retry=1801
          expire=604800 minimum=3601 ttl=3601>]
      query: '[Query(''OoNI.Nu'', 6, 1)]'
      query_type: SOA
      resolver: [208.64.122.244, 53]
    requests:
    - request:
        body: null
        headers:
        - [User-Agent, 'Mozilla/5.0 (iPhone; U; CPU like Mac OS X; en) AppleWebKit/420+
            (KHTML, like Gecko) Version/3.0 Mobile/1A543a Safari/419.3']
        method: GET
        tor: {is_tor: false}
        url: http://www.apple.com/library/test/success.html
      response:
        body: <HTML><HEAD><TITLE>Success</TITLE></HEAD><BODY>Success</BODY></HTML>
        code: 200
        headers:
        - - Date
          - ['Sun, 11 May 2014 16:39:17 GMT']
        - - Content-Length
          - ['68']
        - - Content-Type
          - [text/html]
        - - Connection
          - [close]
    - request:
        body: null
        headers:
        - [User-Agent, 'Mozilla/5.0 (Windows NT 6.1; rv:5.0) Gecko/20100101 Firefox/5.0']
        method: GET
        tor: {is_tor: false}
        url: http://tools.ietf.org/html/draft-nottingham-http-portal-02
      response:
        body: "3e80\r\n<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Transitional//EN\"\
          \n  \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd\">\n<html xmlns=\"\
          http://www.w3.org/1999/xhtml\" xml:lang=\"en\" lang=\"en\">\n<head profile=\"\
          http://dublincore.org/documents/2008/08/04/dc-html/\">\n    <meta http-equiv=\"\
          Content-Type\" content=\"text/html; charset=utf-8\" />\n    <meta name=\"robots\"\
          \ content=\"index,follow\" />\n    <meta name=\"creator\" content=\"rfcmarkup\
          \ version 1.107\" />\n    <link rel=\"schema.DC\" href=\"http://purl.org/dc/elements/1.1/\"\
          \ />\n<meta name=\"DC.Identifier\" content=\"urn:ietf:id:nottingham-http-portal\"\
          \ />\n<meta name=\"DC.Description.Abstract\" content=\"&quot;Captive portals&quot;\
          \ are a commonly-deployed means of obtaining access\\ncredentials and/or payment\
          \ for a network. This memo introduces a new\\nHTTP status code as a means of\
          \ addressing issues found in these\\ndeployments.  This memo should be discussed\
          \ on the ietf-http-wg@w3.org\\nmailing list, although it is not a work item\
          \ of the HTTPbis WG.\" />\n<meta name=\"DC.Creator\" content=\"mnot &lt;mnot@mnot.net&gt;\"\
          \ />\n<meta name=\"DC.Date.Issued\" content=\"2011-02-17\" />\n<meta name=\"\
          DC.Title\" content=\"The Network Authentication Required HTTP Status Code\"\
          \ />\n\n    <link rel=\"icon\" href=\"/images/id.png\" type=\"image/png\" />\n\
          \    <link rel=\"shortcut icon\" href=\"/images/id.png\" type=\"image/png\"\
          \ />\n    <title>draft-nottingham-http-portal-02 - The Network Authentication\
          \ Required HTTP Status Code</title>\n    \n    \n    <style type=\"text/css\"\
          >\n\tbody {\n\t    margin: 0px 8px;\n            font-size: 1em;\n\t}\n    \
          \    h1, h2, h3, h4, h5, h6, .h1, .h2, .h3, .h4, .h5, .h6 {\n\t    font-weight:\
          \ bold;\n            line-height: 0pt;\n            display: inline;\n     \
          \       white-space: pre;\n            font-family: monospace;\n           \
          \ font-size: 1em;\n\t    font-weight: bold;\n        }\n        pre {\n    \
          \        font-size: 1em;\n            margin-top: 0px;\n            margin-bottom:\
          \ 0px;\n        }\n\t.pre {\n\t    white-space: pre;\n\t    font-family: monospace;\n\
          \t}\n\t.header{\n\t    font-weight: bold;\n\t}\n        .newpage {\n       \
          \     page-break-before: always;\n        }\n        .invisible {\n        \
          \    text-decoration: none;\n            color: white;\n        }\n        a.selflink\
          \ {\n          color: black;\n          text-decoration: none;\n        }\n\
          \        @media print {\n            body {\n                font-family: monospace;\n\
          \                font-size: 10.5pt;\n            }\n            h1, h2, h3,\
          \ h4, h5, h6 {\n                font-size: 1em;\n            }\n        \n \
          \           a:link, a:visited {\n                color: inherit;\n         \
          \       text-decoration: none;\n            }\n            .noprint {\n    \
          \            display: none;\n            }\n        }\n\t@media screen {\n\t\
          \    .grey, .grey a:link, .grey a:visited {\n\t\tcolor: #777;\n\t    }\n   \
          \         .docinfo {\n                background-color: #EEE;\n            }\n\
          \            .top {\n                border-top: 7px solid #EEE;\n         \
          \   }\n            .bgwhite  { background-color: white; }\n            .bgred\
          \    { background-color: #F44; }\n            .bggrey   { background-color:\
          \ #666; }\n            .bgbrown  { background-color: #840; }            \n \
          \           .bgorange { background-color: #FA0; }\n            .bgyellow { background-color:\
          \ #EE0; }\n            .bgmagenta{ background-color: #F4F; }\n            .bgblue\
          \   { background-color: #66F; }\n            .bgcyan   { background-color: #4DD;\
          \ }\n            .bggreen  { background-color: #4F4; }\n\n            .legend\
          \   { font-size: 90%; }\n            .cplate   { font-size: 70%; border: solid\
          \ grey 1px; }\n\t}\n    </style>\n    <!--[if IE]>\n    <style>\n    body {\n\
          \       font-size: 13px;\n       margin: 10px 10px;\n    }\n    </style>\n \
          \   <![endif]-->\n\n    <script type=\"text/javascript\"><!--\n    function\
          \ addHeaderTags() {\n\tvar spans = document.getElementsByTagName(\"span\");\n\
          \tfor (var i=0; i < spans.length; i++) {\n\t    var elem = spans[i];\n\t   \
          \ if (elem) {\n\t\tvar level = elem.getAttribute(\"class\");\n             \
          \   if (level == \"h1\" || level == \"h2\" || level == \"h3\" || level == \"\
          h4\" || level == \"h5\" || level == \"h6\") {\n                    elem.innerHTML\
          \ = \"<\"+level+\">\"+elem.innerHTML+\"</\"+level+\">\";\t\t\n             \
          \   }\n\t    }\n\t}\n    }\n    var legend_html = \"Colour legend:<br />   \
          \   <table>         <tr><td>Unknown:</td>                   <td><span class='cplate\
          \ bgwhite'>&nbsp;&nbsp;&nbsp;&nbsp;</span></td></tr>         <tr><td>Draft:</td>\
          \                     <td><span class='cplate bgred'>&nbsp;&nbsp;&nbsp;&nbsp;</span></td></tr>\
          \         <tr><td>Informational:</td>             <td><span class='cplate bgorange'>&nbsp;&nbsp;&nbsp;&nbsp;</span></td></tr>\
          \         <tr><td>Experimental:</td>              <td><span class='cplate bgyellow'>&nbsp;&nbsp;&nbsp;&nbsp;</span></td></tr>\
          \         <tr><td>Best Common Practice:</td>      <td><span class='cplate bgmagenta'>&nbsp;&nbsp;&nbsp;&nbsp;</span></td></tr>\
          \         <tr><td>Proposed Standard:</td>         <td><span class='cplate bgblue'>&nbsp;&nbsp;&nbsp;&nbsp;</span></td></tr>\
          \         <tr><td>Draft Standard (old designation):</td> <td><span class='cplate\
          \ bgcyan'>&nbsp;&nbsp;&nbsp;&nbsp;</span></td></tr>         <tr><td>Internet\
          \ Standard:</td>         <td><span class='cplate bggreen'>&nbsp;&nbsp;&nbsp;&nbsp;</span></td></tr>\
          \         <tr><td>Historic:</td>                  <td><span class='cplate bggrey'>&nbsp;&nbsp;&nbsp;&nbsp;</span></td></tr>\
          \         <tr><td>Obsolete:</td>                  <td><span class='cplate bgbrown'>&nbsp;&nbsp;&nbsp;&nbsp;</span></td></tr>\
          \     </table>\";\n    function showElem(id) {\n        var elem = document.getElementById(id);\n\
          \        elem.innerHTML = eval(id+\"_html\");\n        elem.style.visibility='visible';\n\
          \    }\n    function hideElem(id) {\n        var elem = document.getElementById(id);\n\
          \        elem.style.visibility='hidden';        \n        elem.innerHTML = \"\
          \";\n    }\n    // -->\n    </script>\n</head>\n<body onload=\"addHeaderTags()\"\
          >\n   <div style=\"height: 13px;\">\n      <div onmouseover=\"this.style.cursor='pointer';\"\
          \n         onclick=\"showElem('legend');\"\n         onmouseout=\"hideElem('legend')\"\
          \n\t style=\"height: 6px; position: absolute;\"\n         class=\"pre noprint\
          \ docinfo bgred\"\n         title=\"Click for colour legend.\" >           \
          \                                                             </div>\n     \
          \ <div id=\"legend\"\n           class=\"docinfo noprint pre legend\"\n    \
          \       style=\"position:absolute; top: 4px; left: 4ex; visibility:hidden; background-color:\
          \ white; padding: 4px 9px 5px 7px; border: solid #345 1px; \"\n           onmouseover=\"\
          showElem('legend');\"\n           onmouseout=\"hideElem('legend');\">\n    \
          \  </div>\n   </div>\n<span class=\"pre noprint docinfo top\">[<a href=\"../html/\"\
          \ title=\"Document search and retrieval page\">Docs</a>] [<a href=\"http://tools.ietf.org/id/draft-nottingham-http-portal-02.txt\"\
          \ title=\"Plaintext version of this document\">txt</a>|<a href=\"/pdf/draft-nottingham-http-portal-02.txt\"\
          \ title=\"PDF version of this document\">pdf</a>|<a href=\"/id/draft-nottingham-http-portal-02.xml\"\
          \ title=\"XML source for this document\">xml</a>|<a href=\"/id/draft-nottingham-http-portal-02.html\"\
          \ title=\"HTML version of this document, from XML2RFC\">html</a>] [<a href='https://datatracker.ietf.org/doc/draft-nottingham-http-portal'\
          \ title='IESG Datatracker information for this document'>Tracker</a>] [<a href=\"\
          mailto:draft-nottingham-http-portal@tools.ietf.org?subject=draft-nottingham-http-portal%20\"\
          \ title=\"Send email to the document authors\">Email</a>] [<a href=\"/rfcdiff?difftype=--hwdiff&amp;url2=draft-nottingham-http-portal-02.txt\"\
          \ title=\"Inline diff (wdiff)\">Diff1</a>] [<a href=\"/rfcdiff?url2=draft-nottingham-http-portal-02.txt\"\
          \ title=\"Side-by-side diff\">Diff2</a>] [<a href=\"/idnits?url=http://tools.ietf.org/id/draft-nottingham-http-portal-02.txt\"\
          \ title=\"Run an idnits check of this document\">Nits</a>]      </span><br />\n\
          <span class=\"pre noprint docinfo\">                                       \
          \                                 </span><br />\n<span class=\"pre noprint docinfo\"\
          >Versions: <a href=\"./draft-nottingham-http-portal-00\">00</a> <a href=\"./draft-nottingham-http-portal-01\"\
          >01</a> <a href=\"./draft-nottingham-http-portal-02\">02</a>               \
          \                                       </span><br />\n<span class=\"pre noprint\
          \ docinfo\">                                                               \
          \         </span><br />\n<pre>\nNetwork Working Group                      \
          \                M. Nottingham\nInternet-Draft                             \
          \            February 18, 2011\nIntended status: Standards Track\nExpires: August\
          \ 22, 2011\n\n\n          <span class=\"h1\">The Network Authentication Required\
          \ HTTP Status Code</span>\n                    <span class=\"h1\">draft-nottingham-http-portal-02</span>\n\
          \nAbstract\n\n   \"Captive portals\" are a commonly-deployed means of obtaining\
          \ access\n   credentials and/or payment for a network.  This memo introduces\
          \ a new\n   HTTP status code as a means of addressing issues found in these\n\
          \   deployments.\n\n   This memo should be discussed on the ietf-http-wg@w3.org\
          \ mailing\n   list, although it is not a work item of the HTTPbis WG.\n\nStatus\
          \ of this Memo\n\n   This Internet-Draft is submitted in full conformance with\
          \ the\n   provisions of <a href=\"./bcp78\">BCP 78</a> and <a href=\"./bcp79\"\
          >BCP 79</a>.\n\n   Internet-Drafts are working documents of the Internet Engineering\n\
          \   Task Force (IETF).  Note that other groups may also distribute\n   working\
          \ documents as Internet-Drafts.  The list of current Internet-\n   Drafts is\
          \ at <a href=\"http://datatracker.ietf.org/drafts/current/\">http://datatracker.ietf.org/drafts/current/</a>.\n\
          \n   Internet-Drafts are draft documents valid for a maximum of six months\n\
          \   and may be updated, replaced, or obsoleted by other documents at any\n \
          \  time.  It is inappropriate to use Internet-Drafts as reference\n   material\
          \ or to cite them other than as \"work in progress.\"\n\n   This Internet-Draft\
          \ will expire on August 22, 2011.\n\nCopyright Notice\n\n   Copyright (c) 2011\
          \ IETF Trust and the persons identified as the\n   document authors.  All rights\
          \ reserved.\n\n   This document is subject to <a href=\"./bcp78\">BCP 78</a>\
          \ and the IETF Trust's Legal\n   Provisions Relating to IETF Documents\n   (<a\
          \ href=\"http://trustee.ietf.org/license-info\">http://trustee.ietf.org/license-info</a>)\
          \ in effect on the date of\n   publication of this document.  Please review\
          \ these documents\n   carefully, as they describe your rights and restrictions\
          \ with respect\n   to this document.  Code Components extracted from this document\
          \ must\n   include Simplified BSD License text as described in <a href=\"#section-4\"\
          >Section 4</a>.e of\n\n\n\n<span class=\"grey\">Nottingham               Expires\
          \ August 22, 2011                [Page 1]</span>\n</pre><!--NewPage--><pre class='newpage'><a\
          \ name=\"page-2\" id=\"page-2\" href=\"#page-2\" class=\"invisible\"> </a>\n\
          <span class=\"grey\">Internet-Draft       Network Authentication Required  \
          \     February 2011</span>\n\n\n   the Trust Legal Provisions and are provided\
          \ without warranty as\n   described in the Simplified BSD License.\n\n\nTable\
          \ of Contents\n\n   <a href=\"#section-1\">1</a>.  Introduction  . . . . . .\
          \ . . . . . . . . . . . . . . . . . . . <a href=\"#page-3\">3</a>\n   <a href=\"\
          #section-2\">2</a>.  428 Network Authentication Required . . . . . . . . . .\
          \ . . . . <a href=\"#page-3\">3</a>\n   <a href=\"#section-3\">3</a>.  Security\
          \ Considerations . . . . . . . . . . . . . . . . . . . . <a href=\"#page-4\"\
          >4</a>\n   <a href=\"#section-4\">4</a>.  IANA Considerations . . . . . . .\
          \ . . . . . . . . . . . . . . . <a href=\"#page-4\">4</a>\n   <a href=\"#appendix-A\"\
          >Appendix A</a>.  Using the 428 Status Code  . . . . . . . . . . . . . . <a\
          \ href=\"#page-4\">4</a>\n   <a href=\"#appendix-B\">Appendix B</a>.  Issues\
          \ Raised by Captive Portals . . . . . . . . . . . <a href=\"#page-5\">5</a>\n\
          \   <a href=\"#appendix-C\">Appendix C</a>.  Non-HTTP Applications and Techniques\
          \ . . . . . . . . . <a href=\"#page-6\">6</a>\n   <a href=\"#appendix-D\">Appendix\
          \ D</a>.  Acknowledgements . . . . . . . . . . . . . . . . . . . <a href=\"\
          #page-6\">6</a>\n   Author's Address  . . . . . . . . . . . . . . . . . . .\
          \ . . . . . . <a href=\"#page-6\">6</a>\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\
          \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n<span class=\"grey\">Nottingham        \
          \       Expires August 22, 2011                [Page 2]</span>\n</pre><!--NewPage--><pre\
          \ class='newpage'><a name=\"page-3\" id=\"page-3\" href=\"#page-3\" class=\"\
          invisible\"> </a>\n<span class=\"grey\">Internet-Draft       Network Authentication\
          \ Required       February 2011</span>\n\n\n<span class=\"h2\"><a class=\"selflink\"\
          \ name=\"section-1\" href=\"#section-1\">1</a>.  Introduction</span>\n\n   It\
          \ has become common for networks to require authentication, payment\n   and/or\
          \ acceptance of terms of service before granting access.\n   Typically, this\
          \ occurs when accessing \"public\" networks such as those\n   in hotels, trains,\
          \ conference centres and similar networks.\n\n   While there are several potential\
          \ means of providing credentials to a\n   network, these are not yet universally\
          \ supported, and in some\n   instances the network administrator requires that\
          \ information (e.g.,\n   terms of service, login information) be displayed to\
          \ end users.\n\n   In such cases, it has become widespread practice to use a\
          \ \"captive\n   portal\" that diverts HTTP requests to the administrator's web\
          \ page.\n   Once the user has satisfied requirements (e.g., for payment,\n \
          \  acceptance of terms), the diversion is ended and \"normal\" access to\n \
          \  the network is allowed.\n\n   Typically, this diversion is accomplished by\
          \ one of several possible\n   techniques;\n   o  IP interception - all requests\
          \ on port 80 are intercepted and send\n      to the portal.\n   o  HTTP redirects\
          \ - all requests on port 80 are intercepted and an\n      HTTP redirect to the\
          \ portal's URL is returned.\n   o  DNS interception - all DNS lookups return\
          \ the portal's IP address.\n\n   In each case, the intent is that users connecting\
          \ to the network will\n   open a Web browser and see the portal.\n\n   However,\
          \ because port 80 is used for non-browser traffic, a number of\n   issues (see\
          \ <a href=\"#appendix-B\">Appendix B</a>) have been encountered.\n\n   This\
          \ memo introduces a new HTTP status code, 428 Network\n   Authentication Required,\
          \ as a solution to some of these issues.\n   <a href=\"#appendix-A\">Appendix\
          \ A</a> outlines how it might be used in typical deployments.\n\n\n<span class=\"\
          h2\"><a class=\"selflink\" name=\"section-2\" href=\"#section-2\">2</a>.  428\
          \ Network Authentication Required</span>\n\n   This status code indicates that\
          \ the client should authenticate to\n   gain network access before resubmitting\
          \ the request.\n\n   The response body SHOULD indicate how to do this; e.g.,\
          \ with an HTML\n   form for submitting credentials.\n\n   Responses with the\
          \ 428 status code MUST NOT be stored by a cache.\n\n\n\n\n\n<span class=\"grey\"\
          >Nottingham               Expires August 22, 2011                [Page 3]</span>\n\
          </pre><!--NewPage--><pre class='newpage'><a name=\"page-4\" id=\"page-4\" href=\"\
          #page-4\" class=\"invisible\"> </a>\n<span class=\"grey\">Internet-Draft   \
          \    Network Authentication Required       February 2011</span>\n\n\n<span class=\"\
          h2\"><a class=\"selflink\" name=\"section-3\" href=\"#section-3\">3</a>.  Security\
          \ Considerations</span>\n\n   In common use, a response carrying the 428 status\
          \ code will not come\n   from the origin server indicated in the request's URL.\
          \  This presents\n   many security issues; e.g., an attacking intermediary may\
          \ be\n   inserting cookies into the original domain's name space, may be\n \
          \  observing cookies or HTTP authentication credentials sent from the\n   user\
          \ agent, and so on.\n\n   However, these risks are not unique to the 428 status\
          \ code; in other\n   words, a captive portal that is not using this status code\
          \ introduces\n   the same issues.\n\n\n<span class=\"h2\"><a class=\"selflink\"\
          \ name=\"section-4\" href=\"#section-4\">4</a>.  IANA Considerations</span>\n\
          \n   The HTTP Status Codes Registry should be updated with the following\n \
          \  entry:\n\n   o  Code: 428\n   o  Description: Network Authentication Required\n\
          \   o  Specification: [ this document ]\n\n\n<span class=\"h2\"><a class=\"\
          selflink\" name=\"appendix-A\" href=\"#appendix-A\">Appendix A</a>\r\n1c15\r\
          \n.  Using the 428 Status Code</span>\n\n   This appendix demonstrates a typical\
          \ use of the 428 status code; it\n   is not normative.\n\n   A network operator\
          \ wishing to require some authentication, acceptance\n   of terms or other user\
          \ interaction before granting access usually\n   does so by identify clients\
          \ who have not done so (\"unknown clients\")\n   using their MAC addresses.\n\
          \n   Unknown clients then have all traffic blocked, except for that on TCP\n\
          \   port 80, which is sent to a HTTP server (the \"login server\")\n   dedicated\
          \ to \"logging in\" unknown clients, and of course traffic to\n   the login\
          \ server itself.\n\n   For example, a user agent might connect to a network\
          \ and make the\n   following HTTP request on TCP port 80:\n\n   GET /index.htm\
          \ HTTP/1.1\n   Host: www.example.com\n   User-Agent: ExampleAgent\n\n   Upon\
          \ receiving such a request, the login server would generate a 428\n   response:\n\
          \n\n\n<span class=\"grey\">Nottingham               Expires August 22, 2011\
          \                [Page 4]</span>\n</pre><!--NewPage--><pre class='newpage'><a\
          \ name=\"page-5\" id=\"page-5\" href=\"#page-5\" class=\"invisible\"> </a>\n\
          <span class=\"grey\">Internet-Draft       Network Authentication Required  \
          \     February 2011</span>\n\n\n   HTTP/1.1 428 Network Authentication Required\n\
          \   Refresh: 0; url=https://login.example.net/\n   Content-Type: text/html\n\
          \n   &lt;html&gt;\n      &lt;head&gt;\n      &lt;/head&gt;\n      &lt;body&gt;\n\
          \         &lt;h1&gt;You are being redirected to log into the network...&lt;/h1&gt;\n\
          \      &lt;/body&gt;\n   &lt;/html&gt;\n\n   Here, the 428 status code assures\
          \ that non-browser clients will not\n   interpret the response as being from\
          \ the origin server, and the\n   Refresh header redirects the user agent to\
          \ the login server (an HTML\n   META element can be used for this as well).\n\
          \n   Note that the 428 response can itself contain the login interface,\n  \
          \ but it may not be desirable to do so, because browsers would show the\n  \
          \ login interface as being associated with the originally requested\n   URL,\
          \ which may cause confusion.\n\n\n<span class=\"h2\"><a class=\"selflink\" name=\"\
          appendix-B\" href=\"#appendix-B\">Appendix B</a>.  Issues Raised by Captive\
          \ Portals</span>\n\n   Since clients cannot differentiate between a portal's\
          \ response and\n   that of the HTTP server that they intended to communicate\
          \ with, a\n   number of issues arise.\n\n   One example is the \"favicon.ico\"\
          \n   &lt;<a href=\"http://en.wikipedia.org/wiki/Favicon\">http://en.wikipedia.org/wiki/Favicon</a>&gt;\
          \ commonly used by browsers to\n   identify the site being accessed.  If the\
          \ favicon for a given site is\n   fetched from a captive portal instead of the\
          \ intended site (e.g.,\n   because the user is unauthenticated), it will often\
          \ \"stick\" in the\n   browser's cache (most implementations cache favicons\
          \ aggressively)\n   beyond the portal session, so that it seems as if the portal's\n\
          \   favicon has \"taken over\" the legitimate site.\n\n   Another browser-based\
          \ issue comes about when P3P\n   &lt;<a href=\"http://www.w3.org/TR/P3P/\">http://www.w3.org/TR/P3P/</a>&gt;\
          \ is supported.  Depending on how it is\n   implemented, it's possible a browser\
          \ might interpret a portal's\n   response for the p3p.xml file as the server's,\
          \ resulting in the\n   privacy policy (or lack thereof) advertised by the portal\
          \ being\n   interpreted as applying to the intended site.  Other Web-based\n\
          \   protocols such as WebFinger\n   &lt;<a href=\"http://code.google.com/p/webfinger/wiki/WebFingerProtocol\"\
          >http://code.google.com/p/webfinger/wiki/WebFingerProtocol</a>&gt;, CORS\n \
          \  &lt;<a href=\"http://www.w3.org/TR/cors/\">http://www.w3.org/TR/cors/</a>&gt;\
          \ and OAuth\n   &lt;<a href=\"http://tools.ietf.org/html/draft-ietf-oauth-v2\"\
          >http://tools.ietf.org/html/draft-ietf-oauth-v2</a>&gt; may also be\n\n\n\n\
          <span class=\"grey\">Nottingham               Expires August 22, 2011      \
          \          [Page 5]</span>\n</pre><!--NewPage--><pre class='newpage'><a name=\"\
          page-6\" id=\"page-6\" href=\"#page-6\" class=\"invisible\"> </a>\n<span class=\"\
          grey\">Internet-Draft       Network Authentication Required       February 2011</span>\n\
          \n\n   vulnerable to such issues.\n\n   Although HTTP is most widely used with\
          \ Web browsers, a growing number\n   of non-browsing applications use it as\
          \ a substrate protocol.  For\n   example, WebDAV &lt;<a href=\"http://tools.ietf.org/html/rfc4918\"\
          >http://tools.ietf.org/html/rfc4918</a>&gt; and CalDAV\n   &lt;<a href=\"http://www.ietf.org/rfc/rfc4791.txt\"\
          >http://www.ietf.org/rfc/rfc4791.txt</a>&gt; both use HTTP as the basis (for\n\
          \   network filesystem access and calendaring, respectively).  Using\n   these\
          \ applications from behind a captive portal can result in\n   spurious errors\
          \ being presented to the user, and might result in\n   content corruption, in\
          \ extreme cases.\n\n   Similarly, other non-browser applications using HTTP\
          \ can be affected\n   as well; e.g., widgets &lt;<a href=\"http://www.w3.org/TR/widgets/\"\
          >http://www.w3.org/TR/widgets/</a>&gt;, software\n   updates, and other specialised\
          \ software such as Twitter clients and\n   the iTunes Music Store.\n\n   It\
          \ should be noted that it's sometimes believed that using HTTP\n   redirection\
          \ to direct traffic to the portal addresses these issues.\n   However, since\
          \ many of these uses \"follow\" redirects, this is not a\n   good solution.\n\
          \n\n<span class=\"h2\"><a class=\"selflink\" name=\"appendix-C\" href=\"#appendix-C\"\
          >Appendix C</a>.  Non-HTTP Applications and Techniques</span>\n\n   This memo\
          \ does not address non-HTTP applications, such as IMAP, POP,\n   or even TLS-encapsulated\
          \ HTTP.  Since captive portals almost always\n   target Web browsers (has anyone\
          \ ever seen one that inserts an e-mail\n   into your inbox asking you to authenticate?),\
          \ this is appropriate.\n\n   Instead, it is anticipated that well-behaved portals\
          \ will block all\n   non-HTTP ports (especially port 443) until the user has\
          \ successfully\n   authenticated.\n\n   Overall, there may also be an interesting\
          \ discussion to be had about\n   improving network access methods to the point\
          \ where a user interface\n   can be presented for the same purposes, without\
          \ resorting to\n   intercepting HTTP traffic.  However, since such a mechanism\
          \ would by\n   necessity require modifying the network stack and operating system\
          \ of\n   the client, this memo takes a more modest approach.\n\n\n<span class=\"\
          h2\"><a class=\"selflink\" name=\"appendix-D\" href=\"#appendix-D\">Appendix\
          \ D</a>.  Acknowledgements</span>\n\n   The author takes all responsibility\
          \ for errors and omissions.\n\n\n\n\n\n\n\n<span class=\"grey\">Nottingham \
          \              Expires August 22, 2011                [Page 6]</span>\n</pre><!--NewPage--><pre\
          \ class='newpage'><a name=\"page-7\" id=\"page-7\" href=\"#page-7\" class=\"\
          invisible\"> </a>\n<span class=\"grey\">Internet-Draft       Network Authentication\
          \ Required       February 2011</span>\n\n\nAuthor's Address\n\n   Mark Nottingham\n\
          \n   Email: mnot@mnot.net\n   URI:   <a href=\"http://www.mnot.net/\">http://www.mnot.net/</a>\n\
          \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\
          \n\n\n\n\n\n\nNottingham               Expires August 22, 2011             \
          \   [Page 7]\n\n</pre><br />\n<span class=\"noprint\"><small><small>Html markup\
          \ produced by rfcmarkup 1.107, available from\n<a href=\"http://tools.ietf.org/tools/rfcmarkup/\"\
          >http://tools.ietf.org/tools/rfcmarkup/</a>\n</small></small></span>\n</body></html>\n\
          \r\n0\r\n\r\n"
        code: 200
        headers:
        - - Transfer-Encoding
          - [chunked]
        - - Vary
          - [Accept-Encoding]
        - - Server
          - [Apache/2.2.22 (Debian)]
        - - Connection
          - [close]
        - - Date
          - ['Sun, 11 May 2014 16:39:17 GMT']
        - - Content-Type
          - [text/html; charset=US-ASCII]
    - request:
        body: null
        headers:
        - [User-Agent, Microsoft NCSI]
        method: GET
        tor: {is_tor: false}
        url: http://www.msftncsi.com/ncsi.txt
      response:
        body: Microsoft NCSI
        code: 200
        headers:
        - - Date
          - ['Sun, 11 May 2014 16:39:22 GMT']
        - - Content-Length
          - ['14']
        - - Content-Type
          - [text/plain]
        - - Connection
          - [close]
        - - Cache-Control
          - ['max-age=30, must-revalidate']
    socksproxy: null
    vendor_dns_tests:
      google_dns_cp: !!set {}
      ms_dns_cp: [131.107.255.255]
    vendor_tests:
    - result: true
      vt: ['http://www.apple.com/library/test/success.html', Success, '200', 'Mozilla/5.0
          (iPhone; U; CPU like Mac OS X; en) AppleWebKit/420+ (KHTML, like Gecko) Version/3.0
          Mobile/1A543a Safari/419.3', Apple HTTP Captive Portal]
    - result: true
      vt: ['http://tools.ietf.org/html/draft-nottingham-http-portal-02', 428 Network Authentication
          Required, '428', 'Mozilla/5.0 (Windows NT 6.1; rv:5.0) Gecko/20100101 Firefox/5.0',
        W3 Captive Portal]
    - result: true
      vt: ['http://www.msftncsi.com/ncsi.txt', Microsoft NCSI, '200', Microsoft NCSI,
        MS HTTP Captive Portal]
    ...

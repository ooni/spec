# Specification version number

2013-02-08-000

# Specification name

HTTP Requests Test

# Test preconditions

  * An internet connection
  * Ability to reach the Tor network (either Tor is not censored or the user has a Tor bridge)

# Expected impact

The ability to detect which websites are being blocked.

# Expected inputs

## Import document or import data format

A list of URLs to be tested for censorship.

## Semantics

A http URL one per line as per RFC2616 section 3.2.

# Test description

For every URL given as input we perform a HTTP GET request over the probes
network and one over the Tor network.

By default the HTTP User Agent is chosen at random and is different between the
control request and the experiment request.

Since version 0.2.3 the User Agent is chosen at random, but is the same between
the control request and the experiment request.

The user agent is chosen amongst this set of possible user agents:

    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7",
    "Mozilla/5.0 (iPhone; U; CPU iPhone OS 3 1 2 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Mobile/7D11",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2) Gecko/20100115 Firefox/3.6",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; de; rv:1.9.2) Gecko/20100115 Firefox/3.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2) Gecko/20100115 Firefox/3.6",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7 (.NET CLR 3.5.30729)"


These user agents are taken from the "How Unique Is Your Web Browser?"
(https://panopticlick.eff.org/browser-uniqueness.pdf) paper as the browser user
agents with largest anonymity set.

We compare the HTTP response body and HTTP response headers to of the request
made over Tor and that made over the probes network for consistency.

The response body is considered to match if the proportion between the body of
the response over Tor and the response over the probes network is greater than
a certain factor (by default 0.8).

# Expected output

## Parent data format

df-001-httpt-000

## Required output data

* The requests that have been made.

* The received responses.

* If factor between the two response bodies

* If the response bodies appear to match

Present only in test version >= 0.2:

* The difference between the two response headers

* If the two response headers match

Present only in test version >= 0.2.2:

* If the control responses or experiment requests have failed their error
  message.

## Semantics

    body_length_match:
      true|false

    body_proportion:
      `float` the proportion between the two response bodies

    factor:
      `float` the body proportion factor used to assert length equality

Only in test version >= 0.2:

    headers_diff:
      `set` the keys of the headers that are different between the two responses

    headers_match:
      true|false

Only in test version >= 0.2.2:

    control_failure:
      null or `string` containing the HTTP request error string (for a list of
      possible error string see df-000-base section "Error strings")

    experiment_failure:
      null or `string` containing the HTTP request error string (for a list of
      possible error string see df-000-base section "Error strings")

## Possible conclusions

If the website in question is reachable from the probes network.

## Example output sample

    agent: agent
    body_length_match: true
    body_proportion: 1.0
    control_failure: null
    experiment_failure: null
    factor: 0.8
    headers_diff: !!set {}
    headers_match: true
    requests:
    - request:
        body: null
        headers:
        - - User-Agent
          - ['Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2) Gecko/20100115
              Firefox/3.6']
        method: GET
        url: http://google.com
      response:
        body: ''
        code: 301
        headers:
        - - Content-Length
          - ['219']
        - - X-XSS-Protection
          - [1; mode=block]
        - - Expires
          - ['Sun, 10 Mar 2013 21:42:35 GMT']
        - - Server
          - [gws]
        - - Connection
          - [close]
        - - Location
          - ['http://www.google.com/']
        - - Cache-Control
          - ['public, max-age=2592000']
        - - Date
          - ['Fri, 08 Feb 2013 21:42:35 GMT']
        - - X-Frame-Options
          - [SAMEORIGIN]
        - - Content-Type
          - [text/html; charset=UTF-8]
    - request:
        body: null
        headers:
        - - User-Agent
          - ['Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2) Gecko/20100115
              Firefox/3.6']
        method: GET
        url: shttp://google.com
      response:
        body: ''
        code: 301
        headers:
        - - Content-Length
          - ['219']
        - - X-XSS-Protection
          - [1; mode=block]
        - - Expires
          - ['Sun, 10 Mar 2013 21:42:40 GMT']
        - - Server
          - [gws]
        - - Connection
          - [close]
        - - Location
          - ['http://www.google.com/']
        - - Cache-Control
          - ['public, max-age=2592000']
        - - Date
          - ['Fri, 08 Feb 2013 21:42:40 GMT']
        - - X-Frame-Options
          - [SAMEORIGIN]
        - - Content-Type
          - [text/html; charset=UTF-8]
    socksproxy: null


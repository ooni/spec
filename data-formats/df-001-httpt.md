# HTTPTest template data format

Data Format Version: df-001-httpt-000

This is the specification of the data format that every test that is
based on ooni.templates.httpt.HTTPTest shall be using.

Third party tests that run HTTP related measurements SHOULD also be using such
data format.

## Specification

    ---
    requests:
      - request:
          headers:
            `dict` the headers of the request
          body:
            `string` the body of the response

          url:
            `string` the URL of the request being made (if prefixed with 's' it means
            the request was made via the Tor SOCKS proxy)

        method:
            `string` the HTTP method being used

        response:
          headers:
            `dict` the headers of the response
          body:
            `string` the body of the response

          code:
            `int` the response status code

      - request:
            etc. etc.

    socksproxy:
      null if no socks proxy was used for this request or an IP port
      combination (as a string) if a SOCKS proxy was used.

    agent:
      either 'agent' if 30X redirects should not be followed or 'redirect' if
      they should be followed.

    ...

## Example output

    input: http://google.com/
    report:
      agent: agent
      requests:
      - request:
          body: null
          headers:
          - - User-Agent
            - - &id001 [Mozilla/4.0 (compatible; MSIE 5.0; Windows NT 5.1; .NET CLR 1.1.4322),
                'Internet Explorer 5, Windows XP']
          method: GET
          url: http://google.com/
        response:
          body: ''
          code: 301
          headers:
          - - Content-Length
            - ['219']
          - - X-XSS-Protection
            - [1; mode=block]
          - - Expires
            - ['Tue, 29 Jan 2013 14:29:19 GMT']
          - - Server
            - [gws]
          - - Connection
            - [close]
          - - Location
            - ['http://www.google.com/']
          - - Cache-Control
            - ['public, max-age=2592000']
          - - Date
            - ['Sun, 30 Dec 2012 14:29:19 GMT']
          - - X-Frame-Options
            - [SAMEORIGIN]
          - - Content-Type
            - [text/html; charset=UTF-8]
      - request:
          body: null
          headers:
          - - User-Agent
            - - *id001
          method: GET
          url: shttp://google.com/
        response:
          body: ''
          code: 301
          headers:
          - - Content-Length
            - ['219']
          - - X-XSS-Protection
            - [1; mode=block]
          - - Expires
            - ['Tue, 29 Jan 2013 14:29:20 GMT']
          - - Server
            - [gws]
          - - Connection
            - [close]
          - - Location
            - ['http://www.google.com/']
          - - Cache-Control
            - ['public, max-age=2592000']
          - - Date
            - ['Sun, 30 Dec 2012 14:29:20 GMT']
          - - X-Frame-Options
            - [SAMEORIGIN]
          - - Content-Type
            - [text/html; charset=UTF-8]
      socksproxy: null



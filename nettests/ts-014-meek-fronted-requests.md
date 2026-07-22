# Specification version number

2015-04-01-000

* _status_: obsolete

# Specification name

Meek Fronted Request Test

# Test preconditions

* An internet connection

# Expected impact

Ability to detect uncensored fronted domains that can transmit requests to the
"inside" meek-server via an intermediary web service.

# Expected inputs

## Import document or import data format

A list of domain names (fronted domains) and host headers (meek-server) of the
intermediary web service.

## Semantics

The input document may contain a domain name and a host header combination per
line separated by colon in the format:

	DomainName:HostHeader

Example:

	www.google.com:meek-reflect.appspot.com
	a0.awsstatic.com:d2zfqthxsdq309.cloudfront.net

# Test description

Performs a HTTP GET request over TLS (HTTPS) to a list of fronted domains with
the Host Header of the "inside" meek-server. For diagnostic purposes the
meek-server handles a GET request and respond with: "I’m just a happy little
web server.\n". The GET request is sent over TLS to the root of the fronted
domain with the Host Header option of the desired meek-server host.


# Expected output

## Parent data format

df-001-httpt-000

## Required output data

* The domain name and host header used in the measurement
	(DomainName:HostHeader)

* The requests that have been made

* The received responses

* If the meek server is blocked or unreachable

## Semantics

success:
	**boolean** indicates if an HTTPS GET response to the meek server is
	successfull

## Possible conclusions

If the fronted request/response to the meek server is successful.

## Example output sample

```
agent: agent
input: ajax.aspnetcdn.com:az668014.vo.msecnd.net
requests:
- request:
    body: null
    headers:
    - - Host
      - [az668014.vo.msecnd.net]
    method: GET
    tor: {is_tor: false}
    url: https://ajax.aspnetcdn.com
  response:
    body: "I\u2019m just a happy little web server.\n"
    code: 200
    headers:
    - - Content-Length
      - ['38']
    - - X-Cache
      - [HIT]
    - - X-Powered-By
      - [ASP.NET]
    - - Accept-Ranges
      - [bytes]
    - - Server
      - [ECAcc (fcn/40C4)]
    - - Last-Modified
      - ['Wed, 01 Apr 2015 09:25:13 GMT']
    - - Connection
      - [close]
    - - Date
      - ['Wed, 01 Apr 2015 10:01:37 GMT']
    - - Content-Type
      - [text/plain; charset=utf-8]
socksproxy: null
success: true
```

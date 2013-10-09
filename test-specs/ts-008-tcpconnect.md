# Specification version number

2013-10-08-000

# Specification name

TCP Connect Test

# Test preconditions

  * An internet connection

For reporting to the backend to work that it is possible for
the probe to establish a connection to the Tor network.

# Expected impact

Ability to determine if a TCP connection can be successfully established.

# Expected inputs

## Import document or import data format

A list of URLs to be tested for censorship.

## Data specification version number

## Semantics

The input document may contain an http or https URL, an IP:PORT, or a FQDN:PORT per line. e.g.

  http://www.google.com
  google.com:80
  8.8.8.8:53

are all valid entries

# Test description

For every item given as input we perform a TCP connect. If
the connection is succesful, we record 'success' for the
test. If the connection fails, we record the reason for the
failure. 

# Expected output

The key 'connection' is added to the report. One report entry is written per line in the input document.

## Required output data

The result of the connection attempt, 'success' or failure type.

## Semantics

'success' or a string indicating the reason for the failure.

## Possible conclusions

Ability to determine that a specific host:port is blocked.

## Example output sample

  ###########################################
  # OONI Probe Report for tcp_connect (0.1)
  # Wed Sep 18 20:41:49 2013
  ###########################################
  ---
  input_hashes: [e0611ecd28bead38a7afeb4dda8ae3449d0fc2e1ba53fa7355f2799dce9af290]
  options: [-f, /home/ooni/.ooni/inputs/alexa-top-1m.txt]
  probe_asn: AS1234
  probe_cc: US
  probe_ip: 127.0.0.1
  software_name: ooniprobe
  software_version: 1.0.0-rc3
  start_time: 1379536909.514028
  test_name: tcp_connect
  test_version: '0.1'
  ...
  ---
  {connection: success, input: 'google.com:80'}
  ...
  ---
  {connection: success, input: 'youtube.com:80'}
  ...
  ---
  {connection: success, input: 'google.com.hk:80'}
  ...
  ---
  {connection: success, input: 'google.de:80'}
  ...
  ---
  {connection: success, input: 'google.co.in:80'}
  ...
  ---
  {connection: success, input: 'blogspot.com:80'}

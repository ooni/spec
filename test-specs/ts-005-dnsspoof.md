# Specification version number

2013-9-10-000

# Specification name

DNS Spoof Test

# Test preconditions

  * An Internet connection.

  * A DNS resolver to test against.

  * A Hostname to resolve and check for tampering.

# Expected impact

  * The ability to detect spoofed DNS responses.

# Expected inputs

This test expects the following arguments:

  * The address and port of the resolver to test.

  * The hostname to be resolved.

## Semantics

The resolver to test is passed by argument (-r) with ADDRESS:PORT convention.
A known good backend resolver may also be passed by argument (-b) with the
same convention.  The default known good backend resolver is Google DNS
(8.8.8.8:53).

The hostname to test is passed by argument (-h) as a FQDN, e.g.
www.google.com

# Test Description

We perform an A DNS query (via UDP) to the control resolver. The answer to
such query is called the control answer.

We perform an A DNS query (via UDP) to the test resolver. We then compare
this answer (experiment answer) with the control answer.

If the DNS payload of the received packets matches identically, then spoofing
is considered to be occurring.

# Expected output

The output report will contain a boolean entry 'spoofing'.  If spoofing is
occurring, it shall be True. Otherwise, it is False.

## Parent data format

df-001-scapyt-000

## Required output data

  * Whether or not the DNS payload matches (spoofing).

## Semantics

In addition to the data specified in the parent data format, the following
field(s) are added to the report:

Version 0.0.1:

    spoofing: true|false

## Possible conclusions

Whether or not DNS spoofing is occurring for a particular FQDN.

## Example output sample


  ###########################################
  # OONI Probe Report for dns_spoof (0.0.1)
  # Wed Sep 25 15:39:32 2013
  ###########################################
  ---
  input_hashes: []
  options: [-r, '10.211.0.10:53', -h, google.com]
  probe_asn: AS2819
  probe_cc: CZ
  probe_ip: 127.0.0.1
  software_name: ooniprobe
  software_version: 1.0.0-rc3
  start_time: 1380116372.573729
  test_name: dns_spoof
  test_version: 0.0.1
  ...
  ---
  answer_flags: [ipsrc]
  answered_packets:
  - - raw_packet: !!binary |
        RbgA6OumAAAyEY4+CAgICH8AAAEANQA1ANSshgAAgYAAAQALAAAAAAZnb29nbGUDY29tAAABAAEG
        Z29vZ2xlA2NvbQAAAQABAAAA4AAErcIs5QZnb29nbGUDY29tAAABAAEAAADgAAStwizkBmdvb2ds
        ZQNjb20AAAEAAQAAAOAABK3CLOYGZ29vZ2xlA2NvbQAAAQABAAAA4AAErcIs6QZnb29nbGUDY29t
        AAABAAEAAADgAAStwizoBmdvb2dsZQNjb20AAAEAAQAAAOAABK3CLOcGZ29vZ2xlA2NvbQAAAQAB
        AAAA4AAErcIs4gZnb29nbGUDY29tAAABAAEAAADgAAStwizjBmdvb2dsZQNjb20AAAEAAQAAAOAA
        BK3CLOAGZ29vZ2xlA2NvbQAAAQABAAAA4AAErcIs4QZnb29nbGUDY29tAAABAAEAAADgAAStwizu
      summary: 'IP / UDP / DNS Ans "173.194.44.229" '
  - - raw_packet: !!binary |
        RbgA6J0DAABAEdQUCtMACn8AAAEANQA1ANSxxAAAgYAAAQALAAAAAAZnb29nbGUDY29tAAABAAEG
        Z29vZ2xlA2NvbQAAAQABAAAA3wAErcIs5wZnb29nbGUDY29tAAABAAEAAADfAAStwizoBmdvb2ds
        ZQNjb20AAAEAAQAAAN8ABK3CLOkGZ29vZ2xlA2NvbQAAAQABAAAA3wAErcIs5gZnb29nbGUDY29t
        AAABAAEAAADfAAStwizkBmdvb2dsZQNjb20AAAEAAQAAAN8ABK3CLOUGZ29vZ2xlA2NvbQAAAQAB
        AAAA3wAErcIs7gZnb29nbGUDY29tAAABAAEAAADfAAStwizhBmdvb2dsZQNjb20AAAEAAQAAAN8A
        BK3CLOAGZ29vZ2xlA2NvbQAAAQABAAAA3wAErcIs4wZnb29nbGUDY29tAAABAAEAAADfAAStwizi
      summary: 'IP / UDP / DNS Ans "173.194.44.231" '
  input: null
  sent_packets:
  - - raw_packet: !!binary |
        RQAAOAABAABAEeujfwAAAQgICAgANQA1ACRccgAAAQAAAQAAAAAAAAZnb29nbGUDY29tAAABAAE=
      summary: 'IP / UDP / DNS Qry "google.com" '
  - - raw_packet: !!binary |
        RQAAOAABAABAEfDWfwAAAQrTAAoANQA1ACRhpQAAAQAAAQAAAAAAAAZnb29nbGUDY29tAAABAAE=
      summary: 'IP / UDP / DNS Qry "google.com" '
  spoofing: false
  test_a_lookup:
    answered_packets:
    - raw_packet: !!binary |
        RbgA6J0DAABAEdQUCtMACn8AAAEANQA1ANSxxAAAgYAAAQALAAAAAAZnb29nbGUDY29tAAABAAEG
        Z29vZ2xlA2NvbQAAAQABAAAA3wAErcIs5wZnb29nbGUDY29tAAABAAEAAADfAAStwizoBmdvb2ds
        ZQNjb20AAAEAAQAAAN8ABK3CLOkGZ29vZ2xlA2NvbQAAAQABAAAA3wAErcIs5gZnb29nbGUDY29t
        AAABAAEAAADfAAStwizkBmdvb2dsZQNjb20AAAEAAQAAAN8ABK3CLOUGZ29vZ2xlA2NvbQAAAQAB
        AAAA3wAErcIs7gZnb29nbGUDY29tAAABAAEAAADfAAStwizhBmdvb2dsZQNjb20AAAEAAQAAAN8A
        BK3CLOAGZ29vZ2xlA2NvbQAAAQABAAAA3wAErcIs4wZnb29nbGUDY29tAAABAAEAAADfAAStwizi
      summary: 'IP / UDP / DNS Ans "173.194.44.231" '
  test_control_a_lookup:
    answered_packets:
    - raw_packet: !!binary |
        RbgA6OumAAAyEY4+CAgICH8AAAEANQA1ANSshgAAgYAAAQALAAAAAAZnb29nbGUDY29tAAABAAEG
        Z29vZ2xlA2NvbQAAAQABAAAA4AAErcIs5QZnb29nbGUDY29tAAABAAEAAADgAAStwizkBmdvb2ds
        ZQNjb20AAAEAAQAAAOAABK3CLOYGZ29vZ2xlA2NvbQAAAQABAAAA4AAErcIs6QZnb29nbGUDY29t
        AAABAAEAAADgAAStwizoBmdvb2dsZQNjb20AAAEAAQAAAOAABK3CLOcGZ29vZ2xlA2NvbQAAAQAB
        AAAA4AAErcIs4gZnb29nbGUDY29tAAABAAEAAADgAAStwizjBmdvb2dsZQNjb20AAAEAAQAAAOAA
        BK3CLOAGZ29vZ2xlA2NvbQAAAQABAAAA4AAErcIs4QZnb29nbGUDY29tAAABAAEAAADgAAStwizu
      summary: 'IP / UDP / DNS Ans "173.194.44.229" '
  ...

# Privacy considerations

As this test inherits from the Scapy template (see the Parent data format),
the same warnings apply. In particular, ICMP error messages may contain the
non anonymized user IP address.

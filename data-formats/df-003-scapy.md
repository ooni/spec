# ScapyTest data format

Data Format Version: df-003-scapy-000

This specifies the data format for tests that are based on
ooni.templates.scapyt.ScapyTest.

## Specification

    answer_flags:
      `list` of options that are set for determining how to understand if a
      received packet is answer to a sent packet (these only apply to ICMP
      messages)

      'ipsrc' means that we check to see if the src and destination ports in
      the ICMP IP citation match.

      'ipid' means that we look at the IPID in the response to match it up
      to sent packets.

      'seqack' means that we check if TCP sequence number and ACK match in
      the ICMP citation when processing TCP inside of ICMP.

    sent_packets:
      This contains the list of packets that have been sent.

    - raw_packet:
        `string` BASE64Encoding of packet the packet inclusive of IP
        headers

      summary:
        `string` human readable representation of the packet as is the
        output of scapy.packet.summary().

    - etc. etc.

  answered_packets:
    This contains the list of packets that are considered to be the
    answer of the above sent packets.

    - raw_packet:
        `string` BASE64Encoding of packet the packet inclusive of IP
        headers

      summary:
        `string` human readable representation of the packet as is the
        output of scapy.packet.summary().

    - etc. etc.

## Example output

    answer_flags: [ipsrc]
    answered_packets:
    - - raw_packet: !!binary |
          RQAAqI08AACAATC61Lw2eX8AAAELACiDAAAAAEUAABzCJ0AAARGEQMCosIAuppOaG2gBuwAIr1EA
          AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
          AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIACQ/gAIAQFM9wEB
        summary: IP / ICMP 212.188.54.121 > 127.0.0.1 time-exceeded ttl-zero-during-transit
          / IPerror / UDPerror / Padding
    - - raw_packet: !!binary |
          RQAAqI09AACAAUoF1LwdLX8AAAELACiDAAAAAEUAABzCJ0AAARGEQMCosIAuppOaG2gBuwAIr1EA
          AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
          AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIACL1wAIAQFSHgEB
        summary: IP / ICMP 212.188.29.45 > 127.0.0.1 time-exceeded ttl-zero-during-transit
          / IPerror / UDPerror / Padding
    - - raw_packet: !!binary |
          RQAAOI0+AACAAUn71Lwdpn8AAAELACiDAAAAAEUAABzCJ0AAARGEQMCosIAuppOaG2gBuwAIr1E=
        summary: IP / ICMP 212.188.29.166 > 127.0.0.1 time-exceeded ttl-zero-during-transit
          / IPerror / UDPerror
    - - raw_packet: !!binary |
          RQAAqI0/AACAAUrm1LwcSn8AAAELACiDAAAAAEUAABzCJ0AAARGEQMCosIAuppOaG2gBuwAIr1EA
          AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
          AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIACLtwAIAQFOPgUB
        summary: IP / ICMP 212.188.28.74 > 127.0.0.1 time-exceeded ttl-zero-during-transit
          / IPerror / UDPerror / Padding
    - - raw_packet: !!binary |
          RQAAOI1BAACAAT4U1Lwpin8AAAELACiDAAAAAEUAABzCJ0AAARGEQMCosIAuppOaG2gBuwAIr1E=
        summary: IP / ICMP 212.188.41.138 > 127.0.0.1 time-exceeded ttl-zero-during-transit
          / IPerror / UDPerror
    - - raw_packet: !!binary |
          RQAAOI1CAACAAYzr2cfVpn8AAAELACiDAAAAAEUAABzCJ0AAARGEQMCosIAuppOaG2gBuwAIr1E=
        summary: IP / ICMP 217.199.213.166 > 127.0.0.1 time-exceeded ttl-zero-during-transit
          / IPerror / UDPerror
    - - raw_packet: !!binary |
          RQAAOI1DAACAAXqrLqaTB38AAAELACiDAAAAAEUAABzCJ0AAARGEQMCosIAuppOaG2gBuwAIr1E=
        summary: IP / ICMP 46.166.147.7 > 127.0.0.1 time-exceeded ttl-zero-during-transit
          / IPerror / UDPerror
    sent_packets:
    - - raw_packet: !!binary |
          RQAAHH1NAAABEftCfwAAAS6mk5obaAG7AAiheQ==
        summary: IP / UDP 127.0.0.1:7016 > 46.166.147.154:https
    - - raw_packet: !!binary |
          RQAAHG71AAACEQibfwAAAS6mk5obaAG7AAiheQ==
        summary: IP / UDP 127.0.0.1:7016 > 46.166.147.154:https
    - - raw_packet: !!binary |
          RQAAHAUlAAADEXFrfwAAAS6mk5obaAG7AAiheQ==
        summary: IP / UDP 127.0.0.1:7016 > 46.166.147.154:https
    - - raw_packet: !!binary |
          RQAAHBqUAAAEEVr8fwAAAS6mk5obaAG7AAiheQ==
        summary: IP / UDP 127.0.0.1:7016 > 46.166.147.154:https
    - - raw_packet: !!binary |
          RQAAHPuMAAAFEXkDfwAAAS6mk5obaAG7AAiheQ==
        summary: IP / UDP 127.0.0.1:7016 > 46.166.147.154:https
    - - raw_packet: !!binary |
          RQAAHK4cAAAGEcVzfwAAAS6mk5obaAG7AAiheQ==
        summary: IP / UDP 127.0.0.1:7016 > 46.166.147.154:https
    - - raw_packet: !!binary |
          RQAAHFyiAAAHERXufwAAAS6mk5obaAG7AAiheQ==
        summary: IP / UDP 127.0.0.1:7016 > 46.166.147.154:https

## Privacy considerations

When the user has configured to not include their IP Address in the reports we
will replace the src IP address of the IP Header with "127.0.0.1" of sent
packets and the dst field of the IP header of received packets with
"127.0.0.1".
Note though that such strategy will not fully prevent the leaking of the users
IP address via the IP packet payload (for example ICMP error messages will cite
the packet they are referring to and it will contain the non anonymized user IP
address).
On this specific issue there is an open ticket here:
https://trac.torproject.org/projects/tor/ticket/7933.



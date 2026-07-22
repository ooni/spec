# tq-034 UDP blocking and manipulation

UDP is one of the two most widely used data transport protocols.
Unfortunately, some ISPs or local network firewalls may decide to completely block UDP.
By definition this is against [network neutrality](https://en.wikipedia.org/wiki/Net_neutrality).
In addition, with the upcoming [HTTP/3](https://en.wikipedia.org/wiki/HTTP/3)
protocol being based on [QUIC protocol](https://quicwg.org/) which itself is
built on top of UDP, it is really important that UDP works.

## Measurements

The questions of interest further to be described in this document are if

* UDP works on any random port,
* UDP works on port `443`,
* UDP datagrams were not modified,
* UDP datagrams were not duplicated.

## Methodology

1. Run a UDP server.
2. Send UDP datagrams to the server.
3. Server echoes received datagrams.
4. Client validates the response.

NOTE, the tests MUST be excluded on port `53` which is used for DNS queries.
DNS by itself might be manipulated in different ways and deserves a separate
technique of its own. Hence is out of scope of this document.

### UDP Server

The same UDP server MAY be used for all measurements. UDP server is expected to
be listening on

1. multiple random ports from unprivileged port space - `1025..65535`. Say
   3 arbitrary chosen ports;
2. port `443`. HTTP/3 will be using UDP port `443`. So it is important to
   specifically test, if this port is not blocked.

All the server SHOULD do is echo received datagrams to the client that sent
them.

### UDP client

The UDP test flow is as follows

1. For each port in `[443, rand_port1, rand_port2, rand_port3]` send multiple
   datagrams. One datagram is not enough because UDP datagrams might be
   naturally lost on their way to the destination.
   on their
2. Generate random datagram of size <= 1400 bytes - no more than the usual
   [MTU](https://en.wikipedia.org/wiki/Maximum_transmission_unit#IP_MTUs_for_common_media)
   size. Each datagram must be random (unique), otherwise we won't be able to
   detect UDP datagram duplication.
3. Send the generated datagram to the server. Store the hashes of sent data
   to specific endpoints (IP:port pair).
4. Wait for up to 10 seconds for the response before declaring datagram as lost.
5. In the meantime, keep receiving incoming responses and validate them by
   hashing the payload of the datagram:
5.1. check if echoed datagram was already sent, if it was not, that means
     the tested network is modifying UDP datagrams;
5.2. if it was, increase the count of received datagrams by its hash;
6. Finally, traverse the collected data to form an appropriate measurement.
   The resulting measurement MUST always separate `443` from random ports, e.g.:
```json
{
  "443": "timeout",
  "random": "ok",
}
```

Pseudocode:

```python
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Keeps track of sent/received datagrams.
sent_to = {}

# Send multiple datagrams to different ports
for port in [443, rand_port1, rand_port2, rand_port3]:
    server_addr = (server_ip, port)
    sent_to[server_addr] = {}

    # Send 5 different datagrams to the same port
    for _ in range(5):
        data = rand_data(of_size=1400)

        sock.sendto(data, server_addr)
        # Initial result assigned to every request in case no response is
        # received.
        sent_to[server_addr][hash(data)] = Result.TIMEOUT

while not timeout(10 secs):
    (data, sender_addr) = sock.recvfrom()
    if hash(data) in sent_to[server_addr]:
        if sent_to[server_addr][hash(data)] == Result.TIMEOUT:
            sent_to[server_addr][hash(data)] = Result.RECEIVED
        else:
            sent_to[server_addr][hash(data)] = Result.DUPLICATE
    else:
        # We did not send this datagram to this endpoint
        sent_to[server_addr][hash(data)] = Result.MODIFIED

# Traverse sent_to and format the result
```

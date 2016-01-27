# Specification version number

2013-01-19_000

# Specification name

bridgeT

Note: This test is deprecated

# Test preconditions

  * Tor installed.
  * If testing pluggable transports, the host used for scanning the bridges
    should have the pluggable transport program.

# Expected impact

  * Detect whether or not a Tor bridge is reachable from a specific network
    vantage point on a network.
  * Implementations of bridget should not give the location of Tor bridges to
    adversaries, and thus should attempt to accurately catagorize tests
    according to such test's probability of providing the adversary
    information or oracles pertaining to the bridge's location.
  * Implementations should be automatable in a safe fashion, meaning that they
    should be capable of dynamically determining as best as possible the
    likelihood of the next iteration, ordered by probability of alerting
    adversaries of the bridge location, of alerting the adversaries. Test
    iterations should also be ceased if a test fails in a manner in which it
    is highly unlikely that any further tests would be capable of contacting
    the bridge. For example, if an ICMP-8 ping and a SYNACK cannot reach the
    bridge's ORPORT, it should be clear that a full connection following the
    Tor handshake protocol would likely be unsuccessful, and therefore
    conducting a bridge reachability test which completes a Tor handshake with
    the bridge should be skipped due to a high reachability information to
    adversarial location discovery ratio.
  * Basic active scanning tests which must be implemented: ICMP-8, TCP SYN,
    TCP SYNACK, TLS HANDSHAKE, FULL TOR PROTOCOL CONNECTION.

# Expected inputs

  * Import document or import data format:
    * A file with an IP[4/6]:PORT, one per line.
      Example:
            1.2.3.4:2323
            [2006:2000::0098]:2323
    * If the bridge has a pluggable transport enabled, it should be specified
      before the bridge's IP:PORT. Example:
            obfs2 66.66.66.66:443

# Expected output

  * Should output information in a format which is easily translatable for
    storage in BridgeDB, and parseable for use in metrics.

# Privacy considerations

  * Bridge location should not be devolved to adversaries.
  * If possible, the fact that a scan is running should be difficult to detect.

# Packet capture considerations

  * A montitoring interface is temporarily constructed, when permitted, in
    order to listen for responses to packets sent in ICMP, TCP, and TLS based
    tests.
  * Any packet captures should not be written to disk, due to the scanning
    host likely being located in the country of the adversarial party, which
    is assumed to have the ability to obtain access to information stored on
    the disk of the scanning host.
  * Any packet capture taken on the scanning host should be deleted after the
    scan test is completed.

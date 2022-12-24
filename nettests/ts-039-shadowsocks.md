# Specification version number

2022-12-23-000

# Specification name

Shadowsocks

# Test preconditions

An internet connection

# Expected impact

Ability to detect the censorship of fully-encrypted protocols, specifically Shadowsocks

# Expected inputs

None

# Test description

The main goal of the test is to inform the user (and the community) whether or not they are experiencing censorship on connections that send fully encrypted packets that appear random, as well as to record information about censored packets in order to better understand the censorship algorithm. The test seeks to accomplish these goals by doing the following:

1. If no IP is given by the user, select an IP from the list of IP addressed in the affected range
2. Complete a TCP handshake with the IP address and send a stream of zero bytes as a control test. If this control test succeeds then proceed with the test, otherwise end the test and return the error
3. Complete a TCP handshake with the IP address and send a stream of random bytes. If this connection times out, we attempt to connect once more to check for residual censorship. If the residual censorship test results in a timeout, we end the test, record information about the blocked packet, and inform the user they are experiencing censorship. Otherwise we continue with the test
4. Step 3 is repeated 19 more times to account for the blocking rate
5. If no errors occurred and the test was completed, all connections are then closed and the test informs the user they are not experiencing censorship.

# Expected output

## Parent data format

This is the base data format(s) that this test will adhere to (it is
implicit that it will follow df-000-base).

## Required output data

This is data that should be part of the base dataformat without which the
test cannot properly be interpreted.

## Data specification version number

Question: Isn't this implicit in the test specification number, is there a reason
why we should have two versions one for the data format and one for the
test specification? Would changing the dataformat not imply changing the
test version number?

## Semantics

List the extra keys that will be part of the report that are not part of
the parent data format. Be sure not to have keys that clash with the
parent data format.

## Possible conclusions

Based on the ouput data what conclusions can you draw?

## Example output sample

## Expected Post-processing efforts

Question: What exactly is meant by this? Is this meaning the possible
difficulties that a person doing post-processing may encouter?

# Privacy considerations

There are a few!

# Packet capture considerations

We capture all packets on the interface foo for bar units of time.

# Other notes

Bikesh{r}ed!

# tq-023 OpenVPN Control Hard Reset

It’s possible to use `P_CONTROL_HARD_RESET_CLIENT_V2` packet as “triggering
request” as there are some DPIs filtering OpenVPN traffic using those packets.
That is what was observed for both OpenVPN/TCP and OpenVPN/UDP. That is by no means a
comprehensive OpenVPN test.

TBD: what does Egypt do? They do something.

## Example
- OpenVPN notes in report on [Uganda Social Media Tax](https://ooni.torproject.org/post/uganda-social-media-tax/)

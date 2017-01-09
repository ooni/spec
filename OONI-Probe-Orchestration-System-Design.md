# OONI Probe Orchestration System Design

## Introduction

The goal of the OONI Probe Orchestration System (OPOS) is to support a more dynamic
and adaptive way of instrumenting instances of ooniprobe.

In particular the OPOS should allow us (the OONI project) to:

* Adjust the frequency at which periodic scheduled measurements are run.

* Trigger a measurement on a specific input (URL, IP, keyword, etc.) for a test
  that is already installed on the probe.

Out of scope is the ability to push new tests, as in test code, to probes.

## Design goals

### Resiliency

The OPOS should be as resilient as possible to censorship and should use
concepts such as [collateral freedom](https://en.greatfire.org/blog/2014/jan/collateral-freedom-faq).

Yet, it is still important that a probe can properly function even when the
OPOS is unreachable.

### Latency

The target latency for the OPOS is of around 1 minute. This means that from the
time a new instruction is inserted into the OPOS to the moment that the
affected probes receive it 1 minute should pass.

### Granular

It should be possible to give instructions based on:

* The country of a probe

* The Network of a probe

Moreover it should be possible to say something like:

* Run this instruction on at most `N` probes inside of network `K` of country
  `C`.

### Transparent

There should be full transparency over what is being scheduled to be run on
orchestrated probes. That is to say that it should be possible for anybody to
inspect the log of all the instructions and determine which ones have affected
their probe.

## High level overview

Components:

**OPOS Client**: This is generally an instance of ooniprobe (or
ooniprobe-mobile) that is subscribing to the OPOC event feed.

**OPOS Event feed**: This is the backend component responsible for emitting
events to clients and informing them of what they should be doing.

**OPOS Management Interface**: This is the backend management interface used by
the OONI team to configure the event feed and instrument probes.

**OPOS Event log**: Through this it is possible to inspect the history of
instrumented events.

A **OPOS Client** will subscribe to the **OPOS Event feed** to receive
information on what it should do.

When somebody with proper access permissions adds an event to via the **OPOS
Management Interface** all the subscribed probes that are affected by that
event will be notified and will begin performing the specified action.

A user interested in seeing what has been scheduled in the past can visit the
**OPOS Event log** and see a history of what has happenned.

## Transport protocol requirements

We use the term "Transport" loosely here to mean the protocol that is being
used for communicating between the **OPOS Client** and the **Event Feed**.

It will most likely be something similar to WebSockets or some sort of pub-sub
implementation.

The requirements for this are:

* It MUST be possible to signal the **OPOS Client** when a new event that
  interests them is scheduled.

* It SHOULD be possible to place the **OPOS Event feed** behind a domain front
  or leverage some other collateral freedom like principle (for example hosting
  it on github.com) to avoid it being blocked hence being resilient to censorship.

* It SHOULD be possible to know how many *active* **OPOS Clients** there are at
  a given time.

## Actions

Actions represent operations to be performed by **OPOS Clients** and are
submitted via the **OPOS Management Interface**. **OPOS Clients** are notified
of actions via the **OPOS Event feed**.

It is possible to specify a target for an action so that only clients that
match the target criteria will respond to the specified action.

When no target is specified the action will affect all clients that support the
specified action.

It is sometimes desirable to avoid having all probes run the specific action at
the same time, for example because it could lead to a denial of service of the
affected resources, to this end it's also possible to delay the action by a random delay
by specifying the `random_delay` key.

We use JSON serialization for representing the message structures inside of
this document, however if due to other contraints JSON is not an adequate
serialization protocol we are not necessarily tied to it.

The base data format is the following:

```
{
    "target": {
        "country_codes": [],
        "asns": [],
        "probe_ids": []
    },
    "action": {
        "random_delay": 0
    }
}
```

`country_codes`: is a list of [ISO 3166-2](https://en.wikipedia.org/wiki/ISO_3166-2) two letter
country code of the target countries. To indicate that it should affect ALL
countries you should use the User asigned country code `AA` or an empty list.

`asns`: is a list of Authonomous System numbers that should be affected by this
update. To specify no restriction on ASN you should either provide an empty
list or use the `AS0`.

`probe_ids`: this specifies the `probe_ids` that should be affected by the
action. To affect all `probe_ids` set it to the empty list.

A **OPOS Client** should use the following logic to determine if they should
react to a given action:

```
let "probe_asn" be the Authonomous System number of the probe or AS0 if unknown

let "probe_cc" be the two letter country code of the probe or ZZ if unknown

let "probe_id" be the unique identifier of the probe

let "run" be a bool initialised to true

BEGIN
if country_codes is empty or contains AA
    set run to run & true
else
    if country_codes contains probe_cc
        set run to run & true
    else
        set run to run & false

if asns is empty or contains AS0
    set run to run & true
else
    if asns contains probe_asn
        set run to run & true
    else
        set run to run & false

if probe_ids is empty
    set run to run & true
else
    if probe_ids contains probe_id
        set run to run & true
    else
        set run to run & false
END

run now contains a boolean value that if true means this client should execute
the action, false if it should not.
```

`random_delay`: is an upper bound on the number of seconds to delay the action
by. For example by specifying `"random_delay": 60` the action will be
triggerred after a number of seconds going from `0-60`.

It should be possible for somebody interacting with the Management Interface to
schedule the following types of actions.

#### Run test

This action is used to instruct a probe to run a certain test.

Example:

```json
{
    "action": {
        "name": "Test web connectivity of https://torproject.org/"
        "type": "run_ooni",
        "payload": {
            "test_name": "web_connectivity",
            "url": "https://torproject.org/"
        }
    }
}
```

#### Schedule test

This action is used to schedule a test to be run:

Example:

```json
{
    "action": {
        "name": "Schedule to check reachability of https://torproject.org/ daily",
        "type": "schedule_ooni",
        "payload": {
            "schedule": "@daily",
            "until": "2018-12-23",
            "id": "some unique identifier",
            "test_name": "web_connectivity",
            "url": "https://torproject.org/"
        }
    }
}
```

`schedule`: a cron-like definition of how often the action should be run.

`until`: when we should invalidate this schedule. If this key is not provided we consider it to exist forever.

`id`: a unique identifier for this scheduled test. This is used to then issue unsubscribe actions.


#### Unschedule test

This action is used to unschedule a test to be run by referencing it's ID.

Example:

```json
{
    "action": {
        "name": "Unschedule to check reachability of https://torproject.org/ daily",
        "type": "unschedule_ooni",
        "payload": {
            "id": "some unique identifier"
        }
    }
}
```

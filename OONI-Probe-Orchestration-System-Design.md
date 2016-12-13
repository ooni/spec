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



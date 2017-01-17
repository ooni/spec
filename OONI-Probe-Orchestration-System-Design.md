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

**OPOS Scheduler**: This is the component that knows the status of the jobs
scheduled via the OPOS Management Interface, which OPOS Clients have taken them
on and their progress.

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

## Jobs

Jobs represent operations to be performed by **OPOS Clients** and are submitted
via the **OPOS Management Interface**. **OPOS Clients** are notified of actions
via the **OPOS Event feed**.

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

```json
{
    "name": "I am a happy OPOS schedule",
    "filter": {
        "where": {
            "probe_cc": {
                "or": [
                    {"in": ["IT", "NZ"]},
                    {"limit": 10, "in": ["US"]}
                ]
            },
            "probe_asn": "",
            "probe_id": "",
            "probe_family": "",

            "platform": "macos", # Can be one of lepidopter, macos, linux, mobile, android, ios

            "network_type": "wifi" # can be one of wifi, mobile, 3g, 4g, edge
            "available_bandwidth": {"gt": 10000}
        }
    },
    "schedule": "R1/2018-12-16T19:20:30Z/P",
    "delay": 0,
    "task": {
        "name": "Check for accessibility of https://torproject.org/",
        "ooni": {
            "test_name": "web_connectivity",
            "url": "https://torproject.org/"
        }
    }
}
```

The where clause in the filter definition is an implementation of the [loopback
style filters](https://github.com/strongloop/loopback-filters), but with "in"
in place of "inq".

run now contains a boolean value that if true means this client should execute
the action, false if it should not.

`delay`: is an upper bound on the number of seconds to delay the action by. For
example by specifying `"delay": 60` the action will be triggerred after a
number of seconds going from `0-60`.

`schedule`: The scheduling for the job, in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. Consists of 3 parts separated by /:

* The number of times to repeat the job: Rn to repeat n times, or R to repeat forever

* The start time of the job in ISO 8601 (YYYY-MM-DDThh:mm:ssTZ, where TZ is the timezone of `Z` for UTC).
  An empty start time means start immediately.

* The run interval, defined following the ["Duration" component of the ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#Durations) standard.

The Management Interface will assign to a given job a unique id (hereafter
referred to as `job_id`) that can be used to unschedule jobs.

It should be possible for somebody interacting with the Management Interface to
schedule the following types of actions.

#### Run test

This action is used to instruct a probe to run a certain OONI test once. For
sake of clarity we omit the common elements from the above format.

In practice running a test once means scheduling a test to be run only once at
a given time.

Example:

```json
{
    "schedule": "R1/2018-12-16T19:20:30Z/P",
    "task": {
        "name": "Check for accessibility of https://torproject.org/",
        "ooni": {
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
    "schedule": "R//P1D",
    "task": {
        "name": "Check for accessibility of https://torproject.org/",
        "ooni": {
            "test_name": "web_connectivity",
            "url": "https://torproject.org/"
        }
    }
}
```

#### Unschedule job

This action is used to unschedule a job to be run by referencing it's ID.

Example:

```json
{
    "unschedule": "job_id"
}
```

### Job lifecycle


![OPOS Job Lifecycle](http://g.gravizo.com/g?@startuml;
    [*] --> READY;
    READY --> ASSIGNED;
    ASSIGNED --> STARTING;
    ASSIGNED --> REJECTED;
    STARTING --> RUNNING;
    RUNNING --> COMPLETED;
    COMPLETED --> [*];
    @enduml
)


The OPOS Scheduler keeps track of the lifecycle of a job. With respect to an
**OPOS Client** a job can be in one of the following states:

* **READY**: this is the state in which a job is when it is first added via the OPOS Management Interface.

* **ASSIGNED**: this is the state a job is in when it is given to a certain
  OPOS Client. At this point a OPOS Client can either choose to start running
  the task, in which case it comunicates this to the OPOS Scheduler and the task state becomes **STARTING**.

* **STARTING**: this is the state a job is in when the OPOS Client informs the OPOS Scheduler that it will start running a job.

* **REJECTED**: if an OPOS Client cannot run a certain job (either because of
  some the constraints not being satisfied or something else) it informs the
  scheduler of such and the task state becomes **REJECTED**.

* **RUNNING**: when the job has started it enters this state. The OPOS Client
  is responsible for reporting back to the **OPOS Scheduler** updates on the
  progress of any given task.

* **COMPLETED**: when a job has finished executing it enters the COMPLETED state.

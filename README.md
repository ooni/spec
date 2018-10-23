# OONI Spec

The OONI testing methodology is openly specified as part of OONI Spec. This
includes all the experiments that we run, the backend components used as part
of test and the data formats.

The way in which we do these specifications is similar to the RFC (Request For
Comments) process.

This makes it possible to have a deep understanding of how OONI tests work,
explain the assumption we make in them and make it possible to create
independent implementations.

*Nettests*

Are network experiments in a box that deliver some meaningful results to end users.

*Techniques*

Are strategies that we follow for implementing nettests, hypothesis we are
interesting in testing and implementation details for each target platform.

*Data formats*

Define how data is presented to end users or analysts.

*Backends*

Are core OONI infrastructure components that are necessary to carry out experiments.

We aim to have the specifications for backends eventually be part of the code repository of the relevant backend and have only links pointing to them in here.

## New proposal process

If you are interesting in having a new experiment be part of OONI, that's great!

The process for suggesting a new experiment is as follows:

1. You figure out if you want to specify a technique (it's just an idea or some
   extra data we should collect as part of many tests) or full fledged nettest
   (it's delivering some new and interesting results conclusions to end users)

2. You copy the nettest template or create a new technique document

3. File a pull requests on github

4. Discussion happens on github and it's merged

5. If it's feasible, you implement it as a test or technique in measurement-kit

6. If it's useful for our users to run it, we ship it in OONI Probe

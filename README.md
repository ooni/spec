# OONI Spec

The OONI testing methodology is openly specified as part of OONI Spec. This
includes all the experiments that we run, the backend components used as part
of test and the data formats.

The way in which we do these specifications is similar to the RFC (Request For
Comments) process.

This makes it possible to have a deep understanding of how OONI tests work,
explain the assumption we make in them and make it possible to create
independent implementations.

To get an introduction of how we operate from the point of view of OONI Probe,
i.e. the software that users can install, please see [the specific
documentation describing that](probe). New developers would ideally want
to be familiar with this document to understand the context.

## Terminology

*Nettests (aka experiments)*

Are network experiments that deliver some meaningful results to end users. See
the [nettests](nettests) directory.

*OONI Probe (aka the Probe)*

The software that users run to perform nettests. See the [probe](probe) directory.

*Techniques*

Are strategies that we follow for implementing nettests, hypothesis we are
interested in testing and implementation details for each target platform. See
the [techniques](techniques) directory.

*Data formats*

Define how data is presented to end users or analysts. See the
[data-formats](data-formats) directory.

*Backends*

Are core OONI infrastructure components that are necessary to carry out experiments. See
the [backends](backends) directory.

## New proposal process

If you are interested in having a new experiment be part of OONI, that's great!

The process for suggesting a new experiment is as follows:

1. You figure out if you want to specify a technique (it's just an idea or some
   extra data we should collect as part of many tests) or full fledged nettest
   (it's delivering some new and interesting results conclusions to end users)

2. You copy the nettest template or create a new technique document

3. File a pull requests on github

4. Discussion happens on github and it's merged

5. If it's feasible, you implement it as a test or technique in measurement-kit

6. If it's useful for our users to run it, we ship it in OONI Probe

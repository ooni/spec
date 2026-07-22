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

## Contributing

Please, see [CONTRIBUTING.md](CONTRIBUTING.md).

# Feature Specification

All new features shall be specified before they are implemented. When the
feature is a feature of the client (ooniprobe) it is sufficient to specify it
inside of a ticket. Features that are to be part of the backend (oonib) shall
be specified inside of the [ooni backend
specification](https://github.com/TheTorProject/ooni-spec/blob/master/oonib.md).

Newly developed tests that consistute part of the core ooniprobe tests shall be
specified as part of the ooni-spec repository and should follow the [test
specification template](https://github.com/TheTorProject/ooni-spec/blob/master/test-specs/ts-000-example.md).

An issue shall then be created for the feature and closed once it has been
merged into the master branch.

# Code Review

When new tests are developed they shall be deployed immediately on non m-lab
collectors and backend, while they must pass the approval from m-lab before
they will be fit to run on their platform.

# Testing

Code coverage is measured via coveralls and the results for such tests can be
found [here](https://coveralls.io/r/TheTorProject/ooni-probe).

# Tagging and Signing of a release

All tags should be incremental and they will be signed with either of the
following GPG keys:

```
pub   4096R/150FE210 2011-10-23 [expires: 2014-05-04]
Key fingerprint = 46E5 EF37 DE26 4EA6 8DCF  53EA E3A2 1297 150F E210
uid                  Arturo Filastò <art@torproject.org>
uid                  Arturo Filastò <arturo.filasto@logioshermes.org>
uid                  Arturo Filastò <arturo@filasto.net>
uid                  Arturo Filastò <art@fuffa.org>
uid                  Arturo Filastò <art@globaleaks.org>
uid                  Arturo Filastò <art@baculo.org>
uid                  Arturo Filastò <hellais@gmail.com>
sub   4096R/F423B27C 2011-10-23 [expires: 2014-05-04]
```

# Build systems & environments

We currently only support packages for debian and ubuntu based systems.

# Release announcement

Once a new stable release is tagged a new changelog entry shall be written and
the corresponding changelog entry shall be updated.

Following a new release we should write an email to the ooni-dev mailing list
announcing the new release.

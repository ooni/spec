# Contributing to ooni/spec

This is an open source project, and contributions are welcome! You are welcome
to open pull requests. An open pull request will be reviewed by a core
developer. The review may request you to apply changes. Once the assigned
reviewer is satisfied, they will merge the pull request.

## OONI Software Development Guidelines

Please, make sure you read [OONI Software Development Guidelines](
https://ooni.org/post/ooni-software-development-guidelines/).

When you are developing a new nettest (aka experiment) you should also
read [the probe-cli development guidelines](https://github.com/ooni/probe-cli/blob/master/CONTRIBUTING.md).

## Opening issues

As regards opening issues, please open issues pertaining to this repository at
https://github.com/ooni/probe/issues. Please, before opening a new issue,
check whether the issue or feature request you want us to consider has not
already been reported by someone else.

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

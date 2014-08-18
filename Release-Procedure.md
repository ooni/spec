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

Before a release is fit for release it must pass the automated and manual tests
listed below:

## Unit tests

```
sudo trial ooni
```

Must produce no errors.

## Build source distribution and install

It should be possible to build a source distribution of ooniprobe. Install it
inside of a fresh virtuale environment and then run all the manual tests
needed.

```
rmvirtualenv ooni-testsdist; mkvirtualenv ooni-testsdist
pip install dist/ooniprobe-$OONIPROBE_VERSION.tar.gz
```

## Usage tests

First cd into a temporary directory so that you don't mess up the code tree and
you import what you have just installed.

```
cd `mktemp -d 2>/dev/null || mktemp -d -t 'ooni'`
```

### Running decks

```
ooniprobe -i ~/.virtualenvs/ooni-testsdist/share/ooni/decks/mlab.deck
ooniprobe -i ~/.virtualenvs/ooni-testsdist/share/ooni/decks/fast_no_root.deck
ooniprobe -i ~/.virtualenvs/ooni-testsdist/share/ooni/decks/complete_no_root.deck
```

While this is running you may as well open another shell, get into that
virtualenv and make sure oonireport is working as it should.

Check to see if by running:

```
oonireport status
```

You see a list of "Reports in progress". There should be at least 4 of them.

The above commands should not throw any exceptions and you should now see
inside of your current working directory the following list of files:

```
report-dns_consistency-2014-08-18T134642Z.yamloo
report-http_header_field_manipulation-2014-08-18T134555Z.yamloo
report-http_header_field_manipulation-2014-08-18T134625Z.yamloo
report-http_header_field_manipulation-2014-08-18T134642Z.yamloo
report-http_host-2014-08-18T134642Z.yamloo
report-http_invalid_request_line-2014-08-18T134625Z.yamloo
report-http_invalid_request_line-2014-08-18T134642Z.yamloo
report-http_requests-2014-08-18T134642Z.yamloo
```

### Running single tests

The following command should produce the list of tests installed on your
system:

```
ooniprobe -s
```

The following commands should all succeed and produce some measurements:

```
ooniprobe -n manipulation/http_header_field_manipulation
ooniprobe -n blocking/http_requests -f httpo://ihiderha53f36lsd.onion/input/37e60e13536f6afe47a830bfb6b371b5cf65da66d7ad65137344679b24fdccd1
```

### Testing vagrant installation

To setup and test ooniprobe on a fresh ubuntu installation with
[Vagrant](https://www.vagrantup.com):

```
vagrant destroy -f
vagrant up
vagrant ssh
```

You should now be logged into the vagrant machine with ooniprobe installed.

To make sure everything went as expected try running:

```
sudo ooniprobe -i /usr/share/ooni/decks/fast.deck
```

# Tagging and Signing of a release

To create a new release you should update the following files with the new
version information:

  * ooni/__init__.py: set __version__ = "$OONI_VERSION"

  *  Changelog.md: to include a new changelog entry with the introduced
     changes.

  * debian/changelog: with a new entry for the new release

Once this is done you should commit the changes with a message like this:

```
git commit -a -m 'update ooniprobe to $OONI_VERSION'
```

You can now tag and sign a new release with:

```
git tag -s -a 'v$OONI_VERSION'
```

Then write a reasonable message inside of the tag message body. The format to
follow should be:

```
ooniprobe $OONI_VERSION

$SOME_DESCRIPTION_OR_CHANGELOG_OR_WHATEVER
```

All tags should be incremental and they will be signed with either of the
following GPG keys:

```
pub   4096R/150FE210 2011-10-23 [expires: 2014-11-24]
      Key fingerprint = 46E5 EF37 DE26 4EA6 8DCF  53EA E3A2 1297 150F E210
      uid                  Arturo Filastò <art@torproject.org>
      uid                  Arturo Filastò <arturo@filasto.net>
      uid                  Arturo Filastò <arturo.filasto@logioshermes.org>
      uid                  Arturo Filastò <art@fuffa.org>
      uid                  Arturo Filastò <art@globaleaks.org>
      uid                  Arturo Filastò <art@baculo.org>
      uid                  Arturo Filastò <hellais@gmail.com>
      sub   4096R/F423B27C 2011-10-23 [expires: 2014-11-24]
```

## Versioning scheme

All OONI tools follow [semantic versioning](http://semver.org/).

# Build systems & environments

We currently only support packages for debian and ubuntu based systems.

# Release announcement

Once a new stable release is tagged a new changelog entry shall be written and
the corresponding changelog entry shall be updated.

Following a new release we should write an email to the ooni-dev mailing list
announcing the new release.

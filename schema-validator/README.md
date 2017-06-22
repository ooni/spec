# OONI Report Schema Validator

This folder contains JSON Schemas for validating OONI Probe reports.

## Folder structure

```
├── requirements.txt 	required python libraries
├── schemas 			JSON Schemas
├── test-specs 			JSON representation of markdown test-specs
├── validate-all.sh 	utility script for validating all test-specs against
│ 							header schema and specific test schema
└── validate.py 		validator script ( run with -h for help )

## JSON Schema

> JSON Schema is a vocabulary that allows you to annotate and validate JSON documents.

Quoted from [json-schema.org][json-schema-website]

An useful resource for understanding how to use JSON Schema properly, without
looking at RFC and implementation details is [here][understanding-json-schema].

An useful tool for generating/editing JSON schema via a graphical editor could
be found [here][jsonschema.net].

## How to validate

Validating JSON Report file can be done using `validate.py`: pass to the python
script the schema to be used for validation and the JSON file to validate.

For proper CLI instruction run `validate.py -h`.

## TODO

- Add specific test schemas: currently the only schema available is the Header
  schema. Specific schema tests are missing.
- Gather the proper format for YAML test-specs: some specifications are still
  in YAML format. They need to be ported to JSON.
- Produce example JSON from JSON schemas: each file in the test-specs folder
  contains an "example" paragraph with a JSON example of the Report payload.
  This payload could be generated directly from JSON schemas. A nice tool for
  the work could be [json-schema-faker][json-schema-faker]


[json-schema-website]: http://json-schema.org/
[understanding-json-schema]: https://spacetelescope.github.io/understanding-json-schema/
[json-schema-faker]: https://github.com/json-schema-faker/json-schema-faker/
[jsonschema.net]: https://jsonschema.net

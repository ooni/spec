#!/usr/bin/env python3

import argparse
import jsonschema
import os
import subprocess
import sys
import json
import yaml


def configure_parser():
    usage = "usage: validators/generic.py [options] file.json"
    description = 'Validate json report'
    parser = argparse.ArgumentParser(usage=usage, description=description)
    parser.add_argument("-s", "--schema",
                        help="JSON schema file to be used as validator",
                        required=True)
    parser.add_argument("file",
                        help="JSON file to validate")
    return parser


def verify_args(args):
    if not os.path.isfile(args.file):
        print("File {} does not exists".format(args.file))
        sys.exit(1)

    if not args.file.endswith('json'):
        print("{} is not a valid target file. Only JSON files allowed".format(args.file))
        sys.exit(1)

    if not os.path.isfile(args.schema):
        print("Schema file {} does not exists".format(args.schema))
        sys.exit(1)

    if not args.schema.endswith('yml'):
        print("{} is not a valid schema file. Only YAML files allowed".format(args.schema))
        sys.exit(1)


def get_parsed_arguments():
    parser = configure_parser()
    args = parser.parse_args()
    verify_args(args)
    return args


def load_json_schema(schema_file):
    return yaml.load(open(schema_file, 'r'))


def load_json_data(json_file):
    with open(os.path.abspath(json_file)) as in_file:
        return json.load(in_file)


def validate(obj, json_schema):
    jsonschema.validate(obj, json_schema)


if __name__ == "__main__":
    args = get_parsed_arguments()
    json_schema = load_json_schema(args.schema)
    print("Using validator: {} - {}".format(args.schema, json_schema['title']))
    print("Verifing {}".format(args.file))
    obj = load_json_data(args.file)
    validate(obj, json_schema)
    print("JSON validation passed!")

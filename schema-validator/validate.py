#!/usr/bin/env python3

import os
import sys
import json
import random
import argparse
import subprocess

import yaml
import requests
import jsonschema

def configure_parser():
    usage = "usage: validators/generic.py [options] file.json"
    description = 'Validate json report'
    parser = argparse.ArgumentParser(usage=usage, description=description)
    parser.add_argument("-s", "--schema",
                        help="JSON schema file to be used as validator",
                        required=True)
    parser.add_argument("-f", "--file", help="JSON file to validate")
    return parser


def verify_args(args):
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
    with open(schema_file) as in_file:
        return yaml.load(in_file)

def validate_filepath(filepath, schema):
    print("Verifing {}".format(filepath))
    with open(os.path.abspath(filepath)) as in_file:
        return json.load(in_file)
    return jsonschema.validate(obj, schema)

# XXX these test_names currently trigger a 500 error in the pipeline
# "bridget",
# "dns_spoof",
# "dns_injection",
# "captiveportal",
# "psiphon_test",
# "openvpn_client_test",
# "lantern_circumvention_tool_test",

test_names = [
    "meek_fronted_requests_test",
    "web_connectivity",
    "dns_consistency",
    "http_requests",
    "http_host",
    "http_header_field_manipulation",
    "http_invalid_request_line",
    "tcp_connect",
    "multi_protocol_traceroute",
    "bridge_reachability",
    "vanilla_tor",
    "web_connectivity",
    "whatsapp",
    "facebook_messenger",
    "telegram",
    "dash"
]

def get_random_url(test_name):
    j = requests.get("https://api.ooni.io/api/v1/measurements?test_name={}".format(test_name)).json()
    return random.choice(j["results"])["measurement_url"]


def validate_api_sampling(schema):
    for test_name in test_names:
        url = get_random_url(test_name)
        obj = requests.get(url).json()
        print("Verifing {} ({})".format(test_name, obj["report_id"]))
        jsonschema.validate(obj, schema)

def main():
    args = get_parsed_arguments()
    json_schema = load_json_schema(args.schema)

    print("Using validator: {} - {}".format(args.schema, json_schema['title']))
    if args.file:
        validate_filepath(args.file, json_schema)
    else:
        validate_api_sampling(json_schema)
    print("JSON validation passed!")

if __name__ == "__main__":
    main()

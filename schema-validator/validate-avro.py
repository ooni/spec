import json
from copy import deepcopy
import unittest
from pprint import pprint

from glob import glob
from fastavro import validate, parse_schema

test_names = [
    "web_connectivity",
    "http_invalid_request_line",
    "http_header_field_manipulation",
    "dash",
    "facebook_messenger",
    "telegram",
    "vanilla_tor",
    "whatsapp",
    "tcp_connect",
    "meek_fronted_requests_test",

#    "dns_consistency",
#    "http_requests",
#    "http_host",
#    "multi_protocol_traceroute",
#    "bridge_reachability"
]

def common_schemas():
    schema_list = []
    for name in ['DNSQuery', 'HTTPRequestResponse']:
        with open('schemas/{}.avsc'.format(name)) as in_file:
            schema_list.append(json.load(in_file))
    return schema_list

def test_schema(test_name, base_schema):
    print("validating {}".format(test_name))
    with open('schemas/{}.avsc'.format(test_name)) as in_file:
        test_keys = json.load(in_file)

    schema = deepcopy(base_schema)
    schema['fields'].append({
        'name': 'test_keys',
        'type': test_keys
    })
    schema_list = common_schemas() + [schema]
    parsed_schema = parse_schema(schema_list)

    with open('test-specs/{}.json'.format(test_name)) as in_file:
        validate(json.load(in_file), parsed_schema)

class TestAvroSchema(unittest.TestCase):
    def setUp(self):
        with open('schemas/measurement.avsc') as in_file:
            self.base_schema = json.load(in_file)

    def test_all_schemas(self):
        for tn in test_names:
            test_schema(tn, self.base_schema)

if __name__ == "__main__":
    unittest.main()

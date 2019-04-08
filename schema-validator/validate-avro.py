import json
from copy import deepcopy
import unittest
from pprint import pprint

from glob import glob
from fastavro import validate, parse_schema

def test_schema(test_name, base_schema):
    print("validating {}".format(test_name))
    with open('schemas/{}.avsc'.format(test_name)) as in_file:
        test_keys = json.load(in_file)

    schema = deepcopy(base_schema)
    schema['fields'].append({
        'name': 'test_keys',
        'type': test_keys
    })
    parsed_schema = parse_schema(schema)

    with open('test-specs/{}.json'.format(test_name)) as in_file:
        validate(json.load(in_file), parsed_schema)

class TestAvroSchema(unittest.TestCase):
    def setUp(self):
        with open('schemas/measurement.avsc') as in_file:
            self.base_schema = json.load(in_file)

    def test_all_schemas(self):
        with open('test_meta.json') as in_file:
            test_meta = json.load(in_file)

        for tn in test_meta['test_names']:
            test_schema(tn, self.base_schema)

if __name__ == "__main__":
    unittest.main()

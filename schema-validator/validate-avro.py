import json
from glob import glob
from fastavro import validate, parse_schema

with open('schemas/measurement.avsc') as in_file:
    schema = json.load(in_file)

#print(schema)
parsed_schema = parse_schema(schema)

ok_specs = []
fail_specs = []
for fn in glob('test-specs/*.json'):
    print(fn)
    with open(fn) as in_file:
        try:
            validate(json.load(in_file), parsed_schema)
            ok_specs.append(fn)
        except Exception as exc:
            fail_specs.append([fn, exc])


print("OK")
for fn in ok_specs:
    print(fn)

for fn, exc in fail_specs:
    print("FAIL %s %s" % (fn, exc))

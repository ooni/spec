import os
import subprocess
import sys
import argparse

usage = "usage: validators/header.py [options] folder/file"
description = 'Validate json report headers'
parser = argparse.ArgumentParser(usage=usage, description=description)
parser.add_argument("-s", "--schema",
                  help="JSON schema file to be used as validator",
                  required=True)
parser.add_argument("file",
					help="JSON file to validate")

args = parser.parse_args()

print(args)

file_list = []
if not os.path.isfile(args.file):
	print("File {} does not exists".format(args.file))
	sys.exit(1)
else:
	if not args.file.endswith('json'):
		print("{} is not a valid target file. Only JSON files allowed".format(args.file))
		sys.exit(1)

if not os.path.isfile(args.schema):
	print("Schema file {} does not exists".format(args.schema))
	sys.exit(1)
else:
	if not args.schema.endswith('json'):
		print("{} is not a valid schema file. Only JSON files allowed".format(args.schema))
		sys.exit(1)

print("Using validator: {}".format(args.schema))

print("Verifing {}".format(args.file))
filename = os.path.abspath(args.file)
return_code = subprocess.call(['jsonschema', '-i', filename, args.schema])
if return_code == 0:
	print("OK")
else:
	print("Validation failed, please check")

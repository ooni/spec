#!/bin/bash

for file in test-specs/*.json; do
	echo ""
	./validate.py -s schemas/header.yml $file
	specific_schema="$(basename $file)"
	specific_schema="${specific_schema:7}"
	specific_schema="${specific_schema%.*}.yml"
	if [ -e "schemas/$specific_schema" ]; then
		echo "--"
		validate.py -s "schemas/$specific_schema" $file
	fi
done

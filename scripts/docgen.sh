#!/bin/bash

# Generates python documentation. Move html files to docs dictionary
if [ -z ${RESMONSENSORENV+x} ]; then
    source ./resmon-sensor.env
fi

rm -rf ./docs
mkdir ./docs/

MODULES=`find -name '*.py' | sed -e 's/\//./g' | sed -e 's/\.\.//g' \
    | sed -e 's/\.py//g' | sed 's|.__init__||'`
echo $MODULES
pydoc3 -w $MODULES
for f in ./*.html ; do mv "$f" ./docs/ ; done

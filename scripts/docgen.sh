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

OUT=`for f in $MODULES ; do \
    pydoc3 -w $f; \
    mv "$f.html" ./docs/ ; done`

echo "$OUT"
if [[ "$OUT" =~ "problem in" ]]; then
    exit 1
else
    exit 0
fi

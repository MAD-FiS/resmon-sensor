#!/bin/bash

# Run tests
if [ -z ${RESMONSENSORENV+x} ]; then
    source ./resmon-sensor.env
fi

python3 test/*.py

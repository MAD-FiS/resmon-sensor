#!/bin/bash

# Run tests
if [ -z ${RESMONSENSORENV+x} ]; then
    source ./data/resmon-sensor.env
fi

python3 test/testSensor.py

#!/bin/bash

# Run tests
if [ -z ${RESMONAUTHENV+x} ]; then
    source ./resmon-sensor.env
fi

python3 test/testSensor.py

import unittest
from unittest.mock import MagicMock

import sensor
import json

class TestSensor(unittest.TestCase):

    def test_sensorBuffer(self):
        sensorObj = sensor.Sensor()
        sensorObj.getAllData = MagicMock(return_value={'CPU_USAGE':20, 'RAM_USAGE':40})
        sensorBufferObj = sensor.SensorBuffer(sensorObj)
        sensorBufferObj.performMeasurement()
        jsonData = sensorBufferObj.getJsonData()
        data = json.loads(jsonData)

        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['CPU_USAGE'], 20)
        self.assertEqual(data[0]['RAM_USAGE'], 40)

    def test_sensor(self):
        sensorObj = sensor.Sensor()
        sensorObj.getCpuUsage = MagicMock(return_value=20)
        sensorObj.getRamUsage = MagicMock(return_value=80)

        data = sensorObj.getAllData()

        self.assertEqual(data['CPU_USAGE'], 20)
        self.assertEqual(data['RAM_USAGE'], 80)

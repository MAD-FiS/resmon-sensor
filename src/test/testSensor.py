import unittest
from unittest.mock import MagicMock

import sensor

class TestSensor(unittest.TestCase):

    def test_sensorBuffer(self):
        sensorObj = sensor.Sensor()
        sensorObj.getCpuUsage = MagicMock(return_value=20)
        sensorObj.getRamUsage = MagicMock(return_value=40)
        sensorObj.prepareModules()
        sensorBufferObj = sensor.SensorBuffer(sensorObj)
        sensorBufferObj.performMeasurement()
        data = sensorBufferObj.getData()

        print(sensorObj.getRamUsage())

        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['CPU_USAGE'], 20)
        self.assertEqual(data[0]['RAM_USAGE'], 40)

    def test_sensor(self):
        sensorObj = sensor.Sensor()
        sensorObj.getCpuUsage = MagicMock(return_value=20)
        sensorObj.getRamUsage = MagicMock(return_value=80)
        sensorObj.prepareModules()

        data = sensorObj.getAllData()

        self.assertEqual(data['CPU_USAGE'], 20)
        self.assertEqual(data['RAM_USAGE'], 80)

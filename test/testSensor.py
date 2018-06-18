import unittest
import src.sensor
from unittest.mock import MagicMock


class TestSensor(unittest.TestCase):

    def test_sensorBuffer(self):
        sensorObj = src.sensor.Sensor()
        sensorObj.getCpuUsage = MagicMock(return_value=20)
        sensorObj.getRamUsage = MagicMock(return_value=50)
        sensorObj.getVirtualMemTotal = MagicMock(return_value=4000)
        sensorObj.getVirtualMemAvailable = MagicMock(return_value=2000)
        sensorObj.getLoggedUsersCount = MagicMock(return_value=10)
        sensorObj.getProcessesCount = MagicMock(return_value=235)
        sensorObj.prepareModules()
        sensorBufferObj = src.sensor.SensorBuffer(sensorObj)
        sensorBufferObj.performMeasurement()
        data = sensorBufferObj.getData()

        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['cpu_usage'], 20)
        self.assertEqual(data[0]['ram_usage'], 50)
        self.assertEqual(data[0]['virtual_mem_total'], 4000)
        self.assertEqual(data[0]['virtual_mem_available'], 2000)
        self.assertEqual(data[0]['legged_users_count'], 10)
        self.assertEqual(data[0]['processes_count'], 235)

    def test_sensor(self):
        sensorObj = src.sensor.Sensor()
        sensorObj.getCpuUsage = MagicMock(return_value=20)
        sensorObj.getRamUsage = MagicMock(return_value=50)
        sensorObj.getVirtualMemTotal = MagicMock(return_value=4000)
        sensorObj.getVirtualMemAvailable = MagicMock(return_value=2000)
        sensorObj.getLoggedUsersCount = MagicMock(return_value=10)
        sensorObj.getProcessesCount = MagicMock(return_value=235)
        sensorObj.prepareModules()

        data = sensorObj.getAllData()
        self.assertEqual(data['cpu_usage'], 20)
        self.assertEqual(data['ram_usage'], 50)
        self.assertEqual(data['virtual_mem_total'], 4000)
        self.assertEqual(data['virtual_mem_available'], 2000)
        self.assertEqual(data['legged_users_count'], 10)
        self.assertEqual(data['processes_count'], 235)


if __name__ == '__main__':
    unittest.main()

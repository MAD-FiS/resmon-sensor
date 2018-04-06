"""Contains class connected with gathering and buffering data"""

import psutil
import datetime
import json

class Sensor:
    """This class is responsible for reading various parameters from system"""
    def __init__(self):
        pass

    def getAllData(self):
        """Return all data and return it in dictionary"""
        data = {}
        data['CPU_USAGE'] = self.getCpuUsage()
        data['RAM_USAGE'] = self.getRamUsage()
        data['DATE'] = str(datetime.datetime.now())
        return data

    def getCpuUsage(self):
        """Return CPU usage in percentage"""
        return psutil.cpu_percent()

    def getRamUsage(self):
        """Return RAM usagre in percenrage"""
        return psutil.virtual_memory()[2]

class SensorBuffer:
    """Class responsible for buffering data gathered by sensor"""
    def __init__(self, sensor):
        """Constructor takes sensor, which will be used for getting data"""
        self.sensor = sensor
        self.measurements = []

    def performMeasurement(self):
        """Performs measurement and add data to buffer"""
        self.measurements.append(self.sensor.getAllData())

    def getBufferSize(self):
        """Returns buffer size"""
        return len(self.measurements)

    def getJsonData(self):
        """Produces JSON data and returns it"""
        return json.dumps(self.measurements)

    def clearBuffer(self):
        """Clears buffer"""
        self.measurements = []




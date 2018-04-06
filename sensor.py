import psutil
import datetime
import json

class Sensor:
    def __init__(self):
        pass

    def getAllData(self):
        data = {}
        data['CPU_USAGE'] = self.getCpuUsage()
        data['RAM_USAGE'] = self.getRamUsage()
        data['DATE'] = str(datetime.datetime.now())
        return data

    def getCpuUsage(self):
        return psutil.cpu_percent()

    def getRamUsage(self):
        return psutil.virtual_memory()[2]

class SensorBuffer:
    def __init__(self, sensor):
        self.sensor = sensor
        self.measurements = []

    def performMeasurement(self):
        self.measurements.append(self.sensor.getAllData())

    def getBufferSize(self):
        return len(self.measurements)

    def getJsonData(self):
        return json.dumps(self.measurements)

    def clearBuffer(self):
        self.measurements = []




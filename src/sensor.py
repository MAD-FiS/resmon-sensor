"""Contains class connected with gathering and buffering data"""

import psutil
import datetime
import platform
import hashlib
import random


class SensorModule:
    """Class which stores particular parameter"""
    def __init__(self, tag, description, dataGetter):
        self.tag = tag
        self.description = description
        self.dataGetter = dataGetter

class Sensor:
    """This class is responsible for reading various parameters from system"""
    def __init__(self):
        self.sessionId = '0'
        self.modules = []


    def prepareModules(self):
        """Add defined modules. Could be in constructor but tests involves extra function"""
        self.addSensorModule(SensorModule('DATE', 'Date', self.getDate))
        self.addSensorModule(SensorModule('SESSION_ID', 'Session ID', self.getSessionId))
        self.addSensorModule(SensorModule('CPU_USAGE', 'CPU usage in percentage', self.getCpuUsage))
        self.addSensorModule(SensorModule('RAM_USAGE', 'RAM usage in percentage', self.getRamUsage))

    def addSensorModule(self, module):
        """Just adds modules to array"""
        self.modules.append(module)

    def getAllData(self):
        """Return all data and return it in dictionary"""
        data = {}
        for module in self.modules:
            data[module.tag] = module.dataGetter()
        return data

    def getSessionId(self):
        """Getter for session ID"""
        return self.sessionId

    def setSessionId(self, sessionId):
        """Setter for session ID"""
        self.sessionId = sessionId

    def getDate(self):
        """Getter for date"""
        return str(datetime.datetime.now())

    def getCpuUsage(self):
        """Getter for CPU usage in percentage"""
        return psutil.cpu_percent()

    def getRamUsage(self):
        """Gette for RAM usagre in percenrage"""
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

    def getData(self):
        """Returns stored data"""
        return self.measurements

    def clearBuffer(self):
        """Clears buffer"""
        self.measurements = []

class MetaSensorModule:
    """Class which stores particular parameter used in metadata"""
    def __init__(self, tag, description, dataGetter):
        self.tag = tag
        self.description = description
        self.dataGetter = dataGetter

class MetaSensor:
    """Class which is responsible for composing meta data"""
    def __init__(self, sensor, nameId):
        self.sessionId = '0'
        self.generateSessionId()
        self.sensor = sensor
        self.nameId = nameId
        self.sensor.setSessionId(self.sessionId)
        self.metaModules = []
        self.addMetaModule(MetaSensorModule('OS', 'Host operating system', self.getSystemInfo))
        self.addMetaModule(MetaSensorModule('OS_VER', 'Operating system version', self.getSystemVersion))
        self.addMetaModule(MetaSensorModule('AVAILABLE_FIELDS', 'Available data fields', self.getAvailableFields))
        self.addMetaModule(MetaSensorModule('SESSION_START_DATE', 'Session start date', self.getDate))
        self.addMetaModule(MetaSensorModule('SESSION_ID', 'Session ID', self.getSessionId))
        self.addMetaModule(MetaSensorModule('NAME', 'User friendly identifier', self.getNameId))

    def addMetaModule(self, metaModule):
        """Just add metaModule to aray"""
        self.metaModules.append(metaModule)

    def generateSessionId(self):
        """Generate unique hash string"""
        stringToHash = self.getDate() + str(random.random())
        self.sessionId = hashlib.sha1(stringToHash.encode('UTF-8')).hexdigest()

    def getNameId(self):
        """Getter for user friendly identifier"""
        return self.nameId

    def getDate(self):
        """Getter for date"""
        return str(datetime.datetime.now())

    def getSessionId(self):
        """Getter for session ID"""
        return self.sessionId

    def getSystemInfo(self):
        """Getter for system info"""
        return platform.system()

    def getSystemVersion(self):
        """Getter for system version"""
        return platform.release()

    def getAvailableFields(self):
        """Getter for available fields"""
        fields = []
        for module in self.sensor.modules:
            record = {'TAG':module.tag, 'DESCRIPTION':module.description}
            fields.append(record)
        return fields

    def getData(self):
        """Returns whole stored data"""
        returnData = []
        for metaModule in self.metaModules:
            record = {'TAG':metaModule.tag, 'DESCRIPTION':metaModule.description, 'DATA':metaModule.dataGetter()}
            returnData.append(record)
        return returnData


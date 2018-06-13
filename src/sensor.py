"""Contains class connected with gathering and buffering data"""

import psutil
import datetime
import platform
import hashlib
import random


class SensorModule:
    """Class which stores particular parameter"""
    def __init__(self, tag, description, unit, dataGetter, isInMeta):
        self.tag = tag
        self.description = description
        self.unit = unit
        self.dataGetter = dataGetter
        self.isInMeta = isInMeta


class Sensor:
    """This class is responsible for reading various parameters from system"""
    def __init__(self):
        self.sessionId = '0'
        self.modules = []

    def prepareModules(self):
        """
        Add defined modules.
        Could be in constructor but tests involves extra function
        """
        self.addSensorModule(SensorModule('date',
                                          'Date',
                                          '',
                                          self.getDate, False))
        self.addSensorModule(SensorModule('session_id',
                                          'Session ID',
                                          '',
                                          self.getSessionId, False))
        self.addSensorModule(SensorModule('cpu_usage',
                                          'CPU usage in percentage',
                                          '%',
                                          self.getCpuUsage, True))
        self.addSensorModule(SensorModule('cpu_frequency',
                                          'CPU frequency in MHz',
                                          'MHz',
                                          self.getCpuFrequency, True))
        self.addSensorModule(SensorModule('ram_usage',
                                          'RAM usage in percentage',
                                          '%',
                                          self.getRamUsage, True))
        self.addSensorModule(SensorModule('virtual_mem_total',
                                          'Total virtual memory',
                                          'bytes',
                                          self.getVirtualMemTotal, True))
        self.addSensorModule(SensorModule('virtual_mem_available',
                                          'Available virtual memory',
                                          'bytes',
                                          self.getVirtualMemAvailable, True))
        self.addSensorModule(SensorModule('legged_users_count',
                                          'Amount of currently logged users',
                                          'quantity',
                                          self.getLoggedUsersCount, True))
        self.addSensorModule(SensorModule('processes_count',
                                          'Amount of running processes',
                                          'quantity',
                                          self.getProcessesCount, True))


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

    def getCpuFrequency(self):
        """Getter for CPU usage in percentage"""
        return psutil.cpu_freq()

    def getRamUsage(self):
        """Getter for RAM usagre in percenrage"""
        return psutil.virtual_memory().percent

    def getVirtualMemTotal(self):
        """Getter for total virtual memory"""
        return psutil.virtual_memory().total

    def getVirtualMemAvailable(self):
        """Getter for available virtual memory"""
        return psutil.virtual_memory().availalbe

    def getLoggedUsersCount(self):
        """Getter for amount of logged users"""
        return len(psutil.users())

    def getProcessesCount(self):
        """Getter for amount of logged users"""
        return len(psutil.pids())


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
        self.addMetaModule(MetaSensorModule('os',
                                            'Host operating system',
                                            self.getSystemInfo))
        self.addMetaModule(MetaSensorModule('os_ver',
                                            'Operating system version',
                                            self.getSystemVersion))
        self.addMetaModule(MetaSensorModule('metrics',
                                            'Available metrics',
                                            self.getAvailableFields))
        self.addMetaModule(MetaSensorModule('sesstion_start_date',
                                            'Session start date',
                                            self.getDate))
        self.addMetaModule(MetaSensorModule('session_id',
                                            'Session ID',
                                            self.getSessionId))
        self.addMetaModule(MetaSensorModule('hostname',
                                            'User friendly identifier',
                                            self.getNameId))

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
            if module.isInMeta:
                record = {'metric_id': module.tag,
                          'description': module.description,
                          'unit': module.unit}
                fields.append(record)
        return fields

    def getDescriptions(self):
        """Returns description for metadatas"""
        returnData = []
        for metaModule in self.metaModules:
            record = {metaModule.tag: metaModule.description}
            returnData.append(record)
        return returnData

    def getData(self):
        """Returns whole stored data ver2"""
        returnData = []
        for metaModule in self.metaModules:
            record = {metaModule.tag: metaModule.dataGetter()}
            returnData.append(record)
        returnData.append({'meta_descriptions':self.getDescriptions()})
        return returnData

"""Module with SensorClient class"""

import sensor
import sender
import time
import threading
import json

class SensorClient:
    """Main class for Sensor Client. It is responsible for establish connection and send gathered data"""
    def __init__(self, address, port, interval, bufferSize, certPath):
        """Constructor which takes essential parameters for establish secure connection with server and adjust data interval sending"""
        self.address = address
        self.port = port
        self.interval = interval
        self.bufferSize = bufferSize
        self.certPath = certPath
        self.sender = sender.Sender(address, port, certPath)
        self.isMainThreadWorking = False
        self.maxSendAttemps = 1

    def startClient(self):
        """Start Sensor Client by establishing connection"""
        self.isMainThreadWorking = True
        self.sendAttemps = 0
        self.sensor = sensor.Sensor()
        self.sensor.prepareModules()
        self.sensorBuffer = sensor.SensorBuffer(self.sensor)
        self.metaSensor = sensor.MetaSensor(self.sensor)

        self.sendMetaData()
        """After send meta data increase max attemps in case of accidental network failure"""
        self.maxSendAttemps = 10

        while(self.isMainThreadWorking):
            self.gatherAndSendData()
            time.sleep(self.interval)

    def sendMetaData(self):
        """Sends meta data to server"""
        data = self.metaSensor.getData()
        jsonData = self.getJsonString(data, isMeta=True)
        self.sendingThreadFunction(jsonData)

    def gatherAndSendData(self):
        """Gather buffered data and send it"""
        self.sensorBuffer.performMeasurement()
        if self.sensorBuffer.getBufferSize() >= self.bufferSize:
            data = self.sensorBuffer.getData()
            jsonData = self.getJsonString(data)
            self.sensorBuffer.clearBuffer()

            self.sendingThread = threading.Thread(target=self.sendingThreadFunction, args=(jsonData, ))
            self.sendingThread.start()

    def getJsonString(self, data, isMeta=False):
        """Wrape data in order to distinguish data and meta and generate JSON string"""
        wrappedData = {}
        if isMeta:
            wrappedData['TYPE'] = 'META'
        else:
            wrappedData['TYPE'] = 'DATA'
        wrappedData['DATA'] = data
        return json.dumps(wrappedData)

    def sendingThreadFunction(self, data):
        """Thread function used for sending data"""

        try:
            self.sender.sendData(data)
            self.sendAttemps = 0
        except Exception as ex:
            self.sendAttemps += 1
            print("Failed connecion attempts %d out of %d" % (self.sendAttemps, self.maxSendAttemps))
            print(ex)
            if self.sendAttemps >= self.maxSendAttemps:
                print("Max connection attemps reached. Client will be closed")
                self.isMainThreadWorking = False
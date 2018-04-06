"""Module with SensorClient class"""

import sensor
import sender
import time
import threading

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
        self.maxSendAttemps = 10

    def startClient(self):
        """Start Sensor Client by establishing connection"""
        self.isMainThreadWorking = True
        self.sendAttemps = 0
        self.sensorBuffer = sensor.SensorBuffer(sensor.Sensor())

        while(self.isMainThreadWorking):
            self.gatherAndSendData()
            time.sleep(self.interval)

    def gatherAndSendData(self):
        """Gather buffered data and send it"""
        self.sensorBuffer.performMeasurement()
        if self.sensorBuffer.getBufferSize() >= self.bufferSize:
            data = self.sensorBuffer.getJsonData()
            self.sensorBuffer.clearBuffer()

            self.sendingThread = threading.Thread(target=self.sendingThreadFunction, args=(data, ))
            self.sendingThread.start()

    def sendingThreadFunction(self, data):
        """Thread function used for sending data"""
        try:
            self.sender.sendData(data)
            self.sendAttemps = 0
        except:
            self.sendAttemps += 1
            print("Failed connecion attempts %d out of %d" % (self.sendAttemps, self.maxSendAttemps))
            if self.sendAttemps >= self.maxSendAttemps:
                print("Max connection attemps reached. Client will be closed")
                self.isMainThreadWorking = False
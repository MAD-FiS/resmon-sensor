import sensor
import sender
import argparse
import time
import threading

class SensorClient:
    def __init__(self, address, port, interval, bufferSize, certPath):
        self.address = address
        self.port = port
        self.interval = interval
        self.bufferSize = bufferSize
        self.certPath = certPath
        self.sender = sender.Sender(address, port, certPath)
        self.isMainThreadWorking = False
        self.maxSendAttemps = 10

    def startClient(self):
        self.isMainThreadWorking = True
        self.sendAttemps = 0
        self.sensorBuffer = sensor.SensorBuffer(sensor.Sensor())

        while(self.isMainThreadWorking):
            self.gatherAndSendData()
            time.sleep(self.interval)

    def gatherAndSendData(self):
        self.sensorBuffer.performMeasurement()
        if self.sensorBuffer.getBufferSize() >= self.bufferSize:
            data = self.sensorBuffer.getJsonData()
            self.sensorBuffer.clearBuffer()

            self.sendingThread = threading.Thread(target=self.sendingThreadFunction, args=(data, ))
            self.sendingThread.start()

    def sendingThreadFunction(self, data):
        try:
            self.sender.sendData(data)
            self.sendAttemps = 0
        except:
            self.sendAttemps += 1
            print("Failed connecion attempts %d out of %d" % (self.sendAttemps, self.maxSendAttemps))
            if self.sendAttemps >= self.maxSendAttemps:
                print("Max connection attemps reached. Client will be closed")
                self.isMainThreadWorking = False









"""
sensorObj = sensor.Sensor()


clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.settimeout(1000)

clientSSLSocket = ssl.wrap_socket(clientSocket, cert_reqs=ssl.CERT_REQUIRED, ca_certs='./cert.pem')

clientSSLSocket.connect(('localhost', 8082))
clientSSLSocket.send(sensorObj.getJsonData().encode('utf-8'))
clientSSLSocket.close()
"""

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Sensor client')
    parser.add_argument('-a', '--address', required=True, help='Server address')
    parser.add_argument('-p', '--port', required=True, type=int, help='Server port')
    parser.add_argument('-i', '--interval', required=True, type=int, help='Measurement interval [sec]')
    parser.add_argument('-b', '--buffer', type=int, help='Messages buffer size')
    parser.add_argument('-c', '--cert', required=True, help='Cert path')
    args = parser.parse_args()

    sensorClient = SensorClient(args.address, args.port, args.interval, args.buffer, args.cert)
    sensorClient.startClient()
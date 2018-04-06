import socket
import ssl

class Sender:
    def __init__(self, address, port, certPath):
        self.address = address
        self.port = port
        self.certPath = certPath

    def sendData(self, data):
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientSocket.settimeout(1000)

        clientSSLSocket = ssl.wrap_socket(clientSocket, cert_reqs=ssl.CERT_REQUIRED, ca_certs='./cert.pem')
        clientSSLSocket.connect((self.address, self.port))
        clientSSLSocket.send(data.encode('utf-8'))
        clientSSLSocket.close()


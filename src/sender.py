"""Module responsible for sending data to server"""
import socket
import ssl

class Sender:
    """Class which maintain connection with server"""
    def __init__(self, address, port, certPath):
        """Constructor takes server address, port and certificate file for SSL"""
        self.address = address
        self.port = port
        self.certPath = certPath

    def sendData(self, data):
        """Function which establish connection and send data to server"""
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientSocket.settimeout(1000)

        clientSSLSocket = ssl.wrap_socket(clientSocket, cert_reqs=ssl.CERT_REQUIRED, ca_certs='./cert.pem')
        clientSSLSocket.connect((self.address, self.port))
        clientSSLSocket.send(data.encode('utf-8'))
        clientSSLSocket.close()


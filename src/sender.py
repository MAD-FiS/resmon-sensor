"""Module responsible for sending data to server"""
import requests


class Sender:
    """Class which maintain connection with server"""
    def __init__(self, address):
        """Constructor takes server address"""
        self.address = address

    def sendData(self, data):
        """Function which establish connection and send data to server"""
        requestResponse = requests.post(self.address, data=data)
        print(str(requestResponse.status_code) + " " + requestResponse.reason)
        return requestResponse.status_code

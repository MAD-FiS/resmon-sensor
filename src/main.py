""" Main source file used for running Sensor Client"""

import argparse
import sensorClient

if __name__ == '__main__':
    """Main function which provides argument parser and run Sensor Client"""
    parser = argparse.ArgumentParser(description='Sensor client', epilog='Example usage: python3 main.py -a localhost -p 8083 -i 1 -b 10 -c ./cert.pem')
    parser.add_argument('-a', '--address', required=True, help='Server address')
    parser.add_argument('-p', '--port', required=True, type=int, help='Server port')
    parser.add_argument('-i', '--interval', required=True, type=int, help='Measurement interval [sec]')
    parser.add_argument('-b', '--buffer', type=int, help='Messages buffer size')
    parser.add_argument('-c', '--cert', required=True, help='Cert path')
    args = parser.parse_args()

    sensorClient = sensorClient.SensorClient(args.address, args.port, args.interval, args.buffer, args.cert)
    sensorClient.startClient()
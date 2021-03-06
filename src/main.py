""" Main source file used for running Sensor Client"""

import argparse
import src.sensorClient

if __name__ == '__main__':
    """Main function which provides argument parser and run Sensor Client"""
    parser = argparse.ArgumentParser(
        description='Sensor client',
        epilog='Example usage: python3 main.py -a '
               'http://localhost:4001 -i 1 -b 10 -n workstation1')
    parser.add_argument('-a', '--address', required=True,
                        help='Full server address with protocol and port')
    parser.add_argument('-i', '--interval', required=True, type=int,
                        help='Measurement interval [sec]')
    parser.add_argument('-b', '--buffer', type=int,
                        help='Messages buffer size', default=10)
    parser.add_argument('-n', '--name', required=True,
                        help='User friendly identifier')
    args = parser.parse_args()

    sensorClient = src.sensorClient.SensorClient(args.address, args.interval,
                                                 args.buffer, args.name)
    try:
        sensorClient.startClient()
    except KeyboardInterrupt:
        print()
        print('You stopped the sensor manually')
        exit(0)

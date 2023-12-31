#!/usr/bin/env python

import serial
import sys
import time

# just copy all lines from serial port to stdout.
# use 'flush' so that if we pipe stdout to 'tee', it will
# be immediately visible.

# note the timeout; if the attached device is silent
# for 20 or more seconds, this process will terminate.
# our data generator on the microprocessor issues a
# data value every 10 seconds.

if __name__ == '__main__':

    s = serial.Serial(baudrate=115200, port='/dev/ttyACM0', timeout=20)

    while True:
        ll = s.readline().rstrip()
        sys.stdout.write(ll + '\n')
        sys.stdout.flush()
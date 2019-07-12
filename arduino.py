
from .core import Device

import serial
import time

class Arduino(Device):
    '''Generic Arduino device connected for Serial interface'''

    def __init__(self, address=r'/dev/ttyUSB0', baud=9600):
        self.bus = serial.Serial(address)
        return

    def write(self, message):
        self.bus.write(message)
        return

    def read(self):
        line = self.bus.readline()
        return line

    def jump(self, timeout=100):
        timeout = timeout / 1000
        result = self.read()
        ti = time.time()
        while True:
            result = self.read()
            if time.time() - ti > timeout: return
        

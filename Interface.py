#!/usr/bin/python
import serial
from smbus2 import SMBus, i2c_msg

class Interface:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.port = ""
        self.addr = 0
        self.ser = serial.Serial()
        self.bus = SMBus()

    def getport(self):
        return self.port

    def setport(self, port):
        self.port = port

    def getaddr(self):
        return self.addr

    def setaddr(self, addr):
        self.addr = addr

    def init_serial(self, baudrate, bytsize, stopbits):
        self.ser = serial.Serial(
            port=self.port, baudrate=baudrate, bytesize=bytsize, stopbits=stopbits
        )
        self.ser.flush()

    def init_i2c(self):
        self.bus = SMBus(1)

    def list_i2c(self):
        for device in range(128):
            try:
                self.bus.read_byte(device)
                print(hex(device))
            except:
                print("No device connected to bus")
                pass

    def write_i2c(self):
        data = [65, 66]
        # Write a single byte to address 80
        msg = i2c_msg.write(80, data)
        self.bus.i2c_rdwr(msg)

    def read_i2c(self):
        # Read 64 bytes from address 80
        msg = i2c_msg.read(80, 64)
        self.bus.i2c_rdwr(msg)
        return msg

    def check_connection_serial(self):
        if self.type == 0:
            print("Serial is open: " + str(self.ser.isOpen()))
            return True
        elif self.type == 1:
            #print("Bus is open: " + str(self.ser.isOpen()))
            return True
        else:
            return False

    def open(self):
        if self.type == 0:
            self.ser.open()
            print("Serial is open: " + str(self.ser.isOpen()))
            return True

    def close(self):
        if self.type == 0:
            self.ser.close()
            print("Is still open " + str(self.ser.isOpen()))
            return True

    def write(self, msg):
        if self.type == 0:
            self.ser.write(str(msg).encode("utf-8")) #"!AIBBM,1,1,0,2,8,04a9M>1@PU>0U>06185=08E99V1@E=4,0*7C"

    def read(self):
        if self.type == 0:
            msg = self.ser.readline()
            return msg


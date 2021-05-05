#!/usr/bin/python
import serial
from smbus2 import SMBus, i2c_msg
import socket

class Interface:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.port = ""
        self.addr = 0
        self.ser = serial.Serial()
        self.bus = SMBus()
        self.s = socket.socket()
        self.ip = ""
        self.socket_port = 0

    def getport(self):
        return self.port

    def setport(self, port):
        self.port = port

    def getaddr(self):
        return self.addr

    def setaddr(self, addr):
        self.addr = addr

    def init_serial(self, baudrate):
        self.ser = serial.Serial(
            port=self.port, baudrate=baudrate, bytesize=8, stopbits=serial.STOPBITS_ONE
        )
        self.ser.flush()

    def init_i2c(self):
        self.bus = SMBus(1)

    def init_socket(self, IP, PORT):
        self.ip = IP
        self.socket_port = PORT
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def connect_socket(self):
        self.s.connect((self.ip, self.socket_port))

    def close_socket(self):
        self.s.close()

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
        msg = i2c_msg.write(self.addr, data)
        self.bus.i2c_rdwr(msg)

    def read_i2c(self):
        # Read 64 bytes from address 80
        msg = i2c_msg.read(self.addr, 64)
        self.bus.i2c_rdwr(msg)
        return msg

    def check_connection_rs232(self):
        if self.type == 0:
            print("Serial is open: " + str(self.ser.isOpen()))
            return True
        elif self.type == 1:
            #print("Bus is open: " + str(self.ser.isOpen()))
            return True
        else:
            return False

    def open_rs232(self):
        if self.type == 0:
            self.ser.open()
            print("Serial is open: " + str(self.ser.isOpen()))
            return True

    def close_rs232(self):
        if self.type == 0:
            self.ser.close()
            print("Is still open " + str(self.ser.isOpen()))
            return True

    def write_rs232(self, msg):
        if self.type == 0:
            self.ser.write(str(msg).encode("utf-8")) #"!AIBBM,1,1,0,2,8,04a9M>1@PU>0U>06185=08E99V1@E=4,0*7C"
            print("send: %s", msg)

    def read_rs232(self):
        if self.type == 0:
            msg = self.ser.readline()
            return msg

    def write_socket(self, msg):
        self.s.sendto(msg.encode('utf-8'), (self.ip, self.socket_port))
        print("Client Sent : ", msg)

    def read_socket(self):
        data, addr = self.s.recvfrom(4096)
        return data, addr

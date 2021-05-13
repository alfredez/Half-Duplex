#!/usr/bin/python
import serial
import spidev
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
        self.spi = spi = spidev.SpiDev()

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

    def init_spi(self, spi_bus, spi_device):
        self.spi.open(spi_bus, spi_device)
        self.spi.max_speed_hz = 1000000

    def close_spi(self):
        self.spi.close()

    def connect_socket(self):
        self.s.connect((self.ip, self.socket_port))

    def close_socket(self):
        self.s.close()

    def list_i2c(self):
        for device in range(128):
            try:
                msg = i2c_msg.write(device, [64])
                self.bus.i2c_rdwr(msg)
                self.bus.read_byte(device)
                print(device)
            except:
                print("No device connected to bus")
                pass

    def write_i2c(self, data, type):
        # Write a single byte to address 80
        buff = []
        buff.append(data)
        buff.append(type)
        msg = i2c_msg.write(self.addr, buff)
        self.bus.i2c_rdwr(msg)
        print("data send")

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

    def write_spi(self, data, type):
        # Write a single byte to address 80
        buff = []
        buff.append(data)
        buff.append(type)
        self.spi.writebytes([buff])
        print("data send")

    def read_spi(self):
        # Read 64 bytes from address 80
        msg = self.spi.readbytes(64)
        return msg

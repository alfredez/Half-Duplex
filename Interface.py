#!/usr/bin/python
import serial
import spidev
import socket
from smbus2 import SMBus, i2c_msg


class Interface:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.port = ""
        self.baudrate = 0
        self.addr = 0
        self.ser = serial.Serial()
        self.bus = SMBus()
        self.sock = socket.socket()
        self.ip = ""
        self.socket_port = 0
        self.spi = spidev.SpiDev()
        self.spi_bus = 0
        self.spi_device = 0

    def get_port(self):
        return self.port

    def set_port(self, new_port):
        self.port = new_port

    def get_baudrate(self):
        return self.baudrate

    def set_baudrate(self, new_baudrate):
        self.baudrate = new_baudrate

    def get_addr(self):
        return self.addr

    def set_addr(self, new_addr):
        self.addr = new_addr

    def init_serial(self, port, baudrate):
        self.port = port
        self.baudrate = baudrate
        self.ser = serial.Serial(
            port=self.port, baudrate=self.baudrate, bytesize=8, stopbits=serial.STOPBITS_ONE
        )
        self.ser.flush()

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

    def init_i2c(self, address):
        self.addr = address
        self.bus = SMBus(1)

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

    def init_socket(self, IP, PORT):
        self.ip = IP
        self.socket_port = PORT
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def connect_socket(self):
        self.sock.connect((self.ip, self.socket_port))

    def close_socket(self):
        self.sock.close()

    def write_socket(self, msg):
        self.sock.sendto(msg.encode('utf-8'), (self.ip, self.socket_port))
        print("Client Sent : ", msg)

    def read_socket(self):
        data, addr = self.sock.recvfrom(4096)
        return data, addr

    def init_spi(self, spi_bus, spi_device):
        self.spi_bus = spi_bus
        self.spi_device = spi_device
        self.spi.max_speed_hz = 1000000

    def open_spi(self):
        self.spi.open(self.spi_bus, self.spi_device)

    def close_spi(self):
        self.spi.close()

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

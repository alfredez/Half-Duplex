#!/usr/bin/python
import serial
from serial import Serial


class RS232:
    def __init__(self):
        self.port = ""
        self.baudrate = 0
        self.ser = Serial()
        self.type = 0

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
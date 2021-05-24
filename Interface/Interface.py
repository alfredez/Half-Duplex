#!/usr/bin/python
from I2C import I2C
from Ethernet import Ethernet
from RS232 import RS232
from SPI import SPI


class Interface:
    def __init__(self):
        self.rs232 = RS232()
        self.i2c = I2C()
        self.ethernet = Ethernet()
        self.spi = SPI()

    def get_rs232_settings(self):
        return vars(self.rs232)

    def get_i2c_settings(self):
        return vars(self.i2c)

    def get_ethernet_settings(self):
        return vars(self.ethernet)

    def get_spi_settings(self):
        return vars(self.spi)

#!/usr/bin/python
from Interface import Interface


class Device(Interface):
    def __init__(self, name, branch, model, type):
        super().__init__(name, type)
        self.name = name
        self.branch = branch
        self.model = model
        self.binarydata = 0
        self.status = 0
        self.type = type
        #self.intf = interf.Interface(name, type)


    def getname(self):
        print("Wireless device name " + self.name)

    # def getport(self):
    #     return self.port
    #
    # def setport(self, port):
    #     self.port = port
    #
    # def getaddr(self):
    #     return self.addr
    #
    # def setaddr(self, addr):
    #     self.addr = addr

    # def connect(self):
    #     print("Wireless device port " + self.port)
    #
    # def check_connection(self):
    #     print("Wireless device port " + self.port)
    #
    # def status(self):
    #     print("Wireless device port " + self.port)
    #
    # def transmission(self):
    #     print("Wireless device port " + self.port)
    #
    # def terminate_connection(self):
    #     print("Wireless device port " + self.port)
    #
    # def insert_payload(self):
    #     print("Wireless device port " + self.port)
    #
    # def encode_binarydata(self):
    #     print("Wireless device port " + self.port)

    # def encode_BBM(self, data):
    #     if data == 0:
    #         ebbm = "!AIBBM,1,1,0,2,8,04a9M>1@PU>0U>06185=08E99V1@E=4,0*7C"
    #         return ebbm
    #     else:
    #         return ""
    #
    # def encode_ABM(self):
    #     print("Wireless device port " + self.port)

'''
AIS device with interface
'''
# name, branch, model, port, type
p1 = Device("AIS Transponder1", "True Heading", "AIS Base Station", 0)
# p1.setport("/dev/ttyUSB0")
# p1.init_serial(38400, 8, serial.STOPBITS_ONE)
# p1.check_connection_serial()
p1.init_i2c()
p1.list_i2c()
p1.close()
# p1.intf.setport("/dev/ttyUSB0")
# p1.intf.init_serial(38400, 8, serial.STOPBITS_ONE)
# p1.intf.checkconnection()
# msg = p1.encode_BBM(0)
#p1.intf.write(msg)


# aisin = interf.Interface(p1.name, p1.type)
# aisin.setport("/dev/ttyUSB0")
# aisin.init_serial(38400, 8, serial.STOPBITS_ONE)
# print(aisin.checkconnection())
# print(aisin.read())

p1.getname()


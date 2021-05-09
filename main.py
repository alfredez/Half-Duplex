import os
import sys
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

from Device import Device
from Folder import Folder
from File import File
import time


class MonitorFolder(PatternMatchingEventHandler):
    FILE_SIZE = 1000

    def __init__(self, folder):
        # Set the patterns for PatternMatchingEventHandler
        PatternMatchingEventHandler.__init__(self, patterns=['*.txt'], ignore_directories=True, case_sensitive=False)
        self.folder = folder

    def on_created(self, event):
        print(event.src_path, event.event_type)
        time.sleep(1)
        #self.checkFolderSize(event.src_path)
        newfile = File(str(event.src_path).replace(self.folder.path, ""))

        self.folder.files.append(newfile)
        newfile.setlines(self.folder.path)
        dabid = newfile.get_dab_id()
        msgtype = newfile.get_msg_type()
        print(dabid)
        self.acknowledge(dabid, msgtype)
        # msg = ais.encode_BBM(dabid)
        # ais.write_rs232(msg)

    def checkFolderSize(self, src_path):
        if os.path.isdir(src_path):
            if os.path.getsize(src_path) > self.FILE_SIZE:
                print("Time to backup the dir")
        else:
            if os.path.getsize(src_path) > self.FILE_SIZE:
                print("very big file")

    def acknowledge(self, id, type):
        list_devices = devices
        for d in list_devices:
            if d.type == 0:
                try:
                    d.write_rs232("!AIBBM,1,1,0,2,8,04a9M>1@PU>0U>06185=08E99V1@E=4,0*7C")
                except:
                    print("Could not send with: %s", d.name)
                    pass
            elif d.type == 1:
                try:
                    d.write_i2c(id, type)
                except:
                    print("Could not send with: %s", d.name)
                    pass
            elif d.type == 2:
                try:
                    d.write_socket("!AIBBM,1,1,0,2,8,04a9M>1@PU>0U>06185=08E99V1@E=4,0*7C")
                except:
                    print("Could not send with: %s", d.name)
                    pass



if __name__ == "__main__":

    # ais = Device("AIS Transponder1", "True Heading", "AIS Base Station", 0)
    # ais.setport("/dev/ttyUSB0")
    # ais.init_serial(38400)
    # ais.check_connection_rs232()

    devices = []
    lora = Device("LoRaWAN Transponder1", "PyCom", "FiPy", 1)
    lora.init_i2c()
    lora.addr = 4
    #lora.list_i2c()

    #devices.append(ais)
    devices.append(lora)
#    while True:
#        lora.write_i2c()
#        time.sleep(5)

    f1 = Folder('./correct/')

    event_handler = MonitorFolder(f1)
    observer = Observer()
    observer.schedule(event_handler, path=event_handler.folder.path, recursive=True)

    observer.start()
    print("Monitoring started")
    try:
        while (True):
            time.sleep(1)

    except KeyboardInterrupt:
        observer.stop()
        print("Monitoring Stopped")
    observer.join()

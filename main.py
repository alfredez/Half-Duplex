import os
import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from Device import Device
from Folder import Folder
from File import File


class MonitorFolder(FileSystemEventHandler):
    FILE_SIZE = 1000

    def __init__(self, folder):
        self.folder = folder

    def on_created(self, event):
        print(event.src_path, event.event_type)
        #self.checkFolderSize(event.src_path)
        newfile = File(str(event.src_path).replace(self.folder.path, ""))

        self.folder.files.append(newfile)
        newfile.setlines(self.folder.path)
        dabid = newfile.check_dab_id()
        print(dabid)
        # msg = ais.encode_BBM(dabid)
        # ais.write_rs232(msg)

    def checkFolderSize(self, src_path):
        if os.path.isdir(src_path):
            if os.path.getsize(src_path) > self.FILE_SIZE:
                print("Time to backup the dir")
        else:
            if os.path.getsize(src_path) > self.FILE_SIZE:
                print("very big file")


if __name__ == "__main__":

    # ais = Device("AIS Transponder1", "True Heading", "AIS Base Station", 0)
    # ais.setport("/dev/ttyUSB0")
    # ais.init_serial(38400)
    # ais.check_connection_rs232()

    lora = Device("LoRaWAN Transponder1", "PyCom", "FiPy", 0)
    lora.init_i2c()
    lora.addr = 0x04
    lora.list_i2c()

    while True:
        lora.write_i2c()
        time.sleep(5)


    # f1 = Folder('./correct/')
    #
    # event_handler = MonitorFolder(f1)
    # observer = Observer()
    # observer.schedule(event_handler, path=event_handler.folder.path, recursive=True)
    # print("Monitoring started")
    # observer.start()
    # try:
    #     while (True):
    #         time.sleep(1)
    #
    # except KeyboardInterrupt:
    #     observer.stop()
    #     observer.join()

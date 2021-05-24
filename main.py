import os
import sys
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from aisutils import nmea
from aisutils import BitVector
from aisutils import binary


from Device import Device
from Folder import Folder
from File import File
import time


class Monitor(PatternMatchingEventHandler):
    FILE_SIZE = 1000

    def __init__(self, folder):
        # Set the patterns for PatternMatchingEventHandler
        PatternMatchingEventHandler.__init__(self, patterns=['*.txt'], ignore_directories=True, case_sensitive=False)
        self.folder = folder

    def on_created(self, event):
        print(event.src_path, event.event_type)
        time.sleep(1)
        new_file = File(str(event.src_path).replace(self.folder.path, ""))

        self.folder.files.append(new_file)
        new_file.set_lines(self.folder.path)
        dab_id = new_file.get_dab_id()
        message_type = new_file.get_message_type()
        print(dab_id)
        self.acknowledge(dab_id, message_type)

    # def checkFolderSize(self, src_path):
    #     if os.path.isdir(src_path):
    #         if os.path.getsize(src_path) > self.FILE_SIZE:
    #             print("Time to backup the dir")
    #     else:
    #         if os.path.getsize(src_path) > self.FILE_SIZE:
    #             print("very big file")

    def acknowledge(self, dab_id, message_type):
        for d in devices:
            if d.interface == 0:
                try:
                    if message_type == 4:
                        msg = '  ACK:' + str(dab_id) + ',MSG:' + str(message_type) + ',RSSI:122,SNR:-1'
                        aisBits = BitVector.BitVector(textstring=msg)
                        payloadStr, pad = binary.bitvectoais6(aisBits)  # [0]
                        buffer = nmea.bbmEncode(1, 1, 0, 1, 8, payloadStr, pad, appendEOL=False)
                        d.rs232.write_rs232(buffer)
                    else:
                        msg = '  ACK:' + str(dab_id) + ',MSG:' + str(message_type) + ''
                        aisBits = BitVector.BitVector(textstring=msg)
                        payloadStr, pad = binary.bitvectoais6(aisBits)  # [0]
                        buffer = nmea.bbmEncode(1, 1, 0, 1, 8, payloadStr, pad, appendEOL=False)
                        d.rs232.write_rs232(buffer)

                except ("There is no connection with: %s" % d.name):
                    print("Could not send with: %s" % d.name)
                    pass
            elif d.interface == 1:
                try:
                    d.i2c.write_i2c(dab_id, message_type)
                except ("There is no connection with: %s" % d.name):
                    print("Could not send with: %s" % d.name)
                    pass
            elif d.interface == 2:
                try:
                    d.ethernet.write_socket("!AIBBM,1,1,0,2,8,04a9M>1@PU>0U>06185=08E99V1@E=4,0*7C")
                except ("There is no connection with: %s" % d.name):
                    print("Could not send with: %s" % d.name)
                    pass
            elif d.interface == 3:
                try:
                    d.spi.write_spi(dab_id, message_type)
                except ("There is no connection with: %s" % d.name):
                    print("Could not send with: %s" % d.name)
                    pass


if __name__ == "__main__":

    devices = []
    # ais = Device("AIS Transponder1", "True Heading", "AIS Base Station", 0)
    # ais.set_port("/dev/ttyUSB0")
    # ais.init_serial("/dev/ttyUSB0", 38400)
    # ais.check_connection_rs232()

    lora = Device("LoRaWAN Transponder1", "Sodaq", "One", 1)
    lora.i2c.init_i2c(4)

    #devices.append(ais)
    devices.append(lora)

    #dab_folder = Folder(os.path.expanduser("~/.dab/received-messages"))
    dab_folder = Folder(os.path.expanduser("~/correct"))

    event_handler = Monitor(dab_folder)
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

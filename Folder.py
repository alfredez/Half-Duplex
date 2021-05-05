#!/usr/bin/python
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import File

class Folder():
    def __init__(self, path):
        super().__init__()
        self.path = path
        self.files = []

    def get_listdir(self):
        return self.files

    def set_listdir(self):
        files = []
        for x in os.listdir(self.path):
            if x.endswith(".txt"):
                # Prints only text file present in My Folder
                files.append(x)
        self.files = files


f1 = Folder('./correct/')
# rl = f1.readlines()
# dabid = f1.check_dab_id(rl)
f1.set_listdir()
f1.get_listdir()


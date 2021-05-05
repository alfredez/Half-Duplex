#!/usr/bin/python
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os


class File:
    def __init__(self, filename):
        self.filename = filename
        self.lines = []

    def setlines(self, path):
        mylines = []  # Declare an empty list named mylines.
        with open(str(path+self.filename), 'rt') as myfile:  # Open lorem.txt for reading text data.
            for myline in myfile:  # For each line, stored as myline,
                mylines.append(myline)  # add its contents to mylines.
        self.lines = mylines

    def check_dab_id(self):
        return int(self.lines[0])

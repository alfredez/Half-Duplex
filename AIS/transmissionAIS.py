#!/usr/bin/env python3

import socket

HOST = '192.168.1.100'  # The server's hostname or IP address
PORT = 255        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    #s.send(b'!AIVDM,1,1,,A,10`lQ3hP000EfQ@N7REv4?wF25B4,0*23')
    s.send("!AIBBM,1,1,0,2,8,04a9M>1@PU>0U>06185=08E99V1@E=4,0*7C".encode("utf-8"))
    #s.write("!AIBBM,1,1,0,2,8,04a9M>1@PU>0U>06185=08E99V1@E=4,0*7C".encode("utf-8"))
    data = s.recv(1024)

print('Received', repr(data))

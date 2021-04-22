#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 2947        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'!AIVDM,1,1,,A,10`lQ3hP000EfQ@N7REv4?wF25B4,0*23')
    data = s.recv(1024)

print('Received', repr(data))

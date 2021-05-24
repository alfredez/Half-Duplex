import socket


class Ethernet:
    def __init__(self):
        self.ip = ""
        self.socket_port = 0
        self.sock = socket.socket()

    def init_socket(self, IP, PORT):
        self.ip = IP
        self.socket_port = PORT
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def connect_socket(self):
        self.sock.connect((self.ip, self.socket_port))

    def close_socket(self):
        self.sock.close()

    def write_socket(self, msg):
        self.sock.sendto(msg.encode('utf-8'), (self.ip, self.socket_port))
        print("Client Sent : ", msg)

    def read_socket(self):
        data, addr = self.sock.recvfrom(4096)
        return data, addr

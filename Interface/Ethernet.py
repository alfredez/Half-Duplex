import socket


class Ethernet:
    def __init__(self):
        self.ip_address = ""
        self.socket_port = 0
        self.sock = socket.socket()

    def get_ip_address(self):
        return self.ip_address

    def set_ip_address(self, new_ip_address):
        self.ip_address = new_ip_address

    def get_port(self):
        return self.socket_port

    def set_port(self, new_socket_port):
        self.socket_port = new_socket_port

    def init_socket(self, IP, PORT):
        self.ip_address = IP
        self.socket_port = PORT
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def connect_socket(self):
        self.sock.connect((self.ip_address, self.socket_port))

    def close_socket(self):
        self.sock.close()

    def write_socket(self, msg):
        self.sock.sendto(msg.encode('utf-8'), (self.ip_address, self.socket_port))
        print("Client Sent : ", msg)

    def read_socket(self):
        data, addr = self.sock.recvfrom(4096)
        return data, addr

from utils.utils import check_type
from socket import socket
from .communicate_process import CommunicateProcess


class Receive:
    def __init__(self, ip, port):
        check_type(ip, str)
        check_type(port, int)

        self.address = (ip, port)
        self.server_socket = socket()
        self.server_socket.bind(self.address)

    def start_listen(self):
        print(f"Start receive information from: {self.address}")
        self.server_socket.listen(1)

        while True:
            aux = self.server_socket.accept()
            lister = CommunicateProcess(aux[0], aux[1])
            lister.start()



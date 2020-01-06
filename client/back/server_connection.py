from socket import socket
from multiprocessing import Process, Queue
from utils.utils import check_type
from json import dumps, loads
from time import sleep
from .process_all import ProcessAll


class ServerConnection:
    def __init__(self, ip, port):
        self.address = (ip, port)
        self.socket = socket()

        while True:
            try:
                self.socket.connect(self.address)
                break
            except ConnectionRefusedError:
                continue

        self.queue_send = Queue()
        self.process_send = Process(target=self._process_send, args=(self.queue_send, self.socket))

        self.queue_receive = Queue()
        self.process_receive = Process(target=self._process_receive, args=(self.queue_receive, self.socket))

        self.process = ProcessAll(self.queue_send, self.queue_receive)

    @staticmethod
    def _process_send(queue, socket):
        while True:
            if queue.empty():
                sleep(0.1)
                continue

            aux = queue.get()
            jdata = dumps(aux)
            socket.sendall(jdata.encode())

    @staticmethod
    def _process_receive(queue, socket):
        while True:
            try:
                response = socket.recv(1024)
            except ConnectionResetError:
                break

            jdata = loads(response.decode('utf-8'))
            queue.put(jdata)

    def send(self, jdata):
        check_type(jdata, dict)
        self.queue_send.put(jdata)

    def start(self):
        self.process_send.start()
        self.process_receive.start()
        self.process.start()
        self.process_send.join()
        self.process_receive.join()

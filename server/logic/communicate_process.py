from multiprocessing import Process, Queue
from json import dumps, loads
from time import sleep
from utils.utils import check_type
from .process_all import ProcessAll


class CommunicateProcess:
    def __init__(self, socket,  address):
        check_type(address, tuple)

        self.socket = socket
        self.address = address

        self.queue_send = Queue()
        self.process_send = Process(target=self._process_send, args=(self.queue_send, self.socket))

        self.queue_receive = Queue()
        self.process_receive = Process(target=self._process_receive, args=(self.queue_receive, self.socket))

        self.process = ProcessAll(self.queue_send, self.queue_receive)

    @staticmethod
    def _process_receive(queue, socket):
        while True:
            try:
                response = socket.recv(1024)
            except ConnectionResetError:
                break

            jdata = loads(response.decode('utf-8'))
            print(jdata)
            queue.put(jdata)

    @staticmethod
    def _process_send(queue, socket):
        while True:
            if queue.empty():
                sleep(0.001)
                continue

            aux = queue.get()
            print(aux)

            to_send = dumps(aux)
            to_send = to_send.encode()
            socket.send(to_send)

    def start(self):
        self.process_send.start()
        self.process_receive.start()
        self.process.start()
        self.process_send.join()
        self.process_receive.join()

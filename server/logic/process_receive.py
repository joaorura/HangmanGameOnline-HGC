from multiprocessing import Process
from json import loads
from json.decoder import JSONDecodeError


class ProcessReceive(Process):
    def __init__(self, queue, socket):
        self.queue = queue
        self.socket = socket

        super().__init__(target=self._process_receive)

    def _process_receive(self):
        while True:
            try:
                response = self.socket.recv(1024)
            except ConnectionResetError:
                break

            if response is None:
                continue

            aux = response.decode('utf-8')

            try:
                jdata = loads(aux)
            except JSONDecodeError:
                continue

            self.queue.put(jdata)

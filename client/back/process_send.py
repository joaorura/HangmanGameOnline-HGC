from multiprocessing import Process
from json import dumps


class ProcessSend(Process):
    def __init__(self, queue, socket):
        self.queue = queue
        self.socket = socket

        super().__init__(target=self._process_send)

    def _process_send(self):
        while True:
            if self.queue.empty():
                continue

            aux = self.queue.get()
            jdata = dumps(aux)
            self.socket.sendall(jdata.encode())

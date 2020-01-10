from multiprocessing import Process
from json import dumps


class ProcessSend(Process):
    def __init__(self, queue, socket):
        self.queue = queue
        self.socket = socket

        super().__init__(target=self._process_send)

    def _process_send(self, ):
        while True:
            if self.queue.empty():
                continue

            aux = self.queue.get()
            to_send = dumps(aux)
            to_send = to_send.encode()
            self.socket.send(to_send)

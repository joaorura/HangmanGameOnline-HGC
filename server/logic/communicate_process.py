from multiprocessing import Process, Queue
from json import dumps, loads
from time import sleep
from .game.game_process import GameProcess
from .menu.menu_process import MenuProcess
from utils.utils import check_type


class CommunicateProcess:
    def __init__(self, server_connect, address):
        check_type(address, tuple)

        self.server_connect = server_connect
        self.address = address
        self.on = False
        self.process_receive = Process(target=self._process_receive)

        self.queue_send = Queue()
        self.process_send = Process(target=self._process_send, args=(self.queue_send, ))

    def _process_receive(self):
        while True:
            try:
                response = self.server_connect.recv(1024)
            except ConnectionResetError:
                break

            jdata = loads(response.decode('utf-8'))

            if jdata['type'] == 'game':
                game = GameProcess(jdata, self.queue_send)
            else:
                game = MenuProcess(jdata, self.queue_send)

            game.start()

    def _process_send(self, queue):
        while True:
            if queue.empty():
                sleep(10)
                continue

            aux = queue.get()

            try:
                check_type(aux, dict)
            finally:
                continue

            to_send = dumps(aux)
            self.server_connect.sendall(to_send)

    def start(self):
        self.process_send.start()
        self.process_receive

        self.process.join()



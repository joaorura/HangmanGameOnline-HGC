from multiprocessing import Process

from .game.game import Game
from .game.game_process import GameProcess
from .menu.menu_process import MenuProcess
from time import sleep


class ProcessAll(Process):
    def __init__(self, queue_send, queue_receive, address, client_status, rooms):
        self.queue_send = queue_send
        self.queue_receive = queue_receive
        self.address = address
        self.client_status = client_status
        self.rooms = rooms

        self.game = None

        super().__init__(target=self._run)

    def _run(self):
        self.game = Game(self.queue_send, self.queue_receive, self.rooms)

        while True:
            if not bool(self.client_status.value):
                print(f"\tEnf conection of: {self.address}")
                return

            if self.queue_receive.empty():
                sleep(0.1)
                continue

            jdata = self.queue_receive.get()

            if jdata['type'] == 'game':
                aux = GameProcess(jdata, self.game, self.address, self.queue_send, self.rooms)
            elif jdata['type'] == 'menu':
                aux = MenuProcess(jdata, self.queue_send, self.client_status,
                                  self.address, self.rooms, self.game)
            else:
                raise RuntimeError

            aux.start()

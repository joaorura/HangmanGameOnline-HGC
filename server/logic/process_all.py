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

        self.game = Game(queue_send, queue_receive, rooms)

        super().__init__(target=self._run)

    def _run(self):
        while True:
            if not bool(self.client_status.value):
                return

            if self.queue_receive.empty():
                sleep(0.1)
                continue

            jdata = self.queue_receive.get()
            print(jdata)

            if jdata['type'] == 'game':
                game = GameProcess(jdata, self.queue_send, self.rooms)
            elif jdata['type'] == 'menu':
                game = MenuProcess(jdata, self.queue_send, self.client_status,
                                   self.address, self.rooms, self.game)
            else:
                raise RuntimeError

            game.start()

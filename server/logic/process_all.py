from multiprocessing import Process
from time import sleep
from .game.game_process import GameProcess
from .menu.menu_process import MenuProcess


class ProcessAll:
    def __init__(self, queue_send, queue_receive):
        self.queue_send = queue_send
        self.queue_receive = queue_receive

        self.process = Process(target=self._run, args=(self.queue_send, self.queue_receive))

    @staticmethod
    def _run(queue_send, queue_receive):
        while True:
            if queue_receive.empty():
                sleep(10)
                continue

            jdata = queue_receive.get()

            if jdata['type'] == 'game':
                game = GameProcess(jdata, queue_send)
            else:
                game = MenuProcess(jdata, queue_send)

            game.start()

    def start(self):
        self.process.start()
        self.process.join()

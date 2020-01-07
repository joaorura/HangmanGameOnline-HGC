from multiprocessing import Process
from time import sleep
from interface.server_to_game.game_process import GameProcess
from interface.server_to_game.inter_game import InterGame
from interface.server_to_game.menu_process import MenuProcess


class ProcessAll:
    def __init__(self, queue_send, queue_receive):
        self.intergame = InterGame(queue_send, queue_receive)
        self.queue_send = queue_send
        self.queue_receive = queue_receive

        self.process = Process(target=self._run, args=(self.intergame, self.queue_send, self.queue_receive))

    @staticmethod
    def _run(intergame, queue_send, queue_receive):
        intergame.game_to_server.start()
        while True:
            if queue_receive.empty():
                sleep(0.1)
                continue

            aux = queue_receive.get()

            if aux['type'] == 'menu':
                run = MenuProcess(intergame, aux, queue_send)
            else:
                run = GameProcess(intergame, aux, queue_send)

            aux = Process(target=run.start())
            aux.start()
            print("eoq")

    def start(self):
        self.process.start()
        self.process.join()

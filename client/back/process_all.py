from multiprocessing import Process
from interface.server_to_game.game_process import GameProcess
from interface.server_to_game.inter_game import InterGame
from interface.server_to_game.menu_process import MenuProcess


class ProcessAll(Process):
    def __init__(self, queue_send, queue_receive):
        self.queue_send = queue_send
        self.queue_receive = queue_receive
        self.intergame = InterGame(queue_send, queue_receive)

        super().__init__(target=self._run)

    def _run(self):
        while True:
            if self.queue_receive.empty():
                continue

            aux = self.queue_receive.get()
            test = aux['type']
            if test == "menu":
                run = MenuProcess(self.intergame, aux, self.queue_send)
                run.start()
            elif test == "Game":
                run = GameProcess(self.intergame, aux, self.queue_send)
                run.start()
            elif test == "user":
                self.intergame.game_to_server.id.value = aux["id"]
            else:
                raise RuntimeError

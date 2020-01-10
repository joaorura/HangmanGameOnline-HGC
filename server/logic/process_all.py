from multiprocessing import Process
from .game.game_process import GameProcess
from .menu.menu_process import MenuProcess


class ProcessAll(Process):
    def __init__(self, queue_send, queue_receive, client_status):
        self.queue_send = queue_send
        self.queue_receive = queue_receive
        self.client_status = client_status

        super().__init__(target=self._run)

    def _run(self):
        while True:
            if self.queue_receive.empty():
                continue

            jdata = self.queue_receive.get()
            print(jdata)

            if jdata['type'] == 'game':
                game = GameProcess(jdata, self.queue_send)
            elif jdata['type'] == 'menu':
                game = MenuProcess(jdata, self.queue_send, self.client_status)
            else:
                raise RuntimeError

            game.start()

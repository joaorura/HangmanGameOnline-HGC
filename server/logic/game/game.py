from multiprocessing import Process


class Game(Process):
    def __init__(self, queue_send, queue_receive, rooms):
        self.queue_send = queue_send
        self.queue_receive = queue_receive
        self.rooms = rooms

        self._actual_id = None

        super().__init__(target=self._process)

    def _process(self):
        pass

    def is_ready(self):
        return self._actual_id is not None

    def set_game(self, id_room):
        if self.is_ready():
            raise RuntimeError("Game already set")
        else:
            self._actual_id = id_room

    def start(self):
        if self.is_ready():
            super().start()
        else:
            raise RuntimeError("Game not set")

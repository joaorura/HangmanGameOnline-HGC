from copy import deepcopy
from multiprocessing import Process
from time import sleep


class Game(Process):
    def __init__(self, queue_send, queue_receive, rooms):
        self.queue_send = queue_send
        self.queue_receive = queue_receive
        self.rooms = rooms

        self.actual_id = None

        super().__init__(target=self._process)

    def _process(self):
        while True:
            sleep(0.5)

    def is_ready(self):
        return self.actual_id is not None

    def set_game(self, id_room):
        self.actual_id = id_room

    def _check_state(self):
        if not self.is_ready():
            raise RuntimeError("Game not set")

    def get_room(self):
        self._check_state()
        return self.actual_id

    def remove_player(self, address):
        self._check_state()

        room = deepcopy(self.rooms[self.actual_id])
        players = room["players"]
        if len(players) == 1:
            self.end_game()
            return True

        for i in range(0, len(players)):
            if players[i]["address"] == address:
                del players[i]
                break

        self.rooms[self.actual_id.value] = room

        return False

    def end_game(self):
        self._check_state()
        del self.rooms[self.actual_id]

    def start(self):
        self._check_state()
        super().start()

from utils.utils import check_type
from copy import deepcopy


class GameProcess:
    def __init__(self, jdata, game, address, queue, rooms):
        check_type(jdata, dict)
        self.jdata = jdata
        self.game = game
        self.address = address
        self.queue = queue
        self.rooms = rooms

    def _init_game(self):
        id_room = self.jdata["id_room"]
        room = self.rooms[id_room]

        send = {
            "type": "game",
            "subtype": "init",
            "status": False
        }

        for i in room["players"]:
            if i["address"] == self.address:
                send["status"] = True
                break

        self.queue.put(send)
        self._send_state()

    def _send_state(self):
        id_room = self.jdata["id_room"]
        room = self.rooms[id_room]

        aux = deepcopy(room)
        del aux["word"]
        del aux["password"]
        for j in aux["players"]:
            del j["address"]

        send = {
            "type": "game",
            "subtype": "att_state",
            "state": aux
        }

        self.queue.put(send)

    def start(self):
        aux = self.jdata["subtype"]
        if aux == "init":
            self._init_game()
        else:
            raise RuntimeError("Error game process.")
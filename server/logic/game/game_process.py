from utils.utils import check_type
from copy import deepcopy


class GameProcess:
    def __init__(self, jdata, game, address, queue_send, queue_receive, rooms):
        check_type(jdata, dict)
        self.jdata = jdata
        self.game = game
        self.address = address
        self.queue_send = queue_send
        self.queue_receive = queue_receive
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

        self.queue_send.put(send)
        self._send_state()

    def _exit_game(self):
        aux = self.game.remove_player(self.address)
        if not aux:
            send = {
                "type": "game",
                "subtype": "end"
            }

            self.queue_send.put(send)

    def _end_game(self):
        self.game.end_game()

    def _send_state(self):
        id_room = self.game.get_room()
        try:
            room = self.rooms[id_room]
        except KeyError:
            send_0 = {
                "type": "game",
                "subtype": "end",
            }

            send_1 = {
                "type": "game",
                "subtype": "alert",
                "message": "The room no longer leaves."
            }

            aux = {
                "type": "new_game"
            }
            self.queue_receive.put(aux)

            self.queue_send.put(send_0)
            self.queue_send.put(send_1)

            return

        aux = deepcopy(room)
        aux["admin"] = aux["players"][0]["address"] == self.address
        del aux["word"]
        del aux["password"]
        for j in aux["players"]:
            del j["address"]

        aux["id_room"] = id_room

        send = {
            "type": "game",
            "subtype": "att_state",
            "state": aux
        }

        self.queue_send.put(send)

    def start(self):
        aux = self.jdata["subtype"]
        if aux == "init":
            self._init_game()
        elif aux == "exit":
            self._exit_game()
        elif aux == "end":
            self._end_game()
        elif aux == "att_request":
            self._send_state()
        else:
            raise RuntimeError("Error game process.")

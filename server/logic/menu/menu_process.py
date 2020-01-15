from copy import copy, deepcopy

from utils.utils import check_type, words
from random import randint


class MenuProcess:
    def __init__(self, json_data, queue, client_status, address, rooms, game):
        check_type(json_data, dict)
        self.json_data = json_data
        self.queue = queue
        self.client_status = client_status
        self.address = address
        self.rooms = rooms
        self.game = game

    def _create_room(self):
        while True:
            id_room = str(randint(0, 2000))
            try:
                self.rooms[id_room]
            except KeyError:
                break

            continue

        word = words()
        word_discover = ""
        for i in word:
            word_discover += "X"

        self.rooms[id_room] = {
            "name_room": self.json_data["name_room"],
            "password": self.json_data["password"],
            "players": [],
            "word": words(),
            "word_discover": word_discover,
            "attempts": 6,
            "total_attempts": 0,
            "rounds": 0,
            "turn": 0
        }

        self.json_data["id_room"] = id_room
        self.game.set_game(id_room)
        self.game.start()
        self._enter_room()

    def _enter_send(self, test, text=None):
        send = {
            "type": "menu",
            "subtype": "enter",
            "status": test,
        }

        if text is not None:
            send["message"] = text

        if test:
            send["id_room"] = self.json_data["id_room"]

        self.queue.put(send)

    def _enter_room(self):
        id_room = self.json_data["id_room"]

        try:
            room_data = self.rooms[id_room]
        except KeyError:
            print("Problem Error")
            self._enter_send(False, "Wrong id room.")
            return

        if self.json_data["password"] == room_data["password"]:
            aux = {
                "name_player": self.json_data["name_player"],
                "address": self.address,
            }

            copy = deepcopy(self.rooms[id_room])
            copy["players"].append(aux)
            self.rooms[id_room] = copy

            self._enter_send(True)
        else:
            self._enter_send(False, "Wrong Password.")

    def _exit_room(self):
        id_room = self.json_data["id_room"]

        for a in self.rooms[id_room]["players"]:
            if a["ip"] == self.address[0]:
                self.rooms[id_room]["players"].remove(a)

        send = {
            "type": "menu",
            "subtype": "exit"
        }

        self.queue.put(send)

    def _exit_all(self):
        self.client_status.value = False

    def start(self):
        aux = self.json_data['subtype']

        if aux == "end":
            self._exit_all()
        elif aux == 'create':
            self._create_room()
        elif aux == "enter":
            self._enter_room()
        elif aux == 'exit':
            self._exit_room()
        else:
            raise RuntimeError("Problem in MenuProcess")

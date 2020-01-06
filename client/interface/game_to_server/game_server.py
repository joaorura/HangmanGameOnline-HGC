from time import sleep


class GameServer:
    def __init__(self, queue_send, queue_receive):
        self.queue_send = queue_send
        self.queue_receive = queue_receive
        self.id = None

    def _return_function(self, send):
        def f():
            self.queue_send.put(send)

        return f

    def create_room(self, password):
        send = {
            "type": "room",
            "subtype": "create",
            "id": self.id,
            "password": password
        }

        return self._return_function(send)

    def enter_room(self, id_room, password):
        send = {
            "type": "room",
            "subtype": "enter",
            "id": self.id,
            "id_room": id_room,
            "password": password
        }

        return self._return_function(send)

    def exit_room(self):
        send = {
            "type": "room",
            "subtype": "exit",
            "id": self.id,
        }

        return self._return_function(send)

    def start(self):
        send = {
            "type": "menu",
            "subtype": "user"
        }

        self.queue_send.put(send)
        while self.queue_receive.empty():
            sleep(1)

        aux = self.queue_receive.get()
        self.id = aux["id"]



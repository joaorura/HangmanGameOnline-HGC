class GameServer:
    def __init__(self, queue_send, queue_receive):
        self.queue_send = queue_send
        self.queue_receive = queue_receive

    def _return_function(self, send):
        def f():
            self.queue_send.put(send)

        return f

    def create_room(self, name_player, name_room, password):
        if name_player == "":
            return "Name Player must be a string no empty"
        elif name_room == "":
            return "Name Room must be a string no empty"

        send = {
            "type": "menu",
            "subtype": "create",
            "name_player": name_player,
            "name_room": name_room,
            "password": password
        }

        self.queue_send.put(send)

        return None

    def enter_room(self, name_player, id_room, password):
        if name_player == "":
            return "Name Player must be a string no empty"
        elif id_room == "":
            return "Id Room must be a string no empty"

        send = {
            "type": "menu",
            "subtype": "enter",
            "name_player": name_player,
            "id_room": id_room,
            "password": password
        }

        self.queue_send.put(send)

        return None

    def exit_room(self):
        send = {
            "type": "room",
            "subtype": "exit",
        }

        return self._return_function(send)

    def end(self):
        send = {
            "type": "menu",
            "subtype": "end",
        }

        self.queue_send.put(send)

        while not self.queue_send.empty():
            continue

class GameServer:
    def __init__(self, queue_send, queue_receive):
        self.queue_send = queue_send
        self.queue_receive = queue_receive

    def _return_function(self, send):
        def f():
            self.queue_send.put(send)

        return f

    def create_room(self, name, password):
        send = {
            "type": "menu",
            "subtype": "create",
            "name": name,
            "password": password
        }

        self.queue_send.put(send)

    def enter_room(self, id_room_input, password_input):
        def f():
            id_room = id_room_input.get("1.0", "end-1c")
            password = password_input.get("1.0", "end-1c")

            send = {
                "type": "menu",
                "subtype": "enter",
                "id_room": id_room,
                "password": password
            }

            self.queue_send.put(send)

        return f

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

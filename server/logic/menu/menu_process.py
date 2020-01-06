from utils.utils import check_type


class MenuProcess:
    def __init__(self, jdata, queue):
        check_type(jdata, dict)
        self.jdata = jdata
        self.queue = queue

    def _send_id(self):
        send = {"id": 31231}
        self.queue.put(send)

        send = {
            "type": "menu",
            "subtype": "start"
        }
        self.queue.put(send)

    def _create_room(self):
        print("Create Room")

    def _exit_room(self):
        print("Exit Room")

    def start(self):
        aux = self.jdata['subtype']

        if aux == "user":
            self._send_id()
        elif aux == 'create_room':
            self._create_room()
        elif aux == 'exit_room':
            self._exit_room()
        else:
            print(aux)
            raise RuntimeError("Problem in MenuProcess")

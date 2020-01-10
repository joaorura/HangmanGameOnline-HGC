from utils.utils import check_type


class MenuProcess:
    def __init__(self, jdata, queue, client_status):
        check_type(jdata, dict)
        self.jdata = jdata
        self.queue = queue
        self.client_status = client_status

    def _send_id(self):
        send = {
            "type": "user",
            "subtype": "identification",
            "id": 31231
        }

        self.queue.put(send)

    def _create_room(self):
        print("Create Room")

    def _exit_room(self):
        print("Exit Room")

    def _exit_all(self):
        self.client_status.value = False

    def start(self):
        aux = self.jdata['subtype']

        if aux == "user":
                self._send_id()
        elif aux == "end":
            print("Fim do user k7")
        elif aux == 'create_room':
            self._create_room()
        elif aux == 'exit_room':
            self._exit_room()
        else:
            print(aux)
            raise RuntimeError("Problem in MenuProcess")

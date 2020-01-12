from utils.utils import check_type


class MenuProcess:
    def __init__(self, jdata, queue, client_status):
        check_type(jdata, dict)
        self.jdata = jdata
        self.queue = queue
        self.client_status = client_status

    def _create_room(self):
        print("Create Room")

    def _enter_room(self):
        print("Enter Room")

    def _exit_room(self):
        print("Exit Room")

    def _exit_all(self):
        self.client_status.value = False

    def start(self):
        aux = self.jdata['subtype']

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

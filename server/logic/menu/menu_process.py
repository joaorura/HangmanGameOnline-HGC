from utils.utils import check_type


class MenuProcess:
    def __init__(self, jdata, queue):
        check_type(jdata, dict)
        self.jdata = jdata
        self.queue = queue

    def _create_room(self):
        print("Create Room")

    def exit_room(self):
        print("Exit Room")

    def start(self):
        aux = self.jdata['type']

        if aux == 'create_room':
            self._create_room()
        elif aux == 'exit_room':
            self.exit_room()
        else:
            raise RuntimeError("Problem in MenuProcess")

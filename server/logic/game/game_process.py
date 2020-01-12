from utils.utils import check_type


class GameProcess:
    def __init__(self, jdata, queue, rooms):
        check_type(jdata, dict)
        self.jdata = jdata
        self.queue = queue
        self.rooms = rooms

    def start(self):
        print("Game")

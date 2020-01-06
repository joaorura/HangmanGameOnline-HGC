from utils.utils import check_type


class GameProcess:
    def __init__(self, jdata, queue):
        check_type(jdata, dict)
        self.jdata = jdata
        self.queue = queue

    def start(self):
        print("Game")
class GameProcess:
    def __init__(self, intergame, data, queue):
        self.intergame= intergame
        self.data = data
        self.queue = queue

    def start(self):
        print("Game client")

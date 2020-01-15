class GameProcess:
    def __init__(self, intergame, data, queue):
        self.intergame = intergame
        self.data = data
        self.queue = queue

    def _init_game(self):
        if not self.data["status"]:
            self.intergame.exit_room("Problems with room, please create another.")

    def _att_state(self):
        self.intergame.att_state(self.data["state"])

    def start(self):
        aux = self.data["subtype"]

        if aux == "init":
            self._init_game()
        elif aux == "att_state":
            self._att_state()
        else:
            raise RuntimeError("Error in GameProcess")

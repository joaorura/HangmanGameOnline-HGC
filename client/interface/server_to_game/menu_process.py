class MenuProcess:
    def __init__(self, intergame, data, queue):
        self.intergame = intergame
        self.data = data
        self.queue = queue

    def start(self):
        aux = self.data['subtype']

        if aux == "create" or aux == "enter":
            self.intergame.enter_room(self.data['id_room'], self.data['password'])
        elif aux == "exit":
            self.intergame.exit_room()
        elif aux == "start":
            self.intergame.start()
        else:
            raise RuntimeError

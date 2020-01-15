import tkinter as tk


class GameFront(tk.Frame):
    def __init__(self, inter_game, data, master):
        self.inter_game = inter_game
        self.data = data
        self.master = master

        super().__init__(master)

        self.name_room = tk.Label(self, text=f'Name Room: {self.data["name_room"]}')
        self.name_room.grid(row=0, column=0)

        self.round = tk.Label(self, text=f'Rounds: {self.data["rounds"]}')
        self.round.grid(row=0, column=1)

        self.times = []
        self._init_times()

        self.word = tk.Label(self, text=f'{self.data["word_discover"]}')
        self.word.grid(row=1, column=1)

        self.exit = tk.Button(self, text="Exit Room")
        self.exit.grid(row=2)

        self.players_time = []
        self._init_players_time()

        super().pack()

    def _init_times(self):
        aux = ""
        for i in range(0, self.data["attempts"]):
            aux += "O"

        for i in range(self.data["attempts"], self.data["total_attempts"]):
            aux += "X"

        self.times = tk.Label(self, text=f'Attempts: {aux}')
        self.times.grid(row=1, column=0)

    def _init_players_time(self):
        row = 3
        column = 0

        for i in range(0, len(self.data["players"])):
            if column == 4:
                row += 1

            if i == self.data["turn"]:
                aux = tk.Label(self, text=self.data["players"][i]["name_player"], background='yellow')
            else:
                aux = tk.Label(self, text=self.data["players"][i]["name_player"])

            aux.grid(row=row, column=column)

            self.players_time.append(aux)
            column += 1

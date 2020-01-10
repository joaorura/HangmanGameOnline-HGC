import tkinter as tk


class Menu(tk.Frame):
    def __init__(self, intergame, master=None):
        super().__init__(master)
        self.intergame = intergame
        self.master = master

        self.label = tk.Label(self, text="Hangman Game Online (HGO)")
        self.label.pack()

        self.button_create = tk.Button(self, text="Create Room", command=self._button_create)
        self.button_create.pack()
        self.button_enter = tk.Button(self, text="Enter Room", command=self._button_enter)
        self.button_enter.pack()

    def _button_exit(self):
        self.intergame.exit_client()

    def _button_create(self):
        pass

    def _button_enter(self):
        pass

    def change_menu(self, param):
        pass

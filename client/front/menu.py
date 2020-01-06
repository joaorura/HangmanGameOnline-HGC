import tkinter as tk


class Menu(tk.Frame):
    def __init__(self, intergame, master=None):
        self.__init__()
        self.intergame = intergame
        self.master = master
        self.pack()
        self.create_menu()

    def _button_create(self):
        pass

    def _button_enter(self):
        pass

    def _button_exit(self):
        pass

    def create_menu(self):
        self.label = tk.Label(self, text="Hangman Game Online (HGO)")
        self.button_create = tk.Button(self, text="Create Room", command=self._button_create)
        self.button_enter = tk.Button(self, text="Enter Room", command=self._button_enter)
        self.button_exit = tk.Button(self, text="Exit", command=self._button_exit)

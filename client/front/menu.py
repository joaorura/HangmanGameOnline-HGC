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

    def _button_create(self):
        win = tk.Toplevel()

        title = tk.Label(win, text="Create Room")
        title.pack()

        name = tk.Label(win, text="Name: ")
        name.pack()

        name_input = tk.Text(win)
        name_input.pack()

        password = tk.Label(win, text="Password: ")
        password.pack()

        password_input = tk.Text(win)
        password_input.pack()

        commit_button = tk.Button(win, text="Ok", command=self.intergame.create_room(name_input, password_input))
        commit_button.pack()

    def _button_enter(self):
        win = tk.Toplevel()

        title = tk.Label(win, text="Enter Room")
        title.pack()

        _id = tk.Label(win, text="Code: ")
        _id.pack()

        id_input = tk.Text(win)
        id_input.pack()

        commit_button = tk.Button(win, text="Ok", command=self.intergame.enter_room(id_input))
        commit_button.pack()

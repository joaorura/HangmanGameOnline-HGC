import tkinter as tk


class Menu(tk.Frame):
    def __init__(self, intergame, master):
        super().__init__(master)
        self.intergame = intergame

        self.label = tk.Label(self, text="Hangman Game Online (HGO)")
        self.label.pack()

        self.button_create = tk.Button(self, text="Create Room", command=self._button_create)
        self.button_create.pack()

        self.button_enter = tk.Button(self, text="Enter Room", command=self._button_enter)
        self.button_enter.pack()

        self.sub_window = None

        master.focus_force()
        master.grab_set()

        super().grid()


    def _aux_create(self, input_1, input_2, function):
        def f():
            result_1 = input_1.get("1.0", "end-1c")
            result_2 = input_2.get("1.0", "end-1c")

            function(result_1, result_2)

        return f

    def _close_sub_janel(self):
        self.sub_window.destroy()
        self.sub_window = None

    def _create_sub(self, text, function):
        if self.sub_window is not None:
            self.sub_window.lift()
        else:
            self.sub_window = tk.Toplevel()

            title = tk.Label(self.sub_window, text=text[0])
            title.pack()

            input_name_1 = tk.Label(self.sub_window, text=text[1])
            input_name_1.pack()

            input_1 = tk.Text(self.sub_window, height=1, padx=2, pady=2)
            input_1.pack()

            input_name_2 = tk.Label(self.sub_window, text=text[2])
            input_name_2.pack()

            input_2 = tk.Text(self.sub_window, height=1, padx=2, pady=2)
            input_2.pack()

            commit_button = tk.Button(self.sub_window, text="Ok", command=self._aux_create(input_1, input_2, function))
            commit_button.pack()

            self.sub_window.geometry("150x150")
            self.sub_window.protocol("WM_DELETE_WINDOW", self._close_sub_janel)
            self.sub_window.transient(self)
            self.sub_window.focus_force()
            self.sub_window.grab_set()

    def _button_create(self):
        self._create_sub((
            "Create Room",
            "Name: ",
            "Password: "
        ), self.intergame.game_to_server.create_room)

    def _button_enter(self):
        self._create_sub((
            "Enter Room",
            "Id Room: ",
            "Password: "
        ), self.intergame.game_to_server.enter_room)

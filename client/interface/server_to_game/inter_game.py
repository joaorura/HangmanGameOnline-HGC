from front.menu.menu import Menu
from interface.game_to_server.game_server import GameServer
import tkinter as tk


class InterGame:
    def __init__(self, dict_front, queue_send, queue_receive):
        self.dict_front = dict_front
        self.dict_front["game_start"] = False
        self.game_to_server = GameServer(queue_send, queue_receive)

    def enter_room(self, data):
        self.dict_front["game_start"] = True

    def exit_room(self):
        pass

    def _periodic_inter(self, root, window):
        aux = True

        def f():
            if self.dict_front["game_start"]:
                nonlocal aux
                if aux:
                    window.destroy()
                    aux = False
                else:
                    pass
            root.after(500, f)

        return f

    def start(self):
        root = tk.Tk()
        root.geometry("400x400")
        window = Menu(self, root)
        aux = self._periodic_inter(root, window)
        root.after(200, aux)
        root.mainloop()

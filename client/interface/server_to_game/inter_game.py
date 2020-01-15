from front.game.game_front import GameFront
from front.menu.menu import Menu
from interface.game_to_server.game_server import GameServer
import tkinter as tk
from tkinter.messagebox import showerror


class InterGame:
    def __init__(self, queue_front, queue_send, queue_receive):
        self.queue_front = queue_front
        self.queue_send = queue_send

        self.game_to_server = GameServer(queue_send, queue_receive)

    def enter_room(self, data):
        print(data["status"])
        if not data["status"]:
            self.queue_front.put(("alert", data["message"]))
        else:
            self.queue_front.put(("game_start", None))

            send = {
                "type": "game",
                "subtype": "init",
                "id_room": data["id_room"]
            }

            self.queue_send.put(send)

    def exit_room(self, alert=None):
        self.queue_front.put(("end_game", None))
        if alert is None:
            alert = "Error"

        self.queue_front.put(("alert", alert))

    def att_state(self, data):
        self.queue_front.put(("game_update", data))

    def _periodic_inter(self, root, page):
        def f():
            nonlocal page
            if self.queue_front.empty():
                root.after(500, self._periodic_inter(root, page))
                return

            aux = self.queue_front.get()
            element = aux[0]
            data = aux[1]

            if element == "game_update":
                if type(page) == Menu:
                    page.destroy()
                page = GameFront(self, data, root)
            elif element == "game_start":
                page.destroy()
            elif element == "end_game":
                page = Menu(self, root)
            elif element == "alert" and data is not None:
                showerror("Error", data)
            else:
                raise RuntimeError("Error in periodic inter front")

            root.after(500, self._periodic_inter(root, page))

        return f

    def start(self):
        root = tk.Tk()
        root.geometry("400x400")
        window = Menu(self, root)
        root.after(500, self._periodic_inter(root, window))
        root.mainloop()

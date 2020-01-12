from front.menu import Menu
from interface.game_to_server.game_server import GameServer
import tkinter as tk


class InterGame:
    def __init__(self, queue_send, queue_receive):
        self.game_to_server = GameServer(queue_send, queue_receive)
        self.window = None

    def enter_room(self, id_room_input):
        pass

    def exit_room(self):
        self.window.change_menu((
            self.game_to_server.create_room,
            self.game_to_server.enter_room,
            self.game_to_server.exit_room
        ))

    def start(self):
        root = tk.Tk()
        root.geometry("300x200")

        self.window = Menu(self, root)

        root.mainloop()

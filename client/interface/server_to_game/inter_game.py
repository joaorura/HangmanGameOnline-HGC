from front.menu import Menu
from interface.game_to_server.game_server import GameServer
import tkinter as tk

from interface.server_to_game.window_process import WindowProcess


class InterGame:
    def __init__(self, queue_send, queue_receive):
        self.game_to_server = GameServer(queue_send, queue_receive)
        self.window = None

    def enter_room(self, id_room):
        self.window.change_to_room(id_room, self.game_to_server.enter_room)
        pass

    def exit_room(self):
        self.window.change_menu((
            self.game_to_server.create_room,
            self.game_to_server.enter_room,
            self.game_to_server.exit_room
        ))

        pass

    def start(self):
        aux = tk.Tk()
        self.window = Menu(self, aux)
        self.window.pack()
        self.window.change_menu((
            self.game_to_server.create_room,
            self.game_to_server.enter_room,
            self.game_to_server.exit_room
        ))

        self.window.mainloop()

from front.menu import Menu
from interface.game_to_server.game_server import GameServer
import tkinter as tk


class InterGame:
    def __init__(self, queue_send, queue_receive):
        self.game_to_server = GameServer(queue_send, queue_receive)
        self.window = None

    def create_room(self, name_input, password_input):
        def f():
            name = name_input.get("1.0", "end-1c")
            password = password_input.get("1.0", "end-1c")

            send = {

            }
            print(name, password)

        return f

    def enter_room(self, id_room_input):
        def f():
            id_room = id_room_input.get("1.0", "end-1c")
            print(id_room)

        return f

    def exit_room(self):
        self.window.change_menu((
            self.game_to_server.create_room,
            self.game_to_server.enter_room,
            self.game_to_server.exit_room
        ))

    def start(self):
        aux = tk.Tk()
        self.window = Menu(self, aux)
        self.window.pack()
        self.window.mainloop()

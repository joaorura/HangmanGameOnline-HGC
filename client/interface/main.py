from back.server_connection import ServerConnection
from interface.server_to_game.inter_game import InterGame
from interface.game_to_server.game_server import GameServer


def start():
    print("Starting Client")
    server_connection = ServerConnection("localhost", 20)
    server_connection.start()


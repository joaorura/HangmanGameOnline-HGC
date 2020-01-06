from back.server_connection import ServerConnection


def start():
    print("Starting Client")
    server_connection = ServerConnection("localhost", 20)
    server_connection.start()


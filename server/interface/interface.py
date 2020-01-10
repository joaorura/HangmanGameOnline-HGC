from logic.receive import Receive


def start_server(address, port):
    server = Receive(address, port)
    server.start()


def edit_server():
    pass


def end_server():
    pass

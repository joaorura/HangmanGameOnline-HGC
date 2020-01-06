from logic.receive import Receive


def start_server():
    server = Receive("localhost", 20)
    server.start()


def edit_server():
    pass


def end_server():
    pass

class Room:
    def __init__(self, admin_ip, admin_port, name, password):
        self.admin_ip = admin_ip
        self.admin_port = admin_port
        self.name = name
        self.password = password
        self.code = self._create_code()

    def _create_code(self):
        return self.name

    def att_admin(self, admin_ip, admin_port):
        self.admin_ip = admin_ip
        self.admin_port = admin_port

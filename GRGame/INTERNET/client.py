import socket




class client():
    def __init__(self,host: str = "localhost", port: int = 9090, recv_range: int = 2048, timeout: float = 0.1):
        self.host = host
        self.port = port
        self.recv_range = recv_range
        self.timeout = timeout
        self.sock = socket.socket()
    def connect_server(self):
        try:
            self.sock.connect((self.host, self.port))
        except ConnectionRefusedError as e:
            return False
        else:
            self.sock.settimeout(self.timeout)
            self.response_server = None
            return True
    def send(self,send_data: str):
        try:
            self.sock.send(bytes(str(send_data).encode("utf-8")))
            self.response_server = self.sock.recv(self.recv_range)

        except socket.timeout as e:
            pass
        else:
            if self.response_server == None:
                return "0"
            else:
                return self.response_server
    def get(self):
        return True





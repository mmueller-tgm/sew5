from Abstract import Socket
import socket


class TestSocket(Socket):
    """
    This Socket just returns the given Message and is used for testing.
    """
    def __init__(self):
        Socket.__init__(self)

    def print_line(self, msg):
        return msg

    def read_line(self, msg=''):
        return msg


class ServerSocket(Socket):
    """
    This Socket listens on the specified port and accepts one Connection.
    """
    def __init__(self, ip='localhost', port=5005, buffer=1024):
        Socket.__init__(self)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((ip, port))
        self.buffer = buffer
        self.socket.listen(1)
        self.conn, self.addr = self.socket.accept()

    def print_line(self, msg):
        return self.conn.send(msg)

    def read_line(self, msg=''):
        return self.conn.recv(self.buffer)


class ClientSocket(Socket):
    """
    This Socket connects to the specified ip:port
    """
    def __init__(self, ip='localhost', port=5005, buffer=1024):
        Socket.__init__(self)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((ip, port))
        self.buffer = buffer

    def print_line(self, msg):
        return self.socket.send(msg)

    def read_line(self, msg=''):
        return self.socket.recv(self.buffer)

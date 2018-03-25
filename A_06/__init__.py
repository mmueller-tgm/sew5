import threading

from Decorators import *
from Sockets import *

class ClientThread(threading.Thread):
    def __init__(self, port=5005, addr='localhost'):
        threading.Thread.__init__(self)
        self.port = port
        self.addr = addr
        self.start()

    def run(self):
        """
        Connects to a specified Server and passes inputs from the commandline through.
        :return:
        """
        self.socket = ClientSocket(port=self.port, ip=self.addr)
        self.socket = ConcreteAESDecorator(self.socket)
        self.socket = ConcreteBASE64Decorator(self.socket)
        while True:
            # send message to server from cmdline
            self.socket.print_line(input().encode('utf-8'))
            # print the answer
            print(self.socket.read_line().decode('utf-8'))


class ServerThread(threading.Thread):
    def __init__(self, port=5005):
        threading.Thread.__init__(self)
        self.port = port
        self.start()

    def run(self):
        """
        Initializes for exactly one client and echos it's message
        :return:
        """
        # A server Socket is needed to connect to a client
        self.socket = ServerSocket(port=self.port)

        # Decorators have to be the same as the client, OutputDecorators are optional
        self.socket = ConcreteOutputDecorator(self.socket)

        self.socket = ConcreteAESDecorator(self.socket)

        self.socket = ConcreteBASE64Decorator(self.socket)
        while True:
            # loop read lines back
            line = self.socket.read_line()
            print(line)
            self.socket.print_line(line)


if __name__ == "__main__":
    port = 5005
    st = ServerThread(port)
    ct = ClientThread(port)

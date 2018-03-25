from abc import ABC, abstractmethod


class Socket(ABC):
    """
    Abstract Class that everything inharits from.
    """
    @abstractmethod
    def print_line(self, msg):
        """
        Called when sending a message

        :param msg: message to send
        :return:
        """
        pass

    @abstractmethod
    def read_line(self, msg=''):
        """
        Called when recieving a message

        :param msg: only used by other decorators
        :return:
        """
        pass


class SocketDecorator(Socket, ABC):
    """
    Abstract Socket
    """
    def __init__(self, component):
        Socket.__init__(self)
        self.component = component

    def print_line(self, msg):
        msg = msg
        return self.component.print_line(msg)

    def read_line(self, msg=''):
        msg = self.component.read_line(msg)
        return msg

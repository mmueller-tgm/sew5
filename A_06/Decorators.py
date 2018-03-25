import base64
from Abstract import SocketDecorator
from Crypto.Cipher import AES


class ConcreteBASE64Decorator(SocketDecorator):
    """
    Ein Konkreter Decorator, der BASE64 Codierung umsetzt.
    """
    def __init__(self, component):
        SocketDecorator.__init__(self, component)

    def print_line(self, msg):
        msg = base64.standard_b64encode(msg)
        msg = self.component.print_line(msg)
        return msg

    def read_line(self, msg=''):
        msg = self.component.read_line(msg)
        msg = base64.standard_b64decode(msg)
        return msg


class ConcreteBASE16Decorator(SocketDecorator):
    """
    Ein Konkreter Decorator, der BASE16 Codierung umsetzt.
    """
    def __init__(self, component):
        SocketDecorator.__init__(self, component)

    def print_line(self, msg):
        msg = base64.b16encode(msg)
        msg = self.component.print_line(msg)
        return msg

    def read_line(self, msg=''):
        msg = self.component.read_line(msg)
        msg = base64.b16decode(msg)
        return msg


class ConcreteBASE32Decorator(SocketDecorator):
    """
    Ein Konkreter Decorator, der BASE32 Codierung umsetzt.
    """
    def __init__(self, component):
        SocketDecorator.__init__(self, component)

    def print_line(self, msg):
        msg = base64.b32encode(msg)
        msg = self.component.print_line(msg)
        return msg

    def read_line(self, msg=''):
        msg = self.component.read_line(msg)
        msg = base64.b32decode(msg)
        return msg


class ConcreteOutputDecorator(SocketDecorator):
    """
    Ein Konkreter Decorator, der zwischen andere Layer geschalten werden kann, um deren Werte auszugeben und weiterzugeben.
    """
    def __init__(self, component):
        SocketDecorator.__init__(self, component)

    def print_line(self, msg):
        print(msg)
        return self.component.print_line(msg)

    def read_line(self, msg=''):
        return self.component.read_line(msg)


class ConcreteAESDecorator(SocketDecorator):
    def __init__(self, component, key='qwertzuiopasdfgh', iv='qwertzuiopasdfgh'):
        """
        Initializes a Decorator, that encrypts and decrypts using AES.

        :param component: The Component it decorates
        :param key: The key. It has to be 16, 24, or 32 bytes long
        :param iv: The IV (Initialisation Vector) prevents recognition Attacks by shifting the message. It has to be 16b long
        """
        SocketDecorator.__init__(self, component)
        self.aes = AES.new(key, AES.MODE_CBC, iv)

    def print_line(self, msg):
        """
        Is run when sending a Line.

        :param msg: unencrypted message
        :return: encrypted message
        """
        while(len(msg)%16!=0):
            msg = b' ' + msg
        msg = self.aes.encrypt(msg)
        msg = self.component.print_line(msg)
        return msg

    def read_line(self, msg=''):
        """
        Is run when recieving Message

        :param msg:
        :return:
        """
        msg = self.component.read_line(msg)
        msg = self.aes.decrypt(msg)
        return msg

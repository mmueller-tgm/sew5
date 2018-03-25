import requests
import json


class RESTModel:
    """
        A simple REST client
    """

    def __init__(self, address='localhost', port=8080):
        """
            Initiaizes the address and port of the REST server
        :param address: the dns/ip address of the server
        :param port: the port of the server
        """
        self.addr = address
        self.port = str(int(port))

    def set_addr(self, addr):
        """
            Set the address of the REST server
        :param addr: address of the REST server
        """
        self.addr = addr

    def set_port(self, port):
        """
            Set the port of the REST server
        :param port: port of the REST server
        """
        self.port = str(int(port))

    def get(self, text=''):
        """
            Send a request to the REST server and get the response
        :param text: string being looked at
        :return: json dump of response
        """
        try:
            resp = requests.get('http://' + self.addr +
                                ':' + self.port, {'text': text})
            return resp.text
        except requests.RequestException:
            return json.dumps({'reliable': False, 'language': 'Server Not Reached', 'short': 'nA', 'prob': 0})


if __name__ == "__main__":
    t = RESTModel(port=8080)
    print(t.get('das ist ein test'))
    print(t.get('this is a test'))

import argparse
import cherrypy
import pycld2
import json


@cherrypy.expose
class StringGeneratorWebService(object):
    """
        RESTful webservice using the pycld2 library to check the language of a given text.
    """

    @cherrypy.expose
    def index(self, text=""):
        """
        :param text: String beeing checked
        :return: json dump of the response
        """
        a, b, c = pycld2.detect(text)
        return json.dumps({'reliable': a, 'language': c[0][0], 'short': c[0][1], 'prob': c[0][2]})


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", metavar='p', type=int,
                        help='Port of the server', default=8080)
    parser.add_argument("--address", metavar='addr', type=str,
                        help='Port of the server', default='localhost')
    args = parser.parse_args()

    cherrypy.config.update(
        {'server.socket_port': args.port, 'server.socket_ip': args.address})
    cherrypy.quickstart(StringGeneratorWebService())

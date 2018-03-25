import requests
import xml.etree.ElementTree as ET


class Model:
    """
        The controller handels the requests to the api and parsing of the response

        :var format: the typ of format for the response
    """

    def __init__(self):
        """
            The init sets the standard format, which is json
        """
        self.format = "json"

    def requestJson(self, origin, destination):
        """
            Calls the google navigation api and prases the json to a easily readable String, if a error happens the method
            will return a error message

            :param origin: origin of the route
            :param destination: destination of the route
            :return: String which will be displayed
        """
        url = "http://maps.googleapis.com/maps/api/directions/json"
        params = {"origin": origin, "destination": destination, "sensor": "false", "language": "de"}
        data = requests.get(url, params)
        if data.status_code != requests.codes.ok:
            return "Fehler aufgetreten"
        output = data.json()

        text = ""
        for route in output['routes']:
            for leg in route['legs']:
                text += "Die Gesamtdauer beträgt " + leg['duration']['text'] + ", die Gesamtentfernung: " + \
                        leg['distance']['text'] + "<br><br>"
                for step in leg['steps']:
                    text += step['html_instructions'] + ", Entfernung " + step['distance']['text'] + \
                            ", Dauer " + step['duration']['text'] + "<br>"

        return text

    def requestXml(self, origin, destination):
        """
            Calls the google navigation api and prases the xml to a easily readable String, if a error happens the method
            will return a error message

            :param origin: origin of the route
            :param destination: destination of the route
            :return: String which will be displayed
        """
        url = "http://maps.googleapis.com/maps/api/directions/xml"
        params = {"origin": origin, "destination": destination, "sensor": "false", "language": "de"}
        data = requests.get(url, params)
        if data.status_code != requests.codes.ok:
            return "Fehler aufgetreten"
        print("test")

        text = ""
        tree = ET.ElementTree(ET.fromstring(data.text))
        for leg in tree.findall("route/leg/"):
            if leg.tag == "duration":
                text += "Die Gesamtdauer beträgt " + leg.find("text").text
            if leg.tag == "distance":
                text += ", die Gesamtentfernung: " + leg.find("text").text + "<br><br>"

        for step in tree.findall("route/leg/step/"):
            if step.tag == "html_instructions":
                text += step.text
                print(step.text)
            if step.tag == "duration":
                text += ", " + step.find("text").text + "<br>"
                print(step.find('text').text)
            if step.tag == "distance":
                text += ", " + step.find("text").text
                print(step.find('text').text)

        return text

    def setformat(self, value):
        """
        Sets the format to the given parameter
        :param value: value which can be json or xml
        :return: None
        """
        self.format = value

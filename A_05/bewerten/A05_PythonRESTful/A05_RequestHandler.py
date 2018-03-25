"""
@author: 
@date: 18-10-2017
@use: Contains the class that handles requests
"""
import requests
import xml.etree.ElementTree as ET


class A05RequestHandler:

    def __init__(self):
        """
        The constructor sets some major things for the request.
        """
        self.url = 'https://maps.googleapis.com/maps/api/directions/'
        self.apiKey = "AIzaSyAe_FFYgIouyVQ-TCLT-gfJ2VXc-TqBYlk"
        self.language = "de"

    def handle_request(self, origin, destination, json_or_xml):
        """
        This method sets the params for the request. Then it the method checks if the request should be handled by
        JSON or XML and then it calls the converting method for the responses.

        :param origin: Origin of path finding
        :param destination: Destination of the path finding
        :param json_or_xml: Boolean parameter that decides if the request should be done by JSON or XML
        :return: The converted values
        """
        params = {"origin": origin,
                  "destination": destination,
                  "sensor": "false",
                  "key": self.apiKey,
                  "language": self.language}

        if json_or_xml:
            response = requests.get(self.url + "json", params)
            converted_value = self.convert_json(response.json())
        else:
            response = requests.get(self.url + "xml", params)
            converted_value = self.convert_xml(response.text)

        return converted_value

    @staticmethod
    def convert_json(raw_json_data):
        """
        Converts the JSON response to a string that can be displayed on the output screen. If something went wrong
        it will give back a static output and the status of the request.

        :param raw_json_data: The JSON response that needs to be converted
        :return: An array that contains the converted JSON data and the status of the request
        """
        try:
            json_data = raw_json_data["routes"][0].get("legs")[0]
            duration = json_data.get("duration").get("text")
            distance = json_data.get("distance").get("text")

            output = "Die Gesamtdauer beträgt <b>" + duration + "</b>, " \
                                                                "die Gesamtentfernung: <b>" + distance + "</b><br><br>"

            for item in json_data.get("steps"):
                output += item.get("html_instructions") + ", Entfernung: " + item.get("distance").get("text") \
                         + ", Dauer: " + item.get("duration").get("text") + "<br>"
        except Exception as error:
            print(error)
            output = "Something went wrong :("

        return [output, raw_json_data["status"]]

    @staticmethod
    def convert_xml(raw_xml_data):
        """
        Converts the XML response to a string that can be displayed on the output screen. If something went wrong
        it will give back a static output and the status of the request.

        :param raw_xml_data: The XML response that needs to be converted
        :return: An array that contains the converted XML data and the status of the request
        """
        xml_data = ET.fromstring(raw_xml_data)
        leg_xml_data = xml_data[1][1]
        try:
            output = "Die Gesamtdauer beträgt <b>" + leg_xml_data.find("distance")[1].text + \
                     "</b>, die Gesamtentfernung: <b>" + leg_xml_data.find("duration")[1].text + "</b><br><br>"
            for child in leg_xml_data.iter("step"):
                output += child.find("html_instructions").text + ", Entfernung: " \
                          + child.find("distance")[1].text \
                          + ", Dauer: " + child.find("duration")[1].text + "<br>"
        except Exception as error:
            print(error)
            output = "Something went wrong :("
        return [output, xml_data[0].text]

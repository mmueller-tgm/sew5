#!/bin/python3.4
# -*- coding: utf-8 -*-
"""
Autor: Maximilian Müller
Aufgabe: A05
Datei: GoogleNavModell.py
Bescheibung:
Das Modell beantragt die Route von der Google Directions API anhand der Daten die es vom Controller bekommt.
https://developers.google.com/maps/documentation/directions/
"""
import requests


class GoogleNavModel:
    def __init__(self, src="", dest=""):
        """
        Initializes values for source and destination
        :param src: String identifying the origin of the trip
        :param dest: String identifying the destination of the trip
        """
        self.src = ""
        self.dest = ""
        self.set_source(src)
        self.set_destination(dest)

    def set_source(self, src):
        """
        Sets the Origin of the trip and formats it correctly
        :param src: String identifying the origin of the trip
        :return:
        """
        # REST needs the string formatted with "+" signs instead of spaces (" ")
        self.src = src.split(" ")
        self.src = "+".join(self.src)

    def set_destination(self, dest):
        """
        Sets the Destination of the trip and formats it correctly
        :param dest: String identifying the destination of the trip
        :return:
        """
        # REST needs the string formatted with "+" signs instead of spaces (" ")
        self.dest = dest.split(" ")
        self.dest = "+".join(self.dest)

    def get_directions(self) -> str:
        """
        Returns the formatted text, describing the path to take.
        :rtype: (str, str)
        :return: A tuple with the HTTP status code and the formatted text
        """
        # define the payload
        payload={"mode":"DRIVING", "origin":self.src, "destination":self.dest, "language":"de", "units":"metric"}
        # request from the google api
        x = requests.get("http://maps.googleapis.com/maps/api/directions/json", payload).json()
        # if the request was ok continue
        status = x['status']
        if x['status'] == "OK":
            # time until arrival
            time = (x['routes'][0]['legs'][0]['duration']['text'])
            # the distance to the destination
            distance = (x['routes'][0]['legs'][0]['distance']['text'])
            # print the time and distance
            text = "<p>Die Gesamtdauer beträgt <b>%s</b>, die Gesamtentfernung:<b>%s</b></p>" % (time, distance)

            text += "\n\n<p>"

            # print every step to the destination
            for y in x['routes'][0]['legs'][0]['steps']:
                text += y['html_instructions'] + ". (Dauer: "+y['duration']['text']+", Entfernung: "+y['distance']['text']+") <br>"
            text += "</p>"
        # else return an empty String
        else:
            text = ""
        return status, text

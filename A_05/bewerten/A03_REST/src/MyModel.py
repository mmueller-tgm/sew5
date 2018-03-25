import json
import requests

class MyModel():
    def __init__(self, origin,dest):
        self.url = "http://maps.googleapis.com/maps/api/directions/json"
        self.origin = origin
        self.dest = dest



    def getJson(self):
        params = {"origin": self.origin,
                  "destination" : self.dest,
                  "sensor" : "false",
                  "language" : "de",
        }
        print(params)
        json_data = requests.get(self.url,params)

        return json_data.json()

    def jsonToText(self,jsonD):
        str = ""
        print (jsonD)
        for i in jsonD['routes'][0]['legs'][0]['steps'] :
            str += i['html_instructions'] + "\n"
        return str
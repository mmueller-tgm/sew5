import requests
class MyModel(object):

    def __init__(self):
        """
        Der Konstruktor
        """
        self.url = "https://maps.googleapis.com/maps/api/directions/json"
        self.apiKey = "AIzaSyAlDjrpTxryOjD75F5om3eq1wYqjTpbQWA"

    def findWay(self,origin,destination):
        """
        Hier erfolgt der eigentliche Aufruf der Google-API, das Ergebnis wird dann in self.output für die weiterverarbeitung geschrieben

        :param origin: Startpunkt des Weges
        :param destination: Ziel des Weges
        :return:
        """
        # Params fuer die google API
        params = {"origin": origin,
                  "destination": destination,
                  "sensor": "false",
                  "language": "de",
                  "key":self.apiKey}
        self.output={}

        try:
            response = requests.get(self.url, params, verify=False)
            self.output = response.json()
        except Exception:
            self.output['status']="Fehler beim Verbinden"
        # print(response.content.decode("utf-8"))


    def getStatus(self):
        """
        Returns den Status der Berechnung

        :return: Status der Berechnung
        """
        return self.output['status']


    def getWay(self):
        """
        gibt den von der API generierten weg als html formatiert zurueck

        :return: Weganleitung in html-Format
        """

        gesamtEntfernung=self.output['routes'][0]["legs"][0]["distance"]["text"]
        gesamtDauer=self.output['routes'][0]["legs"][0]["duration"]["text"]
        gesamtInfos="Die Gesamtdauer beträgt <b>"+gesamtDauer+"</b>, die Gesamtentfernung: <b>"+gesamtEntfernung+"</b><br/><br/>"

        schritte=[]
        for step in self.output['routes'][0]["legs"][0]["steps"]:
            # print(step["distance"]["text"])
            schrittEntfernung=step["distance"]["text"]
            schrittDauer=step["duration"]["text"]
            schrittHtml=step["html_instructions"]
            schritte.append(schrittHtml + ", Entfernung "+schrittEntfernung+", Dauer "+schrittDauer)

        alleSchritte = ""
        for schritt in schritte:
            alleSchritte+=schritt+"<br/>"

        return gesamtInfos+"\n"+alleSchritte
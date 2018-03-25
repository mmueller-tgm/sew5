import requests


class Model:
    def __init__(self, src, dest):
        self.set_src(src)
        self.set_dest(dest)

    def set_src(self, src):
        self.src = '+'.join(src.split(" "))

    def set_dest(self, dest):
        self.dest = '+'.join(dest.split(" "))

    def rec(self):
        payload = {"mode": "DRIVING", "origin": self.src, "destination": self.dest, "language": "de", "units": "metric", "sensor": 'false'}
        self.resp = requests.get("http://maps.googleapis.com/maps/api/directions/json", payload).json()
        return self.resp

    def interpreted_rec(self):
        self.rec()
        status = self.resp['status']
        if self.resp['status'] == "OK":
            time = (self.resp['routes'][0]['legs'][0]['duration']['text'])
            distance = (self.resp['routes'][0]['legs'][0]['distance']['text'])
            text = "Die Gesamtdauer beträgt %s, die Gesamtentfernung: %s" % (time, distance)
            text += "\n"
            for y in self.resp['routes'][0]['legs'][0]['steps']:
                text += y['html_instructions'] + ". (Dauer: "+y['duration']['text']+", Entfernung: "+y['distance']['text']+") \n"
        else:
            text = ""
        return status, text


    def send(self):
        pass


if __name__ == '__main__':
    model = Model('wien 19', 'breslau')
    print(model.interpreted_rec()[1])
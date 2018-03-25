#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import threading
import random
import math
import time


def rand_int_range(x, y=0):
    x += 1
    return math.floor(random.randrange(y, x))


class Main:
    def __init__(self, amt, width, height, stime):
        # array von schneeflocken
        self.schneeflocken = []
        self.width = width
        self.height = height

        # initialisieren der x-Positionen
        for i in range(0, amt):
            self.schneeflocken.append(Schneeflocke(rand_int_range(width), height, stime))

        # starten der Schneeflocken Threads
        for o in self.schneeflocken:
            o.start()

        # solage noch nicht alle schneeflocken unten angekommen sind
        while Schneeflocke.counter < amt:
            # array an Positionen der Schneeflocken
            self.pos = []
            time.sleep(stime)
            # abfrage der positionen
            for o in self.schneeflocken:
                self.pos.append(o.get_xy())
            # ausgabe der positionen
            self.print_pos()

        # beenden der Threads
        for o in self.schneeflocken:
            o.join()

    def print_pos(self):
        # ausgabe String
        out = ""
        # iterieren durch die höhe
        for h in range(0, self.height):
            #iterieren durch die breite
            for w in range(0, self.width):
                # wenn (w, h) in den positionen der schneeflocken sind dann ausgabe
                if (w, h) in self.pos:
                    out += "❄"
                else:
                    out += " "
            out += "\n"
        # korrektes clear screen für das os
        if os.name == 'posix':
            os.system('clear')
        else:
            os.system('cls')
        print(out)


class Schneeflocke(threading.Thread):
    # anzahl der schneeflocken die unten angekommen sind
    counter = 0
    lock = threading.Lock()

    def __init__(self, x, height, stime):
        threading.Thread.__init__(self)

        self.x = x
        self.y = rand_int_range(height)
        self.height = height
        self.stime = stime

    def get_xy(self):
        """
        returns x, y position
        :return:
        """
        return (self.x, self.y)

    def run(self):
        """
        tickt bis die Schneeflocke den boden berührt
        :return:
        """
        while self.y < self.height:
            time.sleep(self.stime)
            self.y += rand_int_range(3, -1)
            self.x += rand_int_range(2, -2)
        with Schneeflocke.lock:
            Schneeflocke.counter += 1


if __name__ == "__main__":
    Main(250, 160, 40, 0.07)

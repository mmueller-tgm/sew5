#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import threading
import random
import math

import time



def randIntRange(x,y=0):
    x+=1
    return math.floor(random.randrange(y, x))


class main:
    def __init__(self, amt, width, height, stime):
        self.schneeflocken = []
        self.width = width
        self.height = height
        for i in range(0, amt):
            self.schneeflocken.append(schneeflocke(randIntRange(width), height, stime))

        for o in self.schneeflocken:
            o.start()

        while schneeflocke.counter < amt:
            self.pos = []
            time.sleep(stime)
            for o in self.schneeflocken:
                self.pos.append(o.getxy())
            self.printPos()

        for o in self.schneeflocken:
            o.join()


    def printPos(self):
        out = ""
        for h in range(0, self.height):
            for w in range(0, self.width):
                if (w, h) in self.pos:
                    out += "❄"
                else:
                    out += " "
            out += "\n"
        if os.name == 'posix':
            os.system('clear')
        else:
            os.system('cls')
        print(out)



class schneeflocke(threading.Thread):
    counter = 0
    lock = threading.Lock()
    def __init__(self, x, height, stime):
        threading.Thread.__init__(self)

        self.x = x
        self.y = randIntRange(height)
        self.height = height
        self.stime = stime

    def getxy(self):
        self.finished = False
        return (self.x, self.y)

    def run(self):
        self.finished = False
        while self.y < self.height:
            time.sleep(self.stime)
            self.y += randIntRange(3)
            self.x += randIntRange(2, -2)
            self.finished = True
        with schneeflocke.lock:
            schneeflocke.counter += 1




if __name__ == "__main__":
    main(200, 160, 40, 0.07)

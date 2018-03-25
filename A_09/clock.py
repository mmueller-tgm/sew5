#!/usr/bin/python3
from _datetime import datetime
import threading

import renderStrategy
import pygame, sys
import time


class Clock(threading.Thread):
    def __init__(self):
        super().__init__()
        pygame.init()
        self.time = datetime.time(datetime.now())
        self.events = pygame.event.get()
        self.running = True

        pygame.font.init()

        self.size = {'analog': (1000, 1000), 'digital': (1000, 500)}

        self.canvas = pygame.display.set_mode(self.size['analog'])
        self.strategy = renderStrategy.AnalogRenderStrategy(self.canvas)
        self.update()

    def input(self):
        """
        input() checks if any key has been pressed and updates the strategy
        """
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.canvas = pygame.display.set_mode(self.size['analog'])
                    self.strategy = renderStrategy.AnalogRenderStrategy(self.canvas)
                elif event.key == pygame.K_d:
                    self.canvas = pygame.display.set_mode(self.size['digital'])
                    self.strategy = renderStrategy.DigitalRenderStrategy(self.canvas)
                elif event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_p:
                    if self.strategy.__class__.__name__ == 'AnalogRenderStrategy':
                        self.strategy.switch()
            elif event.type == pygame.QUIT:
                self.running = False

    def update(self):
        """
        updates the model (time)
        :return:
        """
        self.time = datetime.time(datetime.now())

    def handeler(self):
        """
        calls the renderer of the strategy
        :return:
        """
        self.strategy.render(self.time)

    def run(self):
        """
        loops through input(), update() and handler() 30 times per second
        :return:
        """
        while self.running:
            self.input() # check imput
            self.update() # update internal state
            self.handeler() # output
            time.sleep(1 / 30) # sleep for 1 Tick


if __name__ == '__main__':
    clock = Clock()
    clock.start()
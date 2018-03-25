import datetime
from abc import ABC, abstractmethod
import pygame, math


class AbstractRenderStrategy(ABC):
    def __init__(self, canvas):
        """
        initiaizes the clock facae
        :param canvas: the surface to draw on
        """
        ABC.__init__(self)

    @abstractmethod
    def render(self, time):
        """
        Renders the clock face
        :param time: time to display
        """
        pass


class AnalogRenderStrategy(AbstractRenderStrategy):
    def __init__(self, canvas):
        """
        initializes the digital clock strategy
        :param canvas: the surface to draw on
        """
        AbstractRenderStrategy.__init__(self, canvas)
        self.continuous = False  # type: bool
        self.canvas = canvas  # type: pygame.Surface()
        print('analog')

    def switch(self):
        """
        Switches from continious to ticking mode
        :return:
        """
        print('switched')
        if self.continuous:
            self.continuous = False
        else:
            self.continuous = True

    def render(self, time):
        """
        Renders a Analog clock face and displays time
        :param time: type: datetime.time
        :return:
        """
        self.canvas.fill((0, 0, 0))

        pygame.draw.circle(self.canvas, (100, 100, 100),
                           (int(self.canvas.get_width() / 2), int(self.canvas.get_width() / 2)),
                           int(self.canvas.get_height() / 2 - 5), 10)

        # Minutenstriche
        for i in range(0, 60):
            if i % 15 == 0:
                j = 10
            elif i % 5 == 0:
                j = 5
            else:
                j = 2
            x = int(math.sin(2 * math.pi / 60 * i) * (self.canvas.get_height() / 2 - 5) + self.canvas.get_width() / 2)
            y = int(math.cos(2 * math.pi / 60 * i) * (self.canvas.get_height() / 2 - 5) + self.canvas.get_height() / 2)
            pygame.draw.circle(self.canvas, (0, 200, 200), (x, y), j)

        # Sekundenzeiger
        c = (255, 0, 0)
        pl = []
        len = 1

        if not self.continuous:
            x = int(-math.sin(2 * math.pi / 60 * (60 - time.second)) * (
                    self.canvas.get_height() / 2 - 5) * len + self.canvas.get_width() / 2)
            y = int(-math.cos(2 * math.pi / 60 * (60 - time.second)) * (
                    self.canvas.get_height() / 2 - 5) * len + self.canvas.get_width() / 2)

            pl.append((x, y))
            pl.append((int(self.canvas.get_width()) / 2, int(self.canvas.get_width() / 2)))
        else:
            x = int(-math.sin(2 * math.pi / 60 * (60 - time.second - time.microsecond / 1000000)) * (
                    self.canvas.get_height() / 2 - 5) * len + self.canvas.get_width() / 2)
            y = int(-math.cos(2 * math.pi / 60 * (60 - time.second - time.microsecond / 1000000)) * (
                    self.canvas.get_height() / 2 - 5) * len + self.canvas.get_width() / 2)

            pl.append((x, y))
            pl.append((int(self.canvas.get_width()) / 2, int(self.canvas.get_width() / 2)))
        pygame.draw.line(self.canvas, c, pl[0], pl[1])

        # Minutenzeiger
        c = (0, 255, 0)
        pl = []
        len = 0.75

        if not self.continuous:
            x = int(-math.sin(2 * math.pi / 60 * (60 - time.minute)) * (
                    self.canvas.get_height() / 2 - 5) * len + self.canvas.get_width() / 2)
            y = int(-math.cos(2 * math.pi / 60 * (60 - time.minute)) * (
                    self.canvas.get_height() / 2 - 5) * len + self.canvas.get_width() / 2)

            pl.append((x, y))
            pl.append((int(self.canvas.get_width()) / 2, int(self.canvas.get_width() / 2)))
        else:
            x = int(-math.sin(2 * math.pi / 60 * (60 - time.minute - time.second / 60)) * (
                    self.canvas.get_height() / 2 - 5) * len + self.canvas.get_width() / 2)
            y = int(-math.cos(2 * math.pi / 60 * (60 - time.minute - time.second / 60)) * (
                    self.canvas.get_height() / 2 - 5) * len + self.canvas.get_width() / 2)

            pl.append((x, y))
            pl.append((int(self.canvas.get_width()) / 2, int(self.canvas.get_width() / 2)))

        pygame.draw.line(self.canvas, c, pl[0], pl[1], 3)

        # Stundenzeiger
        c = (0, 255, 0)
        pl = []
        len = 0.5

        if not self.continuous:
            x = int(-math.sin(2 * math.pi / 12 * (12 - time.hour)) * (
                    self.canvas.get_height() / 2 - 5) * len + self.canvas.get_width() / 2)
            y = int(-math.cos(2 * math.pi / 12 * (12 - time.hour)) * (
                    self.canvas.get_height() / 2 - 5) * len + self.canvas.get_width() / 2)

            pl.append((x, y))
            pl.append((int(self.canvas.get_width()) / 2, int(self.canvas.get_width() / 2)))
        else:
            x = int(-math.sin(2 * math.pi / 12 * (12 - time.hour - time.minute / 60)) * (
                    self.canvas.get_height() / 2 - 5) * len + self.canvas.get_width() / 2)
            y = int(-math.cos(2 * math.pi / 12 * (12 - time.hour - time.minute / 60)) * (
                    self.canvas.get_height() / 2 - 5) * len + self.canvas.get_width() / 2)

            pl.append((x, y))
            pl.append((int(self.canvas.get_width()) / 2, int(self.canvas.get_width() / 2)))

        pygame.draw.line(self.canvas, c, pl[0], pl[1], 7)

        pygame.draw.circle(self.canvas, (100,100,100), ((int(self.canvas.get_width() / 2), int(self.canvas.get_width() / 2))), 10)

        pygame.display.update()


class DigitalRenderStrategy(AbstractRenderStrategy):
    def __init__(self, canvas):
        """
        initializes the digital clock strategy
        :param canvas: the surface to draw on
        """
        print('digital')
        AbstractRenderStrategy.__init__(self, canvas)
        self.canvas = canvas  # type: pygame.Surface()

        self.font = pygame.font.SysFont('Noto Sans', 100)

    def render(self, time):
        """
        renders a digital clock face
        :param time: time to display
        """
        self.canvas.fill((0, 0, 0))

        pl = []
        margin = 10
        # Outer Rect
        # top left
        x = margin
        y = margin
        pl.append((x, y))
        # top right
        x = self.canvas.get_width() - margin
        y = margin
        pl.append((x, y))
        # bottom right
        x = self.canvas.get_width() - margin
        y = self.canvas.get_height() - margin
        pl.append((x, y))
        # bottom left
        x = margin
        y = self.canvas.get_height() - margin
        pl.append((x, y))

        # Draw the polygons sround the clock
        pygame.draw.polygon(self.canvas, (255, 0, 0), pl, 5)
        pygame.draw.polygon(self.canvas, (100, 100, 100), pl)

        # format time string
        tStr = "%02d:%02d:%02d" % (time.hour, time.minute, time.second)

        text = self.font.render(tStr, True, (0, 0, 0))

        # Put Text in the middle of the surface
        self.canvas.blit(text, (int(self.canvas.get_width()/2 - text.get_width()/2), int(self.canvas.get_height()/2 - text.get_height()/2)))

        pygame.display.update()

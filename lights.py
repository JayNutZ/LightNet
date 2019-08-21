from color import Color
from controller import Controller


class Lights:
    gpio = Controller()
    pins = {'red': 1, 'green': 2, 'blue': 3}
    current_color = Color(0, 0, 0)

    def __init__(self, pins):
        self.pins = pins

    def stop(self):
        self.gpio.kill()

    def colorize(self, color):
        self.current_color = color
        return self.gpio.update(self.pins, self.current_color)

    def get_pins(self):
        return self.pins


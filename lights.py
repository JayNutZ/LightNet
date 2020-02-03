from color import Color
from transition import Transition
from controller import Controller


class Lights:
    transition = Transition()
    gpio = Controller()
    pins = {'red': 1, 'green': 2, 'blue': 3}
    current_color = Color(0, 0, 0)

    def __init__(self, pins):
        self.pins = pins
        self.transition.conf(20, 0.01)
        
    def set_current(self, color):
        self.current_color = color

    def stop(self):
        self.gpio.kill()

    def colorize(self, color):
        self.transition.run(self.current_color, color, self.set_color)
        
    def set_color(self, color):
        self.current_color = color
        return self.gpio.update(self.pins, self.current_color)

    def get_pins(self):
        return self.pins


from color import Color
from gpio import Gpio


class Lights:
    gpio = Gpio()
    on = False
    pins = {'red': 1, 'green': 2, 'blue': 3}
    current_color = Color(0, 0, 0)

    def __init__(self, pin_red, pin_green, pin_blue):
        self.on = False
        self.pins['red'] = pin_red
        self.pins['green'] = pin_green
        self.pins['blue'] = pin_blue

    def stop(self):
        self.gpio.kill()
        return self.on

    def colorize(self, color):
        self.current_color = color
        return self.gpio.update(self.pins, self.current_color)

    def is_active(self):
        return self.on

    def get_pins(self):
        return self.pins


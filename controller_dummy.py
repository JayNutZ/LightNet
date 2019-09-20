from console import Console
from config import Config

class Controller:

    def __init__(self):
        console = Console()
        console.log('INIT')

    def update(self, pins, color):
        self.set_pin(int(pins['red']), self.balance(color.get_red(), 'red'))
        self.set_pin(int(pins['green']), self.balance(color.get_green(), 'green'))
        self.set_pin(int(pins['blue']), self.balance(color.get_blue(), 'blue'))

    def set_pin(self, pin, value):
        console = Console()
        console.log('SET PIN #' + str(pin) + ': ' + str(value))

    def balance(self, value, color):
        config_ctrl = Config()
        conf = config_ctrl.get()

        if color == 'red':
            return int(float(value) * float(conf['balance']['red']))
        elif color == 'green':
            return int(float(value) * float(conf['balance']['green']))
        elif color == 'blue':
            return int(float(value) * float(conf['balance']['blue']))

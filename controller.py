from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import PWMLED
from config import Config
from console import Console


class Controller:
    factory = False
    pwms = {}

    def __init__(self):
        self.factory = PiGPIOFactory()

    def update(self, pins, color):
        self.set_pin(int(pins['red']), self.balance(color.get_red(), 'red'))
        self.set_pin(int(pins['green']), self.balance(color.get_green(), 'green'))
        self.set_pin(int(pins['blue']), self.balance(color.get_blue(), 'blue'))

    def set_pin(self, pin, value):
        console = Console()
        console.log('SET PIN #' + str(pin) + ': ' + str(value))

        if pin in self.pwms:
            self.pwms[pin].value = value
        else:
            self.pwms[pin] = PWMLED(pin, pin_factory=self.factory)
            self.pwms[pin].value = value

    def kill(self):
        for pwm in self.pwms:
            self.pwms[pwm].close()

        self.pwms = {}

    def balance(self, value, color):
        config_ctrl = Config()
        conf = config_ctrl.get()

        value = int(float(value) * float(conf['balance'][color]))

        return self.percentage(value)

    # changed to 0-1
    def percentage(self, value):
        return int(value) / 255

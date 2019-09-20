import RPi.GPIO as GPIO
from config import Config

class Controller:
    pwms = {}

    def __init__(self):
        self.kill()
        GPIO.setmode(GPIO.BCM)

    def update(self, pins, color):
        self.set_pin(int(pins['red']), self.balance(color.get_red(), 'red'))
        self.set_pin(int(pins['green']), self.balance(color.get_green(), 'green'))
        self.set_pin(int(pins['blue']), self.balance(color.get_blue(), 'blue'))

    def set_pin(self, pin, value):
        if pin in self.pwms:
            self.pwms[pin].ChangeDutyCycle(value)
        else:
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(pin, GPIO.OUT)
            self.pwms[pin] = GPIO.PWM(pin, 56)
            self.pwms[pin].start(value)

    def kill(self):
        for pwm in self.pwms:
            self.pwms[pwm].stop()

        self.pwms = {}
        GPIO.cleanup()

    def balance(self, value, color):
        config_ctrl = Config()
        conf = config_ctrl.get()

        value = self.percentage(value)

        if color == 'red':
            return value * float(conf['balance']['red'])
        elif color == 'green':
            return value * float(conf['balance']['green'])
        elif color == 'blue':
            return value * float(conf['balance']['blue'])

    def percentage(self, value):
        return round(int(value) / 2.55)

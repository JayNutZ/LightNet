import RPi.GPIO as GPIO
from config import Config
from console import Console

class Controller:
    frequency = 48;
    pwms = {}

    def __init__(self):
        GPIO.setmode(GPIO.BCM)

    def update(self, pins, color):
        self.set_pin(int(pins['red']), self.balance(color.get_red(), 'red'))
        self.set_pin(int(pins['green']), self.balance(color.get_green(), 'green'))
        self.set_pin(int(pins['blue']), self.balance(color.get_blue(), 'blue'))

    def set_pin(self, pin, value):
        console = Console()
        console.log('SET PIN #' + str(pin) + ': ' + str(value))
        
        if pin in self.pwms:
            self.pwms[pin].ChangeDutyCycle(value)
        else:
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(pin, GPIO.OUT)
            self.pwms[pin] = GPIO.PWM(pin, self.frequency)
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
            return int(float(value) * float(conf['balance']['red']))
        elif color == 'green':
            return int(float(value) * float(conf['balance']['green']))
        elif color == 'blue':
            return int(float(value) * float(conf['balance']['blue']))

    def percentage(self, value):
        return round(int(value) / 2.55)


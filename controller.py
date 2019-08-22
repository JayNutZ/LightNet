import RPi.GPIO as GPIO
from console import Console
import json


class Controller:
    pwms = {}

    def __init__(self):
        self.kill()
        GPIO.setmode(GPIO.BCM)

    def update(self, pins, color):
        self.set_pin(int(pins['red']), color.get_red())
        self.set_pin(int(pins['green']), color.get_green())
        self.set_pin(int(pins['blue']), color.get_blue())
        c = Console()
        c.log(json.dumps(self.pwms))

    def set_pin(self, pin, value):
        if pin in self.pwms:
            self.pwms[pin].ChangeDutyCycle(self.percentage(value))
        else:
            GPIO.setup(pin, GPIO.OUT)
            self.pwms[pin] = GPIO.PWM(pin, 80)
            self.pwms[pin].start(self.percentage(value))

    def kill(self):
        GPIO.cleanup()

    def percentage(self, value):
        return round(int(value) / 2.55)

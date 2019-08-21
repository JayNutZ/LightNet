import RPi.GPIO as GPIO
from console import Console
import sys

class Controller:
    
    def __init__(self):
        GPIO.setmode(GPIO.BCM)

    def update(self, pins, color):
        self.set_pin(int(pins['red']), color.get_red())
        self.set_pin(int(pins['green']), color.get_green())
        self.set_pin(int(pins['blue']), color.get_blue())

    def set_pin(self, pin, value):
        c = Console()
        c.log('P' + str(pin) + '=' + str(value))
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)
        p = GPIO.PWM(pin, 80)
        p.start(self.percentage(value))
        
    def kill(self):
        GPIO.cleanup()
        
    def percentage(self, value):
        return round(int(value) / 2.55)


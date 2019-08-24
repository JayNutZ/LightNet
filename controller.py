import RPi.GPIO as GPIO
from console import Console


class Controller:
    pwms = {}

    def __init__(self):
        self.kill()
        GPIO.setmode(GPIO.BCM)

    def update(self, pins, color):
        self.set_pin(int(pins['red']), color.get_red())
        self.set_pin(int(pins['green']), color.get_green())
        self.set_pin(int(pins['blue']), color.get_blue())

    def set_pin(self, pin, value):
        if pin in self.pwms:
            self.pwms[pin].ChangeDutyCycle(self.percentage(value))
        else:
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(pin, GPIO.OUT)
            self.pwms[pin] = GPIO.PWM(pin, 56)
            self.pwms[pin].start(self.percentage(value))

    def kill(self):
        for pwm in self.pwms:
            self.pwms[pwm].stop()

        self.pwms = {}
        GPIO.cleanup()

    def percentage(self, value):
        return round(int(value) / 2.55)

from flask import jsonify

class Gpio:
    def __init__(self):
        lool = ""

    def update(self, pins, color):
        self.set_pin(pins['red'], color.get_red())
        self.set_pin(pins['green'], color.get_green())
        self.set_pin(pins['blue'], color.get_blue())

    def set_pin(self, pin, value):
        print jsonify({'pin': pin, 'value': value})
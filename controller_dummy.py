from console import Console


class Controller:

    def __init__(self):
        console = Console()
        console.log('INIT')

    def update(self, pins, color):
        self.set_pin(int(pins['red']), color.get_red())
        self.set_pin(int(pins['green']), color.get_green())
        self.set_pin(int(pins['blue']), color.get_blue())

    def set_pin(self, pin, value):
        console = Console()
        console.log('SET PIN #' + str(pin) + ': ' + str(value))

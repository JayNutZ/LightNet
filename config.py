import json


class Config:
    filename = 'config.json'
    config = {
        "pins": {
            "red": 1,
            "green": 2,
            "blue": 3
        },
        "color": {
            "red": 0,
            "green": 0,
            "blue": 0
        },
        "balance": {
            "red": 0,
            "green": 0,
            "blue": 0
        },
        "active": False
    }

    def __init__(self):
        try:
            self.load()
        except IOError:
            self.update()
            self.load()

    def load(self):
        with open(self.filename) as config_file:
            self.config = json.load(config_file)

    def get(self):
        return self.config
    
    def set_pins(self, red, green, blue):
        self.config['pins']['red'] = red
        self.config['pins']['green'] = green
        self.config['pins']['blue'] = blue
        self.update()

    def set_color(self, color):
        self.config['color']['red'] = color.get_red()
        self.config['color']['green'] = color.get_green()
        self.config['color']['blue'] = color.get_blue()
        self.update()

    def set_balance(self, red, green, blue):
        self.config['balance']['red'] = red
        self.config['balance']['green'] = green
        self.config['balance']['blue'] = blue
        self.update()

    def set_active(self, active):
        self.config['active'] = active
        self.update()

    def update(self):
        with open(self.filename, 'w+') as config_file:
            json.dump(self.config, config_file)
        self.load()

    def create(self):
        return self.update()


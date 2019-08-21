import json


class Config:
    filename = 'config.json'
    config = {}

    def __init__(self):
        try:
            self.load()
        except IOError:
            self.create()
            self.load()

    def load(self):
        with open(self.filename) as config_file:
            self.config = json.load(config_file)

    def get(self):
        return self.config

    def update(self, new):
        with open(self.filename, 'w+') as config_file:
            json.dump(new, config_file)

    def create(self):
        return self.update({
            "pins": {
                "red": 1,
                "green": 2,
                "blue": 3
            }
        })


# ,
#            "color": {
#                "red": 0,
#                "green": 0,
#                "blue": 0
#            }

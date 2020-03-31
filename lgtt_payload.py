import json

from lights import Lights
from color import Color
from config import Config


class LgttPayload:
    payload = {
        "state": "OFF",
        "brightness": None,
        "color": None,
        "transition": 2
    }

    def __init__(self, payload):
        payload = json.loads(payload)

        self.payload = {
            "state": payload['state'],
            "brightness": payload['brightness'] if 'brightness' in payload else None,
            "color": payload['color'] if 'color' in payload else None,
            "transition": payload['transition'] if 'transition' in payload else 2,
        }

        self.apply()

    def stop(self, lights, config):
        lights.stop()
        config.set_color(Color(0, 0, 0))
        config.set_active(False)

        self.payload = {
            "state": "OFF",
            "brightness": None,
            "color": None,
            "transition": 2
        }

    def apply(self):
        print("LGTT SET: " + json.dumps(self.payload))

        config = Config()
        current = config.get()

        lights = self.get_lights(current)
        lights.set_current(config.get_color())

        self.apply_transition(lights)

        if self.is_active():
            self.apply_color(lights, config)

        else:
            self.stop(lights, config)

    def apply_color(self, lights, config):
        if self.payload['color'] != None:
            color = self.get_color()
        elif self.payload['brightness'] != None:
            color = self.color_from_brightness(self.payload['brightness'])
        else:
            color = self.color_from_brightness(255)
        
        config.set_color(color)
        config.set_active(True)

        lights.colorize(color)

    def apply_transition(self, lights):
        if 'transition' in self.payload:
            lights.set_transition(self.payload['transition'])

    def get_color(self):
        return Color(self.payload['color']['r'], self.payload['color']['g'], self.payload['color']['b'])

    def is_active(self):
        return self.payload['state'] == 'ON'

    def get_lights(self, config):
        return Lights(config['pins'])

    def color_from_brightness(self, brightness):
        return Color(brightness, self.calc_green(brightness), self.calc_blue(brightness))

    def calc_green(self, red):
        return red * 0.7
    
    def calc_blue(self, blue):
        return blue * 0.05

    def get(self):
        return self.payload

    def json_string(self):
        output = self.payload.copy()
        
        if output['color'] == None:
            del output['color']
        if output['brightness'] == None:
            del output['brightness']

        return json.dumps(output)

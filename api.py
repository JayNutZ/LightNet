from flask import Flask, jsonify, request
from flask_restful import Resource, Api

from lights import Lights
from color import Color
from config import Config

app = Flask(__name__)
api = Api(app)

@app.route('/api/set')
def colorize():
    config = Config()
    current = config.get()

    lights = get_lights(current)

    color = Color(request.args.get('r'), request.args.get('g'), request.args.get('b'))
    
    lights.colorize(color)

    return color.to_string()


@app.route('/api/stop')
def stop():
    config = Config()
    lights = get_lights(config.get())
    running = lights.stop()

    return jsonify({'running': running})


@app.route('/api/conf')
def set_pins():
    config = Config()
    current = config.get()

    current['pins']['red'] = request.args.get('r')
    current['pins']['green'] = request.args.get('g')
    current['pins']['blue'] = request.args.get('b')

    config.update(current)

    return jsonify(config.get())

def summary():
    out = config.get()
    
    return out

def get_lights(config):
    return Lights(config['pins']['red'], config['pins']['blue'], config['pins']['green'])


if __name__ == '__main__':
    app.run(debug=True)

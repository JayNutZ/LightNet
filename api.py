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
    
    config.set_color(color)
    config.set_active(True)
    
    lights.colorize(color)

    return jsonify(config.get())

@app.route('/api/stop')
def stop():
    config = Config()
    
    config.set_active(False)
    
    lights = get_lights(config.get())
    lights.stop()
    
    return jsonify(config.get())

@app.route('/api/conf')
def set_pins():
    config = Config()
    
    config.set_pins(request.args.get('r'), request.args.get('g'), request.args.get('b'))

    return jsonify(config.get())

def get_lights(config):
    return Lights(config['pins'])


if __name__ == '__main__':
    app.run(debug=True)

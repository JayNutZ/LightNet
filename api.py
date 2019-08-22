from flask import Flask, jsonify, request, render_template
from flask_restful import Resource, Api

from lights import Lights
from color import Color
from config import Config

app = Flask(__name__)
api = Api(app)

@app.route('/')
def screen():
    return render_template('app.html')

@app.route('/api/set')
def colorize():
    config = Config()
    current = config.get()

    lights = get_lights(current)

    color = Color(request.args.get('r'), request.args.get('g'), request.args.get('b'))
    
    config.set_color(color)
    config.set_active(True)
    
    lights.colorize(color)

    return api_request(jsonify(config.get()))

@app.route('/api/stop')
def stop():
    config = Config()
    
    config.set_active(False)
    
    lights = get_lights(config.get())
    lights.stop()
    
    return api_request(jsonify(config.get()))

@app.route('/api/conf')
def set_pins():
    config = Config()
    
    config.set_pins(request.args.get('r'), request.args.get('g'), request.args.get('b'))

    return api_request(jsonify(config.get()))


def api_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    response.headers.add('Content-Type', 'application/json')
    return response


def get_lights(config):
    return Lights(config['pins'])


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='80')

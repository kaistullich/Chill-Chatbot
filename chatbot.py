import json
import os
import re

import pyowm
from flask import Flask, render_template, jsonify, request
from rivescript import RiveScript

app = Flask(__name__)

# initialize RiveScript stuff
bot = RiveScript()
bot.load_directory(os.path.join(os.getcwd(), 'brain'))
bot.sort_replies()

# holds API KEY for OpenWeatherMap
with open(os.path.join(os.getcwd(), 'config.json')) as f:
    config = json.load(f)
# initialize OpenWeatherMap
weather = pyowm.OWM(config['API_KEY'])


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/reply', methods=['POST'])
def reply():
    msg = request.json['userMsg']
    regex = re.compile(r'weather')

    # TODO: continue integrating weather stuff
    observation = weather.weather_at_place('San Jose, ca')
    w = observation.get_weather()
    print(w.get_temperature('fahrenheit'))

    if regex.search(msg):
        print()
    else:
        botreply = bot.reply('localuser', msg)
        return jsonify({"reply": botreply})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)

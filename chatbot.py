import os
import re

from flask import Flask, render_template, jsonify, request
from rivescript import RiveScript

from get_weather import Weather

app = Flask(__name__)

# initialize RiveScript stuff
bot = RiveScript()
bot.load_directory(os.path.join(os.getcwd(), 'brain'))
bot.sort_replies()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/reply', methods=['POST'])
def reply():
    # capture what the user said
    user_msg = request.json['userMsg']
    # check if "weather" and "in" are in inside the user input
    weather_regex = re.compile(r'^(?=.*weather)(?=.*in)')

    # TODO: continue integrating weather stuff
    if weather_regex.search(user_msg):
        print('weather and in, inside of string')
        # get all the characters after "in" and remove whitespace
        get_city = user_msg[user_msg.find('in') + 2:].strip()
        w = Weather()
        w.get_woeid(get_city)
        weather_data = w.get_weather()
        return jsonify({"weather_data": weather_data})
    else:
        botreply = bot.reply('localuser', user_msg)
        return jsonify({"reply": botreply})

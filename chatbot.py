import os
import re
import logging
from logging import FileHandler, Formatter

from flask import Flask, render_template, jsonify, request
from rivescript import RiveScript

from get_weather import Weather

app = Flask(__name__)

# initialize RiveScript stuff
bot = RiveScript()
bot.load_directory(os.path.join(os.getcwd(), 'brain'))
bot.sort_replies()

# setup log file
file_handler = FileHandler('error_log.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(
    Formatter('%(asctime)s,%(msecs)d %(levelname)-5s [%(filename)s:%(lineno)d] %(message)s',
              datefmt='%d-%m-%Y:%H:%M:%S'
              )
)
app.logger.addHandler(file_handler)


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
        # get all the characters after "in" and remove whitespace
        get_city = user_msg[user_msg.find('in') + 2:].strip()
        w = Weather()
        w.get_woeid(get_city)
        weather_data = w.get_weather()
        five_day = w.get_5day_forecast()

        return jsonify({"weather_data": weather_data, 'five_day': five_day})
    else:
        botreply = bot.reply('localuser', user_msg)

        return jsonify({"reply": botreply})

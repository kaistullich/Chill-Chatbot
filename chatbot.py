import os
import re

from flask import Flask, render_template, jsonify, request
from rivescript import RiveScript

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
    msg = request.json['userMsg']
    regex = re.compile(r'weather')

    # TODO: continue integrating weather stuff
    if regex.search(msg):
        print()
    else:
        botreply = bot.reply('localuser', msg)
        return jsonify({"reply": botreply})

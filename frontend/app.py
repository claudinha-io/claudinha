from flask import Flask
from flask import request
from claudinha_text.ascii_text import *
from time import strftime

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/message', methods=['GET'])
def default_message():
    input_text = strftime('Hora: %H:%M:%S')
    text = step(message(input_text))
    show_display(text, 'blue')
    return input_text

@app.route('/message/<string:input_text>/', methods=['GET'])
def input_message(input_text):
    text = step(message(input_text))
    show_display(text, request.args.get('color', 'blue'))
    return input_text
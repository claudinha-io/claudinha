from flask import Flask
from ascii_text import *
from time import strftime

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/message')
def default_message():
    input_text = strftime("%H:%M:%S")
    text = step(message(input_text))
    show_display(text, 'blue')
    return input_text

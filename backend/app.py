from flask import Flask
from flask import request, jsonify
from flask import render_template
from claudinha_text.ascii_text import *
from time import strftime

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/message', methods=['GET'])
def default_message():
    input_text = strftime('Hora: %H:%M:%S')
    text = step(message(input_text))
    show_display(text, 'white')
    return jsonify(
        {
            "msg": input_text
        }
    )


@app.route('/message/<string:input_text>/', methods=['PUT'])
def input_message(input_text):
    text = step(message(input_text))
    show_display(text, request.args.get('color', 'white'))
    return jsonify(
        {
            "msg": input_text
        }
    )


if __name__ == '__main__':
    app.run(debug=True)

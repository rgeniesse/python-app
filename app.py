import json
from flask import Flask
import psycopg2
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Docker my old friend!'


@app.route('/widgets')
def hello_world_widgets():
    return 'Hello, Widgets my old friend!'


@app.route('/initdb')
def hello_world_initdb():
    return 'Hello, initdb my old friend!'


if __name__ == "__main__":
    app.run(host='0.0.0.0')

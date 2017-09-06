from flask import Flask
from .autoload import Autoload

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

import flask
from flask import request
import pandas as pd
from datetime import datetime as dt

app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return 'string'
    

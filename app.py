import flask
from flask import request
import pandas as pd
from datetime import datetime as dt
import json 

app = flask.Flask(__name__)


@app.route('/', methods=['POST'])
def home():
    res = request.json


    return json.dumps(dict('key': res['distances'])) 
    

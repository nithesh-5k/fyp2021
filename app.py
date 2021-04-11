import flask
from flask import request
from datetime import datetime as dt
import json

app = flask.Flask(__name__)


@app.route('/', methods=['POST'])
def home():
    res = request.json


    return json.dumps(res['distances'])) 
    

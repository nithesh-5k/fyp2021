import flask
from flask import request
from datetime import datetime as dt

app = flask.Flask(__name__)


@app.route('/', methods=['POST'])
def home():
    res = request.json


    return json.dumps(dict('key': res['distances'])) 
    

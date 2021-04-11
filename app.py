import flask
from flask import request
from datetime import datetime as dt
import json
import pandas as pd

app = flask.Flask(__name__)


@app.route('/', methods=['POST'])
def home():
    res = request.json
    data=pd.DataFrame(res['distances'][0])

    return {'data': data}
    

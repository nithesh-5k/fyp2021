import flask
from flask import request
from datetime import datetime as dt
import json
import pandas as pd

app = flask.Flask(__name__)


@app.route('/', methods=['POST'])
def home():
    data = request.json
    df_distances=pd.DataFrame(data['distances'])
    df_heartbeats=pd.DataFrame(data['heartbeats'])

    return str(df_distances['time'].values[0])
    

if __name__ == "__main__":
    app.run(debug=True)
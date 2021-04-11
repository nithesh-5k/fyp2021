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
    g={}
    g['0']=df_distances['time'].values[0]
    return  json.dumps(g)
    

# if __name__ == "__main__":
#     app.run(debug=True)
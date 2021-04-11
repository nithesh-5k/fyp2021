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
    g['0']=df_distances
    g1['0']=df_heartbeats
    return  json.dumps(g),json.dumps(g1)
    

# if __name__ == "__main__":
#     app.run(debug=True)
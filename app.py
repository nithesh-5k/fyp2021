import flask
from flask import request

app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return 'res'





# @app.route('/', methods=['GET'])
# def home():
    # res = request.json
    
    # print(res)
    # print(res.json())
    # return 'res'

# if __name__ == "__main__":
#     app.run(debug=True)




#Web server. Runs the prediciton.

from flask import Flask
app = Flask(__name__)

from run_model import load_run_model
from flask import request

@app.route("/predict", methods = ['POST'])
def run_model_post():
    #print(request.data)
    submitted_data = request.json
    print(submitted_data ['data'])
    return {
        "Result":load_run_model(submitted_data['data']).tolist()
    }

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

import getpass

@app.route("/api")
def me_api():
    username = getpass.getuser()
    return {
        "greeting":"Kenny is awesome",
        "username":username
    }


    

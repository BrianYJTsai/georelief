import os
from flask import Flask, request
from flask.ext import restful
from flask.ext.pymongo import PyMongo
from flask import make_response
from bson.json_util import dumps

#MONGO_URL = os.environ.get('MONGO_URL')
#if not MONGO_URL:
#    MONGO_URL = "mongodb://localhost:27017/rest";

app = Flask(__name__)

#app.config['MONGO_URI'] = MONGO_URL
#mongo = PyMongo(app)
'''
def output_json(obj, code, headers=None):
    resp = make_response(dumps(obj), code)
    resp.headers.extend(headers or {})
    return resp

DEFAULT_REPRESENTATIONS = {'application/json': output_json}
api = restful.Api(app)
api.representations = DEFAULT_REPRESENTATIONS
s
import flask_rest_service.resources
'''

@app.route('/')
def hello():
	#app = Flask(__name__,static_url_path='')
	#@app.route(./)
    input = open("tweetOutput.txt", "r")
    text = []
    for line in input:
        text.append(str(line))
        print(str(line))
    text = '\n'.join(text)
    input.close()
    return text

if __name__ == '__main__':
	app.run(debug=True)

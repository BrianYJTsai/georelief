import os
from flask import Flask, request
from flask.ext import restful
from flask.ext.pymongo import PyMongo
from flask import make_response
from bson.json_util import dumps

import tweepy
import json

# Twitter API credentials
consumer_key = "ToMJ36rxxLbdi6phSXYEM8Qd0"
consumer_secret = "eMxSeofGj6uK7nyc0uetEJRFNNtlzxyx6k11tXhrYY33Illjeq"
access_key = "924361173214089217-bEHCdGreBj6ndEutzV9nkIFAwLQH9uw"
access_secret = "pjIyb8Kqpr6dv8yaudMYloNtrLtSfr0TCC30asAOSAlq7"


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

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)


    alltweets = [status._json for status in tweepy.Cursor(api.search, q="#georelief", geocode="30.303092,-97.6648322,500mi", lang="en").items(limit = 100)]
    print("Writing tweet objects to JSON please wait...")
    count = 0
    tweets = []
    new_tweet = ""
    for tweet in alltweets:
        count +=1
        print("Tweets downloaded so far: ", count)
        #json.dump(status._json, file, sort_keys=True, indent=4)
        #tweet = json.dumps(status._json)
        #new_tweet = [tweet['user']['name'], tweet['geo']['coordinates'], tweet['text']]
        #new_tweet.append(tweet['user']['name'])
        try:
            #new_tweet.append(tweet['geo']['coordinates'])
            test = tweet['geo']['coordinates'][0]
            new_tweet+=tweet['user']['name'] + "%"
            new_tweet+=str("@" + tweet['user']['screen_name'])
            new_tweet+="%"
            new_tweet+=str(tweet['text'])
            new_tweet+="%"
            new_tweet+=str(tweet['geo']['coordinates'][0])
            new_tweet+="%"
            new_tweet+=str(tweet['geo']['coordinates'][1])
            new_tweet+="%"
        except:
            pass
            #new_tweet.append(["None", "None"])
        #new_tweet.append(tweet['geo']['coordinates'])
        #new_tweet.append(tweet['text'])
        #new_tweet+="<br>"
        #new_tweet.append("THIS IS A TEST")
        #tweets.append(new_tweet)


    #close the file
    #print("Done")

    #input = open("tweetOutput.txt", "r")
    #text = []
    #for line in input:
    #    text.append(str(line))
    #    print(str(line))
    #text = '\n'.join(text)
    #input.close()
    #return text
    #tweets = [[tweets[line:line + 3]] for line in range(0, len(tweets), 3)]
    #return '<br>'.join(str(line) for line in tweets)
    #return str(tweets)
    return new_tweet
if __name__ == '__main__':
	app.run(debug=True)

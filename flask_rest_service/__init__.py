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
	#app = Flask(__name__,static_url_path='')
	#@app.route(./)

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    # initialize a list to hold all the tweepy Tweets
    #alltweets = []

    # make initial request for most recent tweets (200 is the maximum allowed count)
    #new_tweets = api.user_timeline(screen_name=screen_name, count=10)

    # save most recent tweets
    #alltweets.extend(new_tweets)

    # save the id of the oldest tweet less one
    #oldest = alltweets[-1].id - 1
    '''
    # keep grabbing tweets until there are no tweets left to grab
    while (len(alltweets) < 100):
        # all subsequent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name=screen_name, count=10, max_id=oldest)

        # save most recent tweets
        alltweets.extend(new_tweets)

        # update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        print("...%s tweets downloaded so far" % (len(alltweets)))
    '''

    alltweets = [status._json for status in tweepy.Cursor(api.search, q="#georelief", geocode="30.303092,-97.6648322,500mi", lang="en").items(limit = 100)]

    # write tweet objects to JSON
    #file = open("tweet.json", "w", encoding="utf8")
    print("Writing tweet objects to JSON please wait...")
    count = 0
    tweets = []
    for tweet in alltweets:
        count +=1
        print("Tweets downloaded so far: ", count)
        #json.dump(status._json, file, sort_keys=True, indent=4)
        #tweet = json.dumps(status._json)
        #new_tweet = [tweet['user']['name'], tweet['geo']['coordinates'], tweet['text']]
        new_tweet = []
        new_tweet.append(tweet['user']['name'])
        try:
            new_tweet.append(tweet['geo']['coordinates'])
        except:
            new_tweet.append(["None", "None"])
        #new_tweet.append(tweet['geo']['coordinates'])
        new_tweet.append(tweet['text'])
        tweets.append(new_tweet)


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

    return str(tweets)

if __name__ == '__main__':
	app.run(debug=True)

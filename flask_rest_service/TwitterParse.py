import tweepy
import json

# Twitter API credentials
consumer_key = "ToMJ36rxxLbdi6phSXYEM8Qd0"
consumer_secret = "eMxSeofGj6uK7nyc0uetEJRFNNtlzxyx6k11tXhrYY33Illjeq"
access_key = "924361173214089217-bEHCdGreBj6ndEutzV9nkIFAwLQH9uw"
access_secret = "pjIyb8Kqpr6dv8yaudMYloNtrLtSfr0TCC30asAOSAlq7"


def get_all_tweets():
    # Twitter only allows access to a users most recent 3240 tweets with this method

    # authorize twitter, initialize tweepy
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
    file = open("tweetOutput.txt", "w", encoding="utf8")
    print("Writing tweet objects to JSON please wait...")
    count = 0
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
        file.write(str(new_tweet))
        file.write("\n")

    # close the file
    print("Done")
    file.close()


def parse_all_tweets():

    output = open("tweetOutput.txt", "w", encoding="utf8")

    with open('tweet.json') as json_data:
        new_tweet = json.load(json_data)
        tweet = [new_tweet['user']['name'], new_tweet['geo']['coordinates'], new_tweet['text']]
        output.write(str(tweet))

    output.close()

if __name__ == '__main__':
    # pass in the username of the account you want to download
    get_all_tweets()
    #parse_all_tweets()
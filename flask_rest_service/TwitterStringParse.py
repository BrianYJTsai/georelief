import tweepy
import json



def parse_all_tweets():

    output = open("tweetOutput.txt", "w")

    all_tweets = []
    with open('tweet.json') as json_data:
        new_tweet = json.load(json_data)
        tweet = [new_tweet['user']['name'], new_tweet['geo']['coordinates'], new_tweet['text']]
        output.write(str(tweet))
        output.write("\n")

    output.close()




if __name__ == '__main__':
    # pass in the username of the account you want to download
    parse_all_tweets()
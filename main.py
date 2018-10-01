import tweepy
from time import sleep
import json
import creds

consumer_key = creds.consumer_key
consumer_secret = creds.consumer_secret
access_token = creds.access_token
access_token_secret = creds.access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def main():
    i = 0
    def tweet_loop(i):
        tweet = ("@edgyontheledgy will you go to homecoming with @gdogpwns? Reply the word YES to make me stop! This is tweet #" + str(i) + ".")
        i += 1
        api.update_status(tweet)
        sleep(600)
    def mention_loop():
        mentions_list = api.mentions_timeline()
        try:
            status = mentions_list[0]
            json_str = json.dumps(status._json)
        except:
            sleep(10)
            mention_loop()
        text = json.loads(json_str)['text']
        print(text)
        if text == ("@MeganAtHoco YES"):
            tweet = "HOORAY! I CAN GO BACK INTO MY ETERNAL SLUMBER NOW. REALITY IS A SIMULATION. LIFE IS A LIE."
            api.update_status(tweet)
            exit()
        sleep(60)
        mention_loop()
    mention_loop()
    tweet_loop(i)


main()

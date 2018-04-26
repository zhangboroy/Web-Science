import tweepy
import time

#Variables that contains the user credentials to access Twitter API
access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""

#This handles Twitter authetification and the connection to Twitter Streaming API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

users = tweepy.Cursor(api.friends, screen_name='phonedude_mln').items()

f = open("twitterFollowing.csv", "w", encoding='utf-8')
f.write('label\tfriends\n')

#Print the following# of every following into the file 1 by 1
index = 1
while True:
    try:
        user = next(users)
    except tweepy.TweepError:
        time.sleep(60*15)
        user = next(users)
    except StopIteration:
        break
    f.write('f{}'.format(index) + '\t{}'.format(user.friends_count) + '\n')
    index = index + 1

f.write('me\t{}'.format(index-1)+'\n')
f.close()

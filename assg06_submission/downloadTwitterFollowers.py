import tweepy
import time

#Variables that contains the user credentials to access Twitter API
access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""

#This handles Twitter authetification
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

users = tweepy.Cursor(api.followers, screen_name='phonedude_mln').items()

f = open("twitterFollowers.csv", "w", encoding='utf-8')

#Print the follower# of every follower into the file 1 by 1
index = 1
while True:
    try:
        user = next(users)
        f.write(user.screen_name + '\n')
        f.write(user.name + '\n')
        f.write('{}'.format(user.followers_count) + '\n')
        index = index + 1
    except tweepy.TweepError:
        time.sleep(60)
    except StopIteration:
        break

f.write('phonedude_mln\n')
f.write('Michael L. Nelson\n')
f.write('{}'.format(index-1)+'\n')
f.close()

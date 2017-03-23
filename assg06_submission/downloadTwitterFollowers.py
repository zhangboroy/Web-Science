import tweepy
import time

#Variables that contains the user credentials to access Twitter API
access_token = "825062339653271552-q2y3e35bUt1pKxdbqZ9leWIcgIT1mvt"
access_token_secret = "GIyuMRZB2xoIFVVJzJBRCt3kFWZCJh36rHY1T125GcVN0"
consumer_key = "EVKHzzDy0B3mtbvN426yrEZOM"
consumer_secret = "jAydpzL5jYnQGcUkxuwG1DeYGYgF6hu3zzlH9Vx1sG0iHbPKPT"

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

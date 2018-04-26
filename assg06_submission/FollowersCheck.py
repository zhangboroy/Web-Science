import tweepy
import time
from gender_detector import gender_detector
detector = gender_detector.GenderDetector('us')

f = open("twitterFollowers.csv", "r", encoding='utf-8')
lines = f.readlines()
f.close()

usernames=[]
names=[]
firstNames=[]
followerNumbers=[]
for i in range(int(len(lines)/3)):
    usernames.append(lines[i*3].strip())
    names.append(lines[i*3+1].strip())
    firstNames.append(names[i].split()[0])
    followerNumbers.append(lines[i*3+2].strip())

genders=[]
for firstName in firstNames:
    try:
        genders.append(detector.guess(firstName))
    except:
        genders.append('unknown')

usernamesCheck=[]
count = 0
for i in range(len(genders)):
    if genders[i]!='unknown' and count<100:
        usernamesCheck.append(1)
        count = count + 1
    else:
        usernamesCheck.append(0)

usernamesCheck[len(genders)-1]=1

f = open("graph.csv", "w", encoding='utf-8')
f.write('nodes:\n')
for i in range(len(usernames)):
    f.write(usernames[i]+'\n'+genders[i]+'\n{}'.format(usernamesCheck[i])+'\n')
f.write('edges:\n')
f.close()

#Variables that contains the user credentials to access Twitter API
access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""

#This handles Twitter authetification
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

friendships=[]
for i in range(len(usernames)-2):
    if usernamesCheck[i]==1:
        for j in range(i+1,len(usernames)-1):
            if usernamesCheck[j]==1:
                print ('{}'.format(i)+'\t{}'.format(j))
                while True:
                    try:
                        friendship = api.show_friendship(source_screen_name=usernames[i],target_screen_name=usernames[j])
                        if friendship[0].following==True or friendship[0].followed_by==True or friendship[1].following==True or friendship[1].followed_by==True:
                            f = open("graph.csv", "a", encoding='utf-8')
                            f.write('{}'.format(i)+'\n{}'.format(j)+'\n')
                            f.close()
                        break
                    except Exception as err:
                        print (err)
                        if str(err)=='Not authorized.':
                            break
                        else:
                            time.sleep(60)

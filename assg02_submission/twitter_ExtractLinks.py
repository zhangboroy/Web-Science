import json
import re
import urllib.request

#This function extracts links from given string
def extract_link(text):
    regex = r'https?://[^\s<>"]+|www\.[^\s<>"]+'
    match = re.search(regex, text)
    if match:
        return match.group()
    return ''

#Set the JSON format file
tweets_data_path = 'output.txt'

#Set a list to hold the texts of tweets
tweets_data = []

#Open the JSON format file and get the texts of tweets
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet['text'])
    except:
        continue

tweets_file.close()

#Set a list to hold the links in the texts of tweets
tweets_links = []

#Extract the links from the texts of tweets, open them and get the URIs from the responses
for line in tweets_data:
    try:
        link = extract_link(line)
        if (link!=''):
            response = urllib.request.urlopen(link)
            tweets_links.append(response.geturl())
    except:
        continue

#Remove the duplicated links
tweets_LinksRemoveDuplication = list(set(tweets_links))

#Set a list to hold the "real" URIs
tweets_LinksForUse =[]

#Remove the "unreal" URIs and spam URIs
#by deleting URIs linking to twitter and URIs less than 50 bytes(short URIs tend to be spam)
for line in tweets_LinksRemoveDuplication:
    if re.search('https://twitter.com/', line) or len(line)<50:
        continue
    else:
        tweets_LinksForUse.append(line)

#Save the links to a file
f = open("links.txt", 'w')
for link in tweets_LinksForUse:
    line = f.write(link+'\n')

f.close()


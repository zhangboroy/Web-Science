import feedparser
import re

# Returns title and dictionary of word counts for an RSS feed
def getwordcounts(url):
    # Parse the feed
    d=feedparser.parse(url)
    print (d.feed.title)
    feed=[]

    # Loop over all the entries
    for e in d.entries:
        print (e.title)

        wc={}
        summary=''
        if 'content' in e:
            for content in e.content:
                print (content)
                print ()
                summary=summary+content.value+' '
        elif 'summary' in e and e.summary!='':
            print (e.summary)
            print ()
            summary=summary+e.summary+' '
        elif 'description' in e and e.description!='':
            print (e.description)
            print ()
            summary=summary+e.description+' '
        else:
            print ('error!!!!!!!!!!!!!!')
            print ()
        
        # Extract a list of words
        words=getwords(e.title+' '+summary)
        for word in words:
            wc.setdefault(word,0)
            wc[word]+=1

        feed.append([e.title,wc])
    return feed

def getwords(html):
    # Remove all the HTML tags
    txt=re.compile(r'<[^>]+>').sub('',html)

    # Split words by all non-alpha characters
    words=re.compile(r'[^A-Z^a-z]+').split(txt)

    # Convert to lowercase
    return [word.lower( ) for word in words if word!='']

apcount={}
wordcounts={}
feedlist=[line.strip() for line in open('feedlist.txt','r')]
for feedurl in feedlist:
    print (feedurl)
    for feed in getwordcounts(feedurl):
        wordcounts[feed[0]]=feed[1]
        
        for word,count in feed[1].items():
            apcount.setdefault(word,0)
            if count>1:
                apcount[word]+=1
        
wordlist=[]
for w,bc in apcount.items( ):
    wordlist.append([bc,w])

wordlist.sort(reverse=True)

f=open('entries.txt','r',encoding='utf-8')
lines=f.readlines()
f.close()
entries=[]
for i in range(1,len(lines)):
    entries.append(lines[i].strip().split('\t')[0])

out=open('feeddata.txt','a',encoding='utf-8')
out.write('Title')
for i in range(min(len(wordlist),1000)): out.write('\t%s' % wordlist[i][1])
out.write('\n')
for blog,wc in wordcounts.items( ):
    if blog in entries:
        out.write(blog)
        for i in range(min(len(wordlist),1000)):
            if wordlist[i][1] in wc: out.write('\t%d' % wc[wordlist[i][1]])
            else: out.write('\t0')
        out.write('\n')
out.close()

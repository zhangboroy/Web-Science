import feedparser
import re

# Returns title and dictionary of word counts for an RSS feed
def getwordcounts(url):
    # Parse the feed
    d=feedparser.parse(url)
    print (d.feed.title)
    wc={}

    # Loop over all the entries
    for e in d.entries:
        if 'summary' in e: summary=e.summary
        else: summary=e.description
        
        # Extract a list of words
        words=getwords(e.title+' '+summary)
        #words=getwords(e.title)
        for word in words:
            wc.setdefault(word,0)
            wc[word]+=1
    return d.feed.title,wc

def getwords(html):
    # Remove all the HTML tags
    txt=re.compile(r'<[^>]+>').sub('',html)

    # Split words by all non-alpha characters
    words=re.compile(r'[^A-Z^a-z]+').split(txt)

    # Convert to lowercase
    return [word.lower( ) for word in words if word!='']

apcount={}
wordcounts={}
feedlist=[line for line in open('feedlistReady.txt','r')]
for feedurl in feedlist:
    print (feedurl)
    title,wc=getwordcounts(feedurl)
    wordcounts[title]=wc
    for word,count in wc.items( ):
        apcount.setdefault(word,0)
        if count>1:
            apcount[word]+=1

wordlist1=[]
for w,bc in apcount.items( ):
    frac=float(bc)/len(feedlist)
    if frac>0.1 and frac<0.5: wordlist1.append([bc,w])

wordlist1.sort(reverse=True)

out=open('blogdata(allFilter).txt','a')
out.write('Blog')
for i in range(min(len(wordlist1),1000)): out.write('\t%s' % wordlist1[i][1])
out.write('\n')
for blog,wc in wordcounts.items( ):
    out.write(blog)
    for i in range(min(len(wordlist1),1000)):
        if wordlist1[i][1] in wc: out.write('\t%d' % wc[wordlist1[i][1]])
        else: out.write('\t0')
    out.write('\n')
out.close()

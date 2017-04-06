import urllib.request
from bs4 import BeautifulSoup
import langid

f = open('feedlist.txt', 'r', encoding='utf-8')
links = f.read().strip().split('\n')
f.close()

links = list(set(links))
linksForUse = {}
for link in links:
    print (link)
    try:
        with urllib.request.urlopen(link) as res:
            html = res.read()
        soup = BeautifulSoup(html, "html.parser")
        language = langid.classify(soup.title.string)
        if language[0]=='en':
            if soup.title.string not in linksForUse:
                linksForUse.setdefault(soup.title.string,[])
            linksForUse[soup.title.string].append(link)
    except:
        continue

i=0
for blog in linksForUse:
    if i<98:
        f = open('feedlistReady.txt', 'a', encoding='utf-8')
        for link in linksForUse[blog]:
            f.write(link+'\n')
        f.close()
    else:
        f = open('feedlistMore.txt', 'a', encoding='utf-8')
        for link in linksForUse[blog]:
            f.write(link+'\n')
        f.close()
    i = i+1

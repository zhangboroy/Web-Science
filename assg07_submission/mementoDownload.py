import urllib.request
from bs4 import BeautifulSoup
import json
import re
import datetime

def loadMovies(path='ml-100k'):
    movies={}
    f = open(path+'/u.item', 'r', encoding='ISO-8859-1')
    lines = f.readlines()
    f.close()
    for line in lines:
        line=line.split('|')
        (id,title)=line[0:2]
        URL=line[4]
        movies.setdefault(id,{})
        movies[id]['title']=title
        movies[id]['URL']=URL
    return movies

def getRating(url):
    with urllib.request.urlopen(url) as res:
        html = res.read()
    soup = BeautifulSoup(html, "html.parser")
    for b in soup.find_all('b'):
        m=re.search(r'.*(?=/10)', str(b.string))
        if m!=None:
            rating=m.group()
            break

    m=re.search(r'(?<=[(])\d.*(?= votes)', str(soup))
    voters=m.group()
    return rating, voters

def getMemento(link):
    with urllib.request.urlopen('http://memgator.cs.odu.edu/timemap/json/'+link) as res:
        html = res.read()
    soup = BeautifulSoup(html, "html.parser")
    timemap = json.loads(soup.string)
    for memento in timemap['mementos']['list']:
        m=re.search(r'.*(?=T)', memento['datetime'])
        if m.group()>='2005-07-31':
            row=[]
            row.append((datetime.datetime.strptime(m.group(),'%Y-%m-%d')-datetime.datetime(2005, 7, 31)).days)
            (rating, voters)=getRating(memento['uri'])
            row.append(rating)
            row.append(voters)
            break
    return row


movies=loadMovies()
for i in range(len(movies)):
    print (i+1)
    try:
        with urllib.request.urlopen(movies['%d' %(i+1)]['URL']) as res:
            line=getMemento(res.geturl())
        f = open('IMDBmementoRating.csv','a',encoding='utf-8')
        f.write('{}'.format(i+1)+'\t'+line[1]+'\t'+line[2]+'\t{}'.format(line[0])+'\n')
        f.close()
    except:
        continue

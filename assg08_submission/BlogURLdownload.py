import urllib.request
from bs4 import BeautifulSoup

def getNextPage(url,file):
    with urllib.request.urlopen(url) as res:
        html = res.read()
    soup = BeautifulSoup(html, "html.parser")
    for link in soup.find_all('link'):
        if link['rel']==['next']:
            f = open(file,'a',encoding='utf-8')
            f.write(link['href']+'\n')
            f.close()
            getNextPage(link['href'],file)
            break
    return


startLink='https://www.blogger.com/next-blog?navBar=true&blogID=3471633091411211117'
for i in range(500):
    print (i)
    try:
        with urllib.request.urlopen(startLink) as res:
            html = res.read()
        soup = BeautifulSoup(html, "html.parser")
        print (soup.title)

        for link in soup.find_all('link'):
            if link['rel']==['alternate'] and link['type']=='application/atom+xml':
                f = open('feedlist.txt','a',encoding='utf-8')
                f.write(link['href']+'\n')
                f.close()
                getNextPage(link['href'],'feedlist.txt')
                break
    except:
        continue


with urllib.request.urlopen('http://f-measure.blogspot.com/') as res:
    html = res.read()
soup = BeautifulSoup(html, "html.parser")
for link in soup.find_all('link'):
    if link['rel']==['alternate'] and link['type']=='application/atom+xml':
        f = open('feedlistReady.txt','a',encoding='utf-8')
        f.write(link['href']+'\n')
        f.close()
        getNextPage(link['href'],'feedlistReady.txt')
        break

with urllib.request.urlopen('http://ws-dl.blogspot.com/') as res:
    html = res.read()
soup = BeautifulSoup(html, "html.parser")
for link in soup.find_all('link'):
    if link['rel']==['alternate'] and link['type']=='application/atom+xml':
        f = open('feedlistReady.txt','a',encoding='utf-8')
        f.write(link['href']+'\n')
        f.close()
        getNextPage(link['href'],'feedlistReady.txt')
        break

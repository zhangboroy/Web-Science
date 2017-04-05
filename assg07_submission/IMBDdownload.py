import urllib.request
from bs4 import BeautifulSoup

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

movies=loadMovies()
for i in range(len(movies)):
    try:
        with urllib.request.urlopen(movies['%d' %(i+1)]['URL']) as res:
            html = res.read()
        soup = BeautifulSoup(html, "html.parser")
        line = soup.strong['title'].split(' ')
        f = open('IMDBrating.csv','a',encoding='ISO-8859-1')
        f.write('{}'.format(i+1)+'\t'+line[0]+'\t'+line[3]+'\n')
        f.close()
    except:
        f = open('missingMovies.csv','a',encoding='ISO-8859-1')
        f.write('{}'.format(i+1)+'\n')
        f.close()

import urllib.request
import re
from bs4 import BeautifulSoup

f = open('links.txt', 'r')
#Set a list to hold the links
links = []
#Set a list to hold the number of Mementos of the link
mementos = []

#Read links from the file 1 by 1
for line in f:
    links.append(line)
    memento = 0

    try:
        #Get the TimeMaps html
        response = urllib.request.urlopen('http://memgator.cs.odu.edu/timemap/link/'+line)
        html = response.read()
        soup = BeautifulSoup(html, "html.parser")
        
        #Traverse all the descendants and count the number of Mementos
        for child in soup.descendants:
            #For each descendant, search if there is any Memento in it
            if re.search(r'rel=".*memento"', str(child.string)):
                memento = memento+1

        mementos.append(memento)
    except:
        mementos.append(0)
        continue

f.close()

#Save the links and numbers of Mementos to a file
f = open('data_hist.csv', 'w')
line = f.write('URI\tmementos\n')
for i in range(len(links)):
    line = f.write(links[i].replace('\n','')+'\t{}'.format(mementos[i])+'\n')

f.close()

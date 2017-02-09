import urllib.request
import re
from bs4 import BeautifulSoup
import datetime

f = open('links.txt', 'r')
#Set a list to hold the links
links = []
#Set a list to hold the Estimated Creation Dates
EstimatedCreationDates = []

#Read links from the file 1 by 1
for line in f:
    links.append(line)
    print (line)

    try:
        #Get the Carbon Date html
        response = urllib.request.urlopen('http://cd.cs.odu.edu/cd?url='+line)
        html = response.read()
        soup = BeautifulSoup(html, "html.parser")
        print (soup.string)
        #Extract the Estimated Creation Date from it
        m=re.search(r'(?<="Estimated Creation Date":).*', soup.string)
        EstimatedCreationDates.append(m.group())

    except:
        EstimatedCreationDates.append('')
        continue

f.close()

#Set a list to hold ages of the links
ages = []
for date in EstimatedCreationDates:
    #Extract the date string
    m=re.search(r'(?<=").*(?=T)', date)
    if m:
        #Calculate the age (days between the date and now)
        ages.append((datetime.datetime.now()-datetime.datetime.strptime(m.group(),"%Y-%m-%d")).days)
    else:
        ages.append(-1)
    
#Save the links and ages to a file
f = open('ages.txt', 'w')
line = f.write('URI\tage\n')
for i in range(len(links)):
    line = f.write(links[i].replace('\n','')+'\t{}'.format(ages[i])+'\n')

f.close()

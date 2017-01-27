import urllib.request
from bs4 import BeautifulSoup

# Ask to input a URI
uri=input('Please enter a URI\n')

# Open this URI and save it into an html object
with urllib.request.urlopen(uri) as res:
    html = res.read()

# Extracts all the links from the html object
soup = BeautifulSoup(html, "html.parser")

# Open all the links 1 by 1 and check their Content-Type from the response
for links in soup.find_all('a'):
    response = urllib.request.urlopen(links.get('href'))

    # If the Content-Type is PDF, get the URI from the response of the opened link and print it
    if response.info()['Content-Type']=='application/pdf':
        print ("The original URI is: "+links.get('href'))
        if links.get('href')!=response.geturl():
            print ("The final URI is: "+response.geturl())

        # Print the Content-Length from the response of the opened link
        print ("The size of the PDF is: "+response.info()['Content-Length']+" bytes\n")

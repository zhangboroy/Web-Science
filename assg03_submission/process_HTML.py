import urllib.request
from bs4 import BeautifulSoup

for i in range(1000):
    try:
        #set the input file name
        file = "htmls/html{}".format(i)+".html"
        #open and read the html file
        f = open(file, 'rb')
        html = f.read()
        f.close()
        #remove the HTML markup
        soup = BeautifulSoup(html, 'html.parser')
        [s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
        visible_text = soup.getText()

        #save it to the corresponding output file
        f = open("htmls_processed/html{}".format(i)+"_processed.txt", 'w', encoding='utf-8')
        f.write(visible_text)
        f.close()
    except:
        continue


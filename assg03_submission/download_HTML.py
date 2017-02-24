import urllib.request
import os

#open the links file
f1 = open("links.txt", "r")
#reset the output file index
i = 0

for line in f1:
    #for every link, set the corresponding output file name
    outputFile = "htmls/html{}".format(i)+".html"
    #check if the output file exists.
    if os.path.exists(outputFile)==False:
        #if not, try to open the link and write the content to the output file.
        try:
            response = urllib.request.urlopen(line)
            html = response.read()
            response.close()
            f2 = open(outputFile, "wb")
            f2.write(html)
            f2.close()
        #if there is something wrong, save the link to another file.
        except:
            f3 = open('missingLinks.txt', 'a')
            f3.write(line)
            f3.close()
    #move the output file index
    i=i+1
f1.close()

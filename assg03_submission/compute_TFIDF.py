import math

#reset the count of suitable files
count=0
#set a list for TF of the suitable files
TF=[]
#set a list for the index of the suitable files
URI=[]

for i in range(1000):
    #stop when 10+ files have been found
    if count>9:
        break
    else:
        #reset the term number in this file
        terms=0
        #set the input txt file
        file = "htmls_processed/html{}".format(i)+"_processed.txt"
        try:
            #open and read the txt file
            f = open(file, 'r', encoding='utf-8')
            text = f.read()
            f.close()
            #split the content of the file into words
            texts = text.split()
            #check the words 1 by 1
            for word in texts:
                #count the number of found files and number of terms in the file
                if word.lower()=='wenger':
                    if terms==0:
                        count=count+1

                    terms=terms+1

            #compute TF and add it as well as the file's index to the corresponding lists
            if terms>0:
                total_words = len(texts)
                TF.append(terms/total_words)
                URI.append(i)

        except:
            continue

#compute IDF
IDF = math.log(46.8*(10**9)/55600000, 2)

#print the title of the output table
print ('TFIDF\tTF\tIDF\tURI')
#open the links file and read the links to a list
f = open('links.txt', 'r')
links = f.readlines()
f.close()

#set a list for the output table
output = []
#add content to the output list
for i in range(len(TF)):
    row = []
    row.append(TF[i]*IDF)
    row.append(TF[i])
    row.append(links[URI[i]])
    output.append(row)

#sort the output list
output.sort(reverse=True)

#print the content of the output table
for i in range(10):
    print ('{}'.format(round(output[i][0],5))+'\t{}'.format(round(output[i][1],5))+'\t{}'.format(round(IDF,5))+'\t'+output[i][2])


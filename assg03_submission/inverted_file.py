#set a list for the words in word index
words=[]
#set a list for the word frequencies in word index
wordsNumber=[]

for i in range(1000):
    #set the input txt file
    print (i)
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
            #reset the found mark
            found=0
            #check the words in the word index 1 by 1
            for j in range(len(words)):
                #update the corresponding number of the word index
                if word.lower()==words[j]:
                    wordsNumber[j]=wordsNumber[j]+1
                    found=1
                    break

            #add it to word index
            if found==0:
                words.append(word.lower())
                wordsNumber.append(1)

    except:
        continue

#set a list for the word index
wordIndex=[]

#merge the 2 lists into 1 single word index list
for k in range(len(words)):
    row = []
    row.append(wordsNumber[k])
    row.append(words[k])
    wordIndex.append(row)

#sort the word index list
wordIndex.sort(reverse=True)

#output the word index list into the inverted file
f = open("inverted file.txt", "w", encoding='utf-8')
f.write('word\tnumber\n')
f1 = open("inverted file.csv", "w")
for line in wordIndex:
    f.write(line[1]+'\t{}'.format(line[0])+'\n')
    f1.write('{}'.format(line[0])+'\n')

f.close()
f1.close()


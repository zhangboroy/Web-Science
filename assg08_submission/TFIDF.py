import math

def readfile(filename):
    f = open(filename, 'r', encoding='utf-8')
    lines=f.readlines()
    f.close()

    # First line is the column titles
    colnames=lines[0].strip( ).split('\t')[1:]
    rownames=[]
    data=[]
    for line in lines[1:]:
        p=line.strip( ).split('\t')
        # First column in each row is the rowname
        rownames.append(p[0])
        # The data for this row is the remainder of the row
        data.append([float(x) for x in p[1:]])
    return rownames,colnames,data


blognames,words,data=readfile('blogdata(allFilter).txt')
sumRow = [0 for i in range(len(blognames))]
countCol = [0 for i in range(len(words))]

for i in range(len(blognames)):
    for j in range(len(words)):
        sumRow[i] = sumRow[i] + data[i][j]
        if data[i][j]>0:
            countCol[j] = countCol[j] + 1

TFIDF=[]
for i in range(len(blognames)):
    line=[]
    for j in range(len(words)):
        line.append(data[i][j]/sumRow[i]*math.log(len(blognames)/countCol[j], 2))
    TFIDF.append(line)

f = open('blogdata(Q5).txt', 'w', encoding='utf-8')
f.write('Blog')
for word in words:
    f.write('\t'+word)
f.write('\n')
for i in range(len(blognames)):
    f.write(blognames[i])
    for j in range(len(words)):
        f.write('\t{}'.format(TFIDF[i][j]))
    f.write('\n')
f.close()

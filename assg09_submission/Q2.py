import re
import math

def readfile(filename):
    f = open(filename, 'r')
    lines=f.readlines()
    f.close()
    #lines=[line for line in file(filename)]

    # First line is the column titles
    colnames=lines[0].strip( ).split('\t')[1:]
    rownames=[]
    data=[]
    for line in lines[1:]:
        p=line.strip().split('\t')
        # First column in each row is the rowname
        rownames.append(p[0])
        # The data for this row is the remainder of the row
        data.append([float(x) for x in p[1:]])
    return rownames,colnames,data


def getwords(doc):
    splitter=re.compile('\\W*')
    # Split the words by non-alpha characters
    words=[s.lower() for s in splitter.split(doc)
           if len(s)>2 and len(s)<20]

    # Return the unique set of words only
    return dict([(w,1) for w in words])


class classifier:
    def __init__(self,getfeatures,filename=None):
        # Counts of feature/category combinations
        self.fc={}
        # Counts of documents in each category
        self.cc={}
        self.getfeatures=getfeatures

    # Increase the count of a feature/category pair
    def incf(self,f,cat):
        self.fc.setdefault(f,{})
        self.fc[f].setdefault(cat,0)
        self.fc[f][cat]+=1

    # Increase the count of a category
    def incc(self,cat):
        self.cc.setdefault(cat,0)
        self.cc[cat]+=1

    # The number of times a feature has appeared in a category
    def fcount(self,f,cat):
        if f in self.fc and cat in self.fc[f]:
            return float(self.fc[f][cat])
        return 0.0

    # The number of items in a category
    def catcount(self,cat):
        if cat in self.cc:
            return float(self.cc[cat])
        return 0

    # The list of all categories
    def categories(self):
        return self.cc.keys( )

    def train(self,item,cat):
        features=self.getfeatures(item)
        # Increment the count for every feature with this category
        for f in features:
            self.incf(f,cat)

        # Increment the count for this category
        self.incc(cat)

    def fprob(self,f,cat):
        if self.catcount(cat)==0: return 0
        
        # The total number of times this feature appeared in this
        # category divided by the total number of items in this category
        return self.fcount(f,cat)/self.catcount(cat)

    def weightedprob(self,f,cat,prf,weight=1.0,ap=0.5):
        # Calculate current probability
        basicprob=prf(f,cat)

        # Count the number of times this feature has appeared in
        # all categories
        totals=sum([self.fcount(f,c) for c in self.categories( )])

        # Calculate the weighted average
        bp=((weight*ap)+(totals*basicprob))/(weight+totals)
        return bp


class fisherclassifier(classifier):
    def cprob(self,f,cat):
        # The frequency of this feature in this category
        clf=self.fprob(f,cat)
        if clf==0: return 0

        # The frequency of this feature in all the categories
        freqsum=sum([self.fprob(f,c) for c in self.categories( )])

        # The probability is the frequency in this category divided by
        # the overall frequency
        p=clf/(freqsum)

        return p

    def fisherprob(self,item,cat):
        # Multiply all the probabilities together
        p=1
        features=self.getfeatures(item)
        for f in features:
            p*=(self.weightedprob(f,cat,self.cprob))

        # Take the natural log and multiply by -2
        fscore=-2*math.log(p)

        # Use the inverse chi2 function to get a probability
        return self.invchi2(fscore,len(features)*2)

    def invchi2(self,chi,df):
        m = chi / 2.0
        sum = term = math.exp(-m)
        for i in range(1, df//2):
            term *= m / i
            sum += term
        return min(sum, 1.0)

    def __init__(self,getfeatures):
        classifier.__init__(self,getfeatures)
        self.minimums={}

    def setminimum(self,cat,min):
        self.minimums[cat]=min

    def getminimum(self,cat):
        if cat not in self.minimums: return 0
        return self.minimums[cat]

    def classify(self,item,default=None):
        # Loop through looking for the best result
        best=default
        max=0.0
        for c in self.categories( ):
            p=self.fisherprob(item,c)
            # Make sure it exceeds its minimum
            if p>self.getminimum(c) and p>max:
                best=c
                max=p
        return best


cl=fisherclassifier(getwords)

f=open('summary.txt','r',encoding='utf-8')
summary=f.readlines()
f.close()
f=open('entries.txt','r',encoding='utf-8')
lines=f.readlines()
f.close()

categories={}
for i in range(50):
    cat=lines[i+1].strip().split('\t')[1]
    cl.train(summary[i].strip(),cat)
    if cat not in categories:
        categories.setdefault(cat,[0,0,0])

result=[]
f=open('Q2.txt','w',encoding='utf-8')
f.write('title\tactual\tpredicted\n')
for i in range(50,100):
    line=lines[i+1].strip().split('\t')
    result.append([line[1],cl.classify(summary[i].strip())])
    f.write(line[0]+'\t'+result[i-50][0]+'\t'+result[i-50][1]+'\n')
f.close()

for i in range(50):
    if result[i][0]==result[i][1]:
        categories[result[i][0]][0]+=1
    else:
        categories[result[i][0]][1]+=1
        categories[result[i][1]][2]+=1

print ('Category\tPrecision\tRecall\tF-Measure')
TP=0
FP=0
FN=0
for cat in categories:
    TP+=categories[cat][0]
    FN+=categories[cat][1]
    FP+=categories[cat][2]
    precision=categories[cat][0]/(categories[cat][0]+categories[cat][2])
    recall=categories[cat][0]/(categories[cat][0]+categories[cat][1])
    print (cat+'\t{}'.format(precision)+'\t{}'.format(recall)
           +'\t{}'.format(2*precision*recall/(precision+recall)))

TP=TP/len(categories)
FP=FP/len(categories)
FN=FN/len(categories)
precision=TP/(TP+FP)
recall=TP/(TP+FN)
print ('Average\t{}'.format(precision)+'\t{}'.format(recall)
       +'\t{}'.format(2*precision*recall/(precision+recall)))

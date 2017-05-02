from svm import *
from svmutil import *

f=open('entries.txt','r',encoding='utf-8')
lines=f.readlines()
f.close()
entries=[]
for i in range(1,len(lines)):
    entries.append(lines[i].strip().split('\t'))
entries.sort()

f=open('feeddata.txt','r',encoding='utf-8')
lines=f.readlines()
f.close()
feeddata=[]
for i in range(1,len(lines)):
    feeddata.append(lines[i].strip().split('\t'))
feeddata.sort()

answers=[]
inputs=[]
categories=[]
for i in range(len(entries)):
    answers.append(entries[i][1])
    if entries[i][1] not in categories:
        categories.append(entries[i][1])
    inputs.append(list(map(int,feeddata[i][1:len(feeddata[i])])))

cat=[]
for i in range(len(categories)):
    cat.append([])
    for ans in answers:
        if ans==categories[i]:
            cat[i].append(1)
        else:
            cat[i].append(0)
            

svm_model.predict = lambda self, x: svm_predict([0], [x], self)[0][0]
param = svm_parameter()
param.kernel_type = RBF

for i in range(len(categories)):
    print ('\n'+categories[i]+':')
    acc=0
    for j in range(10):
        trainCat=[]
        trainInputs=[]
        testCat=[]
        testInputs=[]
        for k in range(len(cat[i])):
            if k<(j+1)*len(cat[i])/10 and k>=j*len(cat[i])/10:
                testCat.append(cat[i][k])
                testInputs.append(inputs[k])
            else:
                trainCat.append(cat[i][k])
                trainInputs.append(inputs[k])

        prob = svm_problem(trainCat,trainInputs)
        m = svm_train(prob, param)
        p_labels, p_acc, p_vals = svm_predict(testCat,testInputs, m)
        acc+=p_acc[0]
    print ('Average Accuracy = {}'.format(acc/10)+'%')

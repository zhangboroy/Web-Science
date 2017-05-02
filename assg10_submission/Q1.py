import math

def cosine(v1,v2):
    x=0.0
    for i in range(len(v1)):
        x+=v1[i]**2
        
    y=0.0
    for i in range(len(v2)):
        y+=v2[i]**2
        
    z=0.0
    for i in range(len(v1)):
        z+=(v1[i]-v2[i])**2
        
    return (x+y-z)/2/math.sqrt(x*y)

def getdistances(data,vec1):
    distancelist=[]
    for i in range(len(data)):
        vec2=data[i]['input']
        distancelist.append((cosine(vec1,vec2),i))
    distancelist.sort(reverse=True)
    return distancelist

def knnestimate(data,vec1,k=3):
    # Get sorted distances
    dlist=getdistances(data,vec1)

    result=[]
    for i in range(k):
        idx=dlist[i][1]
        result.append(data[idx]['Blog'])
    return result


f=open('blogdata(allFilter).txt','r',encoding='utf-8')
lines=f.readlines()
f.close()
data=[]
for i in range(1,len(lines)):
    line=lines[i].strip().split('\t')
    row={}
    row.setdefault('Blog',line[0])
    row.setdefault('input',[])
    for j in range(1,len(line)):
        row['input'].append(int(line[j]))
    data.append(row)
    if row['Blog']=='F-Measure':
        fMeasure=row['input']
    if row['Blog']=='Web Science and Digital Libraries Research Group':
        WSDLRG=row['input']

print(knnestimate(data,fMeasure,1))
print(knnestimate(data,fMeasure,2))
print(knnestimate(data,fMeasure,5))
print(knnestimate(data,fMeasure,10))
print(knnestimate(data,fMeasure,20))
print(knnestimate(data,WSDLRG,1))
print(knnestimate(data,WSDLRG,2))
print(knnestimate(data,WSDLRG,5))
print(knnestimate(data,WSDLRG,10))
print(knnestimate(data,WSDLRG,20))

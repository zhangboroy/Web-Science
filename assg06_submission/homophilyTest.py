f = open("graph.csv", "r", encoding='utf-8')
f.readline()

usernames=[]
genders=[]
usernamesCheck=[]

while True:
    line = f.readline().strip()
    if line!='edges:':
        usernames.append(line)
        line = f.readline().strip()
        genders.append(line)
        line = f.readline().strip()
        usernamesCheck.append(int(line))
    else:
        break

lines=f.readlines()
f.close()

genderTable=[]
for i in range(len(usernames)):
    row = [genders[i], usernames[i], usernamesCheck[i]]
    genderTable.append(row)

genderTable.sort()

f = open("genderTable.txt", "w", encoding='utf-8')
f.write('Username')
for i in range(12):
    f.write(' ')
f.write('Gender\tUsername')
for i in range(12):
    f.write(' ')
f.write('Gender\tUsername')
for i in range(12):
    f.write(' ')
f.write('Gender\n')
for i in range(0,int(len(genderTable)/3)*3,3):
    f.write(genderTable[i][1])
    for j in range(20-len(genderTable[i][1])):
        f.write(' ')
    f.write(genderTable[i][0]+'\t'+genderTable[i+1][1])
    for j in range(20-len(genderTable[i+1][1])):
        f.write(' ')
    f.write(genderTable[i+1][0]+'\t'+genderTable[i+2][1])
    for j in range(20-len(genderTable[i+2][1])):
        f.write(' ')
    f.write(genderTable[i+2][0]+'\n')
if i+3<len(genderTable):
    f.write(genderTable[i+3][1])
    for j in range(20-len(genderTable[i+3][1])):
        f.write(' ')
    f.write(genderTable[i+3][0])
if i+4<len(genderTable):
    f.write('\t'+genderTable[i+4][1])
    for j in range(20-len(genderTable[i+4][1])):
        f.write(' ')
    f.write(genderTable[i+4][0])
f.write('\n')
f.close()

genderTable100=[]
for i in range(len(genderTable)):
    if genderTable[i][2]==1:
        genderTable100.append(genderTable[i])

edges = int(len(lines)/2) + (len(genderTable100) - 1)
edgesCross = 0

f = open("genderTable100.txt", "w", encoding='utf-8')
f.write('Username')
for i in range(12):
    f.write(' ')
f.write('Gender\tUsername')
for i in range(12):
    f.write(' ')
f.write('Gender\tUsername')
for i in range(12):
    f.write(' ')
f.write('Gender\n')
for i in range(0,int(len(genderTable100)/3)*3,3):
    if genderTable100[i][0]=='female':
        edgesCross = edgesCross + 1
    if genderTable100[i+1][0]=='female':
        edgesCross = edgesCross + 1
    if genderTable100[i+2][0]=='female':
        edgesCross = edgesCross + 1
    f.write(genderTable100[i][1])
    for j in range(20-len(genderTable100[i][1])):
        f.write(' ')
    f.write(genderTable100[i][0]+'\t'+genderTable100[i+1][1])
    for j in range(20-len(genderTable100[i+1][1])):
        f.write(' ')
    f.write(genderTable100[i+1][0]+'\t'+genderTable100[i+2][1])
    for j in range(20-len(genderTable100[i+2][1])):
        f.write(' ')
    f.write(genderTable100[i+2][0]+'\n')
if i+3<len(genderTable100):
    if genderTable100[i+3][0]=='female':
        edgesCross = edgesCross + 1
    f.write(genderTable100[i+3][1])
    for j in range(20-len(genderTable100[i+3][1])):
        f.write(' ')
    f.write(genderTable100[i+3][0])
if i+4<len(genderTable100):
    if genderTable100[i+4][0]=='female':
        edgesCross = edgesCross + 1
    f.write('\t'+genderTable100[i+4][1])
    for j in range(20-len(genderTable100[i+4][1])):
        f.write(' ')
    f.write(genderTable100[i+4][0])
f.write('\n')
f.close()

print ('Males: {}'.format(len(genderTable100)-edgesCross)+'\tFemales: {}'.format(edgesCross))
print ('Randomly assigned cross-gender edges fraction: {}'.format(2*edgesCross*(len(genderTable100)-edgesCross)/(len(genderTable100)**2)))

for i in range(int(len(lines)/2)):
    if genders[int(lines[i*2].strip())]!=genders[int(lines[i*2+1].strip())]:
        edgesCross = edgesCross +1

print ('edges: {}'.format(edges)+'\tedgesCross: {}'.format(edgesCross))
print ('Actual cross-gender edges fraction: {}'.format(edgesCross/edges))

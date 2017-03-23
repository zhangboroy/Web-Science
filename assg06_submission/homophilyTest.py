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
f.write('Gender\n')
for element in genderTable:
    f.write(element[1])
    for i in range(20-len(element[1])):
        f.write(' ')
    f.write(element[0]+'\n')

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
f.write('Gender\n')
for element in genderTable100:
    if element[0]=='female':
        edgesCross = edgesCross + 1
    f.write(element[1])
    for i in range(20-len(element[1])):
        f.write(' ')
    f.write(element[0]+'\n')

f.close()

print ('Males: {}'.format(len(genderTable100)-edgesCross)+'\tFemales: {}'.format(edgesCross))
print ('Randomly assigned cross-gender edges fraction: {}'.format(2*edgesCross*(len(genderTable100)-edgesCross)/(len(genderTable100)**2)))

for i in range(int(len(lines)/2)):
    if genders[int(lines[i*2].strip())]!=genders[int(lines[i*2+1].strip())]:
        edgesCross = edgesCross +1

print ('edges: {}'.format(edges)+'\tedgesCross: {}'.format(edgesCross))
print ('Actual cross-gender edges fraction: {}'.format(edgesCross/edges))

f = open("linkedinConnectionsNumber.txt", "r", encoding='utf-8')
lines = f.readlines()
f.close()

f = open("linkedinConnections.csv", "w", encoding='utf-8')
f.write('label\tfriends\n')
for i in range(len(lines)):
    if lines[i]=='500+\n':
        f.write('f{}'.format(i+1)+'\t500\n')
    else:
        f.write('f{}'.format(i+1)+'\t{}'.format(int(lines[i])-1)+'\n')

f.write('me\t{}'.format(len(lines))+'\n')
f.close()

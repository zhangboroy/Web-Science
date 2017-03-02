import re

f = open('linkedinConnections.txt', 'r')
lines=f.readlines()
f.close()

f = open('linkedinContactLinks.txt', 'w', encoding='utf-8')
for line in lines:
    m = re.search(r'(?<=href=")\S*(?=")', line)
    if m:
        f.write('https://www.linkedin.com'+m.group()+'\n')

f.close()

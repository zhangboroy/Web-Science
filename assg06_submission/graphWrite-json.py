import networkx as nx
from networkx.readwrite import json_graph
import json

g = nx.Graph()

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

for i in range(len(usernames)):
    g.add_node(i, username=usernames[i], gender=genders[i], usernamesCheck=usernamesCheck[i])

for i in range(len(usernames)-1):
    g.add_edge(len(usernames)-1,i)

for i in range(int(len(lines)/2)):
    g.add_edge(int(lines[i*2].strip()),int(lines[i*2+1].strip()))

data = json_graph.node_link_data(g)
s = json.dumps(data)

f = open('graph.json', 'w')
f.write(s)
f.close()


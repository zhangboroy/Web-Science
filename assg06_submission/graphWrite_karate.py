import networkx as nx
from networkx.readwrite import json_graph
import json

g = nx.Graph()

f = open("karateGraph.txt", "r", encoding='utf-8')

edge=[]
while True:
    line = f.readline().strip()
    if line!='nodes.gender:':
        line = line.split()
        row = [int(line[0]),int(line[1])]
        edge.append(row)
    else:
        break

lines=f.readlines()
f.close()

for element in edge:
    if lines[element[0]]==lines[element[1]]:
        g.add_edge(element[0],element[1],broken=0)
    else:
        g.add_edge(element[0],element[1],broken=1)

for i in range(len(lines)):
    g.add_node(i, name=i, group=int(lines[i].strip()))

data = json_graph.node_link_data(g)
s = json.dumps(data)

f = open('karate.json', 'w')
f.write(s)
f.close()

import pygraphml

file = input('Please input file name: ')

g = pygraphml.Graph()

f = open(file+".csv", "r", encoding='utf-8')
f.readline()

nodes=f.readlines()

for i in range(len(nodes)):
    line = nodes[i].split('\t')
    n = g.add_node(line[0])
    n['Label'] = line[0]
    n['friend_count'] = line[1]

f.close()
parser = pygraphml.GraphMLParser()
parser.write(g, file+".graphml")

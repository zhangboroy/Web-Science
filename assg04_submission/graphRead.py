import pygraphml

parser = pygraphml.GraphMLParser()
g = parser.parse("mln.graphml")

f = open("facebookFriends.csv", "w", encoding='utf-8')
f.write('label\tfriends\n')

index = 1
for node in g.nodes():
    try:
        f.write('f{}'.format(index)+'\t'+node['friend_count']+'\n')
        index = index + 1
    except:
        continue

f.write('me\t{}'.format(index-1)+'\n')
f.close()

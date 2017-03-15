library("igraph")
karate = graph.famous("Zachary")
ebc = edge.betweenness.community(karate)
cut = cutat(ebc,2)
colors = rainbow(2)
plot(karate, vertex.color=colors[cut])
cut

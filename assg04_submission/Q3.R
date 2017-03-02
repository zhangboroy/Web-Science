data=read.csv("linkedinConnections.csv", header=T, sep='\t')
friends=data[-nrow(data),]
print(mean(friends[,"friends"]))
print(sd(friends[,"friends"]))
print(median(friends[,"friends"]))
data=data[order(data[,"friends"],decreasing=TRUE),]
me=which(data[,"label"]=='me')
plot(data[,"friends"],main="Connection# of My Connections", xlab="My Connections",ylab="Number of Connections")
text(me, data[me,"friends"]+20,"me", col="Red")

data=read.csv("facebookFriends.csv", header=T, sep='\t')
friends=data[-nrow(data),]
print(mean(friends[,"friends"]))
print(sd(friends[,"friends"]))
print(median(friends[,"friends"]))
data=data[order(data[,"friends"],decreasing=TRUE),]
me=which(data[,"label"]=='me')
plot(log(data[,"friends"],base=2),main="Friend# of My Friends", xlab="My Friends",ylab="log2(Number of Friends)")
text(me, log(data[me,"friends"],base=2)+0.5,"me", col="Red")

data=read.csv("twitterFollowing.csv", header=T, sep='\t')
friends=data[-nrow(data),]
print(mean(friends[,"friends"]))
print(sd(friends[,"friends"]))
print(median(friends[,"friends"]))
data=data[order(data[,"friends"],decreasing=TRUE),]
me=which(data[,"label"]=='me')
plot(log(data[,"friends"]+1,base=2),main="Following# of My Followings", xlab="My Followings",ylab="log2(Number of Followings)")
text(me, log(data[me,"friends"]+1,base=2)+1,"me", col="Red")

data=read.csv("data_hist.csv", header=T, sep='\t')
hist(log(data[,"mementos"]+1,base=2), right=FALSE, col=7, main="URIs vs. number of Mementos", xlab="log2(Number of Mementos)", ylab="URIs")

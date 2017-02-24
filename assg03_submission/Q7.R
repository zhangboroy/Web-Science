data=read.csv("inverted file.csv", header=F, sep='\t')
hist(log(data[,1],base=2), right=FALSE, col=7, main="the Frequency of Words", xlab="log2(Frequency)", ylab="Words")

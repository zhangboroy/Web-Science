data=read.csv("data_scatter.csv", header=T, sep='\t')
plot(log(data[,"age"],base=2),log(data[,"mementos"],base=2), main="Number of Mementos vs. URI's age", xlab="log2(URI's age)",ylab="log2(Number of Mementos)")

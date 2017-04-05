data=read.csv("rankContrast.csv", header=T, sep='\t')
plot(data[,"MovieLense.Rank"], data[,"IMDB.Rank"], xlab="MovieLense Rank",ylab="IMDB Rank")
cor.test(~MovieLense.Rank + IMDB.Rank, data=data, method="pearson")

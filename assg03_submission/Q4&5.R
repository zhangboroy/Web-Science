data=read.csv("alexa.csv", header=T, sep='\t')
cor.test(~PageRank + TFIDF, data=data, method="kendall")
cor.test(~PageRank + alexa, data=data, method="kendall")
cor.test(~alexa + TFIDF, data=data, method="kendall")

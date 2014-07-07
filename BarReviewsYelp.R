#plots data from downloaded text files, transformed by the Python Script 

library(ggplot2)
library(reshape)
bardata<-read.table("C:/path/counts.txt",header=TRUE,sep="\t",row.names=NULL)
head(bardata)
bardata$date<-as.Date(bardata$date,"%m/%d/%Y")
bardatayr<-subset(bardata,bardata$date>as.Date("2014-01-01"))
bardatamo<-as.integer(format(bardatayr$date,"%m"))
baragg<-aggregate(comment~Bar+bardatamo,sum,data=bardatayr)
ggplot(baragg,aes(x=bardatamo,y=comment,col=Bar,size=1))+geom_line()+theme(legend.text=element_text(size=15))+guides(colour=guide_legend(override.aes=list(size=5)))+theme(legend.key=element_rect(fill=NA))

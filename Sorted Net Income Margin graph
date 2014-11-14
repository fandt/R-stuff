#read file of stock Net Income Margins and graph in order of gain or loss over 3 yrs
DG<-read.table("C:/Users/Public/Documents/today.txt",header=TRUE,sep="\t")
headers<-colnames(DG)
SDF<-data.frame(setNames(nm=headers))
SDF[,1]<- t(DG[1,])
SDF[,2]<- t(DG[6,])
SDF[,3]<- as.numeric(SDF[,1])-as.numeric(SDF[,2])
SDFR<-SDF[order(SDF[,3]),]
NetIncomeMargin <- list()
for (eq in 1:dim(SDFR)[1]){
 NetIncomeMargin[eq]<-as.numeric(as.character(SDFR[eq,1]))
 }
company <- 1:length(NetIncomeMargin)
plot(company,NetIncomeMargin,col="blue",xaxt='no',xaxs="i",yaxs="i",ylim=c(-28,58))
axis(1,at=company,labels=headers,cex.axis=.75,las=2)
NIM3prev <- list()
for (eq3p in 1:dim(SDFR)[1]){
 NIM3prev[eq3p]<-as.numeric(as.character(SDFR[eq3p,2]))
}
#NIMavg <- list()
#for (eq3p in 1:dim(DG)[2]){
# NIMavg[eq3p]<-as.numeric(as.character(DG[6,eq3p]))
#}
points(company,NIM3prev,col="green")
for (col in 2:length(NetIncomeMargin)){
 ycord<-c(NetIncomeMargin[col],NIM3prev[col])
 xcord<-c(col,col)
 lines(xcord,ycord)
 if (as.numeric(NetIncomeMargin[col])<as.numeric(NIM3prev[col]) & NIM3prev[col]!="NA" & NetIncomeMargin[col]!="NA"){
  lines(xcord,ycord,col='red')
 }
}
title("3 yr previous Net Income Margin (green) vs present (blue)")

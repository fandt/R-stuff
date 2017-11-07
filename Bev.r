library(MASS)

PL<-read.table("C:/Users/Rebecca/Desktop/Bevager/Test Doc 2.txt", sep="\t",header=T,colClass=c("character",NA),strip.white=T)
head(PL)
Prices<-read.table("C:/Users/Rebecca/Desktop/Bevager/Test Doc 1.txt", sep="\t",header=T)
head(Prices)
Prices$Price<-gsub("$","",as.character(Prices$Price))

PLwP<-unique(PL)
for (boo in 1:dim(PLwP)[1]){
 PLwP[boo,1]<-  gsub("\\s+"," ",as.character(PLwP[boo,1]))
 price<-Prices[grep(PLwP[boo,1],Prices$Name),2] 
#this mess looks for more than one price
 if (length(price)>1){
  for (dee in 2:length(price)){
   if (price[1]!= price[dee]){
    price<-paste("This product has more than one price:",PLwP[boo,1])
    break
 }else (price<-price[1])
}}
 PLwP[boo,2]<-  as.character(price)
}
ProductListWithPrice<-PLwP[!duplicated(PLwP$Name),]
write.matrix(ProductListWithPrice,"C:/Users/Rebecca/Desktop/Bevager/rm.xls",sep="\t")


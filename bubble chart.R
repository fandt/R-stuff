names <- c("a","b","c","d",
            "e","f","g",
            "h","i","j","k",
            "l","m","n","o",
            "p")
a <- c(1,.84,7530134,.65,9275991)
b <- c(2, 1.05,8440178,.97,6519392)
c <- c(3, 1.27, 8499850,1.07,3231934)
d <- c(4, 1.12, 9248838,1.01,7364730)
e <- c(5, .92,11279190,1,8097959)
f <- c(6, .74, 11944166,.9,10856683)
g <- c(7, 1.27, 12077664,.98,12606910)
h <- c(8, 1.05, 17709842,.89,19381090)
i <- c(9, .97, 17754273,.91,15747292)
j <- c(10, 1.16, 19286408, 1.03, 20322061)
k <- c(11, .94, 23178754, .98, 15039275)
l <- c(12, 0.79, 25607760, 1.09, 13277209)
m <- c(13, 1.05, 33341408, .99, 33330399)
n <- c(14, 1.16,60743107, 1.11, 48138507)
o <- c(15, 1.02,68799231, .86, 76395194)
p <- c(16, 1.10,289158768, 1.04, 193304000)
oDF <- data.frame(a, b, c, d, e, f, g,
                    h, i, j, k, l, m, n, o, p )
#a<- c(1,2,3)
#b<-c(4,5,6)
#fuckme<-data.frame(a,b)
#fuckme
#  a b
#1 1 4
#2 2 5
#3 3 6

radius2011 <- sqrt( oDF[3,]/pi)
radius2002 <- sqrt( oDF[5,]/pi)
EoR2011 <- (oDF[2,])
EoR2002 <- (oDF[4,])
radius <- data.frame(radius2011,radius2002)
EoR <- data.frame(EoR2011,EoR2002)
order <- t(oDF[1,])
#symbols(oDF[1,],oDF[4,],circles=radius2002, inches=.65,
#       fg="white", bg="grey")
#symbols(oDF[1,],oDF[2,],circles=radius2011, inches=.65,
#        fg="white",bg="blue",xlab="Company",ylab="Expense/Revenue")

colors <- c(rep("grey",16),rep("blue",16))
symbols(c(order,order),c(EoR2002,EoR2011),
        circles=c(radius2002,radius2011), inches=.65,
        fg="white", bg=colors,
        xlab="Company (bubble size represents Revenue)",xaxt='n',ylab="Expense/Revenue",main="2002 and 2011 Expense:Revenue and Revenue")
text(order,EoR2011,names,cex=.5)

for (op in 1:dim(oDF)[2]){
  arrows(oDF[1,op],oDF[4,op],oDF[1,op],oDF[2,op])
}
abline(h=1)
legend("topright",c("2002","2011"),col=c("grey","blue"),pch=c(1,1))

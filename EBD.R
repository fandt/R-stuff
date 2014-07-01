#just plotting of labeled points with curved lines between matches

X<-c(-40,-15,40,-5,2,1,3,3.5,4.25,2,24.5,	26.5,38,-4,-4,-8)
Y<-c(10.75,8.8,9.2,8.9,-3,6,5.5,3,3.5,8.25,6.5,5.5,10.25,4,2.4,1.3)
Z<-c("Mission Support
<-($xxk)","XXX
$xxk","

XXX  
(XXXX)","XX/XXX","sifla e mapekng","Wenirot","Poiuy","Yuiop[]/mnbvcx Qwrete","Qweritval WID","Pkfce 
Devpmt","Qe Mioeinn Eo;q Okwf","VMB","Qweritvaaa
 Poiuale","Asdfgvot","Zxcvoni Lkjhgu","Blabalablala")

X<-c(-15,35,26.5)
Y<-c(8.5,9.2,5.5)
Z<-c("XXX ($xxk)","
XXX (XXX) 
$XXk","XXX 
$XXk")

plot(X, Y, main="Monthly Earnings Before Depreciation (EBD)
Month 20XX (6 months)", sub="",
   xlab="(Mission Aligment)", ylab="(Profit/Month)",
   xlim=c(-45, 45), ylim=c(-10, 11), col="red",axes=FALSE) 
text(X,Y,Z, cex=0.6, pos=4,col="red")

xm<-c(8.9,-.6,3,-15,1,-.45,.45,3,.825,36,-19,9)
xmb<-c(38,-40,42,-36)
ym<-c(8.6,4,2.4,1.3,8.25,6,5.5,3.5,3,5.6,5.5,-3)
ymb<-c(8.5,10.7,10.5,9.2)
zm<-c("XX/XXX","Wenirot","Zxcvoni Lkjhgu", "Gobblygooky","Pkfce Devpmt","Qweniohs","Tyuiop","Zrxcvvaer WID","Yuiop[]/mnbvcx Qwrete","Dr Romenasdl 
Qwer Mgmt $xxk","PMB ($xxk)","Blabalablala")
zmb<-c("

GOO $xxk","Qisszon Ryoott <-($xxk)","
Ohmanthisis 
Boring
-> $xxk","DSK (FAET) ($xxk)")
lines(xm,ym, type="b", pch=4, col="black", lty=0)
text(xm,ym,zm, cex=.6, pos=4,col="black")
lines(xmb,ymb,type="b",pch=4,col="black",lty=0)
text(xmb,ymb,zmb, cex=.65,pos=4,col="black",font=2)
 

axis(side=2,pos=0, tck=0, at = c(-10,10), labels = NA) 
axis(side=1,pos=0, tck=0, at = c(-40,-30,-20,-10,0,10,20,30,40),labels = c("-$50k","-$30k","-$20k","-$10k","0","$10k","$20k","$30k","$50k"))

lm1x<-c(38,-11)
lm1y<-c(8.8,8.8)

lm2x<-c(-16,26.5)
lm2y<-c(5.5,5.5)

lm3x<-c(-28,40)
lm3y<-c(9.2,9.2)

#arrows(-29.4,9.3,34.1,9.3,length=.15,angle=30, col='red',lty=2)
#arrows(36.5,8.9,-11.2,8.9,length=.15, angle=30, col='red', lty=2)
#arrows(-16,5.5,26.1,5.5,length=.15,angle=30, col='red',lty=2)
igraph:::igraph.Arrows(34.1,9.3,-25,9.3, curved=-.07, sh.col='red', sh.lty=2)
igraph:::igraph.Arrows(-9,8.3,36.5,8.3, curved=-.09, sh.col='red', sh.lty=2)
igraph:::igraph.Arrows(26.1,5.5,-12,5.5, curved=.04, sh.col='red', sh.lty=2)

cutptrtx<-c(36,34,36,34,36,34,36,34,36,34,36,34,36)
cutptrty<-c(-12,-10,-8,-6,-4,-2,0,2,4,6,8,10,12)
lines(cutptrtx,cutptrty,type="c",col="black",lty=2)
cutptrtx<-c(37,35,37,35,37,35,37,35,37,35,37)
cutptrty<-c(-12,-10,-8,-6,-4,-2,0,2,4,6,8)
cutptlfx<-c(35,37)
cutptlfy<-c(10,12)
lines(cutptlfx,cutptlfy,type="c",col="black",lty=2)
lines(cutptrtx,cutptrty,type="c",col="black",lty=2)
cutptlfx<-c(-34,-36,-34,-36,-34,-36,-34,-36,-34,-36,-34)
cutptlfy<-c(-12,-10,-8,-6,-4,-2,0,2,4,6,8)
lines(cutptrtx,cutptrty,type="c",col="black",lty=2)
cutptlfx<-c(-35,-37,-35,-37,-35,-37,-35,-37,-35,-37,-35)
cutptrlfy<-c(-12,-10,-8,-6,-4,-2,0,2,4,6,8)
lines(cutptlfx, cutptrlfy, type="c",col="black",lty=2)


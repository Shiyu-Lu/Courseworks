library(fBasics)
library(timeDate)
library(timeSeries)
library(seasonal)
library(seasonalview)
CHN_quarterlyGDP <- read.csv("Desktop/CHN_quarterlyGDP.csv")
qGDP <- CHN_quarterlyGDP$qGDP

qGDPt_r1 <- ts(qGDP[1:106],start=c(1992,1),frequency=4)
plot(qGDPt_r1)
adj_r1 <- seas(qGDPt_r1,x11='',outlier=NULL,forecast.maxlead=10)
summary(adj_r1)
a1 <- series(adj_r1,c('d11','d10','forecast.forecasts'))
a1

qGDPt_r2 <- ts(qGDP[2:107],start=c(1992,2),frequency=4)
plot(qGDPt_r2)
adj_r2 <- seas(qGDPt_r2,x11='',outlier=NULL,forecast.maxlead=10)
summary(adj_r2)
a2 <- series(adj_r2,c('d11','d10','forecast.forecasts'))
a2

qGDPt_r3 <- ts(qGDP[3:108],start=c(1992,3),frequency=4)
plot(qGDPt_r3)
adj_r3 <- seas(qGDPt_r3,x11='',outlier=NULL,forecast.maxlead=10)
summary(adj_r3)
a3 <- series(adj_r3,c('d11','d10','forecast.forecasts'))
a3

qGDPt_r4 <- ts(qGDP[4:109],start=c(1992,4),frequency=4)
plot(qGDPt_r4)
adj_r4 <- seas(qGDPt_r4,x11='',outlier=NULL,forecast.maxlead=10)
summary(adj_r4)
a4 <- series(adj_r4,c('d11','d10','forecast.forecasts'))
a4

qGDPt_r5 <- ts(qGDP[5:110],start=c(1993,1),frequency=4)
plot(qGDPt_r5)
adj_r5 <- seas(qGDPt_r5,x11='',outlier=NULL,forecast.maxlead=10)
summary(adj_r5)
a5 <- series(adj_r5,c('d11','d10','forecast.forecasts'))
a5
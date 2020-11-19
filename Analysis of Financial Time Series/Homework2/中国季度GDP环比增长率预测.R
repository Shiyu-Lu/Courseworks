library(fBasics)
library(timeDate)
library(timeSeries)
library(seasonal)
library(seasonalview)
CHN_POPgr <- read.csv("Desktop/CHN_POPgr.csv")
POPgr <- CHN_POPgr$POPgrowth

POPgrt_r1 <- ts(POPgr[1:105],start=c(1992,2),frequency=4)
plot(POPgrt_r1)
adj_r1 <- seas(POPgrt_r1,x11='',outlier=NULL,forecast.maxlead=10)
summary(adj_r1)
a1 <- series(adj_r1,c('d11','d10','forecast.forecasts'))
a1

POPgrt_r2 <- ts(POPgr[2:106],start=c(1992,3),frequency=4)
plot(POPgrt_r2)
adj_r2 <- seas(POPgrt_r2,x11='',outlier=NULL,forecast.maxlead=10)
summary(adj_r2)
a2 <- series(adj_r2,c('d11','d10','forecast.forecasts'))
a2

POPgrt_r3 <- ts(POPgr[3:107],start=c(1992,4),frequency=4)
plot(POPgrt_r3)
adj_r3 <- seas(POPgrt_r3,x11='',outlier=NULL,forecast.maxlead=10)
summary(adj_r3)
a3 <- series(adj_r3,c('d11','d10','forecast.forecasts'))
a3

POPgrt_r4 <- ts(POPgr[4:108],start=c(1993,1),frequency=4)
plot(POPgrt_r4)
adj_r4 <- seas(POPgrt_r4,x11='',outlier=NULL,forecast.maxlead=10)
summary(adj_r4)
a4 <- series(adj_r4,c('d11','d10','forecast.forecasts'))
a4

POPgrt_r5 <- ts(POPgr[5:109],start=c(1993,2),frequency=4)
plot(POPgrt_r5)
adj_r5 <- seas(POPgrt_r5,x11='',outlier=NULL,forecast.maxlead=10)
summary(adj_r5)
a5 <- series(adj_r5,c('d11','d10','forecast.forecasts'))
a5
library(fBasics)
CN <- read.csv('~/Desktop/CNGDPgr.csv')
US <- read.csv('~/Desktop/USGDPgr.csv')
GRofCN <- CN$growth   # Growth Rate of China
GRofUS <- US$growth   # Growth Rate of the USA

# Monthly Growth Rate of China
pacf(GRofCN)
CN1 <- arima(GRofCN,order=c(1,0,0),method="ML")
CN1
CN2 <- arima(GRofCN,order=c(2,0,0),method="ML")
CN2
CN3 <- arima(GRofCN,order=c(3,0,0),method="ML")
CN3

# Monthly Growth Rate of the USA
pacf(GRofUS)
# Automatically choose AR model
US1 <- auto.arima(GRofUS,d=0,max.q=0,ic='aic')
summary(US1)
library(fBasics)
library(timeDate)
library(timeSeries)
library(tseries)
library(forecast)
CHN_YOYgr <- read.csv("Desktop/CHN_YOYgr.csv")
YOYgr <- CHN_YOYgr$YOYgrowth

tx_r1 <- ts(YOYgr[1:102])
plot(tx_r1)
acf(tx_r1)
pacf(tx_r1)
a1 <- auto.arima(tx_r1)
a1
forecast_r1 <- forecast(a1,h=2)
forecast_r1

tx_r2 <- ts(YOYgr[2:103])
plot(tx_r2)
acf(tx_r2)
pacf(tx_r2)
a2 <- auto.arima(tx_r2)
a2
forecast_r2 <- forecast(a2,h=2)
forecast_r2

tx_r3 <- ts(YOYgr[3:104])
plot(tx_r3)
acf(tx_r3)
pacf(tx_r3)
a3 <- auto.arima(tx_r3)
a3
forecast_r3 <- forecast(a3,h=2)
forecast_r3

tx_r4 <- ts(YOYgr[4:105])
plot(tx_r4)
acf(tx_r4)
pacf(tx_r4)
a4 <- auto.arima(tx_r4)
a4
forecast_r4 <- forecast(a4,h=2)
forecast_r4

tx_r5 <- ts(YOYgr[5:106])
plot(tx_r5)
acf(tx_r5)
pacf(tx_r5)
a5 <- auto.arima(tx_r5)
a5
forecast_r5 <- forecast(a5,h=2)
forecast_r5
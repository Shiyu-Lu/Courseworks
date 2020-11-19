library(rugarch)
library(tseries)
library(fBasics)
library(zoo)
library(FinTS)
library(vars)
library(forecast)
library(fUnitRoots)

data <- read.csv("~/Desktop/CPI.csv")
cpi <- data$CPI

##### ARMA Forecasting #####

tx <- ts(cpi[1:104])
a <- auto.arima(tx)
forecast_ARMA <- forecast(a,h=5,level=c(95))
forecast_ARMA

##### VAR Forecasting #####

# Set the model
et1 <- data[, c("CPI", "M1")]
outv <- VAR(et1, type="const", lag.max=6, ic = c("AIC"))
summary(outv)

# Out-sample prediction
predict(outv, n.ahead = 5, ci=0.95)

##### Impulse Response #####
outirf=irf(outv, impulse = "M1", response = c("M1", "CPI") , n.ahead = 10,
           ortho = FALSE, cumulative = FALSE, ci = 0.95)
outirf
plot(outirf)

##### Variance Decomposition #####
outvdc=fevd(outv, n.ahead=10)
outvdc

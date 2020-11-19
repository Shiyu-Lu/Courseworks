library(rugarch)
library(tseries)
library(fBasics)
library(zoo)
library(FinTS)
Index <- read.csv("~/Desktop/index.csv")
CHGPct <- log(Index$CHGPct[1:1456]+1)   # log returns


### Generate Time Series
dates <- as.Date(Index$tradeDate[1:1456])
r <- zoo(CHGPct,dates)
plot(r)


### Basic Statistical Analysis
n <- length(r)                  # Num of Samples
u <- sum(r)/n                   # Mean
u
e <- sqrt(sum((r-u)^2)/(n-1))   # Std.
e
s <- sum((r-u)^3)/((n-1)*e^3)   # Skewness
s
k <- sum((r-u)^4)/((n-1)*e^4)   # Kurtosis
k
jarque.bera.test(r)             # JB Test


### ACF/PACF Analysis
acf(CHGPct)
pacf(CHGPct)


### Testing for ARCH Effect
ArchTest(r,lag=1)
ArchTest(r,lag=4)
ArchTest(r,lag=8)
ArchTest(r,lag=12)


### Estimate the GARCH model
dist.spec = c("norm")
y = r[,1]

# AR(1)-GARCH(1,1)
mean.spec1 = list(armaOrder=c(1,0))
var.spec1 = list(model="sGARCH", garchOrder=c(1,1))
myspec1 = ugarchspec(mean.model=mean.spec1, variance.model=var.spec1, distribution.model=dist.spec)
out1 = ugarchfit(spec=myspec1, data=y, solver.control=list(trace=0))
out1

# AR(1)-GARCH(1,2)
mean.spec2 = list(armaOrder=c(1,0))
var.spec2 = list(model="sGARCH", garchOrder=c(2,1))
myspec2 = ugarchspec(mean.model=mean.spec2, variance.model=var.spec2, distribution.model=dist.spec)
out2 = ugarchfit(spec=myspec2, data=y, solver.control=list(trace=0))
out2

# AR(1)-GARCH(2,1)
mean.spec3 = list(armaOrder=c(1,0))
var.spec3 = list(model="sGARCH", garchOrder=c(1,2))
myspec3 = ugarchspec(mean.model=mean.spec3, variance.model=var.spec3, distribution.model=dist.spec)
out3 = ugarchfit(spec=myspec3, data=y, solver.control=list(trace=0))
out3

# AR(0)-GARCH(1,1)
mean.spec4 = list(armaOrder=c(0,0))
var.spec4 = list(model="sGARCH", garchOrder=c(1,1))
myspec4 = ugarchspec(mean.model=mean.spec4, variance.model=var.spec4, distribution.model=dist.spec)
out4 = ugarchfit(spec=myspec4, data=y, solver.control=list(trace=0))
out4

# AR(0)-GARCH(1,2)
mean.spec5 = list(armaOrder=c(1,0))
var.spec5 = list(model="sGARCH", garchOrder=c(2,1))
myspec5 = ugarchspec(mean.model=mean.spec5, variance.model=var.spec5, distribution.model=dist.spec)
out5 = ugarchfit(spec=myspec5, data=y, solver.control=list(trace=0))
out5

# AR(0)-GARCH(2,1)
mean.spec6 = list(armaOrder=c(1,0))
var.spec6 = list(model="sGARCH", garchOrder=c(1,2))
myspec6 = ugarchspec(mean.model=mean.spec6, variance.model=var.spec6, distribution.model=dist.spec)
out6 = ugarchfit(spec=myspec6, data=y, solver.control=list(trace=0))
out6


### Model Checking
resi<-residuals(out1,standardize=T)
plot(res,xlab='Date',ylab='std.resi',type='l')
par(mfcol=c(2,2))
acf(resi,lag=24)
acf(resi^2,lag=24)
pacf(resi,lag=24)
pacf(resi^2,lag=24)
Box.test(resi^2,lag=10,type='Ljung')
Box.test(resi^2,lag=15,type='Ljung')
Box.test(resi^2,lag=20,type='Ljung')

### Estimation of Volatility
sig = sigma(out1)
var = sig*sig
colnames(var) = c('var')
colnames(resi) = c('resi')
comp = cbind(dates,r,var,resi)
tail(comp)


### Forecasting
forec <- ugarchforecast(out4,n.ahead=10,n.roll=0)
forec


library(rugarch)
library(FinTS)
library(forecast)
library(qcc)

##### Series Generation #####

## Build a GARCH Model
mean.spec = list(armaOrder = c(1,0), include.mean = FALSE)
var.spec = list(model="sGARCH",garchOrder=c(1,1))
# AR(1) - GARCH(1,1)
spec <- ugarchspec(
  variance.model = var.spec,
  mean.model = mean.spec,
  distribution.model = "norm",
  fixed.pars = list(
    "ar1" = 0.2, "omega" = 0.2, "alpha1" = 0.1, "beta1" = 0.7))

## Monte Carlo Simulation
x_obj <- ugarchpath(
  spec, n.sim = 5000, n.start = 500, rseed = 1000)
show(x_obj)
x <- x_obj@path$seriesSim
plot.ts(x, ylab = "Series x") # Plot of Series

## Volatility Calculation
sig = sigma(x_obj)
var = sig*sig
tail(var)

##### Volatility Prediction #####

## GARCH Model ##

# ACF/PACF Analysis #
acf(x)
pacf(x)

# Tests for ARCH effects #
ArchTest(x,lag=1)
ArchTest(x,lag=4)
ArchTest(x,lag=8)
ArchTest(x,lag=12)

# Estimation of GARCH model #
y <- x[1:4990]
# AR(1)-GARCH(1,1)
mean.spec1 = list(armaOrder=c(1,0))
var.spec1 = list(model="sGARCH", garchOrder=c(1,1))
myspec1 = ugarchspec(mean.model=mean.spec1, variance.model=var.spec1, distribution.model="norm")
out1 = ugarchfit(spec=myspec1, data=y, solver.control=list(trace=0))
out1
# AR(1)-GARCH(1,2)
mean.spec2 = list(armaOrder=c(1,0))
var.spec2 = list(model="sGARCH", garchOrder=c(2,1))
myspec2 = ugarchspec(mean.model=mean.spec2, variance.model=var.spec2, distribution.model="norm")
out2 = ugarchfit(spec=myspec2, data=y, solver.control=list(trace=0))
out2
# AR(1)-GARCH(2,1)
mean.spec3 = list(armaOrder=c(1,0))
var.spec3 = list(model="sGARCH", garchOrder=c(1,2))
myspec3 = ugarchspec(mean.model=mean.spec3, variance.model=var.spec3, distribution.model="norm")
out3 = ugarchfit(spec=myspec3, data=y, solver.control=list(trace=0))
out3

# Model Checking #
resi<-residuals(out1,standardize=T)
plot(resi,xlab='Period',ylab='std.resi',type='l')
par(mfcol=c(2,2))
acf(resi,lag=24)
acf(resi^2,lag=24)
pacf(resi,lag=24)
pacf(resi^2,lag=24)
Box.test(resi^2,lag=10,type='Ljung')
Box.test(resi^2,lag=15,type='Ljung')
Box.test(resi^2,lag=20,type='Ljung')

# Estimation of Volatility #
forec <- ugarchforecast(out1,n.ahead=10,n.roll=0)
forec

sig1 = sigma(forec)
var1 = sig1*sig1

## Equal Weighted Realized Volatility ##
# Use 10 historical data
sig_d10 = data.frame()
for(i in 1:10){
  row <- var[(i+4979):(i+4989)]
  sig_d10 <- rbind(sig_d10, c(sqrt(1/10*sum(row))))
}
names(sig_d10) <- c("sig_d10")

var_d10 = data.frame()
for(i in 1:10){
  row <- (sig_d10$sig_d10[i])^2
  var_d10 <- rbind(var_d10, c(row))
}
names(var_d10) <- c("var_d10")

# Use 20 historical data
sig_d20 = data.frame()
for(i in 1:10){
  row <- var[(i+4969):(i+4989)]
  sig_d20 <- rbind(sig_d20, c(sqrt(1/20*sum(row))))
}
names(sig_d20) <- c("sig_d20")

var_d20 = data.frame()
for(i in 1:10){
  row <- (sig_d20$sig_d20[i])^2
  var_d20 <- rbind(var_d20, c(row))
}
names(var_d20) <- c("var_d20")

# Use 30 historical data
sig_d30 = data.frame()
for(i in 1:10){
  row <- var[(i+4969):(i+4989)]
  sig_d30 <- rbind(sig_d30, c(sqrt(1/30*sum(row))))
}
names(sig_d30) <- c("sig_d30")

var_d30 = data.frame()
for(i in 1:10){
  row <- (sig_d30$sig_d30[i])^2
  var_d30 <- rbind(var_d30, c(row))
}
names(var_d30) <- c("var_d30")

## Exponentially Weighted Moving Average ##
lambda1 = 0.75
lambda2 = 0.85
lambda3 = 0.95

# lambda = 0.75
var_l1 = data.frame()
df1 <- data.frame()
for(i in 1:4990){
  df1 <- rbind(df1, c(lambda1^(4990-i)))
}
for(i in 1:10){
  var_l1 <- rbind(var_l1, 
                  c((1-lambda1)*sum(df1*var[i:(i+4989)])))
}
names(var_l1) <- c("var_l1")

# lambda = 0.85
var_l2 = data.frame()
df2 <- data.frame()
for(i in 1:4990){
  df2 <- rbind(df2, c(lambda2^(4990-i)))
}
for(i in 1:10){
  var_l2 <- rbind(var_l2, 
                  c((1-lambda2)*sum(df2*var[i:(i+4989)])))
}
names(var_l2) <- c("var_l2")

# lambda = 0.95
var_l3 = data.frame()
df3 <- data.frame()
for(i in 1:4990){
  df3 <- rbind(df3, c(lambda3^(4990-i)))
}
for(i in 1:10){
  var_l3 <- rbind(var_l3, 
                  c((1-lambda3)*sum(df3*var[i:(i+4989)])))
}
names(var_l3) <- c("var_l3")

##### Prediction Accuracy Analysis #####
# GARCH
acc1 <- mean(abs(var1/var[4991:5000]-1))
# Equal Weighted Realized Volatility
acc_d10 <- mean(abs(var_d10$var_d10/var[4991:5000]-1))
acc_d20 <- mean(abs(var_d20$var_d20/var[4991:5000]-1))
acc_d30 <- mean(abs(var_d30$var_d30/var[4991:5000]-1))
acc2 <- min(acc_d10,acc_d20,acc_d30)
# Exponentially Weighted Moving Average
acc_l1 <- mean(abs(var_l1$var_l1/var[4991:5000]-1))
acc_l2 <- mean(abs(var_l2$var_l2/var[4991:5000]-1))
acc_l3 <- mean(abs(var_l3$var_l3/var[4991:5000]-1))
acc3 <- min(acc_l1,acc_l2,acc_l3)

##### Change the Sample Size to 3000 #####

## Monte Carlo Simulation
x_obj <- ugarchpath(
  spec, n.sim = 3000, n.start = 500, rseed = 1000)
show(x_obj)
x <- x_obj@path$seriesSim
plot.ts(x, ylab = "Series x") # Plot of Series

## Volatility Calculation
sig = sigma(x_obj)
var = sig*sig
tail(var)

## GARCH Model ##

# ACF/PACF Analysis #
acf(x)
pacf(x)

# Tests for ARCH effects #
ArchTest(x,lag=1)
ArchTest(x,lag=4)
ArchTest(x,lag=8)
ArchTest(x,lag=12)

# Estimation of GARCH model #
y <- x[1:2990]
# AR(1)-GARCH(1,1)
mean.spec1 = list(armaOrder=c(1,0))
var.spec1 = list(model="sGARCH", garchOrder=c(1,1))
myspec1 = ugarchspec(mean.model=mean.spec1, variance.model=var.spec1, distribution.model="norm")
out1 = ugarchfit(spec=myspec1, data=y, solver.control=list(trace=0))
out1
# AR(1)-GARCH(1,2)
mean.spec2 = list(armaOrder=c(1,0))
var.spec2 = list(model="sGARCH", garchOrder=c(2,1))
myspec2 = ugarchspec(mean.model=mean.spec2, variance.model=var.spec2, distribution.model="norm")
out2 = ugarchfit(spec=myspec2, data=y, solver.control=list(trace=0))
out2
# AR(1)-GARCH(2,1)
mean.spec3 = list(armaOrder=c(1,0))
var.spec3 = list(model="sGARCH", garchOrder=c(1,2))
myspec3 = ugarchspec(mean.model=mean.spec3, variance.model=var.spec3, distribution.model="norm")
out3 = ugarchfit(spec=myspec3, data=y, solver.control=list(trace=0))
out3

# Model Checking #
resi<-residuals(out1,standardize=T)
plot(resi,xlab='Period',ylab='std.resi',type='l')
par(mfcol=c(2,2))
acf(resi,lag=24)
acf(resi^2,lag=24)
pacf(resi,lag=24)
pacf(resi^2,lag=24)
Box.test(resi^2,lag=10,type='Ljung')
Box.test(resi^2,lag=15,type='Ljung')
Box.test(resi^2,lag=20,type='Ljung')

# Estimation of Volatility #
forec <- ugarchforecast(out1,n.ahead=10,n.roll=0)
forec

sig1 = sigma(forec)
var1 = sig1*sig1

## Equal Weighted Realized Volatility ##
# Use 10 historical data
sig_d10 = data.frame()
for(i in 1:10){
  row <- var[(i+2979):(i+2989)]
  sig_d10 <- rbind(sig_d10, c(sqrt(1/10*sum(row))))
}
names(sig_d10) <- c("sig_d10")

var_d10 = data.frame()
for(i in 1:10){
  row <- (sig_d10$sig_d10[i])^2
  var_d10 <- rbind(var_d10, c(row))
}
names(var_d10) <- c("var_d10")

# Use 20 historical data
sig_d20 = data.frame()
for(i in 1:10){
  row <- var[(i+2969):(i+2989)]
  sig_d20 <- rbind(sig_d20, c(sqrt(1/20*sum(row))))
}
names(sig_d20) <- c("sig_d20")

var_d20 = data.frame()
for(i in 1:10){
  row <- (sig_d20$sig_d20[i])^2
  var_d20 <- rbind(var_d20, c(row))
}
names(var_d20) <- c("var_d20")

# Use 30 historical data
sig_d30 = data.frame()
for(i in 1:10){
  row <- var[(i+2969):(i+2989)]
  sig_d30 <- rbind(sig_d30, c(sqrt(1/30*sum(row))))
}
names(sig_d30) <- c("sig_d30")

var_d30 = data.frame()
for(i in 1:10){
  row <- (sig_d30$sig_d30[i])^2
  var_d30 <- rbind(var_d30, c(row))
}
names(var_d30) <- c("var_d30")

## Exponentially Weighted Moving Average ##
lambda1 = 0.75
lambda2 = 0.85
lambda3 = 0.95

# lambda = 0.75
var_l1 = data.frame()
df1 <- data.frame()
for(i in 1:2990){
  df1 <- rbind(df1, c(lambda1^(2990-i)))
}
for(i in 1:10){
  var_l1 <- rbind(var_l1, 
                  c((1-lambda1)*sum(df1*var[i:(i+2989)])))
}
names(var_l1) <- c("var_l1")

# lambda = 0.85
var_l2 = data.frame()
df2 <- data.frame()
for(i in 1:2990){
  df2 <- rbind(df2, c(lambda2^(2990-i)))
}
for(i in 1:10){
  var_l2 <- rbind(var_l2, 
                  c((1-lambda2)*sum(df2*var[i:(i+2989)])))
}
names(var_l2) <- c("var_l2")

# lambda = 0.95
var_l3 = data.frame()
df3 <- data.frame()
for(i in 1:2990){
  df3 <- rbind(df3, c(lambda3^(2990-i)))
}
for(i in 1:10){
  var_l3 <- rbind(var_l3, 
                  c((1-lambda3)*sum(df3*var[i:(i+2989)])))
}
names(var_l3) <- c("var_l3")

##### Prediction Accuracy Analysis #####
# GARCH
acc1 <- mean(abs(var1/var[2991:3000]-1))
# Equal Weighted Realized Volatility
acc_d10 <- mean(abs(var_d10$var_d10/var[2991:3000]-1))
acc_d20 <- mean(abs(var_d20$var_d20/var[2991:3000]-1))
acc_d30 <- mean(abs(var_d30$var_d30/var[2991:3000]-1))
acc2 <- min(acc_d10,acc_d20,acc_d30)
# Exponentially Weighted Moving Average
acc_l1 <- mean(abs(var_l1$var_l1/var[2991:3000]-1))
acc_l2 <- mean(abs(var_l2$var_l2/var[2991:3000]-1))
acc_l3 <- mean(abs(var_l3$var_l3/var[2991:3000]-1))
acc3 <- min(acc_l1,acc_l2,acc_l3)

##### Change the Sample Size to 1000 #####

## Monte Carlo Simulation
x_obj <- ugarchpath(
  spec, n.sim = 1000, n.start = 500, rseed = 1000)
show(x_obj)
x <- x_obj@path$seriesSim
plot.ts(x, ylab = "Series x") # Plot of Series

## Volatility Calculation
sig = sigma(x_obj)
var = sig*sig
tail(var)

## GARCH Model ##

# ACF/PACF Analysis #
acf(x)
pacf(x)

# Tests for ARCH effects #
ArchTest(x,lag=1)
ArchTest(x,lag=4)
ArchTest(x,lag=8)
ArchTest(x,lag=12)

# Estimation of GARCH model #
y <- x[1:990]
# AR(1)-GARCH(1,1)
mean.spec1 = list(armaOrder=c(1,0))
var.spec1 = list(model="sGARCH", garchOrder=c(1,1))
myspec1 = ugarchspec(mean.model=mean.spec1, variance.model=var.spec1, distribution.model="norm")
out1 = ugarchfit(spec=myspec1, data=y, solver.control=list(trace=0))
out1
# AR(1)-GARCH(1,2)
mean.spec2 = list(armaOrder=c(1,0))
var.spec2 = list(model="sGARCH", garchOrder=c(2,1))
myspec2 = ugarchspec(mean.model=mean.spec2, variance.model=var.spec2, distribution.model="norm")
out2 = ugarchfit(spec=myspec2, data=y, solver.control=list(trace=0))
out2
# AR(1)-GARCH(2,1)
mean.spec3 = list(armaOrder=c(1,0))
var.spec3 = list(model="sGARCH", garchOrder=c(1,2))
myspec3 = ugarchspec(mean.model=mean.spec3, variance.model=var.spec3, distribution.model="norm")
out3 = ugarchfit(spec=myspec3, data=y, solver.control=list(trace=0))
out3

# Model Checking #
resi<-residuals(out1,standardize=T)
plot(resi,xlab='Period',ylab='std.resi',type='l')
par(mfcol=c(2,2))
acf(resi,lag=24)
acf(resi^2,lag=24)
pacf(resi,lag=24)
pacf(resi^2,lag=24)
Box.test(resi^2,lag=10,type='Ljung')
Box.test(resi^2,lag=15,type='Ljung')
Box.test(resi^2,lag=20,type='Ljung')

# Estimation of Volatility #
forec <- ugarchforecast(out1,n.ahead=10,n.roll=0)
forec

sig1 = sigma(forec)
var1 = sig1*sig1

## Equal Weighted Realized Volatility ##
# Use 10 historical data
sig_d10 = data.frame()
for(i in 1:10){
  row <- var[(i+979):(i+989)]
  sig_d10 <- rbind(sig_d10, c(sqrt(1/10*sum(row))))
}
names(sig_d10) <- c("sig_d10")

var_d10 = data.frame()
for(i in 1:10){
  row <- (sig_d10$sig_d10[i])^2
  var_d10 <- rbind(var_d10, c(row))
}
names(var_d10) <- c("var_d10")

# Use 20 historical data
sig_d20 = data.frame()
for(i in 1:10){
  row <- var[(i+969):(i+989)]
  sig_d20 <- rbind(sig_d20, c(sqrt(1/20*sum(row))))
}
names(sig_d20) <- c("sig_d20")

var_d20 = data.frame()
for(i in 1:10){
  row <- (sig_d20$sig_d20[i])^2
  var_d20 <- rbind(var_d20, c(row))
}
names(var_d20) <- c("var_d20")

# Use 30 historical data
sig_d30 = data.frame()
for(i in 1:10){
  row <- var[(i+969):(i+989)]
  sig_d30 <- rbind(sig_d30, c(sqrt(1/30*sum(row))))
}
names(sig_d30) <- c("sig_d30")

var_d30 = data.frame()
for(i in 1:10){
  row <- (sig_d30$sig_d30[i])^2
  var_d30 <- rbind(var_d30, c(row))
}
names(var_d30) <- c("var_d30")

## Exponentially Weighted Moving Average ##
lambda1 = 0.75
lambda2 = 0.85
lambda3 = 0.95

# lambda = 0.75
var_l1 = data.frame()
df1 <- data.frame()
for(i in 1:990){
  df1 <- rbind(df1, c(lambda1^(990-i)))
}
for(i in 1:10){
  var_l1 <- rbind(var_l1, 
                  c((1-lambda1)*sum(df1*var[i:(i+989)])))
}
names(var_l1) <- c("var_l1")

# lambda = 0.85
var_l2 = data.frame()
df2 <- data.frame()
for(i in 1:990){
  df2 <- rbind(df2, c(lambda2^(990-i)))
}
for(i in 1:10){
  var_l2 <- rbind(var_l2, 
                  c((1-lambda2)*sum(df2*var[i:(i+989)])))
}
names(var_l2) <- c("var_l2")

# lambda = 0.95
var_l3 = data.frame()
df3 <- data.frame()
for(i in 1:990){
  df3 <- rbind(df3, c(lambda3^(990-i)))
}
for(i in 1:10){
  var_l3 <- rbind(var_l3, 
                  c((1-lambda3)*sum(df3*var[i:(i+989)])))
}
names(var_l3) <- c("var_l3")

##### Prediction Accuracy Analysis #####
# GARCH
acc1 <- mean(abs(var1/var[991:1000]-1))
# Equal Weighted Realized Volatility
acc_d10 <- mean(abs(var_d10$var_d10/var[991:1000]-1))
acc_d20 <- mean(abs(var_d20$var_d20/var[991:1000]-1))
acc_d30 <- mean(abs(var_d30$var_d30/var[991:1000]-1))
acc2 <- min(acc_d10,acc_d20,acc_d30)
# Exponentially Weighted Moving Average
acc_l1 <- mean(abs(var_l1$var_l1/var[991:1000]-1))
acc_l2 <- mean(abs(var_l2$var_l2/var[991:1000]-1))
acc_l3 <- mean(abs(var_l3$var_l3/var[991:1000]-1))
acc3 <- min(acc_l1,acc_l2,acc_l3)




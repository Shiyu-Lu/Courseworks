library(rugarch)
library(tseries)
library(fBasics)
library(zoo)
library(FinTS)
library(vars)
library(fUnitRoots)

Index <- read.csv("~/Desktop/Index.csv")

p = trunc((length(Index$Siclose)-1)^(1/3))

df1 <- adfTest(Index$Siclose,lags=p,type=c("ct"))
df1

df2 <- adfTest(Index$SIFclose,lags=p,type=c("ct"))
df2

# SI is Stock Index and SIF is Stock Index Futures
et1 <- Index[, c("Siclose", "SIFclose")]
outv = VAR(et1, p=5, type="const",ic="AIC")

causality(outv, cause="Siclose")
causality(outv, cause="SIFclose")



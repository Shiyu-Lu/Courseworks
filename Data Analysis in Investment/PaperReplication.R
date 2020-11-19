library(pastecs)
library(plotrix)
library(labeling)
library(farver)
library(fUnitRoots)
library(vars)
library(forecast)

### Import the Dataset
data <- read.csv("Desktop/DA/DataSet.csv", header = TRUE)
DATE <- data$Date
CSTIND <- data$CSTIND
USTIND <- data$USTIND
RREL <- data$RREL
DPS <- data$DPS
EPS <- data$EPS
SPLEVEL <- data$SPLEVEL
Rm_Rf <- data$Rm_Rf
d_p <- data$d_p
d_e <- data$d_e
p_e5 <- data$p_e5
d_e5 <- data$d_e5
e_e5 <- data$e_e5
e_p <- data$e_p

##### Table I. Summary Statistics, 1947Q1–1994Q4 #####
df1 <- data.frame(Rm_Rf, RREL, d_p, d_e, p_e5, d_e5, e_e5)
### Correlation Matrix
corr <- cor(df1)
round(corr, 2)
### Univariate Summary Statistics
summ <- stat.desc(df1)
round(summ, 2)
acf(Rm_Rf, lag.max = 1, plot = FALSE)
acf(RREL, lag.max = 1, plot = FALSE)
acf(d_p, lag.max = 1, plot = FALSE)
acf(d_e, lag.max = 1, plot = FALSE)
acf(p_e5, lag.max = 1, plot = FALSE)
acf(d_e5, lag.max = 1, plot = FALSE)
acf(e_e5, lag.max = 1, plot = FALSE)

##### Figure 1. Payout ratio and dividend yield #####
df2 <- data.frame(DATE, d_p, d_e)
twoord.plot(lx = df2$DATE, ly = df2$d_e, rx = df2$DATE, ry = df2$d_p,
            xlab="Quarter", xtickpos=as.numeric(df2$DATE), xticklab=as.character(df2$DATE),
            ylab="d-e", lytickpos=seq(-3,4,by=1),rylab="d-p", type=c('line','line'), lylim = range(-3,4))

##### Figure 2. Scaled prices, dividends, and earnings #####
x <- as.numeric(DATE)
plot(x, y = p_e5, type = "l", col = "red", xlab = "Quarter", 
     ylab = "p_e5", xaxt = "n", yaxt = "n", ylim = c(1, 4))
axis(1, at = DATE, labels = as.character(DATE))
axis(2, ylim = c(1.3, 3.5), las = 1)
par(new=TRUE)
plot(x, y = e_e5, type = "l", col = "blue", xlab = "Quarter", 
     ylab = "", xaxt = "n", yaxt = "n", ylim = c(-5.5, -0.5))
axis(4, ylim = c(-5.5, -0.5), las = 1)
par(new=TRUE)
plot(x, y = d_e5, type = "l", col = "green", xlab = "Quarter", 
     ylab = "", xaxt = "n", yaxt = "n", ylim = c(-5.5, -0.5))
mtext("e_e5, d_e5", side = 4, line = 2.5)

##### Table II. Bivariate Cointegration Tests #####
### Panel A: Regressions of Levels on Levels
p <- log(SPLEVEL, base = exp(1))
d <- log(DPS, base = exp(1))
e <- log(EPS, base = exp(1))
lm1 <- lm(p ~ d)
summary(lm1)
lm2 <- lm(e ~ d)
summary(lm2)
lm3 <- lm(p ~ e)
summary(lm3)
lm4 <- lm(d ~ p)
summary(lm4)
lm5 <- lm(d ~ e)
summary(lm5)
lm6 <- lm(e ~ p)
summary(lm6)
### Panel B: Adjusted Dickey–Fuller Tests
err1 <- residuals(lm1)
err2 <- residuals(lm2)
err3 <- residuals(lm3)
err4 <- residuals(lm4)
err5 <- residuals(lm5)
err6 <- residuals(lm6)
summary(ur.df(d-p, type = "none", lags = 1))
summary(ur.df(d-p, type = "trend", lags = 1))
summary(ur.df(d-p, type = "none", lags = 4))
summary(ur.df(d-e, type = "none", lags = 1))
summary(ur.df(d-e, type = "trend", lags = 1))
summary(ur.df(d-e, type = "none", lags = 4))
summary(ur.df(e-p, type = "none", lags = 1))
summary(ur.df(e-p, type = "trend", lags = 1))
summary(ur.df(e-p, type = "none", lags = 4))

##### Table III. Trivariate Cointegration Test #####
delta_p <- diff(p)
delta_d <- diff(d)
delta_e <- diff(e)
lm7 <- lm(delta_p[2:71] ~ delta_p[1:70] + delta_d[1:70] + delta_e[1:70] +
          d_p[2:71] + d_e[2:71])
summary(lm7)
lm8 <- lm(delta_d[2:71] ~ delta_p[1:70] + delta_d[1:70] + delta_e[1:70] +
            d_p[2:71] + d_e[2:71])
summary(lm8)
lm9 <- lm(delta_e[2:71] ~ delta_p[1:70] + delta_d[1:70] + delta_e[1:70] +
            d_p[2:71] + d_e[2:71])
summary(lm9)

##### Table IV. Forecasting Quarterly Excess Return Using Dividend Yield, Earnings Yield, and Payout #####
df3 <- data.frame("Rm_Rf" = Rm_Rf[72], RREL[72], "d_p" = d_p[72], "e_p" = e_p[72], "d_e" = d_e[72])
lm10 <- lm(Rm_Rf[2:72] ~ d_p[1:71])
summary(lm10)
predict(lm10, df3, se.fit = TRUE)
lm11 <- lm(Rm_Rf[2:72] ~ e_p[1:71])
summary(lm11)
predict(lm11, df3, se.fit = TRUE)
lm12 <- lm(Rm_Rf[2:72] ~ d_p[1:71] + e_p[1:71])
summary(lm12)
predict(lm12, df3, se.fit = TRUE)
lm13 <- lm(Rm_Rf[2:72] ~ d_p[1:71] + d_e[1:71])
summary(lm13)
predict(lm13, df3, se.fit = TRUE)
lm14 <- lm(Rm_Rf[2:72] ~ d_e[1:71])
summary(lm14)
predict(lm14, df3, se.fit = TRUE)
lm15 <- lm(Rm_Rf[2:72] ~ Rm_Rf[1:71] + RREL[1:71] + d_p[1:71] + d_e[1:71])
summary(lm15)
predict(lm15, df3, se.fit = TRUE)

##### Table V. Quarterly Forecasting Equations Using Prices, Dividends, and Earnings #####
lm16 <- lm(Rm_Rf[2:72] ~ Rm_Rf[1:71] + RREL[1:71] + p_e5[1:71] + d_e5[1:71] + e_e5[1:71])
summary(lm16)

##### Table VI. Forecasting Equations for Stocks and Bonds #####
lm17 <- lm(Rm_Rf[2:72] ~ Rm_Rf[1:71] + RREL[1:71] + d_p[1:71] + d_e[1:71])
summary(lm17)

##### Table VII. #####
##### Vector Autoregression (VAR) of Excess Returns, Dividend Yields, and Dividend Payout Ratios #####
lm18 <- lm(RREL[2:72] ~ Rm_Rf[1:71] + RREL[1:71] + d_p[1:71] + d_e[1:71])
summary(lm18)
lm19 <- lm(d_p[2:72] ~ Rm_Rf[1:71] + RREL[1:71] + d_p[1:71] + d_e[1:71])
summary(lm19)
lm20 <- lm(d_e[2:72] ~ Rm_Rf[1:71] + RREL[1:71] + d_p[1:71] + d_e[1:71])
summary(lm20)
a <- predict(lm17, df3, se.fit = TRUE)
b <- predict(lm18, df3, se.fit = TRUE)
c <- predict(lm19, df3, se.fit = TRUE)
d <- predict(lm20, df3, se.fit = TRUE)
total_return <- a$fit[1]

# 1 Year
for(i in range(3)){
  df4 <- data.frame("Rm_Rf" = a$fit[1], "RREL" = b$fit[1], "d_p" = c$fit[1], "d_e" = d$fit[1])
  a <- predict(lm17, df4, se.fit = TRUE)
  b <- predict(lm18, df4, se.fit = TRUE)
  c <- predict(lm19, df4, se.fit = TRUE)
  d <- predict(lm20, df4, se.fit = TRUE)
  total_return <- total_return + a$fit[1]
}
a$fit[1]
a$se.fit[1]
a$residual.scale
total_return

# 2 Year
for(i in range(4)){
  df4 <- data.frame("Rm_Rf" = a$fit[1], "RREL" = b$fit[1], "d_p" = c$fit[1], "d_e" = d$fit[1])
  a <- predict(lm17, df4, se.fit = TRUE)
  b <- predict(lm18, df4, se.fit = TRUE)
  c <- predict(lm19, df4, se.fit = TRUE)
  d <- predict(lm20, df4, se.fit = TRUE)
  total_return <- total_return + a$fit[1]
}
a$fit[1]
a$se.fit[1]
a$residual.scale
total_return

# 3 Year
for(i in range(4)){
  df4 <- data.frame("Rm_Rf" = a$fit[1], "RREL" = b$fit[1], "d_p" = c$fit[1], "d_e" = d$fit[1])
  a <- predict(lm17, df4, se.fit = TRUE)
  b <- predict(lm18, df4, se.fit = TRUE)
  c <- predict(lm19, df4, se.fit = TRUE)
  d <- predict(lm20, df4, se.fit = TRUE)
  total_return <- total_return + a$fit[1]
}
a$fit[1]
a$se.fit[1]
a$residual.scale
total_return

# 5 Year
for(i in range(8)){
  df4 <- data.frame("Rm_Rf" = a$fit[1], "RREL" = b$fit[1], "d_p" = c$fit[1], "d_e" = d$fit[1])
  a <- predict(lm17, df4, se.fit = TRUE)
  b <- predict(lm18, df4, se.fit = TRUE)
  c <- predict(lm19, df4, se.fit = TRUE)
  d <- predict(lm20, df4, se.fit = TRUE)
  total_return <- total_return + a$fit[1]
}
a$fit[1]
a$se.fit[1]
a$residual.scale
total_return

# 10 Year
for(i in range(20)){
  df4 <- data.frame("Rm_Rf" = a$fit[1], "RREL" = b$fit[1], "d_p" = c$fit[1], "d_e" = d$fit[1])
  a <- predict(lm17, df4, se.fit = TRUE)
  b <- predict(lm18, df4, se.fit = TRUE)
  c <- predict(lm19, df4, se.fit = TRUE)
  d <- predict(lm20, df4, se.fit = TRUE)
  total_return <- total_return + a$fit[1]
}
a$fit[1]
a$se.fit[1]
a$residual.scale
total_return

##### Table VIII. #####
##### Vector Autoregression (VAR) of Excess Returns, Prices, Dividends, and Earnings #####
df5 <- data.frame("Rm_Rf" = Rm_Rf[72], RREL[72], "p_e5" = p_e5[72], "d_e5" = d_e5[72], "e_e5" = e_e5[72])
lm21 <- lm(Rm_Rf[2:72] ~ Rm_Rf[1:71] + RREL[1:71] + p_e5[1:71] + d_e5[1:71] + e_e5[1:71])
summary(lm21)
lm22 <- lm(RREL[2:72] ~ Rm_Rf[1:71] + RREL[1:71] + p_e5[1:71] + d_e5[1:71] + e_e5[1:71])
summary(lm22)
lm23 <- lm(p_e5[2:72] ~ Rm_Rf[1:71] + RREL[1:71] + p_e5[1:71] + d_e5[1:71] + e_e5[1:71])
summary(lm23)
lm24 <- lm(d_e5[2:72] ~ Rm_Rf[1:71] + RREL[1:71] + p_e5[1:71] + d_e5[1:71] + e_e5[1:71])
summary(lm24)
lm25 <- lm(e_e5[2:72] ~ Rm_Rf[1:71] + RREL[1:71] + p_e5[1:71] + d_e5[1:71] + e_e5[1:71])
summary(lm25)

a1 <- predict(lm21, df5, se.fit = TRUE)
b1 <- predict(lm22, df5, se.fit = TRUE)
c1 <- predict(lm23, df5, se.fit = TRUE)
d1 <- predict(lm24, df5, se.fit = TRUE)
e1 <- predict(lm25, df5, se.fit = TRUE)
total_return1 <- a1$fit[1]

# 1 Year
for(i in range(3)){
  df6 <- data.frame("Rm_Rf" = a1$fit[1], "RREL" = b1$fit[1], "p_e5" = c1$fit[1],
                    "d_e5" = d1$fit[1], "e_e5" = e1$fit[1])
  a1 <- predict(lm21, df6, se.fit = TRUE)
  b1 <- predict(lm22, df6, se.fit = TRUE)
  c1 <- predict(lm23, df6, se.fit = TRUE)
  d1 <- predict(lm24, df6, se.fit = TRUE)
  e1 <- predict(lm25, df6, se.fit = TRUE)
  total_return1 <- total_return1 + a1$fit[1]
}
a1$fit[1]
a1$se.fit[1]
a1$residual.scale
total_return1

# 2 Year
for(i in range(4)){
  df6 <- data.frame("Rm_Rf" = a1$fit[1], "RREL" = b1$fit[1], "p_e5" = c1$fit[1],
                    "d_e5" = d1$fit[1], "e_e5" = e1$fit[1])
  a1 <- predict(lm21, df6, se.fit = TRUE)
  b1 <- predict(lm22, df6, se.fit = TRUE)
  c1 <- predict(lm23, df6, se.fit = TRUE)
  d1 <- predict(lm24, df6, se.fit = TRUE)
  e1 <- predict(lm25, df6, se.fit = TRUE)
  total_return1 <- total_return1 + a1$fit[1]
}
a1$fit[1]
a1$se.fit[1]
a1$residual.scale
total_return1

# 3 Year
for(i in range(4)){
  df6 <- data.frame("Rm_Rf" = a1$fit[1], "RREL" = b1$fit[1], "p_e5" = c1$fit[1],
                    "d_e5" = d1$fit[1], "e_e5" = e1$fit[1])
  a1 <- predict(lm21, df6, se.fit = TRUE)
  b1 <- predict(lm22, df6, se.fit = TRUE)
  c1 <- predict(lm23, df6, se.fit = TRUE)
  d1 <- predict(lm24, df6, se.fit = TRUE)
  e1 <- predict(lm25, df6, se.fit = TRUE)
  total_return1 <- total_return1 + a1$fit[1]
}
a1$fit[1]
a1$se.fit[1]
a1$residual.scale
total_return1

# 5 Year
for(i in range(8)){
  df6 <- data.frame("Rm_Rf" = a1$fit[1], "RREL" = b1$fit[1], "p_e5" = c1$fit[1],
                    "d_e5" = d1$fit[1], "e_e5" = e1$fit[1])
  a1 <- predict(lm21, df6, se.fit = TRUE)
  b1 <- predict(lm22, df6, se.fit = TRUE)
  c1 <- predict(lm23, df6, se.fit = TRUE)
  d1 <- predict(lm24, df6, se.fit = TRUE)
  e1 <- predict(lm25, df6, se.fit = TRUE)
  total_return1 <- total_return1 + a1$fit[1]
}
a1$fit[1]
a1$se.fit[1]
a1$residual.scale
total_return1

# 10 Year
for(i in range(20)){
  df6 <- data.frame("Rm_Rf" = a1$fit[1], "RREL" = b1$fit[1], "p_e5" = c1$fit[1],
                    "d_e5" = d1$fit[1], "e_e5" = e1$fit[1])
  a1 <- predict(lm21, df6, se.fit = TRUE)
  b1 <- predict(lm22, df6, se.fit = TRUE)
  c1 <- predict(lm23, df6, se.fit = TRUE)
  d1 <- predict(lm24, df6, se.fit = TRUE)
  e1 <- predict(lm25, df6, se.fit = TRUE)
  total_return1 <- total_return1 + a1$fit[1]
}
a1$fit[1]
a1$se.fit[1]
a1$residual.scale
total_return1

##### Table IX. The Importance of Different Forecasting Variables #####
lm26 <- lm(Rm_Rf[2:72] ~ Rm_Rf[1:71] + RREL[1:71] + p_e5[1:71] + d_e5[1:71] + e_e5[1:71])
summary(lm26)
lm27 <- lm(Rm_Rf[2:72] ~ Rm_Rf[1:71] + p_e5[1:71] + d_e5[1:71] + e_e5[1:71])
summary(lm27)
lm28 <- lm(Rm_Rf[2:72] ~ Rm_Rf[1:71] + RREL[1:71] + d_e5[1:71] + e_e5[1:71])
summary(lm28)
lm29 <- lm(Rm_Rf[2:72] ~ Rm_Rf[1:71] + RREL[1:71] + p_e5[1:71] + e_e5[1:71])
summary(lm29)
lm30 <- lm(Rm_Rf[2:72] ~ Rm_Rf[1:71] + RREL[1:71] + p_e5[1:71] + d_e5[1:71])
summary(lm30)
lm31 <- lm(Rm_Rf[2:72] ~ Rm_Rf[1:71] + RREL[1:71])
summary(lm31)
lm32 <- lm(Rm_Rf[2:72] ~ Rm_Rf[1:71] + p_e5[1:71])
summary(lm32)
lm33 <- lm(Rm_Rf[2:72] ~ Rm_Rf[1:71] + d_e5[1:71])
summary(lm33)
lm34 <- lm(Rm_Rf[2:72] ~ Rm_Rf[1:71] + e_e5[1:71])
summary(lm34)

R1 <- predict(lm26, df5, se.fit = TRUE)
R2 <- predict(lm27, df5, se.fit = TRUE)
R3 <- predict(lm28, df5, se.fit = TRUE)
R4 <- predict(lm29, df5, se.fit = TRUE)
R5 <- predict(lm30, df5, se.fit = TRUE)
R6 <- predict(lm31, df5, se.fit = TRUE)
R7 <- predict(lm32, df5, se.fit = TRUE)
R8 <- predict(lm33, df5, se.fit = TRUE)
R9 <- predict(lm34, df5, se.fit = TRUE)
tr1 <- R1$fit[1]
tr2 <- R2$fit[1]
tr3 <- R3$fit[1]
tr4 <- R4$fit[1]
tr5 <- R5$fit[1]
tr6 <- R6$fit[1]
tr7 <- R7$fit[1]
tr8 <- R8$fit[1]
tr9 <- R9$fit[1]

# 1 Year
for(i in range(3)){
  df7 <- data.frame("Rm_Rf" = R1$fit[1], RREL[72], "p_e5" = p_e5[72], "d_e5" = d_e5[72], "e_e5" = e_e5[72])
  R1 <- predict(lm26, df7, se.fit = TRUE)
  tr1 <- tr1 + R1$fit[1]
}
R1$fit[1]
R1$se.fit[1]
R1$residual.scale
tr1

# 5 Year
for(i in range(16)){
  df7 <- data.frame("Rm_Rf" = R1$fit[1], RREL[72], "p_e5" = p_e5[72], "d_e5" = d_e5[72], "e_e5" = e_e5[72])
  R1 <- predict(lm26, df7, se.fit = TRUE)
  tr1 <- tr1 + R1$fit[1]
}
R1$fit[1]
R1$se.fit[1]
R1$residual.scale
tr1

# 1 Year
for(i in range(3)){
  df7 <- data.frame("Rm_Rf" = R2$fit[1], RREL[72], "p_e5" = p_e5[72], "d_e5" = d_e5[72], "e_e5" = e_e5[72])
  R2 <- predict(lm27, df7, se.fit = TRUE)
  tr2 <- tr2 + R2$fit[1]
}
R2$fit[1]
R2$se.fit[1]
R2$residual.scale
tr2

# 5 Year
for(i in range(16)){
  df7 <- data.frame("Rm_Rf" = R2$fit[1], RREL[72], "p_e5" = p_e5[72], "d_e5" = d_e5[72], "e_e5" = e_e5[72])
  R2 <- predict(lm27, df7, se.fit = TRUE)
  tr2 <- tr2 + R2$fit[1]
}
R2$fit[1]
R2$se.fit[1]
R2$residual.scale
tr2

# 1 Year
for(i in range(3)){
  df7 <- data.frame("Rm_Rf" = R3$fit[1], RREL[72], "p_e5" = p_e5[72], "d_e5" = d_e5[72], "e_e5" = e_e5[72])
  R3 <- predict(lm28, df7, se.fit = TRUE)
  tr3 <- tr3 + R3$fit[1]
}
R3$fit[1]
R3$se.fit[1]
R3$residual.scale
tr3

# 5 Year
for(i in range(16)){
  df7 <- data.frame("Rm_Rf" = R3$fit[1], RREL[72], "p_e5" = p_e5[72], "d_e5" = d_e5[72], "e_e5" = e_e5[72])
  R3 <- predict(lm28, df7, se.fit = TRUE)
  tr3 <- tr3 + R3$fit[1]
}
R3$fit[1]
R3$se.fit[1]
R3$residual.scale
tr3

# 1 Year
for(i in range(3)){
  df7 <- data.frame("Rm_Rf" = R4$fit[1], RREL[72], "p_e5" = p_e5[72], "d_e5" = d_e5[72], "e_e5" = e_e5[72])
  R4 <- predict(lm29, df7, se.fit = TRUE)
  tr4 <- tr4 + R4$fit[1]
}
R4$fit[1]
R4$se.fit[1]
R4$residual.scale
tr4

# 5 Year
for(i in range(16)){
  df7 <- data.frame("Rm_Rf" = R4$fit[1], RREL[72], "p_e5" = p_e5[72], "d_e5" = d_e5[72], "e_e5" = e_e5[72])
  R4 <- predict(lm29, df7, se.fit = TRUE)
  tr4 <- tr4 + R4$fit[1]
}
R4$fit[1]
R4$se.fit[1]
R4$residual.scale
tr4

# 1 Year
for(i in range(3)){
  df7 <- data.frame("Rm_Rf" = R5$fit[1], RREL[72], "p_e5" = p_e5[72], "d_e5" = d_e5[72], "e_e5" = e_e5[72])
  R5 <- predict(lm30, df7, se.fit = TRUE)
  tr5 <- tr5 + R5$fit[1]
}
R5$fit[1]
R5$se.fit[1]
R5$residual.scale
tr5

# 5 Year
for(i in range(16)){
  df7 <- data.frame("Rm_Rf" = R5$fit[1], RREL[72], "p_e5" = p_e5[72], "d_e5" = d_e5[72], "e_e5" = e_e5[72])
  R5 <- predict(lm30, df7, se.fit = TRUE)
  tr5 <- tr5 + R5$fit[1]
}
R5$fit[1]
R5$se.fit[1]
R5$residual.scale
tr5

# 1 Year
for(i in range(3)){
  df7 <- data.frame("Rm_Rf" = R6$fit[1], RREL[72], "p_e5" = p_e5[72], "d_e5" = d_e5[72], "e_e5" = e_e5[72])
  R6 <- predict(lm31, df7, se.fit = TRUE)
  tr6 <- tr6 + R6$fit[1]
}
R6$fit[1]
R6$se.fit[1]
R6$residual.scale
tr6

# 5 Year
for(i in range(16)){
  df7 <- data.frame("Rm_Rf" = R6$fit[1], RREL[72], "p_e5" = p_e5[72], "d_e5" = d_e5[72], "e_e5" = e_e5[72])
  R6 <- predict(lm31, df7, se.fit = TRUE)
  tr6 <- tr6 + R6$fit[1]
}
R6$fit[1]
R6$se.fit[1]
R6$residual.scale
tr6

# 1 Year
for(i in range(3)){
  df7 <- data.frame("Rm_Rf" = R7$fit[1], RREL[72], "p_e5" = p_e5[72], "d_e5" = d_e5[72], "e_e5" = e_e5[72])
  R7 <- predict(lm32, df7, se.fit = TRUE)
  tr7 <- tr7 + R7$fit[1]
}
R7$fit[1]
R7$se.fit[1]
R7$residual.scale
tr7

# 5 Year
for(i in range(16)){
  df7 <- data.frame("Rm_Rf" = R7$fit[1], RREL[72], "p_e5" = p_e5[72], "d_e5" = d_e5[72], "e_e5" = e_e5[72])
  R7 <- predict(lm32, df7, se.fit = TRUE)
  tr7 <- tr7 + R7$fit[1]
}
R7$fit[1]
R7$se.fit[1]
R7$residual.scale
tr7

# 1 Year
for(i in range(3)){
  df7 <- data.frame("Rm_Rf" = R8$fit[1], RREL[72], "p_e5" = p_e5[72], "d_e5" = d_e5[72], "e_e5" = e_e5[72])
  R8 <- predict(lm33, df7, se.fit = TRUE)
  tr8 <- tr8 + R8$fit[1]
}
R8$fit[1]
R8$se.fit[1]
R8$residual.scale
tr8

# 5 Year
for(i in range(16)){
  df7 <- data.frame("Rm_Rf" = R8$fit[1], RREL[72], "p_e5" = p_e5[72], "d_e5" = d_e5[72], "e_e5" = e_e5[72])
  R8 <- predict(lm33, df7, se.fit = TRUE)
  tr8 <- tr8 + R8$fit[1]
}
R8$fit[1]
R8$se.fit[1]
R8$residual.scale
tr8

# 1 Year
for(i in range(3)){
  df7 <- data.frame("Rm_Rf" = R9$fit[1], RREL[72], "p_e5" = p_e5[72], "d_e5" = d_e5[72], "e_e5" = e_e5[72])
  R9 <- predict(lm34, df7, se.fit = TRUE)
  tr9 <- tr9 + R9$fit[1]
}
R9$fit[1]
R9$se.fit[1]
R9$residual.scale
tr9

# 5 Year
for(i in range(16)){
  df7 <- data.frame("Rm_Rf" = R9$fit[1], RREL[72], "p_e5" = p_e5[72], "d_e5" = d_e5[72], "e_e5" = e_e5[72])
  R9 <- predict(lm34, df7, se.fit = TRUE)
  tr9 <- tr9 + R9$fit[1]
}
R9$fit[1]
R9$se.fit[1]
R9$residual.scale
tr9



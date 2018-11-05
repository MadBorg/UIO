menn <- c(36.1, 36.3, 36.4, 36.6, 36.6, 36.7, 36.7, 37.0, 36.5, 37.1)
kvinner <- c(36.6, 36.7, 36.8, 36.8, 36.7, 37.0, 37.1, 37.3, 36.9, 37.4)

#a) Lag boksplott som viser fordelingen av observasjonene. Kommennter hva du finner.

boxplot(menn, kvinner, names=c('menn', 'kvinner'))

'
Vi ser fra plottet at menn har litt høyere kroppstemperatur enn menn.
Vi ser også at mennene sin fordeling er sjevt mot lavere verdier,
menns kvinners fordeling er har ingen skjevhet
'

#b) Lag normalfordelingsplott for de to observasjonssettene. Kommennter hva du ser.
limy = c(36,37.5)
par(mfrow=c(1,2))
qqnorm(menn, ylab='(C) temp menn', ylim=limy)
qqline(menn)
qqnorm(kvinner, ylab='(C) temp kinner', ylim=limy)
qqline(kvinner)

'komentar

'
#c) 
Z <- function(sm, sd, n){
  z <- (sm[1] - sm[2])/sqrt(sd[1]**2/n[1] + sd[2]**2/n[2])
  return(z)
}

T <- function(sm, S, N){
  m = N[1]
  n = N[2]
  X = sm[1]
  Y = sm[2]
  sp_square <- (m-1)/(m+n-2) *S[1]**2 + (n-1)/(m+n-2) * S[2]**2
  t <- (X-Y)/sqrt(sp_square*(1/m + 1/n))
  return(t)
}

Nmenn = length(menn)
x = SMmenn = mean(menn)
Smenn = sd(menn)

y = SMkvinner = mean(kvinner)
Skvinner = sd(kvinner)
Nkvinner = length(kvinner)

sm <- c(SMkvinner, SMmenn)
S <- c(Skvinner, Smenn)
n <- c(Nkvinner, Nmenn)

#t.test(menn, kvinner)
#grense = 2.1 #hentet fra A.7 v = 18, alfa = 0.025. probably remove

z <- Z(sm, S, n); t <- Z(sm, S, n)
v1 = sum(n)-2
P = 2*0.011 #hentet fra A.7, v = 18, 2.5 siden det er største tall i tabellen under 2.59

varT <- (m-1)/(m+n-2) *S[1]**2 + (n-1)/(m+n-2) * S[2]**2

CIT <- function(sm, n, S, alfa, v){
  #same sd
  m = n[1]
  n = n[2]
  X = sm[1]
  Y = sm[2]
  varT <- (m-1)/(m+n-2) *S[1]**2 + (n-1)/(m+n-2) * S[2]**2
  ci <- X - Y + c(1,-1)*qt(alfa/2, v)*sqrt(varT*(1/m + 1/n))
  return(sort(ci))
}

CIT2sd <- function(sm, N, S, alfa,v){
  #diff sd
  m = N[1]
  n = N[2]
  X = sm[1]
  Y = sm[2]
  ci = X - Y + c(-1,1)*qt(alfa/2, v)*sqrt(sp_square*(1/m + 1/n))
  return(sort(ci))
}
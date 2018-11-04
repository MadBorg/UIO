set.seed(11)
mu = 1
sigma = 1
n = 8
ant_setts = 1000
Clvl = 0.975 #konfidens nivaa

simulation <- function(mu, sigma, n, ant_sets, Clvl){
  simres=numeric(0)
  for (i in 1:ant_setts) {
    x=rnorm(n,mu,sigma)
    muhat=mean(x)
    sdx=sd(x)
    
    muCIt = muhat +c(-1,1)*qt(Clvl,df=n-1)*sdx/sqrt(n) #CI for  my
    sdxCIKJI = sdx*sqrt((n-1)/qchisq(c(Clvl,1-Clvl), n-1))#CI for sigma
    
    nyres = c(muhat,sdx, muCIt,sdxCIKJI)
    simres=rbind(simres,nyres)
  }
  
  muCItinInterval= sum((simres[,3]<1)*(1<simres[,4]));
  sdxCIKJIinIntervall = sum((simres[,5]<1)*(1<simres[,6])); 
  c(muCItinInterval, sdxCIKJIinIntervall)
}
print(simulation(mu, sigma, n, ant_sets, Clvl))
#d

n = c(30,200)
for (i in n){
  print(simulation(mu, sigma, i, ant_sets, Clvl))
}
#e
n = 8
my = 1
sigma= 1
exponent <- function(mu, sigma, n, ant_sets, Clvl){
  simres=numeric(0)
  for (i in 1:ant_setts) {
    x=rexp(n,rate=1)
    muhat=mean(x)
    sdx=sd(x)
    
    muCIt = muhat +c(-1,1)*qt(Clvl,df=n-1)*sdx/sqrt(n) #CI for  my
    sdxCIKJI = sdx*sqrt((n-1)/qchisq(c(Clvl,1-Clvl), n-1))#CI for sigma
    
    nyres = c(muhat,sdx, muCIt,sdxCIKJI)
    simres=rbind(simres,nyres)
  }
  
  muCItinInterval= sum((simres[,3]<1)*(1<simres[,4]));
  sdxCIKJIinIntervall = sum((simres[,5]<1)*(1<simres[,6])); 
  c(muCItinInterval, sdxCIKJIinIntervall)
}
exponent(mu, sigma, n, ant_sets, Clvl)
#f
n  = c(30,200)
for (i in n){
  print(exponent(mu, sigma, i, ant_sets, Clvl))
}
#set.seed(123)
n=8

simres=numeric(0)
for (sim in 1:1000){
  x=rnorm(n,1,1)
  muhat=mean(x)
  sdx=sd(x)
  KJIKI=sdx*(sqrt((n-1)/qchisq(c(0.975,0.025),n-1)))
  TKI= muhat +c(-1,1)*qt(0.975,n-1)*sdx/sqrt(n)
  nyres=c(muhat,sdx, KJIKI,TKI)
  simres=rbind(simres,nyres)
}


anttreffKJIKI = sum((simres[,3]<1)*(1<simres[,4])); anttreffKJIKI
anttreffTKI = sum((simres[,5]<1)*(1<simres[,6])); anttreffTKI

#-----------
n=8
# Trekker 100 sett av data fra N(1,sigma)
sigma = 1
simres=numeric(0)
for (sim in 1:100){
  x=rnorm(n,1,sigma)
  muhat=mean(x)
  normKI=muhat+c(-1,1)*1.96*sigma/sqrt(n)
  nyres=c(muhat,normKI)
  simres=rbind(simres,nyres)
}

# Trekker 1000 sett av data fra N(1,sigma)
simres=numeric(0)
for (sim in 1:1000){
  x=rnorm(n,1,sigma)
  muhat=mean(x)
  normKI=muhat+c(-1,1)*1.96*sigma/sqrt(n)
  sigmaKi = sigma*sqrt((n-1))/qchisq(c(.95, .05),n-1)
  nyres=c(muhat,normKI)
  simres=rbind(simres,nyres)
}
anttreff=sum((simres[,2]<1)*(sigma<simres[,3]))
anttreff;anttreff/1000
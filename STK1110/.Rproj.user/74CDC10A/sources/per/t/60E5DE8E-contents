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
#Plotter 100 konfidensintervall.
plot(simres[1,2:3],c(1,1),ylim=c(0,101),type="l",xlim=c(min(simres[,2]),max(simres[,3])),xlab="KI",ylab="Sim.no.")
for (sim in 2:100) lines(simres[sim,2:3],c(sim,sim))
points(simres[,1],1:100,pch="*")
abline(v=14)

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

init = c(249,254, 243, 268, 253, 269, 287, 241, 273, 306, 303, 280, 260, 256, 278, 344, 304, 283, 310)
#a
#finner estimert forventing, til de uavhengige og stokastiske veridene
n = length((init))
mu = 1/n * sum(init); #mean(init)

#finner forventingsrett estimert standardavvik.
S = sdinit = sqrt(1/(n-1)*sum((init - mu)^2))#sd(init)

#finner 90% CI for mu
tCI = mu +c(1,-1)*qt(0.05,df=n-1)*(S/sqrt(n))

#b
#sigma estimeres til S
sigma = S

#finner 90% CI for sigma
chiCI = S*sqrt(18/qchisq(c(0.95,1-0.95), n-1))

#c
#plotter dataen for ? se om det er tilnemet en normallinjes
qqnorm(init)
qqline(init)







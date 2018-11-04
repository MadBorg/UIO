indata = c(15.0, 10.0, 10.0, 15.0, 25.0, 7.0, 3.0, 8.0, 10.0, 10.0, 11.0, 7.0, 5.0, 15.0, 7.5, 7.5, 12.0, 7.0, 10.5, 6.0, 10.0, 7.5)
n = length(indata)

#a) t 95 CD

tCD = sort(mean(indata)+c(1,-1)*qt(0.975,n-1)*sd(indata)/sqrt(n)); tCD

#b) normal plot, normal?
qqnorm(indata);qqline(indata)

#c) boot 999 means

n_boots = 1:1000
gjtempboot = numeric(0)
for (i in n_boots){
bootsamp = sample(indata, replace = T)
gjtempboot[i] = mean(bootsamp) 
}
summary(gjtempboot)
sd(gjtempboot)

#d) use SD (c) to get a 95% CD
sort(mean(indata)+c(1,-1)*qt(0.975,n-1)*sd(gjtempboot)/sqrt(n))
hist(gjtempboot,nclass=20)

#f)
alpha = 0.95
gjtbSorted = sort(gjtempboot)
gjtIndexAlpha = c((1-alpha)/2, alpha +(1-alpha)/2)*length(n_boots)
gjtbSorted[gjtIndexAlpha]

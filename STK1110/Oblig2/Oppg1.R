y =menn <- c(36.1, 36.3, 36.4, 36.6, 36.6, 36.7, 36.7, 37.0, 36.5, 37.1)
x = kvinner <- c(36.6, 36.7, 36.8, 36.8, 36.7, 37.0, 37.1, 37.3, 36.9, 37.4)

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


#c) 
alfa = 0.05
nx = length(kvinner)
ny = length(menn)
Sx = sd(x)
Sy = sd(y)
sp_square = ((nx-1)*Sx**2 + (ny-1)*Sy**2)/(nx+ny-2)
t_obs = abs((mean(kvinner)-mean(menn)))/sqrt(sp_square*(1/nx + 1/ny))
t_lim = qt(1-alfa/2,nx-1)
P = 2* pt(t_obs, nx+ny-2)
t_CI = mean(x) - mean(y) + c(1,-1)*qt(alfa/2, nx+ny-2)*sqrt(sp_square*(1/nx + 1/ny))

#d)
t_obs_NonEqualVar = abs(mean(kvinner)-mean(menn))/sqrt(Sx**2**2/nx + Sy**2/ny)
v = round((Sx**2/nx + Sy**2/ny)**2/((Sx**2/nx)**2/(nx-1) + (Sy**2/ny)**2/(ny-1)))
P = 2* pt(t_obs_NonEqualVar, v)
#e) Utled og gjennomfør en F-test for ˚a sjekke om det er noen grunn til ˚a p˚ast˚a at
#variansene er forskjellige. Sjekk mot var.test() i R.

f = Sx**2/Sy**2
CIf = qf(c(alfa/2, 1-alfa/2),nx-1,ny-1)

path="https://www.uio.no/studier/emner/matnat/math/STK1110/data/plastic.txt"
plast=read.table(path,header=T)


y =Strength = plast[, 'Strength']
x1 = Temp = plast[, 'Temperature']
x2 = Pressure = plast[, 'Pressure']

par(mfrow=c(2,2))
qqnorm(Strength, ylab='Strength')
qqline(Strength)
#Plottet ser tilnermet normalfordelt ut.


boxplot(Strength, name='Strength')
#Boxplotet viser en poseti sjevhet


qqplot(x1,y, xlab='Temp')
#qqpline(y)
qqplot(x2,y, xlab='Pressure')

#Det ser ut som y er mer gjevnt avengig av Temp, mens det er en stor endring når Pressure er 12 som kan vise til at Styrken til plasten øker betydlig når trykket er 12.
#Dette kan ytteliger vises med en korrelasjonskoefisient.

#b)Regresjon, y(x1)

x_bar = c(mean(x1), mean(x2))
y_bar = mean(y)


#b1_hat = sum((x1-x_bar[1])*(y-mean(y)))/sum((x1-x_bar[1])**2) s
#a1_hat = y_bar-b1_hat*x_bar[1]

#b2 = sum((x2-x_bar[2])*(y-mean(y)))/ sum((x-x_bar[1])**2)

l.lm = lm(y~x1)
plot(x1, y, xlab='Temp',ylab='Strength')
abline(l.lm)
# ser tilsynelatende ut til å ha en korrelasjon

#c)
alfa = 0.05
n = length(y)
sb = sd(y)
Sxx = sd(x1)
b1CI = 





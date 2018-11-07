path="https://www.uio.no/studier/emner/matnat/math/STK1110/data/plastic.txt"
plast=read.table(path,header=T)


y =Strength = plast[, 'Strength']
x1 = Temp = plast[, 'Temperature']
x2 = Pressure = plast[, 'Pressure']

par(mfrow=c(2,2))
qqnorm(Strength, ylab='Strength')
qqline(Strength)

boxplot(Strength, name='Strength')

qqplot(x1,y, xlab='Temp')
#qqpline(y)
qqplot(x2,y, xlab='Pressure')


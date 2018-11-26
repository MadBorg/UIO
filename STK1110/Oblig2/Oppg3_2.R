path="https://www.uio.no/studier/emner/matnat/math/STK1110/data/plastic.txt"
plast=read.table(path,header=T)


y =Strength = plast[, 'Strength']
x1 = Temp = plast[, 'Temperature']
x2 = Pressure = plast[, 'Pressure']

#b)

l.lm = lm(y~x1)
plot(x1, y, xlab='Temp',ylab='Strength')
abline(l.lm)

beta1X1hat = coefficients(l.lm)[2]
beta0x1hat = coefficients(l.lm)[1]

#c)
alfa = 0.05
n = length(y)
#Sxx1 = sd(x1)
Sxx1 = sum(x1^2)- (sum(x1)^2)/n
SSE = sum((y - (beta0x1hat + beta1X1hat*x1))^2)
s_square = SSE/(n-2)
s = sqrt(s_square)
S_beta1x1hat = s/sqrt(Sxx1)
CI_beta1x1 = beta1X1hat + c(1,-1)*qt(alfa/2,n-2) * S_beta1x1hat

#d

x1_star = c(210, 240, 270)
y_hat = beta0x1hat+beta1X1hat*x1_star
S_y_hat = s*sqrt(1/n + (x1_star - mean(x1))^2/Sxx1)

CI_y_hat_pluss = y_hat + qt(alfa/2, n-2)*S_y_hat
CI_y_hat_minus = y_hat - qt(alfa/2, n-2)*S_y_hat
CI_y_hat = cbind(CI_y_hat_pluss, CI_y_hat_minus)

PI_y_hat_pluss = y_hat + qt(alfa/2, n-2)*sqrt(s_square +S_y_hat^2)
PI_y_hat_minus = y_hat - qt(alfa/2, n-2)*sqrt(s_square +S_y_hat^2)
PI_y_hat = cbind(PI_y_hat_pluss, PI_y_hat_minus)

#e
s = sqrt(sum((y-mean(y))^2)*1/(n-1))
PI_pred = mean(y)+ c(1,-1)*qt(alfa/2,n-1)*s*sqrt(1+1/n)

#f) b)

l.lm = lm(y~x2)
plot(x2, y, xlab='Pressure',ylab='Strength')
abline(l.lm)

beta1X2hat = coefficients(l.lm)[2]
beta0x2hat = coefficients(l.lm)[1]

#f) c)
alfa = 0.05
n = length(y)
#Sxx2 = sd(x2)
Sxx2 = sum(x2^2)- (sum(x2)^2)/n #vet ikke hvorfor dette blir ulikt linjen over.
SSE2 = sum((y - (beta0x2hat + beta1X2hat*x2))^2)
s_square2 = SSE2/(n-2)
s2 = sqrt(s_square2)
S_beta1x2hat = s2/sqrt(Sxx2)
CI_beta1x2 = beta1X2hat + c(1,-1)*qt(alfa/2,n-2) * S_beta1x2hat

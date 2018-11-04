#4
df2 = read.csv('https://www.uio.no/studier/emner/matnat/math/STK1110/data/exe7_04.txt', sep='\t')
head(df2)
dim(df2)
males = df2[df2$mf == 'male', ]$VERBIQ
females = df2[df2$mf == 'female', ]$VERBIQ

n1 = length(males) 
n2 = length(females)

#a E(Xb - Yb) = E(Xb) - E(Yb) = my1 - my2

Mean_males = 1/n1 *sum(males)
Mean_females = 1/n2 *sum(females)
Mean_males-Mean_females

mean(males) - mean(females)

#b V(Xb - Yb) = V(Xb) + V(Yb) = sigma1^2 / n1 + sigma2^2 / n2
  #my solution
S_square_Males= sum((males - Mean_males)^2)/(n1-1)
S_square_Females= sum((females - Mean_females)^2)/(n2-1)
vars_my = S_square_Males/n1 + S_square_Females/n2
sqrt(vars_my) #estiamated square errror

  #not my solution
vars = sd(males)^2/length(males) + sd(females)^2/length(females)
sqrt(vars)

#c
  #my solution
S_males = sqrt(S_square_Males)
S_females = sqrt(S_square_Females)

S_males/S_females

  #not my solution
sd(males)/sd(females)


#d  V(X - Y) = V(X) + V(Y) = sigma1^2 + sigma2^2
  #my solution
S_square_Males + S_square_Females


  #not my solution
sd(males)^2 + sd(females)^2



#6
df3 = read.csv('https://www.uio.no/studier/emner/matnat/math/STK1110/data/exe7_06.txt')
df3
flow = df3$flow
flow
#my common data
n_flow = length(flow)

# a
  #my solution
x_m = log(flow)
my = sum(x_m)/n_flow
var_flow = sum((x_m - my)^2)/(n_flow-1)
sd_mine = sqrt(var_flow); sd_mine

  #not my solution
x = log(flow)
mu = mean(x)
mu
sigma = sd(x)
sigma

#b mean of log-normal is exp(mu + sigma^2/2)
  #my solution
exp(my + var_flow/2)

  #not my solution
exp(mu + sigma^2/2)


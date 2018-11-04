%inndata
K = 400000;
theta = 3;
n = 10000;
%getting n uniformed u between 0 and 1 
u = unifrnd(0,1,[1 n]);

x = K./(nthroot(1-u,theta));
%finding the mean
mean(x)
%finding the median
median(x)
hold on
%d) plotting the histogram 
histogram(x,"normalization","pdf","binlimits", [400000 2000000])
X = (400000:0.1:2000000);
%e) printer tetheten til Paretofordelingen
line(X,theta*(K.^theta)*(X.^(-theta-1)), 'color', 'red')
hold off

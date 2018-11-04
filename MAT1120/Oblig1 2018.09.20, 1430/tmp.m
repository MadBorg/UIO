

p3 = [1 2 3 4]%[a3 a2 a1 a0] = a3*x^3+a2*x^2+a1*x+a0
pt = [1 3 -1 -3 -1 1]


function [xvals,muvals]=powermethod(A,x,numtimes,tol)
xvals = [];
muvals = [];
for r=1:numtimes
    x = A*x;
    [maxval,maxnr]=max(abs(x));
    mu = x(maxnr);
    x = (1/mu)*x;
    % Kunne her brukt R = x’*A*x/(x’*x) i stedet for mu
    muvals = [muvals mu];
    xvals = [xvals x];
    error = max(abs(A*x-mu*x));
    if error<tol
    break;
    end
end

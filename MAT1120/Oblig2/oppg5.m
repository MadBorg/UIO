A = [1 1 1 1 1 1
     1 2 3 4 5 6
     1 3 6 10 15 21
     1 4 10 20 35 56
     1 5 15 35 70 126
     1 6 21 56 126 252];
 polyA = poly(A);%finner det karakteristiske polynomet til A
 
rotEst = sdrot(polyA)
rot = max(eig(A))

relerror = (abs(rot-rotEst))/abs(rot)


 
 function rot = sdrot(p)
    numtimes = 100;
    tol = 1e-6;
    n = length(p)-1;
  
    x = rand(n,1);
  
    A = zeros(n,n);
    for i = 1:n
        A(end,i) = -p(n+2-i);
        if i > 1
          A(i-1,i)= 1;
        end
    end
    
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
            rot = muvals(end);
            break;
        end
    
    end
    if  error>tol
        sprintf('error = %f > %f = tol, mu = %f ', [error, tol, muvals(end)])
        rot = muvals(end);
    end

    %sprintf('loop ended without giving value with error less than %f, lambda = %f', [tol, muvals(end)])
end

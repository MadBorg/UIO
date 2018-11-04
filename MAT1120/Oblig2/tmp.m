

eigfunc(0)




function num = eigfunc(t)
    v1 = [1;1;1];
    v2 = [1;2;4];
    v3 = [1;-1;1];
    
    num = -v1*exp(t)+v2*exp(2*t)-v3*exp(-t);
end


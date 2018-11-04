F = []
F(1) = 1;
F(2) = 1;
x = 0;
while x < 10
    z = F(1) + F(2)
    F(1) = F(2);
    F(2) = z;
    
    x = x + 1;
end

%a)
a11 = input('a:');
a12 = input('b:');
a21 = input('c:');
a22 = input('d:');

a = 1;
b = -a11*a22;
c = (a11*a22) - (a12*a21);

x1 = (-b + sqrt((-b)^2 - 4*a*c)) / 2*a;
x2 = (-b - sqrt((-b)^2 - 4*a*c)) / 2*a;
%b)
syms x y

eqn1 = a11*x + a12*y - x1*x == 0
eqn2 = a21*x + a22*y - x1*y == 0
eqn12 = a11*x + a12*y - x2*x == 0
eqn22 = a21*x + a22*y - x2*y == 0

%4:20IN THE EVENIN'
%August Reierstad Haugen
if (a11-x1) ~= 0
    x = solve(eqn1, x)
elseif a21 ~= 0
    x = solve(eqn2, x)
elseif a22 ~= 0
    y = solve(eqn1, y)
else
    y = solve(eqn2, y)
end



%solve(eqn1, eqn2)
%solve(eqn12, eqn22)


rref(a)



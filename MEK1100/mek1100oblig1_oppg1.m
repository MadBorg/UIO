n = 1:3

theta1 = 0:pi/6
theta2 = pi/4
theta3 = pi/3

v0 = 2%try different values
g = 9.81 %try different values

t = linspace(0,1,10000)
hold on
plot(t, tan(theta1)*t - tan(theta)*t.^2)
plot(t, tan(theta2)*t - tan(theta)*t.^2)
plot(t, tan(theta3)*t - tan(theta)*t.^2)
hold off


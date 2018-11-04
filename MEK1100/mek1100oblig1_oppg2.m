start = -3
stop = 3
inc = 0.5

[x,y] = meshgrid(start:inc:stop);
vx = x.*y;
vy = y;

quiver(x,y,vx,vy,1)
axis equal

f = y - log(abs(x));

c = start:inc:stop
b =zeros((size(c)))
hold on
contour(x,y,f)
plot(c,b)

hold off


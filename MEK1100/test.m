[x,y] = meshgrid(-1:0.5:5);

vx = -3*y;
vy = 3*x;
hold on
quiver(x,y,vx,vy,1)
f = 1/2*3*(x^2+y^2);
contour(x,y,f)
hold of


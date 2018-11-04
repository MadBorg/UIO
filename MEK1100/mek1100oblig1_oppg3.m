[x,y] = meshgrid(-1:0.5:5)

vx = -sin(x)
vy = sin(y)
f = cos(x)*cos(y)
hold on
quiver(x,y,vx,vy,1)
contour(x,y,f)
axis equal
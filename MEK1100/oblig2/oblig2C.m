load("data.mat")

dimensions = [
    "name", "y", "x", "points";
    "u: ", size(u), numel(u); 
    "v :", size(v), numel(v);
    "x: ",size(x), numel(x);
    "xit: ", size(xit), numel(xit);
    "y: ", size(y), numel(y);
    "yit: ", size(yit), numel(yit)
    ]

%b)
z = sqrt(u^2+v^2)
contourf(x,y,z)


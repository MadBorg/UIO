
%a)

load("data.mat");

%sjekker at alle data stemmer 
%sjekker dimensonene, size for kolonnene og nummel for radene
%antal "points" er antall dataverdier som er i en matrise
dimensions = [
    "name", "kolonner", "Rader", "points";
    "u: ", size(u), numel(u); 
    "v :", size(v), numel(v);
    "x: ",size(x), numel(x);
    "xit: ", size(xit), numel(xit);
    "y: ", size(y), numel(y);
    "yit: ", size(yit), numel(yit)
    ]

%sjekker at xy flaten er gjevnt fordelt med 0.5 i delta
DIF = 0.5;
count = [0 0];
b = size(x);
for n = 1:b(1)
    h = x(1,1) - DIF;
    count(1) = count(1) + 1;
    count(2) = 0;
    for j = x(1,:)
        count(2) = count(2) + 1;
        %skjekker om alle aksepunktene er gjevnt fordelt i x matrisen
        if abs(h - j) ~= DIF
            statment = 'x: aksene er ikke gjevnt fordelt med angitt DIF';
            count;
            break    
        end
        h = j;
    end
end

g = size(y);
for n = 1:b(2)
    h = y(1,1) - DIF;
    count(2) = count(2) + 1;
    count(1) = 0;
    for j = y(:,1)
        count(1) = count(1) + 1;
        %skjekker om alle aksepunktene er gjevnt fordelt i x matrisen
        if abs(h - j) ~= DIF
            statment = 'y: aksene er ikke gjevnt fordelt med angitt DIF';
            count;
            break    
        end
        h = j;
    end
end


%4)
%finner diameterene av sylynderen
diameter = abs(y(1,1) - y(end,end));

%b)

figure
%Z deffineres som hastigheten
Z = sqrt(u.^2 + v.^2);

subplot(2,1,1)
hold on
%plotter et contur plott av hastigheten Z, har bare veridene 600-4000 siden
%jeg vil vise kontraster i gassen
contourf(x,y,Z, 600:500:4000)
%plotter inn skillelinjen
plot(xit,yit, '*r');
%plotter boksene
plot_box(x,y);
%vieser verider for fargene
colorbar()
hold off
title('gass konturplott')

subplot(2,1,2)
hold on
%plotter et contur plott av hastigheten Z, har bare veridene -100-600 siden
%jeg vil vise kontraster i vesken
contourf(x,y,Z, -100:40:600)
plot(xit,yit, '*r');
plot_box(x,y);
colorbar()
hold off
title('Vekse konturplott')


%c)
figure
hold on
%plotter et pilplott av u og v inne i boksene
%definerer en konstant som skalerer pilene
scale = 0.7;

%box1
subplot(3,1,1)
quiver(x(160:170,35:70), y(160:170,35:70), u(160:170,35:70), v(160:170,35:70), scale)
title('160:170, 35:70')
%box23
subplot(3,1,2)
quiver(x(85:100,35:70), y(85:100,35:70), u(85:100,35:70), v(85:100,35:70), scale)
title('85:100, 35:70')
%box3
subplot(3,1,3)
quiver(x(50:60,35:70), y(50:60,35:70), u(50:60,35:70), v(50:60,35:70), scale)
title('50:60, 35:70')

%title('farten sqrt(u^2+v^2)')


figure
hold on
% %d)
%regner utr divergensen og plotter et contour polott av dataen
div = divergence(x,y,u,v);
%setter poe grenser siden jeg vil ha kontroll over kontrasten
contourf(x,y,div, -2000:500:1500);
colorbar()
plot(xit,yit, '*r');
plot_box(x,y);
title('divergensen')
hold off

% %e)
figure
hold on
%regner ut curl verdier av u v, i x,y koordinatene
CURL = curl(x,y,u,v);
contourf(x,y, CURL, -2000:200:1500)
colorbar()
plot(xit,yit, '*r');
plot_box(x,y);
title('curl')

figure
%plotter stromlinjer med en for lokke, definerer en start og stop, tar med
%2 ekstra punkter for sikkerhets skjyld, p er en faktor som bestememr hvor
%mange linjer det skal veare
start = -51;
stop = 51;
p = 3;
lidste = start:p:stop;

for i=1:(floor(abs(start-stop)/p))
    
    streamline(x,y,u,v,0,lidste(i));
    ylim([start stop]);
    hold on
end

plot(xit,yit, '*r');
plot_box(x,y);
title('streamlines')


%)f

%)curveintegral, greens
%box1
CurvInt1 = (-sum(v(160:170,35)) + sum(u(160,35:70)) + sum(v(160:170,70)) - sum(u(170,35:70)))*0.5;
%box2
CurvInt2 = (-sum(v(85:100,35)) + sum(u(85,35:70)) + sum(v(85:100,70)) - sum(u(100,35:70)))*0.5;
%box3
CurvInt3 = (-sum(v(50:60,35)) + sum(u(50,35:70)) + sum(v(50:60,70)) - sum(u(60,35:70)))*0.5;
CurvInt = [CurvInt1 CurvInt2 CurvInt3]

%flateintegral, stokes
%box1
sto1 = sum(CURL(160:170,:));
stokes1 = sum(sto1(35:70))*0.5;
%box2
sto2 = sum(CURL(85:100,:));
stokes2 = sum(sto2(35:70))*0.5;
%box3
sto3= sum(CURL(50:60,:));
stokes3 = sum(sto3(35:70))*0.5;
stokes = [stokes1 stokes2 stokes3]

DifCurvIntStokes = abs(CurvInt - stokes)



%g
%curveintegral gauss
%box1
gauss1 = (-sum(v(160:170,35)) - sum(u(160,35:70)) + sum(v(160:170,70)) + sum(u(170,35:70)))*0.5;
%box2
gauss2 = (-sum(v(85:100,35)) - sum(u(85,35:70)) + sum(v(85:100,70)) + sum(u(100,35:70)))*0.5;
%box3
gauss3 = (-sum(v(50:60,35)) - sum(u(50,35:70)) + sum(v(50:60,70)) + sum(u(60,35:70)))*0.5;
gauss = [gauss1 gauss2 gauss3]









%funksjoner
function [x,y]= plot_box(x,y);
%plotter boksene
line([x(160,35) x(170,35)] , [y(160, 35) y(170, 35)],'color', 'black')
line([x(160,35) x(160,70)] , [y(160, 35) y(160, 70)],'color', 'red')
line([x(160,70) x(170,70)] , [y(160, 70) y(170, 70)],'color', 'green')
line([x(170,35) x(170,70)] , [y(170, 35) y(170, 70)],'color', 'blue')

line([x(85,35) x(100,35)] , [y(85, 35) y(100, 35)],'color', 'black')
line([x(85,35) x(85,70)] , [y(85, 35) y(85, 70)],'color', 'red')
line([x(85,70) x(100,70)] , [y(85, 70) y(100, 70)],'color', 'green')
line([x(100,35) x(100,70)] , [y(100, 35) y(100, 70)],'color', 'blue')

line([x(50,35) x(60,35)] , [y(50,35) y(60, 35)],'color', 'black')
line([x(50,35) x(50,70)] , [y(50,35) y(50,70)],'color', 'red')
line([x(50,70) x(60,70)] , [y(50,70) y(60,70)],'color', 'green')
line([x(60,35) x(60,70)] , [y(60,35) y(60,70)],'color', 'blue')
end







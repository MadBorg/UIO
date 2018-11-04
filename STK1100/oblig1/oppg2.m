%2c
% for aa plotte punktsannsynligheten trengs, den kumulative fordelingen:

    % for å regne ut den kumulative fordelingen trengs, den ettaarlige doedssannsynlighetene:
    
        %finner den ettaarlige doedssannsynlighetene
qk = dod/1000;

    %finner saa den kumulative fordelingen
Fx = 1-cumprod(1-qk(35+1:107));   

% Beregner punktsannsynlighetne
px = Fx -[0;Fx(1:71)];

%plotter punktsannsynlighetene
bar(0:72,px)
xlabel("Gjennstående levetid")
title("Punktsannsynlighet")

%2f
SUM = 0;
for x = 35:71
    SUM = SUM + (1/1.03)^(x-34)*px(x+1);
end    

Ehx = (100000/1.03^35) * (((1-Fx(35)) - SUM)  / (1-1/1.03))
%i)
SUM2 =0;
for x = 0:34
    SUM2 = SUM2 + (1/1.03)^(x+1)*px(x+1);
end   
Egx = (1- SUM2 - (1/1.03)^35*(1-Fx(35)))/(1/1.03)


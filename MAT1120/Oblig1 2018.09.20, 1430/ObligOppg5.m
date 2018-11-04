%oppg5 d

p = [0.15, 0.5, 0.35]


Walk(p)

function x = Walk(p)
    %1. sjekker at minVal=1 < pj < 1=maxVal og beregner qj = 1-pj for j =
    %2,3,4.
    %2. Setter opp matrisen A og vektoren b.
    %3. Løser systemet A*y = b og returnerer vektoren y = (x2, x3, x4)
    
    
    %.1
    minValP = 0;%max verdi tillat for p
    maxValP = 1;%min verdi tillat for p
    j = 0; %counter
    q = []; %init q
    for pj = p%går gjennom 
        j = j + 1;%counter
        if(pj < minValP)%sjekker om pj er mindre enn min verdi
            sprintf('p%.f = %.5f < %.f = minVal',[j,pj,minValP])
            return %kanselerer funksjonen siden innput ikke er lov
        elseif(pj > maxValP)% sjekker om pj er større enn max verdi
            sprintf('p%.f = %.5f > %.f = maxVal',[j,pj,maxValP])
            return %kanselerer funksjonen siden innput ikke er lov
        else
            q(j+1) = 1-pj; %hvis pj er innenfor max og min så legges til qj = 1-pj til vektoren q
            
        end    
    end
    
    %2.
    q
    A = [1,-q(2),0;-p(3-1),1,-q(3);,0,-p(4-1),1];%konstruerer matrisen A
    b = [p(2-1);0;0]; %konstruerer matrisen B fra oppg 5b)
    %3.
    y = A\b;%løse A*y = b for yx
    x = y;%setter y til return verdien
    
end

% ObligOppg5
% 
% p =
% 
%     0.1500    0.5000    0.3500
% 
% 
% q =
% 
%          0    0.8500    0.5000    0.6500
% 
% 
% ans =
% 
%     0.3094
%     0.1875
%     0.0656






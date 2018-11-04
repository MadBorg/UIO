% Regner ut et grid og en strømfunksjon
function[X, Y, psi] = streamfun(n)

% Setter standardverdi for n til 20 dersom den ikke er oppgitt
if nargin < 1; 
  n=20;
end

% Lag en vektor med n elementer fra -pi/2 til pi/2
x = linspace(-0.5*pi, 0.5*pi, n);
% Lag et kvadratisk grid med n elementer i begge retninger
[X, Y] = meshgrid(x, x);
% Regn ut strømfunksjonen i hvert gridpunkt
psi = cos(X).*cos(Y);
end








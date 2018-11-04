P = [1,0.7,0,0,0
    0,0,0.5,0,0
    0,0.3,0,0.6,0
    0,0,0.5,0,0
    0,0,0,0.4,1]

%oppg1

k = [2,3,4,50,100];%inndata
M = cell(length(k),1);%tom cell for å lagre matrisene
x0 = [0;0;0;1;0]%x0 matrise

for i = k
    sprintf('P^%.0f *x0 = ', i)
    Pi = P^i*x0;%renger ut sannsynligheten for å komme fra x0
    disp(Pi)
    M{i} = Pi;%lagrer sannsynlighetene
end


for i = k
    sprintf('P(S_4 -> S_2)= %.10f, when k = %.f', M{i}(2), i)%printer S_4 -> S_2 verdier for alle k
end
%2
%mellomregninger for oppg 2
n = length(P);
I5 = eye(5);
null5 = zeros(n, 1);
PI = P - I5
rrPI = rref(PI-null5)


% Oblig1
% 
% P =
% 
%     1.0000    0.7000         0         0         0
%          0         0    0.5000         0         0
%          0    0.3000         0    0.6000         0
%          0         0    0.5000         0         0
%          0         0         0    0.4000    1.0000
% 
% 
% x0 =
% 
%      0
%      0
%      0
%      1
%      0
% 
% 
% ans =
% 
%     'P^2 *x0 = '
% 
%          0
%     0.3000
%          0
%     0.3000
%     0.4000
% 
% 
% ans =
% 
%     'P^3 *x0 = '
% 
%     0.2100
%          0
%     0.2700
%          0
%     0.5200
% 
% 
% ans =
% 
%     'P^4 *x0 = '
% 
%     0.2100
%     0.1350
%          0
%     0.1350
%     0.5200
% 
% 
% ans =
% 
%     'P^50 *x0 = '
% 
%     0.3818
%     0.0000
%          0
%     0.0000
%     0.6182
% 
% 
% ans =
% 
%     'P^100 *x0 = '
% 
%     0.3818
%     0.0000
%          0
%     0.0000
%     0.6182
% 
% 
% ans =
% 
%     'P(S_4 -> S_2)= 0.3000000000, when k = 2'
% 
% 
% ans =
% 
%     'P(S_4 -> S_2)= 0.0000000000, when k = 3'
% 
% 
% ans =
% 
%     'P(S_4 -> S_2)= 0.1350000000, when k = 4'
% 
% 
% ans =
% 
%     'P(S_4 -> S_2)= 0.0000000014, when k = 50'
% 
% 
% ans =
% 
%     'P(S_4 -> S_2)= 0.0000000000, when k = 100'
% 
% 
% PI =
% 
%          0    0.7000         0         0         0
%          0   -1.0000    0.5000         0         0
%          0    0.3000   -1.0000    0.6000         0
%          0         0    0.5000   -1.0000         0
%          0         0         0    0.4000         0
% 
% 
% rrPI =
% 
%      0     1     0     0     0
%      0     0     1     0     0
%      0     0     0     1     0
%      0     0     0     0     0
%      0     0     0     0     0  
% 

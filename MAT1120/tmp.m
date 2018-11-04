p2 = [1 -1 4 -4]
n = length(p2)
a = zeros(n,n)

for i = 1:n
    a(end,i) = p2(n-(i-1))
    if i > 1
      a(i-1,i)= 1  
    end
end

a

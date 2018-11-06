path="https://www.uio.no/studier/emner/matnat/math/STK1110/data/plastic.txt"
plast=read.table(path,header=T)

Strength = plast[1]
Temperature = plast[2]
Pressure = plast[3]
qqnorm(Strength)

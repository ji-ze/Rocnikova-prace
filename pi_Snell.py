import math
from decimal import *
getcontext().prec = 24

r=1
S=2*r
s=Decimal((2*r)/2**0.5)
ss=(Decimal(s**2)/(Decimal(2)+Decimal(4-s**2)**Decimal(0.5)))**Decimal(0.5)
k=4

out_file=open("Snell.csv", "w")
p=(s*k)/(2*r)
out_file.write("n, p, P\n")
for n in range(64):
  q=Decimal((S*k)/(2*r))
  P=Decimal((ss*k*2)/(2*r))
  out_file.write("{}, {}, {}\n".format(n+1, abs(Decimal(4*P/3)-Decimal(p/3)-Decimal(math.pi)), abs(Decimal(2*p/3) + Decimal(q/3)-Decimal(math.pi))))
  p=P
  S=Decimal(2*S)/(Decimal(2)+Decimal(4+S**2)**Decimal(0.5))
  s=(Decimal(s**2)/(Decimal(2)+Decimal(4-s**2)**Decimal(0.5)))**Decimal(0.5)
  ss=(Decimal(ss**2)/(Decimal(2)+Decimal(4-ss**2)**Decimal(0.5)))**Decimal(0.5)  
  k*=2

out_file.close()

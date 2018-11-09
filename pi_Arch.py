import math
from decimal import *
getcontext().prec = 24

r=1
S=2*r
s=Decimal((2*r)/2**0.5)
k=4
n=1

out_file=open("Arch.csv", "w")
out_file.write("n, p, P\n")
for i in range(64):
  out_file.write("{}, {}, {}\n".format(n, abs(Decimal(math.pi)-Decimal(s*k)/(2*r)), abs(Decimal(math.pi)-Decimal(S*k)/(2*r))))
  S=Decimal(2*S)/(Decimal(2)+Decimal(4+S**2)**Decimal(0.5))
  s=(Decimal(s**2)/(Decimal(2)+Decimal(4-s**2)**Decimal(0.5)))**Decimal(0.5)
  k*=2
  n+=1

out_file.close()
print((Decimal(1/7)/7)-Decimal(1/7**2))

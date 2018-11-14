import math
from decimal import *
getcontext().prec = 24

r=1/4
R=Decimal((2**0.5)/4)

out_file=open("Kus.csv", "w")
out_file.write("n, p, P\n")
for n in range(64):
  out_file.write("{}, {}, {}\n".format(n+1, abs(Decimal(1/R)-Decimal(math.pi)), abs(Decimal(1/r)-Decimal(math.pi))))
  r=(Decimal(R)+Decimal(r))/2
  R=Decimal(R*r).sqrt()

out_file.close()

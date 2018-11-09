import math
from decimal import *
getcontext().prec = 50

sin=1/2**0.5
k=8

out_file=open("Ptol.csv", "w")
out_file.write("n, p\n")
for n in range(64):
  out_file.write("{}, {}\n".format(n+1, abs(Decimal(k*sin/2)-Decimal(math.pi))))
  sin=(Decimal(0.5)*(Decimal(1)-Decimal(1-sin**2)**Decimal(0.5)))**Decimal(0.5)
  k*=2

out_file.close()

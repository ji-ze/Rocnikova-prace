import math
from decimal import *
getcontext().prec = 24

a=1
b=Decimal(1/2**0.5)
s=1/4

out_file=open("Leg.csv", "w")
out_file.write("n, p, P\n")
for n in range(64):
  aa=(Decimal(a)+Decimal(b))/2
  b=Decimal(a*b).sqrt()
  c=Decimal(a)-Decimal(aa)
  out_file.write("{}, {}, {}\n".format(n, abs(Decimal(aa**2)/Decimal(s)-Decimal(math.pi)), abs(Decimal(a**2)/Decimal(s)-Decimal(math.pi))))
  a=Decimal(aa)
  s=Decimal(s)-Decimal((2**n)*c**2)
  
out_file.close()

import math
from decimal import *
getcontext().prec = 24

r=1
O=Decimal(4*r**2) # plocha opsaneho
o=Decimal(2*r**2) # plocha vepsaneho

out_file=open("Greg.csv", "w")
out_file.write("n, p, P\n")
for n in range(64):
  out_file.write("{}, {}, {}\n".format(n+1, abs(Decimal(o/r**2)-Decimal(math.pi)), abs(Decimal(O/r**2)-Decimal(math.pi))))
  oo=Decimal((o*O)).sqrt()
  O=Decimal(2*o*O)/(Decimal(o)+Decimal(oo))
  o=oo

out_file.close()

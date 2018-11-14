import math
from decimal import *
getcontext().prec = 24

r=1/4
R=(Decimal(2).sqrt())/4

out_file=open("Desc.csv", "w")
out_file.write("n, p, P\n")
for n in range(64):
  out_file.write("{}, {}, {}\n".format(n+1, abs(Decimal(math.pi)-Decimal(1/R)), abs(Decimal(math.pi)-Decimal(1/r))))
  G=(Decimal(R)+Decimal(r))/2
  R=Decimal((R*(Decimal(r)+Decimal(R)))/2).sqrt()
  r=G
  
out_file.close()

import math
from decimal import *
getcontext().prec = 24
def fac(n):
   if n == 0:
       return 1
   else:
       return n*fac(n-1)

x=0

out_file=open("New.csv", "w")
out_file.write("n, p\n")
for i in range(64):
  x+=Decimal(fac(2*i)/(2**(4*i+1)*fac(i)**2*(2*i+1)))
  out_file.write("{}, {}\n".format(i+1, abs(Decimal(6*x)-Decimal(math.pi))))

out_file.close()

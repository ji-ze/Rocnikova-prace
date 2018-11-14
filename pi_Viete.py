import math
from decimal import *
getcontext().prec = 24

out_file=open("Viete.csv", "w")
out_file.write("n, p\n")
pi=Decimal(2)
for i in range(1,64):
    x=Decimal(0)
    out_file.write("{}, {}\n".format(i, abs(Decimal(pi)-Decimal(math.pi))))
    for j in range(i):
        x=(2+Decimal(x))**Decimal(0.5)
    pi=Decimal(pi*2/x)

out_file.close()

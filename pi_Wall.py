import math

x=1
i=1
x*=4*i**2/(4*i**2-1)
pp=abs(2*x-math.pi)
mem=0

print("n, mem")
for i in range(2,1000000+2):
    p=pp
    x*=4*i**2/(4*i**2-1)
    pp=abs(2*x-math.pi)
    mem+=(p-pp)/8
    
print("{}, {}".format(i-1, mem))

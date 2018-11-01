import math

a=1
b=1/2**0.5
s=1/4

print("n, p, P")
for n in range(10):
  aa=(a+b)/2
  b=(a*b)**0.5
  c=a-aa
  print("{}, {}, {}".format(n, abs(aa**2/s-math.pi), abs(a**2/s-math.pi)))
  a=aa
  s=s-(2**n)*c**2
  

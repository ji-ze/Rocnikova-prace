import math

r=1/4
R=(2**0.5)/4
n=4
print("n, p, P")
for i in range(26):
  print("{}, {}, {}".format(n, abs(1/R-math.pi), abs(1/r-math.pi)))
  r=(R+r)/2
  R=(R*r)**0.5
  n*=2

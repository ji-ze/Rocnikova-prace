import math

sin=1/2**0.5
n=8

print("alpha ve stup, p")
for i in range(26):
  print("{}, {}".format(round(360/n, 6), abs(n*sin/2-math.pi)))
  sin=(0.5*(1-(1-sin**2)**0.5))**0.5
  n*=2

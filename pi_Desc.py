import math

r=1/4
R=(2**0.5)/4
n=4

print("n, e, E")
for i in range(26):
  print("{}, {}, {};".format(n, abs(math.pi-1/R), abs(math.pi-1/r)))
  rr=(R+r)/2
  R=((R*(r+R))/2)**0.5
  r=rr
  n*=2

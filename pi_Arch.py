import math

r=1
S=2*r
s=(2*r)/2**0.5
k=4

print("n, e, E")
for i in range(26):
  print("{}, {}, {};".format(k, abs(math.pi-(s*k)/(2*r)), abs(math.pi-(S*k)/(2*r))))
  S=2*S/(2+(4+S**2)**0.5)
  s=(s**2/(2+(4-s**2)**0.5))**0.5
  k*=2

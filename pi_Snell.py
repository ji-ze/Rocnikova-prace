import math

r=1
S=2*r
s=(2*r)/2**0.5
ss=(s**2/(2+(4-s**2)**0.5))**0.5
k=4

p=(s*k)/(2*r)
print("n, p, P")
for i in range(20):
  q=(S*k)/(2*r)
  P=(ss*k*2)/(2*r)
  print("{}, {}, {}".format(k, abs(4*P/3-p/3-math.pi), 2*p/3 + q/3-math.pi))
  p=P
  S=2*S/(2+(4+S**2)**0.5)
  s=(s**2/(2+(4-s**2)**0.5))**0.5
  ss=(ss**2/(2+(4-ss**2)**0.5))**0.5
  k*=2

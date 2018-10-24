r=1
S=2*r
s=(2*r)/2**0.5
k=4

print("n, e, E")
for i in range(26):
  SS=2*S/(2+(4+S**2)**0.5)
  ss=(s**2/(2+(4-s**2)**0.5))**0.5
  k*=2
  print("{}, {}, {}".format(i+2, abs((s*(k/2))/(2*r)-(ss*k)/(2*r)), abs((S*(k/2))/(2*r)-(SS*k)/(2*r))))
  s=ss
  S=SS

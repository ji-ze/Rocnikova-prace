import math

r=1

O=8*r
S=4*r**2
n=4

print("Opsany n-uhelnik")
print("n, p, P")
for i in range(26):
  print("{}uhelnik: {} < pi < {}".format(n, abs(S/2-math.pi), abs(O/(2*r)-math.pi)))  #proc S/2, spravně S/r**2
  SS=(S*O)**0.5
  O=(2*S*O)/(S+SS)
  S=SS
  n*=2

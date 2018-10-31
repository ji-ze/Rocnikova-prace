r=1

O=8*r
S=4*r**2
n=4

print("Opsany n-uhelnik")
for i in range(26):
  print("{}uhelnik: {} < pi < {}".format(n, S/2, O/(2*r)))  #proc S/2, spravně S/r**2
  SS=(S*O)**0.5
  O=(2*S*O)/(S+SS)
  S=SS
  n*=2

o=4*(2**0.5)*r
s=2*r**2
k=4

print("Vepsany n-uhelnik")
for i in range(26):
  print("{}uhelnik: {} < pi < {}".format(k, s/2, o/(2*r)))  #nefunguje
  ss=(s*o)**0.5
  o=(2*s*o)/(S+SS)
  s=ss
  k*=2

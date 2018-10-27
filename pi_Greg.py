o=2
V=1/4
n=4

for i in range(26):
  print("{}uhelnik: {} < pi < {}".format(n, V, o))
  VV=(V*o)**0.5
  o=(2*V*o)/(V+VV)
  V=VV
  n*=2

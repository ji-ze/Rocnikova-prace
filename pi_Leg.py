a=1
b=1/2**0.5
s=1/4

for n in range(10):
  aa=(a+b)/2
  b=(a*b)**0.5
  c=a-aa
  print("{}: {} < pi < {}".format(n, aa**2/s, a**2/s))
  a=aa
  s=s-(2**n)*c**2

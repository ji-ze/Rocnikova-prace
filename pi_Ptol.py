sin=1/2**0.5
n=8

print("alpha ve stup, pi")
for i in range(26):
  print("{}, {}".format(round(360/n, 6), n*sin/2))
  sin=(0.5*(1-(1-sin**2)**0.5))**0.5
  n*=2

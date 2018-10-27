x=0

print("n, pi")
for i in range(50):
  x=x+(((-1)**i)/(2.0*i+1))
  print("{}, {}".format(i+1, x*4))

import math

x=0

print("n, pi")
for i in range(50):
  x=x+(((-1)**i)/(2.0*i+1))
  if i%2==1:
    print("{}, {}".format(i+1, abs(x*4-math.pi)))
  else:
    print("{},                      {}".format(i+1, abs(x*4-math.pi)))

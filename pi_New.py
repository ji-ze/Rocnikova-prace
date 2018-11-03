def fac(n):
   if n == 0:
       return 1
   else:
       return n*fac(n-1)

x=0

print("n, pi")
for i in range(25):
  x+=fac(2*i)/(2**(4*i+1)*fac(i)**2*(2*i+1))
  print("{}, {}".format(i+1, 6*x))

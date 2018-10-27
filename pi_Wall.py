print("n, pi")
p=1
for i in range(1,50):
    p*=4*i**2/(4*i**2-1)
    print("{}, {}".format(i, 2*p))


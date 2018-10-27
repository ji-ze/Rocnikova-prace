import math

x=1

print("n, p")
for i in range(1,50):
    x*=4*i**2/(4*i**2-1)
    print("{}, {}".format(i, abs(2*x-math.pi)))


import math

print("n, p")
pi=2
for i in range(1,30):
    x=0
    print("{}, {}".format(i+1, abs(pi-math.pi)))
    for j in range(i):
        x=(2+x)**0.5
    pi=pi*2/(x)

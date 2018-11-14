import math

x=1

out_file=open("Wall.csv", "w")
out_file.write("n, p\n")
for i in range(1,64):
    x*=4*i**2/(4*i**2-1)
    out_file.write("{}, {}\n".format(i, abs(2*x-math.pi)))

out_file.close()

import math

x=0

out_file=open("Leib.csv", "w")
out_file.write("n, p\n")
for i in range(64):
  x=x+(((-1)**i)/(2.0*i+1))
  out_file.write("{}, {}\n".format(i+1, abs(x*4-math.pi)))

out_file.close()

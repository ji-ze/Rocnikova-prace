r=1/4
R=(2**0.5)/4
n=4
for i in range(26):
  print("{}uhelnik: {} < pi < {}".format(n, 1/R, 1/r))
  r=(R+r)/2
  R=(R*r)**0.5
  n*=2

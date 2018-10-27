r=1/4
R=(2**0.5)/4
n=4

for i in range(26):
  print("{}uhelnik: {} < pi < {}".format(n, 1/R, 1/r))
  rr=(R+r)/2
  R=((R*(r+R))/2)**0.5
  r=rr
  n*=2

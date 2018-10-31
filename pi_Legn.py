R=1/4
r=(2**0.5)/4
n=4

for i in range(30):
  print("{}uhelnik: {} < pi < {}".format(n, 1/R, 1/r))
  rr=((r*(r+R))/2)**0.5
  R=(r*R)**0.5
  r=rr
  n*=2

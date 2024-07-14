n=int(input())
x=""
while n>0:
  digit=n%10
  y=str(digit)
  x+=y
  n//=10
print(x)

def fact(x):
  if x>0:
    res=1
    for i in range(1,x+1):
      res=res*x
      x=x-1
  return res
def perm_com(n,r):
  perm=int(fact(n)/fact(n-r))
  com=int(fact(n)/(fact(n-r)*fact(r)))
  return perm,com
x=int(input())
y=int(input())
print(perm_com(x,y))

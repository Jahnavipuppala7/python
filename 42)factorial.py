def fact(n):
  f=1
  while n>0:
    f=f*n
    n=n-1
  return f
n=int(input())
print(fact(n))

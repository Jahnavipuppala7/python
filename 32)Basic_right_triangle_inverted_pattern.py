n=int(input())
num=2*n+2
for i in range(1,n+1):
  for j in range(n+1,i,-1):
    print(num,end=" ")
    num=num-1
  print()

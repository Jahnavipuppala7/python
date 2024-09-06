n=int(input())
count=0
for i in range(1,n+1):
  if n%i==0:
    count=count+1
if count>2 or count<2:
  print("not a prime")
else:
  print("prime")

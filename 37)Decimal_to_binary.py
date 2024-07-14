n=int(input())
bin=[]
while n>0:
  rem=n%2
  n=n//2
  bin.append(rem)
bin.reverse()
print(bin)

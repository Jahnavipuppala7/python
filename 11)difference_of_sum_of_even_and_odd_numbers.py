num=int(input())
even,odd=0,0
for i in range(1,num+1):
  n=int(input())
  if n%2==0:
    even=even+n
  else:
    odd=odd+n
print("The sum of even numbers is:",even)
print("The sum of odd numbers is:",odd)
print("The difference is:",abs(even-odd))

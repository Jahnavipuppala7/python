#A positive integer that is equal to the sum of its proper divisors..ex:6--1,2,3
def perfect_num(n):
  rem=0
  for i in range(1,n):
    if n%i==0:
      rem=rem+i
  if rem==n:
      print("perfect number")
  else:
      print("not a perfect number")
x=int(input())
print(perfect_num(x))

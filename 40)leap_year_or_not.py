num=int(input())
if (num%400==0) or (num%4==0 and num%100!=0):
  print("leap year")
else:
  print("Not a leap year")

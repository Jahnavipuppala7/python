num=int(input())
sum=0
n=num
while n>0:
    rem=n%10
    sum=sum+rem**3
    n=n//10
if num==sum:
    print("yes")
else:
    print("no")

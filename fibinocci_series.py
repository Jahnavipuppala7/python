n1,n2=0,1
n=int(input())
print(n1,n2,end=" ")
for i in range(1,n+1):
    x=n1+n2
    n1=n2
    n2=x
    print(x,end=" ")

def factor(n,k):
    lst=[]
    for i in range(1,n+1):
        if n%i==0:
            lst.append(i)
    if len(lst)>=k:
        return lst[k]
    else:
        return 1
n=int(input())
k=int(input())
print(factor(n,k))

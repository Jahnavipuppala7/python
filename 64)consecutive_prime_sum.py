def prime_lst(n):
    primes=[]
    for i in range(n):
        cnt=0
        for j in range(1,i+1):
            if i%j==0:
                cnt+=1
        if cnt==2:
            primes.append(i)
    return primes
n=int(input())
a=prime_lst(n)
sumy=2
cnt=0
for i in range(1,len(a)):
    sumy+=a[i]
    if sumy in a:
        cnt+=1
print(cnt)

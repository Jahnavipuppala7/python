def prime_lst(D):
    lst=[]
    for i in range(D):
        cnt=0
        for j in range(1,i+1):
            if i%j==0:
                cnt+=1
        if cnt==2:
            lst.append(i)
    return lst
D=int(input())
p=int(input())
d_cnt=0
if D%p==0:
    x=D//p
    primes=prime_lst(D)
    for prime in primes:
        cnt=1
        a=prime
        for i in range(p):
            a+=x
            if a not in primes:
                break
            else:
                cnt+=1
        if cnt==p:
            d_cnt+=1
print(d_cnt)

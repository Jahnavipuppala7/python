def string(p,s):
    a=''
    for i in range(len(p)):
        if p[i] in s:
            a+=p[i]
    return a
t=int(input())
ans=[]
for i in range(t):
    p=input()
    s=input()
    ans.append(string(p,s))
for i in ans:
    print(i)

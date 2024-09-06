n=int(input())
lst=[]
for i in range(n):
    lst.append(int(input()))
big=lst[0]
for i in range(n-1):
    if big<lst[i+1]:
        big=lst[i+1]
print(big)

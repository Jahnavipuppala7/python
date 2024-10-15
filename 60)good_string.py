string=input()
name=input()
sumy=0
prev=ord(string[0])
sorted_string=sorted(string)
for i in name:
    if i not in string:
        d1=abs(ord(i)-prev)
        lst=[]
        lst=[abs(ord(j)-ord(i)) for j in string]
        d2=min(lst)
        if lst.count(d2)>=2:
            ind=lst.index(d2)
            d2=abs(ord(string[ind])-prev)
            sumy+=d2
        elif d1<d2:
            sumy+=d1
        else:
            ind=lst.index(d2)
            prev=ord(sorted_string[ind])
            sumy+=d2
print(sumy)

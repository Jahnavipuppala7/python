'''In lambda we use 3 operations to keep the code simple
they are  map,filter and reduce'''
list1=[3,7,4,5,62,1]
lis1=list(filter(lambda x:x%2!=0,list1))
print(lis1)
lis2=list(map(lambda x:x*2,list1))
print(lis2)

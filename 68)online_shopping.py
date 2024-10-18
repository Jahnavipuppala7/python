n=int(input())
token=[int(i) for i in input().split(" ")]
claim=[int(i) for i  in input().split(" ")]
k=int(input()) #bumper offer consecutive claim days
item_input=input().strip()
items={}
for item in item_input.split():
    name,cost=item.split(':')
    items[name]=int(cost)
claimed_token=0
for i in range(n):
    claimed_token+=(token[i]*claim[i])
max_token=0
for i in range(n-k+1):
    current_token=claimed_token
    for j in range(i,i+k):
        if claim[j]==0:
            current_token+=token[j]
    max_token=max(current_token,max_token)
affordable_items=[]
min_wastage=float('inf')
for name,cost in items.items():
    if cost<=max_token:
        wastage=max_token-cost
        if wastage<min_wastage:
            min_wastage=wastage
            affordable_items=[name]
        elif wastage==min_wastage:
            affordable_items.append(name)
affordable_items.sort()
print(" ".join(affordable_items))

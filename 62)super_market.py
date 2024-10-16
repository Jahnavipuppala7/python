n,m=map(int,input().split(" "))
quant=[]
price=[]
for i in range(n+m):
    q,p=map(int,input().split(" "))
    quant.append(q)
    price.append(p)
customer_quant=quant[:n]
customer_price=price[:n]
bag_quant=quant[n:]
bag_price=price[n:]
cnt=0
cust_details=dict(zip(customer_quant,customer_price))
prod_details=dict(zip(bag_quant,bag_price))
for i in range(n):
    a=customer_quant[i]
    bag_quant.sort()
    for j in range(m):
        if bag_quant[j]>a:
            d=bag_quant[j]
            e=prod_details[d]
            if customer_price[i]>e or customer_price==e:
                cnt+=1
                break
print(cnt)

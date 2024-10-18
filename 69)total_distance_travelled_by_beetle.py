def calculate_dis1(point1,point2):
    x1,y1,z1=point1
    x2,y2,z2=point2
    res=abs(x1-x2)+abs(y1-y2)+abs(z1-z2)
    return res
def calculate_dis2(point1,point2):
    pi=3.14
    x1,y1,z1=point1
    x2,y2,z2=point2
    a=0
    if x1!=x2:
        a=max(x1,x2)
        return (a*pi)/6
    if y1!=y2:
        a=max(y1,y2)
        return (a*pi)/6
    else:
        a=max(z1,z2)
        return (a*pi)/6
n=int(input())
points_input=input()
points=[int(i) for i in points_input.split(" ")]
total_dis=0.0
for i in range(0,n-1):
    point1=points[i*3:i*3+3]
    point2=points[i*3+3:i*3+6]
    cnt=0
    for i in range(3):
        if point1[i]==point2[i]:
            cnt+=1
    if cnt==2:
        total_dis+=calculate_dis2(point1,point2)
    else:
        total_dis+=calculate_dis1(point1,point2)
dis=round(total_dis,2)
print(dis)

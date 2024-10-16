def lcm(a,b):
    if a<b:
        d=b
        while True:
            if b%a==0:
                return b
            else:
                b+=d
    else:
        if a>b:
            d=a
            while True:
                if a%b==0:
                    return a
                else:
                    a+=d
def gcd(nums):
    nums.sort()
    for i in range(len(nums)-1):
        nums[i+1]=lcm(nums[i],nums[i+1])
    return nums[-1]
n=int(input())
nums=[int(i) for i in input().split(" ")]
mini=min(nums)
nums.remove(mini)
res=gcd(nums)+mini
cnt=0
for i in range(1,res+1):
    if res%i==0:
        cnt+=1
if cnt>2:
    print('None')
else:
    print(res)

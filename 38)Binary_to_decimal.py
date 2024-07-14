x=input()
num=0
x=x[::-1]
for i in range(len(x)):
  digit=int(x[i])
  pow=2**i
  res=digit*pow
  num=num+res
print(num)

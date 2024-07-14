n=input()
count=0
for i in range(len(n)):
  if (n[i]=='a' or n[i]=='e' or n[i]=='i' or n[i]=='u' or n[i]=='o' or n[i]=='A' or n[i]=='E' or n[i]=='I' or n[i]=='O' or n[i]=='U'):
    count=count+1
print(count)

n=int(input())
a=[]
for i in range(3):
    a.append(list(input().strip()))
i=0
while i<n:
    if a[0][i]=='#':
        print("#",end="")
        i+=1
        continue
    if i+2<n:
        if a[0][i]=='*' and a[0][i+1]=='*' and a[0][i+2]=='*':
            if a[1][i]=='*' and a[1][i+1]=='*' and a[1][i+2]=='*':
                if a[2][i]=='*' and a[2][i+1]=='*' and a[2][i+2]=='*':
                    print('E',end="")
                    i+=3
                    continue
            elif a[1][i]=='.' and a[1][i+1]=='*' and a[1][i+2]=='.':
                if a[2][i]=='*' and a[2][i+1]=='*' and a[2][i+2]=='*':
                    print('I',end="")
                    i+=3
                    continue
            elif a[1][i]=='*' and a[1][i+1]=='.' and a[1][i+2]=='*': 
                if a[2][i]=='*' and a[2][i+1]=='*' and a[2][i+2]=='*':
                    print('O',end="")
                    i+=3
                    continue
        if a[0][i]=='.' and a[0][i+1]=='*'and a[0][i+2]=='.':
            if a[1][i]=='*' and a[1][i+1]=='*' and a[1][i+2]=='*':
                if a[2][i]=='*' and a[2][i+1]=='.' and a[2][i+2]=='*':
                    print('A',end="")
                    i+=3
                    continue
        if a[0][i]=='*' and a[0][i+1]=='.'and a[0][i+2]=='*':
            if a[1][i]=='*'and a[1][i+1]=='.'and a[1][i+2]=='*':
                if a[2][i]=='*'and a[2][i+1]=='*' and a[2][i+2]=='*':
                    print('U',end="")
                    i+=3
                    continue
    i+=1

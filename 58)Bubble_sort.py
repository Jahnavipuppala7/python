def Bubble(arr,l):
    for i in range(l-1,1,-1):
        for j in range(l-1):
            if arr[j]>arr[j+1]:
               arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr=[2,4,1,6,3]
l=len(arr)
print(Bubble(arr,l))

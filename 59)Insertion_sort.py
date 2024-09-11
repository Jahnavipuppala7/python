def Insertion(arr,l):
    for i  in range(l):
        j=i
        while j>0 and arr[j-1]>arr[j]:
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j=j-1
    return arr
arr=[2,4,1,6,3]
l=len(arr)
print(Insertion(arr,l))

def selection_sort(arr,l):
    for i in range(l):
        mini=i
        for j in range(i+1,l):
            if arr[j]<arr[mini]:
                mini=j
        arr[i],arr[mini]=arr[mini],arr[i]
    return arr
arr=[3,5,1,7,4,2]
l=len(arr)
print(selection_sort(arr,l))

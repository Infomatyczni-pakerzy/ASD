def binarySearch(arr,num):
    l,p = 0,len(arr)-1
    print(l,p)
    while l<=p:
        sr = (l+p)//2
        if num == arr[sr]:
            return sr
        elif num > arr[sr]:
            l = sr+1
        else:
            p = sr-1
    return 'nie ma'

t = [number for number in range(21,37)]
print(t)
print(binarySearch(t,21))

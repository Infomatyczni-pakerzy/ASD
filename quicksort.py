#ascending order, pivot is the last array element
#start and end are the range in the array we want to call partition on
def partition(arr, start, end):
    pivot = arr[end]
    i = start
    for j in range(start, end):
        if arr[j]<=pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i=i+1
    arr[end], arr[i] = arr[i], arr[end]
    #return the current position of the pivot
    return i

def quickSort(arr, start, end):
    if start<end:
        pivotIndex = partition(arr, start, end)
        quickSort(arr, start, pivotIndex-1)
        quickSort(arr, pivotIndex+1, end)

tab = [1,4,7,8,3,2,6,5]
quickSort(tab, 0, len(tab)-1)
print(tab)

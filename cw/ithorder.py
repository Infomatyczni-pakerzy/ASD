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

def select(arr, start, end, i):
    if start == end:
        return arr[start]
    pivot = partition(arr, start, end)
    left = pivot - start + 1
    if i == left:
        return arr[pivot]
    elif i < left:
        return select(arr, start, pivot-1, i)
    else:
        return select(arr, pivot+1, end, i-left)

tab = [1, 4, 6, 7, 3, 5, 6, 3]
print(select(tab, 0, 7, 5))

def bubbleSort(arr):
    for i in range(len(arr)):
        swapped = False
        for j in range(0,len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True
        if swapped == False:
            break

def selectSort(arr):
    for i in range(len(arr)-1):
        smallest = arr[i]
        smallestIndex = i
        for j in range(i+1, len(arr)):
            if arr[j]<smallest:
                smallest = arr[j]
                smallestIndex = j
        if smallestIndex != i:
            arr[i],arr[smallestIndex] = arr[smallestIndex],arr[i]

def insertSort(arr):
    for i in range(1,len(arr)):
        numberToInsert = arr[i]
        j = i-1
        while j>=0 and arr[j]>numberToInsert:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = numberToInsert

t = [5,7,2,4,9,3]
print(t)
insertSort(t)
print(t)

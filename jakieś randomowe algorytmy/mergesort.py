#mergesort, ascending order
def merge(arr, tab1, tab2):
    i = j = k = 0
    while i<len(tab1) and j<len(tab2):
        if tab1[i] < tab2[j]:
            arr[k] = tab1[i]
            i+=1
        else:
            arr[k] = tab2[j]
            j+=1
        k+=1
    if i<len(tab1):
        while i<len(tab1):
            arr[k] = tab1[i]
            i+=1
            k+=1
    if j<len(tab2):
        while j<len(tab2):
            arr[k] = tab2[j]
            j+=1
            k+=1

def mergeSort(arr):
    if len(arr)>1:
        half = len(arr)//2
        L = arr[:half]
        R = arr[half:]

        mergeSort(L)
        mergeSort(R)

        merge(arr,L,R)

list = [1,65,34,87,2,6,98]
mergeSort(list)

print(list)

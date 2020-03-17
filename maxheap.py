#returns indices of specified items
def parent(i):
    return (i-1)//2
def leftChild(i):
    return 2*i+1
def rightChild(i):
    return 2*i+2

#function to heapify the node at i position
def heapify(arr,i):
    left = leftChild(i)
    right = rightChild(i)
    size = len(arr) - 1
    if left <= size and arr[left] > arr[i]:
        largest = left
    else:
        largest = i
    if right <= size and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[largest],arr[i] = arr[i],arr[largest]
        heapify(arr,largest)

def buildHeap(arr):
    for i in reversed(range(len(arr)//2)):#
        #(n+1)/2 is the number of leaves in a complete binary tree
        #therefore len(arr)//2 is the number of leaves to check
        #it doesn't matter that we don't get the exact number of leaves
        #because we have to check the parent node regardless of the number
        #of its leaves (1 or 2)
        heapify(arr,i)

def getMax(arr):
    arr[0],arr[-1] = arr[-1],arr[0]
    max = arr.pop()
    heapify(arr,0)
    return max

#returns a sorted list, does not make changes to the original one
def heapSort(arr):
    arrCopy = arr[:]
    buildHeap(arrCopy)
    sortedArr = []
    size = len(arrCopy)
    for i in range(size):
        sortedArr.insert(0,getMax(arrCopy))
    return sortedArr

k = [2,6,9,2,9,4,6,3]
buildHeap(k)
print(k)
print(heapSort(k))

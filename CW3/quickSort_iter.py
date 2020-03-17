def partition(arr, l, h): 
    i = ( l - 1 ) 
    x = arr[h] 
  
    for j in range(l, h): 
        if   arr[j] <= x: 
  
            # increment index of smaller element 
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i] 
  
    arr[i + 1], arr[h] = arr[h], arr[i + 1] 
    return (i + 1) 

def quickSort_iter(arr, low, high):
    size = high-low+1
    stack = [0]*size
    top = -1
    top+=1
    stack[top] = low
    top+=1
    stack[top] = high
    while top >= 0:
        high = stack[top]
        top-=1
        low = stack[top]
        top-=1
        p = partition(arr,low,high)
        if p-1 > low:
            top+=1
            stack[top]
            top+=1
            stack[top] = p-1
        if p+1 < high:
            top+=1
            stack[top] = p+1
            top+=1
            stack[top] = high

L=[9,4,7,1,5,8,3,5,0,5,2,3,1,5]
quickSort_iter(L, 0, len(L)-1)
print(L)

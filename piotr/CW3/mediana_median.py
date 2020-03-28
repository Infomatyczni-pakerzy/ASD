def median_of_medians(A, i):
    sublists = [A[j:j+5] for j in range(0, len(A), 5)]
    medians = [sorted(sublist)[len(sublists)//2] for sublist in sublists]

    if len(medians) <= 5:
        pivot = sorted(medians)[len(medians)//2]
    else:
        pivot = median_of_medians(medians, len(medians)//2)

    low = [j for j in A if j < pivot]
    high = [j for j in A if j > pivot]

    k = len(low)
    if i < k:
        return median_of_medians(low,i)
    elif i > k:
        return median_of_medians(high, i-k-1)
    else:
        return pivot


A = [ 9, 5 ,12, 7, 346, 12, 7, 4, 1 ,6, 34, 2, 6 , 53, 234, 7, 3 ,4 ,8, 5, 3, 34,7]
print(median_of_medians(A, (len(A) - 1)//2 )

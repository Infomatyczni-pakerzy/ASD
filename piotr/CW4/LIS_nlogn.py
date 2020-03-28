def Binary_search(A, length, x):
    
    l = -1
    r = length - 1
    while r-l > 1:
        med = l + (r - l)//2
        if A[med] >= x:
            r = med
        else:
            l = med
    return r

def LIS(A):
    size = len(A)
    if size == 1:
        return 1
    
    T = [0 for i in range(size+1)]
    length = 0

    T[0] = A[0]
    length = 1

    for i in range(1, size):

        if A[i] < T[0]:     # nowa najmniejsza wartosc  ( na poczatek nowego )
            T[0] = A[i]

        elif A[i] > T[length-1]:    # nowa najwieksza wartosc ( na koniec najdluzszego)
            T[length] = A[i]
            length+= 1

        else:                                           # jezeli nie jest najw ani nie jest najmn
            T[ Binary_search(T, length, A[i]) ] = A[i]  # zastepujemy ciag tej samej dlugosci
    return length



A = [1, 8, 3, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
print(LIS(A))

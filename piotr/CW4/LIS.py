# longest increasing subsequence  O(n^2)
def print_LIS(A, P, i):
    if P[i] >= 0:
        print_LIS(A, P, P[i])
    print(A[i])

def max_ind(F):
    i = 0
    max = 0
    for j in range(len(F)):
        if F[i] > max:
            i = j
    return i

def LIS(A):
    n = len(A)
    F = [1]*n
    P = [-1]*n
    for i in range(1,n):
        for j in range(i):
            if A[j] < A[i] and F[i] < F[j] + 1:
                F[i] = F[j] + 1
                P[i] = j
    return (max(F), F, P)

S = [1, 6, 2, 8, 3, 7, 5, 3 , 8, 9, 6, 7, 2]
print_LIS(S, LIS(S)[2], max_ind(LIS(S)[1]))

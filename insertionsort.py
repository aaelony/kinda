## M-x conda-env-activate ret py311
## M-x run-python
## C-c C-r to evaluate

def insertion_sort(A):
    n = len(A)
    for i in range(0, n):
        temp = A[i]
        j = i - 1
        
        while A[j] > temp and j>=0:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = temp
    return A

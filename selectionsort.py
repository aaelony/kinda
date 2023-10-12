## M-x conda-env-activate ret py311
## M-x run-python
## C-c C-r to evaluate

def selectionsort(A):
    n = len(A)
    for i in range(0, n):
        index_of_min_value = i
        for j in range(i+1, n):
            if A[j] < A[index_of_min_value]:
                index_of_min_value = j
                A[i], A[index_of_min_value] = A[index_of_min_value], A[i]
    return A


import random

A = random.sample(range(-5, 50), 10)

selectionsort(A)

## M-x conda-env-activate ret py311
## M-x run-python
## C-c C-r to evaluate

def mergesort(A):
    n = len(A)
    if n > 1:
        mid = n // 2
        left = A[:mid]
        right = A[mid:]

        mergesort(left)
        mergesort(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                A[k] = left[i]
                i += 1
            else:
                A[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            A[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            A[k] = right[j]
            j += 1
            k += 1
            

import random
A = [ random.randint(-10, 10) for _ in range(10)]
print(A)
mergesort(A)
print(A)


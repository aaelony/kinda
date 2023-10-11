## M-x conda-env-activate ret py311
## M-x run-python
## C-c C-r to evaluate


def partition(A,start,stop):
    piv = start 
    i = start + 1
    for j in range(start + 1, stop + 1):
        if A[j] <= A[piv]:
            A[i] , A[j] = A[j] , A[i]
            i += 1
    A[piv] , A[i - 1] = A[i - 1] , A[piv]
    piv = i - 1
    return (piv)

def rand_partition(A , start, stop):
    randpiv = random.randrange(start, stop)
    A[start], A[randpiv] = A[randpiv], A[start]
    return partition(A, start, stop)


def _quicksort(A, start , stop):
    if(start < stop):         
        pivindex = rand_partition(A, start, stop)
        _quicksort(A , start, pivindex-1)
        _quicksort(A, pivindex + 1, stop)
    return A


def quicksort(A):
    A =  _quicksort(A, 0, len(A) -1 )
    print(A)
    return A



A = [10, 7, 8, 9, 1, 5, 20, -4, -10, 30]
quicksort(A)
print(A)


 


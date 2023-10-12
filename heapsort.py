## M-x conda-env-activate ret py311
## M-x run-python
## C-c C-r to evaluate

def heapify(A, n, i):
    largest     = i  # Initialize largest as root (maxheap)
    left_child  = 2*i + 1  
    right_child = (2*i + 1) + 1
 
    if left_child<n and A[i]<A[left_child]: largest = left_child        
    if right_child<n and A[largest]<A[right_child]: largest = right_child
    if largest != i:                              # if root is not the largest, make it so.
        A[i], A[largest] = A[largest], A[i]   # swap
        A = heapify(A, n, largest)                # recurse
    return A

 
def heapsort(A):
    n = len(A)
    print(f"Original Array: {A}")
 
    # Build a maxheap.
    # Since last parent will be at ((n//2)-1) we can start at that location.
    start = n // 2 - 1   ## Parents are accessed by n//2 - 1 (opposite of child access by 2i+1)
    to    = -1
    by    = -1  ## reverse range from right to left.
    print(f"calling range( n//2 - 1 = {start}, to = {to}, by = {by}")
    ## each i is a tree root of a subtree
    for i in range(start, to, by):   
        print(f"range i:{i}")
        A = heapify(A, n, i)
 
    for i in range(n-1, 0, -1):      # Reverse loop ending to zero.
        A[i], A[0] = A[0], A[i]  # swap
        A = heapify(A, i, 0)
    
    print(f"Sorted Array: {A}")
    return A
 
 
# Driver code to test above
 
A = [12, 11, 13, 5, 6, 7, ]
print(f"Before: {A}")

heapsort(A)
print(f"After: {A}")

B = [9, 8, 7, 6, 7, 2, 6, 5, 1]
heapsort(B)
    

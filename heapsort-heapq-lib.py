## M-x conda-env-activate ret py311
## M-x run-python
## C-c C-r to evaluate
        
    
import heapq

A = [ 9, 8, 7, 6, 7, 2, 6, 5, 1]    

heapq.heapify(A)
heapq.nlargest(5, A)
heapq.nsmallest(3, A)
heapq.heappush(A, 12)
heapq.heappush(A, 4)

heapq.heappop(A) ## pop the smallest item off the heap

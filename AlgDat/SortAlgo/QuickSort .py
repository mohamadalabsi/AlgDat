def partition(A, low, high):
    i = low
    j = high
    pivot = A[low]
    while i < j:
        while i < high and A[i] <= pivot:
            i += 1
        while j > low and A[j] > pivot:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
    
    A[low], A[j] = A[j], A[low]
    return j

def QuickSort(A, low, high):
    if low < high:
        j = partition(A, low, high)
        QuickSort(A, low, j - 1)
        QuickSort(A, j + 1, high)
    return A    

A = [10, 9, 4, 6, 2, 65, 21, 2, 5]    
low = 0
high = len(A) - 1
result=QuickSort(A, low, high)
print(result)  

  
    
    
    
     
      
        
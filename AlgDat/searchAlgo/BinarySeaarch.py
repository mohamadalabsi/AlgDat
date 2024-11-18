def BinarySearch(A  , low , high , target ):
  if low > high :
    return False 
  else :
    mid= int((low + high) /2 )
  if A[mid]== target : 
      return True
  elif  target> A[mid]: 
      return  BinarySearch(A  , mid+1 , high , target )
  elif target< A [mid] :
      return  BinarySearch(A  , low  , mid-1 , target )
    
    
    
    

A =[1,2,4,5,7,9,11]
low = 0 
high= len(A)-1
target = 4
print(BinarySearch(A , low , high , target))

  
  
def MergeSort(A:list , lb ,ub ):
  if lb > ub :
    return A 
  else :
    mid = (lb+ub)/2 
    MergeSort(A , mid+1, ub)
    MergeSort(A , lb , mid )
    Merge(A, lb , ub , mid )
    
    
def Merge(A , lb , ub , mid ):
  i=lb 
  j=mid+1
  k=lb 
  
  while i<= mid and j <= ub :
    if A[i]<= A[j]:
      A[k]=A[i]
      i+=1
    else :
      A[k]= A[j]
      j+=1
  k+=1  
  
  if i > mid :
    while j <= ub :
      A[k]=A[j]
      j+=1
      k+=1
  else :
    while i <= mid :
      A[k]=A[i]
      i+=1
      k+=1  
  k=ub
  B=[]
  for k in range(ub) :
    A[k]=B[k]
    
  return B
    
      
    
    
    
A=[8,5,6,3,12,6,43,0,2]    
lb=0
ub=len(A)-1
result= MergeSort(A, lb , ub )
print(result)

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
def MergeSort(A:list ):
  
  if len(A)>1 :
    mid = int(len(A)/2)
    rightHalf=A[:mid]
    leftHalf=A[mid:]
    # i=0
    # for i in range(mid-1):
    #   rightHalf[i]=A[i]
    # j=mid
    # for j in range(ub):
    #   leftHalf[j]=A[j]  
      
    MergeSort(rightHalf)
    MergeSort(leftHalf)
    return Merge(A , rightHalf, leftHalf)
    
    
def Merge(A, rightHalf, leftHalf):
  i=0 
  j=0
  k=0
  while i< len(rightHalf) and j <len(leftHalf) :
    if rightHalf[i]< leftHalf[j]:
      A[k]=rightHalf[i]
      i+=1
    else :
      A[k]= leftHalf[j]
      j+=1
    k+=1  
  
  # if j > len(rightHalf) :
  while j < len(leftHalf) :
      A[k]=leftHalf[j]
      j+=1
      k+=1
  # else :
  while i < len(rightHalf) :
      A[k]=rightHalf[i]
      i+=1
      k+=1  
  return A
      
    
    
    
A=[8,5,6,3,12,6,43,0]    
print(A)
result=MergeSort(A)
print(result)

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
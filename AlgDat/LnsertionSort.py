def InsertionSort(A:list): 
  j=1
  for j in range(len(A)):
    Key=A[j]
    i=j-1
    while i>=0 and A[i]<Key :
      A[i+1]=A[i]
      i-=1
      A[i+1]=Key
  return A


A=[3,7,4,1,0,8,45]    
result=InsertionSort(A)
print(result)
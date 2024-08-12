def InsertionSortRec(A:list,j): 
  if j>=len(A):
    return A 
  else:
    Key=A[j]
    i=j-1
    while i>=0 and A[i]> Key :
       A[i+1]=A[i]
       A[i]=Key
       i-=1
    return InsertionSortRec(A,j+1)  



j=1
A=[3,7,4,1,0,8,45]    
result=InsertionSortRec(A,j) 
print(result)
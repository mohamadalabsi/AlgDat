def BubbleSort(A , n):
  i=0
  j=0
  for  i in range(n-1):
    flag =0 
    for j in range(n-1-i):
      if A[j]>A[j+1]:
        A[j],A[j+1]=A[j+1],A[j]
        flag+=1
    if flag==0 :
      break
  return A  
    
    
    
    
A=[2,3,5,1,6,44,7]
n=len(A)
print(A)
result=BubbleSort(A,n)        
print(result)
        